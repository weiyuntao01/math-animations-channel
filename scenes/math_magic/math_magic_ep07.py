"""
数学之美系列 EP07 - 遗忘曲线与间隔重复
为什么分手后还会想起TA？记忆的数学真相
6分钟深度科普
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple

# 品牌色彩系统
BRAND_PURPLE = "#8B5CF6"
BRAND_PINK = "#FF006E"
BRAND_BLUE = "#00F5FF"
BRAND_YELLOW = "#FFD60A"
BRAND_GREEN = "#06FFB4"
BRAND_RED = "#FF4444"
BRAND_GRAY = "#6B7280"
BRAND_DARK = "#0A0E27"

class ForgettingCurveEP07(Scene):
    """EP07: 遗忘曲线与间隔重复
    
    用真实的认知科学数学模型解释记忆机制
    包含艾宾浩斯曲线、间隔重复算法、情感记忆等核心概念
    """
    
    def construct(self):
        # 设置中文字体和背景
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BRAND_DARK
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场：初恋为什么忘不掉（30秒）
        self.show_opening()
        
        # 2. 遗忘曲线的数学形式（90秒）
        self.ebbinghaus_curve()
        
        # 3. 记忆强度的衰减模型（120秒）
        self.memory_decay_model()
        
        # 4. 间隔重复算法设计（90秒）
        self.spaced_repetition_algorithm()
        
        # 5. 情感记忆的特殊性（60秒）
        self.emotional_memory_special()
        
        # 6. 科学遗忘的方法（30秒）
        self.scientific_forgetting()
    
    def show_opening(self):
        """开场：初恋为什么忘不掉"""
        # 痛点展示
        hook = VGroup(
            Text("分手3年了", font_size=44, color=WHITE),
            Text("为什么还会梦到TA？", font_size=52, color=BRAND_PINK, weight=BOLD),
            Text("记忆并不随机", font_size=36, color=BRAND_YELLOW),
            Text("它遵循数学规律", font_size=48, color=BRAND_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(hook[0], run_time=0.5))
        self.wait(0.3)
        self.play(
            Write(hook[1], run_time=0.8),
            hook[1].animate.scale(1.05)
        )
        self.wait(0.5)
        self.play(Write(hook[2], run_time=0.5))
        self.play(
            Write(hook[3], run_time=0.6),
            hook[3].animate.set_color(BRAND_GREEN)
        )
        self.wait(1)
        
        self.play(FadeOut(hook, shift=UP))
    
    def ebbinghaus_curve(self):
        """遗忘曲线的数学形式"""
        # 标题
        title = Text("艾宾浩斯遗忘曲线", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 左侧：经典遗忘曲线
        left_group = VGroup()
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 100, 20],
            x_length=5,
            y_length=4,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "include_tip": True
            }
        )
        axes.shift(LEFT * 3.5)
        
        # 坐标轴标签
        x_label = Text("时间（天）", font_size=22)
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("记忆保留率（%）", font_size=22)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3).rotate(PI/2)
        
        # 遗忘曲线
        t = np.linspace(0, 7, 100)
        # 经典艾宾浩斯曲线
        retention = 100 * (0.21 + 0.79 * np.exp(-t/1.2))
        
        curve = axes.plot_line_graph(
            x_values=t,
            y_values=retention,
            line_color=BRAND_RED,
            stroke_width=3,
            add_vertex_dots=False
        )
        
        # 关键时间点标注
        time_points = [
            (0.014, "20分钟", 58),  # 20分钟后
            (1, "1天", 33),          # 1天后
            (7, "7天", 25)           # 7天后
        ]
        
        dots = VGroup()
        for time, label_text, retention_val in time_points:
            point = axes.c2p(time, retention_val)
            dot = Dot(point, radius=0.08, color=BRAND_YELLOW)
            label = Text(f"{label_text}: {retention_val}%", font_size=18, color=BRAND_YELLOW)
            label.next_to(dot, UR if time < 2 else RIGHT, buff=0.2)
            dots.add(VGroup(dot, label))
        
        left_group.add(axes, x_label, y_label, curve, dots)
        
        # 右侧：数学公式和解释
        right_group = VGroup()
        
        # 艾宾浩斯公式
        formula_title = Text("记忆衰减公式", font_size=26, color=BRAND_PURPLE, weight=BOLD)
        formula_title.shift(RIGHT * 3.5 + UP * 2)
        
        # 主公式
        main_formula = MathTex(
            r"R(t) = e^{-\frac{t}{S}}",
            font_size=44,
            color=BRAND_GREEN
        )
        main_formula.shift(RIGHT * 3.5 + UP * 1)
        
        # 参数解释
        params = VGroup(
            Text("R(t) = 记忆保留率", font_size=20),
            Text("t = 时间间隔", font_size=20),
            Text("S = 记忆强度", font_size=20, color=BRAND_YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        params.shift(RIGHT * 3.5)
        
        # 修正公式
        modified_title = Text("修正模型", font_size=22, color=BRAND_PINK)
        modified_title.shift(RIGHT * 3.5 + DOWN * 1.2)
        
        modified_formula = MathTex(
            r"R(t) = a + b \cdot e^{-\frac{t}{S}}",
            font_size=36
        )
        modified_formula.shift(RIGHT * 3.5 + DOWN * 2)
        
        modified_note = Text("a = 基础记忆, b = 可遗忘部分", font_size=18, color=BRAND_GRAY)
        modified_note.shift(RIGHT * 3.5 + DOWN * 2.7)
        
        right_group.add(formula_title, main_formula, params, 
                       modified_title, modified_formula, modified_note)
        
        # 动画展示
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(curve), run_time=1.5)
        
        for dot_group in dots:
            self.play(Create(dot_group[0]), Write(dot_group[1]), run_time=0.5)
        
        self.play(Write(formula_title))
        self.play(Write(main_formula))
        for param in params:
            self.play(Write(param), run_time=0.4)
        
        self.play(Write(modified_title))
        self.play(Write(modified_formula))
        self.play(Write(modified_note))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, left_group, right_group)))
    
    def memory_decay_model(self):
        """记忆强度的衰减模型"""
        # 标题
        title = Text("记忆强度的数学模型", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 上部分：记忆强度的多因素模型
        upper_section = VGroup()
        
        # 综合模型标题
        model_title = Text("记忆强度综合模型", font_size=28, color=BRAND_GREEN, weight=BOLD)
        model_title.shift(UP * 2.2)
        
        # 主方程
        strength_equation = MathTex(
            r"S(t) = S_0 \cdot f(n) \cdot g(i) \cdot h(e)",
            font_size=40
        )
        strength_equation.shift(UP * 1.3)
        
        # 因素解释 - 水平排列
        factors = VGroup()
        
        factor_data = [
            (r"S_0", "初始强度", BRAND_YELLOW),
            (r"f(n)", "重复次数", BRAND_BLUE),
            (r"g(i)", "间隔效应", BRAND_GREEN),
            (r"h(e)", "情感权重", BRAND_PINK)
        ]
        
        for i, (symbol, desc, color) in enumerate(factor_data):
            factor_group = VGroup(
                MathTex(symbol, font_size=32, color=color),
                Text(desc, font_size=20, color=color)
            ).arrange(DOWN, buff=0.15)
            factor_group.shift(LEFT * 4.5 + RIGHT * i * 3 + UP * 0.2)
            factors.add(factor_group)
        
        upper_section.add(model_title, strength_equation, factors)
        
        # 下部分：三种记忆类型的对比
        lower_section = VGroup()
        
        # 创建三个小坐标系展示不同类型记忆的衰减
        memory_types = VGroup()
        
        type_data = [
            ("普通信息", BRAND_GRAY, lambda t: np.exp(-t/0.5), LEFT * 5),
            ("重复学习", BRAND_BLUE, lambda t: np.exp(-t/2), ORIGIN),
            ("情感记忆", BRAND_PINK, lambda t: 0.3 + 0.7*np.exp(-t/5), RIGHT * 5)
        ]
        
        for name, color, func, position in type_data:
            # 小坐标系
            small_axes = Axes(
                x_range=[0, 10, 5],
                y_range=[0, 1, 0.5],
                x_length=2.5,
                y_length=1.8,
                axis_config={
                    "include_numbers": False,
                    "include_tip": False
                }
            )
            small_axes.shift(position + DOWN * 1.5)
            
            # 曲线
            t = np.linspace(0, 10, 50)
            y = func(t)
            
            curve = small_axes.plot_line_graph(
                x_values=t,
                y_values=y,
                line_color=color,
                stroke_width=2.5,
                add_vertex_dots=False
            )
            
            # 标题
            type_title = Text(name, font_size=22, color=color, weight=BOLD)
            type_title.next_to(small_axes, UP, buff=0.2)
            
            # 半衰期标注
            if name == "情感记忆":
                half_life = Text("半衰期: 5天", font_size=18, color=color)
            elif name == "重复学习":
                half_life = Text("半衰期: 2天", font_size=18, color=color)
            else:
                half_life = Text("半衰期: 0.5天", font_size=18, color=color)
            half_life.next_to(small_axes, DOWN, buff=0.2)
            
            memory_types.add(VGroup(small_axes, curve, type_title, half_life))
        
        lower_section.add(memory_types)
        
        # 底部：关键洞察
        insight = Text(
            "情感记忆的衰减速度是普通记忆的1/10",
            font_size=26,
            color=BRAND_PINK,
            weight=BOLD
        )
        insight.shift(DOWN * 3.2)
        
        # 动画展示
        self.play(Write(model_title))
        self.play(Write(strength_equation))
        
        for factor in factors:
            self.play(FadeIn(factor, shift=UP * 0.2), run_time=0.4)
        
        self.wait(0.5)
        
        for memory_type in memory_types:
            self.play(
                Create(memory_type[0]),  # axes
                Create(memory_type[1]),  # curve
                Write(memory_type[2]),   # title
                Write(memory_type[3]),   # half_life
                run_time=0.6
            )
        
        self.play(Write(insight))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, upper_section, lower_section, insight)))
    
    def spaced_repetition_algorithm(self):
        """间隔重复算法设计"""
        # 标题
        title = Text("间隔重复的最优算法", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 左侧：SuperMemo算法
        left_section = VGroup()
        
        algo_title = Text("SuperMemo 2算法", font_size=28, color=BRAND_GREEN, weight=BOLD)
        algo_title.shift(LEFT * 3.5 + UP * 2.2)
        
        # 核心公式
        sm2_formula = MathTex(
            r"I_n = \begin{cases} 1 & n = 1 \\ 6 & n = 2 \\ I_{n-1} \cdot EF & n > 2 \end{cases}",
            font_size=32
        )
        sm2_formula.shift(LEFT * 3.5 + UP * 1)
        
        # EF公式
        ef_formula = MathTex(
            r"EF' = EF + (0.1 - (5-q) \cdot (0.08 + (5-q) \cdot 0.02))",
            font_size=24
        )
        ef_formula.shift(LEFT * 3.5 + UP * 0.1)
        
        # 参数说明
        params = VGroup(
            Text("I = 复习间隔（天）", font_size=18),
            Text("EF = 简易因子（≥1.3）", font_size=18),
            Text("q = 回忆质量（0-5分）", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        params.shift(LEFT * 3.5 + DOWN * 0.8)
        
        # 间隔序列示例
        sequence_title = Text("最优间隔序列", font_size=22, color=BRAND_YELLOW)
        sequence_title.shift(LEFT * 3.5 + DOWN * 1.8)
        
        intervals = Text("1天 → 6天 → 15天 → 35天 → ...", font_size=20, color=WHITE)
        intervals.shift(LEFT * 3.5 + DOWN * 2.4)
        
        left_section.add(algo_title, sm2_formula, ef_formula, params, sequence_title, intervals)
        
        # 右侧：可视化展示
        right_section = VGroup()
        
        # 创建记忆强度随时间和复习的变化图
        viz_axes = Axes(
            x_range=[0, 60, 10],
            y_range=[0, 100, 20],
            x_length=5.5,
            y_length=4,
            axis_config={
                "include_numbers": True,
                "font_size": 18
            }
        )
        viz_axes.shift(RIGHT * 3.5 + DOWN * 0.5)
        
        # 坐标轴标签
        x_label = Text("时间（天）", font_size=20)
        x_label.next_to(viz_axes.x_axis, DOWN, buff=0.2)
        y_label = Text("记忆强度", font_size=20)
        y_label.next_to(viz_axes.y_axis, LEFT, buff=0.2).rotate(PI/2)
        
        # 复习点
        review_days = [1, 7, 22, 57]
        
        # 创建记忆曲线段
        curves = VGroup()
        dots = VGroup()
        
        current_strength = 100
        last_day = 0
        
        for i, review_day in enumerate(review_days):
            # 遗忘曲线段
            t = np.linspace(last_day, review_day, 50)
            # 使用不同的衰减率模拟间隔效应
            decay_rate = 1.5 * (1 + i * 0.5)  # 衰减越来越慢
            strength = current_strength * np.exp(-(t - last_day) / decay_rate)
            
            curve_segment = viz_axes.plot_line_graph(
                x_values=t,
                y_values=strength,
                line_color=BRAND_RED if i == 0 else BRAND_PINK,
                stroke_width=2.5,
                add_vertex_dots=False
            )
            curves.add(curve_segment)
            
            # 复习点
            review_point = viz_axes.c2p(review_day, strength[-1])
            dot = Dot(review_point, radius=0.08, color=BRAND_GREEN)
            
            # 复习后恢复
            restore_line = Line(
                review_point,
                viz_axes.c2p(review_day, min(100, strength[-1] + 30)),
                color=BRAND_GREEN,
                stroke_width=3
            )
            
            dots.add(VGroup(dot, restore_line))
            
            # 更新下一段的起始值
            current_strength = min(100, strength[-1] + 30)
            last_day = review_day
        
        # 图例
        legend = VGroup(
            VGroup(
                Line(ORIGIN, RIGHT * 0.3, color=BRAND_RED, stroke_width=2),
                Text("遗忘", font_size=16)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Line(ORIGIN, RIGHT * 0.3, color=BRAND_GREEN, stroke_width=2),
                Text("复习", font_size=16)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, buff=0.15)
        legend.shift(RIGHT * 5.5 + UP * 2.2)
        
        right_section.add(viz_axes, x_label, y_label, curves, dots, legend)
        
        # 动画展示
        self.play(Write(algo_title))
        self.play(Write(sm2_formula))
        self.play(Write(ef_formula))
        for param in params:
            self.play(Write(param), run_time=0.3)
        self.play(Write(sequence_title))
        self.play(Write(intervals))
        
        self.play(Create(viz_axes), Write(x_label), Write(y_label))
        
        # 逐段展示记忆曲线
        for i, (curve, dot_group) in enumerate(zip(curves, dots)):
            self.play(Create(curve), run_time=0.5)
            self.play(
                Create(dot_group[0]),  # 复习点
                Create(dot_group[1]),  # 恢复线
                run_time=0.3
            )
        
        self.play(FadeIn(legend))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, left_section, right_section)))
    
    def emotional_memory_special(self):
        """情感记忆的特殊性"""
        # 标题
        title = Text("为什么情感记忆如此持久", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 上部分：神经科学解释
        upper_section = VGroup()
        
        neuro_title = Text("杏仁核的调节作用", font_size=28, color=BRAND_PINK, weight=BOLD)
        neuro_title.shift(UP * 2.5)
        
        # 情感强度对记忆的影响公式
        emotion_formula = MathTex(
            r"S_{emotional} = S_{normal} \cdot (1 + \alpha \cdot E)",
            font_size=36
        )
        emotion_formula.shift(UP * 1.5)
        
        # 参数解释
        formula_params = VGroup(
            Text("E = 情感强度 (0-1)", font_size=20),
            MathTex(r"\alpha", font_size=20).set_color(BRAND_PINK),
            Text(" = 情感调节系数 (≈2-5)", font_size=20)
        ).arrange(RIGHT, buff=0.1)
        formula_params.shift(UP * 0.8)
        
        upper_section.add(neuro_title, emotion_formula, formula_params)
        
        # 中部分：对比展示
        middle_section = VGroup()
        
        # 创建对比图
        comparison_axes = Axes(
            x_range=[0, 365, 50],
            y_range=[0, 100, 20],
            x_length=8,
            y_length=3,
            axis_config={
                "include_numbers": True,
                "font_size": 16
            }
        )
        comparison_axes.shift(DOWN * 0.3)
        
        # 坐标轴标签
        x_label = Text("时间（天）", font_size=20)
        x_label.next_to(comparison_axes.x_axis, DOWN, buff=0.2)
        y_label = Text("记忆强度（%）", font_size=20)
        y_label.next_to(comparison_axes.y_axis, LEFT, buff=0.2).rotate(PI/2)
        
        # 三条曲线
        t = np.linspace(0, 365, 200)
        
        # 普通记忆（快速衰减）
        normal_memory = 100 * np.exp(-t/10)
        normal_curve = comparison_axes.plot_line_graph(
            x_values=t,
            y_values=normal_memory,
            line_color=BRAND_GRAY,
            stroke_width=2,
            add_vertex_dots=False
        )
        
        # 学习记忆（中等衰减）
        study_memory = 100 * np.exp(-t/50)
        study_curve = comparison_axes.plot_line_graph(
            x_values=t,
            y_values=study_memory,
            line_color=BRAND_BLUE,
            stroke_width=2,
            add_vertex_dots=False
        )
        
        # 情感记忆（缓慢衰减+基线）
        emotional_memory = 20 + 80 * np.exp(-t/200)
        emotional_curve = comparison_axes.plot_line_graph(
            x_values=t,
            y_values=emotional_memory,
            line_color=BRAND_PINK,
            stroke_width=3,
            add_vertex_dots=False
        )
        
        # 图例
        legend = VGroup(
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=BRAND_GRAY, stroke_width=2),
                Text("日常事件", font_size=18)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=BRAND_BLUE, stroke_width=2),
                Text("学习内容", font_size=18)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=BRAND_PINK, stroke_width=3),
                Text("情感记忆", font_size=18, color=BRAND_PINK, weight=BOLD)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, buff=0.15)
        legend.shift(RIGHT * 4.5 + UP * 1.2)
        
        middle_section.add(comparison_axes, x_label, y_label, 
                          normal_curve, study_curve, emotional_curve, legend)
        
        # 底部：关键发现
        findings = VGroup(
            Text("情感记忆特点：", font_size=24, color=BRAND_YELLOW),
            Text("• 衰减速度慢10倍", font_size=20),
            Text("• 存在永久基线（20%）", font_size=20),
            Text("• 闪光灯记忆效应", font_size=20, color=BRAND_PINK)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        findings.shift(LEFT * 3 + DOWN * 2.8)
        
        # 动画展示
        self.play(Write(neuro_title))
        self.play(Write(emotion_formula))
        self.play(Write(formula_params))
        
        self.play(Create(comparison_axes), Write(x_label), Write(y_label))
        self.play(Create(normal_curve), run_time=0.8)
        self.play(Create(study_curve), run_time=0.8)
        self.play(
            Create(emotional_curve),
            emotional_curve.animate.set_stroke(width=4),
            run_time=1
        )
        
        self.play(FadeIn(legend))
        
        for finding in findings:
            self.play(Write(finding), run_time=0.4)
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, upper_section, middle_section, findings)))
    
    def scientific_forgetting(self):
        """科学遗忘的方法"""
        # 标题
        title = Text("如何科学地忘记", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 策略展示
        strategies = VGroup()
        
        # 策略1：干扰理论
        strat1 = VGroup(
            Text("1. 主动干扰", font_size=28, color=BRAND_BLUE, weight=BOLD),
            Text("用新记忆覆盖旧记忆", font_size=22),
            MathTex(r"M_{new} > M_{old} \Rightarrow", font_size=24),
            Text("遗忘加速", font_size=22, color=BRAND_GREEN)
        ).arrange(DOWN, buff=0.2)
        strat1.shift(LEFT * 4 + UP * 1)
        
        # 策略2：情境改变
        strat2 = VGroup(
            Text("2. 情境隔离", font_size=28, color=BRAND_YELLOW, weight=BOLD),
            Text("改变环境线索", font_size=22),
            Text("减少提取触发", font_size=22, color=BRAND_GREEN)
        ).arrange(DOWN, buff=0.2)
        strat2.shift(UP * 1)
        
        # 策略3：认知重构
        strat3 = VGroup(
            Text("3. 认知重构", font_size=28, color=BRAND_PINK, weight=BOLD),
            Text("改变记忆意义", font_size=22),
            MathTex(r"E \downarrow \Rightarrow S \downarrow", font_size=24),
            Text("情感降级", font_size=22, color=BRAND_GREEN)
        ).arrange(DOWN, buff=0.2)
        strat3.shift(RIGHT * 4 + UP * 1)
        
        strategies.add(strat1, strat2, strat3)
        
        # 动画展示策略
        for strategy in strategies:
            self.play(FadeIn(strategy, shift=UP * 0.2), run_time=0.6)
        
        # 核心结论
        conclusion = VGroup(
            Text("记忆的数学真相：", font_size=32, color=WHITE),
            Text("遗忘不是bug，是feature", font_size=36, color=BRAND_GREEN, weight=BOLD),
            Text("理解规律，才能掌控记忆", font_size=28, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.3)
        conclusion.shift(DOWN * 1.5)
        
        self.play(Write(conclusion[0]))
        self.play(Write(conclusion[1]))
        self.play(Write(conclusion[2]))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, strategies, conclusion)))
        
        # 结束语
        self.show_conclusion()
    
    def show_conclusion(self):
        """展示结论"""
        # 核心洞察
        main_insight = VGroup(
            Text("为什么分手后还会想起TA？", font_size=36),
            Text("不是因为爱情特别", font_size=40, color=BRAND_YELLOW),
            Text("而是情感记忆的", font_size=44, color=BRAND_PINK),
            Text("数学规律在起作用", font_size=44, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(main_insight[0]))
        self.play(Write(main_insight[1]))
        self.play(
            Write(main_insight[2]),
            Write(main_insight[3]),
            main_insight[2].animate.scale(1.05),
            main_insight[3].animate.scale(1.05)
        )
        self.wait(2)
        
        self.play(FadeOut(main_insight))
        
        # 实用建议
        practical = VGroup(
            Text("记住三个数字：", font_size=32, color=BRAND_PURPLE),
            Text("20分钟 = 第一个复习点", font_size=26, color=BRAND_GREEN),
            Text("EF = 2.5 = 最优简易因子", font_size=26, color=BRAND_YELLOW),
            Text("10倍 = 情感vs普通记忆", font_size=26, color=BRAND_PINK)
        ).arrange(DOWN, buff=0.4)
        
        for line in practical:
            self.play(Write(line), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(practical))
        
        # 品牌结尾
        self.show_brand_ending()
    
    def show_brand_ending(self):
        """品牌结尾"""
        # 品牌标识
        brand_main = Text(
            "数学之美",
            font_size=64,
            color=BRAND_PINK,
            weight=BOLD
        )
        brand_sub = Text(
            "Math Magic",
            font_size=38,
            color=BRAND_BLUE,
            slant=ITALIC
        )
        brand = VGroup(brand_main, brand_sub).arrange(DOWN, buff=0.25)
        brand.set_stroke(width=3)
        
        # 本集信息
        episode_info = Text(
            "EP07: 遗忘曲线与间隔重复",
            font_size=28,
            color=WHITE
        )
        episode_info.next_to(brand, DOWN, buff=0.6)
        
        # 系列标语
        series_tagline = Text(
            "用真实的数学，理解真实的世界",
            font_size=32,
            color=BRAND_YELLOW
        )
        series_tagline.next_to(episode_info, DOWN, buff=0.4)
        
        
        # 装饰粒子效果
        particles = VGroup()
        for i in range(25):
            particle = Dot(
                radius=0.05,
                color=random.choice([BRAND_PINK, BRAND_BLUE, BRAND_YELLOW, BRAND_GREEN]),
                fill_opacity=random.uniform(0.5, 1)
            )
            angle = (i / 25) * TAU
            radius = random.uniform(2.5, 3.8)
            particle.move_to([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ])
            particles.add(particle)
        
        # 动画展示
        self.play(
            Write(brand, run_time=1),
            FadeIn(particles, lag_ratio=0.1),
            run_time=1.5
        )
        self.play(
            Write(episode_info),
            Write(series_tagline),
            Rotate(particles, angle=PI/8, about_point=ORIGIN),
            run_time=1.5
        )
        self.play(
            Rotate(particles, angle=-PI/16, about_point=ORIGIN),
            run_time=1
        )
        
        self.wait(3)

# 测试命令（低质量预览）：
# manim -pql -r 1920,1080 math_magic_ep07.py ForgettingCurveEP07

# 生产命令（高质量 60fps）：
# manim -pql  math_magic_ep07.py ForgettingCurveEP07