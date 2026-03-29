from __future__ import annotations

from manim import *
import numpy as np
import random
from typing import Iterable, List, Sequence

# --- 信息论系列公共配色 ---
IT_GREEN = "#00FF41"
IT_RED = "#FF2A68"
IT_BLUE = "#00BFFF"
IT_YELLOW = "#FFD700"
IT_PURPLE = "#8B5CF6"
IT_ORANGE = "#F97316"
IT_WHITE = "#FFFFFF"
IT_BLACK = "#000000"

# --- 统一布局常量 (16:9 默认 Manim 坐标系) ---
LEFT_ZONE = LEFT * 3.5
RIGHT_ZONE = RIGHT * 3.5
SAFE_TOP_Y = 3.6
SAFE_BOTTOM_Y = -3.5


class ITSceneBase(Scene):
    """信息论系列公共基类: 统一布局、节奏和基础校验。"""

    def setup_scene(self, seed: int = 42) -> None:
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = IT_BLACK
        random.seed(seed)
        np.random.seed(seed)

    def make_title_block(
        self,
        ep: int,
        cn_title: str,
        en_title: str,
        color=IT_BLUE,
        title_size: int = 54,
        subtitle_size: int = 28,
    ) -> VGroup:
        title = Text(f"EP{ep:02d}: {cn_title}", font_size=title_size, color=color, weight=BOLD)
        subtitle = Text(en_title, font_size=subtitle_size, color=IT_WHITE)
        subtitle.next_to(title, DOWN, buff=0.3)
        block = VGroup(title, subtitle)
        block.to_edge(UP, buff=0.9)
        return block

    def make_right_panel(
        self,
        items: Sequence[Mobject | str],
        font_size: int = 26,
        buff: float = 0.24,
        top_offset: float = 2.2,
    ) -> VGroup:
        rows: List[Mobject] = []
        for item in items:
            if isinstance(item, str):
                rows.append(Text(item, font_size=font_size, color=IT_WHITE))
            else:
                rows.append(item)
        group = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=buff)
        group.move_to(RIGHT_ZONE + UP * top_offset)
        return group

    def stage_summary(self, text: str, color=IT_YELLOW, font_size: int = 30) -> Text:
        summary = Text(text, font_size=font_size, color=color, weight=BOLD)
        summary.to_edge(DOWN, buff=0.8)
        return summary

    def clear_stage(self, *mobs: Mobject, run_time: float = 0.8) -> None:
        if mobs:
            self.play(*[FadeOut(m) for m in mobs], run_time=run_time)
        else:
            self.play(FadeOut(VGroup(*self.mobjects)), run_time=run_time)

    def assert_in_safe_area(self, mob: Mobject, name: str = "mob") -> None:
        top = mob.get_top()[1]
        bottom = mob.get_bottom()[1]
        if top > SAFE_TOP_Y:
            raise ValueError(f"{name} exceeds safe top: {top:.2f} > {SAFE_TOP_Y:.2f}")
        if bottom < SAFE_BOTTOM_Y:
            raise ValueError(f"{name} exceeds safe bottom: {bottom:.2f} < {SAFE_BOTTOM_Y:.2f}")

    def assert_no_overlap(self, mobs: Sequence[Mobject], name: str = "group") -> None:
        for i in range(len(mobs)):
            for j in range(i + 1, len(mobs)):
                a = mobs[i]
                b = mobs[j]
                if self._overlap(a, b):
                    raise ValueError(f"{name} overlap detected between index {i} and {j}")

    @staticmethod
    def _overlap(a: Mobject, b: Mobject) -> bool:
        ax1, ay1, _ = a.get_left()
        ax2, ay2, _ = a.get_right()
        at = a.get_top()[1]
        ab = a.get_bottom()[1]

        bx1, by1, _ = b.get_left()
        bx2, by2, _ = b.get_right()
        bt = b.get_top()[1]
        bb = b.get_bottom()[1]

        horiz = (ax1 <= bx2) and (ax2 >= bx1)
        vert = (ab <= bt) and (at >= bb)
        return horiz and vert


def formula_text(content: str, size: int = 34, color=IT_YELLOW) -> Text:
    """在不依赖 LaTeX 的环境下，使用 Consolas 显示公式文本。"""
    return Text(content, font_size=size, color=color, font="Consolas")
