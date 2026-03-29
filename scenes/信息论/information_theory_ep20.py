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


class InformationTheoryEP20(ITSceneBase):
    """信息论 EP20: It from Bit"""

    def construct(self):
        self.setup_scene(seed=20)
        self.hook_opening()
        self.intuition_demo()
        self.math_core()
        self.meaning_section()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(20, "It from Bit", "Wheeler's Vision", color=IT_YELLOW)
        hook = Text("宇宙，会不会本质上是信息处理机？", font_size=38, color=IT_GREEN, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.45)
        tag = Text("Wheeler: every it derives from bit", font_size=30, color=IT_BLUE)
        tag.next_to(hook, DOWN, buff=0.45)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(tag, shift=UP), run_time=0.8)
        self.wait(5.0)
        self.clear_stage(title, hook, tag)

    def intuition_demo(self):
        title = Text("直觉：观测把世界写成比特", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        atom = Circle(radius=0.95, color=IT_BLUE, stroke_width=4).set_fill(IT_BLUE, 0.12)
        atom.move_to(LEFT_ZONE + UP * 0.45)
        atom_t = Text("物理系统", font_size=24, color=IT_WHITE).next_to(atom, DOWN, buff=0.25)

        meter = RoundedRectangle(width=2.7, height=1.5, corner_radius=0.2, color=IT_ORANGE).set_fill(IT_ORANGE, 0.14)
        meter.move_to(LEFT_ZONE + RIGHT * 2.4 + UP * 0.45)
        meter_t = Text("测量装置", font_size=24, color=IT_WHITE).move_to(meter)

        bits = VGroup(
            Square(0.48, color=IT_GREEN).set_fill(IT_GREEN, 0.15),
            Square(0.48, color=IT_GREEN).set_fill(IT_GREEN, 0.15),
            Square(0.48, color=IT_GREEN).set_fill(IT_GREEN, 0.15),
            Square(0.48, color=IT_GREEN).set_fill(IT_GREEN, 0.15),
        ).arrange(RIGHT, buff=0.18)
        bits.move_to(LEFT_ZONE + RIGHT * 1.2 + DOWN * 1.15)
        bit_txt = VGroup(
            Text("0", font_size=22, color=IT_GREEN, font="Consolas"),
            Text("1", font_size=22, color=IT_GREEN, font="Consolas"),
            Text("1", font_size=22, color=IT_GREEN, font="Consolas"),
            Text("0", font_size=22, color=IT_GREEN, font="Consolas"),
        )
        for i in range(4):
            bit_txt[i].move_to(bits[i])

        a1 = Arrow(atom.get_right(), meter.get_left(), color=IT_YELLOW)
        a2 = Arrow(meter.get_bottom(), bits.get_top(), color=IT_YELLOW)
        a1_t = Text("相互作用", font_size=22, color=IT_YELLOW).next_to(a1, UP, buff=0.12)
        a2_t = Text("读出结果", font_size=22, color=IT_YELLOW).next_to(a2, RIGHT, buff=0.12)

        panel = self.make_right_panel(
            [
                Text("核心想法", font_size=30, color=IT_YELLOW, weight=BOLD),
                Text("物理量通过观测给出离散结果", font_size=24, color=IT_WHITE),
                Text("结果可编码为比特序列", font_size=24, color=IT_WHITE),
                Text("可验证现实由信息约束", font_size=24, color=IT_GREEN),
            ],
            font_size=24,
            top_offset=1.8,
        )

        self.play(Create(atom), Write(atom_t), run_time=1.0)
        self.play(Create(meter), Write(meter_t), GrowArrow(a1), Write(a1_t), run_time=1.0)
        self.play(Create(bits), Write(bit_txt), GrowArrow(a2), Write(a2_t), run_time=1.0)
        self.play(Write(panel), run_time=1.0)
        self.wait(5.5)
        self.clear_stage(title, atom, atom_t, meter, meter_t, bits, bit_txt, a1, a2, a1_t, a2_t, panel)

    def math_core(self):
        title = Text("参与式宇宙", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        eq1 = formula_text("Question = {yes, no}  =>  1 bit of reality", size=34, color=IT_YELLOW)
        eq1.move_to(LEFT_ZONE + UP * 1.0)
        eq2 = formula_text("N binary questions  =>  2^N possible states", size=32, color=IT_BLUE)
        eq2.next_to(eq1, DOWN, buff=0.45)
        eq3 = formula_text("Physical law  =  constraint on valid bit-strings", size=31, color=IT_GREEN)
        eq3.next_to(eq2, DOWN, buff=0.42)

        notes = VGroup(
            Text("观测行为把潜在选项坍缩为确定答案", font_size=24, color=IT_WHITE),
            Text("答案的集合构成物理现实的描述", font_size=24, color=IT_ORANGE),
            Text("定律不产生实体，而是筛选允许的比特模式", font_size=24, color=IT_RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        notes.next_to(eq3, DOWN, buff=0.38)

        panel = self.make_right_panel(
            [
                Text("Wheeler 的洞察", font_size=30, color=IT_YELLOW, weight=BOLD),
                Text("观测者参与构建现实", font_size=24, color=IT_WHITE),
                Text("延迟选择实验可实验验证", font_size=24, color=IT_WHITE),
                Text("信息先于物质存在", font_size=24, color=IT_GREEN),
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
        title = Text("系列回顾：从比特到宇宙", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        # Timeline-style series recap with 4 phases
        phases = VGroup()
        phase_data = [
            ("基础 EP1-5", "熵·编码·信道", IT_BLUE),
            ("方法 EP6-10", "压缩·纠错·率失真", IT_ORANGE),
            ("边界 EP11-17", "复杂性·停机·不可判定", IT_RED),
            ("现实 EP18-20", "生命·时空·万物", IT_GREEN),
        ]
        for i, (label, desc, color) in enumerate(phase_data):
            node = VGroup(
                Circle(radius=0.35, color=color, stroke_width=3).set_fill(color, 0.2),
                Text(label, font_size=18, color=color, weight=BOLD),
                Text(desc, font_size=16, color=IT_WHITE),
            )
            node[1].next_to(node[0], DOWN, buff=0.15)
            node[2].next_to(node[1], DOWN, buff=0.08)
            phases.add(node)
        phases.arrange(RIGHT, buff=0.65)
        phases.move_to(LEFT_ZONE + UP * 0.3)

        # Connecting arrows between phases
        arrows = VGroup()
        for i in range(3):
            a = Arrow(
                phases[i][0].get_right(),
                phases[i + 1][0].get_left(),
                color=IT_YELLOW,
                buff=0.08,
                stroke_width=2,
            )
            arrows.add(a)

        summary = self.stage_summary(
            "20集旅程: 一个 log 之问，通向理解世界的方式",
            color=IT_YELLOW,
            font_size=29,
        )

        self.play(LaggedStart(*[Create(p) for p in phases], lag_ratio=0.3), run_time=2.0)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.25), run_time=1.2)
        self.play(Write(summary), run_time=0.9)
        self.wait(8.0)
        self.clear_stage(title, phases, arrows, summary)

    def closing(self):
        quote = VGroup(
            Text("我们从“消息传输”出发", font_size=34, color=IT_WHITE),
            Text("最终走到“宇宙如何编码自己”", font_size=42, color=IT_GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.3)

        ending = VGroup(
            Text("信息论系列完结", font_size=30, color=IT_YELLOW, weight=BOLD),
            Text("下一系列将继续从数学走向现实", font_size=26, color=IT_BLUE),
        ).arrange(DOWN, buff=0.25)
        ending.to_edge(DOWN, buff=0.85)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(4.8)
        self.play(Write(ending), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, ending)
