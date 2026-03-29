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


class InformationTheoryEP18(ITSceneBase):
    """信息论 EP18: 生命与信息"""

    def construct(self):
        self.setup_scene(seed=18)
        self.hook_opening()
        self.intuition_demo()
        self.math_core()
        self.meaning_section()
        self.closing()

    def hook_opening(self):
        title = self.make_title_block(18, "生命与信息", "Life as Information", color=IT_GREEN)
        hook = Text("生命，是否只是四字母编码系统？", font_size=38, color=IT_YELLOW, weight=BOLD)
        hook.move_to(ORIGIN + UP * 0.45)
        tag = Text("A T C G 不只是化学符号，也是信息载体", font_size=30, color=IT_BLUE)
        tag.next_to(hook, DOWN, buff=0.45)

        self.play(Write(title), run_time=1.2)
        self.play(Write(hook), run_time=1.0)
        self.play(FadeIn(tag, shift=UP), run_time=0.8)
        self.wait(5.0)
        self.clear_stage(title, hook, tag)

    def intuition_demo(self):
        title = Text("直觉：从序列到功能", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        dna_box = RoundedRectangle(width=6.0, height=1.8, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.14)
        dna_box.move_to(LEFT_ZONE + UP * 1.1)
        dna_t1 = Text("DNA", font_size=24, color=IT_BLUE, weight=BOLD).move_to(dna_box.get_center() + UP * 0.45)
        dna_t2 = Text("ATG CCT GAA TTT CGA ...", font_size=28, color=IT_WHITE, font="Consolas")
        dna_t2.move_to(dna_box.get_center() + DOWN * 0.35)

        rna_box = RoundedRectangle(width=6.0, height=1.45, corner_radius=0.2, color=IT_ORANGE).set_fill(IT_ORANGE, 0.14)
        rna_box.move_to(LEFT_ZONE + DOWN * 0.35)
        rna_t = Text("mRNA: AUG CCU GAA UUU CGA ...", font_size=24, color=IT_WHITE, font="Consolas")
        rna_t.move_to(rna_box)

        protein_box = RoundedRectangle(width=6.0, height=1.45, corner_radius=0.2, color=IT_GREEN).set_fill(IT_GREEN, 0.14)
        protein_box.move_to(LEFT_ZONE + DOWN * 1.95)
        protein_t = Text("Protein: Met-Pro-Glu-Phe-Arg ...", font_size=24, color=IT_WHITE, font="Consolas")
        protein_t.move_to(protein_box)

        a1 = Arrow(dna_box.get_bottom(), rna_box.get_top(), color=IT_YELLOW)
        a2 = Arrow(rna_box.get_bottom(), protein_box.get_top(), color=IT_YELLOW)
        a1_t = Text("转录", font_size=22, color=IT_YELLOW).next_to(a1, RIGHT, buff=0.15)
        a2_t = Text("翻译", font_size=22, color=IT_YELLOW).next_to(a2, RIGHT, buff=0.15)

        panel = self.make_right_panel(
            [
                Text("核心流程", font_size=30, color=IT_YELLOW, weight=BOLD),
                Text("DNA 保存遗传信息", font_size=24, color=IT_WHITE),
                Text("RNA 传递信息", font_size=24, color=IT_WHITE),
                Text("蛋白质执行功能", font_size=24, color=IT_GREEN),
            ],
            font_size=24,
            top_offset=1.8,
        )

        self.play(Create(dna_box), Write(dna_t1), Write(dna_t2), run_time=1.1)
        self.play(Create(rna_box), Write(rna_t), GrowArrow(a1), Write(a1_t), run_time=1.0)
        self.play(Create(protein_box), Write(protein_t), GrowArrow(a2), Write(a2_t), run_time=1.0)
        self.play(Write(panel), run_time=1.0)
        self.wait(5.5)
        self.clear_stage(
            title,
            dna_box,
            dna_t1,
            dna_t2,
            rna_box,
            rna_t,
            protein_box,
            protein_t,
            a1,
            a1_t,
            a2,
            a2_t,
            panel,
        )

    def math_core(self):
        title = Text("数学核心", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        eq1 = formula_text("Alphabet = {A,T,C,G},  log2(4) = 2 bits/base", size=34, color=IT_YELLOW)
        eq1.move_to(LEFT_ZONE + UP * 1.0)
        eq2 = formula_text("Genome length N  =>  information upper bound = 2N bits", size=32, color=IT_BLUE)
        eq2.next_to(eq1, DOWN, buff=0.45)
        eq3 = formula_text("Codon count: 4^3 = 64  -> maps to 20 amino acids + stop", size=31, color=IT_GREEN)
        eq3.next_to(eq2, DOWN, buff=0.42)

        notes = VGroup(
            Text("冗余编码提升容错性", font_size=24, color=IT_ORANGE),
            Text("突变 = 信息扰动；选择 = 信息筛选", font_size=24, color=IT_RED),
            Text("遗传系统是“可复制+可更新”的信息系统", font_size=25, color=IT_WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        notes.next_to(eq3, DOWN, buff=0.38)

        panel = self.make_right_panel(
            [
                Text("注意边界", font_size=30, color=IT_YELLOW, weight=BOLD),
                Text("2N bits 是上界估计", font_size=24, color=IT_WHITE),
                Text("真实生物意义受调控网络影响", font_size=24, color=IT_WHITE),
                Text("生命不止代码，还包括动力学", font_size=24, color=IT_GREEN),
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
        title = Text("生物信息学视角", font_size=34, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=0.8)

        cards = VGroup(
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_BLUE).set_fill(IT_BLUE, 0.14),
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_ORANGE).set_fill(IT_ORANGE, 0.14),
            RoundedRectangle(width=5.2, height=1.35, corner_radius=0.2, color=IT_GREEN).set_fill(IT_GREEN, 0.14),
        ).arrange(DOWN, buff=0.4)
        cards.move_to(LEFT_ZONE + DOWN * 0.15)

        labels = VGroup(
            Text("基因组 ~750MB，压缩后仅 ~4MB → 高冗余结构", font_size=22, color=IT_WHITE),
            Text("同义突变不改变蛋白质 → 天然纠错码", font_size=22, color=IT_WHITE),
            Text("合成生物学：从信息蓝图设计全新生命", font_size=22, color=IT_WHITE),
        )
        for i, t in enumerate(labels):
            t.move_to(cards[i].get_center())

        summary = self.stage_summary("遗传系统的精妙，正是信息编码的精妙", color=IT_YELLOW, font_size=30)

        self.play(Create(cards), run_time=1.0)
        self.play(Write(labels), run_time=1.0)
        self.play(Write(summary), run_time=0.9)
        self.wait(8.0)
        self.clear_stage(title, cards, labels, summary)

    def closing(self):
        quote = VGroup(
            Text("生命当然不止代码", font_size=34, color=IT_WHITE),
            Text("但没有信息，就没有可遗传的生命", font_size=42, color=IT_GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.45)
        quote.move_to(ORIGIN + UP * 0.2)

        preview = VGroup(
            Text("下期预告", font_size=28, color=IT_YELLOW),
            Text("EP19: 全息宇宙论", font_size=34, color=IT_BLUE, weight=BOLD),
            Text("为什么黑洞面积决定信息量？", font_size=26, color=IT_WHITE),
        ).arrange(DOWN, buff=0.25)
        preview.to_edge(DOWN, buff=0.8)

        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=1.0)
        self.wait(4.8)
        self.play(Write(preview), run_time=1.0)
        self.wait(5.0)
        self.clear_stage(quote, preview)
