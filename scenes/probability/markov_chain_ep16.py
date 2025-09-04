"""
EP16: 马尔可夫链
未来只取决于现在，不在乎过去
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple

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


class MarkovChainEP16(Scene):
    """马尔可夫链 - 概率论系列 EP16"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(16, "马尔可夫链")
        
        # 2. 问题引入 - 天气预报
        self.introduce_weather_prediction()
        
        # 3. 马尔可夫性质
        self.markov_property()
        
        # 4. 转移矩阵
        self.transition_matrix()
        
        # 5. 天气模型演示
        self.weather_model_demo()
        
        # 6. 稳态分布
        self.steady_state_distribution()
        
        # 7. PageRank算法
        self.pagerank_algorithm()
        
        # 8. 现实应用
        self.real_world_applications()
        
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
    
    def introduce_weather_prediction(self):
        """引入问题 - 天气预报"""
        self.clear()
        
        title = Text("一个日常问题", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：天气图标
        weather_icons = self.create_weather_icons()
        weather_icons.shift(LEFT * 3.5)
        self.play(Create(weather_icons))
        
        # 右侧：问题
        questions = VGroup(
            Text("明天会下雨吗？", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("气象学家如何预测？", font_size=NORMAL_SIZE, color=WHITE),
            Text("为什么只看今天就够了？", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.5)
        questions.shift(RIGHT * 3.5)
        
        for q in questions:
            self.play(Write(q), run_time=0.8)
        
        # 关键洞察
        insight = Text(
            "秘密：天气有短期记忆",
            font_size=SUBTITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        insight.shift(DOWN * 2.5)
        self.play(Write(insight))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(weather_icons),
            FadeOut(questions), FadeOut(insight)
        )
    
    def create_weather_icons(self):
        """创建天气图标"""
        icons = VGroup()
        
        # 晴天
        sun = VGroup(
            Circle(radius=0.3, fill_color=PROB_YELLOW, fill_opacity=1),
            *[Line(
                0.4 * np.array([np.cos(a), np.sin(a), 0]),
                0.6 * np.array([np.cos(a), np.sin(a), 0]),
                color=PROB_YELLOW,
                stroke_width=3
            ) for a in np.linspace(0, TAU, 8, endpoint=False)]
        )
        sun.shift(UP * 1.5)
        sun_label = Text("晴天", font_size=SMALL_SIZE)
        sun_label.next_to(sun, DOWN, buff=0.2)
        
        # 多云
        cloud = VGroup(
            *[Circle(
                radius=0.25,
                fill_color=GRAY,
                fill_opacity=0.7,
                stroke_width=0
            ).shift(RIGHT * i * 0.2) for i in range(3)]
        )
        cloud_label = Text("多云", font_size=SMALL_SIZE)
        cloud_label.next_to(cloud, DOWN, buff=0.2)
        
        # 雨天
        rain = VGroup(
            # 云
            VGroup(*[Circle(
                radius=0.2,
                fill_color=DARK_GRAY,
                fill_opacity=0.8,
                stroke_width=0
            ).shift(RIGHT * i * 0.15) for i in range(3)]),
            # 雨滴
            *[Line(
                DOWN * 0.3 + RIGHT * i * 0.2,
                DOWN * 0.6 + RIGHT * i * 0.2,
                color=PROB_BLUE,
                stroke_width=2
            ) for i in range(-1, 2)]
        )
        rain.shift(DOWN * 1.5)
        rain_label = Text("雨天", font_size=SMALL_SIZE)
        rain_label.next_to(rain, DOWN, buff=0.2)
        
        icons.add(
            VGroup(sun, sun_label),
            VGroup(cloud, cloud_label),
            VGroup(rain, rain_label)
        )
        return icons
    
    def markov_property(self):
        """马尔可夫性质"""
        self.clear()
        
        title = Text("马尔可夫性质：无记忆性", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 时间线
        timeline = self.create_timeline()
        timeline.shift(UP * 0.5)
        self.play(Create(timeline))
        
        # 马尔可夫性质公式
        markov_formula = MathTex(
            r"P(X_{t+1} | X_t, X_{t-1}, ..., X_0) = P(X_{t+1} | X_t)"
        ).scale(1.2)
        markov_formula.shift(DOWN * 0.8)
        
        self.play(Write""" """  """ """(markov_formula))
        
        # 通俗解释
        explanation = VGroup(
            Text("用人话说就是：", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("未来只取决于现在", font_size=SUBTITLE_SIZE, color=PROB_GREEN),
            Text("不在乎你是怎么到现在的", font_size=NORMAL_SIZE, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(DOWN * 2.5)
        
        for line in explanation:
            self.play(Write(line), run_time=0.8)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(timeline),
            FadeOut(markov_formula), FadeOut(explanation)
        )
    
    def create_timeline(self):
        """创建时间线"""
        timeline = VGroup()
        
        # 主线
        main_line = Arrow(
            LEFT * 5, RIGHT * 5,
            color=WHITE,
            stroke_width=2
        )
        
        # 时间点
        times = ["过去", "...", "昨天", "今天", "明天"]
        positions = [-4, -2, 0, 2, 4]
        
        for time, pos in zip(times, positions):
            # 点
            dot = Dot([pos, 0, 0], radius=0.1, color=PROB_BLUE)
            # 标签
            label = Text(time, font_size=SMALL_SIZE)
            label.next_to(dot, DOWN, buff=0.3)
            
            timeline.add(dot, label)
        
        # 强调今天和明天
        today_highlight = Circle(
            radius=0.3,
            color=PROB_YELLOW,
            stroke_width=3
        ).move_to([2, 0, 0])
        
        tomorrow_highlight = Circle(
            radius=0.3,
            color=PROB_GREEN,
            stroke_width=3
        ).move_to([4, 0, 0])
        
        timeline.add(main_line, today_highlight, tomorrow_highlight)
        return timeline
    
    def transition_matrix(self):
        """转移矩阵"""
        self.clear()
        
        title = Text("转移矩阵：状态的跳跃规则", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：状态转移图
        transition_graph = self.create_transition_graph()
        transition_graph.shift(LEFT * 3.5)
        self.play(Create(transition_graph))
        
        # 右侧：转移矩阵
        matrix_title = Text("转移概率矩阵", font_size=NORMAL_SIZE, color=PROB_YELLOW)
        matrix_title.move_to([3.5, 2.5, 0])
        
        # 矩阵
        matrix = Matrix(
            [
                ["0.7", "0.2", "0.1"],
                ["0.3", "0.4", "0.3"],
                ["0.2", "0.3", "0.5"]
            ],
            element_alignment_corner=ORIGIN,
            left_bracket="[",
            right_bracket="]"
        ).scale(0.8)
        matrix.move_to([3.5, 0.5, 0])
        
        # 标签
        row_labels = VGroup(
            Text("晴", font_size=SMALL_SIZE),
            Text("云", font_size=SMALL_SIZE),
            Text("雨", font_size=SMALL_SIZE)
        ).arrange(DOWN, buff=0.55)
        row_labels.next_to(matrix, LEFT, buff=0.3)
        
        col_labels = VGroup(
            Text("晴", font_size=SMALL_SIZE),
            Text("云", font_size=SMALL_SIZE),
            Text("雨", font_size=SMALL_SIZE)
        ).arrange(RIGHT, buff=0.7)
        col_labels.next_to(matrix, UP, buff=0.3)
        
        self.play(Write(matrix_title))
        self.play(Create(matrix))
        self.play(Write(row_labels), Write(col_labels))
        
        # 解释某个元素
        highlight = SurroundingRectangle(
            matrix.get_entries()[2],
            color=PROB_GREEN,
            stroke_width=3
        )
        
        explanation = Text(
            "晴→雨的概率 = 0.1",
            font_size=SMALL_SIZE,
            color=PROB_GREEN
        )
        explanation.move_to([3.5, -1.5, 0])
        
        self.play(Create(highlight))
        self.play(Write(explanation))
        
        # 关键性质
        property_text = Text(
            "每行之和 = 1",
            font_size=NORMAL_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        property_text.move_to([3.5, -2.5, 0])
        self.play(Write(property_text))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(transition_graph),
            FadeOut(matrix_title), FadeOut(matrix),
            FadeOut(row_labels), FadeOut(col_labels),
            FadeOut(highlight), FadeOut(explanation),
            FadeOut(property_text)
        )
    
    def create_transition_graph(self):
        """创建状态转移图"""
        graph = VGroup()
        
        # 三个状态节点
        states = []
        state_names = ["晴", "云", "雨"]
        colors = [PROB_YELLOW, GRAY, PROB_BLUE]
        positions = [
            [0, 1.5, 0],
            [-1.3, -0.75, 0],
            [1.3, -0.75, 0]
        ]
        
        for name, color, pos in zip(state_names, colors, positions):
            state = VGroup(
                Circle(radius=0.5, fill_color=color, fill_opacity=0.7),
                Text(name, font_size=NORMAL_SIZE, color=WHITE)
            )
            state.move_to(pos)
            states.append(state)
            graph.add(state)
        
        # 转移箭头和概率
        transitions = [
            (0, 0, 0.7, "0.7"),  # 晴→晴
            (0, 1, 0.2, "0.2"),  # 晴→云
            (0, 2, 0.1, "0.1"),  # 晴→雨
            (1, 0, 0.3, "0.3"),  # 云→晴
            (1, 1, 0.4, "0.4"),  # 云→云
            (1, 2, 0.3, "0.3"),  # 云→雨
            (2, 0, 0.2, "0.2"),  # 雨→晴
            (2, 1, 0.3, "0.3"),  # 雨→云
            (2, 2, 0.5, "0.5"),  # 雨→雨
        ]
        
        for from_idx, to_idx, prob, label in transitions:
            if from_idx == to_idx:
                # 自环
                angle = [PI/2, -PI/2, -PI/2][from_idx]
                arc = Arc(
                    radius=0.3,
                    start_angle=angle - PI/3,
                    angle=2*PI/3,
                    color=WHITE,
                    stroke_width=2
                )
                arc.move_to(states[from_idx].get_center() + 0.7 * np.array([
                    np.cos(angle), np.sin(angle), 0
                ]))
                graph.add(arc)
                
                # 概率标签
                prob_label = Text(label, font_size=16, color=PROB_GREEN)
                prob_label.move_to(arc.get_center() + 0.3 * np.array([
                    np.cos(angle), np.sin(angle), 0
                ]))
                graph.add(prob_label)
            else:
                # 普通箭头
                start = states[from_idx].get_center()
                end = states[to_idx].get_center()
                
                # 调整起点和终点，避免重叠
                direction = end - start
                direction = direction / np.linalg.norm(direction)
                start = start + direction * 0.5
                end = end - direction * 0.5
                
                arrow = Arrow(
                    start, end,
                    color=WHITE,
                    stroke_width=2,
                    buff=0
                )
                graph.add(arrow)
                
                # 概率标签
                prob_label = Text(label, font_size=16, color=PROB_GREEN)
                prob_label.move_to((start + end) / 2 + 0.3 * np.array([
                    -direction[1], direction[0], 0
                ]))
                graph.add(prob_label)
        
        return graph
    
    def weather_model_demo(self):
        """天气模型演示"""
        self.clear()
        
        title = Text("让我们预测一周的天气", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建一周的格子
        week_grid = self.create_week_grid()
        week_grid.shift(UP * 0.5)
        self.play(Create(week_grid))
        
        # 转移概率提示（简化版）
        prob_reminder = VGroup(
            Text("转移概率：", font_size=SMALL_SIZE, color=PROB_YELLOW),
            Text("晴→晴:70%  晴→云:20%  晴→雨:10%", font_size=16),
            Text("云→晴:30%  云→云:40%  云→雨:30%", font_size=16),
            Text("雨→晴:20%  雨→云:30%  雨→雨:50%", font_size=16)
        ).arrange(DOWN, buff=0.2)
        prob_reminder.shift(DOWN * 2)
        self.play(Write(prob_reminder))
        
        # 模拟一周天气
        self.simulate_week_weather(week_grid)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(week_grid),
            FadeOut(prob_reminder)
        )
    
    def create_week_grid(self):
        """创建一周的格子"""
        grid = VGroup()
        
        days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        
        for i, day in enumerate(days):
            # 日期框
            box = Rectangle(
                width=1.5, height=1.5,
                stroke_color=WHITE,
                stroke_width=2
            )
            box.shift(RIGHT * (i - 3) * 1.6)
            
            # 日期标签
            label = Text(day, font_size=SMALL_SIZE)
            label.next_to(box, UP, buff=0.2)
            
            grid.add(VGroup(box, label))
        
        return grid
    
    def simulate_week_weather(self, week_grid):
        """模拟一周天气"""
        # 转移矩阵
        P = np.array([
            [0.7, 0.2, 0.1],  # 晴
            [0.3, 0.4, 0.3],  # 云
            [0.2, 0.3, 0.5]   # 雨
        ])
        
        # 天气图标（简化版）
        weather_icons = {
            0: ("☀", PROB_YELLOW, "晴"),
            1: ("☁", GRAY, "云"),
            2: ("🌧", PROB_BLUE, "雨")
        }
        
        # 初始状态（周一晴天）
        current_state = 0
        
        for i in range(7):
            # 获取图标和颜色
            icon, color, name = weather_icons[current_state]
            
            # 创建天气图标
            weather = Text(name, font_size=SUBTITLE_SIZE, color=color)
            weather.move_to(week_grid[i][0].get_center())
            
            self.play(Write(weather), run_time=0.5)
            
            # 如果不是最后一天，计算下一天
            if i < 6:
                # 根据概率选择下一个状态
                probs = P[current_state]
                current_state = np.random.choice(3, p=probs)
                
                # 显示转移箭头
                arrow = Arrow(
                    week_grid[i][0].get_right(),
                    week_grid[i+1][0].get_left(),
                    color=PROB_GREEN,
                    stroke_width=2,
                    buff=0.1
                )
                self.play(Create(arrow), run_time=0.3)
                self.play(FadeOut(arrow), run_time=0.2)
    
    def steady_state_distribution(self):
        """稳态分布"""
        self.clear()
        
        title = Text("长期来看：稳态分布", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：迭代过程
        iteration_viz = self.create_iteration_visualization()
        iteration_viz.shift(LEFT * 3.5)
        self.play(Create(iteration_viz))
        
        # 右侧：收敛图
        convergence_plot = self.create_convergence_plot()
        convergence_plot.shift(RIGHT * 3.5)
        self.play(Create(convergence_plot))
        
        # 结论
        conclusion = VGroup(
            Text("无论从哪个状态开始", font_size=NORMAL_SIZE),
            Text("最终都会收敛到同一个分布", font_size=NORMAL_SIZE, color=PROB_GREEN),
            Text("晴:40%  云:35%  雨:25%", font_size=SUBTITLE_SIZE, color=PROB_PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        conclusion.shift(DOWN * 2.5)
        
        for line in conclusion:
            self.play(Write(line), run_time=0.8)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(iteration_viz),
            FadeOut(convergence_plot), FadeOut(conclusion)
        )
    
    def create_iteration_visualization(self):
        """创建迭代可视化"""
        viz = VGroup()
        
        # 标题
        title = Text("概率分布演化", font_size=NORMAL_SIZE, color=PROB_YELLOW)
        title.shift(UP * 2)
        
        # 初始分布
        initial = VGroup(
            Text("初始:", font_size=SMALL_SIZE),
            Text("[1, 0, 0]", font_size=SMALL_SIZE, color=PROB_BLUE)
        ).arrange(RIGHT, buff=0.3)
        initial.shift(UP * 1)
        
        # 几次迭代后
        iter5 = VGroup(
            Text("5天后:", font_size=SMALL_SIZE),
            Text("[0.5, 0.3, 0.2]", font_size=SMALL_SIZE, color=PROB_BLUE)
        ).arrange(RIGHT, buff=0.3)
        
        iter10 = VGroup(
            Text("10天后:", font_size=SMALL_SIZE),
            Text("[0.42, 0.34, 0.24]", font_size=SMALL_SIZE, color=PROB_BLUE)
        ).arrange(RIGHT, buff=0.3)
        iter10.shift(DOWN * 1)
        
        iter_inf = VGroup(
            Text("∞天后:", font_size=SMALL_SIZE),
            Text("[0.4, 0.35, 0.25]", font_size=SMALL_SIZE, color=PROB_GREEN)
        ).arrange(RIGHT, buff=0.3)
        iter_inf.shift(DOWN * 2)
        
        viz.add(title, initial, iter5, iter10, iter_inf)
        
        # 添加箭头
        for i in range(3):
            arrow = Arrow(
                UP * (1 - i) + DOWN * 0.3,
                UP * (0 - i) + UP * 0.3,
                color=GRAY,
                stroke_width=2
            )
            viz.add(arrow)
        
        return viz
    
    def create_convergence_plot(self):
        """创建收敛图"""
        # 简化的坐标系
        axes = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 1, 0.2],
            x_length=4,
            y_length=3,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 14
            }
        )
        
        x_label = Text("天数", font_size=16).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("概率", font_size=16).next_to(axes.y_axis, LEFT, buff=0.2).rotate(PI/2)
        
        # 三条收敛曲线
        t = np.linspace(0, 20, 100)
        
        # 晴天概率曲线（从1开始，收敛到0.4）
        sunny_curve = axes.plot_line_graph(
            x_values=t,
            y_values=0.4 + 0.6 * np.exp(-t/5),
            line_color=PROB_YELLOW,
            stroke_width=2,
            add_vertex_dots=False
        )
        
        # 多云概率曲线（从0开始，收敛到0.35）
        cloudy_curve = axes.plot_line_graph(
            x_values=t,
            y_values=0.35 * (1 - np.exp(-t/5)),
            line_color=GRAY,
            stroke_width=2,
            add_vertex_dots=False
        )
        
        # 雨天概率曲线（从0开始，收敛到0.25）
        rainy_curve = axes.plot_line_graph(
            x_values=t,
            y_values=0.25 * (1 - np.exp(-t/5)),
            line_color=PROB_BLUE,
            stroke_width=2,
            add_vertex_dots=False
        )
        
        # 稳态线
        steady_lines = VGroup(
            DashedLine(
                axes.c2p(0, 0.4), axes.c2p(20, 0.4),
                color=PROB_YELLOW, stroke_width=1
            ),
            DashedLine(
                axes.c2p(0, 0.35), axes.c2p(20, 0.35),
                color=GRAY, stroke_width=1
            ),
            DashedLine(
                axes.c2p(0, 0.25), axes.c2p(20, 0.25),
                color=PROB_BLUE, stroke_width=1
            )
        )
        
        return VGroup(axes, x_label, y_label, sunny_curve, cloudy_curve, rainy_curve, steady_lines)
    
    def pagerank_algorithm(self):
        """PageRank算法"""
        self.clear()
        
        title = Text("Google的秘密武器：PageRank", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建网页链接图
        web_graph = self.create_web_graph()
        web_graph.shift(LEFT * 3)
        self.play(Create(web_graph))
        
        # 右侧：算法说明
        algorithm_explanation = VGroup(
            Text("PageRank原理", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("1. 网页是状态", font_size=SMALL_SIZE),
            Text("2. 链接是转移", font_size=SMALL_SIZE),
            Text("3. 随机冲浪者模型", font_size=SMALL_SIZE),
            Text("4. 稳态 = 重要性", font_size=SMALL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        algorithm_explanation.shift(RIGHT * 3.5 + UP * 0.5)
        
        for line in algorithm_explanation:
            self.play(Write(line), run_time=0.6)
        
        # 模拟随机冲浪者
        self.simulate_random_surfer(web_graph)
        
        # 显示PageRank值
        pagerank_values = Text(
            "最终排名：A > C > B > D",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        pagerank_values.shift(DOWN * 2.5)
        self.play(Write(pagerank_values))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(web_graph),
            FadeOut(algorithm_explanation), FadeOut(pagerank_values)
        )
    
    def create_web_graph(self):
        """创建网页链接图"""
        graph = VGroup()
        
        # 四个网页节点
        pages = []
        page_names = ["A", "B", "C", "D"]
        positions = [
            [-1, 1, 0],
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0]
        ]
        
        for name, pos in zip(page_names, positions):
            page = VGroup(
                Circle(radius=0.4, fill_color=PROB_BLUE, fill_opacity=0.7),
                Text(name, font_size=NORMAL_SIZE, color=WHITE)
            )
            page.move_to(pos)
            pages.append(page)
            graph.add(page)
        
        # 链接关系（箭头）
        links = [
            (0, 1),  # A → B
            (0, 2),  # A → C
            (1, 2),  # B → C
            (2, 0),  # C → A
            (2, 3),  # C → D
            (3, 0),  # D → A
            (3, 2),  # D → C
        ]
        
        for from_idx, to_idx in links:
            start = pages[from_idx].get_center()
            end = pages[to_idx].get_center()
            
            # 调整起点和终点
            direction = end - start
            direction = direction / np.linalg.norm(direction)
            start = start + direction * 0.4
            end = end - direction * 0.4
            
            arrow = Arrow(
                start, end,
                color=GRAY,
                stroke_width=2,
                buff=0,
                max_tip_length_to_length_ratio=0.15
            )
            graph.add(arrow)
        
        return graph
    
    def simulate_random_surfer(self, web_graph):
        """模拟随机冲浪者"""
        # 创建冲浪者（小圆点）
        surfer = Dot(
            web_graph[0].get_center(),
            radius=0.15,
            color=PROB_YELLOW
        )
        self.play(Create(surfer))
        
        # 访问计数
        visit_counts = [0, 0, 0, 0]
        
        # 模拟20步
        current_page = 0
        
        # 链接关系字典
        links = {
            0: [1, 2],     # A可以去B和C
            1: [2],        # B可以去C
            2: [0, 3],     # C可以去A和D
            3: [0, 2]      # D可以去A和C
        }
        
        for _ in range(20):
            visit_counts[current_page] += 1
            
            # 选择下一个页面
            next_pages = links[current_page]
            next_page = random.choice(next_pages)
            
            # 移动冲浪者
            self.play(
                surfer.animate.move_to(web_graph[next_page].get_center()),
                run_time=0.3
            )
            
            current_page = next_page
        
        self.play(FadeOut(surfer))
    
    def real_world_applications(self):
        """现实应用"""
        self.clear()
        
        title = Text("马尔可夫链的应用", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 应用网格
        applications = VGroup()
        
        # 1. 文本生成
        text_gen = self.create_application_card(
            "文本生成",
            PROB_BLUE,
            [
                "预测下一个词",
                "手机输入法",
                "ChatGPT的基础"
            ]
        )
        text_gen.shift(LEFT * 5 + UP * 1)
        
        # 2. 金融建模
        finance = self.create_application_card(
            "金融建模",
            PROB_GREEN,
            [
                "信用评级转移",
                "股市状态切换",
                "风险评估"
            ]
        )
        finance.shift(LEFT * 1.7 + UP * 1)
        
        # 3. 生物信息
        bio = self.create_application_card(
            "生物信息",
            PROB_YELLOW,
            [
                "DNA序列分析",
                "蛋白质折叠",
                "进化模型"
            ]
        )
        bio.shift(RIGHT * 1.7 + UP * 1)
        
        # 4. 排队论
        queue = self.create_application_card(
            "排队系统",
            PROB_RED,
            [
                "客服中心",
                "网络流量",
                "医院调度"
            ]
        )
        queue.shift(RIGHT * 5 + UP * 1)
        
        applications.add(text_gen, finance, bio, queue)
        
        # 逐个显示
        for app in applications:
            self.play(FadeIn(app, shift=UP), run_time=0.5)
        
        # 核心思想
        core_idea = Text(
            "只要满足无记忆性，就能用马尔可夫链建模",
            font_size=NORMAL_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        core_idea.shift(DOWN * 2.5)
        self.play(Write(core_idea))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(applications), FadeOut(core_idea))
    
    def create_application_card(self, title: str, color, points: List[str]):
        """创建应用卡片"""
        card = VGroup()
        
        # 背景
        bg = RoundedRectangle(
            width=3, height=2.5,
            corner_radius=0.2,
            fill_color=color,
            fill_opacity=0.2,
            stroke_color=color,
            stroke_width=2
        )
        
        # 标题
        title_text = Text(title, font_size=NORMAL_SIZE, color=color, weight=BOLD)
        title_text.shift(UP * 0.8)
        
        # 要点
        points_text = VGroup()
        for point in points:
            point_text = Text(f"• {point}", font_size=SMALL_SIZE, color=WHITE)
            points_text.add(point_text)
        points_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        points_text.shift(DOWN * 0.2)
        
        card.add(bg, title_text, points_text)
        return card
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        # 核心总结
        summary = VGroup(
            Text("马尔可夫链告诉我们：", font_size=38, color=WHITE),
            Text("历史不重要，当下最关键", font_size=TITLE_SIZE, color=PROB_PURPLE, weight=BOLD),
            Text("这就是无记忆性的力量", font_size=34, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 三个核心概念回顾
        review = VGroup(
            Text("记住三个要点：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("1. 马尔可夫性质：未来只依赖现在", font_size=NORMAL_SIZE),
            Text("2. 转移矩阵：状态跳跃的规则", font_size=NORMAL_SIZE),
            Text("3. 稳态分布：长期的必然", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.4)
        
        for line in review:
            self.play(Write(line), run_time=0.8)
        
        self.wait(3)
        self.play(FadeOut(review))
        
        # 系列结尾
        self.show_series_ending(
            "从随机到确定",
            "这就是概率的魅力"
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
        
        # EP17 内容预告
        ep17_title = Text(
            "第17集：泊松分布",
            font_size=TITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep17_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("为什么排队总是这么久？", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("地震发生有规律吗？", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("稀有事件的数学", font_size=34, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep17_title, DOWN, buff=0.8)
        
        self.play(Write(ep17_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "公交车为什么总是一起来？",
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
            FadeOut(preview_title), FadeOut(ep17_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))