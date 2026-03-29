"""
数学之美系列 EP03 - 为什么刷视频停不下来？上瘾的数学密码
60秒短视频 - 横屏版 1920x1080
完整版代码 - 包含所有修改
"""

from manim import *
import numpy as np
import random

class AddictionMechanism(Scene):
    def construct(self):
        # 设置背景为深色
        self.camera.background_color = "#0A0E27"
        
        # ========== 0-5秒：钩子 - 制造强烈共鸣 ==========
        # 痛点文字 - 更强烈的情感表达
        hook_text = VGroup(
            Text("刚想刷5分钟", font="Microsoft YaHei", font_size=60, color="#06FFB4"),
            Text("怎么就", font="Microsoft YaHei", font_size=72, color=WHITE, weight=BOLD),
            Text("2小时过去了？！", font="Microsoft YaHei", font_size=64, color="#FF006E")
        ).arrange(DOWN, buff=0.35)
        
        # 添加强烈的视觉效果
        hook_text[0].set_stroke(color="#06FFB4", width=3)
        hook_text[1].set_stroke(color=WHITE, width=2)
        hook_text[2].set_stroke(color="#FF006E", width=4)
        
        # 时钟图标快速旋转效果
        clock = Text("⏰", font_size=80)
        clock.next_to(hook_text[2], RIGHT, buff=0.3)
        
        self.play(
            Write(hook_text[0], run_time=0.8),
            hook_text[0].animate.scale(1.05),
        )
        self.play(Write(hook_text[1], run_time=0.5))
        self.play(
            Write(hook_text[2], run_time=0.8),
            FadeIn(clock),
            Rotate(clock, angle=2*PI, run_time=0.8),
            hook_text[2].animate.scale(1.1).set_color("#FF006E"),
        )
        self.wait(1.5)
        self.play(FadeOut(VGroup(hook_text, clock), scale=0.8))
        
        # ========== 5-20秒：揭秘 - 展示数学原理 ==========
        # 标题
        title = Text("上瘾的多巴胺公式", font="Microsoft YaHei", font_size=46, color="#FFD60A", weight=BOLD)
        title.to_edge(UP, buff=0.35)
        title.set_stroke(color="#FFD60A", width=2)
        self.play(Write(title, run_time=1))
        
        # 核心公式 - 更醒目
        formula = MathTex(
            r"D", r"=", r"\frac{k \times R}{P(R)}",
            font_size=88
        )
        formula[0].set_color("#FF006E")  # D - 多巴胺
        formula[2].set_color(WHITE)
        formula.shift(UP*0.5)
        
        # 公式解释 - 包含k的解释
        explanations = VGroup(
            VGroup(
                Text("D", font="Microsoft YaHei", font_size=42, color="#FF006E", weight=BOLD),
                Text("多巴胺", font="Microsoft YaHei", font_size=32, color="#FF006E")
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("k", font="Microsoft YaHei", font_size=42, color="#B388FF", weight=BOLD),
                Text("刺激强度", font="Microsoft YaHei", font_size=32, color="#B388FF")
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("R", font="Microsoft YaHei", font_size=42, color="#06FFB4", weight=BOLD),
                Text("奖励频率", font="Microsoft YaHei", font_size=32, color="#06FFB4")
            ).arrange(DOWN, buff=0.1),
            
            VGroup(
                Text("P(R)", font="Microsoft YaHei", font_size=42, color="#FFD60A", weight=BOLD),
                Text("可预测性", font="Microsoft YaHei", font_size=32, color="#FFD60A")
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.5)
        
        explanations.next_to(formula, DOWN, buff=0.7)
        
        # 关键洞察
        key_insight = Text(
            "关键：不确定性 = 上瘾", 
            font="Microsoft YaHei", 
            font_size=38, 
            color="#FF006E",
            weight=BOLD
        )
        key_insight.next_to(explanations, DOWN, buff=0.5)
        key_insight.set_stroke(color="#FF006E", width=2)
        
        # 动态展示
        self.play(Write(formula, run_time=1.5))
        self.wait(1.5)
        
        for exp in explanations:
            self.play(
                FadeIn(exp, shift=UP*0.15),
                exp.animate.scale(1.03),
                run_time=0.4
            )
        
        self.play(
            Write(key_insight),
            key_insight.animate.scale(1.08),
            Flash(key_insight, color="#FF006E", line_length=0.3),
            run_time=1
        )
        
        self.wait(2)
        
        # ========== 20-40秒：可视化 - 震撼对比 ==========
        # 清空画面
        self.play(
            FadeOut(formula),
            FadeOut(explanations),
            FadeOut(key_insight),
            title.animate.scale(0.85).to_edge(UP, buff=0.25)
        )
        
        # 创建对比场景
        scene_title = Text("多巴胺曲线对比", font="Microsoft YaHei", font_size=40, color=WHITE, weight=BOLD)
        scene_title.shift(UP*1.8)
        self.play(Write(scene_title))
        
        # 左侧：看书（可预测）
        left_title = Text("📚 看书", font="Microsoft YaHei", font_size=38, color="#666666")
        left_title.shift(LEFT*4.5 + UP*0.8)
        
        # 左侧多巴胺曲线 - 平稳
        left_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 20],
            x_length=4,
            y_length=2.5,
            axis_config={"color": "#333333"},
        ).shift(LEFT*4.5 + DOWN*0.8)
        
        left_curve = left_axes.plot(
            lambda x: 30 + 5*np.sin(x),
            color="#666666",
            stroke_width=3
        )
        
        left_label = Text("平均: 30", font="Microsoft YaHei", font_size=28, color="#666666", weight=BOLD)
        left_label.next_to(left_axes, DOWN, buff=0.2)
        
        # 右侧：刷视频（不可预测）
        right_title = Text("📱 刷视频", font="Microsoft YaHei", font_size=38, color="#FF006E")
        right_title.shift(RIGHT*4.5 + UP*0.8)
        
        # 右侧多巴胺曲线 - 峰值变化
        right_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 100, 20],
            x_length=4,
            y_length=2.5,
            axis_config={"color": "#333333"},
        ).shift(RIGHT*4.5 + DOWN*0.8)
        
        # 创建随机峰值
        def dopamine_spike(x):
            base = 20
            if 2 < x < 2.5:
                return base + 70  # 大峰值
            elif 4.5 < x < 5:
                return base + 60
            elif 7 < x < 7.5:
                return base + 75
            elif 9 < x < 9.5:
                return base + 65
            else:
                return base + 10*np.sin(3*x)
        
        right_curve = right_axes.plot(
            dopamine_spike,
            color="#FF006E",
            stroke_width=3
        )
        
        right_label = Text("峰值: 95!", font="Microsoft YaHei", font_size=28, color="#FF006E", weight=BOLD)
        right_label.next_to(right_axes, DOWN, buff=0.2)
        
        # VS标识
        vs_text = Text("VS", font="Microsoft YaHei", font_size=56, color="#FFD60A", weight=BOLD)
        vs_text.set_stroke(color="#FFD60A", width=3)
        
        # 动画展示
        self.play(
            Write(left_title),
            Write(right_title),
            Write(vs_text),
            run_time=0.8
        )
        
        self.play(
            Create(left_axes),
            Create(right_axes),
            run_time=0.5
        )
        
        self.play(
            Create(left_curve),
            Create(right_curve),
            FadeIn(left_label),
            FadeIn(right_label),
            run_time=1.5
        )
        
        # 强调差距 - 震撼数字
        diff_text = VGroup(
            Text("3倍峰值差距", font="Microsoft YaHei", font_size=48, color="#FFD60A", weight=BOLD),
            Text("大脑无法抗拒！", font="Microsoft YaHei", font_size=42, color="#FF006E", weight=BOLD)
        ).arrange(DOWN, buff=0.2)
        diff_text.shift(DOWN*1.8)
        diff_text.set_stroke(width=2)
        
        # 添加闪电连接效果
        lightning = Line(
            left_axes.get_right() + UP*0.5,
            right_axes.get_left() + UP*0.5,
            color="#FFD60A",
            stroke_width=4
        )
        
        self.play(
            Create(lightning),
            Write(diff_text[0]),
            diff_text[0].animate.scale(1.1),
            Flash(diff_text[0], color="#FFD60A", line_length=0.4),
            run_time=0.8
        )
        self.play(
            Write(diff_text[1]),
            diff_text[1].animate.scale(1.05),
            run_time=0.6
        )
        
        # 添加时间统计 - 增强紧迫感
        time_stat = Text(
            "平均每天4.8小时", 
            font="Microsoft YaHei", 
            font_size=32, 
            color="#FF006E"
        )
        time_stat.next_to(diff_text, DOWN, buff=0.2)
        self.play(FadeIn(time_stat, shift=UP*0.1), run_time=0.5)
        
        self.wait(2)
        
        # ========== 40-50秒：解决方案 - 实用技巧 ==========
        # 清空画面
        self.play(
            FadeOut(VGroup(
                scene_title, left_title, right_title, vs_text,
                left_axes, right_axes, left_curve, right_curve,
                left_label, right_label, diff_text, lightning, time_stat
            )),
            title.animate.move_to(UP*5)
        )
        
        # 解决方案标题
        solution_title = Text(
            "3步戒断刷视频上瘾", 
            font="Microsoft YaHei", 
            font_size=48, 
            color="#06FFB4", 
            weight=BOLD
        )
        solution_title.shift(UP*1.6)
        solution_title.set_stroke(color="#06FFB4", width=2)
        
        # 三个技巧 - 更具体可操作
        tips = VGroup()
        
        # 技巧1
        tip1_circle = Circle(radius=0.45, color="#FFD60A", stroke_width=3)
        tip1_num = Text("1", font="Microsoft YaHei", font_size=44, color="#FFD60A", weight=BOLD)
        tip1_num.move_to(tip1_circle.get_center())
        tip1_title = Text("设时间锁", font="Microsoft YaHei", font_size=30, color=WHITE, weight=BOLD)
        tip1_desc = Text("每30分钟\n强制休息", font="Microsoft YaHei", font_size=24, color="#06FFB4")
        tip1_title.next_to(tip1_circle, DOWN, buff=0.5)
        tip1_desc.next_to(tip1_title, DOWN, buff=0.2)
        tip1 = VGroup(tip1_circle, tip1_num, tip1_title, tip1_desc)
        
        # 技巧2 - 修改为关闭推送
        tip2_circle = Circle(radius=0.45, color="#FFD60A", stroke_width=3)
        tip2_num = Text("2", font="Microsoft YaHei", font_size=44, color="#FFD60A", weight=BOLD)
        tip2_num.move_to(tip2_circle.get_center())
        tip2_title = Text("关闭推送", font="Microsoft YaHei", font_size=30, color=WHITE, weight=BOLD)
        tip2_desc = Text("切断诱惑\n源头", font="Microsoft YaHei", font_size=24, color="#06FFB4")
        tip2_title.next_to(tip2_circle, DOWN, buff=0.5)
        tip2_desc.next_to(tip2_title, DOWN, buff=0.2)
        tip2 = VGroup(tip2_circle, tip2_num, tip2_title, tip2_desc)
        
        # 技巧3
        tip3_circle = Circle(radius=0.45, color="#FFD60A", stroke_width=3)
        tip3_num = Text("3", font="Microsoft YaHei", font_size=44, color="#FFD60A", weight=BOLD)
        tip3_num.move_to(tip3_circle.get_center())
        tip3_title = Text("替代奖励", font="Microsoft YaHei", font_size=30, color=WHITE, weight=BOLD)
        tip3_desc = Text("运动释放\n多巴胺", font="Microsoft YaHei", font_size=24, color="#06FFB4")
        tip3_title.next_to(tip3_circle, DOWN, buff=0.5)
        tip3_desc.next_to(tip3_title, DOWN, buff=0.2)
        tip3 = VGroup(tip3_circle, tip3_num, tip3_title, tip3_desc)
        
        tips = VGroup(tip1, tip2, tip3).arrange(RIGHT, buff=2.2)
        tips.shift(DOWN*0.3)
        
        self.play(Write(solution_title, run_time=0.8))
        
        # 快速展示技巧
        for i, tip in enumerate(tips):
            circle = tip[0]
            num = tip[1]
            title = tip[2]
            desc = tip[3]
            
            self.play(
                DrawBorderThenFill(circle),
                Write(num),
                run_time=0.3
            )
            self.play(
                FadeIn(title, shift=UP*0.1),
                FadeIn(desc, shift=UP*0.1),
                circle.animate.scale(1.05),
                run_time=0.35
            )
        
        self.wait(2)
        
        # ========== 50-60秒：品牌强化 + CTA ==========
        # 清空画面
        self.play(
            FadeOut(VGroup(title, solution_title, tips)),
            run_time=0.8
        )
        
        # 品牌标识 - 保持一致性
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
        
        # 关注引导 - 更强烈的号召
        cta_main = Text(
            "关注我", 
            font="Microsoft YaHei", 
            font_size=48, 
            color="#FFD60A", 
            weight=BOLD
        )
        cta_sub = Text(
            "夺回你的时间控制权", 
            font="Microsoft YaHei", 
            font_size=36, 
            color=WHITE
        )
        cta = VGroup(cta_main, cta_sub).arrange(DOWN, buff=0.3)
        cta.next_to(brand, DOWN, buff=1.2)
        
        # 添加装饰元素 - 30个粒子（保持品牌一致性）
        particles = VGroup()
        for i in range(30):
            particle = Dot(
                radius=0.08,
                color=random.choice(["#FF006E", "#00F5FF", "#FFD60A", "#06FFB4"]),
                fill_opacity=random.uniform(0.5, 1)
            )
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
        
        self.wait(2)

# 测试命令：
# manim -pql math_magic_ep03.py AddictionMechanism
# 生产命令（横屏高清）：
# manim -qh --frame_rate 60 math_magic_ep03.py AddictionMechanism