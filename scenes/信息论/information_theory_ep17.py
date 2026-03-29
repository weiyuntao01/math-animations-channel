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
    LEFT_ZONE,
    RIGHT_ZONE,
    formula_text,
)


class InformationTheoryEP17(ITSceneBase):
    """信息论 EP17: 停机问题"""

    def construct(self):
        self.setup_scene(seed=17)
        self.hook_opening()
        self.intuition_demo()
        self.math_core()
        self.impact_section()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(17, "停机问题", "The Halting Problem", color=IT_RED)
        hook = Text("有没有程序，能判断任意程序会不会停？", font_size=38, color=IT_YELLOW, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.45)
        tag = Text("图灵的结论：不存在这样的万能判定器", font_size=30, color=IT_GREEN)
        tag.next_to(hook, DOWN, buff=0.45)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(tag, shift=UP), run_time=0.8)
        self.wait(5.1)
        self.clear_stage(title, hook, tag)

    def intuition_demo(self):
        title = Text("直觉：你想造一个“停机预言机”", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        detector = RoundedRectangle(width=3.8, height=1.6, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.15)
        detector.move_to(LEFT * 2.8 + UP * 0.4)
        detector_t = VGroup(
            Text("Halt(P, x)", font_size=30, color=IT_YELLOW, font="Consolas", weight=BOLD),
            Text("输入: 程序 P 与输入 x", font_size=20, color=IT_WHITE),
        ).arrange(DOWN, buff=0.2).move_to(detector)

        yes_box = RoundedRectangle(width=2.4, height=1.1, corner_radius=0.18, color=IT_GREEN).set_fill(IT_GREEN, 0.14)
        yes_box.move_to(LEFT * 0.2 + UP * 1.0)
        yes_t = Text("输出 YES\n(会停机)", font_size=21, color=IT_GREEN).move_to(yes_box)

        no_box = RoundedRectangle(width=2.4, height=1.1, corner_radius=0.18, color=IT_RED).set_fill(IT_RED, 0.14)
        no_box.move_to(LEFT * 0.2 + DOWN * 0.5)
        no_t = Text("输出 NO\n(不停止)", font_size=21, color=IT_RED).move_to(no_box)

        a1 = Arrow(detector.get_right(), yes_box.get_left(), color=IT_GREEN)
        a2 = Arrow(detector.get_right() + DOWN * 0.25, no_box.get_left(), color=IT_RED)

        panel = VGroup(
            Text("看上去很合理", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("给定代码预测运行命运", font_size=22, color=IT_WHITE),
            Text("可自动证明无穷循环", font_size=22, color=IT_WHITE),
            Text("但会被“自指”击穿", font_size=22, color=IT_ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.0 + UP * 1.0)

        self.play(Create(detector), Write(detector_t), run_time=1.1)
        self.play(Create(yes_box), Write(yes_t), GrowArrow(a1), run_time=1.0)
        self.play(Create(no_box), Write(no_t), GrowArrow(a2), run_time=1.0)
        self.play(Write(panel), run_time=1.0)
        self.wait(5.8)
        self.clear_stage(title, detector, detector_t, yes_box, yes_t, no_box, no_t, a1, a2, panel)

    def math_core(self):
        title = Text("数学反证", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        assume = formula_text("Assume H(P,x): HALT/LOOP", size=26, color=IT_YELLOW)
        assume.move_to(LEFT * 2.5 + UP * 1.15)

        code_lines = VGroup(
            Text("Construct D(y):", font_size=24, color=IT_WHITE, font="Consolas"),
            Text("if Halt(y,y)==1: loop", font_size=22, color=IT_RED, font="Consolas"),
            Text("else: halt", font_size=22, color=IT_GREEN, font="Consolas"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        code_lines.next_to(assume, DOWN, buff=0.35)

        paradox = VGroup(
            Text("现在询问 D(D)", font_size=26, color=IT_BLUE, weight=BOLD),
            Text("Halt(D,D)=1 -> D循环,矛盾", font_size=22, color=IT_RED),
            Text("Halt(D,D)=0 -> D停机,矛盾", font_size=22, color=IT_RED),
            Text("Halt不可能对所有程序正确", font_size=24, color=IT_ORANGE, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        paradox.next_to(code_lines, DOWN, buff=0.25)

        panel = VGroup(
            Text("结论", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("停机问题不可判定", font_size=22, color=IT_WHITE),
            Text("不存在通用算法", font_size=22, color=IT_WHITE),
            Text("是能力边界,非算力不足", font_size=22, color=IT_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.0 + UP * 1.0)

        self.play(Write(assume), run_time=1.0)
        self.play(Write(code_lines), run_time=1.0)
        self.play(Write(paradox), run_time=1.1)
        self.play(Write(panel), run_time=1.0)
        self.wait(8.0)
        self.clear_stage(title, assume, code_lines, paradox, panel)

    def impact_section(self):
        title = Text("现实影响", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        cards = VGroup(
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.14),
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_ORANGE).set_fill(IT_ORANGE, 0.14),
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_GREEN).set_fill(IT_GREEN, 0.14),
        ).arrange(DOWN, buff=0.4)
        cards.move_to(LEFT * 1.5 + DOWN * 0.15)

        labels = VGroup(
            Text("分析器无法给所有程序完美答案", font_size=24, color=IT_WHITE),
            Text("自动验错存在先天盲区", font_size=24, color=IT_WHITE),
            Text("可计算性理论给出工程边界", font_size=24, color=IT_WHITE),
        )
        for i, t in enumerate(labels):
            t.move_to(cards[i].get_center())

        summary = self.stage_summary("有些问题不是难，而是原则上不可判定", color=IT_YELLOW, font_size=30)

        self.play(Create(cards), run_time=1.0)
        self.play(Write(labels), run_time=1.0)
        self.play(Write(summary), run_time=0.9)
        self.wait(8.0)
        self.clear_stage(title, cards, labels, summary)

    def closing(self):
        quote = VGroup(
            Text("图灵告诉我们的，不只是计算有多强", font_size=33, color=IT_WHITE),
            Text("更是计算有边界", font_size=42, color=IT_RED, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.2)

        preview = VGroup(
            Text("下期预告", font_size=28, color=IT_YELLOW),
            Text("EP18: 生命与信息", font_size=34, color=IT_BLUE, weight=BOLD),
            Text("生命是否只是四字母编码系统？", font_size=26, color=IT_WHITE),
        ).arrange(DOWN, buff=0.25)
        preview.to_edge(DOWN, buff=0.8)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(4.8)
        self.play(Write(preview), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, preview)
