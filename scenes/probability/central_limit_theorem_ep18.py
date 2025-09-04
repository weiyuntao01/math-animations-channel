"""
EP18: 中心极限定理
为什么一切都趋向正态分布
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple
from scipy import stats

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


class CentralLimitTheoremEP18(Scene):
    """中心极限定理 - 概率论系列 EP18"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(18, "中心极限定理")
        
        # 2. 问题引入 - 硬币实验的奇迹
        self.introduce_coin_flip_miracle()
        
        # 3. 不同分布的求和实验（重新设计）
        self.sum_of_different_distributions_v2()
        
        # 4. 中心极限定理陈述
        self.state_central_limit_theorem()
        
        # 5. 动态演示收敛过程
        self.dynamic_convergence_demo()
        
        # 6. 数学直觉解释
        self.mathematical_intuition()
        
        # 7. 德莫佛-拉普拉斯定理
        self.de_moivre_laplace()
        
        # 8. 误差叠加原理
        self.error_stacking_principle()
        
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
        
        # 集数标题
        episode_text = Text(
            f"第{episode_num}集：{episode_title}",
            font_size=34,
            color=WHITE
        )
        episode_text.next_to(series_title, DOWN, buff=0.8)
        
        # 动画效果
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(series_title), FadeOut(episode_text))
    
    def introduce_coin_flip_miracle(self):
        """引入问题 - 硬币实验的奇迹"""
        self.clear()
        
        title = Text("一个简单的实验", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 硬币图标
        coin = self.create_coin()
        coin.shift(UP * 1)
        self.play(FadeIn(coin))
        
        # 问题
        question = VGroup(
            Text("抛100次硬币", font_size=SUBTITLE_SIZE),
            Text("正面次数会是多少？", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.3)
        question.shift(DOWN * 0.5)
        
        self.play(Write(question))
        self.wait(1)
        
        # 多人实验结果
        results = Text(
            "1000人做实验，结果分布是？",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN
        )
        results.shift(DOWN * 2)
        self.play(Write(results))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(coin),
            FadeOut(question), FadeOut(results)
        )
    
    def create_coin(self):
        """创建硬币图标"""
        coin = VGroup()
        
        # 硬币圆形
        circle = Circle(
            radius=0.8,
            fill_color=PROB_YELLOW,
            fill_opacity=0.3,
            stroke_color=PROB_YELLOW,
            stroke_width=3
        )
        
        # 正反面标记
        front = Text("正", font_size=30, color=PROB_YELLOW)
        back = Text("反", font_size=30, color=PROB_GRAY)
        back.set_opacity(0.3)
        
        coin.add(circle, front, back)
        return coin
    
    def sum_of_different_distributions_v2(self):
        """重新设计的不同分布求和实验 - 更规整的布局"""
        self.clear()
        
        # 标题
        title = Text("神奇的统一性", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建三列布局
        col_width = 4.0
        col_positions = [LEFT * col_width, ORIGIN, RIGHT * col_width]
        
        # 三种分布的数据
        distributions_data = [
            {
                "name": "均匀分布",
                "desc": "掷骰子",
                "color": PROB_BLUE,
                "icon": self.create_dice_icon(),
                "histogram": self.create_uniform_histogram()
            },
            {
                "name": "指数分布", 
                "desc": "等待时间",
                "color": PROB_RED,
                "icon": self.create_clock_icon(),
                "histogram": self.create_exponential_histogram()
            },
            {
                "name": "伯努利分布",
                "desc": "成功/失败",
                "color": PROB_GREEN,
                "icon": self.create_binary_icon(),
                "histogram": self.create_bernoulli_histogram()
            }
        ]
        
        # 创建每列的内容
        columns = VGroup()
        
        for i, (pos, data) in enumerate(zip(col_positions, distributions_data)):
            # 创建单列
            column = VGroup()
            
            # 1. 标题
            title_text = Text(
                data["name"],
                font_size=26,
                color=data["color"],
                weight=BOLD
            )
            
            # 2. 描述
            desc_text = Text(
                data["desc"],
                font_size=20,
                color=WHITE
            )
            
            # 3. 图标
            icon = data["icon"]
            icon.scale(0.8)
            
            # 4. 分布图
            histogram = data["histogram"]
            histogram.scale(0.8)
            
            # 垂直排列
            column.add(title_text, desc_text, icon, histogram)
            column.arrange(DOWN, buff=0.3)
            
            # 移动到对应位置
            column.move_to(pos + UP * 0.5)
            columns.add(column)
        
        # 动画显示三列
        self.play(
            *[FadeIn(col, shift=UP * 0.3) for col in columns],
            run_time=1.5
        )
        
        self.wait(1)
        
        # 添加求和箭头 - 更规整的设计
        arrow_group = VGroup()
        
        # 三个向下的箭头
        for pos in col_positions:
            arrow = Arrow(
                pos + DOWN * 1.5,
                pos + DOWN * 2.3,
                color=PROB_YELLOW,
                stroke_width=2,
                buff=0
            )
            arrow_group.add(arrow)
        
        # 汇聚线
        convergence_lines = VGroup()
        for pos in [LEFT * col_width, RIGHT * col_width]:
            line = Line(
                pos + DOWN * 2.3,
                DOWN * 2.8,
                color=PROB_YELLOW,
                stroke_width=2
            )
            convergence_lines.add(line)
        
        arrow_group.add(convergence_lines)
        
        self.play(Create(arrow_group), run_time=1)
        
        # 添加求和符号
        sum_symbol = MathTex(r"\sum", color=PROB_YELLOW, font_size=40)
        sum_symbol.move_to(DOWN * 2.0)
        self.play(Write(sum_symbol))
        
        # 最终结果 - 正态分布
        result_group = VGroup()
        
        # 正态曲线
        normal_curve = self.create_normal_curve_clean()
        normal_curve.scale(1.2)
        normal_curve.shift(DOWN * 3.5)
        
        # 结果文字
        result_text = Text(
            "都变成钟形曲线！",
            font_size=28,
            color=PROB_PURPLE,
            weight=BOLD
        )
        result_text.next_to(normal_curve, DOWN, buff=0.3)
        
        result_group.add(normal_curve, result_text)
        
        # 动画显示结果
        self.play(
            Create(normal_curve),
            Write(result_text),
            run_time=1.5
        )
        
        self.wait(2)
        
        # 清理场景
        self.play(
            FadeOut(title),
            FadeOut(columns),
            FadeOut(arrow_group),
            FadeOut(sum_symbol),
            FadeOut(result_group),
            run_time=1
        )
    
    def create_dice_icon(self):
        """创建骰子图标"""
        dice = VGroup()
        
        # 骰子正方形
        square = Square(side_length=0.8, color=PROB_BLUE, stroke_width=2)
        square.set_fill(PROB_BLUE, opacity=0.2)
        
        # 点数（显示6）
        dots = VGroup()
        positions = [
            [-0.25, 0.25], [0.25, 0.25],
            [-0.25, 0], [0.25, 0],
            [-0.25, -0.25], [0.25, -0.25]
        ]
        
        for pos in positions:
            dot = Dot(point=square.get_center() + RIGHT * pos[0] + UP * pos[1],
                     radius=0.06, color=WHITE)
            dots.add(dot)
        
        dice.add(square, dots)
        return dice
    
    def create_clock_icon(self):
        """创建时钟图标"""
        clock = VGroup()
        
        # 时钟圆形
        circle = Circle(radius=0.4, color=PROB_RED, stroke_width=2)
        circle.set_fill(PROB_RED, opacity=0.2)
        
        # 时针和分针
        hour_hand = Line(
            circle.get_center(),
            circle.get_center() + UP * 0.2 + RIGHT * 0.1,
            color=WHITE,
            stroke_width=2
        )
        
        minute_hand = Line(
            circle.get_center(),
            circle.get_center() + UP * 0.3,
            color=WHITE,
            stroke_width=2
        )
        
        clock.add(circle, hour_hand, minute_hand)
        return clock
    
    def create_binary_icon(self):
        """创建二元选择图标"""
        binary = VGroup()
        
        # 圆形背景
        circle = Circle(radius=0.4, color=PROB_GREEN, stroke_width=2)
        circle.set_fill(PROB_GREEN, opacity=0.2)
        
        # 0和1
        zero = Text("0", font_size=20, color=WHITE)
        one = Text("1", font_size=20, color=WHITE)
        zero.shift(LEFT * 0.15)
        one.shift(RIGHT * 0.15)
        
        # 分隔线
        line = Line(UP * 0.3, DOWN * 0.3, color=WHITE, stroke_width=1)
        
        binary.add(circle, zero, one, line)
        return binary
    
    def create_uniform_histogram(self):
        """创建均匀分布直方图"""
        histogram = VGroup()
        
        # 创建6个等高的柱子
        bar_width = 0.25
        bar_height = 0.8
        
        for i in range(6):
            bar = Rectangle(
                width=bar_width,
                height=bar_height,
                fill_color=PROB_BLUE,
                fill_opacity=0.7,
                stroke_width=0
            )
            bar.shift(RIGHT * (i - 2.5) * (bar_width + 0.05))
            bar.shift(UP * bar_height * 0.5)
            histogram.add(bar)
        
        # 添加坐标轴
        x_axis = Line(LEFT * 1, RIGHT * 1, color=WHITE, stroke_width=1)
        x_axis.shift(DOWN * 0.1)
        histogram.add(x_axis)
        
        return histogram
    
    def create_exponential_histogram(self):
        """创建指数分布直方图"""
        histogram = VGroup()
        
        # 创建递减的柱子
        bar_width = 0.25
        heights = [1.0, 0.6, 0.36, 0.22, 0.13, 0.08]
        
        for i, height in enumerate(heights):
            bar = Rectangle(
                width=bar_width,
                height=height * 0.8,
                fill_color=PROB_RED,
                fill_opacity=0.7,
                stroke_width=0
            )
            bar.shift(RIGHT * (i - 2.5) * (bar_width + 0.05))
            bar.shift(UP * height * 0.4)
            histogram.add(bar)
        
        # 添加坐标轴
        x_axis = Line(LEFT * 1, RIGHT * 1, color=WHITE, stroke_width=1)
        x_axis.shift(DOWN * 0.1)
        histogram.add(x_axis)
        
        return histogram
    
    def create_bernoulli_histogram(self):
        """创建伯努利分布直方图"""
        histogram = VGroup()
        
        # 只有两个柱子（0和1）
        bar_width = 0.4
        bar_height = 0.8
        
        # 0的柱子
        bar0 = Rectangle(
            width=bar_width,
            height=bar_height,
            fill_color=PROB_GREEN,
            fill_opacity=0.7,
            stroke_width=0
        )
        bar0.shift(LEFT * 0.3)
        bar0.shift(UP * bar_height * 0.5)
        
        # 1的柱子
        bar1 = Rectangle(
            width=bar_width,
            height=bar_height,
            fill_color=PROB_GREEN,
            fill_opacity=0.7,
            stroke_width=0
        )
        bar1.shift(RIGHT * 0.3)
        bar1.shift(UP * bar_height * 0.5)
        
        histogram.add(bar0, bar1)
        
        # 添加坐标轴
        x_axis = Line(LEFT * 1, RIGHT * 1, color=WHITE, stroke_width=1)
        x_axis.shift(DOWN * 0.1)
        histogram.add(x_axis)
        
        # 添加标签
        label0 = Text("0", font_size=16, color=WHITE)
        label0.next_to(bar0, DOWN, buff=0.1)
        label1 = Text("1", font_size=16, color=WHITE)
        label1.next_to(bar1, DOWN, buff=0.1)
        histogram.add(label0, label1)
        
        return histogram
    
    def create_normal_curve_clean(self):
        """创建干净的正态曲线"""
        # 创建坐标轴
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 0.5, 0.1],
            x_length=4,
            y_length=1.5,
            axis_config={
                "color": WHITE,
                "stroke_width": 1,
                "include_numbers": False,
                "include_ticks": False
            }
        )
        
        # 生成正态曲线数据
        x = np.linspace(-3, 3, 100)
        y = stats.norm.pdf(x, 0, 1)
        
        # 创建曲线点
        curve_points = []
        for xi, yi in zip(x, y):
            curve_points.append(axes.c2p(xi, yi))
        
        # 创建曲线
        curve = VMobject(color=PROB_PURPLE, stroke_width=3)
        curve.set_points_smoothly(curve_points)
        
        # 填充曲线下方区域
        fill = VMobject(fill_color=PROB_PURPLE, fill_opacity=0.3, stroke_width=0)
        fill_points = curve_points.copy()
        fill_points.append(axes.c2p(3, 0))
        fill_points.append(axes.c2p(-3, 0))
        fill.set_points_smoothly(fill_points)
        
        return VGroup(axes, fill, curve)
    
    def state_central_limit_theorem(self):
        """陈述中心极限定理"""
        self.clear()
        
        title = Text("中心极限定理", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 定理陈述
        theorem = VGroup(
            Text("设 X₁, X₂, ..., Xₙ", font_size=SUBTITLE_SIZE),
            Text("独立同分布的随机变量", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("均值为μ，方差为σ²", font_size=NORMAL_SIZE),
            Text("则当n→∞时：", font_size=NORMAL_SIZE),
        ).arrange(DOWN, buff=0.3)
        theorem.shift(UP * 0.5)
        
        for line in theorem:
            self.play(Write(line), run_time=0.6)
        
        # 数学表达式
        formula = MathTex(
            r"\frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}}",
            r"\xrightarrow{d}",
            r"N(0, 1)"
        ).scale(1.2)
        formula.shift(DOWN * 1.5)
        
        self.play(Write(formula[0]))
        self.play(Write(formula[1]))
        self.play(Write(formula[2]), formula[2].animate.set_color(PROB_GREEN))
        
        # 通俗解释
        explanation = Text(
            "和的标准化趋向标准正态分布",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN
        )
        explanation.shift(DOWN * 2.8)
        self.play(Write(explanation))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(theorem),
            FadeOut(formula), FadeOut(explanation)
        )
    
    def dynamic_convergence_demo(self):
        """动态演示收敛过程"""
        self.clear()
        
        title = Text("收敛的魔法", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建坐标系
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            x_length=8,
            y_length=4,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 16
            }
        ).shift(DOWN * 0.5)
        
        x_label = Text("标准化和", font_size=SMALL_SIZE).next_to(axes.x_axis, DOWN)
        y_label = Text("概率密度", font_size=SMALL_SIZE).next_to(axes.y_axis, LEFT).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # n值标签
        n_label = Text("n = 1", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        n_label.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(n_label))
        
        # 动态展示不同n值的分布
        n_values = [1, 2, 5, 10, 30, 100]
        colors = [PROB_RED, PROB_YELLOW, PROB_GREEN, PROB_BLUE, PROB_PURPLE, PROB_PURPLE]
        
        previous_curve = None
        for n, color in zip(n_values, colors):
            # 更新n值标签
            new_label = Text(f"n = {n}", font_size=SUBTITLE_SIZE, color=color)
            new_label.to_edge(RIGHT).shift(UP * 2)
            self.play(Transform(n_label, new_label), run_time=0.5)
            
            # 生成分布曲线
            x = np.linspace(-4, 4, 100)
            
            if n == 1:
                # 原始分布（均匀）
                y = np.where(np.abs(x) < 1.7, 0.3, 0)
            else:
                # 使用中心极限定理的近似
                y = stats.norm.pdf(x, 0, 1)
                # 加入一些偏差表示还未完全收敛
                if n < 30:
                    y = y * (1 - 0.5/n) + 0.05/n
            
            # 创建曲线
            curve_points = []
            for xi, yi in zip(x, y):
                curve_points.append(axes.c2p(xi, yi))
            
            curve = VMobject(color=color, stroke_width=3)
            curve.set_points_smoothly(curve_points)
            
            if previous_curve is None:
                self.play(Create(curve), run_time=1)
            else:
                self.play(Transform(previous_curve, curve), run_time=1)
            
            if previous_curve is None:
                previous_curve = curve
            
            self.wait(0.5)
        
        # 添加标准正态曲线作为参考
        x = np.linspace(-4, 4, 100)
        y = stats.norm.pdf(x, 0, 1)
        
        reference_points = []
        for xi, yi in zip(x, y):
            reference_points.append(axes.c2p(xi, yi))
        
        reference_curve = VMobject(color=WHITE, stroke_width=2)
        reference_curve.set_points_smoothly(reference_points)
        reference_curve.set_stroke(opacity=0.5)
        
        reference_label = Text(
            "标准正态分布",
            font_size=SMALL_SIZE,
            color=WHITE
        ).next_to(axes, DOWN, buff=0.5)
        
        self.play(
            Create(reference_curve),
            Write(reference_label)
        )
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(axes),
            FadeOut(x_label), FadeOut(y_label),
            FadeOut(n_label), FadeOut(previous_curve),
            FadeOut(reference_curve), FadeOut(reference_label)
        )
    
    def mathematical_intuition(self):
        """数学直觉解释"""
        self.clear()
        
        title = Text("为什么是正态分布？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 关键思想
        key_ideas = VGroup(
            Text("1. 独立性", font_size=SUBTITLE_SIZE, color=PROB_BLUE),
            Text("每个变量互不影响", font_size=NORMAL_SIZE),
            Text("2. 大量叠加", font_size=SUBTITLE_SIZE, color=PROB_GREEN),
            Text("微小影响的累积", font_size=NORMAL_SIZE),
            Text("3. 对称性", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("正负偏差相互抵消", font_size=NORMAL_SIZE),
        ).arrange(DOWN, buff=0.3)
        key_ideas.shift(UP * 0.5)
        
        for i in range(0, len(key_ideas), 2):
            self.play(
                Write(key_ideas[i]),
                Write(key_ideas[i+1]),
                run_time=1
            )
        
        # 图形化解释
        self.wait(1)
        self.play(FadeOut(key_ideas))
        
        # 误差叠加示意
        self.show_error_stacking()
        
        self.play(FadeOut(title))
    
    def show_error_stacking(self):
        """展示误差叠加"""
        # 创建多个小误差
        errors = VGroup()
        n_errors = 20
        
        for i in range(n_errors):
            # 随机误差大小和方向
            error_size = random.uniform(0.2, 0.5)
            error_direction = random.choice([-1, 1])
            
            arrow = Arrow(
                ORIGIN,
                RIGHT * error_size * error_direction,
                color=PROB_BLUE if error_direction > 0 else PROB_RED,
                stroke_width=2
            )
            arrow.shift(UP * (2 - i * 0.2))
            arrow.shift(LEFT * 2)
            
            errors.add(arrow)
        
        # 逐个显示
        for error in errors:
            self.play(FadeIn(error), run_time=0.1)
        
        # 合成结果
        total_arrow = Arrow(
            LEFT * 2,
            RIGHT * 1,
            color=PROB_PURPLE,
            stroke_width=4
        )
        total_arrow.shift(DOWN * 2)
        
        label = Text(
            "总和接近中心值",
            font_size=NORMAL_SIZE,
            color=PROB_PURPLE
        )
        label.next_to(total_arrow, DOWN)
        
        self.play(
            Create(total_arrow),
            Write(label)
        )
        
        self.wait(2)
        self.play(FadeOut(errors), FadeOut(total_arrow), FadeOut(label))
    
    def de_moivre_laplace(self):
        """德莫佛-拉普拉斯定理"""
        self.clear()
        
        title = Text("历史时刻：1733年", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 历史背景
        history = VGroup(
            Text("德莫佛发现：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("二项分布的极限是正态分布", font_size=NORMAL_SIZE),
            Text("这是中心极限定理的雏形", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.4)
        history.shift(UP * 1)
        
        for line in history:
            self.play(Write(line), run_time=0.8)
        
        # 二项分布到正态分布的过渡
        self.show_binomial_to_normal()
        
        self.play(FadeOut(title), FadeOut(history))
    
    def show_binomial_to_normal(self):
        """展示二项分布到正态分布的过渡"""
        # 创建坐标系
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 0.1, 0.02],
            x_length=8,
            y_length=3,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 14
            }
        ).shift(DOWN * 1.5)
        
        self.play(Create(axes))
        
        # 二项分布 B(100, 0.5)
        n, p = 100, 0.5
        x = np.arange(0, 101)
        y = stats.binom.pmf(x, n, p)
        
        # 创建柱状图
        bars = VGroup()
        for i in range(30, 71, 2):  # 只显示中间部分
            bar = Rectangle(
                width=0.15,
                height=y[i] * 30,
                fill_color=PROB_BLUE,
                fill_opacity=0.7,
                stroke_width=0
            )
            bar.move_to(axes.c2p(i, y[i]/2))
            bars.add(bar)
        
        self.play(Create(bars))
        
        # 叠加正态曲线
        mu = n * p
        sigma = np.sqrt(n * p * (1 - p))
        x_continuous = np.linspace(20, 80, 100)
        y_continuous = stats.norm.pdf(x_continuous, mu, sigma)
        
        curve_points = []
        for xi, yi in zip(x_continuous, y_continuous):
            curve_points.append(axes.c2p(xi, yi))
        
        curve = VMobject(color=PROB_PURPLE, stroke_width=3)
        curve.set_points_smoothly(curve_points)
        
        label = Text(
            "完美拟合！",
            font_size=NORMAL_SIZE,
            color=PROB_PURPLE
        )
        label.next_to(axes, RIGHT)
        
        self.play(Create(curve), Write(label))
        
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(bars), FadeOut(curve), FadeOut(label))
    
    def error_stacking_principle(self):
        """误差叠加原理"""
        self.clear()
        
        title = Text("现实应用：误差分析", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 测量场景
        measurement_scene = VGroup()
        
        # 左侧：多个误差源
        error_sources = VGroup(
            Text("误差来源：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("• 仪器误差", font_size=NORMAL_SIZE),
            Text("• 环境干扰", font_size=NORMAL_SIZE),
            Text("• 人为误差", font_size=NORMAL_SIZE),
            Text("• 随机涨落", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        error_sources.shift(LEFT * 4 + UP * 0.5)
        
        self.play(Write(error_sources))
        
        # 右侧：结果分布
        result = VGroup(
            Text("总误差分布", font_size=SUBTITLE_SIZE, color=PROB_GREEN),
            self.create_normal_curve()
        ).arrange(DOWN, buff=0.5)
        result.shift(RIGHT * 3 + UP * 0.5)
        
        self.play(Create(result))
        
        # 中间：箭头连接
        arrow = Arrow(
            error_sources.get_right(),
            result.get_left(),
            color=PROB_PURPLE,
            stroke_width=3
        )
        
        arrow_label = Text(
            "CLT",
            font_size=NORMAL_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        arrow_label.next_to(arrow, UP)
        
        self.play(Create(arrow), Write(arrow_label))
        
        # 结论
        conclusion = Text(
            "这就是为什么测量误差服从正态分布！",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        conclusion.shift(DOWN * 2.5)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(error_sources),
            FadeOut(result), FadeOut(arrow),
            FadeOut(arrow_label), FadeOut(conclusion)
        )
    
    def create_normal_curve(self):
        """创建正态曲线"""
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 0.5, 0.1],
            x_length=3,
            y_length=2,
            axis_config={
                "color": WHITE,
                "stroke_width": 1,
                "include_numbers": False
            }
        )
        
        x = np.linspace(-3, 3, 100)
        y = stats.norm.pdf(x)
        
        curve_points = []
        for xi, yi in zip(x, y):
            curve_points.append(axes.c2p(xi, yi))
        
        curve = VMobject(color=PROB_GREEN, stroke_width=3)
        curve.set_points_smoothly(curve_points)
        
        return VGroup(axes, curve)
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        # 核心总结
        summary = VGroup(
            Text("中心极限定理告诉我们：", font_size=38, color=WHITE),
            Text("无序中蕴含着秩序", font_size=TITLE_SIZE, color=PROB_PURPLE, weight=BOLD),
            Text("这是统计学最深刻的洞察", font_size=34, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 三个要点
        key_points = VGroup(
            Text("记住三点：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("1. 独立随机变量之和", font_size=NORMAL_SIZE),
            Text("2. 样本量足够大", font_size=NORMAL_SIZE),
            Text("3. 必然趋向正态分布", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.4)
        
        for point in key_points:
            self.play(Write(point), run_time=0.8)
        
        self.wait(3)
        self.play(FadeOut(key_points))
        
        # 系列结尾
        self.show_series_ending(
            "从混沌到有序",
            "数学之美，尽在概率"
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
        preview_title = Text("下期预告", font_size=38, color=PROB_YELLOW)
        preview_title.to_edge(UP)
        self.play(Write(preview_title))
        
        # EP19 内容预告
        ep19_title = Text(
            "第19集：条件概率的陷阱",
            font_size=TITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep19_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("辛普森悖论", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("数据会说谎吗？", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("统计的反直觉", font_size=34, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep19_title, DOWN, buff=0.8)
        
        self.play(Write(ep19_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "同样的数据，为什么结论完全相反？",
            font_size=26,
            color=PROB_YELLOW
        )
        think_question.next_to(preview_content, DOWN, buff=0.3)
        
        self.play(Write(think_question))
        self.wait(3)
        
        # 期待语
        see_you = Text(
            "下期见！",
            font_size=38,
            color=WHITE
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title), FadeOut(ep19_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))