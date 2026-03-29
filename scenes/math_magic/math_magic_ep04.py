"""
数学之美系列 EP04 - 为什么减肥总失败？数学告诉你真相
60秒短视频 - 竖版友好（1080x1920 推荐）
"""

from manim import *
import numpy as np
import random


class WeightLossFormula(Scene):
    """EP04: 减脂曲线与行为策略

    设计目标：
    1) 保留前几集的品牌视觉风格（配色、CTA、粒子）
    2) 增强“深度感”：给出可验证的数学模型与参数含义
    3) 竖版友好：元素集中、字号更大、信息密度更高
    """

    def construct(self):
        # 全局风格
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#0A0E27"
        random.seed(7)
        np.random.seed(7)

        # 0-5秒：钩子
        self.show_hook()

        # 5-20秒：数学原理
        self.show_principle()

        # 20-40秒：可视化对比（线性幻想 vs 指数/逻辑斯谛现实）
        self.visualize_curves()

        # 40-50秒：可执行解决方案
        self.show_solution()

        # 50-60秒：品牌强化 + CTA
        self.show_ending()

    # ---------- 片段 1：钩子 ----------
    def show_hook(self):
        hook = VGroup(
            Text("是不是每次减肥都坚持不到两周？", font_size=60, color="#FF006E", weight=BOLD),
            Text("不是你不自律——", font_size=56, color=WHITE),
            Text("数学没告诉你曲线不是直线", font_size=56, color="#00F5FF")
        ).arrange(DOWN, buff=0.4)

        hook[0].set_stroke(color="#FF006E", width=3)
        hook[2].set_stroke(color="#00F5FF", width=3)

        self.play(Write(hook[0], run_time=0.8))
        self.play(Write(hook[1], run_time=0.5))
        self.play(Write(hook[2], run_time=0.8))
        self.wait(2.0)
        self.play(FadeOut(hook, scale=0.9))

    # ---------- 片段 2：数学原理 ----------
    def show_principle(self):
        title = Text("减脂并非直线：指数/逻辑斯谛曲线", font_size=42, color="#FFD60A", weight=BOLD)
        title.to_edge(UP, buff=0.3)
        title.set_stroke(color="#FFD60A", width=2)
        self.play(Write(title))

        # 体重变化常用模型（指数衰减到平台）- 竖版优化
        formula = MathTex(
            r"W(t) = W_{\infty} + (W_0 - W_{\infty}) e^{-kt}",
            font_size=48  # 减小字号适配竖版
        )
        formula.next_to(title, DOWN, buff=0.5)

        # 参数解释 - 竖版垂直排列
        facts = VGroup(
            VGroup(
                Text("W(t)", font_size=28, color="#06FFB4", weight=BOLD),
                Text("时间t时的体重", font_size=24, color="#06FFB4")
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("W∞", font_size=28, color="#00F5FF", weight=BOLD),
                Text("平台体重（代谢适应后）", font_size=24, color="#00F5FF")
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("k", font_size=28, color="#B388FF", weight=BOLD),
                Text("收敛速度（习惯/代谢/强度）", font_size=24, color="#B388FF")
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)  # 垂直排列避免重叠

        kcal = Text("事实：1 kg 脂肪≈7700 千卡", font_size=26, color="#FFD60A")

        # 竖版布局：垂直排列所有元素
        content = VGroup(formula, facts, kcal).arrange(DOWN, buff=0.6)
        content.next_to(title, DOWN, buff=0.4)
        
        # 确保内容适配屏幕宽度
        if content.width > 10:
            content.scale_to_fit_width(10)

        self.play(Write(formula), run_time=1.0)
        self.play(FadeIn(facts, shift=UP * 0.15), run_time=0.8)
        self.play(Write(kcal), run_time=0.5)
        self.wait(2)

        self.play(FadeOut(VGroup(content, title), shift=DOWN * 0.2))

    # ---------- 片段 3：可视化 ----------
    def visualize_curves(self):
        subtitle = Text("线性幻想 vs 现实曲线", font_size=36, color=WHITE, weight=BOLD)
        subtitle.to_edge(UP, buff=0.3)
        self.play(Write(subtitle))

        # 坐标轴（竖版优化）
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[55, 75, 5],
            x_length=7,  # 适配竖版宽度
            y_length=3.2,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 16},
        )
        
        # 图表居中放置
        axes.move_to(UP * 0.5)

        x_label = Text("周数", font_size=20).next_to(axes.x_axis, DOWN, buff=0.15)
        y_label = Text("体重(kg)", font_size=20).next_to(axes.y_axis, LEFT, buff=0.15).rotate(PI / 2)
        
        # 左图右字布局：图表在左侧
        chart_group = VGroup(axes, x_label, y_label)
        chart_group.shift(LEFT * 1.5)
        
        self.play(Create(axes))
        self.play(FadeIn(VGroup(x_label, y_label), shift=UP * 0.1))

        # 参数（示例）：初始72kg，平台60kg
        W0 = 72
        Winf = 60
        k = 0.25  # 收敛速度（越大越快接近平台）

        # 线性幻想（每周恒定-0.7kg）
        def w_linear(t):
            return W0 - 0.7 * t

        # 指数现实
        def w_exp(t):
            return Winf + (W0 - Winf) * np.exp(-k * t)

        curve_linear = axes.plot(lambda t: w_linear(t), color="#999999", stroke_width=3)
        curve_exp = axes.plot(lambda t: w_exp(t), color="#FF006E", stroke_width=4)

        # 右侧文字说明 - 垂直排列避免重叠
        legend_group = VGroup(
            VGroup(
                Dot(color="#999999", radius=0.08),
                Text("线性幻想", font_size=24, color="#999999")
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Dot(color="#FF006E", radius=0.08),
                Text("现实曲线", font_size=26, color="#FF006E", weight=BOLD)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                DashedLine(start=ORIGIN, end=RIGHT*0.4, color="#00F5FF", stroke_width=2),
                Text("平台体重", font_size=24, color="#00F5FF")
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        # 右侧放置文字说明
        legend_group.next_to(axes, RIGHT, buff=1.2)
        legend_group.shift(UP * 0.5)

        self.play(Create(curve_linear), run_time=0.8)
        self.play(Create(curve_exp), run_time=0.8)
        self.play(FadeIn(legend_group))

        # 移动点对比（强调"前快后慢"与平台）
        dot_linear = Dot(color="#999999", radius=0.06).move_to(axes.c2p(0, w_linear(0)))
        dot_exp = Dot(color="#FFD60A", radius=0.07).move_to(axes.c2p(0, w_exp(0)))

        self.play(FadeIn(dot_linear), FadeIn(dot_exp))
        for t in [3, 6, 9, 12]:
            self.play(
                dot_linear.animate.move_to(axes.c2p(t, w_linear(t))),
                dot_exp.animate.move_to(axes.c2p(t, w_exp(t))),
                run_time=0.6
            )

        # 平台虚线
        plateau = DashedLine(axes.c2p(0, Winf), axes.c2p(12, Winf), color="#00F5FF", stroke_width=2)
        self.play(Create(plateau))

        # 底部提示
        stall = Text("停滞≠失败：多是代谢与水重", font_size=26, color="#06FFB4")
        stall.shift(DOWN * 2.5)
        self.play(Write(stall))
        self.wait(3)

        self.play(
            FadeOut(VGroup(subtitle, chart_group, curve_linear, curve_exp,
                           legend_group, dot_linear, dot_exp, plateau, stall))
        )

    # ---------- 片段 4：解决方案 ----------
    def show_solution(self):
        title = Text("3步拿回体脂主导权", font_size=44, color="#06FFB4", weight=BOLD)
        title.to_edge(UP, buff=0.3)
        title.set_stroke(color="#06FFB4", width=2)
        self.play(Write(title))

        # 技巧1：温和缺口
        tip1_circle = Circle(radius=0.4, color="#FFD60A", stroke_width=3)
        tip1_num = Text("1", font_size=36, color="#FFD60A", weight=BOLD)
        tip1_num.move_to(tip1_circle.get_center())
        tip1_title = Text("温和缺口", font_size=28, color=WHITE, weight=BOLD)
        tip1_desc = Text("10%-20%热量缺口\n更可持续", font_size=22, color="#06FFB4")
        tip1_title.next_to(tip1_circle, DOWN, buff=0.3)
        tip1_desc.next_to(tip1_title, DOWN, buff=0.2)
        tip1 = VGroup(tip1_circle, tip1_num, tip1_title, tip1_desc)

        # 技巧2：提升NEAT
        tip2_circle = Circle(radius=0.4, color="#FFD60A", stroke_width=3)
        tip2_num = Text("2", font_size=36, color="#FFD60A", weight=BOLD)
        tip2_num.move_to(tip2_circle.get_center())
        tip2_title = Text("提升NEAT", font_size=28, color=WHITE, weight=BOLD)
        tip2_desc = Text("站立/步行/家务\n日常多动", font_size=22, color="#06FFB4")
        tip2_title.next_to(tip2_circle, DOWN, buff=0.3)
        tip2_desc.next_to(tip2_title, DOWN, buff=0.2)
        tip2 = VGroup(tip2_circle, tip2_num, tip2_title, tip2_desc)

        # 技巧3：破停滞策略
        tip3_circle = Circle(radius=0.4, color="#FFD60A", stroke_width=3)
        tip3_num = Text("3", font_size=36, color="#FFD60A", weight=BOLD)
        tip3_num.move_to(tip3_circle.get_center())
        tip3_title = Text("破停滞", font_size=28, color=WHITE, weight=BOLD)
        tip3_desc = Text("计划性维持/再激活\n睡眠>7h", font_size=22, color="#06FFB4")
        tip3_title.next_to(tip3_circle, DOWN, buff=0.3)
        tip3_desc.next_to(tip3_title, DOWN, buff=0.2)
        tip3 = VGroup(tip3_circle, tip3_num, tip3_title, tip3_desc)

        # 横向排列三个技巧
        tips = VGroup(tip1, tip2, tip3).arrange(RIGHT, buff=0.8)
        tips.next_to(title, DOWN, buff=0.8)
        
        # 确保内容适配屏幕宽度
        if tips.width > 10:
            tips.scale_to_fit_width(10)

        for i, tip in enumerate(tips):
            circle, num, t_title, t_desc = tip
            self.play(DrawBorderThenFill(circle), Write(num), run_time=0.3)
            self.play(FadeIn(t_title, shift=UP * 0.1), FadeIn(t_desc, shift=UP * 0.1),
                      circle.animate.scale(1.05), run_time=0.35)
            if i < len(tips) - 1:  # 不是最后一个时稍作停顿
                self.wait(0.2)

        self.wait(3)

        self.play(FadeOut(VGroup(title, tips)))

    # ---------- 片段 5：品牌 + CTA ----------
    def show_ending(self):
        brand_main = Text("数学之美", font_size=72, color="#FF006E", weight=BOLD)
        brand_sub = Text("Math Magic", font_size=42, color="#00F5FF", slant=ITALIC)
        brand = VGroup(brand_main, brand_sub).arrange(DOWN, buff=0.3)
        brand.set_stroke(width=3)

        cta_main = Text("关注我", font_size=48, color="#FFD60A", weight=BOLD)
        cta_sub = Text("用数学拿回身体主导权", font_size=36, color=WHITE)
        cta = VGroup(cta_main, cta_sub).arrange(DOWN, buff=0.3)
        cta.next_to(brand, DOWN, buff=1.0)

        particles = VGroup()
        for i in range(30):
            p = Dot(
                radius=0.08,
                color=random.choice(["#FF006E", "#00F5FF", "#FFD60A", "#06FFB4"]),
                fill_opacity=random.uniform(0.5, 1),
            )
            angle = (i / 30) * TAU
            radius = random.uniform(3.0, 5.0)
            p.move_to([radius * np.cos(angle), radius * np.sin(angle), 0])
            particles.add(p)

        self.play(Write(brand, run_time=1.0), FadeIn(particles, lag_ratio=0.1), run_time=1.5)
        self.play(Write(cta, run_time=0.8), brand.animate.scale(1.1),
                  Rotate(particles, angle=PI / 4, about_point=ORIGIN), run_time=1.3)
        self.play(cta_main.animate.set_color("#06FFB4").scale(1.18), rate_func=there_and_back, run_time=0.5)
        self.wait(2)


# Windows PowerShell 预览/生产命令（竖版1080x1920，60fps）
# 预览：
# manim -pql scenes\math_magic\math_magic_ep04.py WeightLossFormula
# 生产：
# manim -qh --resolution 1080,1920 --frame_rate 60 scenes\math_magic\math_magic_ep04.py WeightLossFormula


