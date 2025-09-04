from manim import *
import numpy as np

class StockFibonacciEP8(Scene):
    """股市技术分析中的斐波那契 - 黄金分割系列 EP08"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：斐波那契回撤理论
        self.show_fibonacci_retracement()
        
        # 第二部分：支撑位与阻力位
        self.show_support_resistance()
        
        # 第三部分：斐波那契扇形
        self.show_fibonacci_fan()
        
        # 第四部分：时间周期分析
        self.show_time_cycles()
        
        # 第五部分：艾略特波浪理论
        self.show_elliott_waves()
        
        # 结尾与系列总结
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第八集：股市技术分析中的斐波那契", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_fibonacci_retracement(self):
        """斐波那契回撤理论 - 0:10-1:00"""
        title = Text("斐波那契回撤", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建简化的K线图
        # 价格数据（模拟上升趋势后的回撤）
        price_points = [
            (0, 100), (1, 105), (2, 110), (3, 120), (4, 115),
            (5, 125), (6, 140), (7, 155), (8, 170), (9, 180),  # 上升
            (10, 175), (11, 165), (12, 160), (13, 155), (14, 150)  # 回撤
        ]
        
        # 坐标轴
        axes = Axes(
            x_range=[0, 15, 5],
            y_range=[90, 190, 20],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY},
            x_axis_config={"numbers_to_include": [0, 5, 10, 15]},
            y_axis_config={"numbers_to_include": [100, 120, 140, 160, 180]}
        ).shift(LEFT * 2.5)
        
        # 价格线
        price_line = axes.plot_line_graph(
            x_values=[p[0] for p in price_points],
            y_values=[p[1] for p in price_points],
            line_color=WHITE,
            vertex_dot_radius=0.03,
            vertex_dot_style=dict(color=WHITE)
        )
        
        self.play(Create(axes), Create(price_line["line_graph"]))
        
        # 标记高点和低点
        low_point = axes.coords_to_point(0, 100)
        high_point = axes.coords_to_point(9, 180)
        
        low_dot = Dot(low_point, color=GREEN, radius=0.1)
        high_dot = Dot(high_point, color=RED, radius=0.1)
        
        low_label = Text("低点", font_size=16, color=GREEN).next_to(low_dot, DOWN)
        high_label = Text("高点", font_size=16, color=RED).next_to(high_dot, UP)
        
        self.play(
            Create(low_dot), Write(low_label),
            Create(high_dot), Write(high_label)
        )
        
        # 斐波那契回撤水平线
        fib_levels = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1]
        fib_colors = [GREEN, BLUE, YELLOW, ORANGE, GOLD, PURPLE, RED]
        fib_lines = VGroup()
        fib_labels = VGroup()
        
        price_range = 180 - 100
        
        for level, color in zip(fib_levels, fib_colors):
            y_value = 180 - price_range * level
            line = DashedLine(
                axes.coords_to_point(0, y_value),
                axes.coords_to_point(15, y_value),
                color=color,
                stroke_width=1.5,
                dash_length=0.1
            )
            fib_lines.add(line)
            
            # 标签
            percentage = f"{level*100:.1f}%" if level != 0.5 else "50%"
            label = Text(percentage, font_size=14, color=color)
            label.next_to(line, RIGHT, buff=0.1)
            fib_labels.add(label)
        
        self.play(*[Create(line) for line in fib_lines])
        self.play(*[Write(label) for label in fib_labels])
        
        # 关键比例说明
        key_ratios = VGroup(
            Text("关键回撤位：", font_size=20, color=WHITE),
            Text("38.2% - 弱回撤", font_size=18, color=YELLOW),
            Text("50.0% - 中等回撤", font_size=18, color=ORANGE),
            Text("61.8% - 黄金回撤", font_size=18, color=GOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        key_ratios.shift(RIGHT * 4 + UP * 0.5)
        
        self.play(Write(key_ratios))
        
        # 说明文字
        explanation = Text(
            "价格常在斐波那契水平获得支撑或阻力",
            font_size=22,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(price_line),
            FadeOut(low_dot), FadeOut(low_label),
            FadeOut(high_dot), FadeOut(high_label),
            FadeOut(fib_lines), FadeOut(fib_labels),
            FadeOut(key_ratios), FadeOut(explanation)
        )
    
    def show_support_resistance(self):
        """支撑位与阻力位 - 1:00-1:40"""
        title = Text("支撑位与阻力位的斐波那契", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建更复杂的价格走势
        # 展示多个波段
        price_data = []
        x = np.linspace(0, 12, 100)
        # 创建带有多个波峰波谷的价格走势
        y = 150 + 30*np.sin(x/2) + 15*np.sin(x) + 5*np.random.normal(0, 1, 100)
        
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[100, 200, 20],
            x_length=7,
            y_length=4,
            axis_config={"color": GRAY}
        ).shift(LEFT * 2)
        
        # 价格曲线
        price_curve = axes.plot(
            lambda t: 150 + 30*np.sin(t/2) + 15*np.sin(t),
            x_range=[0, 12],
            color=WHITE,
            stroke_width=2
        )
        
        self.play(Create(axes), Create(price_curve))
        
        # 标记关键斐波那契水平
        fib_levels = [
            (161.8, GOLD, "161.8%"),
            (150, ORANGE, "100%"),
            (138.2, YELLOW, "61.8%"),
            (130, BLUE, "50%")
        ]
        
        support_resistance_lines = VGroup()
        labels = VGroup()
        
        for level, color, label_text in fib_levels:
            line = DashedLine(
                axes.coords_to_point(0, level),
                axes.coords_to_point(12, level),
                color=color,
                stroke_width=2,
                dash_length=0.15
            )
            support_resistance_lines.add(line)
            
            label = Text(label_text, font_size=16, color=color)
            label.next_to(line, RIGHT, buff=0.1)
            labels.add(label)
        
        self.play(*[Create(line) for line in support_resistance_lines])
        self.play(*[Write(label) for label in labels])
        
        # 标记价格反弹点
        bounce_points = [
            (2.5, 138.2, "支撑"),
            (5, 161.8, "阻力"),
            (8, 130, "支撑")
        ]
        
        bounce_markers = VGroup()
        for x, y, text in bounce_points:
            point = axes.coords_to_point(x, y)
            circle = Circle(radius=0.15, color=RED, stroke_width=2).move_to(point)
            label = Text(text, font_size=14, color=RED).next_to(circle, DOWN, buff=0.1)
            bounce_markers.add(VGroup(circle, label))
        
        self.play(*[Create(marker) for marker in bounce_markers])
        
        # 原理说明
        principle = VGroup(
            Text("斐波那契原理：", font_size=20, color=WHITE),
            Text("• 前期高低点的斐波那契", font_size=18, color=WHITE),
            Text("  比例常成为支撑/阻力", font_size=18, color=WHITE),
            Text("• 多个斐波那契水平", font_size=18, color=WHITE),
            Text("  重叠处更为重要", font_size=18, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        principle.shift(RIGHT * 4 + UP * 0.3)
        
        self.play(Write(principle))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(price_curve),
            FadeOut(support_resistance_lines), FadeOut(labels),
            FadeOut(bounce_markers), FadeOut(principle)
        )
    
    def show_fibonacci_fan(self):
        """斐波那契扇形 - 1:40-2:20"""
        title = Text("斐波那契扇形", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY}
        ).shift(LEFT * 2.5 + DOWN * 0.5)
        
        self.play(Create(axes))
        
        # 起点和终点
        start_point = axes.coords_to_point(1, 2)
        end_point = axes.coords_to_point(8, 8)
        
        start_dot = Dot(start_point, color=GREEN, radius=0.08)
        end_dot = Dot(end_point, color=RED, radius=0.08)
        
        base_line = Line(start_point, end_point, color=WHITE, stroke_width=2)
        
        self.play(
            Create(start_dot), Create(end_dot),
            Create(base_line)
        )
        
        # 斐波那契扇形线
        fan_ratios = [0.236, 0.382, 0.5, 0.618, 0.786]
        fan_colors = [BLUE, YELLOW, ORANGE, GOLD, PURPLE]
        fan_lines = VGroup()
        fan_labels = VGroup()
        
        # 计算扇形线
        dx = 8 - 1
        dy = 8 - 2
        
        for ratio, color in zip(fan_ratios, fan_colors):
            # 计算斜率
            slope = dy * ratio / dx
            # 延长线的终点
            x_end = 10
            y_end = 2 + slope * (x_end - 1)
            
            if y_end <= 10:  # 确保在坐标系内
                fan_line = Line(
                    start_point,
                    axes.coords_to_point(x_end, y_end),
                    color=color,
                    stroke_width=1.5
                )
                fan_lines.add(fan_line)
                
                # 标签
                label = Text(f"{ratio:.3f}", font_size=14, color=color)
                label.move_to(fan_line.get_end()).shift(RIGHT * 0.3)
                fan_labels.add(label)
        
        self.play(*[Create(line) for line in fan_lines])
        self.play(*[Write(label) for label in fan_labels])
        
        # 价格走势示例
        price_curve = VMobject()
        points = []
        for t in np.linspace(1, 9, 50):
            y = 2 + (t-1) * 0.7 + 1.5 * np.sin(t)
            if y > 0 and y < 10:
                points.append(axes.coords_to_point(t, y))
        
        price_curve.set_points_smoothly(points)
        price_curve.set_stroke(color=GRAY, width=2)
        
        self.play(Create(price_curve))
        
        # 扇形线用途说明
        usage = VGroup(
            Text("斐波那契扇形：", font_size=20, color=WHITE),
            Text("• 预测趋势线角度", font_size=18, color=WHITE),
            Text("• 动态支撑/阻力", font_size=18, color=WHITE),
            Text("• 趋势强度判断", font_size=18, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        usage.shift(RIGHT * 4 + UP * 0.5)
        
        self.play(Write(usage))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(axes),
            FadeOut(start_dot), FadeOut(end_dot), FadeOut(base_line),
            FadeOut(fan_lines), FadeOut(fan_labels),
            FadeOut(price_curve), FadeOut(usage)
        )
    
    def show_time_cycles(self):
        """时间周期分析 - 2:20-3:00"""
        title = Text("斐波那契时间周期", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 时间轴
        time_axis = NumberLine(
            x_range=[0, 34, 1],
            length=10,
            include_numbers=False,
            color=GRAY
        ).shift(DOWN * 0.5)
        
        self.play(Create(time_axis))
        
        # 斐波那契数列
        fib_numbers = [1, 2, 3, 5, 8, 13, 21, 34]
        fib_markers = VGroup()
        fib_labels = VGroup()
        
        for fib in fib_numbers:
            if fib <= 34:
                point = time_axis.number_to_point(fib)
                
                # 垂直线
                line = Line(
                    point + DOWN * 0.2,
                    point + UP * 2,
                    color=YELLOW,
                    stroke_width=2
                )
                fib_markers.add(line)
                
                # 数字标签
                label = Text(str(fib), font_size=18, color=YELLOW)
                label.next_to(line, UP)
                fib_labels.add(label)
        
        self.play(*[Create(marker) for marker in fib_markers])
        self.play(*[Write(label) for label in fib_labels])
        
        # 价格走势与时间周期
        price_curve = FunctionGraph(
            lambda t: 1.5 + 0.8 * np.sin(t/3) + 0.3 * np.sin(t),
            x_range=[0, 34],
            color=WHITE,
            stroke_width=2
        ).shift(UP * 0.5)
        
        self.play(Create(price_curve))
        
        # 标记转折点
        turning_points = [1, 3, 5, 8, 13, 21]
        point_markers = VGroup()
        
        for tp in turning_points:
            x = tp
            y = 1.5 + 0.8 * np.sin(x/3) + 0.3 * np.sin(x) + 0.5
            dot = Dot([x - 17, y, 0], color=RED, radius=0.08)
            point_markers.add(dot)
        
        self.play(*[Create(dot) for dot in point_markers])
        
        # 时间周期说明
        cycle_explanation = VGroup(
            Text("斐波那契时间周期：", font_size=20, color=WHITE),
            Text("• 市场转折常发生在", font_size=18, color=WHITE),
            Text("  斐波那契数字的时间点", font_size=18, color=WHITE),
            Text("• 可用于预测时间窗口", font_size=18, color=WHITE),
            Text("• 结合价格分析更有效", font_size=18, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        cycle_explanation.shift(RIGHT * 3.5 + DOWN * 2)
        
        self.play(Write(cycle_explanation))
        
        # 标注"天"或"周"
        time_unit = Text("时间单位：天/周/月", font_size=16, color=GRAY)
        time_unit.next_to(time_axis, DOWN)
        self.play(Write(time_unit))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(time_axis),
            FadeOut(fib_markers), FadeOut(fib_labels),
            FadeOut(price_curve), FadeOut(point_markers),
            FadeOut(cycle_explanation), FadeOut(time_unit)
        )
    
    def show_elliott_waves(self):
        """艾略特波浪理论 - 3:00-3:40"""
        title = Text("艾略特波浪与斐波那契", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建典型的艾略特波浪
        wave_points = [
            (0, 100),    # 起点
            (1, 150),    # 波1顶
            (2, 120),    # 波2底
            (3, 200),    # 波3顶
            (4, 170),    # 波4底
            (5, 220),    # 波5顶
            (6, 150),    # 波A底
            (7, 190),    # 波B顶
            (8, 130)     # 波C底
        ]
        
        # 坐标系
        axes = Axes(
            x_range=[0, 9, 1],
            y_range=[80, 240, 20],
            x_length=7,
            y_length=4,
            axis_config={"color": GRAY}
        ).shift(LEFT * 2 + DOWN * 0.5)
        
        # 绘制波浪
        wave_line = VMobject()
        points = [axes.coords_to_point(x, y) for x, y in wave_points]
        wave_line.set_points_smoothly(points)
        wave_line.set_stroke(color=WHITE, width=3)
        
        self.play(Create(axes), Create(wave_line))
        
        # 标记波浪
        wave_labels = ["1", "2", "3", "4", "5", "A", "B", "C"]
        label_positions = wave_points[1:]
        
        labels = VGroup()
        for i, (label_text, (x, y)) in enumerate(zip(wave_labels, label_positions)):
            color = BLUE if i < 5 else RED  # 推动浪蓝色，调整浪红色
            label = Text(label_text, font_size=20, color=color)
            label.move_to(axes.coords_to_point(x, y))
            if i % 2 == 0:  # 顶部
                label.shift(UP * 0.3)
            else:  # 底部
                label.shift(DOWN * 0.3)
            labels.add(label)
        
        self.play(*[Write(label) for label in labels])
        
        # 斐波那契关系
        fib_relations = VGroup(
            Text("波浪斐波那契关系：", font_size=20, color=WHITE),
            Text("波3 = 波1 × 1.618", font_size=18, color=BLUE),
            Text("波5 = 波1 × 1.0", font_size=18, color=BLUE),
            Text("波2回撤 = 波1 × 0.618", font_size=18, color=YELLOW),
            Text("波4回撤 = 波3 × 0.382", font_size=18, color=YELLOW),
            Text("波C = 波A × 1.0或1.618", font_size=18, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        fib_relations.shift(RIGHT * 3.5)
        
        self.play(Write(fib_relations))
        
        # 添加斐波那契比例示意
        # 波3与波1的关系
        wave1_height = 50
        wave3_height = 80
        
        brace1 = Brace(Line(axes.coords_to_point(0, 100), axes.coords_to_point(1, 150)), LEFT)
        brace3 = Brace(Line(axes.coords_to_point(2, 120), axes.coords_to_point(3, 200)), LEFT)
        
        ratio_label = MathTex(r"\times 1.618", font_size=16, color=GOLD)
        ratio_label.move_to((brace1.get_center() + brace3.get_center()) / 2)
        
        self.play(Create(brace1), Create(brace3), Write(ratio_label))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(wave_line),
            FadeOut(labels), FadeOut(fib_relations),
            FadeOut(brace1), FadeOut(brace3), FadeOut(ratio_label)
        )
    
    def show_ending(self):
        """结尾与系列总结 - 3:40-4:20"""
        # 风险提示
        warning = VGroup(
            Text("重要提示", font_size=36, color=RED),
            Text("技术分析仅供参考，不构成投资建议", font_size=24, color=YELLOW),
            Text("投资有风险，入市需谨慎", font_size=24, color=YELLOW)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(warning))
        self.wait(2)
        self.play(FadeOut(warning))
        
        # 系列总结
        series_title = Text("数学之美 · 黄金分割系列", font_size=42, color=GOLD)
        series_title.to_edge(UP)
        self.play(Write(series_title))
        
        # 八集回顾
        episodes = VGroup(
            Text("EP1: 向日葵的螺旋密码", font_size=20),
            Text("EP2: 斐波那契与兔子问题", font_size=20),
            Text("EP3: 鹦鹉螺的等角螺线", font_size=20),
            Text("EP4: 黄金矩形与艺术构图", font_size=20),
            Text("EP5: 人体比例中的1.618", font_size=20),
            Text("EP6: 音乐和弦中的数学", font_size=20),
            Text("EP7: 建筑设计的数学美学", font_size=20),
            Text("EP8: 股市技术分析中的斐波那契", font_size=20)
        ).arrange(DOWN, buff=0.3)
        
        # 分两列显示
        left_episodes = VGroup(*episodes[:4]).shift(LEFT * 3)
        right_episodes = VGroup(*episodes[4:]).shift(RIGHT * 3)
        
        self.play(
            *[Write(ep) for ep in left_episodes],
            *[Write(ep) for ep in right_episodes]
        )
        self.wait(2)
        
        self.play(
            FadeOut(left_episodes), FadeOut(right_episodes),
            FadeOut(series_title)
        )
        
        # 最终总结
        final_summary = VGroup(
            Text("从自然到艺术", font_size=36, color=WHITE),
            Text("从音乐到建筑", font_size=36, color=WHITE),
            Text("从人体到金融", font_size=36, color=WHITE),
            Text("数学无处不在", font_size=42, color=GOLD)
        ).arrange(DOWN, buff=0.5)
        
        for line in final_summary:
            self.play(Write(line), run_time=1)
        
        self.wait(2)
        self.play(FadeOut(final_summary))
        
        # 结束语
        ending = VGroup(
            Text("感谢陪伴", font_size=48, color=GOLD),
            Text("让我们继续在生活中", font_size=32, color=WHITE),
            Text("发现数学之美", font_size=32, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(ending))
        
        # 订阅提醒
        subscribe = Text("喜欢请三连支持！期待下个系列再见！", font_size=28, color=RED)
        subscribe.next_to(ending, DOWN, buff=1)
        
        self.play(Write(subscribe))
        self.wait(3)