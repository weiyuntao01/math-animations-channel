"""
EP20: 本福特定律
自然数的秘密 - 第一数字定律
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple
from collections import Counter

# 概率系列颜色主题
PROB_PURPLE = "#8B5CF6"    # 主色：概率紫
PROB_GREEN = "#10B981"     # 成功绿
PROB_RED = "#EF4444"       # 失败红
PROB_BLUE = "#3B82F6"      # 数据蓝
PROB_YELLOW = "#F59E0B"    # 警告黄
PROB_GRAY = "#6B7280"      # 中性灰

# 字体大小调整
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class BenfordLawEP20(Scene):
    """本福特定律 - 概率论系列 EP20（特别篇）"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(20, "本福特定律")
        
        # 2. 神秘的发现
        self.mysterious_discovery()
        
        # 3. 本福特定律陈述
        self.state_benford_law()
        
        # 4. 真实数据验证
        self.real_data_verification()
        
        # 5. 数学原理解释
        self.mathematical_explanation()
        
        # 6. 斐波那契数列演示
        self.fibonacci_demonstration()
        
        # 7. 财务欺诈检测
        self.fraud_detection_application()
        
        # 8. 为什么有效？
        self.why_it_works()
        
        # 9. 结尾
        self.show_ending()
    
    def show_series_intro(self, episode_num: int, episode_title: str):
        """显示系列介绍动画"""
        # 系列标题
        series_title = Text(
            "概率论的反直觉世界",
            font_size=50,
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 特别篇标记
        special_mark = Text(
            "【特别篇】",
            font_size=28,
            color=PROB_YELLOW
        )
        special_mark.next_to(series_title, UP, buff=0.3)
        
        # 集数标题
        episode_text = Text(
            f"第{episode_num}集：{episode_title}",
            font_size=34,
            color=WHITE
        )
        episode_text.next_to(series_title, DOWN, buff=0.8)
        
        # 动画效果
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(special_mark, shift=DOWN), run_time=1)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(series_title), FadeOut(special_mark), FadeOut(episode_text))
    
    def mysterious_discovery(self):
        """神秘的发现"""
        self.clear()
        
        title = Text("1938年，一个物理学家的意外发现", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 故事叙述 - 调整布局避免重叠
        story = VGroup(
            Text("Frank Benford 翻阅对数表时发现：", font_size=NORMAL_SIZE),
            Text("前几页（1开头）磨损严重", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("后几页（9开头）几乎全新", font_size=NORMAL_SIZE, color=PROB_BLUE),
            Text("↓", font_size=36, color=PROB_RED),  # 减小箭头大小
            Text("难道1比9更常见？", font_size=28, color=PROB_GREEN, weight=BOLD)  # 减小字体
        ).arrange(DOWN, buff=0.5)  # 增加间距
        story.shift(DOWN * 0.5)
        
        for line in story:
            self.play(Write(line), run_time=0.7)
        
        self.wait(2)
        
        # 揭示
        revelation = Text(
            "这个发现改变了我们对数字的认知",
            font_size=SUBTITLE_SIZE,
            color=PROB_PURPLE
        )
        revelation.shift(DOWN * 2.8)
        self.play(Transform(story[-1], revelation))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(story))
    
    def state_benford_law(self):
        """陈述本福特定律"""
        self.clear()
        
        title = Text("本福特定律（第一数字定律）", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 定律公式
        formula = MathTex(
            r"P(d) = \log_{10}\left(1 + \frac{1}{d}\right)"
        ).scale(1.2)
        formula.shift(UP * 1.5)
        self.play(Write(formula))
        
        # 概率分布
        distribution = self.create_benford_distribution()
        distribution.shift(DOWN * 0.5)
        self.play(Create(distribution))
        
        # 关键洞察
        insight = Text(
            "1出现的概率是9的6倍！",
            font_size=SUBTITLE_SIZE,
            color=PROB_RED,
            weight=BOLD
        )
        insight.shift(DOWN * 3)
        self.play(Write(insight))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(formula), FadeOut(distribution), FadeOut(insight))
    
    def create_benford_distribution(self):
        """创建本福特分布图"""
        distribution = VGroup()
        
        # 计算本福特定律概率（数学精确值）
        # P(d) = log10(1 + 1/d)
        probabilities = []
        exact_values = [
            0.30103,  # log10(2) ≈ 0.30103
            0.17609,  # log10(3/2) ≈ 0.17609
            0.12494,  # log10(4/3) ≈ 0.12494
            0.09691,  # log10(5/4) ≈ 0.09691
            0.07918,  # log10(6/5) ≈ 0.07918
            0.06695,  # log10(7/6) ≈ 0.06695
            0.05799,  # log10(8/7) ≈ 0.05799
            0.05115,  # log10(9/8) ≈ 0.05115
            0.04576   # log10(10/9) ≈ 0.04576
        ]
        
        # 创建条形图
        bars = VGroup()
        labels = VGroup()
        values = VGroup()
        
        max_height = 2.5
        for i, p in enumerate(exact_values):
            # 条形
            bar = Rectangle(
                width=0.6,
                height=p * max_height / exact_values[0],
                fill_color=PROB_BLUE if i == 0 else PROB_GRAY,
                fill_opacity=0.7,
                stroke_color=WHITE,
                stroke_width=2
            )
            bar.shift(RIGHT * (i - 4) * 0.8)
            bar.align_to(DOWN * 1.5, DOWN)
            bars.add(bar)
            
            # 数字标签
            label = Text(str(i + 1), font_size=NORMAL_SIZE)
            label.next_to(bar, DOWN, buff=0.2)
            labels.add(label)
            
            # 概率值（百分比）
            value = Text(f"{p*100:.1f}%", font_size=SMALL_SIZE, color=PROB_YELLOW)
            value.next_to(bar, UP, buff=0.2)
            values.add(value)
        
        distribution.add(bars, labels, values)
        return distribution
    
    def real_data_verification(self):
        """真实数据验证"""
        self.clear()
        
        title = Text("本福特定律无处不在", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建多个数据源的验证
        data_sources = [
            ("人口数据", self.generate_population_data()),
            ("股票价格", self.generate_stock_data()),
            ("物理常数", self.generate_physical_constants()),
            ("河流长度", self.generate_river_lengths())
        ]
        
        # 创建所有mini charts但不重叠
        all_charts = VGroup()
        for i, (name, data) in enumerate(data_sources):
            chart = self.create_mini_distribution_fixed(name, data, i)
            all_charts.add(chart)
        
        # 按顺序展示
        for chart in all_charts:
            self.play(FadeIn(chart, shift=UP), run_time=0.5)
            self.wait(0.5)
        
        # 总结
        conclusion = Text(
            "都符合本福特定律！",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        conclusion.shift(DOWN * 2.5)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(all_charts), FadeOut(conclusion))
    
    def generate_population_data(self):
        """生成人口数据（模拟）"""
        populations = []
        for _ in range(200):  # 增加样本量
            # 使用对数正态分布模拟人口
            pop = int(np.exp(np.random.normal(12, 2)))
            populations.append(pop)
        return populations
    
    def generate_stock_data(self):
        """生成股票价格数据（模拟）"""
        prices = []
        for _ in range(200):  # 增加样本量
            # 模拟股票价格
            price = np.exp(np.random.normal(3, 1.5))
            prices.append(price)
        return prices
    
    def generate_physical_constants(self):
        """生成物理常数（真实值）"""
        constants = [
            3.14159,  # π
            2.71828,  # e
            6.626e-34,  # 普朗克常数
            9.8,  # 重力加速度
            3e8,  # 光速
            1.602e-19,  # 电子电荷
            6.022e23,  # 阿伏伽德罗常数
            1.381e-23,  # 玻尔兹曼常数
            8.314,  # 气体常数
            6.674e-11,  # 万有引力常数
        ]
        return constants * 15  # 重复以增加样本
    
    def generate_river_lengths(self):
        """生成河流长度数据（模拟）"""
        lengths = []
        for _ in range(200):  # 增加样本量
            # 模拟河流长度（公里）
            length = np.exp(np.random.normal(6, 1.5))
            lengths.append(length)
        return lengths
    
    def create_mini_distribution_fixed(self, name: str, data: List, index: int):
        """创建小型分布图（修复版）"""
        # 计算第一位数字分布
        first_digits = []
        for num in data:
            # 获取第一位非零数字
            num_str = str(abs(num))
            for digit in num_str:
                if digit != '0' and digit != '.':
                    first_digits.append(int(digit))
                    break
        
        # 统计分布
        counter = Counter(first_digits)
        
        chart = VGroup()
        
        # 标题
        title = Text(name, font_size=SMALL_SIZE, color=PROB_YELLOW)
        # 修复位置计算，使用2x2网格布局
        row = index // 2
        col = index % 2
        title.shift(UP * (1.5 - row * 2) + RIGHT * (col * 6 - 3))
        
        # 条形图
        bars = VGroup()
        total = sum(counter.values())
        
        for digit in range(1, 10):
            count = counter.get(digit, 0)
            proportion = count / total if total > 0 else 0
            
            bar = Rectangle(
                width=0.15,
                height=proportion * 2,
                fill_color=PROB_BLUE if digit == 1 else PROB_GRAY,
                fill_opacity=0.6
            )
            # 修复位置计算
            bar.shift(
                RIGHT * ((digit - 5) * 0.2 + (col * 6 - 3)) +
                UP * (0.5 - row * 2)
            )
            bar.align_to(UP * (0.5 - row * 2), DOWN)
            bars.add(bar)
        
        chart.add(title, bars)
        return chart
    
    def mathematical_explanation(self):
        """数学原理解释"""
        self.clear()
        
        title = Text("为什么是对数分布？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左图右文布局
        # 左侧：可视化
        visual_group = self.create_scale_invariance_visual()
        visual_group.scale(0.8)  # 缩小以留出更多空间
        visual_group.shift(LEFT * 3.5)
        
        # 右侧：文字解释 - 修复重叠问题
        explanation = VGroup()
        
        # 分组创建文字，确保不重叠
        line1 = Text("核心原理：", font_size=24, color=PROB_YELLOW)
        line2 = Text("尺度不变性", font_size=20, color=PROB_GREEN, weight=BOLD)
        line3 = MathTex(r"P(kx) = P(x)", font_size=28)
        
        line4 = Text("数学推导：", font_size=20, color=PROB_YELLOW)
        line5 = Text("对数尺度均匀分布", font_size=16)
        line6 = Text("→ 第一位数字概率", font_size=16)
        line7 = MathTex(r"P(d) = \log_{10}\left(1+\frac{1}{d}\right)", font_size=24)
        
        line8 = Text("唯一满足尺度不变的分布！", font_size=18, color=PROB_PURPLE, weight=BOLD)
        
        # 手动排列，确保间距合适
        line1.move_to(RIGHT * 3 + UP * 1.5)
        line2.move_to(RIGHT * 3 + UP * 1.0)
        line3.move_to(RIGHT * 3 + UP * 0.4)
        
        line4.move_to(RIGHT * 3 + DOWN * 0.3)
        line5.move_to(RIGHT * 3 + DOWN * 0.7)
        line6.move_to(RIGHT * 3 + DOWN * 1.1)
        line7.move_to(RIGHT * 3 + DOWN * 1.7)
        
        line8.move_to(RIGHT * 3 + DOWN * 2.5)
        
        explanation.add(line1, line2, line3, line4, line5, line6, line7, line8)
        
        # 动画展示
        self.play(Create(visual_group))
        self.play(Write(line1), Write(line2))
        self.play(Write(line3))
        self.wait(0.5)
        self.play(Write(line4))
        self.play(Write(line5), Write(line6))
        self.play(Write(line7))
        self.play(Write(line8))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(visual_group), FadeOut(explanation))
    
    def create_scale_invariance_visual(self):
        """创建尺度不变性可视化"""
        visual = VGroup()
        
        # 创建对数尺度图示
        # 线性尺度
        linear_line = Line(LEFT * 3, RIGHT * 3, color=PROB_BLUE)
        linear_label = Text("线性", font_size=SMALL_SIZE, color=PROB_BLUE)
        linear_label.next_to(linear_line, UP, buff=0.2)
        
        # 标记1-10的位置
        linear_marks = VGroup()
        for i in [1, 2, 5, 10]:
            pos = LEFT * 3 + RIGHT * 6 * (i-1)/9
            mark = Line(pos + UP * 0.1, pos + DOWN * 0.1, color=WHITE)
            label = Text(str(i), font_size=14)
            label.next_to(mark, DOWN, buff=0.1)
            linear_marks.add(mark, label)
        
        linear_group = VGroup(linear_line, linear_label, linear_marks)
        linear_group.shift(UP * 1.5)
        
        # 对数尺度
        log_line = Line(LEFT * 3, RIGHT * 3, color=PROB_GREEN)
        log_label = Text("对数", font_size=SMALL_SIZE, color=PROB_GREEN)
        log_label.next_to(log_line, UP, buff=0.2)
        
        # 标记1-10在对数尺度上的位置
        log_marks = VGroup()
        for i in [1, 2, 5, 10]:
            # 对数位置：log10(i) 在 [0, 1] 范围内
            log_pos = np.log10(i) if i > 0 else 0
            pos = LEFT * 3 + RIGHT * 6 * log_pos
            mark = Line(pos + UP * 0.1, pos + DOWN * 0.1, color=WHITE)
            label = Text(str(i), font_size=14)
            label.next_to(mark, DOWN, buff=0.1)
            log_marks.add(mark, label)
        
        log_group = VGroup(log_line, log_label, log_marks)
        log_group.shift(DOWN * 0.5)
        
        # 显示1-2区间的差异
        # 线性尺度上1-2的距离
        linear_bracket = BraceBetweenPoints(
            LEFT * 3 + UP * 1.3,
            LEFT * 3 + RIGHT * 0.67 + UP * 1.3,
            direction=UP,
            color=PROB_YELLOW
        )
        linear_dist = Text("11%", font_size=14, color=PROB_YELLOW)
        linear_dist.next_to(linear_bracket, UP, buff=0.1)
        
        # 对数尺度上1-2的距离
        log_bracket = BraceBetweenPoints(
            LEFT * 3 + DOWN * 0.7,
            LEFT * 3 + RIGHT * 1.8 + DOWN * 0.7,  # log10(2) ≈ 0.301
            direction=DOWN,
            color=PROB_YELLOW
        )
        log_dist = Text("30%", font_size=14, color=PROB_YELLOW)
        log_dist.next_to(log_bracket, DOWN, buff=0.1)
        
        visual.add(
            linear_group, log_group,
            linear_bracket, linear_dist,
            log_bracket, log_dist
        )
        
        return visual
    
    def visualize_logarithmic_scale(self):
        """可视化对数尺度（独立页面）"""
        self.clear()
        
        title = Text("对数尺度的秘密", font_size=SUBTITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建数轴对比
        axes_group = self.create_dual_axes()
        axes_group.shift(UP * 0.5)
        self.play(Create(axes_group))
        
        # 显示映射关系
        mappings = self.create_mappings()
        self.play(Create(mappings))
        
        # 关键洞察
        insight = Text(
            "在对数尺度上均匀分布 → 第一位数字服从本福特定律",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        insight.shift(DOWN * 3)
        self.play(Write(insight))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(axes_group), FadeOut(mappings), FadeOut(insight))
    
    def create_dual_axes(self):
        """创建双数轴对比"""
        axes = VGroup()
        
        # 线性数轴
        linear_axis = NumberLine(
            x_range=[1, 100, 10],
            length=10,
            include_numbers=False,
            color=PROB_BLUE
        )
        linear_axis.shift(UP * 1.5)
        
        # 添加关键数字标签
        linear_labels = VGroup()
        for num in [1, 10, 20, 50, 100]:
            label = Text(str(num), font_size=14)
            label.next_to(linear_axis.n2p(num), DOWN, buff=0.1)
            linear_labels.add(label)
        
        linear_title = Text("线性尺度", font_size=SMALL_SIZE, color=PROB_BLUE)
        linear_title.next_to(linear_axis, UP, buff=0.3)
        
        # 对数数轴
        log_axis = NumberLine(
            x_range=[0, 2, 0.2],
            length=10,
            include_numbers=False,
            color=PROB_GREEN
        )
        log_axis.shift(DOWN * 1.5)
        
        # 添加对数标签
        log_labels = VGroup()
        for num in [1, 2, 5, 10, 20, 50, 100]:
            if num <= 100:
                log_val = np.log10(num)
                label = Text(str(num), font_size=14)
                label.next_to(log_axis.n2p(log_val), DOWN, buff=0.1)
                log_labels.add(label)
        
        log_title = Text("对数尺度", font_size=SMALL_SIZE, color=PROB_GREEN)
        log_title.next_to(log_axis, UP, buff=0.3)
        
        axes.add(
            linear_axis, linear_labels, linear_title,
            log_axis, log_labels, log_title
        )
        
        return axes
    
    def create_mappings(self):
        """创建映射关系线"""
        mappings = VGroup()
        
        # 创建关键数字的映射线
        for num in [1, 2, 10, 20, 100]:
            # 线性位置
            linear_y = 2.5
            linear_x = -5 + 10 * (num - 1) / 99
            
            # 对数位置
            log_y = -2.5
            log_x = -5 + 5 * np.log10(num)
            
            line = DashedLine(
                np.array([linear_x, linear_y, 0]),
                np.array([log_x, log_y, 0]),
                color=PROB_YELLOW if num < 10 else PROB_GRAY,
                stroke_width=2 if num < 10 else 1
            )
            mappings.add(line)
        
        return mappings
    
    def fibonacci_demonstration(self):
        """斐波那契数列演示"""
        self.clear()
        
        title = Text("斐波那契数列完美符合", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 生成更多斐波那契数
        fib = [1, 1]
        for _ in range(100):  # 增加到100个数
            fib.append(fib[-1] + fib[-2])
        
        # 统计第一位数字
        first_digits = []
        for num in fib:
            first_digit = int(str(num)[0])
            first_digits.append(first_digit)
        
        # 创建分布对比
        self.create_fibonacci_comparison(first_digits)
        
        self.wait(3)
        self.play(FadeOut(title))
    
    def create_fibonacci_comparison(self, first_digits: List[int]):
        """创建斐波那契对比图"""
        # 统计分布
        counter = Counter(first_digits)
        total = len(first_digits)
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 0.35, 0.05],
            x_length=8,
            y_length=4,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 16
            }
        )
        axes.shift(DOWN * 0.5)
        
        x_label = Text("第一位数字", font_size=SMALL_SIZE)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("概率", font_size=SMALL_SIZE)
        y_label.next_to(axes.y_axis, LEFT).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 实际分布（条形图）
        bars = VGroup()
        for digit in range(1, 10):
            count = counter.get(digit, 0)
            proportion = count / total
            
            bar = Rectangle(
                width=0.5,
                height=proportion * 11.4,  # 缩放到坐标系
                fill_color=PROB_BLUE,
                fill_opacity=0.6,
                stroke_width=1
            )
            bar.move_to(axes.c2p(digit, proportion/2))
            bars.add(bar)
        
        self.play(Create(bars))
        
        # 理论曲线（本福特定律）- 使用正确的API
        x_vals = np.linspace(1, 9, 100)
        y_vals = [np.log10(1 + 1/d) for d in x_vals]
        
        theory_curve = axes.plot(
            lambda x: np.log10(1 + 1/x),
            x_range=[1, 9],
            color=PROB_RED,
            stroke_width=3
        )
        
        self.play(Create(theory_curve))
        
        # 图例
        legend = VGroup(
            VGroup(
                Square(side_length=0.2, fill_color=PROB_BLUE, fill_opacity=0.6),
                Text("斐波那契", font_size=16)
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Line(LEFT * 0.2, RIGHT * 0.2, color=PROB_RED, stroke_width=3),
                Text("本福特定律", font_size=16)
            ).arrange(RIGHT, buff=0.1)
        ).arrange(DOWN, buff=0.2)
        legend.shift(UP * 2 + RIGHT * 3)
        
        self.play(Create(legend))
        
        # 匹配度
        match_text = Text(
            "几乎完美匹配！",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        match_text.shift(DOWN * 3)
        self.play(Write(match_text))
        
        self.wait(2)
        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(bars), FadeOut(theory_curve), FadeOut(legend),
            FadeOut(match_text)
        )
    
    def fraud_detection_application(self):
        """财务欺诈检测应用"""
        self.clear()
        
        title = Text("应用：识破财务造假", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建两组数据对比
        real_data = self.create_financial_data("真实账目", PROB_GREEN, True)
        fake_data = self.create_financial_data("伪造账目", PROB_RED, False)
        
        real_data.shift(LEFT * 3.5)
        fake_data.shift(RIGHT * 3.5)
        
        self.play(Create(real_data), Create(fake_data))
        
        # 检测结果
        detection = VGroup(
            Text("🔍 检测结果：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("✓ 真实数据符合本福特定律", font_size=NORMAL_SIZE, color=PROB_GREEN),
            Text("✗ 伪造数据偏离本福特定律", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("准确率高达95%！", font_size=NORMAL_SIZE, color=PROB_PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        detection.shift(DOWN * 2)
        
        for line in detection:
            self.play(Write(line), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(real_data), FadeOut(fake_data), FadeOut(detection))
    
    def create_financial_data(self, title: str, color, is_real: bool):
        """创建财务数据图表"""
        chart = VGroup()
        
        # 标题
        title_text = Text(title, font_size=NORMAL_SIZE, color=color)
        title_text.shift(UP * 2)
        
        # 生成分布
        bars = VGroup()
        for digit in range(1, 10):
            if is_real:
                # 真实数据符合本福特定律
                height = np.log10(1 + 1/digit) * 3
            else:
                # 伪造数据趋向均匀分布
                height = 0.3 + random.uniform(-0.05, 0.05)
            
            bar = Rectangle(
                width=0.25,
                height=height,
                fill_color=color,
                fill_opacity=0.6,
                stroke_width=1
            )
            bar.shift(RIGHT * (digit - 5) * 0.3)
            bar.align_to(DOWN * 0.5, DOWN)
            bars.add(bar)
        
        # 数字标签
        labels = VGroup()
        for digit in range(1, 10):
            label = Text(str(digit), font_size=14)
            label.shift(RIGHT * (digit - 5) * 0.3 + DOWN * 1)
            labels.add(label)
        
        chart.add(title_text, bars, labels)
        return chart
    
    def why_it_works(self):
        """为什么有效？"""
        self.clear()
        
        title = Text("本福特定律为什么如此普遍？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 三个原因
        reasons = VGroup(
            Text("原因一：自然增长是指数的", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("人口、股价、细菌...都是倍数增长", font_size=NORMAL_SIZE),
            Text("原因二：数据跨越多个数量级", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("从几十到几百万的数据集", font_size=NORMAL_SIZE),
            Text("原因三：乘法过程的结果", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("多个随机变量相乘的分布", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        reasons.shift(UP * 0.5)
        
        for i in range(0, 6, 2):
            self.play(
                Write(reasons[i]),
                Write(reasons[i+1]),
                run_time=0.8
            )
        
        # 核心洞察
        insight = Text(
            "世界是按比例而非按差值运行的",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        insight.shift(DOWN * 2.5)
        self.play(Write(insight))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(reasons), FadeOut(insight))
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        # 核心总结
        summary = VGroup(
            Text("本福特定律揭示：", font_size=38, color=WHITE),
            Text("自然界有偏好", font_size=TITLE_SIZE, color=PROB_PURPLE, weight=BOLD),
            Text("1真的比9重要", font_size=34, color=PROB_YELLOW),
            Text("这不是巧合，是数学！", font_size=34, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.play(Write(summary[3]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 实用应用
        applications = VGroup(
            Text("实际应用：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("✓ 审计财务报表", font_size=NORMAL_SIZE),
            Text("✓ 检测选举舞弊", font_size=NORMAL_SIZE),
            Text("✓ 验证科学数据", font_size=NORMAL_SIZE),
            Text("✓ 识别税务欺诈", font_size=NORMAL_SIZE, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        for app in applications:
            self.play(Write(app), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(applications))
        
        # 系列结尾
        self.show_series_ending(
            "数字的指纹",
            "真相藏在分布中"
        )
    
    def show_series_ending(self, main_message: str, sub_message: str):
        """显示系列结尾动画"""
        # 主信息
        main_text = Text(
            main_message,
            font_size=50,
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 副信息
        sub_text = Text(
            sub_message,
            font_size=30,
            color=WHITE
        )
        sub_text.next_to(main_text, DOWN, buff=0.8)
        
        # 动画
        self.play(Write(main_text), run_time=2)
        self.play(Write(sub_text), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(main_text), FadeOut(sub_text))
        
        # 下期预告
        self.show_next_episode_preview()
    
    def show_next_episode_preview(self):
        """下期预告"""
        # 预告标题
        preview_title = Text("系列终章预告", font_size=38, color=PROB_YELLOW)
        preview_title.to_edge(UP)
        self.play(Write(preview_title))
        
        # EP21 内容预告
        ep21_title = Text(
            "第21集：概率思维的10个应用",
            font_size=TITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep21_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("系列大总结", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("改变人生的概率智慧", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("从赌场到华尔街的秘密", font_size=34, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep21_title, DOWN, buff=0.8)
        
        self.play(Write(ep21_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "概率思维如何让你做出更好的决定？",
            font_size=26,
            color=PROB_YELLOW
        )
        think_question.next_to(preview_content, DOWN, buff=0.3)
        
        self.play(Write(think_question))
        self.wait(3)
        
        # 期待语
        see_you = Text(
            "敬请期待系列终章！",
            font_size=38,
            color=WHITE,
            weight=BOLD
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title), FadeOut(ep21_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))