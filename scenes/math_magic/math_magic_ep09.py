"""
数学之美系列 EP09 - 财富分布的幂律法则
为什么富人越来越富？帕累托法则的数学真相
"""

from manim import *
import numpy as np
import random

# 品牌色彩系统
BRAND_PURPLE = "#8B5CF6"
BRAND_PINK = "#FF006E"
BRAND_BLUE = "#00F5FF"
BRAND_YELLOW = "#FFD60A"
BRAND_GREEN = "#06FFB4"
BRAND_RED = "#FF4444"
BRAND_GRAY = "#6B7280"


class WealthParetoLaw(Scene):
    """EP09: 财富分布的幂律法则"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#0A0E27"

        random.seed(42)
        np.random.seed(42)

        self.show_opening()
        self.show_pareto_law()
        self.show_compound_growth()
        self.show_takeaways()
        self.show_brand_finale()

    def show_opening(self):
        self.clear()

        hook_lines = VGroup(
            Text("为什么富人会越来越富？", font_size=56, color=BRAND_PINK, weight=BOLD),
            Text("其实是一套隐藏的数学机制", font_size=42, color=BRAND_YELLOW, weight=BOLD),
            Text("一起来拆解帕累托法则", font_size=36, color=WHITE),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        hook_lines.move_to(UP * 0.3)

        self.play(Write(hook_lines[0], run_time=1.4))
        self.play(Write(hook_lines[1], run_time=1.2))
        self.play(FadeIn(hook_lines[2], shift=UP * 0.3, run_time=1.0))
        self.wait(1.4)

        promise = Text(
            "掌握它，就能看懂贫富差距背后的数学逻辑",
            font_size=34,
            color=BRAND_GREEN,
            weight=BOLD,
        )
        promise.next_to(hook_lines, DOWN, buff=0.9, aligned_edge=LEFT)

        self.play(FadeIn(promise, shift=UP * 0.3, run_time=1.0))
        self.wait(1.2)

        self.play(FadeOut(VGroup(hook_lines, promise), shift=UP * 0.5, run_time=1.0))
        self.wait(0.4)

        stat_group = VGroup(
            Text("全球最富的 1%", font_size=48, color=BRAND_YELLOW, weight=BOLD),
            Text("掌握了全球 50% 的财富", font_size=54, color=BRAND_RED, weight=BOLD),
        ).arrange(DOWN, buff=0.5)
        stat_group.shift(DOWN * 0.1)

        self.play(FadeIn(stat_group[0], run_time=1.0))
        self.play(FadeIn(stat_group[1], run_time=1.1))
        self.wait(1.1)

        question = Text("这只是偶然吗？", font_size=48, color=BRAND_PINK, weight=BOLD)
        question.next_to(stat_group, DOWN, buff=0.8)

        self.play(Write(question, run_time=1.0))
        self.wait(0.9)

        answer = Text("更可能是数学规律在发挥作用", font_size=48, color=BRAND_GREEN, weight=BOLD)
        answer.move_to(question.get_center())

        self.play(Transform(question, answer), run_time=1.1)
        self.wait(1.3)

        self.play(FadeOut(VGroup(stat_group, question), shift=DOWN * 0.4, run_time=1.0))
        self.wait(0.5)

    def show_pareto_law(self):
        self.clear()

        title = Text("帕累托法则如何分配财富", font_size=44, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=UP * 0.2, run_time=1.2))
        self.wait(0.6)

        distribution = self.build_distribution_panel()
        distribution["group"].scale(0.95)
        distribution["group"].move_to(DOWN * 0.2)

        self.play(FadeIn(distribution["panel"], run_time=1.0))
        self.play(
            LaggedStart(
                *[FadeIn(person, scale=0.4) for person in distribution["people"]],
                lag_ratio=0.025,
                run_time=3.2,
            )
        )
        self.play(FadeIn(distribution["highlight"], run_time=0.9))
        self.play(FadeIn(distribution["labels"], shift=UP * 0.2, run_time=0.9))
        self.wait(1.2)

        insight_distribution = Text(
            "现实中的 20/80 现象，其实是幂律分布在起作用",
            font_size=30,
            color=BRAND_PINK,
            weight=BOLD,
        )
        insight_distribution.next_to(distribution["group"], DOWN, buff=0.8)

        self.play(FadeIn(insight_distribution, shift=UP * 0.2, run_time=1.0))
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(title, distribution["group"], insight_distribution), shift=UP * 0.3, run_time=1.1)
        )
        self.wait(0.6)

        self.clear()

        formula_title = Text("指数参数，决定了不平等的程度", font_size=42, color=BRAND_PURPLE, weight=BOLD)
        formula_title.to_edge(UP, buff=0.5)
        self.play(FadeIn(formula_title, shift=UP * 0.2, run_time=1.2))
        self.wait(0.6)

        formula_panel = self.build_formula_panel()
        formula_panel["group"].move_to(DOWN * 0.2)

        self.play(FadeIn(formula_panel["panel"], run_time=1.0))
        self.play(Write(formula_panel["formula"], run_time=1.2))
        for detail in formula_panel["details"]:
            self.play(FadeIn(detail, shift=UP * 0.2, run_time=0.8))
        self.wait(1.0)

        formula_insight = Text(
            "α 越小，尾部越厚，财富越容易集中在少数人手中",
            font_size=30,
            color=BRAND_PINK,
            weight=BOLD,
        )
        formula_insight.next_to(formula_panel["group"], DOWN, buff=0.8)

        self.play(FadeIn(formula_insight, shift=UP * 0.2, run_time=1.0))
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(formula_title, formula_panel["group"], formula_insight), shift=UP * 0.3, run_time=1.1)
        )
        self.wait(0.5)

    def show_compound_growth(self):
        self.clear()

        title = Text("同样收益率，为什么差距越拉越大？", font_size=44, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=UP * 0.2, run_time=1.2))
        self.wait(0.6)

        comparison = self.build_growth_comparison()
        comparison["group"].move_to(DOWN * 0.1)

        self.play(FadeIn(comparison["panel"], run_time=1.0))
        self.play(FadeIn(comparison["rich_header"], shift=UP * 0.3, run_time=0.9))
        for box in comparison["rich_boxes"]:
            self.play(FadeIn(box, shift=UP * 0.15, run_time=0.6))
        self.wait(0.6)

        self.play(FadeIn(comparison["poor_header"], shift=UP * 0.3, run_time=0.9))
        for box in comparison["poor_boxes"]:
            self.play(FadeIn(box, shift=UP * 0.15, run_time=0.6))
        self.wait(0.8)

        gap_text = Text(
            "本金越大，同样的 20% 涨幅带来的绝对差距也越大",
            font_size=30,
            color=BRAND_RED,
            weight=BOLD,
        )
        gap_text.next_to(comparison["group"], DOWN, buff=0.9)

        self.play(FadeIn(gap_text, shift=UP * 0.2, run_time=1.0))
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(title, comparison["group"], gap_text), shift=UP * 0.3, run_time=1.1)
        )
        self.wait(0.6)

    def show_takeaways(self):
        self.clear()

        card = RoundedRectangle(
            width=8.5,
            height=4.6,
            corner_radius=0.3,
            fill_color=WHITE,
            fill_opacity=0.05,
            stroke_color=WHITE,
            stroke_width=2,
        )

        lines = VGroup(
            Text("破局关键：主动提升自己的收益率", font_size=34, color=BRAND_GREEN, weight=BOLD),
            Text("持续学习与积累，让复利为你服务", font_size=32, color=BRAND_YELLOW),
            Text("善用幂律思维，聚焦指数级的机会", font_size=30, color=BRAND_PINK),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        lines.move_to(card.get_center() + DOWN * 0.1)

        group = VGroup(card, lines)
        group.move_to(ORIGIN)

        self.play(FadeIn(card, run_time=1.0))
        for line in lines:
            self.play(FadeIn(line, shift=UP * 0.2, run_time=0.9))
        self.wait(1.4)

        self.play(FadeOut(group, shift=UP * 0.3, run_time=1.0))
        self.wait(0.5)

    def show_brand_finale(self):
        self.clear()

        summary = VGroup(
            Text("财富分布遵循幂律法则", font_size=40, color=WHITE, weight=BOLD),
            Text("理解规律，就能重新设计自己的增长曲线", font_size=34, color=BRAND_GREEN),
        ).arrange(DOWN, buff=0.55)
        summary.shift(UP * 0.6)

        self.play(FadeIn(summary[0], shift=UP * 0.2, run_time=1.0))
        self.play(FadeIn(summary[1], shift=UP * 0.2, run_time=1.0))
        self.wait(1.4)

        self.play(FadeOut(summary, shift=UP * 0.3, run_time=1.0))
        self.wait(0.4)

        brand_main = Text("数学之美", font_size=64, color=BRAND_PINK, weight=BOLD)
        brand_sub = Text("发现生活中的数学奥秘", font_size=32, color=BRAND_BLUE)
        brand = VGroup(brand_main, brand_sub).arrange(DOWN, buff=0.35)
        brand.move_to(UP * 0.2)

        particles = VGroup()
        for _ in range(20):
            particle = Dot(
                radius=0.06,
                color=random.choice([BRAND_YELLOW, BRAND_GREEN, BRAND_PINK]),
                fill_opacity=random.uniform(0.6, 1),
            )
            angle = random.uniform(0, TAU)
            radius = random.uniform(2.2, 3.2)
            particle.move_to([radius * np.cos(angle), radius * np.sin(angle), 0])
            particles.add(particle)

        particles.scale(0.95)

        cta = Text("关注「数学之美」，一起把数学变成成长杠杆", font_size=34, color=BRAND_YELLOW)
        cta.shift(DOWN * 2.4)

        self.play(Write(brand, run_time=1.1), FadeIn(particles, lag_ratio=0.1))
        self.play(
            FadeIn(cta, shift=UP * 0.2),
            Rotate(particles, angle=PI / 5, about_point=ORIGIN),
            run_time=1.1,
        )
        self.wait(1.6)

    def build_distribution_panel(self):
        panel = RoundedRectangle(
            width=5.6,
            height=5.8,
            corner_radius=0.3,
            fill_color=WHITE,
            fill_opacity=0.05,
            stroke_color=WHITE,
            stroke_width=2,
        )

        people = VGroup()
        for idx in range(100):
            person = Circle(radius=0.12, stroke_width=2, fill_opacity=0.85)
            if idx < 20:
                person.set_fill(BRAND_YELLOW, opacity=1)
                person.set_stroke(BRAND_YELLOW)
            else:
                person.set_fill(BRAND_GRAY, opacity=0.25)
                person.set_stroke(BRAND_GRAY)
            people.add(person)

        people.arrange_in_grid(rows=10, cols=10, buff=0.12)
        people.move_to(panel.get_center())

        highlight = SurroundingRectangle(VGroup(*people[:20]), color=BRAND_YELLOW, buff=0.18)
        highlight.set_stroke(width=3)

        label_20 = Text("前20%人口", font_size=24, color=BRAND_YELLOW, weight=BOLD)
        label_80 = Text("掌握80%财富", font_size=28, color=BRAND_RED, weight=BOLD)
        label_20.next_to(panel, UP, buff=0.35)
        label_80.next_to(panel, DOWN, buff=0.35)

        base_label = Text("剩余80%人口 → 仅分得20%财富", font_size=24, color=BRAND_GRAY)
        base_label.next_to(label_80, DOWN, buff=0.3)

        group = VGroup(panel, people, highlight, label_20, label_80, base_label)

        return {
            "group": group,
            "panel": panel,
            "people": people,
            "highlight": highlight,
            "labels": VGroup(label_20, label_80, base_label),
        }

    def build_formula_panel(self):
        panel = RoundedRectangle(
            width=6.0,
            height=5.2,
            corner_radius=0.3,
            fill_color=WHITE,
            fill_opacity=0.04,
            stroke_color=WHITE,
            stroke_width=2,
        )

        title = Text("数学视角", font_size=30, color=BRAND_PURPLE, weight=BOLD)
        formula = MathTex(
            r"P(X > x) = \left(\frac{x_m}{x}\right)^\alpha",
            font_size=34,
            color=BRAND_GREEN,
        )

        detail_1 = Text("α = 帕累托指数", font_size=24, color=WHITE)
        detail_2 = Text("α 常见取值在 1.5 - 2 左右", font_size=24, color=BRAND_YELLOW)
        detail_3 = Text("α 越小 → 不平等越严重", font_size=24, color=BRAND_RED)

        content = VGroup(title, formula, detail_1, detail_2, detail_3).arrange(
            DOWN,
            buff=0.35,
            aligned_edge=LEFT,
        )
        content.move_to(panel.get_center() + DOWN * 0.1)

        group = VGroup(panel, content)

        return {
            "group": group,
            "panel": panel,
            "formula": formula,
            "details": [detail_1, detail_2, detail_3],
        }

    def build_growth_comparison(self):
        panel = RoundedRectangle(
            width=8.9,
            height=6.4,
            corner_radius=0.3,
            fill_color=WHITE,
            fill_opacity=0.05,
            stroke_color=WHITE,
            stroke_width=2,
        )

        rich_row = self._create_growth_row(
            "富人：起点 1 万，收益率 20%",
            ["1万", "1.2万", "1.44万", "1.73万"],
            BRAND_YELLOW,
        )
        poor_row = self._create_growth_row(
            "普通人：起点 100，收益率同样 20%",
            ["100", "120", "144", "173"],
            BRAND_GRAY,
        )

        rows = VGroup(rich_row["group"], poor_row["group"]).arrange(DOWN, buff=1.2, aligned_edge=LEFT)
        rows.move_to(panel.get_center())

        group = VGroup(panel, rows)

        return {
            "group": group,
            "panel": panel,
            "rich_header": rich_row["header"],
            "rich_boxes": rich_row["boxes"],
            "poor_header": poor_row["header"],
            "poor_boxes": poor_row["boxes"],
        }

    def _create_growth_row(self, title, values, color):
        header = Text(title, font_size=30, color=color, weight=BOLD)
        boxes = VGroup()
        for value in values:
            cell_bg = RoundedRectangle(
                width=1.6,
                height=0.85,
                corner_radius=0.18,
                stroke_color=color,
                stroke_width=2,
                fill_color=color,
                fill_opacity=0.2,
            )
            cell_text = Text(value, font_size=24, color=WHITE)
            cell_text.move_to(cell_bg.get_center())
            boxes.add(VGroup(cell_bg, cell_text))
        boxes.arrange(RIGHT, buff=0.6)

        row = VGroup(header, boxes).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        row.align_to(header, LEFT)

        return {
            "group": row,
            "header": header,
            "boxes": boxes,
        }


# 渲染命令：
# 预览：python -m manim scenes/math_magic/math_magic_ep09.py WealthParetoLaw -pql
# 发布：python -m manim scenes/math_magic/math_magic_ep09.py WealthParetoLaw -qh --resolution 1080,1920 --frame_rate 60
