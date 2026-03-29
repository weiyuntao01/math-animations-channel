from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd: list[str]) -> None:
    print("[PIPELINE]", " ".join(cmd))
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        raise SystemExit(proc.returncode)



def run_episode(ep: int, do_preview: bool, do_final: bool) -> None:
    ep2 = f"{ep:02d}"
    script = f"information_theory_ep{ep2}.py"
    klass = f"InformationTheoryEP{ep2}"

    if not Path(script).exists():
        raise FileNotFoundError(f"missing script: {script}")

    py = sys.executable

    if do_preview:
        run_cmd([py, "-m", "manim", script, klass, "-ql"])
        run_cmd([py, "it_qa.py", "--ep", str(ep), "--stage", "preview", "--sample-frames", "8"])

    if do_final:
        run_cmd([py, "-m", "manim", script, klass, "-qh", "--fps", "60", "-r", "1920,1080"])
        run_cmd([py, "it_qa.py", "--ep", str(ep), "--stage", "final", "--sample-frames", "12"])

    print(f"[PIPELINE] EP{ep2} completed")



def main() -> int:
    parser = argparse.ArgumentParser(description="信息论单集生产管线")
    parser.add_argument("--ep", type=int, required=True)
    parser.add_argument("--preview", action="store_true", help="run preview stage")
    parser.add_argument("--final", action="store_true", help="run final stage")
    args = parser.parse_args()

    do_preview = args.preview
    do_final = args.final
    if not do_preview and not do_final:
        do_preview = True
        do_final = True

    run_episode(args.ep, do_preview=do_preview, do_final=do_final)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
