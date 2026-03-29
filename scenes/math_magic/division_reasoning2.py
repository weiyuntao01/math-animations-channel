"""
竖式除法填空题的数学思维讲解
Mathematical Thinking in Division Fill-in Problems
优化版：左图右文，横向布局，字体更大
"""

from manim import *
import numpy as np

# 颜色主题
THEME_PURPLE = "#8B5CF6"
THEME_GREEN = "#10B981"
THEME_RED = "#EF4444"
THEME_BLUE = "#3B82F6"
THEME_YELLOW = "#F59E0B"
THEME_GRAY = "#6B7280"
THEME_DARK = "#111827"

# 字体大小（增大）
TITLE_SIZE = 48
SUBTITLE_SIZE = 34
NORMAL_SIZE = 28
SMALL_SIZE = 24


class DivisionReasoningLesson(Scene):
    """竖式除法填空题的数学思维讲解"""
    
    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        
        self.show_intro()
        self.show_problem_with_image()
        self.show_simple_method()
        self.show_detailed_reasoning()
        self.mathematical_thinking_summary()
        self.show_ending()
    
    def show_intro(self):
        """开场介绍"""
        title = Text("竖式除法填空题", font_size=52, color=THEME_PURPLE, weight=BOLD)
        subtitle = Text("巧用余数规律的艺术", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(4)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_problem_with_image(self):
        """题目展示：分两页，左图右文"""
        self.clear()
        
        # ========== 第一页：左图 + 右边题目描述 ==========
        title = Text("竖式除法填空题", font_size=TITLE_SIZE, color=THEME_PURPLE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 左侧：原题图片
        image_loaded = False
        try:
            problem_image = ImageMobject("images/原题.png")
            problem_image.scale_to_fit_height(4)
            problem_image.shift(LEFT * 3.5 + DOWN * 0.3)
            self.play(FadeIn(problem_image))
            image_loaded = True
        except Exception:
            # 图片占位符
            image_placeholder = Rectangle(
                width=4, height=4,
                stroke_color=THEME_GREEN,
                stroke_width=3,
                fill_color=THEME_GREEN,
                fill_opacity=0.1
            )
            placeholder_text = Text("原题图片", font_size=NORMAL_SIZE, color=THEME_GREEN)
            image_group = VGroup(image_placeholder, placeholder_text)
            image_group.shift(LEFT * 3.5 + DOWN * 0.3)
            self.play(Create(image_placeholder), Write(placeholder_text))
            problem_image = image_group
        
        # 右侧：题目描述文字
        problem_text = VGroup(
            Text("被除数：2□2", font_size=32, color=THEME_YELLOW),
            Text("除数：23", font_size=32, color=THEME_BLUE),
            Text("商的末尾有0", font_size=28, color=THEME_GREEN),
            Text("求：□最小填多少？", font_size=28, color=WHITE),
            Text("    □最大填多少?", font_size=28, color=WHITE)
        )
        problem_text.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        problem_text.next_to(problem_image, RIGHT, buff=1.5, aligned_edge=UP)
        problem_text.shift(DOWN * 0.5)
        
        self.play(LaggedStart(*[Write(line) for line in problem_text], lag_ratio=0.3, run_time=2))
        self.wait(5)
        
        # 淡出题目描述，保留标题和图片
        self.play(FadeOut(problem_text))
        self.wait(1)
        
        # ========== 第二页：左图 + 右边关键观察 ==========
        # 右侧：关键观察分析
        analysis = VGroup(
            Text("关键观察", font_size=SUBTITLE_SIZE, color=THEME_YELLOW, weight=BOLD),
            Text("商末尾有0 意味着什么？", font_size=NORMAL_SIZE, color=WHITE),
            Text("↓", font_size=NORMAL_SIZE, color=THEME_BLUE),
            Text("最后一步除法不够除", font_size=NORMAL_SIZE, color=THEME_BLUE),
            Text("↓", font_size=NORMAL_SIZE, color=THEME_BLUE),
            Text("余数与2组合 < 23", font_size=NORMAL_SIZE, color=THEME_GREEN, weight=BOLD),
        )
        analysis.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        analysis.next_to(problem_image, RIGHT, buff=1.5, aligned_edge=UP)
        analysis.shift(DOWN * 0.5)
        
        self.play(LaggedStart(*[Write(line) for line in analysis], lag_ratio=0.3, run_time=2.5))
        self.wait(5)
        
        # 淡出所有内容
        self.play(FadeOut(title), FadeOut(problem_image), FadeOut(analysis))
    
    def show_simple_method(self):
        """展示简便方法：横向布局"""
        self.clear()
        
        title = Text("简便方法", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 核心思路（顶部居中）
        key_idea = Text(
            "核心思路：商末尾有0 → 余数×10+2 < 23",
            font_size=30,
            color=THEME_GREEN,
            weight=BOLD
        )
        key_idea.shift(UP * 2.2)
        self.play(Write(key_idea))
        
        # 推理步骤（横向三列布局）
        step1 = VGroup(
            Text("步骤1", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("2□ ÷ 23", font_size=SMALL_SIZE),
            Text("商只能是1", font_size=SMALL_SIZE),
            Text("(∵2□<46)", font_size=20, color=THEME_GRAY)
        ).arrange(DOWN, buff=0.2)
        
        step2 = VGroup(
            Text("步骤2", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("余数范围", font_size=SMALL_SIZE),
            Text("2□ - 23", font_size=SMALL_SIZE),
            Text("= 0到22", font_size=SMALL_SIZE, color=THEME_YELLOW)
        ).arrange(DOWN, buff=0.2)
        
        step3 = VGroup(
            Text("步骤3", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("关键约束", font_size=SMALL_SIZE),
            Text("余数×10+2<23", font_size=SMALL_SIZE),
            Text("余数<2.1", font_size=SMALL_SIZE, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.2)
        
        steps = VGroup(step1, step2, step3).arrange(RIGHT, buff=1.5)
        steps.shift(UP * 0.2)
        
        for step in steps:
            box = SurroundingRectangle(step, color=THEME_GRAY, corner_radius=0.15, buff=0.25)
            box.set_fill(color=THEME_DARK, opacity=0.2)
            self.play(Create(box), Write(step), run_time=1.3)
            self.wait(1.5)
        
        # 结论（底部）
        conclusion = VGroup(
            Text("余数只能是：0, 1, 2", font_size=NORMAL_SIZE, color=THEME_YELLOW),
            Text("所以 2□ = 23, 24, 25", font_size=NORMAL_SIZE, color=WHITE),
            Text("答案：□最小填3，最大填5", font_size=32, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.25)
        conclusion.to_edge(DOWN, buff=0.8)
        
        answer_box = SurroundingRectangle(conclusion[-1], color=THEME_GREEN, corner_radius=0.15, buff=0.2)
        
        self.play(Write(conclusion))
        self.play(Create(answer_box))
        self.wait(5)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def show_detailed_reasoning(self):
        """展示详细推理：横向三个验证框"""
        self.clear()
        
        title = Text("推理验证", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 三个验证框横向排列
        verify_3 = VGroup(
            Text("□=3", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("232÷23", font_size=SMALL_SIZE),
            Text("第一步:23÷23=1余0", font_size=20),
            Text("第二步:落下2得02", font_size=20),
            Text("02<23 商10 ✓", font_size=SMALL_SIZE, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.15)
        
        verify_4 = VGroup(
            Text("□=4", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("242÷23", font_size=SMALL_SIZE),
            Text("第一步:24÷23=1余1", font_size=20),
            Text("第二步:落下2得12", font_size=20),
            Text("12<23 商10 ✓", font_size=SMALL_SIZE, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.15)
        
        verify_5 = VGroup(
            Text("□=5", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("252÷23", font_size=SMALL_SIZE),
            Text("第一步:25÷23=1余2", font_size=20),
            Text("第二步:落下2得22", font_size=20),
            Text("22<23 商10 ✓", font_size=SMALL_SIZE, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.15)
        
        verifications = VGroup(verify_3, verify_4, verify_5).arrange(RIGHT, buff=1.0)
        verifications.shift(DOWN * 0.3)
        
        for i, verification in enumerate(verifications):
            box = SurroundingRectangle(verification, color=THEME_GREEN, corner_radius=0.15, buff=0.3)
            box.set_fill(color=THEME_DARK, opacity=0.15)
            
            self.play(Create(box), Write(verification), run_time=1.5)
            self.wait(1.5)
        
        # 最终结论
        final_conclusion = Text(
            "验证结果：□=3、4、5都满足，最小填3，最大填5",
            font_size=28,
            color=THEME_GREEN,
            weight=BOLD
        )
        final_conclusion.to_edge(DOWN, buff=0.5)
        self.play(Write(final_conclusion))
        
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def mathematical_thinking_summary(self):
        """数学思维总结：2x2网格"""
        self.clear()
        
        main_title = Text("数学思维精华", font_size=50, color=THEME_PURPLE, weight=BOLD)
        main_title.to_edge(UP, buff=0.3)
        self.play(Write(main_title))
        self.wait(1)
        
        # 四个思维（2x2布局）
        self.show_four_thinkings()
        
        self.final_summary()
    
    def show_four_thinkings(self):
        """展示四个思维（2x2网格）"""
        thinking1 = VGroup(
            Text("1. 条件分析", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("商末尾0 →", font_size=SMALL_SIZE),
            Text("最后不够除", font_size=SMALL_SIZE, color=THEME_GREEN)
        ).arrange(DOWN, buff=0.2)
        
        thinking2 = VGroup(
            Text("2. 余数思维", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("余数×10+2<23", font_size=SMALL_SIZE),
            Text("余数<2.1", font_size=SMALL_SIZE, color=THEME_GREEN)
        ).arrange(DOWN, buff=0.2)
        
        thinking3 = VGroup(
            Text("3. 试错验证", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("尝试所有可能", font_size=SMALL_SIZE),
            Text("找到满足条件的", font_size=SMALL_SIZE, color=THEME_GREEN)
        ).arrange(DOWN, buff=0.2)
        
        thinking4 = VGroup(
            Text("4. 规律总结", font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD),
            Text("通过余数范围", font_size=SMALL_SIZE),
            Text("反推填空数字", font_size=SMALL_SIZE, color=THEME_GREEN)
        ).arrange(DOWN, buff=0.2)
        
        thinkings = VGroup(thinking1, thinking2, thinking3, thinking4)
        thinkings.arrange_in_grid(2, 2, buff=(2, 1.2))
        thinkings.shift(DOWN * 0.3)
        
        for thinking in thinkings:
            box = SurroundingRectangle(thinking, color=THEME_GREEN, corner_radius=0.15, buff=0.3)
            box.set_fill(color=THEME_DARK, opacity=0.15)
            self.play(Create(box), Write(thinking), run_time=1)
            self.wait(1)
        
        self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
    def final_summary(self):
        """最终总结"""
        self.clear()
        
        title = Text("解题思维的深层价值", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        conclusion = VGroup(
            Text("简单的填空题", font_size=32, color=WHITE),
            Text("蕴含着深刻的数学思维", font_size=36, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        conclusion.center()
        
        self.play(Write(conclusion[0]))
        self.wait(1)
        self.play(Write(conclusion[1]), conclusion[1].animate.scale(1.08))
        
        self.wait(5)
        self.play(FadeOut(VGroup(title, conclusion)))
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        main_message = Text("数学思维，从简单题目开始", font_size=48, color=THEME_PURPLE, weight=BOLD)
        sub_message = Text("每一道题都值得深入思考", font_size=40, color=WHITE)
        sub_message.next_to(main_message, DOWN, buff=0.8)
        
        self.play(Write(main_message), run_time=2)
        self.play(Write(sub_message), run_time=1.5)
        self.wait(5)
        
        self.play(FadeOut(main_message), FadeOut(sub_message))
        
        thanks = Text("感谢观看", font_size=42, color=WHITE)
        self.play(Write(thanks))
        self.wait(3)
        self.play(FadeOut(thanks))