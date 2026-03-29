"""
数学之美系列 EP01 - 为什么总是拖延？数学公式告诉你答案
60秒短视频 - 横屏版 1920x1080
"""

from manim import *
import numpy as np
import random

class ProcrastinationFormula(Scene):
    def construct(self):
        # 设置背景为深色
        self.camera.background_color = "#0A0E27"
        
        # ========== 0-5秒：钩子 - 制造共鸣 ==========
        # 痛点文字，横屏优化排版
        hook_text = VGroup(
            Text("明明知道很重要", font="Microsoft YaHei", font_size=64, color="#FF006E"),
            Text("为什么", font="Microsoft YaHei", font_size=72, color=WHITE, weight=BOLD),
            Text("总是拖到最后？", font="Microsoft YaHei", font_size=64, color="#00F5FF")
        ).arrange(DOWN, buff=0.4)
        
        # 添加发光效果
        hook_text[0].set_stroke(color="#FF006E", width=3)
        hook_text[1].set_stroke(color=WHITE, width=2)
        hook_text[2].set_stroke(color="#00F5FF", width=3)
        
        self.play(
            Write(hook_text[0], run_time=1),
            hook_text[0].animate.scale(1.1).set_color("#FF006E"),
        )
        self.play(Write(hook_text[1], run_time=0.5))
        self.play(
            Write(hook_text[2], run_time=1),
            hook_text[2].animate.scale(1.1).set_color("#00F5FF"),
        )
        self.wait(1)
        self.play(FadeOut(hook_text, scale=0.8))
        
        # ========== 5-20秒：揭秘 - 展示数学原理 ==========
        # 标题 - 放在顶部
        title = Text("拖延症的数学公式", font="Microsoft YaHei", font_size=48, color="#FFD60A", weight=BOLD)
        title.to_edge(UP, buff=0.4)
        title.set_stroke(color="#FFD60A", width=2)
        self.play(Write(title, run_time=1))
        
        # 公式展示 - 横屏中央偏上
        formula = MathTex(
            r"U", r"=", r"\frac{E \times V}{I \times D}",
            font_size=96
        )
        formula[0].set_color("#00F5FF")  # U
        formula[2].set_color(WHITE)
        formula.shift(UP*0.5)
        
        # 公式解释 - 横向排列，充分利用横屏空间
        explanations_top = VGroup(
            VGroup(
                Text("U", font="Microsoft YaHei", font_size=42, color="#00F5FF", weight=BOLD),
                Text("行动力", font="Microsoft YaHei", font_size=36, color="#00F5FF")
            ).arrange(DOWN, buff=0.15),
            
            VGroup(
                Text("E", font="Microsoft YaHei", font_size=42, color="#06FFB4", weight=BOLD),
                Text("期望值", font="Microsoft YaHei", font_size=36, color="#06FFB4")
            ).arrange(DOWN, buff=0.15),
            
            VGroup(
                Text("V", font="Microsoft YaHei", font_size=42, color="#06FFB4", weight=BOLD),
                Text("价值感", font="Microsoft YaHei", font_size=36, color="#06FFB4")
            ).arrange(DOWN, buff=0.15),
        ).arrange(RIGHT, buff=1.5)
        
        explanations_bottom = VGroup(
            VGroup(
                Text("I", font="Microsoft YaHei", font_size=42, color="#FF006E", weight=BOLD),
                Text("冲动性", font="Microsoft YaHei", font_size=36, color="#FF006E")
            ).arrange(DOWN, buff=0.15),
            
            VGroup(
                Text("D", font="Microsoft YaHei", font_size=42, color="#FF006E", weight=BOLD),
                Text("延迟时间", font="Microsoft YaHei", font_size=36, color="#FF006E")
            ).arrange(DOWN, buff=0.15)
        ).arrange(RIGHT, buff=2)
        
        explanations_top.next_to(formula, DOWN, buff=0.8)
        explanations_bottom.next_to(explanations_top, DOWN, buff=0.5)
        
        # 动态展示公式
        self.play(Write(formula, run_time=2))
        self.wait(0.5)
        
        # 展示解释 - 分组动画
        # 积极因素（分子）
        for exp in explanations_top:
            exp[0].set_stroke(color="#06FFB4", width=2)
            self.play(
                FadeIn(exp, shift=UP*0.2),
                exp.animate.scale(1.05),
                run_time=0.6
            )
        
        # 消极因素（分母）
        for exp in explanations_bottom:
            exp[0].set_stroke(color="#FF006E", width=2)
            self.play(
                FadeIn(exp, shift=DOWN*0.2),
                exp.animate.scale(1.05),
                run_time=0.6
            )
        
        self.wait(1)
        
        # ========== 20-40秒：可视化 - 动态演示 ==========
        # 清空画面，保留标题
        self.play(
            FadeOut(formula),
            FadeOut(explanations_top),
            FadeOut(explanations_bottom),
            title.animate.scale(0.9).to_edge(UP, buff=0.3)
        )
        
        # 创建对比展示 - 横屏左右布局
        left_group = VGroup()
        right_group = VGroup()
        
        # 左侧：DDL很远
        left_title = Text("DDL还很远", font="Microsoft YaHei", font_size=42, color="#FF006E")
        left_title.shift(LEFT*4 + UP*2)
        
        # 左侧公式计算 - 使用 Text 对象避免 LaTeX 中文问题
        left_calc = VGroup(
            Text("D = 30 天", font="Microsoft YaHei", font_size=36, color="#FF006E"),
            MathTex(r"U = \frac{50 \times 80}{30 \times 30}", font_size=36),
            Text("= 4.4", font="Microsoft YaHei", font_size=42, color="#FF006E", weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        left_calc.shift(LEFT*4)
        left_calc[2].set_stroke(color="#FF006E", width=2)
        
        # 左侧可视化 - 低能量条
        left_bar_bg = Rectangle(
            width=3, 
            height=0.3, 
            color="#333333", 
            fill_opacity=0.3,
            stroke_width=2
        )
        left_bar = Rectangle(
            width=0.3, 
            height=0.3, 
            color="#FF006E", 
            fill_opacity=0.8,
            stroke_width=0
        )
        left_bar.align_to(left_bar_bg, LEFT)
        left_bar_group = VGroup(left_bar_bg, left_bar).shift(LEFT*4 + DOWN*1.5)
        
        # 左侧能量值标签
        left_energy_label = Text("4.4", font="Microsoft YaHei", font_size=24, color="#FF006E")
        left_energy_label.next_to(left_bar, RIGHT, buff=0.2)
        
        left_group.add(left_title, left_calc, left_bar_group, left_energy_label)
        
        # 右侧：DDL临近
        right_title = Text("DDL前一天", font="Microsoft YaHei", font_size=42, color="#06FFB4")
        right_title.shift(RIGHT*4 + UP*2)
        
        # 右侧公式计算 - 使用 Text 对象
        right_calc = VGroup(
            Text("D = 1 天", font="Microsoft YaHei", font_size=36, color="#06FFB4"),
            MathTex(r"U = \frac{50 \times 80}{30 \times 1}", font_size=36),
            Text("= 133", font="Microsoft YaHei", font_size=42, color="#06FFB4", weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        right_calc.shift(RIGHT*4)
        right_calc[2].set_stroke(color="#06FFB4", width=2)
        
        # 右侧可视化 - 高能量条
        right_bar_bg = Rectangle(
            width=3, 
            height=0.3, 
            color="#333333", 
            fill_opacity=0.3,
            stroke_width=2
        )
        right_bar = Rectangle(
            width=2.8, 
            height=0.3, 
            color="#06FFB4", 
            fill_opacity=1,
            stroke_width=0
        )
        right_bar.align_to(right_bar_bg, LEFT)
        right_bar_group = VGroup(right_bar_bg, right_bar).shift(RIGHT*4 + DOWN*1.5)
        
        # 右侧能量值标签
        right_energy_label = Text("133", font="Microsoft YaHei", font_size=24, color="#06FFB4")
        right_energy_label.next_to(right_bar, RIGHT, buff=0.2)
        
        right_group.add(right_title, right_calc, right_bar_group, right_energy_label)
        
        # VS 标识
        vs_text = Text("VS", font="Microsoft YaHei", font_size=64, color="#FFD60A", weight=BOLD)
        vs_text.set_stroke(color="#FFD60A", width=3)
        
        # 动画展示对比
        self.play(
            Write(left_title),
            Write(right_title),
            Write(vs_text),
            run_time=1
        )
        
        self.play(
            FadeIn(left_calc, shift=UP*0.2),
            FadeIn(right_calc, shift=UP*0.2),
            run_time=1
        )
        
        self.play(
            Create(left_bar_bg),
            Create(right_bar_bg),
            run_time=0.5
        )
        
        self.play(
            GrowFromEdge(left_bar, LEFT),
            GrowFromEdge(right_bar, LEFT),
            FadeIn(left_energy_label),
            FadeIn(right_energy_label),
            run_time=1.5
        )
        
        # 强调差距
        diff_text = Text("30倍差距！", font="Microsoft YaHei", font_size=56, color="#FFD60A", weight=BOLD)
        diff_text.shift(DOWN*3)
        diff_text.set_stroke(color="#FFD60A", width=3)
        
        # 添加闪电效果连接两个能量条
        lightning = Line(
            left_bar_group.get_right() + UP*0.1,
            right_bar_group.get_left() + UP*0.1,
            color="#FFD60A",
            stroke_width=3
        )
        
        self.play(
            Create(lightning),
            Write(diff_text),
            diff_text.animate.scale(1.2),
            Flash(diff_text, color="#FFD60A", line_length=0.5),
            run_time=1
        )
        
        self.wait(1)
        
        # ========== 40-50秒：解决方案 - 实用技巧 ==========
        # 清空画面
        self.play(
            FadeOut(VGroup(
                left_group, right_group, vs_text, diff_text, lightning
            )),
            title.animate.move_to(UP*5)  # 移动到更远的位置，确保超出可视范围
        )
        
        # 解决方案标题
        solution_title = Text(
            "破解拖延的数学技巧", 
            font="Microsoft YaHei", 
            font_size=52, 
            color="#06FFB4", 
            weight=BOLD
        )
        solution_title.shift(UP*1.5)
        solution_title.set_stroke(color="#06FFB4", width=2)
        
        # 三个技巧 - 横向排列，更精细的布局
        tips = VGroup()
        
        # 技巧1
        tip1_circle = Circle(radius=0.5, color="#FFD60A", stroke_width=3)
        tip1_num = Text("1", font="Microsoft YaHei", font_size=48, color="#FFD60A", weight=BOLD)
        tip1_title = Text("提高价值感", font="Microsoft YaHei", font_size=32, color=WHITE)
        tip1_desc = Text("想象完成后\n的成就", font="Microsoft YaHei", font_size=24, color="#06FFB4")
        tip1_title.next_to(tip1_circle, DOWN, buff=0.8)
        tip1_desc.next_to(tip1_title, DOWN, buff=0.3)
        tip1 = VGroup(tip1_circle, tip1_num, tip1_title, tip1_desc)
        
        # 技巧2
        tip2_circle = Circle(radius=0.5, color="#FFD60A", stroke_width=3)
        tip2_num = Text("2", font="Microsoft YaHei", font_size=48, color="#FFD60A", weight=BOLD)
        tip2_title = Text("缩短延迟", font="Microsoft YaHei", font_size=32, color=WHITE)
        tip2_desc = Text("设置小目标\n截止日", font="Microsoft YaHei", font_size=24, color="#06FFB4")
        tip2_title.next_to(tip2_circle, DOWN, buff=0.8)
        tip2_desc.next_to(tip2_title, DOWN, buff=0.3)
        tip2 = VGroup(tip2_circle, tip2_num, tip2_title, tip2_desc)
        
        # 技巧3
        tip3_circle = Circle(radius=0.5, color="#FFD60A", stroke_width=3)
        tip3_num = Text("3", font="Microsoft YaHei", font_size=48, color="#FFD60A", weight=BOLD)
        tip3_title = Text("降低冲动", font="Microsoft YaHei", font_size=32, color=WHITE)
        tip3_desc = Text("远离\n干扰源", font="Microsoft YaHei", font_size=24, color="#06FFB4")
        tip3_title.next_to(tip3_circle, DOWN, buff=0.8)
        tip3_desc.next_to(tip3_title, DOWN, buff=0.3)
        tip3 = VGroup(tip3_circle, tip3_num, tip3_title, tip3_desc)
        
        tips = VGroup(tip1, tip2, tip3).arrange(RIGHT, buff=2.5)
        tips.shift(DOWN*0.5)
        
        self.play(Write(solution_title, run_time=1))
        
        # 逐个展示技巧，带有更好的动画
        for tip in tips:
            circle = tip[0]
            num = tip[1]
            title = tip[2]
            desc = tip[3]
            
            self.play(
                DrawBorderThenFill(circle),
                Write(num),
                run_time=0.5
            )
            self.play(
                FadeIn(title, shift=UP*0.2),
                FadeIn(desc, shift=UP*0.2),
                circle.animate.scale(1.1),
                run_time=0.5
            )
        
        self.wait(1)
        
        # ========== 50-60秒：品牌强化 + CTA ==========
        # 清空画面，确保标题完全消失
        self.play(
            FadeOut(VGroup(title, solution_title, tips)),
            run_time=1.0  # 增加淡出时间，确保用户能看到淡出效果
        )
        
        # 品牌标识 - 横屏中央
        brand_main = Text(
            "数学之美", 
            font="Microsoft YaHei", 
            font_size=72, 
            color="#FF006E", 
            weight=BOLD
        )
        brand_sub = Text(
            "Math Magic", 
            font="Microsoft YaHei", 
            font_size=42, 
            color="#00F5FF", 
            slant=ITALIC
        )
        brand = VGroup(brand_main, brand_sub).arrange(DOWN, buff=0.3)
        brand.set_stroke(width=3)
        
        # 关注引导
        cta_main = Text(
            "关注我", 
            font="Microsoft YaHei", 
            font_size=48, 
            color="#FFD60A", 
            weight=BOLD
        )
        cta_sub = Text(
            "用数学破解生活难题", 
            font="Microsoft YaHei", 
            font_size=36, 
            color=WHITE
        )
        cta = VGroup(cta_main, cta_sub).arrange(DOWN, buff=0.3)
        cta.next_to(brand, DOWN, buff=1.2)
        
        # 添加装饰元素 - 横屏分布
        particles = VGroup()
        for i in range(30):
            particle = Dot(
                radius=0.08,
                color=random.choice(["#FF006E", "#00F5FF", "#FFD60A", "#06FFB4"]),
                fill_opacity=random.uniform(0.5, 1)
            )
            # 围绕品牌标识分布
            angle = (i / 30) * TAU
            radius = random.uniform(3, 5)
            particle.move_to([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ])
            particles.add(particle)
        
        # 最终动画
        self.play(
            Write(brand, run_time=1),
            FadeIn(particles, lag_ratio=0.1),
            run_time=1.5
        )
        self.play(
            Write(cta, run_time=1),
            brand.animate.scale(1.1),
            Rotate(particles, angle=PI/4, about_point=ORIGIN),
            run_time=1.5
        )
        
        # 脉冲效果
        self.play(
            cta_main.animate.set_color("#06FFB4").scale(1.2),
            rate_func=there_and_back,
            run_time=0.5
        )
        
        self.wait(1)

# 测试命令：
# manim -pql math_magic_ep01.py ProcrastinationFormula
# 生产命令（横屏高清）：
# manim -qh --frame_rate 60 math_magic_ep01.py ProcrastinationFormula