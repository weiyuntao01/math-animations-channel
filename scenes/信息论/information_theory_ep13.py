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


class InformationTheoryEP13(ITSceneBase):
    """信息论 EP13: 零知识证明"""

    def construct(self):
        self.setup_scene(seed=13)
        self.hook_opening()
        self.alibaba_cave_demo()
        self.math_core()
        self.real_world_value()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(13, "零知识证明", "Zero-Knowledge Proof", color=IT_PURPLE)
        hook = Text("你能证明你知道密码，却一句密码都不说吗？", font_size=40, color=IT_YELLOW, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.4)
        conflict = Text("这就是零知识证明", font_size=34, color=IT_GREEN)
        conflict.next_to(hook, DOWN, buff=0.5)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(conflict, shift=UP), run_time=0.8)
        self.wait(3.5)
        self.clear_stage(title, hook, conflict)

    def _make_cave(self):
        left_arc = Arc(radius=1.8, start_angle=PI * 0.2, angle=PI * 0.8, color=IT_BLUE, stroke_width=6)
        right_arc = Arc(radius=1.8, start_angle=-PI, angle=PI * 0.8, color=IT_BLUE, stroke_width=6)
        left_arc.move_to(LEFT_ZONE + DOWN * 0.2)
        right_arc.move_to(LEFT_ZONE + DOWN * 0.2)

        branch_l = Line(LEFT_ZONE + UP * 1.4, LEFT_ZONE + LEFT * 1.4 + DOWN * 0.2, color=IT_BLUE, stroke_width=6)
        branch_r = Line(LEFT_ZONE + UP * 1.4, LEFT_ZONE + RIGHT * 1.4 + DOWN * 0.2, color=IT_BLUE, stroke_width=6)
        door = Line(LEFT_ZONE + LEFT * 0.2 + DOWN * 1.7, LEFT_ZONE + RIGHT * 0.2 + DOWN * 1.7, color=IT_RED, stroke_width=8)
        cave = VGroup(left_arc, right_arc, branch_l, branch_r, door)
        return cave, door

    def alibaba_cave_demo(self):
        section_title = Text("直觉演示：阿里巴巴洞穴", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(section_title), run_time=0.8)

        cave, door = self._make_cave()
        peggy = Dot(color=IT_GREEN, radius=0.12).move_to(LEFT_ZONE + UP * 1.5)
        victor = Dot(color=IT_YELLOW, radius=0.12).move_to(LEFT_ZONE + UP * 2.1)
        peggy_label = Text("Peggy", font_size=20, color=IT_GREEN).next_to(peggy, LEFT, buff=0.2)
        victor_label = Text("Victor", font_size=20, color=IT_YELLOW).next_to(victor, RIGHT, buff=0.2)

        panel = self.make_right_panel(
            [
                Text("流程", font_size=28, color=IT_YELLOW, weight=BOLD),
                Text("1) Peggy 随机进左或右", font_size=22, color=IT_WHITE),
                Text("2) Victor 喊她从某侧出来", font_size=22, color=IT_WHITE),
                Text("3) 知道咒语可开门换边", font_size=22, color=IT_WHITE),
                Text("4) 多轮后可信度快速上升", font_size=22, color=IT_GREEN),
            ],
            font_size=22,
            top_offset=1.2,
        )

        self.play(Create(cave), FadeIn(peggy), FadeIn(victor), Write(peggy_label), Write(victor_label), run_time=1.2)
        self.play(Write(panel), run_time=1.2)
        self.wait(3.5)

        # 一轮演示
        self.play(peggy.animate.move_to(LEFT_ZONE + LEFT * 1.2 + DOWN * 0.3), run_time=0.8)
        request = Text("Victor: 从右边出来", font_size=26, color=IT_YELLOW)
        request.to_edge(DOWN, buff=1.0)
        self.play(Write(request), run_time=0.7)

        self.play(door.animate.set_color(IT_GREEN), run_time=0.4)
        self.play(peggy.animate.move_to(LEFT_ZONE + RIGHT * 1.2 + DOWN * 0.3), run_time=0.8)

        verified = Text("Victor 看到结果，但没得到密码", font_size=28, color=IT_GREEN, weight=BOLD)
        verified.next_to(request, UP, buff=0.4)
        self.play(Write(verified), run_time=0.8)
        self.wait(5.5)
        self.clear_stage(section_title, cave, peggy, victor, peggy_label, victor_label, panel, request, verified)

    def math_core(self):
        section_title = Text("数学核心", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(section_title), run_time=0.8)

        eq1 = formula_text("CheatProb = (1/2)^k", size=36, color=IT_YELLOW)
        eq1.move_to(LEFT * 2.8 + UP * 0.6)

        eq2 = Text("k 是独立验证轮数", font_size=26, color=IT_WHITE)
        eq2.next_to(eq1, DOWN, buff=0.5)

        examples = VGroup(
            Text("k=1 -> 50%", font_size=24, color=IT_WHITE),
            Text("k=10 -> 0.098%", font_size=24, color=IT_GREEN),
            Text("k=20 -> 0.000095%", font_size=24, color=IT_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        examples.next_to(eq2, DOWN, buff=0.5)

        right = VGroup(
            Text("三条性质", font_size=28, color=IT_YELLOW, weight=BOLD),
            Text("完备性: 诚实者能通过", font_size=22, color=IT_WHITE),
            Text("可靠性: 作弊概率极低", font_size=22, color=IT_WHITE),
            Text("零知识: 学不到秘密", font_size=22, color=IT_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        right.move_to(RIGHT * 3.0 + UP * 1.2)

        self.play(Write(eq1), run_time=0.9)
        self.play(Write(eq2), run_time=0.7)
        self.play(Write(examples), run_time=1.0)
        self.play(Write(right), run_time=1.0)
        self.wait(8.0)
        self.clear_stage(section_title, eq1, eq2, examples, right)

    def real_world_value(self):
        title = Text("现实价值", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        left_cards = VGroup(
            RoundedRectangle(width=4.2, height=1.3, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.15),
            RoundedRectangle(width=4.2, height=1.3, corner_radius=0.2, color=IT_ORANGE).set_fill(IT_ORANGE, 0.15),
            RoundedRectangle(width=4.2, height=1.3, corner_radius=0.2, color=IT_GREEN).set_fill(IT_GREEN, 0.15),
        ).arrange(DOWN, buff=0.4)
        left_cards.move_to(LEFT * 1.5 + DOWN * 0.2)

        labels = VGroup(
            Text("无密码泄露的身份认证", font_size=24, color=IT_WHITE),
            Text("区块链隐私证明", font_size=24, color=IT_WHITE),
            Text("在不公开数据下证明合规", font_size=24, color=IT_WHITE),
        )
        for i, t in enumerate(labels):
            t.move_to(left_cards[i].get_center())

        philosophy = self.stage_summary("信任不必靠坦白，可以靠可验证的结构", color=IT_YELLOW, font_size=30)

        self.play(Create(left_cards), run_time=1.0)
        self.play(Write(labels), run_time=1.0)
        self.play(Write(philosophy), run_time=0.9)
        self.wait(8.0)
        self.clear_stage(title, left_cards, labels, philosophy)

    def closing(self):
        quote = VGroup(
            Text("你不需要交出秘密", font_size=34, color=IT_WHITE),
            Text("你只需要证明你掌握了秘密", font_size=42, color=IT_GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.2)

        preview = VGroup(
            Text("下期预告", font_size=28, color=IT_YELLOW),
            Text("EP14: 交叉熵", font_size=34, color=IT_BLUE, weight=BOLD),
            Text("模型每次猜错，到底错了多少？", font_size=26, color=IT_WHITE),
        ).arrange(DOWN, buff=0.25)
        preview.to_edge(DOWN, buff=0.8)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(4.0)
        self.play(Write(preview), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, preview)
