from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

import cv2
import numpy as np


EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F5FF"
    "\U0001F600-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\U0001F700-\U0001F77F"
    "\U0001F780-\U0001F7FF"
    "\U0001F800-\U0001F8FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\u2600-\u27BF"
    "]+"
)


@dataclass
class CheckResult:
    ok: bool
    errors: List[str]
    warnings: List[str]
    details: Dict[str, Any]



def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")



def check_static_rules(py_file: Path) -> CheckResult:
    content = _read_text(py_file)
    errors: List[str] = []
    warnings: List[str] = []

    if "import random" not in content:
        errors.append("missing `import random`")

    # 禁灰字: 信息文本不允许灰色
    gray_text_patterns = [
        r"Text\([^\n]*color\s*=\s*IT_GRAY",
        r"Text\([^\n]*color\s*=\s*GRAY",
        r"Text\([^\n]*color\s*=\s*DARK_GRAY",
        r"Text\([^\n]*color\s*=\s*#6B7280",
        r"Text\([^\n]*color\s*=\s*#333333",
    ]
    for p in gray_text_patterns:
        if re.search(p, content):
            errors.append(f"gray text detected by pattern: {p}")

    # 禁emoji
    if EMOJI_RE.search(content):
        errors.append("emoji characters found in script")

    # 底线检查
    if re.search(r"DOWN\s*\*\s*4(\.0+)?", content):
        errors.append("unsafe bottom placement: DOWN * 4")
    if re.search(r"DOWN\s*\*\s*3\.[6-9]", content):
        warnings.append("possible bottom-risk placement below DOWN * 3.5")

    # 右侧绝对堆叠风险 (提示)
    if re.search(r"Text\([^\n]*\)\.move_to\(RIGHT_ZONE\s*\+\s*(UP|DOWN)", content):
        warnings.append("right-zone text uses absolute move_to; prefer arranged flow")

    # 连续解释段时长风险
    run_times = [float(v) for v in re.findall(r"run_time\s*=\s*([0-9]+(?:\.[0-9]+)?)", content)]
    long_runs = [v for v in run_times if v > 12.0]
    if long_runs:
        errors.append(f"run_time > 12 found: {long_runs}")

    waits = [float(v) for v in re.findall(r"self\.wait\(\s*([0-9]+(?:\.[0-9]+)?)\s*\)", content)]
    long_waits = [v for v in waits if v > 4.0]
    if long_waits:
        warnings.append(f"self.wait > 4 found: {long_waits}")

    details = {
        "run_times_count": len(run_times),
        "waits_count": len(waits),
        "long_runs": long_runs,
        "long_waits": long_waits,
    }
    return CheckResult(ok=len(errors) == 0, errors=errors, warnings=warnings, details=details)



def _find_video(ep: int, stage: str) -> Path | None:
    ep2 = f"{ep:02d}"
    quality = "480p15" if stage == "preview" else "1080p60"
    expected_name = f"InformationTheoryEP{ep2}.mp4"

    candidates = [
        Path("..") / "media" / "videos" / f"information_theory_ep{ep2}" / quality / expected_name,
        Path("media") / "videos" / f"information_theory_ep{ep2}" / quality / expected_name,
    ]
    for p in candidates:
        if p.exists():
            return p

    search_roots = [Path("..") / "media" / "videos", Path("media") / "videos"]
    for root in search_roots:
        if not root.exists():
            continue
        for p in root.rglob("*.mp4"):
            if "partial_movie_files" in str(p):
                continue
            if quality not in str(p):
                continue
            if f"information_theory_ep{ep2}" not in str(p):
                continue
            if p.name.lower() == expected_name.lower():
                return p
    return None



def check_duration(video_path: Path, min_s: float = 60.0, max_s: float = 75.0) -> CheckResult:
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS) or 0
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0
    cap.release()

    duration = (frames / fps) if fps else 0.0
    errors: List[str] = []
    warnings: List[str] = []

    if duration < min_s:
        errors.append(f"duration too short: {duration:.2f}s < {min_s:.2f}s")
    if duration > max_s:
        errors.append(f"duration too long: {duration:.2f}s > {max_s:.2f}s")

    details = {
        "duration_sec": round(duration, 2),
        "fps": round(fps, 2),
        "frames": int(frames),
        "resolution": f"{int(w)}x{int(h)}",
    }
    return CheckResult(ok=len(errors) == 0, errors=errors, warnings=warnings, details=details)



def _overlap_ratio(box1: Tuple[float, float, float, float], box2: Tuple[float, float, float, float]) -> float:
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    if x2 <= x1 or y2 <= y1:
        return 0.0
    inter = (x2 - x1) * (y2 - y1)
    a1 = max((box1[2] - box1[0]) * (box1[3] - box1[1]), 1.0)
    a2 = max((box2[2] - box2[0]) * (box2[3] - box2[1]), 1.0)
    return inter / min(a1, a2)



def check_video_ocr_layout(video_path: Path, sample_frames: int = 12, conf_th: float = 0.35) -> CheckResult:
    errors: List[str] = []
    warnings: List[str] = []

    try:
        import easyocr  # type: ignore
    except Exception as exc:  # pragma: no cover
        warnings.append(f"easyocr unavailable: {exc}")
        return CheckResult(ok=True, errors=[], warnings=warnings, details={"skipped": True})

    reader = easyocr.Reader(["ch_sim", "en"], gpu=False)

    cap = cv2.VideoCapture(str(video_path))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if total <= 0:
        cap.release()
        return CheckResult(ok=False, errors=["video has no frames"], warnings=[], details={})

    idxs = np.linspace(0, max(total - 1, 1), sample_frames, dtype=int)
    top_margin = 20
    bottom_margin = 40

    detected_count = 0
    failed_ocr_frames: List[int] = []
    out_of_bounds = []
    overlaps = []

    for idx in idxs:
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))
        ok, frame = cap.read()
        if not ok:
            continue

        # easyocr + OpenCV 在低分辨率帧上偶发崩溃，先放大可显著降低异常概率
        scale = 2.0
        proc_frame = cv2.resize(frame, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        try:
            results = reader.readtext(proc_frame)
        except Exception:
            failed_ocr_frames.append(int(idx))
            continue
        boxes: List[Tuple[float, float, float, float, float, str]] = []

        for r in results:
            pts = np.array(r[0], dtype=float)
            txt = str(r[1])
            conf = float(r[2])
            if conf < conf_th:
                continue
            x1, y1 = float(np.min(pts[:, 0]) / scale), float(np.min(pts[:, 1]) / scale)
            x2, y2 = float(np.max(pts[:, 0]) / scale), float(np.max(pts[:, 1]) / scale)
            boxes.append((x1, y1, x2, y2, conf, txt))

        detected_count += len(boxes)

        for b in boxes:
            if b[1] < top_margin or b[3] > (h - bottom_margin):
                out_of_bounds.append({
                    "frame": int(idx),
                    "box": [round(v, 1) for v in b[:4]],
                    "text": b[5],
                    "conf": round(b[4], 2),
                })

        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                a = boxes[i]
                b = boxes[j]
                ratio = _overlap_ratio(a[:4], b[:4])
                if ratio > 0.25:
                    overlaps.append({
                        "frame": int(idx),
                        "ratio": round(ratio, 2),
                        "text_a": a[5],
                        "text_b": b[5],
                    })

    cap.release()

    if out_of_bounds:
        errors.append(f"OCR out-of-bounds boxes: {len(out_of_bounds)}")
    if overlaps:
        errors.append(f"OCR overlapping boxes: {len(overlaps)}")
    if detected_count == 0:
        warnings.append("OCR detected zero text boxes; review manually")
    if failed_ocr_frames:
        warnings.append(f"OCR failed on frames: {failed_ocr_frames[:10]}")

    details = {
        "sample_frames": int(sample_frames),
        "detected_boxes": int(detected_count),
        "ocr_failed_frames": failed_ocr_frames[:20],
        "out_of_bounds_samples": out_of_bounds[:20],
        "overlap_samples": overlaps[:20],
    }
    return CheckResult(ok=len(errors) == 0, errors=errors, warnings=warnings, details=details)



def check_rhythm_proxy(py_file: Path) -> CheckResult:
    content = _read_text(py_file)
    errors: List[str] = []
    warnings: List[str] = []

    # 钩子代理: 前 6 秒至少有一条问题句
    head = "\n".join(content.splitlines()[:120])
    if not re.search(r"[？?]", head):
        warnings.append("no question mark found near script header; hook may be weak")

    # 预告时长代理: 预告段 run_time 过长预警
    if "下期预告" in content:
        preview_block = content.split("下期预告", 1)[-1]
        rt = [float(v) for v in re.findall(r"run_time\s*=\s*([0-9]+(?:\.[0-9]+)?)", preview_block)]
        if sum(rt) > 8:
            warnings.append(f"preview runtime sum seems long: {sum(rt):.2f}s")

    return CheckResult(ok=len(errors) == 0, errors=errors, warnings=warnings, details={})



def run_qa(ep: int, stage: str, sample_frames: int) -> Dict[str, Any]:
    ep2 = f"{ep:02d}"
    py_file = Path(f"information_theory_ep{ep2}.py")
    if not py_file.exists():
        raise FileNotFoundError(f"missing script: {py_file}")

    static_res = check_static_rules(py_file)
    rhythm_res = check_rhythm_proxy(py_file)

    video = _find_video(ep, stage)
    if video is None:
        raise FileNotFoundError(f"video not found for ep{ep2} stage={stage}")

    dur_res = check_duration(video)
    ocr_res = check_video_ocr_layout(video, sample_frames=sample_frames)

    all_errors = static_res.errors + rhythm_res.errors + dur_res.errors + ocr_res.errors
    all_warnings = static_res.warnings + rhythm_res.warnings + dur_res.warnings + ocr_res.warnings

    report = {
        "ep": ep,
        "stage": stage,
        "script": str(py_file),
        "video": str(video),
        "ok": len(all_errors) == 0,
        "errors": all_errors,
        "warnings": all_warnings,
        "checks": {
            "static": asdict(static_res),
            "rhythm_proxy": asdict(rhythm_res),
            "duration": asdict(dur_res),
            "ocr_layout": asdict(ocr_res),
        },
    }
    return report



def save_report(report: Dict[str, Any]) -> Path:
    ep2 = f"{report['ep']:02d}"
    out_dir = Path("qa_reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"ep{ep2}_report.json"

    if out_path.exists():
        try:
            existing = json.loads(out_path.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
    else:
        existing = {}

    existing[report["stage"]] = report
    out_path.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path



def main() -> int:
    parser = argparse.ArgumentParser(description="信息论单集 QA")
    parser.add_argument("--ep", type=int, required=True, help="episode number, e.g. 13")
    parser.add_argument("--stage", choices=["preview", "final"], required=True)
    parser.add_argument("--sample-frames", type=int, default=10)
    args = parser.parse_args()

    report = run_qa(args.ep, args.stage, sample_frames=args.sample_frames)
    out_path = save_report(report)

    print(f"[QA] EP{args.ep:02d} stage={args.stage} ok={report['ok']}")
    print(f"[QA] report: {out_path}")

    if report["errors"]:
        print("[QA] errors:")
        for err in report["errors"]:
            print(f"  - {err}")
    if report["warnings"]:
        print("[QA] warnings:")
        for w in report["warnings"]:
            print(f"  - {w}")

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
