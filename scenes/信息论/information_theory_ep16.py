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


class InformationTheoryEP16(ITSceneBase):
    """信息论 EP16: 柯尔莫哥洛夫复杂性"""

    def construct(self):
        self.setup_scene(seed=16)
        self.hook_opening()
        self.intuition_demo()
        self.math_core()
        self.meaning_section()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(16, "柯尔莫哥洛夫复杂性", "Kolmogorov Complexity", color=IT_PURPLE)
        hook = Text("一句描述，真的能压缩你的全部信息吗？", font_size=38, color=IT_YELLOW, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.45)
        tag = Text("复杂性 = 生成对象的最短程序长度", font_size=30, color=IT_GREEN)
        tag.next_to(hook, DOWN, buff=0.45)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(tag, shift=UP), run_time=0.8)
        self.wait(5.3)
        self.clear_stage(title, hook, tag)

    def intuition_demo(self):
        title = Text("直觉：可压缩 vs 不可压缩", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        box1 = RoundedRectangle(width=5.6, height=2.0, corner_radius=0.22, color=IT_GREEN).set_fill(IT_GREEN, 0.14)
        box1.move_to(LEFT * 2.2 + UP * 0.85)
        s1 = Text("x1 = 0101010101010101...", font_size=21, color=IT_WHITE, font="Consolas")
        s1.move_to(box1.get_center() + UP * 0.38)
        d1 = Text("最短描述: 重复 01 全16次", font_size=22, color=IT_GREEN)
        d1.move_to(box1.get_center() + DOWN * 0.42)

        box2 = RoundedRectangle(width=5.6, height=2.0, corner_radius=0.22, color=IT_RED).set_fill(IT_RED, 0.14)
        box2.move_to(LEFT * 2.2 + DOWN * 1.55)
        s2 = Text("x2 = 1100100001101110...", font_size=21, color=IT_WHITE, font="Consolas")
        s2.move_to(box2.get_center() + UP * 0.38)
        d2 = Text("无规律: 描述几乎等于原串", font_size=22, color=IT_RED)
        d2.move_to(box2.get_center() + DOWN * 0.42)

        panel = VGroup(
            Text("关键差别", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("有规律: 短程序可生成", font_size=22, color=IT_GREEN),
            Text("无规律: 难以再压缩", font_size=22, color=IT_RED),
            Text("关心“最短生成描述”", font_size=22, color=IT_ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.0 + UP * 1.0)

        self.play(Create(box1), Write(s1), Write(d1), run_time=1.1)
        self.play(Create(box2), Write(s2), Write(d2), run_time=1.1)
        self.play(Write(panel), run_time=1.0)
        self.wait(5.8)
        self.clear_stage(title, box1, s1, d1, box2, s2, d2, panel)

    def math_core(self):
        title = Text("数学核心", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        eq1 = formula_text("K(x) = min{ |p| : U(p)=x }", size=32, color=IT_YELLOW)
        eq1.move_to(LEFT * 2.5 + UP * 1.0)

        eq2 = Text("U=固定通用图灵机, |p|=程序长度", font_size=22, color=IT_WHITE)
        eq2.next_to(eq1, DOWN, buff=0.35)

        fact = VGroup(
            Text("仅差常数依赖于 U 的选择", font_size=22, color=IT_GREEN),
            Text("不存在算法可精确计算 K(x)", font_size=22, color=IT_RED),
            Text("大多数串满足 K(x) 接近 n", font_size=22, color=IT_ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        fact.next_to(eq2, DOWN, buff=0.35)

        count = formula_text("Count{K(x)<k} <= 2^k - 1", size=26, color=IT_BLUE)
        count.next_to(fact, DOWN, buff=0.35)

        panel = VGroup(
            Text("直观含义", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("短描述 = 结构化信息", font_size=22, color=IT_WHITE),
            Text("长描述 = 随机性更强", font_size=22, color=IT_WHITE),
            Text("复杂性是可压缩性刻度", font_size=22, color=IT_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.0 + UP * 1.0)

        self.play(Write(eq1), run_time=1.0)
        self.play(Write(eq2), run_time=0.9)
        self.play(Write(fact), run_time=1.0)
        self.play(Write(count), run_time=0.9)
        self.play(Write(panel), run_time=1.0)
        self.wait(8.0)
        self.clear_stage(title, eq1, eq2, fact, count, panel)

    def meaning_section(self):
        title = Text("现实意义", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        c1 = RoundedRectangle(width=4.9, height=1.35, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.14)
        c2 = RoundedRectangle(width=4.9, height=1.35, corner_radius=0.2, color=IT_ORANGE).set_fill(IT_ORANGE, 0.14)
        c3 = RoundedRectangle(width=4.9, height=1.35, corner_radius=0.2, color=IT_GREEN).set_fill(IT_GREEN, 0.14)
        cards = VGroup(c1, c2, c3).arrange(DOWN, buff=0.42)
        cards.move_to(LEFT * 1.5 + DOWN * 0.15)

        labels = VGroup(
            Text("机器学习中的模型简洁偏好", font_size=24, color=IT_WHITE),
            Text("压缩算法中的可预测性利用", font_size=24, color=IT_WHITE),
            Text("科学理论追求“最短解释”", font_size=24, color=IT_WHITE),
        )
        for i, t in enumerate(labels):
            t.move_to(cards[i].get_center())

        summary = self.stage_summary("理解世界，本质上是寻找更短的生成规则", color=IT_YELLOW, font_size=30)

        self.play(Create(cards), run_time=1.0)
        self.play(Write(labels), run_time=1.0)
        self.play(Write(summary), run_time=0.9)
        self.wait(8.0)
        self.clear_stage(title, cards, labels, summary)

    def closing(self):
        quote = VGroup(
            Text("复杂，不一定是内容多", font_size=34, color=IT_WHITE),
            Text("也可能是你找不到更短规律", font_size=42, color=IT_RED, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.2)

        preview = VGroup(
            Text("下期预告", font_size=28, color=IT_YELLOW),
            Text("EP17: 停机问题", font_size=34, color=IT_BLUE, weight=BOLD),
            Text("有没有程序能判断所有程序会不会停？", font_size=26, color=IT_WHITE),
        ).arrange(DOWN, buff=0.25)
        preview.to_edge(DOWN, buff=0.8)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(5.0)
        self.play(Write(preview), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, preview)
