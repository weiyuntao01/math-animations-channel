"""
数字仿生系列 第9集：免疫系统的战争艺术（优化版）
Digital Biomimetics EP09: The Art of War in Immune System (Optimized)

针对视频号优化：简化视觉、放大字体、缩短时长
"""

from manim import *
import numpy as np
from typing import List, Tuple

# 系列通用色彩
BIO_CYAN = ManimColor("#00FFE5")
BIO_PURPLE = ManimColor("#8B5CF6")
BIO_GREEN = ManimColor("#00FF88")
BIO_BLUE = ManimColor("#007EFF")
BIO_YELLOW = ManimColor("#FFE500")
BIO_RED = ManimColor("#FF0066")
BIO_WHITE = ManimColor("#FFFFFF")
BIO_GRAY = ManimColor("#303030")

# EP09 主题色
IMMUNE_GREEN = ManimColor("#4ADE80")
VIRUS_RED = ManimColor("#EF4444")
ANTIBODY_BLUE = ManimColor("#3B82F6")

# 视频号优化字体大小
TITLE_SIZE = 52       # 超大标题
SUBTITLE_SIZE = 40    # 大标题
NORMAL_SIZE = 32      # 正常文字
SMALL_SIZE = 28       # 最小文字


class DigitalBiomimeticsEP09(Scene):
    """数字仿生系列 第9集 - 优化版"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        # 1. 快速开场（5秒）
        self.show_series_intro()
        
        # 2. 问题钩子（10秒）
        self.vaccine_question()
        
        # 3. 三道防线演示（30秒）
        self.three_defense_lines()
        
        # 4. 疫苗原理（20秒）
        self.vaccine_principle()
        
        # 5. 实用知识（15秒）
        self.practical_knowledge()
        
        # 6. 结尾总结（10秒）
        self.show_ending()

    def show_series_intro(self):
        """快速系列开场 - 5秒"""
        series_title = Text("数字仿生", font_size=60, color=BIO_CYAN, weight=BOLD)
        episode_text = Text("第9集：免疫系统的战争艺术", font_size=36, color=IMMUNE_GREEN)
        episode_text.next_to(series_title, DOWN, buff=0.5)
        
        self.play(Write(series_title), run_time=1)
        self.play(FadeIn(episode_text), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(series_title), FadeOut(episode_text), run_time=0.5)

    def vaccine_question(self):
        """问题钩子 - 10秒"""
        # 大字提问
        question = Text(
            "为什么打了疫苗",
            font_size=TITLE_SIZE,
            color=BIO_YELLOW
        )
        question2 = Text(
            "还会感冒？",
            font_size=TITLE_SIZE,
            color=BIO_YELLOW
        )
        question2.next_to(question, DOWN, buff=0.3)
        
        self.play(Write(question), run_time=1)
        self.play(Write(question2), run_time=1)
        self.wait(3)
        
        # 先让问题文字消失，避免重叠
        self.play(FadeOut(question), FadeOut(question2), run_time=0.8)
        
        # 简单图示：疫苗符号和病毒
        vaccine = self.create_simple_vaccine()
        vaccine.shift(LEFT * 2.5)
        virus = self.create_simple_virus()
        virus.shift(RIGHT * 2.5)
        
        self.play(
            FadeIn(vaccine, shift=UP),
            FadeIn(virus, shift=UP),
            run_time=1
        )
        
        # 问号
        question_mark = Text("?", font_size=80, color=BIO_WHITE)
        question_mark.move_to(ORIGIN)
        self.play(Write(question_mark), run_time=0.5)
        
        self.wait(3)
        self.play(
            FadeOut(vaccine), FadeOut(virus), FadeOut(question_mark),
            run_time=1
        )

    def create_simple_vaccine(self):
        """创建简单的疫苗图标"""
        syringe = VGroup(
            Rectangle(width=0.3, height=1.5, fill_color=ANTIBODY_BLUE, fill_opacity=0.8),
            Triangle(fill_color=ANTIBODY_BLUE, fill_opacity=1).scale(0.3).shift(DOWN * 0.9)
        )
        label = Text("疫苗", font_size=SMALL_SIZE, color=ANTIBODY_BLUE)
        label.next_to(syringe, DOWN, buff=0.3)
        return VGroup(syringe, label)

    def create_simple_virus(self):
        """创建简单的病毒图标"""
        virus = VGroup(
            Circle(radius=0.4, fill_color=VIRUS_RED, fill_opacity=0.8),
            *[Dot(radius=0.08, color=VIRUS_RED).move_to(
                0.4 * np.array([np.cos(a), np.sin(a), 0])
            ) for a in np.linspace(0, TAU, 8, endpoint=False)]
        )
        label = Text("病毒", font_size=SMALL_SIZE, color=VIRUS_RED)
        label.next_to(virus, DOWN, buff=0.3)
        return VGroup(virus, label)

    def three_defense_lines(self):
        """三道防线演示 - 30秒"""
        title = Text("身体的三道防线", font_size=SUBTITLE_SIZE, color=IMMUNE_GREEN)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)
        
        # 创建三道防线的可视化
        defense_lines = VGroup()
        
        # 第一道：皮肤屏障
        line1 = self.create_defense_line_1()
        line1.shift(LEFT * 4)
        self.play(FadeIn(line1), run_time=1)
        self.wait(1)
        
        # 演示病毒被挡住
        virus = Circle(radius=0.1, color=VIRUS_RED, fill_opacity=1)
        virus.move_to([-4, 1.5, 0])
        self.play(virus.animate.move_to([-4, 0.5, 0]), run_time=0.5)
        bounce_back = virus.animate.move_to([-4, 1.5, 0])
        self.play(bounce_back, run_time=0.3)
        self.play(FadeOut(virus), run_time=0.2)
        
        # 第二道：白细胞
        line2 = self.create_defense_line_2()
        line2.move_to(ORIGIN)
        self.play(FadeIn(line2), run_time=1)
        self.wait(1)
        
        # 演示吞噬
        virus2 = Circle(radius=0.1, color=VIRUS_RED, fill_opacity=1)
        virus2.move_to([0, 1.5, 0])
        self.play(virus2.animate.move_to([0, 0, 0]), run_time=0.5)
        # 白细胞吞噬动画
        white_cell = Circle(radius=0.3, color=BIO_WHITE, fill_opacity=0.8)
        white_cell.move_to([0, -0.5, 0])
        self.play(
            white_cell.animate.scale(1.5).move_to([0, 0, 0]),
            FadeOut(virus2),
            run_time=0.5
        )
        self.play(white_cell.animate.scale(0.67), run_time=0.3)
        
        # 第三道：抗体
        line3 = self.create_defense_line_3()
        line3.shift(RIGHT * 4)
        self.play(FadeIn(line3), run_time=1)
        self.wait(1)
        
        # 演示抗体结合
        virus3 = Circle(radius=0.1, color=VIRUS_RED, fill_opacity=1)
        virus3.move_to([4, 1.5, 0])
        antibody = self.create_antibody_symbol()
        antibody.move_to([4, -0.5, 0])
        
        self.play(virus3.animate.move_to([4, 0.5, 0]), run_time=0.5)
        self.play(antibody.animate.move_to([4, 0.5, 0]), run_time=0.5)
        self.play(
            FadeOut(virus3),
            antibody.animate.set_color(IMMUNE_GREEN),
            run_time=0.5
        )
        
        # 总结
        summary = Text(
            "层层防御，分工明确",
            font_size=SUBTITLE_SIZE,
            color=BIO_YELLOW,
            weight=BOLD
        )
        summary.shift(DOWN * 2.5)
        self.play(Write(summary), run_time=1)
        self.wait(1)
        
        self.play(
            FadeOut(title), FadeOut(line1), FadeOut(line2), FadeOut(line3),
            FadeOut(white_cell), FadeOut(antibody), FadeOut(summary),
            run_time=1
        )

    def create_defense_line_1(self):
        """第一道防线：皮肤"""
        wall = Rectangle(width=1.5, height=3, fill_color=BIO_GRAY, fill_opacity=0.5)
        label = Text("皮肤", font_size=NORMAL_SIZE, color=BIO_WHITE)
        number = Text("1", font_size=40, color=BIO_YELLOW, weight=BOLD)
        number.next_to(wall, UP, buff=0.2)
        label.next_to(wall, DOWN, buff=0.2)
        return VGroup(wall, label, number)

    def create_defense_line_2(self):
        """第二道防线：白细胞"""
        cells = VGroup(
            *[Circle(radius=0.25, fill_color=BIO_WHITE, fill_opacity=0.7)
              .shift(UP * i * 0.6) for i in range(-2, 3)]
        )
        label = Text("白细胞", font_size=NORMAL_SIZE, color=BIO_WHITE)
        number = Text("2", font_size=40, color=BIO_YELLOW, weight=BOLD)
        number.next_to(cells, UP, buff=0.2)
        label.next_to(cells, DOWN, buff=0.2)
        return VGroup(cells, label, number)

    def create_defense_line_3(self):
        """第三道防线：抗体"""
        antibodies = VGroup(
            *[self.create_antibody_symbol().scale(0.5).shift(UP * i * 0.8)
              for i in range(-2, 3)]
        )
        label = Text("抗体", font_size=NORMAL_SIZE, color=ANTIBODY_BLUE)
        number = Text("3", font_size=40, color=BIO_YELLOW, weight=BOLD)
        number.next_to(antibodies, UP, buff=0.2)
        label.next_to(antibodies, DOWN, buff=0.2)
        return VGroup(antibodies, label, number)

    def create_antibody_symbol(self):
        """创建Y形抗体符号"""
        stem = Line(DOWN * 0.3, ORIGIN, stroke_width=4, color=ANTIBODY_BLUE)
        left_arm = Line(ORIGIN, UP * 0.3 + LEFT * 0.2, stroke_width=4, color=ANTIBODY_BLUE)
        right_arm = Line(ORIGIN, UP * 0.3 + RIGHT * 0.2, stroke_width=4, color=ANTIBODY_BLUE)
        return VGroup(stem, left_arm, right_arm)

    def vaccine_principle(self):
        """疫苗原理 - 20秒"""
        title = Text("疫苗 = 军事演习", font_size=TITLE_SIZE, color=BIO_YELLOW, weight=BOLD)
        title.shift(UP * 2)
        self.play(Write(title), run_time=1)
        
        # 简单的类比动画
        # 左边：演习
        drill_label = Text("演习", font_size=SUBTITLE_SIZE, color=IMMUNE_GREEN)
        drill_label.move_to([-3, 0.5, 0])
        
        fake_enemy = Circle(radius=0.3, fill_color=VIRUS_RED, fill_opacity=0.3)
        fake_enemy.move_to([-3, -0.5, 0])
        fake_label = Text("假敌人", font_size=SMALL_SIZE, color=GRAY)
        fake_label.next_to(fake_enemy, DOWN)
        
        # 右边：实战
        battle_label = Text("实战", font_size=SUBTITLE_SIZE, color=VIRUS_RED)
        battle_label.move_to([3, 0.5, 0])
        
        real_enemy = Circle(radius=0.3, fill_color=VIRUS_RED, fill_opacity=1)
        real_enemy.move_to([3, -0.5, 0])
        real_label = Text("真敌人", font_size=SMALL_SIZE, color=VIRUS_RED)
        real_label.next_to(real_enemy, DOWN)
        
        # 中间：军队（免疫系统）
        army = VGroup(
            *[self.create_antibody_symbol().scale(0.7) for _ in range(5)]
        ).arrange(RIGHT, buff=0.2)
        army.move_to(ORIGIN)
        
        self.play(
            FadeIn(drill_label), FadeIn(fake_enemy), FadeIn(fake_label),
            run_time=1
        )
        self.play(FadeIn(army), run_time=0.5)
        self.wait(1)
        
        # 演习让军队有准备
        self.play(army.animate.set_color(IMMUNE_GREEN), run_time=0.5)
        
        self.play(
            FadeIn(battle_label), FadeIn(real_enemy), FadeIn(real_label),
            run_time=1
        )
        
        # 准备好的军队消灭真敌人
        self.play(
            army.animate.move_to([3, -0.5, 0]),
            run_time=1
        )
        self.play(
            FadeOut(real_enemy),
            Flash(army[2], color=IMMUNE_GREEN),
            run_time=0.5
        )
        
        # 核心信息
        key_message = Text(
            "提前认识，快速反应",
            font_size=SUBTITLE_SIZE,
            color=BIO_CYAN,
            weight=BOLD
        )
        key_message.shift(DOWN * 2.5)
        self.play(Write(key_message), run_time=1)
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(drill_label), FadeOut(fake_enemy), FadeOut(fake_label),
            FadeOut(battle_label), FadeOut(real_label), FadeOut(army), FadeOut(key_message),
            run_time=1
        )

    def practical_knowledge(self):
        """实用知识 - 15秒"""
        title = Text("记住3个数字", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.5)
        
        # 三个关键数字
        facts = VGroup()
        
        # 1. 抗体产生时间
        fact1 = VGroup(
            Text("14", font_size=60, color=IMMUNE_GREEN, weight=BOLD),
            Text("天", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("疫苗生效时间", font_size=SMALL_SIZE, color=GRAY)
        ).arrange(DOWN, buff=0.2)
        fact1.shift(LEFT * 4)
        
        # 2. 加强针间隔
        fact2 = VGroup(
            Text("6", font_size=60, color=BIO_YELLOW, weight=BOLD),
            Text("个月", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("加强针间隔", font_size=SMALL_SIZE, color=GRAY)
        ).arrange(DOWN, buff=0.2)
        fact2.move_to(ORIGIN)
        
        # 3. 群体免疫
        fact3 = VGroup(
            Text("70%", font_size=60, color=BIO_CYAN, weight=BOLD),
            Text("覆盖率", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("群体免疫", font_size=SMALL_SIZE, color=GRAY)
        ).arrange(DOWN, buff=0.2)
        fact3.shift(RIGHT * 4)
        
        facts.add(fact1, fact2, fact3)
        
        for fact in facts:
            self.play(FadeIn(fact, scale=0.8), run_time=0.8)
        
        self.wait(3)
        
        # 一句话总结
        conclusion = Text(
            "记住数字，科学防护",
            font_size=SUBTITLE_SIZE,
            color=BIO_PURPLE,
            weight=BOLD
        )
        conclusion.shift(DOWN * 2.5)
        self.play(Write(conclusion), run_time=1)
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(facts), FadeOut(conclusion),
            run_time=1
        )

    def show_ending(self):
        """结尾总结 - 10秒"""
        # 金句
        quote = VGroup(
            Text("免疫系统不是墙", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("是一支会学习的军队", font_size=TITLE_SIZE, color=IMMUNE_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(quote[0]), run_time=1)
        self.play(Write(quote[1]), run_time=1.5)
        self.wait(3)
        
        self.play(FadeOut(quote), run_time=1)
        
        # 下期预告
        preview = VGroup(
            Text("下期预告", font_size=NORMAL_SIZE, color=BIO_YELLOW),
            Text("第10集：生物钟的数学节律", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("为什么倒时差这么痛苦？", font_size=NORMAL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(preview[0]), run_time=0.5)
        self.play(Write(preview[1]), run_time=0.8)
        self.play(Write(preview[2]), run_time=0.7)
        self.wait(3)
        
        self.play(FadeOut(preview), run_time=1)