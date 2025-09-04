"""
EP13: 正态分布
自然界最美的曲线
"""

from manim import *
import numpy as np
import random
from scipy import stats
from typing import List, Dict, Tuple

# 概率系列颜色主题
PROB_PURPLE = "#8B5CF6"    # 主色：概率紫
PROB_GREEN = "#10B981"     # 成功绿
PROB_RED = "#EF4444"       # 失败红
PROB_BLUE = "#3B82F6"      # 数据蓝
PROB_YELLOW = "#F59E0B"    # 警告黄
PROB_GRAY = "#6B7280"      # 中性灰


class NormalDistributionEP13(Scene):
    """正态分布 - 概率论系列 EP13"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(13, "正态分布")
        
        # 2. 问题引入 - 身高分布
        self.introduce_height_distribution()
        
        # 3. 正态分布的发现
        self.discover_normal_distribution()
        
        # 4. 数学定义与性质
        self.mathematical_definition()
        
        # 5. 高尔顿板实验
        self.galton_board_experiment()
        
        # 6. 中心极限定理
        self.central_limit_theorem()
        
        # 7. 现实应用
        self.real_world_applications()
        
        # 8. 结尾
        self.show_ending()
    
    def show_series_intro(self, episode_num: int, episode_title: str):
        """显示系列介绍动画"""
        # 系列标题
        series_title = Text(
            "概率论的反直觉世界",
            font_size=48,
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 集数标题
        episode_text = Text(
            f"第{episode_num}集：{episode_title}",
            font_size=32,
            color=WHITE
        )
        episode_text.next_to(series_title, DOWN, buff=0.8)
        
        # 动画效果
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(series_title), FadeOut(episode_text))
    
    def introduce_height_distribution(self):
        """引入问题 - 身高分布"""
        title = Text("一个简单的问题", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 问题文字
        question = Text(
            "你的身高在人群中排第几？",
            font_size=36,
            color=PROB_YELLOW
        )
        question.shift(UP * 1)
        self.play(Write(question))
        
        # 创建身高标尺（左侧）
        height_scale = self.create_height_scale()
        height_scale.shift(LEFT * 4)
        self.play(Create(height_scale))
        
        # 展示不同身高的人物剪影（右侧）
        people = self.create_people_silhouettes()
        people.shift(RIGHT * 2)
        
        # 逐个显示人物
        for person in people:
            self.play(FadeIn(person, shift=UP), run_time=0.3)
        
        # 提示思考
        think_text = Text(
            "大多数人在哪里？",
            font_size=28,
            color=WHITE
        )
        think_text.shift(DOWN * 2.5)
        self.play(Write(think_text))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(height_scale), FadeOut(people),
            FadeOut(think_text)
        )
    
    def create_height_scale(self):
        """创建身高标尺"""
        scale = VGroup()
        
        # 主轴
        main_line = Line(
            UP * 2.5, DOWN * 2.5,
            color=WHITE,
            stroke_width=3
        )
        
        # 刻度和标签
        heights = [150, 160, 170, 180, 190]
        for i, height in enumerate(heights):
            y_pos = UP * (2 - i)
            
            # 刻度线
            tick = Line(
                LEFT * 0.2, RIGHT * 0.2,
                color=WHITE
            ).shift(y_pos)
            
            # 标签
            label = Text(f"{height}cm", font_size=16)
            label.next_to(tick, LEFT, buff=0.3)
            
            scale.add(tick, label)
        
        scale.add(main_line)
        return scale
    
    def create_people_silhouettes(self):
        """创建不同身高的人物剪影"""
        people = VGroup()
        
        # 身高数据（接近正态分布）
        heights = [155, 163, 168, 170, 172, 174, 176, 178, 183, 190]
        mean_height = 172
        
        for i, height in enumerate(heights):
            # 人物剪影（简化为矩形）
            person = Rectangle(
                width=0.6,
                height=(height - 140) / 20,  # 缩放比例
                fill_color=PROB_BLUE,
                fill_opacity=0.7,
                stroke_width=0
            )
            
            # 根据身高调整颜色
            if abs(height - mean_height) <= 5:
                person.set_fill(PROB_GREEN)
            elif abs(height - mean_height) > 15:
                person.set_fill(PROB_RED)
            
            # 排列位置
            person.shift(RIGHT * (i - 4.5) * 0.8)
            person.shift(DOWN * (2 - person.get_height() / 2))
            
            people.add(person)
        
        return people
    
    def discover_normal_distribution(self):
        """发现正态分布"""
        title = Text("神奇的钟形曲线", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建坐标系
        axes = Axes(
            x_range=[140, 200, 10],
            y_range=[0, 0.05, 0.01],
            x_length=10,
            y_length=5,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "decimal_number_config": {"num_decimal_places": 0}
            }
        ).shift(DOWN * 0.5)
        
        x_label = Text("身高(cm)", font_size=20).next_to(axes.x_axis, DOWN)
        y_label = Text("概率密度", font_size=20).next_to(axes.y_axis, LEFT).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 生成正态分布数据
        mu, sigma = 172, 7  # 平均身高172cm，标准差7cm
        x = np.linspace(140, 200, 1000)
        y = stats.norm.pdf(x, mu, sigma)
        
        # 绘制曲线
        curve = axes.plot_line_graph(
            x_values=x,
            y_values=y,
            line_color=PROB_PURPLE,
            stroke_width=3,
            add_vertex_dots=False
        )
        
        self.play(Create(curve), run_time=2)
        
        # 标注特征
        # 平均值线
        mean_line = DashedLine(
            axes.c2p(mu, 0),
            axes.c2p(mu, 0.057),
            color=PROB_GREEN,
            stroke_width=2
        )
        mean_label = Text(f"μ = {mu}cm", font_size=18, color=PROB_GREEN)
        mean_label.next_to(mean_line, UP)
        
        self.play(Create(mean_line), Write(mean_label))
        
        # 标准差区域
        sigma_areas = VGroup()
        colors = [PROB_BLUE, PROB_YELLOW, PROB_RED]
        alphas = [0.3, 0.2, 0.1]
        
        for i in range(1, 4):
            left_x = mu - i * sigma
            right_x = mu + i * sigma
            
            # 创建区域
            area_points = []
            for x_val in np.linspace(left_x, right_x, 50):
                if 140 <= x_val <= 200:
                    y_val = stats.norm.pdf(x_val, mu, sigma)
                    area_points.append(axes.c2p(x_val, y_val))
            
            if area_points:
                area_points.append(axes.c2p(min(right_x, 200), 0))
                area_points.append(axes.c2p(max(left_x, 140), 0))
                
                area = Polygon(
                    *area_points,
                    fill_color=colors[i-1],
                    fill_opacity=alphas[i-1],
                    stroke_width=0
                )
                sigma_areas.add(area)
        
        self.play(FadeIn(sigma_areas))
        
        # 百分比标注
        percentages = VGroup(
            Text("68%", font_size=20, color=PROB_BLUE).shift(DOWN * 1.5),
            Text("95%", font_size=20, color=PROB_YELLOW).shift(DOWN * 2),
            Text("99.7%", font_size=20, color=PROB_RED).shift(DOWN * 2.5)
        )
        
        for i, pct in enumerate(percentages):
            self.play(Write(pct), run_time=0.5)
        
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(curve), FadeOut(mean_line), FadeOut(mean_label),
            FadeOut(sigma_areas), FadeOut(percentages)
        )
    
    def mathematical_definition(self):
        """数学定义与性质"""
        title = Text("正态分布的数学定义", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 第一部分：概率密度函数
        self.show_pdf_formula()
        
        # 第二部分：关键性质
        self.show_key_properties()
        
        self.play(FadeOut(title))
    
    def show_pdf_formula(self):
        """展示概率密度函数"""
        # 公式标题
        formula_title = Text("概率密度函数", font_size=28, color=PROB_YELLOW)
        formula_title.shift(UP * 2)
        self.play(Write(formula_title))
        
        # 主公式
        pdf = MathTex(
            r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}"
        ).scale(1.2)
        
        self.play(Write(pdf))
        self.wait(1)
        
        # 参数解释
        params = VGroup(
            VGroup(
                MathTex(r"\mu", color=PROB_GREEN),
                Text("：平均值（位置参数）", font_size=20)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\sigma", color=PROB_BLUE),
                Text("：标准差（尺度参数）", font_size=20)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"e \approx 2.718", color=PROB_YELLOW),
                Text("：自然常数", font_size=20)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        params.shift(DOWN * 1.5)
        
        self.play(Write(params))
        self.wait(2)
        
        self.play(FadeOut(formula_title), FadeOut(pdf), FadeOut(params))
    
    def show_key_properties(self):
        """展示关键性质"""
        # 性质标题
        props_title = Text("正态分布的优美性质", font_size=28, color=PROB_YELLOW)
        props_title.shift(UP * 2.5)
        self.play(Write(props_title))
        
        # 左侧：对称性
        symmetry_group = VGroup(
            Text("完美对称", font_size=24, color=PROB_BLUE),
            MathTex(r"f(\mu + x) = f(\mu - x)"),
            Text("左右完全镜像", font_size=18, color=GRAY)
        ).arrange(DOWN, buff=0.3)
        symmetry_group.shift(LEFT * 3.5 + UP * 0.5)
        
        # 右侧：经验法则
        rule_group = VGroup(
            Text("68-95-99.7法则", font_size=24, color=PROB_GREEN),
            VGroup(
                MathTex(r"P(\mu - \sigma < X < \mu + \sigma) = 0.68"),
                MathTex(r"P(\mu - 2\sigma < X < \mu + 2\sigma) = 0.95"),
                MathTex(r"P(\mu - 3\sigma < X < \mu + 3\sigma) = 0.997")
            ).arrange(DOWN, buff=0.2).scale(0.8),
        ).arrange(DOWN, buff=0.3)
        rule_group.shift(RIGHT * 3.5 + UP * 0.5)
        
        self.play(Write(symmetry_group), Write(rule_group))
        
        # 底部：线性变换性质
        transform_text = Text(
            "线性变换后仍是正态分布",
            font_size=22,
            color=PROB_PURPLE
        )
        transform_formula = MathTex(
            r"\text{If } X \sim N(\mu, \sigma^2), \text{ then } aX + b \sim N(a\mu + b, a^2\sigma^2)"
        ).scale(0.8)
        transform_group = VGroup(transform_text, transform_formula).arrange(DOWN, buff=0.2)
        transform_group.shift(DOWN * 2)
        
        self.play(Write(transform_group))
        self.wait(2)
        
        self.play(
            FadeOut(props_title), FadeOut(symmetry_group),
            FadeOut(rule_group), FadeOut(transform_group)
        )
    
    def galton_board_experiment(self):
        """高尔顿板实验"""
        title = Text("高尔顿板：正态分布的诞生", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建高尔顿板
        board = self.create_galton_board()
        board.shift(LEFT * 3)
        self.play(Create(board))
        
        # 右侧说明
        explanation = VGroup(
            Text("高尔顿板原理", font_size=28, color=PROB_YELLOW),
            Text("• 小球随机左右弹跳", font_size=20),
            Text("• 每次弹跳概率相等", font_size=20),
            Text("• 多次累加形成分布", font_size=20),
            Text("• 完美演示中心极限定理", font_size=20, color=PROB_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        explanation.shift(RIGHT * 3.5)
        
        self.play(Write(explanation))
        
        # 模拟小球下落
        bars = self.simulate_galton_balls(board)  # 接收返回的bars
        
        # 结果说明
        result_text = Text(
            "二项分布的极限就是正态分布！",
            font_size=26,
            color=PROB_GREEN,
            weight=BOLD
        )
        result_text.shift(DOWN * 3)
        self.play(Write(result_text))
        self.wait(2)
        
        # 清理时包含bars
        self.play(
            FadeOut(title), FadeOut(board),
            FadeOut(explanation), FadeOut(result_text),
            FadeOut(bars)  # 添加bars的淡出
        )
    
    def create_galton_board(self):
        """创建高尔顿板"""
        board = VGroup()
        
        # 外框
        frame = Rectangle(
            width=4, height=5,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        # 钉子（简化版）
        pegs = VGroup()
        rows = 8
        for row in range(rows):
            for col in range(row + 1):
                x = (col - row / 2) * 0.4
                y = 2 - row * 0.5
                peg = Dot(
                    point=[x, y, 0],
                    radius=0.05,
                    color=GRAY
                )
                pegs.add(peg)
        
        # 收集槽
        bins = VGroup()
        n_bins = 9
        bin_width = 0.4
        for i in range(n_bins):
            x = (i - n_bins / 2 + 0.5) * bin_width
            bin_rect = Rectangle(
                width=bin_width * 0.9,
                height=0.3,
                fill_color=PROB_BLUE,
                fill_opacity=0.3,
                stroke_color=WHITE
            )
            bin_rect.shift(RIGHT * x + DOWN * 2.3)
            bins.add(bin_rect)
        
        board.add(frame, pegs, bins)
        return board
    
    def simulate_galton_balls(self, board):
        """模拟小球下落"""
        # 简化版：直接显示结果分布
        bins = board[2]  # 获取收集槽
        
        # 预计算的分布（接近正态）
        heights = [1, 4, 10, 20, 30, 20, 10, 4, 1]
        max_height = max(heights)
        
        bars = VGroup()
        for i, height in enumerate(heights):
            bar_height = height / max_height * 2
            bar = Rectangle(
                width=0.35,
                height=bar_height,
                fill_color=PROB_PURPLE,
                fill_opacity=0.8,
                stroke_width=0
            )
            bar.move_to(bins[i].get_center())
            bar.shift(UP * (bar_height / 2 + 0.15))
            bars.add(bar)
        
        # 动画显示
        for bar in bars:
            self.play(GrowFromEdge(bar, DOWN), run_time=0.3)
        return bars
    def central_limit_theorem(self):
        """中心极限定理"""
        title = Text("中心极限定理：万物归一", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 定理陈述
        theorem_text = VGroup(
            Text("中心极限定理", font_size=32, color=PROB_YELLOW),
            Text("大量独立随机变量之和", font_size=24),
            Text("趋向于正态分布", font_size=28, color=PROB_GREEN),
            Text("无论原始分布是什么！", font_size=24, color=PROB_RED)
        ).arrange(DOWN, buff=0.3)
        theorem_text.shift(UP * 0.5)
        
        self.play(Write(theorem_text))
        self.wait(1)
        
        # 展示不同分布的叠加
        self.show_clt_demo()
        
        self.play(FadeOut(title), FadeOut(theorem_text))
    
    def show_clt_demo(self):
        """展示中心极限定理演示"""
        # 创建三个不同的初始分布
        distributions = VGroup()
        
        # 均匀分布
        uniform_axes = self.create_mini_axes("均匀分布", PROB_BLUE)
        uniform_axes.shift(LEFT * 5 + DOWN * 1.5)
        distributions.add(uniform_axes)
        
        # 指数分布
        exp_axes = self.create_mini_axes("指数分布", PROB_RED)
        exp_axes.shift(DOWN * 1.5)
        distributions.add(exp_axes)
        
        # 二项分布
        binom_axes = self.create_mini_axes("二项分布", PROB_YELLOW)
        binom_axes.shift(RIGHT * 5 + DOWN * 1.5)
        distributions.add(binom_axes)
        
        self.play(Create(distributions))
        
        # 箭头指向结果
        arrows = VGroup()
        for dist in distributions:
            arrow = Arrow(
                dist.get_top(),
                DOWN * 0.5,
                color=WHITE,
                stroke_width=2
            )
            arrows.add(arrow)
        
        self.play(Create(arrows))
        
        # 最终的正态分布
        final_text = Text(
            "叠加后都变成正态分布！",
            font_size=28,
            color=PROB_GREEN,
            weight=BOLD
        )
        final_text.shift(DOWN * 3)
        
        self.play(Write(final_text))
        self.wait(2)
        
        self.play(FadeOut(distributions), FadeOut(arrows), FadeOut(final_text))
    
    def create_mini_axes(self, title: str, color):
        """创建小型坐标系"""
        group = VGroup()
        
        # 标题
        title_text = Text(title, font_size=16, color=color)
        
        # 简化的坐标轴
        axes = VGroup(
            Line(LEFT * 0.8, RIGHT * 0.8, color=GRAY),
            Line(DOWN * 0.5, UP * 0.5, color=GRAY)
        )
        axes.shift(DOWN * 0.3)
        
        group.add(title_text, axes)
        return group
    
    def real_world_applications(self):
        """现实应用"""
        title = Text("正态分布无处不在", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 应用场景网格
        applications = VGroup()
        
        # 1. 考试成绩
        exam_app = self.create_application_example(
            "考试成绩",
            "大部分人在中等水平",
            PROB_BLUE,
            self.create_exam_visual
        )
        exam_app.shift(LEFT * 5 + UP * 1)
        
        # 2. 产品质量
        quality_app = self.create_application_example(
            "产品质量",
            "6σ质量管理",
            PROB_GREEN,
            self.create_quality_visual
        )
        quality_app.shift(LEFT * 1.7 + UP * 1)
        
        # 3. 金融市场
        finance_app = self.create_application_example(
            "金融市场",
            "收益率分布",
            PROB_YELLOW,
            self.create_finance_visual
        )
        finance_app.shift(RIGHT * 1.7 + UP * 1)
        
        # 4. 测量误差
        error_app = self.create_application_example(
            "测量误差",
            "随机误差分布",
            PROB_RED,
            self.create_error_visual
        )
        error_app.shift(RIGHT * 5 + UP * 1)
        
        applications.add(exam_app, quality_app, finance_app, error_app)
        
        # 逐个显示
        for app in applications:
            self.play(FadeIn(app, shift=UP), run_time=0.5)
        
        # 总结
        summary = Text(
            "正态分布：自然界的基本规律",
            font_size=28,
            color=PROB_PURPLE,
            weight=BOLD
        )
        summary.shift(DOWN * 2.5)
        self.play(Write(summary))
        self.wait(3)
        
        self.play(FadeOut(title), FadeOut(applications), FadeOut(summary))
    
    def create_application_example(self, title: str, subtitle: str, color, visual_func):
        """创建应用示例"""
        group = VGroup()
        
        # 背景框
        bg = RoundedRectangle(
            width=2.8, height=2,
            corner_radius=0.15,
            fill_color=color,
            fill_opacity=0.1,
            stroke_color=color,
            stroke_width=2
        )
        
        # 标题
        title_text = Text(title, font_size=20, color=color, weight=BOLD)
        title_text.shift(UP * 0.7)
        
        # 副标题
        subtitle_text = Text(subtitle, font_size=14, color=WHITE)
        subtitle_text.shift(UP * 0.4)
        
        # 可视化
        visual = visual_func()
        visual.shift(DOWN * 0.3)
        
        group.add(bg, title_text, subtitle_text, visual)
        return group
    
    def create_exam_visual(self):
        """创建考试成绩可视化"""
        # 简化的成绩分布
        bars = VGroup()
        heights = [0.5, 1, 2, 3, 2, 1, 0.5]
        for i, h in enumerate(heights):
            bar = Rectangle(
                width=0.2, height=h * 0.3,
                fill_color=PROB_BLUE,
                fill_opacity=0.8,
                stroke_width=0
            )
            bar.shift(RIGHT * (i - 3) * 0.25 + UP * h * 0.15)
            bars.add(bar)
        return bars
    
    def create_quality_visual(self):
        """创建质量控制可视化"""
        # 控制限
        lines = VGroup(
            Line(LEFT * 1, RIGHT * 1, color=PROB_GREEN),  # 中心线
            DashedLine(LEFT * 1, RIGHT * 1, color=PROB_YELLOW).shift(UP * 0.3),  # 上限
            DashedLine(LEFT * 1, RIGHT * 1, color=PROB_YELLOW).shift(DOWN * 0.3)  # 下限
        )
        return lines
    
    def create_finance_visual(self):
        """创建金融市场可视化"""
        # 简化的价格曲线
        points = [
            [-1, 0], [-0.5, 0.2], [0, -0.1],
            [0.5, 0.3], [1, 0.1]
        ]
        curve = VMobject(color=PROB_YELLOW)
        curve.set_points_smoothly([np.array([x, y, 0]) for x, y in points])
        curve.scale(0.8)
        return curve
    
    def create_error_visual(self):
        """创建测量误差可视化"""
        # 目标和散点
        target = Circle(radius=0.3, color=PROB_RED, stroke_width=2)
        dots = VGroup()
        for _ in range(8):
            angle = random.uniform(0, TAU)
            radius = np.random.normal(0, 0.15)
            dot = Dot(
                point=[radius * np.cos(angle), radius * np.sin(angle), 0],
                radius=0.03,
                color=PROB_RED
            )
            dots.add(dot)
        return VGroup(target, dots)
    
    def show_ending(self):
        """结尾"""
        # 核心总结
        summary = VGroup(
            Text("正态分布的哲学", font_size=36, color=WHITE),
            Text("极端罕见，平庸常见", font_size=42, color=PROB_PURPLE, weight=BOLD),
            Text("这就是世界的本质", font_size=32, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 系列结尾
        self.show_series_ending(
            "从钟形曲线中",
            "我们看到了宇宙的秩序"
        )
    
    def show_series_ending(self, main_message: str, sub_message: str):
        """显示系列结尾动画"""
        # 主信息
        main_text = Text(
            main_message,
            font_size=48,
            color=PROB_PURPLE,
            weight=BOLD
       )
       
        # 副信息
        sub_text = Text(
            sub_message,
            font_size=28,
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
       preview_title = Text("下期预告", font_size=36, color=PROB_YELLOW)
       preview_title.to_edge(UP)
       self.play(Write(preview_title))
       
       # EP14 内容预告
       ep14_title = Text(
           "第14集：贝叶斯思维",
           font_size=42,
           color=PROB_PURPLE,
           weight=BOLD
       )
       ep14_title.shift(UP * 0.5)
       
       # 预告内容
       preview_content = VGroup(
           Text("如何像侦探一样思考？", font_size=28, color=WHITE),
           Text("证据如何改变信念", font_size=28, color=WHITE),
           Text("理性决策的终极武器", font_size=32, color=PROB_GREEN, weight=BOLD)
       ).arrange(DOWN, buff=0.4)
       preview_content.next_to(ep14_title, DOWN, buff=0.8)
       
       self.play(Write(ep14_title))
       self.play(Write(preview_content[0]))
       self.play(Write(preview_content[1]))
       self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
       
       # 思考问题
       think_question = Text(
           "医生说你可能生病了，你该相信吗？",
           font_size=24,
           color=PROB_YELLOW
       )
       think_question.next_to(preview_content, DOWN, buff=0.3)
       
       self.play(Write(think_question))
       self.wait(3)
       
       # 期待语
       see_you = Text(
           "下期见！",
           font_size=36,
           color=WHITE
       )
       see_you.move_to(ORIGIN)
       
       self.play(
           FadeOut(preview_title), FadeOut(ep14_title),
           FadeOut(preview_content), FadeOut(think_question),
           Write(see_you)
       )
       self.wait(2)
       self.play(FadeOut(see_you))
