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


class InformationTheoryEP14(ITSceneBase):
    """信息论 EP14: 交叉熵"""

    def construct(self):
        self.setup_scene(seed=14)
        self.hook_opening()
        self.intuition_demo()
        self.math_core()
        self.learning_meaning()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(14, "交叉熵", "Cross Entropy", color=IT_BLUE)
        hook = Text("模型明明猜得差不多，为什么损失还很大？", font_size=38, color=IT_YELLOW, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.4)
        tag = Text("关键在“错得有多自信”", font_size=32, color=IT_RED)
        tag.next_to(hook, DOWN, buff=0.45)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(tag, shift=UP), run_time=0.8)
        self.wait(4.0)
        self.clear_stage(title, hook, tag)

    def _bars(self, values, color):
        bars = VGroup()
        for i, v in enumerate(values):
            bar = Rectangle(width=0.7, height=2.8 * v, color=color, fill_opacity=0.7)
            bar.move_to(np.array([i * 1.0 - 1.0, 1.4 * v - 0.6, 0]))
            bars.add(bar)
        return bars

    def intuition_demo(self):
        section_title = Text("直觉演示：真实 P vs 预测 Q", font_size=32, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(section_title), run_time=0.8)

        p_label = Text("真实 P", font_size=26, color=IT_GREEN).move_to(LEFT * 3.0 + UP * 2.0)
        q_label = Text("预测 Q", font_size=26, color=IT_BLUE).move_to(LEFT * 3.0 + DOWN * 0.6)

        p_bars = self._bars([0.05, 0.9, 0.05], IT_GREEN).move_to(LEFT * 3.0 + UP * 1.0)
        q_good = self._bars([0.1, 0.82, 0.08], IT_BLUE).move_to(LEFT * 3.0 + DOWN * 1.7)

        panel = VGroup(
            Text("分类场景", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("真实标签是第2类", font_size=22, color=IT_WHITE),
            Text("Q 第2类概率高 -> 损失低", font_size=22, color=IT_GREEN),
            Text("Q 第2类概率低 -> 损失高", font_size=22, color=IT_RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        panel.move_to(RIGHT * 3.0 + UP * 1.0)

        self.play(Write(p_label), Create(p_bars), run_time=1.2)
        self.play(Write(q_label), Create(q_good), run_time=1.2)
        self.play(Write(panel), run_time=1.0)

        bad_title = Text("反例：预测很自信但方向错了", font_size=26, color=IT_RED)
        bad_title.to_edge(DOWN, buff=1.0)
        q_bad = self._bars([0.78, 0.08, 0.14], IT_RED).move_to(LEFT_ZONE + DOWN * 1.7)

        self.play(Write(bad_title), run_time=0.8)
        self.play(ReplacementTransform(q_good, q_bad), run_time=1.0)
        self.wait(5.5)
        self.clear_stage(section_title, p_label, q_label, p_bars, q_bad, panel, bad_title)

    def math_core(self):
        section_title = Text("数学核心", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(section_title), run_time=0.8)

        eq1 = formula_text("H(P,Q) = -sum p(x)log q(x)", size=32, color=IT_YELLOW)
        eq1.move_to(LEFT * 2.5 + UP * 0.8)
        eq2 = formula_text("One-hot: Loss = -log q(y)", size=30, color=IT_BLUE)
        eq2.next_to(eq1, DOWN, buff=0.5)

        ex = VGroup(
            Text("q(y)=0.9 -> -log(0.9)=0.105", font_size=22, color=IT_GREEN, font="Consolas"),
            Text("q(y)=0.1 -> -log(0.1)=2.303", font_size=22, color=IT_RED, font="Consolas"),
            Text("错得越自信，惩罚越重", font_size=26, color=IT_ORANGE, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        ex.next_to(eq2, DOWN, buff=0.5)

        right = VGroup(
            Text("为什么用 log", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("1) 概率相乘变求和", font_size=22, color=IT_WHITE),
            Text("2) 低概率错误被放大", font_size=22, color=IT_WHITE),
            Text("3) 便于梯度优化", font_size=22, color=IT_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        right.move_to(RIGHT * 3.0 + UP * 1.0)

        self.play(Write(eq1), run_time=1.0)
        self.play(Write(eq2), run_time=1.0)
        self.play(Write(ex), run_time=1.0)
        self.play(Write(right), run_time=1.0)
        self.wait(8.0)
        self.clear_stage(section_title, eq1, eq2, ex, right)

    def learning_meaning(self):
        title = Text("学习含义", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        model = RoundedRectangle(width=2.8, height=1.4, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.15)
        model.move_to(LEFT * 2.0 + UP * 0.6)
        model_t = Text("模型参数", font_size=26, color=IT_WHITE).move_to(model)

        loss = RoundedRectangle(width=2.8, height=1.4, corner_radius=0.2, color=IT_RED).set_fill(IT_RED, 0.15)
        loss.move_to(LEFT * 2.0 + DOWN * 1.2)
        loss_t = Text("交叉熵损失", font_size=26, color=IT_WHITE).move_to(loss)

        arrow_down = Arrow(model.get_bottom(), loss.get_top(), color=IT_YELLOW)
        arrow_up = Arrow(loss.get_right() + RIGHT * 0.1, model.get_right() + RIGHT * 0.1, color=IT_GREEN)
        step1 = Text("前向: 计算损失", font_size=22, color=IT_YELLOW).next_to(arrow_down, LEFT, buff=0.2)
        step2 = Text("反向: 更新参数", font_size=22, color=IT_GREEN).next_to(arrow_up, RIGHT, buff=0.2)

        summary = self.stage_summary("学习 = 持续降低对真实世界的惊讶", color=IT_YELLOW, font_size=30)

        self.play(Create(model), Write(model_t), run_time=0.9)
        self.play(Create(loss), Write(loss_t), run_time=0.9)
        self.play(GrowArrow(arrow_down), Write(step1), run_time=0.8)
        self.play(GrowArrow(arrow_up), Write(step2), run_time=0.8)
        self.play(Write(summary), run_time=0.9)
        self.wait(8.0)
        self.clear_stage(title, model, model_t, loss, loss_t, arrow_down, arrow_up, step1, step2, summary)

    def closing(self):
        quote = VGroup(
            Text("模型不是怕犯错", font_size=34, color=IT_WHITE),
            Text("模型怕的是：自信地犯错", font_size=42, color=IT_RED, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.2)

        preview = VGroup(
            Text("下期预告", font_size=28, color=IT_YELLOW),
            Text("EP15: KL 散度", font_size=34, color=IT_BLUE, weight=BOLD),
            Text("同样偏差，为什么方向不同代价不同？", font_size=26, color=IT_WHITE),
        ).arrange(DOWN, buff=0.25)
        preview.to_edge(DOWN, buff=0.8)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(4.0)
        self.play(Write(preview), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, preview)
