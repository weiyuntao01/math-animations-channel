from manim import *
import numpy as np
import random

from it_common import (
    ITSceneBase,
    IT_GREEN,
    IT_RED,
    IT_BLUE,
    IT_YELLOW,
    IT_PURPLE,
    IT_ORANGE,
    IT_WHITE,
    IT_BLACK,
    LEFT_ZONE,
    RIGHT_ZONE,
    formula_text,
)


class InformationTheoryEP19(ITSceneBase):
    """信息论 EP19: 全息宇宙论"""

    def construct(self):
        self.setup_scene(seed=19)
        self.hook_opening()
        self.intuition_demo()
        self.math_core()
        self.meaning_section()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(19, "全息宇宙论", "Holographic Principle", color=IT_BLUE)
        hook = Text("为什么黑洞是三维物体，信息却按面积算？", font_size=38, color=IT_YELLOW, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.45)
        tag = Text("这条反直觉规律，改变了我们对时空的看法", font_size=30, color=IT_GREEN)
        tag.next_to(hook, DOWN, buff=0.45)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(tag, shift=UP), run_time=0.8)
        self.wait(5.0)
        self.clear_stage(title, hook, tag)

    def intuition_demo(self):
        title = Text("直觉冲突：体积直觉 vs 面积定律", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        sphere = Circle(radius=1.2, color=IT_BLUE, stroke_width=4).set_fill(IT_BLUE, 0.12)
        sphere.move_to(LEFT_ZONE + UP * 0.4)
        sphere_label = Text("普通直觉: 信息 ~ 体积", font_size=24, color=IT_WHITE).next_to(sphere, DOWN, buff=0.28)

        bh_outer = Circle(radius=1.35, color=IT_ORANGE, stroke_width=6).set_fill(IT_ORANGE, 0.12)
        bh_inner = Circle(radius=0.9, color=IT_BLACK, stroke_width=0).set_fill(IT_BLACK, 1.0)
        bh = VGroup(bh_outer, bh_inner).move_to(LEFT_ZONE + RIGHT * 2.7 + UP * 0.35)
        horizon = Text("事件视界", font_size=22, color=IT_ORANGE).next_to(bh_outer, DOWN, buff=0.2)
        bh_label = Text("黑洞结果: 信息 ~ 视界面积", font_size=24, color=IT_YELLOW).next_to(horizon, DOWN, buff=0.25)

        arrow = Arrow(sphere.get_right(), bh.get_left(), color=IT_RED)
        arrow_t = Text("重力极限下规则改变", font_size=22, color=IT_RED).next_to(arrow, UP, buff=0.12)

        panel = self.make_right_panel(
            [
                Text("关键反直觉", font_size=30, color=IT_YELLOW, weight=BOLD),
                Text("黑洞熵不随体积增长", font_size=24, color=IT_WHITE),
                Text("而随事件视界面积增长", font_size=24, color=IT_WHITE),
                Text("边界可编码内部信息", font_size=24, color=IT_GREEN),
            ],
            font_size=24,
            top_offset=1.8,
        )

        self.play(Create(sphere), Write(sphere_label), run_time=1.0)
        self.play(Create(bh), Write(horizon), Write(bh_label), run_time=1.1)
        self.play(GrowArrow(arrow), Write(arrow_t), run_time=0.9)
        self.play(Write(panel), run_time=1.0)
        self.wait(5.5)
        self.clear_stage(title, sphere, sphere_label, bh, horizon, bh_label, arrow, arrow_t, panel)

    def math_core(self):
        title = Text("数学核心", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        eq1 = formula_text("S_BH = (k_B * A) / (4 * l_p^2)", size=42, color=IT_YELLOW)
        eq1.move_to(LEFT_ZONE + UP * 1.0)
        eq2 = formula_text("In natural units: S = A / 4", size=38, color=IT_BLUE)
        eq2.next_to(eq1, DOWN, buff=0.45)
        eq3 = formula_text("Bits ~ A / (4 ln2 * l_p^2)", size=34, color=IT_GREEN)
        eq3.next_to(eq2, DOWN, buff=0.42)

        notes = VGroup(
            Text("A 是事件视界面积，不是体积", font_size=24, color=IT_WHITE),
            Text("单位面积可承载有限比特数", font_size=24, color=IT_ORANGE),
            Text("这给出信息密度的上限约束", font_size=24, color=IT_RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        notes.next_to(eq3, DOWN, buff=0.38)

        panel = self.make_right_panel(
            [
                Text("结论", font_size=30, color=IT_YELLOW, weight=BOLD),
                Text("信息极限是几何量", font_size=24, color=IT_WHITE),
                Text("面积成为核心自由度计数", font_size=24, color=IT_WHITE),
                Text("Bekenstein 上限约束最大信息量", font_size=24, color=IT_GREEN),
            ],
            font_size=24,
            top_offset=1.8,
        )

        self.play(Write(eq1), run_time=1.0)
        self.play(Write(eq2), run_time=0.9)
        self.play(Write(eq3), run_time=0.9)
        self.play(Write(notes), run_time=1.0)
        self.play(Write(panel), run_time=1.0)
        self.wait(8.0)
        self.clear_stage(title, eq1, eq2, eq3, notes, panel)

    def meaning_section(self):
        title = Text("现实意义", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        cards = VGroup(
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.14),
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_ORANGE).set_fill(IT_ORANGE, 0.14),
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_GREEN).set_fill(IT_GREEN, 0.14),
        ).arrange(DOWN, buff=0.4)
        cards.move_to(LEFT_ZONE + DOWN * 0.15)

        labels = VGroup(
            Text("黑洞热力学连接引力、量子与信息", font_size=24, color=IT_WHITE),
            Text("全息思想启发了 AdS/CFT 对偶", font_size=24, color=IT_WHITE),
            Text("黑洞信息悖论至今尚未完全解决", font_size=24, color=IT_WHITE),
        )
        for i, t in enumerate(labels):
            t.move_to(cards[i].get_center())

        summary = self.stage_summary("全息原理让引力、量子与信息首次汇合", color=IT_YELLOW, font_size=30)

        self.play(Create(cards), run_time=1.0)
        self.play(Write(labels), run_time=1.0)
        self.play(Write(summary), run_time=0.9)
        self.wait(8.0)
        self.clear_stage(title, cards, labels, summary)

    def closing(self):
        quote = VGroup(
            Text("黑洞给出的最深刻线索是", font_size=34, color=IT_WHITE),
            Text("几何本身就是信息法则", font_size=42, color=IT_BLUE, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.2)

        preview = VGroup(
            Text("下期预告", font_size=28, color=IT_YELLOW),
            Text("EP20: It from Bit", font_size=34, color=IT_GREEN, weight=BOLD),
            Text("宇宙会不会本质上是信息处理机？", font_size=26, color=IT_WHITE),
        ).arrange(DOWN, buff=0.25)
        preview.to_edge(DOWN, buff=0.8)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(4.8)
        self.play(Write(preview), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, preview)
