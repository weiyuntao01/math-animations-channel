"""
数学之美系列 EP08 - 股市的随机游走理论
为什么股票一买就跌？随机游走提供答案
8分钟深度科普
"""

from manim import *
import numpy as np
import random
from typing import List, Optional

BRAND_PURPLE = "#8B5CF6"
BRAND_PINK = "#FF006E"
BRAND_BLUE = "#00F5FF"
BRAND_YELLOW = "#FFD60A"
BRAND_GREEN = "#06FFB4"
BRAND_RED = "#FF4444"
BRAND_GRAY = "#6B7280"


class RandomWalkMarketsEP08(Scene):
    """EP08: 股市的随机游走理论"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#0A0E27"

        random.seed(42)
        np.random.seed(42)

        self.show_opening()
        self.random_walk_foundation()
        self.why_predictions_fail()
        self.technical_analysis_limitations()
        self.rational_investing_principles()
        self.kelly_criterion_application()
        self.show_conclusion()
        self.show_brand_ending()

    def show_opening(self):
        self.clear()

        hook = VGroup(
            Text("股市的随机游走理论", font_size=56, color=BRAND_PINK, weight=BOLD),
            Text("为什么股票一买就跌？", font_size=46, color=BRAND_YELLOW, weight=BOLD),
            Text("短期噪声 ≠ 长期价值", font_size=40, color=WHITE)
        ).arrange(DOWN, buff=0.4)

        self.play(Write(hook[0], run_time=0.7))
        self.play(Write(hook[1], run_time=0.6), hook[1].animate.scale(1.05))
        self.play(Write(hook[2], run_time=0.6))
        self.wait(1)

        promise = Text("本集：用真实的数学解释股价波动", font_size=36, color=BRAND_GREEN, weight=BOLD)
        promise.next_to(hook, DOWN, buff=0.6)
        self.play(FadeIn(promise, shift=UP))
        self.wait(1.5)

        self.play(FadeOut(VGroup(hook, promise)))

    def random_walk_foundation(self):
        self.clear()

        title = Text("随机游走：价格像醉汉漫步", font_size=40, color=BRAND_PINK, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        chart_group = self.create_random_walk_chart()
        for mob in chart_group:
            self.play(Create(mob), run_time=0.4)

        theory_points = self.create_random_walk_theory_points()
        for point in theory_points:
            self.play(FadeIn(point, shift=UP), run_time=0.5)

        self.wait(2)
        self.play(FadeOut(VGroup(title, chart_group, theory_points)))

    def create_random_walk_chart(self) -> VGroup:
        axes = Axes(
            x_range=[0, 60, 10],
            y_range=[80, 120, 10],
            x_length=6,
            y_length=4,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 16
            }
        )
        axes.shift(LEFT * 3.5 + DOWN * 0.2)

        x_label = Text("交易日", font_size=24, color=WHITE)
        x_label.next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("价格指数", font_size=24, color=WHITE)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3).rotate(PI / 2)

        steps = 60
        dt = 1 / 252
        mu = 0.08
        sigma = 0.2
        increments = np.random.normal(0, 1, steps)
        log_returns = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * increments
        log_returns = np.insert(log_returns, 0, 0.0)
        prices = 100 * np.exp(np.cumsum(log_returns))
        x_values = np.arange(len(prices))

        price_path = axes.plot_line_graph(
            x_values=x_values,
            y_values=prices,
            add_vertex_dots=False,
            line_color=BRAND_BLUE,
            stroke_width=4
        )

        expected_curve = axes.plot(
            lambda x: 100 * np.exp(mu * x * dt),
            x_range=[0, 60],
            color=BRAND_PURPLE,
            stroke_width=2,
            use_smoothing=False
        )

        start_dot = Dot(color=BRAND_GREEN, radius=0.08)
        start_dot.move_to(axes.c2p(0, prices[0]))
        end_dot = Dot(color=BRAND_YELLOW, radius=0.08)
        end_dot.move_to(axes.c2p(x_values[-1], prices[-1]))

        caption = Text("几何布朗运动模拟", font_size=28, color=BRAND_BLUE, weight=BOLD)
        caption.next_to(axes, DOWN, buff=0.6)

        legend = VGroup(
            Square(side_length=0.25, fill_color=BRAND_BLUE, fill_opacity=1, stroke_width=0),
            Text("实际路径", font_size=20, color=WHITE),
            Square(side_length=0.25, fill_color=BRAND_PURPLE, fill_opacity=1, stroke_width=0),
            Text("期望轨迹", font_size=20, color=WHITE)
        )
        legend.arrange(RIGHT, buff=0.2)
        legend.next_to(axes, UP, buff=0.4)

        return VGroup(axes, x_label, y_label, price_path, expected_curve, start_dot, end_dot, caption, legend)

    def create_random_walk_theory_points(self) -> VGroup:
        header = Text("数学模型", font_size=34, color=BRAND_YELLOW, weight=BOLD)
        formula = MathTex(
            r"S_{t+\Delta t} = S_t \exp\left((\mu - \tfrac{\sigma^2}{2})\Delta t + \sigma \sqrt{\Delta t}\, Z\right)",
            font_size=32
        ).set_color(WHITE)
        normal_note = MathTex(r"Z \sim \mathcal{N}(0,1)", font_size=30).set_color(WHITE)
        independence = Text("增量独立，方差与时间成正比", font_size=30, color=WHITE)
        takeaway = Text("短期难以预测，长期收益由 μ 决定", font_size=30, color=BRAND_GREEN)

        points = VGroup(header, formula, normal_note, independence, takeaway)
        points.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        points.to_edge(RIGHT, buff=0.8)

        return points

    def why_predictions_fail(self):
        self.clear()

        title = Text("为什么预测无效：有效市场假说", font_size=40, color=BRAND_PINK, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        equation = MathTex(
            r"\mathbb{E}[S_{t+1} \mid \mathcal{F}_t] = (1 + r) S_t",
            font_size=40
        ).set_color(WHITE)
        equation.to_edge(LEFT, buff=1.0)
        highlight = SurroundingRectangle(equation, color=BRAND_GREEN, buff=0.3, corner_radius=0.2)

        self.play(Write(equation))
        self.play(Create(highlight))

        explanations = VGroup(
            Text("公开信息会被瞬间写进价格", font_size=30, color=WHITE),
            Text("超额收益 = 承担额外风险", font_size=30, color=BRAND_YELLOW),
            Text("套利者会压平可预测性", font_size=30, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanations.next_to(equation, RIGHT, buff=1.0)

        for item in explanations:
            self.play(FadeIn(item, shift=UP), run_time=0.5)

        caution = Text("结论：短期价格像噪声，长期收益靠企业盈利", font_size=32, color=BRAND_GREEN, weight=BOLD)
        caution.next_to(explanations, DOWN, buff=0.5)
        self.play(Write(caution))

        self.wait(2)
        self.play(FadeOut(VGroup(title, equation, highlight, explanations, caution)))

    def technical_analysis_limitations(self):
        self.clear()

        title = Text("技术分析的数学漏洞", font_size=40, color=BRAND_PINK, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        cards = VGroup(
            self.create_pattern_card(
                "形态记忆幻觉",
                BRAND_BLUE,
                ["样本量不足以支撑显著性", "噪声中找模式是认知偏差", "需要假设检验 + P 值校验"],
            ),
            self.create_pattern_card(
                "指标滞后效应",
                BRAND_YELLOW,
                ["移动平均本质是平滑历史", "信号滞后导致追涨杀跌", "高频交易会抹平简单策略"],
            ),
            self.create_pattern_card(
                "数据挖掘偏差",
                BRAND_GREEN,
                ["过拟合历史噪声", "缺少交叉验证", "统计显著性 + 稳健性缺位"],
            ),
        )
        cards.arrange(RIGHT, buff=0.8)
        cards.move_to(DOWN * 0.2)

        for card in cards:
            self.play(FadeIn(card, shift=UP), run_time=0.6)

        footnote = Text("可靠策略必须同时通过统计检验与风险控制", font_size=28, color=WHITE)
        footnote.next_to(cards, DOWN, buff=0.6)
        self.play(Write(footnote))

        self.wait(2)
        self.play(FadeOut(VGroup(title, cards, footnote)))

    def rational_investing_principles(self):
        self.clear()

        title = Text("理性投资的数学原则", font_size=40, color=BRAND_PINK, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        grid = self.create_principle_grid()
        self.play(FadeIn(grid, lag_ratio=0.1, run_time=1.2))

        self.wait(2)
        self.play(FadeOut(VGroup(title, grid)))

    def kelly_criterion_application(self):
        self.clear()

        title = Text("凯利公式：下注多少才科学", font_size=40, color=BRAND_PINK, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))

        # 公式居中显示
        formula = MathTex(r"f^{*} = \frac{bp - q}{b}", font_size=48).set_color(BRAND_GREEN)
        formula.move_to(UP * 2)
        self.play(Write(formula))

        # 第一排：公式含义解释
        top_row = VGroup(
            Text("含义：f* 为最优仓位占比", font_size=28, color=WHITE),
            Text("b 为赔率，p 为胜率，q = 1 - p", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.2)
        top_row.next_to(formula, DOWN, buff=0.5)

        # 第二排：实例计算
        example_title = Text("例子：胜率 55%，赔率 1:1", font_size=30, color=BRAND_YELLOW, weight=BOLD)
        example_calc = MathTex(r"f^{*} = \frac{1 \times 0.55 - 0.45}{1} = 0.10", font_size=34).set_color(WHITE)
        example_result = Text("→ 把资金的 10% 投入该策略", font_size=30, color=BRAND_GREEN, weight=BOLD)
        
        bottom_row = VGroup(example_title, example_calc, example_result)
        bottom_row.arrange(DOWN, buff=0.25)
        bottom_row.next_to(top_row, DOWN, buff=0.7)

        # 风险提示居中
        caution = Text("现实中参数存在误差，应折半或更保守", font_size=28, color=BRAND_RED, weight=BOLD)
        caution.next_to(bottom_row, DOWN, buff=0.6)

        # 动画播放
        self.play(FadeIn(top_row, shift=UP), run_time=0.8)
        
        for item in bottom_row:
            self.play(FadeIn(item, shift=UP), run_time=0.6)
            
        self.play(Write(caution))

        self.wait(2)
        self.play(FadeOut(VGroup(title, formula, top_row, bottom_row, caution)))

    def show_conclusion(self):
        self.clear()

        summary = VGroup(
            Text("请记住三个结论：", font_size=36, color=BRAND_YELLOW, weight=BOLD),
            Text("1. 股价短期 ≈ 随机游走，没人能稳定预测", font_size=32, color=WHITE),
            Text("2. 超额收益来自风险补偿与资本结构", font_size=32, color=BRAND_GREEN),
            Text("3. 策略有效性要靠数学模型 + 数据检验", font_size=32, color=WHITE),
        ).arrange(DOWN, buff=0.4)

        for item in summary:
            self.play(Write(item), run_time=0.7)

        self.wait(2)
        self.play(FadeOut(summary))

    def show_brand_ending(self):
        self.clear()

        brand_main = Text("数学之美", font_size=64, color=BRAND_PINK, weight=BOLD)
        brand_sub = Text("Math Magic", font_size=38, color=BRAND_BLUE, slant=ITALIC)
        brand = VGroup(brand_main, brand_sub).arrange(DOWN, buff=0.25)
        brand.set_stroke(width=3)

        episode_info = Text("EP08: 股市的随机游走理论", font_size=28, color=WHITE)
        episode_info.next_to(brand, DOWN, buff=0.6)

        tagline = Text("用真实的数学守护你的投资决策", font_size=32, color=BRAND_YELLOW)
        tagline.next_to(episode_info, DOWN, buff=0.4)

        particles = VGroup()
        for i in range(24):
            particle = Dot(
                radius=0.05,
                color=random.choice([BRAND_PINK, BRAND_BLUE, BRAND_YELLOW, BRAND_GREEN]),
                fill_opacity=random.uniform(0.5, 1.0)
            )
            angle = (i / 24) * TAU
            radius = random.uniform(2.3, 3.7)
            particle.move_to([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ])
            particles.add(particle)

        self.play(Write(brand, run_time=1.2), FadeIn(particles, lag_ratio=0.1), run_time=1.5)
        self.play(Write(episode_info), Write(tagline), Rotate(particles, angle=PI / 6, about_point=ORIGIN), run_time=1.5)
        self.wait(3)

    def create_pattern_card(self, title: str, color, bullet_lines: List[str]) -> VGroup:
        bg = RoundedRectangle(
            width=3.6,
            height=3.4,
            corner_radius=0.25,
            fill_color=color,
            fill_opacity=0.12,
            stroke_color=color,
            stroke_width=2
        )

        header = Text(title, font_size=28, color=color, weight=BOLD)
        header.move_to(bg.get_top() + DOWN * 0.6)

        bullets = VGroup(*[Text(f"- {line}", font_size=22, color=WHITE) for line in bullet_lines])
        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        bullets.next_to(header, DOWN, buff=0.3, aligned_edge=LEFT)

        header.align_to(bg, LEFT).shift(RIGHT * 0.3)
        bullets.align_to(header, LEFT)

        return VGroup(bg, header, bullets)

    def create_principle_grid(self) -> VGroup:
        cards = [
            self.create_principle_card(
                "资产配置 = 风险分散",
                BRAND_BLUE,
                ["目标：最小化组合方差", "相关性越低，组合越稳"],
                r"\sigma_p^2 = w^{\top} \Sigma w",
            ),
            self.create_principle_card(
                "长期收益来自风险补偿",
                BRAND_GREEN,
                ["资本资产定价模型 (CAPM)", "\beta 衡量系统性风险"],
                r"\mathbb{E}[R] \approx r_f + \beta (R_m - r_f)",
            ),
            self.create_principle_card(
                "再平衡：锁定波动收益",
                BRAND_PINK,
                ["定期回归目标权重", "低买高卖的机械化执行", "减少情绪化操作"],
                None,
            ),
            self.create_principle_card(
                "成本与风险控制",
                BRAND_YELLOW,
                ["费用率差 1% = 长期收益差 20%+", "用 VaR / CVaR 约束最大回撤", "现金流匹配保障安全边际"],
                None,
            ),
        ]

        left_column = VGroup(cards[0], cards[2]).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        right_column = VGroup(cards[1], cards[3]).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        layout = VGroup(left_column, right_column).arrange(RIGHT, buff=1.4, aligned_edge=UP)
        layout.move_to(DOWN * 0.3)
        layout.scale(0.88)
        return layout

    def create_principle_card(
        self,
        title: str,
        color,
        lines: List[str],
        formula: Optional[str] = None,
    ) -> VGroup:
        bg = RoundedRectangle(
            width=5.4,
            height=3.6,
            corner_radius=0.25,
            fill_color=color,
            fill_opacity=0.12,
            stroke_color=color,
            stroke_width=2
        )

        header = Text(title, font_size=28, color=color, weight=BOLD)
        header.move_to(bg.get_top() + DOWN * 0.7)

        body_items: List[Mobject] = []
        if formula:
            formula_tex = MathTex(formula, font_size=28).set_color(WHITE)
            body_items.append(formula_tex)

        for line in lines:
            body_items.append(Text(line, font_size=22, color=WHITE))

        body = VGroup(*body_items)
        body.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        body.next_to(header, DOWN, buff=0.35, aligned_edge=LEFT)

        header.align_to(bg, LEFT).shift(RIGHT * 0.4)
        body.align_to(header, LEFT)

        return VGroup(bg, header, body)
