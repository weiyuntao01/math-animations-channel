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


class InformationTheoryEP15(ITSceneBase):
    """信息论 EP15: KL 散度"""

    def construct(self):
        self.setup_scene(seed=15)
        self.hook_opening()
        self.intuition_demo()
        self.math_core()
        self.application_view()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(15, "KL 散度", "Kullback-Leibler Divergence", color=IT_BLUE)
        hook = Text("同样偏差，为什么方向一换，代价就不同？", font_size=38, color=IT_YELLOW, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.45)
        tag = Text("KL 测的是“用 Q 解释 P”的额外代价", font_size=30, color=IT_GREEN)
        tag.next_to(hook, DOWN, buff=0.45)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(tag, shift=UP), run_time=0.8)
        self.wait(4.5)
        self.clear_stage(title, hook, tag)

    def _bars(self, values, color):
        bars = VGroup()
        for i, v in enumerate(values):
            bar = Rectangle(width=0.9, height=2.8 * v, color=color, fill_opacity=0.72)
            bar.move_to(np.array([i * 1.25 - 0.65, 1.4 * v - 0.8, 0]))
            bars.add(bar)
        return bars

    def intuition_demo(self):
        title = Text("直觉：方向不同，惩罚不同", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        p_label = Text("真实分布 P", font_size=26, color=IT_GREEN).move_to(LEFT * 3.0 + UP * 2.0)
        q_label = Text("近似分布 Q", font_size=26, color=IT_BLUE).move_to(LEFT * 3.0 + DOWN * 0.4)

        p_bars = self._bars([0.99, 0.01], IT_GREEN).move_to(LEFT * 3.0 + UP * 0.95)
        q_bars = self._bars([0.90, 0.10], IT_BLUE).move_to(LEFT * 3.0 + DOWN * 1.6)

        p_text = Text("P: 罕见事件 1%", font_size=20, color=IT_WHITE).next_to(p_bars, DOWN, buff=0.08).shift(UP * 0.15)
        q_text = Text("Q: 罕见事件 10%", font_size=20, color=IT_WHITE).next_to(q_bars, DOWN, buff=0.06).shift(UP * 0.25)

        panel = VGroup(
            Text("同一对分布", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("D(P||Q) = 0.071", font_size=24, color=IT_GREEN, font="Consolas"),
            Text("D(Q||P) = 0.145", font_size=24, color=IT_RED, font="Consolas"),
            Text("数值不同 -> KL 非对称", font_size=22, color=IT_ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.0 + UP * 1.0)

        arrow1 = Arrow(LEFT * 1.8 + UP * 0.15, RIGHT * 1.5 + UP * 0.15, color=IT_GREEN)
        arrow2 = Arrow(RIGHT * 1.5 + DOWN * 0.5, LEFT * 1.8 + DOWN * 0.5, color=IT_RED)
        a1_t = Text("P -> Q", font_size=22, color=IT_GREEN).next_to(arrow1, UP, buff=0.15)
        a2_t = Text("Q -> P", font_size=22, color=IT_RED).next_to(arrow2, DOWN, buff=0.15)

        self.play(Write(p_label), Create(p_bars), run_time=1.1)
        self.play(Write(q_label), Create(q_bars), run_time=1.1)
        self.play(Write(p_text), Write(q_text), run_time=0.8)
        self.play(Write(panel), run_time=1.0)
        self.play(GrowArrow(arrow1), Write(a1_t), GrowArrow(arrow2), Write(a2_t), run_time=1.0)
        self.wait(5.5)
        self.clear_stage(title, p_label, q_label, p_bars, q_bars, p_text, q_text, panel, arrow1, arrow2, a1_t, a2_t)

    def math_core(self):
        title = Text("数学核心", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        eq1 = formula_text("D_KL(P||Q) = sum p(x)log(p/q)", size=30, color=IT_YELLOW)
        eq1.move_to(LEFT * 2.5 + UP * 0.95)
        eq2 = formula_text("D_KL >= 0, =0 iff P=Q", size=28, color=IT_GREEN)
        eq2.next_to(eq1, DOWN, buff=0.4)
        eq3 = formula_text("D_KL(P||Q) != D_KL(Q||P)", size=30, color=IT_RED)
        eq3.next_to(eq2, DOWN, buff=0.35)

        ex = VGroup(
            Text("若 P(x)>0 且 Q(x)=0", font_size=22, color=IT_WHITE),
            Text("D_KL(P||Q) = +inf", font_size=24, color=IT_ORANGE, font="Consolas", weight=BOLD),
            Text("漏掉真实可能性 = 高代价", font_size=22, color=IT_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        ex.next_to(eq3, DOWN, buff=0.25)

        panel = VGroup(
            Text("不是距离", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("1) 不对称", font_size=22, color=IT_WHITE),
            Text("2) 不满足三角不等式", font_size=22, color=IT_WHITE),
            Text("它是信息损失度量", font_size=22, color=IT_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.0 + UP * 1.0)

        self.play(Write(eq1), run_time=1.0)
        self.play(Write(eq2), run_time=0.9)
        self.play(Write(eq3), run_time=0.9)
        self.play(Write(ex), run_time=1.0)
        self.play(Write(panel), run_time=1.0)
        self.wait(8.0)
        self.clear_stage(title, eq1, eq2, eq3, ex, panel)

    def application_view(self):
        title = Text("建模含义", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        left_box = RoundedRectangle(width=4.8, height=2.0, corner_radius=0.25, color=IT_GREEN).set_fill(IT_GREEN, 0.14)
        left_box.move_to(LEFT * 2.8 + UP * 0.5)
        left_txt = VGroup(
            Text("最小化 D(P||Q)", font_size=28, color=IT_GREEN, weight=BOLD),
            Text("倾向覆盖全部模式", font_size=22, color=IT_WHITE),
        ).arrange(DOWN, buff=0.2).move_to(left_box)

        right_box = RoundedRectangle(width=4.8, height=2.0, corner_radius=0.25, color=IT_BLUE).set_fill(IT_BLUE, 0.14)
        right_box.move_to(RIGHT * 2.8 + UP * 0.5)
        right_txt = VGroup(
            Text("最小化 D(Q||P)", font_size=28, color=IT_BLUE, weight=BOLD),
            Text("倾向抓住高密度区域", font_size=22, color=IT_WHITE),
        ).arrange(DOWN, buff=0.2).move_to(right_box)

        note = VGroup(
            Text("同一数据，不同KL方向，不同模型行为", font_size=26, color=IT_YELLOW),
            Text("优化方向本身就是建模决策", font_size=26, color=IT_ORANGE, weight=BOLD),
        ).arrange(DOWN, buff=0.28)
        note.to_edge(DOWN, buff=0.85)

        self.play(Create(left_box), Write(left_txt), run_time=1.0)
        self.play(Create(right_box), Write(right_txt), run_time=1.0)
        self.play(Write(note), run_time=1.0)
        self.wait(8.0)
        self.clear_stage(title, left_box, right_box, left_txt, right_txt, note)

    def closing(self):
        quote = VGroup(
            Text("KL 的核心提醒不是“有差异”", font_size=34, color=IT_WHITE),
            Text("而是“差异朝哪个方向看”", font_size=42, color=IT_RED, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.25)

        preview = VGroup(
            Text("下期预告", font_size=28, color=IT_YELLOW),
            Text("EP16: 柯尔莫哥洛夫复杂性", font_size=32, color=IT_BLUE, weight=BOLD),
            Text("一句描述能压缩多少信息?", font_size=24, color=IT_WHITE),
        ).arrange(DOWN, buff=0.25)
        preview.to_edge(DOWN, buff=0.8)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(4.0)
        self.play(Write(preview), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, preview)
