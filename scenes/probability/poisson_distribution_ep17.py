"""
EP17: 泊松分布
稀有事件的数学规律
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple
from scipy.stats import poisson

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


class PoissonDistributionEP17(Scene):
    """泊松分布 - 概率论系列 EP17"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(17, "泊松分布")
        
        # 2. 问题引入 - 公交车悖论
        self.introduce_bus_paradox()
        
        # 3. 泊松过程的本质
        self.poisson_process_essence()
        
        # 4. 泊松分布公式
        self.poisson_distribution_formula()
        
        # 5. 排队系统模拟
        self.queue_system_simulation()
        
        # 6. 参数λ的意义
        self.lambda_parameter_meaning()
        
        # 7. 实验验证 - 放射性衰变
        self.radioactive_decay_experiment()
        
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
    
    def introduce_bus_paradox(self):
        """引入问题 - 公交车悖论"""
        self.clear()
        
        title = Text("为什么公交车总是一起来？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        
        # 创建公交站场景 - 左侧
        bus_stop_scene = self.create_bus_stop_scene()
        bus_stop_scene.shift(LEFT * 3.5 + UP * 0.3)
        self.play(Create(bus_stop_scene), run_time=1.5)
        
        # 右侧：常见现象
        observations = VGroup(
            Text("日常观察：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW, weight=BOLD),
            Text("· 等了20分钟没车", font_size=NORMAL_SIZE),
            Text("· 突然来了3辆", font_size=NORMAL_SIZE),
            Text("· 明明10分钟一班", font_size=NORMAL_SIZE, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        observations.shift(RIGHT * 3.5 + UP * 0.3)
        
        for obs in observations:
            self.play(Write(obs), run_time=0.8)
        
        # 揭示真相 - 放在底部
        revelation = Text(
            "这不是运气差，是数学规律！",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        revelation.shift(DOWN * 2.5)
        self.play(Write(revelation), run_time=1.5)
        self.play(revelation.animate.scale(1.1), run_time=0.5)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(bus_stop_scene),
            FadeOut(observations), FadeOut(revelation)
        )
    
    def create_bus_stop_scene(self):
        """创建公交站场景"""
        scene = VGroup()
        
        # 时间轴
        timeline = Arrow(
            LEFT * 2, RIGHT * 2,
            color=WHITE,
            stroke_width=2
        )
        
        # 时间标记
        time_labels = VGroup()
        for i, t in enumerate([0, 10, 20, 30]):
            label = Text(f"{t}min", font_size=14)
            label.next_to(timeline.get_start() + RIGHT * i * 1.33, DOWN, buff=0.15)
            time_labels.add(label)
        
        # 公交车图标（聚集现象）
        buses = VGroup()
        bus_times = [22, 23, 24]  # 聚集在一起
        for t in bus_times:
            bus = VGroup(
                Rectangle(width=0.4, height=0.3, fill_color=PROB_YELLOW, fill_opacity=0.8),
                Text("B", font_size=10, color=BLACK)
            )
            bus[1].move_to(bus[0])
            bus.move_to(timeline.get_start() + RIGHT * (t/30 * 4) + UP * 0.4)
            buses.add(bus)
        
        # 等待的人
        people = VGroup()
        for i in range(5):
            person = Circle(radius=0.12, fill_color=WHITE, fill_opacity=0.8)
            person.shift(DOWN * 1.2 + LEFT * 1 + RIGHT * i * 0.3)
            people.add(person)
        
        # 标签
        label = Text("公交站", font_size=16, color=PROB_BLUE)
        label.shift(DOWN * 1.8)
        
        scene.add(timeline, time_labels, buses, people, label)
        return scene
    
    def poisson_process_essence(self):
        """泊松过程的本质"""
        self.clear()
        
        title = Text("泊松过程：稀有事件的模型", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        
        # 左侧：三个核心假设 - 调整位置避免太靠下
        assumptions = VGroup(
            Text("三个关键假设", font_size=SUBTITLE_SIZE, color=PROB_YELLOW, weight=BOLD),
            Text("1. 独立性", font_size=NORMAL_SIZE, color=PROB_BLUE),
            Text("   事件相互独立", font_size=SMALL_SIZE),
            Text("2. 平稳性", font_size=NORMAL_SIZE, color=PROB_GREEN),
            Text("   发生率恒定", font_size=SMALL_SIZE),
            Text("3. 稀有性", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("   短时间最多一个", font_size=SMALL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        assumptions.shift(LEFT * 3.5 + UP * 0.2)
        
        for assumption in assumptions:
            self.play(Write(assumption), run_time=0.8)
        
        # 右侧：时间轴演示
        timeline_demo = self.create_poisson_timeline()
        timeline_demo.shift(RIGHT * 3.5 + UP * 0.2)
        self.play(Create(timeline_demo), run_time=1.5)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(assumptions), FadeOut(timeline_demo))
    
    def create_poisson_timeline(self):
        """创建泊松过程时间轴"""
        demo = VGroup()
        
        # 时间轴
        timeline = Arrow(
            LEFT * 2, RIGHT * 2,
            color=WHITE,
            stroke_width=2
        )
        
        # 随机事件点
        event_times = np.random.exponential(0.5, 8).cumsum()
        event_times = event_times[event_times < 4] * 1 - 2
        
        events = VGroup()
        for t in event_times:
            event = Dot(
                [t, 0, 0],
                radius=0.1,
                color=PROB_RED
            )
            events.add(event)
        
        # 间隔标注
        intervals = VGroup()
        for i in range(min(len(event_times) - 1, 3)):  # 最多显示3个间隔
            interval = DoubleArrow(
                [event_times[i], -0.4, 0],
                [event_times[i+1], -0.4, 0],
                color=PROB_GREEN,
                stroke_width=1,
                buff=0
            )
            intervals.add(interval)
        
        # 标签
        label = Text("间隔：指数分布", font_size=SMALL_SIZE, color=PROB_GREEN)
        label.shift(DOWN * 1)
        
        demo.add(timeline, events, intervals, label)
        return demo
    
    def poisson_distribution_formula(self):
        """泊松分布公式 - 修复重叠问题"""
        self.clear()
        
        title = Text("泊松分布的数学表达", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        
        # 左侧：公式推导 - 调整位置和大小
        formula_group = VGroup()
        
        # 主公式
        main_formula = MathTex(
            r"P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}"
        ).scale(1.1)  # 减小尺寸
        main_formula.set_color(PROB_PURPLE)
        
        # 期望和方差
        expectation = MathTex(r"E[X] = \lambda").scale(0.9)
        variance = MathTex(r"Var(X) = \lambda").scale(0.9)
        
        expectation.next_to(main_formula, DOWN, buff=0.4)
        variance.next_to(expectation, DOWN, buff=0.3)
        
        # 特殊性质
        special_property = Text(
            "均值 = 方差",
            font_size=SMALL_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        special_property.next_to(variance, DOWN, buff=0.4)
        
        formula_group.add(main_formula, expectation, variance, special_property)
        formula_group.shift(LEFT * 3.5 + UP * 0.5)  # 整体上移
        
        self.play(Write(main_formula), run_time=2)
        self.play(Write(expectation), run_time=1)
        self.play(Write(variance), run_time=1)
        self.play(Write(special_property), run_time=1)
        self.play(special_property.animate.scale(1.1), run_time=0.5)
        
        # 右侧：分布图 - 调整位置和大小
        distribution_plot = self.create_poisson_plot()
        distribution_plot.shift(RIGHT * 3.5 + UP * 0.5)  # 整体上移
        self.play(Create(distribution_plot), run_time=2)
        
        # 参数说明 - 调整到合适位置
        param_explanation = VGroup(
            MathTex(r"\lambda = ", "\\text{rate}").set_color(PROB_YELLOW).scale(0.9),
            MathTex(r"k = ", "\\text{count}").set_color(PROB_BLUE).scale(0.9),
            MathTex(r"e = ", "2.718...").set_color(PROB_GREEN).scale(0.9)
        ).arrange(RIGHT, buff=1)
        param_explanation.shift(DOWN * 2.8)  # 不要太靠下
        
        for param in param_explanation:
            self.play(Write(param), run_time=0.8)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(formula_group),
            FadeOut(distribution_plot), FadeOut(param_explanation)
        )
    
    def create_poisson_plot(self):
        """创建泊松分布图 - 缩小尺寸"""
        # 坐标轴 - 缩小
        axes = Axes(
            x_range=[0, 15, 5],
            y_range=[0, 0.25, 0.1],
            x_length=4,  # 缩小
            y_length=2.5,  # 缩小
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 14,
                "decimal_number_config": {"num_decimal_places": 1}
            }
        )
        
        x_label = MathTex("k").scale(0.8).next_to(axes.x_axis, DOWN, buff=0.15)
        y_label = MathTex("P(X=k)").scale(0.8).next_to(axes.y_axis, LEFT, buff=0.15)
        
        # 绘制不同λ的分布
        plots = VGroup()
        lambdas = [2, 5, 8]
        colors = [PROB_BLUE, PROB_GREEN, PROB_YELLOW]
        
        for lam, color in zip(lambdas, colors):
            bars = VGroup()
            for k in range(16):
                prob = poisson.pmf(k, lam)
                if prob > 0.001:
                    bar = Rectangle(
                        width=0.2,  # 缩小
                        height=prob * 10,  # 缩放到坐标系
                        fill_color=color,
                        fill_opacity=0.7,
                        stroke_width=0.5
                    )
                    bar.move_to(axes.c2p(k, prob/2))
                    bars.add(bar)
            plots.add(bars)
        
        # 图例 - 缩小并调整位置
        legend = VGroup()
        for i, (lam, color) in enumerate(zip(lambdas, colors)):
            legend_item = VGroup(
                Square(side_length=0.15, fill_color=color, fill_opacity=0.7),
                MathTex(f"\\lambda = {lam}").scale(0.7)
            ).arrange(RIGHT, buff=0.1)
            legend_item.shift(UP * (0.8 - i * 0.3))
            legend.add(legend_item)
        legend.shift(RIGHT * 1.5)
        
        return VGroup(axes, x_label, y_label, plots, legend)
    
    def queue_system_simulation(self):
        """排队系统模拟 - 修复重叠问题"""
        self.clear()
        
        title = Text("银行排队系统模拟", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        
        # 创建银行场景 - 调整位置避免重叠
        bank_scene = self.create_bank_scene()
        bank_scene.shift(UP * 0.2)  # 稍微上移
        self.play(Create(bank_scene), run_time=1.5)
        
        # 模拟顾客到达和服务
        self.simulate_queue_system(bank_scene)
        
        # 统计结果 - 调整位置确保不重叠
        stats = VGroup(
            Text("统计结果", font_size=26, color=PROB_YELLOW, weight=BOLD),
            Text("平均到达率：λ = 3人/分钟", font_size=20),
            Text("平均等待时间：2.5分钟", font_size=20),
            Text("最大队长：7人", font_size=20, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        stats.shift(DOWN * 2.5)  # 确保在底部但不超出屏幕
        
        for stat in stats:
            self.play(Write(stat), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(bank_scene), FadeOut(stats))
    
    def create_bank_scene(self):
        """创建银行场景 - 调整布局"""
        scene = VGroup()
        
        # 服务窗口 - 缩小并调整位置
        windows = VGroup()
        for i in range(3):
            window = VGroup(
                Rectangle(width=1.2, height=0.9, stroke_color=PROB_BLUE, stroke_width=2),
                Text(f"窗口{i+1}", font_size=16)
            )
            window[1].move_to(window[0])
            window.shift(RIGHT * (i - 1) * 2 + UP * 0.8)
            windows.add(window)
        
        # 等待区 - 调整大小和位置
        waiting_area = Rectangle(
            width=6, height=1.5,
            stroke_color=PROB_GRAY,
            stroke_width=2,
            stroke_opacity=0.5
        )
        waiting_area.shift(DOWN * 0.8)
        
        # 等待位置标记 - 调整位置
        queue_positions = VGroup()
        for i in range(6):
            pos = Circle(
                radius=0.12,
                stroke_color=PROB_GRAY,
                stroke_width=1,
                fill_opacity=0
            )
            pos.shift(LEFT * 2.5 + RIGHT * i * 1 + DOWN * 0.8)
            queue_positions.add(pos)
        
        scene.add(windows, waiting_area, queue_positions)
        return scene
    
    def simulate_queue_system(self, bank_scene):
        """模拟排队系统 - 调整动画位置"""
        customers = VGroup()
        
        # 模拟6个顾客（减少数量以避免拥挤）
        for i in range(6):
            # 顾客到达
            customer = Circle(
                radius=0.18,
                fill_color=PROB_GREEN,
                fill_opacity=0.8
            )
            
            # 初始位置
            customer.move_to(LEFT * 3.5 + DOWN * 0.8)
            self.play(FadeIn(customer), run_time=0.2)
            
            # 移动到队列
            queue_pos = LEFT * 2.5 + RIGHT * (i % 6) * 1 + DOWN * 0.8
            self.play(customer.animate.move_to(queue_pos), run_time=0.4)
            customers.add(customer)
            
            # 随机服务顾客
            if i > 2 and random.random() < 0.4 and len(customers) > 0:
                served = customers[0]
                window_pos = UP * 0.8 + RIGHT * random.choice([-2, 0, 2])
                self.play(served.animate.move_to(window_pos), run_time=0.4)
                self.play(FadeOut(served), run_time=0.2)
                customers.remove(served)
                
                # 队列前移
                for j, c in enumerate(customers):
                    new_pos = LEFT * 2.5 + RIGHT * j * 1 + DOWN * 0.8
                    self.play(c.animate.move_to(new_pos), run_time=0.2)
    
    def lambda_parameter_meaning(self):
        """参数λ的意义"""
        self.clear()
        
        title = Text("参数λ：控制一切的关键", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        
        # 左侧：不同λ值的比较 - 调整位置
        lambda_comparison = self.create_lambda_comparison()
        lambda_comparison.shift(LEFT * 3.5 + UP * 1.0)
        self.play(Create(lambda_comparison), run_time=2)
        
        # 右侧：实际例子 - 调整位置和间距
        examples = VGroup(
            Text("实际场景的λ值", font_size=26, color=PROB_YELLOW, weight=BOLD),
            Text("电话呼叫中心", font_size=22),
            Text("  λ = 20次/小时", font_size=18, color=PROB_BLUE),
            Text("地震", font_size=22),
            Text("  λ = 0.1次/年", font_size=18, color=PROB_RED),
            Text("网站访问", font_size=22),
            Text("  λ = 1000次/分钟", font_size=18, color=PROB_GREEN),
            Text("放射性衰变", font_size=22),
            MathTex(r"\lambda = 10^6", "\\text{ /s}").scale(0.7).set_color(PROB_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        examples.shift(RIGHT * 3.5 + UP * 0.3)
        
        for example in examples:
            self.play(Write(example), run_time=0.5)
        
        # 核心洞察 - 调整位置
        insight = Text(
            "λ越大，事件越频繁，分布越对称",
            font_size=28,
            color=PROB_GREEN,
            weight=BOLD
        )
        insight.shift(DOWN * 2.8)
        self.play(Write(insight), run_time=1.5)
        self.play(insight.animate.scale(1.05), run_time=0.5)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(lambda_comparison),
            FadeOut(examples), FadeOut(insight)
        )
    
    def create_lambda_comparison(self):
        """创建λ值比较 - 调整间距"""
        comparison = VGroup()
        
        lambdas = [1, 5, 10]
        titles = ["稀疏 (λ=1)", "中等 (λ=5)", "密集 (λ=10)"]
        colors = [PROB_RED, PROB_YELLOW, PROB_GREEN]
        
        for i, (lam, title, color) in enumerate(zip(lambdas, titles, colors)):
            # 时间轴
            timeline = Line(
                LEFT * 2, RIGHT * 2,
                color=WHITE,
                stroke_width=1
            )
            timeline.shift(DOWN * i * 1.4)  # 减小间距
            
            # 标题
            label = Text(title, font_size=18, color=color)
            label.next_to(timeline, UP, buff=0.15)
            
            # 事件点
            num_events = np.random.poisson(lam * 2)
            num_events = min(num_events, 15)  # 限制最大数量
            event_positions = np.sort(np.random.uniform(-2, 2, num_events))
            
            events = VGroup()
            for pos in event_positions:
                event = Dot(
                    [pos, -i * 1.4, 0],
                    radius=0.06,
                    color=color
                )
                events.add(event)
            
            comparison.add(VGroup(timeline, label, events))

        return comparison
    
    def radioactive_decay_experiment(self):
        """放射性衰变实验"""
        self.clear()
        
        title = Text("经典验证：卢瑟福的放射性实验", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        
        # 左侧：实验装置 - 调整位置
        experiment_setup = self.create_experiment_setup()
        experiment_setup.shift(LEFT * 3.5 + UP * 0.2)
        self.play(Create(experiment_setup), run_time=1.5)
        
        # 右侧：数据对比 - 调整布局
        data_section = VGroup()
        
        # 标题
        data_title = Text(
            "实验 vs 理论",
            font_size=26,
            color=PROB_YELLOW,
            weight=BOLD
        )
        
        # 实验信息
        info = VGroup(
            Text("2608个时间段", font_size=20),
            Text("平均：3.87粒子", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        info.next_to(data_title, DOWN, buff=0.3)
        
        # 数据表格 - 缩小
        table = self.create_data_table()
        table.next_to(info, DOWN, buff=0.3)
        
        data_section.add(data_title, info, table)
        data_section.shift(RIGHT * 3.5 + UP * 1.0)
        
        for element in data_section:
            self.play(Write(element), run_time=0.6)
        
        # 结论 - 调整位置
        conclusion = Text(
            "完美符合泊松分布！",
            font_size=28,
            color=PROB_GREEN,
            weight=BOLD
        )
        conclusion.shift(DOWN * 2.8)
        self.play(Write(conclusion), run_time=1.5)
        self.play(conclusion.animate.scale(1.05), run_time=0.5)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(experiment_setup),
            FadeOut(data_section), FadeOut(conclusion)
        )
    
    def create_experiment_setup(self):
        """创建实验装置 - 调整大小"""
        setup = VGroup()
        
        # 放射源
        source = VGroup(
            Circle(radius=0.3, fill_color=PROB_YELLOW, fill_opacity=0.8),
            MathTex(r"\alpha").scale(0.9)
        )
        source[1].move_to(source[0])
        source.shift(LEFT * 0.8)
        
        # 探测器
        detector = Rectangle(
            width=1, height=2,
            fill_color=PROB_BLUE,
            fill_opacity=0.3,
            stroke_color=PROB_BLUE,
            stroke_width=2
        )
        detector.shift(RIGHT * 1.2)
        
        # 粒子轨迹
        particles = VGroup()
        for i in range(5):
            angle = -PI/6 + i * PI/12
            particle = Arrow(
                source.get_center(),
                source.get_center() + 2 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=PROB_RED,
                stroke_width=1.5,
                max_tip_length_to_length_ratio=0.12
            )
            particles.add(particle)
        
        # 标签
        labels = VGroup(
            Text("α粒子源", font_size=16).next_to(source, DOWN, buff=0.2),
            Text("探测器", font_size=16).next_to(detector, DOWN, buff=0.2),
            Text("7.5秒计数", font_size=16, color=PROB_GRAY).shift(DOWN * 1.5)
        )
        
        setup.add(source, detector, particles, labels)
        return setup
    
    def create_data_table(self):
        """创建数据表格 - 缩小尺寸"""
        table = VGroup()
        
        # 表头
        headers = ["k", "观测", "理论"]
        header_row = VGroup()
        for i, header in enumerate(headers):
            cell = Text(header, font_size=16, color=PROB_YELLOW)
            cell.move_to(RIGHT * (i - 1) * 1.2)
            header_row.add(cell)
        
        # 数据行 - 减少行数
        data_rows = [
            ["0", "57", "54"],
            ["1", "203", "211"],
            ["2", "383", "407"],
            ["3", "525", "525"],
            ["...", "...", "..."]
        ]
        
        rows = VGroup()
        for j, row in enumerate(data_rows):
            row_group = VGroup()
            for i, value in enumerate(row):
                cell = Text(value, font_size=14)
                cell.move_to(RIGHT * (i - 1) * 1.2 + DOWN * (j + 1) * 0.3)
                row_group.add(cell)
            rows.add(row_group)
        
        table.add(header_row, rows)
        return table
    
    def real_world_applications(self):
        """现实应用"""
        self.clear()
        
        title = Text("泊松分布无处不在", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=2)
        
        # 创建应用网格 - 2x2布局，调整位置确保不超出屏幕
        applications = VGroup()
        
        # 1. 服务系统
        service = self.create_application_card(
            "服务系统",
            PROB_BLUE,
            ["呼叫中心", "急诊室", "网络流量"]
        )
        service.shift(LEFT * 3.5 + UP * 0.8)
        
        # 2. 自然现象
        nature = self.create_application_card(
            "自然现象",
            PROB_GREEN,
            ["地震频率", "流星雨", "基因突变"]
        )
        nature.shift(RIGHT * 3.5 + UP * 0.8)
        
        # 3. 商业分析
        business = self.create_application_card(
            "商业分析",
            PROB_YELLOW,
            ["客户到达", "订单处理", "库存管理"]
        )
        business.shift(LEFT * 3.5 + DOWN * 1.2)
        
        # 4. 质量控制
        quality = self.create_application_card(
            "质量控制",
            PROB_RED,
            ["产品缺陷", "故障检测", "可靠性"]
        )
        quality.shift(RIGHT * 3.5 + DOWN * 1.2)
        
        applications.add(service, nature, business, quality)
        
        for app in applications:
            self.play(FadeIn(app, shift=UP * 0.2), run_time=0.5)
        
        # 核心特征 - 确保在屏幕内
        core_feature = Text(
            "共同特征：独立、稀有、恒定率",
            font_size=26,
            color=PROB_PURPLE,
            weight=BOLD
        )
        core_feature.shift(DOWN * 3)
        self.play(Write(core_feature), run_time=1.5)
        self.play(core_feature.animate.scale(1.05), run_time=0.5)
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(applications), FadeOut(core_feature))
    
    def create_application_card(self, title: str, color, points: List[str]):
        """创建应用卡片 - 调整大小"""
        card = VGroup()
        
        # 背景 - 缩小
        bg = RoundedRectangle(
            width=2.8, height=1.6,
            corner_radius=0.15,
            fill_color=color,
            fill_opacity=0.15,
            stroke_color=color,
            stroke_width=2
        )
        
        # 标题
        title_text = Text(title, font_size=20, color=color, weight=BOLD)
        title_text.shift(UP * 0.5)
        
        # 要点 - 缩小字体
        points_text = VGroup()
        for i, point in enumerate(points):
            point_text = Text(f"· {point}", font_size=16)
            point_text.shift(DOWN * (0 + i * 0.3))
            points_text.add(point_text)
        points_text.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        points_text.shift(DOWN * 0.1)
        
        card.add(bg, title_text, points_text)
        return card
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        # 回答开始的问题
        answer = VGroup(
            Text("现在你知道了：", font_size=36, color=WHITE),
            Text("公交车聚集是泊松过程的必然", font_size=28, color=PROB_PURPLE),
            Text("随机中蕴含着规律", font_size=28, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(answer[0]), run_time=1)
        self.play(Write(answer[1]), run_time=1.5)
        self.play(Write(answer[2]), run_time=1.5)
        self.wait(2)
        
        self.play(FadeOut(answer))
        
        # 三个要点总结
        summary = VGroup(
            Text("泊松分布三要素", font_size=SUBTITLE_SIZE, color=PROB_YELLOW, weight=BOLD),
            Text("1. 适用于稀有事件", font_size=NORMAL_SIZE),
            Text("2. 均值等于方差 (都是λ)", font_size=NORMAL_SIZE),
            Text("3. 间隔服从指数分布", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.35)
        
        for line in summary:
            self.play(Write(line), run_time=0.8)
        
        self.wait(3)
        self.play(FadeOut(summary))
        
        # 系列结尾
        self.show_series_ending(
            "看透随机的本质",
            "数学让世界可预测"
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
        sub_text.next_to(main_text, DOWN, buff=0.6)
        
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
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title), run_time=1)
        
        # EP18 内容预告
        ep18_title = Text(
            "第18集：中心极限定理",
            font_size=40,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep18_title.shift(UP * 0.3)
        
        # 预告内容
        preview_content = VGroup(
            Text("为什么一切都是正态分布？", font_size=28),
            Text("大数的魔法", font_size=28),
            Text("统计学的基石", font_size=32, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.35)
        preview_content.next_to(ep18_title, DOWN, buff=0.6)
        
        self.play(Write(ep18_title), run_time=1.5)
        for content in preview_content:
            self.play(Write(content), run_time=0.8)
        self.play(preview_content[2].animate.scale(1.05), run_time=0.5)
        
        # 思考问题
        think_question = Text(
            "身高、成绩、误差...为什么都是钟形曲线？",
            font_size=24,
            color=PROB_YELLOW
        )
        think_question.shift(DOWN * 3)
        
        self.play(Write(think_question), run_time=1.5)
        self.wait(3)
        
        # 期待语
        see_you = Text(
            "下期见！",
            font_size=36,
            color=WHITE
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title), FadeOut(ep18_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))