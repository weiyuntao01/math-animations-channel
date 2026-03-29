"""
数学之美系列 EP02 - 为什么总买贵的？商家定价的数学陷阱
60秒短视频 - 横屏版 1920x1080
"""

from manim import *
import numpy as np
import random

class AnchoringEffect(Scene):
    def construct(self):
        # 设置背景为深色
        self.camera.background_color = "#0A0E27"
        
        # ========== 0-5秒：钩子 - 制造共鸣 ==========
        # 痛点文字，横屏优化排版
        hook_text = VGroup(
            Text("明明不需要", font="Microsoft YaHei", font_size=56, color="#FF006E"),
            Text("为什么", font="Microsoft YaHei", font_size=64, color=WHITE, weight=BOLD),
            Text("总买贵的？", font="Microsoft YaHei", font_size=56, color="#00F5FF")
        ).arrange(DOWN, buff=0.3)
        
        # 添加发光效果
        hook_text[0].set_stroke(color="#FF006E", width=2)
        hook_text[1].set_stroke(color=WHITE, width=2)
        hook_text[2].set_stroke(color="#00F5FF", width=2)
        
        self.play(
            Write(hook_text[0], run_time=1),
            hook_text[0].animate.scale(1.05).set_color("#FF006E"),
        )
        self.play(Write(hook_text[1], run_time=0.5))
        self.play(
            Write(hook_text[2], run_time=1),
            hook_text[2].animate.scale(1.05).set_color("#00F5FF"),
        )
        self.wait(1)
        self.play(FadeOut(hook_text, scale=0.8))
        
        # ========== 5-20秒：揭秘 - 展示数学原理 ==========
        # 标题 - 放在顶部
        title = Text("锚定效应的数学陷阱", font="Microsoft YaHei", font_size=42, color="#FFD60A", weight=BOLD)
        title.to_edge(UP, buff=0.3)
        title.set_stroke(color="#FFD60A", width=2)
        self.play(Write(title, run_time=1))
        
        # 公式展示 - 居中
        formula = MathTex(
            r"P_{perceived}", r"=", r"w \cdot P_{anchor}", r"+", r"(1-w) \cdot P_{actual}",
            font_size=64
        )
        formula[0].set_color("#00F5FF")  # P感知
        formula[2].set_color("#FF006E")  # 锚点价格
        formula[4].set_color("#06FFB4")  # 实际价格
        formula.shift(UP*0.5)
        
        # 公式解释 - 简化版本，确保在屏幕内
        explanations = VGroup(
            VGroup(
                Text("P感知", font="Microsoft YaHei", font_size=32, color="#00F5FF", weight=BOLD),
                Text("心理价格", font="Microsoft YaHei", font_size=26, color="#00F5FF")
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("P锚点", font="Microsoft YaHei", font_size=32, color="#FF006E", weight=BOLD),
                Text("高价锚点", font="Microsoft YaHei", font_size=26, color="#FF006E")
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("P实际", font="Microsoft YaHei", font_size=32, color="#06FFB4", weight=BOLD),
                Text("真实价值", font="Microsoft YaHei", font_size=26, color="#06FFB4")
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.5)
        
        explanations.next_to(formula, DOWN, buff=0.6)
        
        # 权重说明
        weight_text = Text(
            "w = 0.7 (锚点影响70%)", 
            font="Microsoft YaHei", 
            font_size=32, 
            color="#FFD60A",
            weight=BOLD
        )
        weight_text.next_to(explanations, DOWN, buff=0.4)
        weight_text.set_stroke(color="#FFD60A", width=1)
        
        # 动态展示公式
        self.play(Write(formula, run_time=2))
        self.wait(0.5)
        
        # 展示解释
        for exp in explanations:
            self.play(
                FadeIn(exp, shift=UP*0.1),
                exp.animate.scale(1.02),
                run_time=0.4
            )
        
        self.play(
            Write(weight_text),
            weight_text.animate.scale(1.05),
            run_time=1
        )
        
        self.wait(1)
        
        # ========== 20-40秒：可视化 - 动态演示 ==========
        # 清空画面，保留标题
        self.play(
            FadeOut(formula),
            FadeOut(explanations),
            FadeOut(weight_text),
            title.animate.scale(0.8).to_edge(UP, buff=0.2)
        )
        
        # 创建咖啡店场景
        scene_title = Text("咖啡店的价格陷阱", font="Microsoft YaHei", font_size=38, color=WHITE, weight=BOLD)
        scene_title.shift(UP*1.8)  # 稍微降低位置，避免过于接近屏幕边缘
        self.play(Write(scene_title))
        
        # 三个咖啡杯选项 - 确保在屏幕内
        # 小杯
        small_cup = VGroup()
        small_rect = RoundedRectangle(
            width=1.8, height=2.5, corner_radius=0.15,
            color="#666666", fill_opacity=0.2, stroke_width=2
        )
        small_icon = Text("☕", font_size=40)
        small_icon.move_to(small_rect.get_center() + UP*0.3)
        small_size = Text("小杯", font="Microsoft YaHei", font_size=28, color=WHITE)
        small_size.move_to(small_rect.get_center())
        small_price = Text("¥25", font="Microsoft YaHei", font_size=32, color="#06FFB4", weight=BOLD)
        small_price.move_to(small_rect.get_center() + DOWN*0.5)
        small_cup.add(small_rect, small_icon, small_size, small_price)
        small_cup.shift(LEFT*4.5)
        
        # 中杯（锚点）
        medium_cup = VGroup()
        medium_rect = RoundedRectangle(
            width=2.2, height=3, corner_radius=0.15,
            color="#FF006E", fill_opacity=0.3, stroke_width=3
        )
        medium_icon = Text("☕", font_size=52)
        medium_icon.move_to(medium_rect.get_center() + UP*0.4)
        medium_size = Text("中杯", font="Microsoft YaHei", font_size=32, color=WHITE, weight=BOLD)
        medium_size.move_to(medium_rect.get_center())
        medium_price_old = Text("¥45", font="Microsoft YaHei", font_size=28, color="#999999")
        medium_price_old.move_to(medium_rect.get_center() + DOWN*0.3)
        strike_line = Line(
            medium_price_old.get_left() + LEFT*0.1,
            medium_price_old.get_right() + RIGHT*0.1,
            color="#999999", stroke_width=2
        )
        medium_price_new = Text("¥35", font="Microsoft YaHei", font_size=38, color="#FFD60A", weight=BOLD)
        medium_price_new.move_to(medium_rect.get_center() + DOWN*0.7)
        medium_label = Text("最受欢迎", font="Microsoft YaHei", font_size=22, color="#FFD60A", weight=BOLD)
        medium_label.next_to(medium_rect, UP, buff=0.1)
        medium_label.set_stroke(color="#FFD60A", width=1)
        medium_cup.add(medium_rect, medium_icon, medium_size, medium_price_old, strike_line, medium_price_new, medium_label)
        medium_cup.shift(ORIGIN)
        
        # 大杯（极端锚点）
        large_cup = VGroup()
        large_rect = RoundedRectangle(
            width=1.8, height=2.5, corner_radius=0.15,
            color="#666666", fill_opacity=0.2, stroke_width=2
        )
        large_icon = Text("☕", font_size=44)
        large_icon.move_to(large_rect.get_center() + UP*0.3)
        large_size = Text("大杯", font="Microsoft YaHei", font_size=28, color=WHITE)
        large_size.move_to(large_rect.get_center())
        large_price = Text("¥65", font="Microsoft YaHei", font_size=32, color="#FF006E", weight=BOLD)
        large_price.move_to(large_rect.get_center() + DOWN*0.5)
        large_cup.add(large_rect, large_icon, large_size, large_price)
        large_cup.shift(RIGHT*4.5)
        
        # 整体下移
        coffee_group = VGroup(small_cup, medium_cup, large_cup)
        coffee_group.shift(DOWN*0.5)
        
        # 动画展示
        # 先展示极端锚点
        self.play(
            FadeIn(large_cup, shift=DOWN*0.2),
            Flash(large_price, color="#FF006E", line_length=0.3),
            run_time=1
        )
        
        # 大脑反应
        brain_reaction = Text("😱 太贵了！", font="Microsoft YaHei", font_size=32, color="#FF006E")
        brain_reaction.next_to(large_cup, RIGHT, buff=0.3)
        self.play(Write(brain_reaction), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(brain_reaction))
        
        # 展示其他选项
        self.play(
            FadeIn(medium_cup, shift=DOWN*0.2),
            FadeIn(small_cup, shift=DOWN*0.2),
            run_time=1
        )
        
        # 突出中杯
        self.play(
            medium_rect.animate.set_stroke(color="#FFD60A", width=4),
            medium_cup.animate.scale(1.05),
            Flash(medium_price_new, color="#FFD60A", line_length=0.4),
            run_time=1
        )
        
        # 显示选择统计
        stat_text = Text("73%的人选择中杯", font="Microsoft YaHei", font_size=42, color="#FFD60A", weight=BOLD)
        stat_text.shift(DOWN*2.5)
        stat_text.set_stroke(color="#FFD60A", width=2)
        
        # 添加短箭头
        arrow = Arrow(
            stat_text.get_top() + UP*0.05,
            medium_cup.get_bottom() + DOWN*0.05,
            color="#FFD60A",
            stroke_width=4,
            max_tip_length_to_length_ratio=0.15,
            buff=0
        )
        
        self.play(
            Write(stat_text),
            Create(arrow),
            run_time=1
        )
        
        # 揭示真相
        truth_text = Text("成本差：仅¥3", font="Microsoft YaHei", font_size=28, color="#06FFB4")
        truth_text.next_to(stat_text, DOWN, buff=0.2)
        self.play(Write(truth_text), run_time=1)
        
        self.wait(1)
        
        # ========== 40-50秒：解决方案 - 破解技巧 ==========
        # 清空画面，确保scene_title完全消失
        self.play(
            FadeOut(VGroup(
                scene_title, coffee_group, stat_text, arrow, truth_text
            )),
            title.animate.move_to(UP*5),  # 移动到更远的位置，确保超出可视范围
            run_time=1.2  # 增加时间确保FadeOut完全生效
        )
        
        # 解决方案标题
        solution_title = Text(
            "破解定价陷阱", 
            font="Microsoft YaHei", 
            font_size=44, 
            color="#06FFB4", 
            weight=BOLD
        )
        solution_title.shift(UP*1.8)
        solution_title.set_stroke(color="#06FFB4", width=2)
        
        # 三个技巧 - 紧凑排列
        tips = VGroup()
        
        # 技巧1
        tip1_circle = Circle(radius=0.4, color="#FFD60A", stroke_width=3)
        tip1_num = Text("1", font="Microsoft YaHei", font_size=40, color="#FFD60A", weight=BOLD)
        tip1_num.move_to(tip1_circle.get_center())
        tip1_title = Text("忽略极端", font="Microsoft YaHei", font_size=28, color=WHITE, weight=BOLD)
        tip1_desc = Text("无视最贵", font="Microsoft YaHei", font_size=22, color="#06FFB4")
        tip1_title.next_to(tip1_circle, DOWN, buff=0.4)
        tip1_desc.next_to(tip1_title, DOWN, buff=0.15)
        tip1 = VGroup(tip1_circle, tip1_num, tip1_title, tip1_desc)
        
        # 技巧2
        tip2_circle = Circle(radius=0.4, color="#FFD60A", stroke_width=3)
        tip2_num = Text("2", font="Microsoft YaHei", font_size=40, color="#FFD60A", weight=BOLD)
        tip2_num.move_to(tip2_circle.get_center())
        tip2_title = Text("独立判断", font="Microsoft YaHei", font_size=28, color=WHITE, weight=BOLD)
        tip2_desc = Text("想清需求", font="Microsoft YaHei", font_size=22, color="#06FFB4")
        tip2_title.next_to(tip2_circle, DOWN, buff=0.4)
        tip2_desc.next_to(tip2_title, DOWN, buff=0.15)
        tip2 = VGroup(tip2_circle, tip2_num, tip2_title, tip2_desc)
        
        # 技巧3
        tip3_circle = Circle(radius=0.4, color="#FFD60A", stroke_width=3)
        tip3_num = Text("3", font="Microsoft YaHei", font_size=40, color="#FFD60A", weight=BOLD)
        tip3_num.move_to(tip3_circle.get_center())
        tip3_title = Text("延迟决策", font="Microsoft YaHei", font_size=28, color=WHITE, weight=BOLD)
        tip3_desc = Text("冷静10秒", font="Microsoft YaHei", font_size=22, color="#06FFB4")
        tip3_title.next_to(tip3_circle, DOWN, buff=0.4)
        tip3_desc.next_to(tip3_title, DOWN, buff=0.15)
        tip3 = VGroup(tip3_circle, tip3_num, tip3_title, tip3_desc)
        
        tips = VGroup(tip1, tip2, tip3).arrange(RIGHT, buff=2)
        tips.shift(DOWN*0.5)
        
        self.play(Write(solution_title, run_time=1))
        
        # 逐个展示技巧
        for tip in tips:
            circle = tip[0]
            num = tip[1]
            title = tip[2]
            desc = tip[3]
            
            self.play(
                DrawBorderThenFill(circle),
                Write(num),
                run_time=0.4
            )
            self.play(
                FadeIn(title, shift=UP*0.1),
                FadeIn(desc, shift=UP*0.1),
                circle.animate.scale(1.05),
                run_time=0.4
            )
        
        self.wait(1)
        
        # ========== 50-60秒：品牌强化 + CTA ==========
        # 清空画面，确保所有标题完全消失（双重保险）
        self.play(
            FadeOut(VGroup(title, solution_title, tips)),
            run_time=1.0  # 增加淡出时间，确保用户能看到淡出效果
        )
        
        # 品牌标识 - 横屏中央（与EP01完全一致）
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
        
        # 关注引导（与EP01一致的格式）
        cta_main = Text(
            "关注我", 
            font="Microsoft YaHei", 
            font_size=48, 
            color="#FFD60A", 
            weight=BOLD
        )
        cta_sub = Text(
            "识破商家套路 理性消费", 
            font="Microsoft YaHei", 
            font_size=36, 
            color=WHITE
        )
        cta = VGroup(cta_main, cta_sub).arrange(DOWN, buff=0.3)
        cta.next_to(brand, DOWN, buff=1.2)
        
        # 添加装饰元素 - 横屏分布（与EP01一致，30个粒子）
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
        
        # 最终动画（与EP01完全一致）
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
# manim -pql math_magic_ep02.py AnchoringEffect
# 生产命令（横屏高清）：
# manim -qh --frame_rate 60 math_magic_ep02.py AnchoringEffect