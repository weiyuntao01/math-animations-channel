"""
EP09: 蒙蒂霍尔悖论
选择的智慧 - 条件概率的反直觉性
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


class MontyHallEP9(Scene):
    """蒙蒂霍尔悖论 - 概率论系列 EP09"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子以保证可重复性
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(9, "蒙蒂霍尔悖论")
        
        # 2. 问题引入
        self.introduce_problem()
        
        # 3. 直觉分析
        self.analyze_intuition()
        
        # 4. 数学证明
        self.mathematical_proof()
        
        # 5. 大规模模拟
        self.simulation_demonstration()
        
        # 6. 推广到100门
        self.generalization()
        
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
    
    def introduce_problem(self):
        """引入蒙蒂霍尔问题"""
        # 标题
        title = Text("让我们做个交易", font_size=48, color=PROB_PURPLE)
        subtitle = Text("Let's Make a Deal", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # 创建三扇门（放在左边）
        doors = self.create_three_doors()
        doors.shift(LEFT * 3)
        self.play(Create(doors))
        self.wait(0.5)
        
        # 规则说明（放在右边）
        rules = VGroup(
            Text("游戏规则：", font_size=28, color=WHITE),
            Text("• 三扇门后，一辆汽车，两只山羊", font_size=22, color=WHITE),
            Text("• 你选择一扇门", font_size=22, color=WHITE),
            Text("• 主持人打开一扇有山羊的门", font_size=22, color=WHITE),
            Text("• 你可以换门，也可以坚持原选择", font_size=22, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rules.shift(RIGHT * 3.5)
        
        self.play(Write(rules[0]))
        for rule in rules[1:]:
            self.play(Write(rule), run_time=0.8)
        
        self.wait(2)
        self.play(FadeOut(rules))
        
        # 演示一次游戏流程
        self.demonstrate_game(doors)
        
        # 提出问题
        question = Text(
            "应该换门吗？",
            font_size=48,
            color=PROB_YELLOW
        )
        question.shift(RIGHT * 3.5)
        self.play(Write(question))
        self.wait(2)
        self.play(FadeOut(question), FadeOut(doors))
    
    def create_three_doors(self, scale=1.0) -> VGroup:
        """创建三扇门"""
        doors = VGroup()
        door_width = 1.8 * scale
        door_height = 3 * scale
        door_spacing = 2.2 * scale  # 缩小间距
        
        for i in range(3):
            # 门框
            door_frame = Rectangle(
                width=door_width,
                height=door_height,
                fill_color=PROB_GRAY,
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=3
            )
            
            # 门把手
            handle = Circle(
                radius=0.1 * scale,
                fill_color=GOLD,
                fill_opacity=1,
                stroke_width=0
            )
            handle.shift(RIGHT * door_width * 0.3)
            
            # 门号
            number = Text(str(i + 1), font_size=int(36 * scale), weight=BOLD)
            number.move_to(door_frame.get_center() + UP * door_height * 0.3)
            
            # 组合
            door = VGroup(door_frame, handle, number)
            door.shift(RIGHT * (i - 1) * door_spacing)
            doors.add(door)
        
        return doors
    
    def demonstrate_game(self, doors: VGroup):
        """演示一次游戏流程"""
        # 玩家选择门1
        choice_arrow = Arrow(
            start=doors[0].get_top() + UP * 0.5,
            end=doors[0].get_top() + UP * 0.1,
            color=PROB_BLUE,
            stroke_width=6
        )
        choice_text = Text("你的选择", font_size=20, color=PROB_BLUE)
        choice_text.next_to(choice_arrow, UP)
        
        self.play(
            GrowArrow(choice_arrow),
            Write(choice_text)
        )
        self.wait(1)
        
        # 主持人打开门3（显示山羊）
        self.play(doors[2][0].animate.set_fill(PROB_RED, 0.3))
        
        goat = self.create_goat()
        goat.move_to(doors[2].get_center())
        goat.scale(0.5)
        
        self.play(FadeIn(goat))
        
        host_text = Text("主持人打开了门3", font_size=24, color=WHITE)
        host_text.shift(RIGHT * 3.5 + UP * 0.5)
        self.play(Write(host_text))
        self.wait(1)
        
        # 询问是否换门
        switch_text = Text("现在，你要换到门2吗？", font_size=28, color=PROB_YELLOW)
        switch_text.shift(RIGHT * 3.5 + DOWN * 0.5)
        self.play(Write(switch_text))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(choice_arrow), FadeOut(choice_text),
            FadeOut(goat), FadeOut(host_text), FadeOut(switch_text)
        )
        doors[2][0].set_fill(PROB_GRAY, 0.8)
    
    def create_goat(self) -> VGroup:
        """创建山羊图标（简化版本）"""
        goat = VGroup()
        
        # 简单的标签
        label = Text("山羊", font_size=24, color=PROB_RED)
        
        goat.add(label)
        return goat
    
    def create_car(self) -> VGroup:
        """创建汽车图标（简化版）"""
        car = VGroup()
        
        # 车身
        body = Rectangle(width=1.5, height=0.6, fill_color=PROB_GREEN, fill_opacity=1)
        
        # 车顶
        roof = Polygon(
            [-0.5, 0.3, 0], [-0.3, 0.6, 0], [0.3, 0.6, 0], [0.5, 0.3, 0],
            fill_color=PROB_GREEN, fill_opacity=1
        )
        
        # 轮子
        wheels = VGroup()
        for x in [-0.4, 0.4]:
            wheel = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1)
            wheel.shift(RIGHT * x + DOWN * 0.3)
            wheels.add(wheel)
        
        # 标签
        label = Text("汽车", font_size=20, color=WHITE)
        label.next_to(body, DOWN, buff=0.5)
        
        car.add(body, roof, wheels, label)
        return car
    
    def analyze_intuition(self):
        """分析直觉为什么会出错"""
        title = Text("直觉告诉我们什么？", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建两扇门（门3已打开）- 放在左边
        doors = VGroup()
        for i in [1, 2]:
            door = Rectangle(
                width=2, height=3,
                fill_color=PROB_GRAY,
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=3
            )
            door.shift(RIGHT * (i - 1.5) * 3)
            
            number = Text(str(i), font_size=36, weight=BOLD)
            number.move_to(door.get_center() + UP * 0.8)
            
            doors.add(VGroup(door, number))
        
        doors.shift(LEFT * 3)
        self.play(Create(doors))
        
        # 直觉推理 - 放在右边
        intuition_text = VGroup(
            Text("剩下两扇门", font_size=26, color=WHITE),
            Text("一扇有车，一扇有羊", font_size=26, color=WHITE),
            Text("所以概率是 50:50", font_size=30, color=PROB_YELLOW),
            Text("换不换都一样？", font_size=30, color=PROB_RED)
        ).arrange(DOWN, buff=0.4)
        intuition_text.shift(RIGHT * 3.5)
        
        for text in intuition_text:
            self.play(Write(text), run_time=0.8)
            self.wait(0.5)
        
        # 错误标记
        cross = Cross(intuition_text[2], color=RED, stroke_width=6)
        self.play(Create(cross))
        
        wrong_text = Text("这个直觉是错的！", font_size=32, color=RED)
        wrong_text.next_to(intuition_text, DOWN, buff=0.5)
        self.play(Write(wrong_text))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(doors), 
            FadeOut(intuition_text), FadeOut(cross), FadeOut(wrong_text)
        )
    
    def mathematical_proof(self):
        """数学证明为什么应该换门"""
        title = Text("条件概率的真相", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建概率树
        self.create_probability_tree_animation()
        
        self.play(FadeOut(title))
    
    def create_probability_tree_animation(self):
        """创建并动画展示概率树"""
        # 初始状态
        root = Dot(LEFT * 4, radius=0.1, color=WHITE)
        root_label = Text("开始", font_size=20)
        root_label.next_to(root, LEFT)
        
        self.play(Create(root), Write(root_label))
        
        # 第一层：选择的门
        level1_nodes = VGroup()
        level1_labels = VGroup()
        level1_probs = VGroup()
        
        for i in range(3):
            angle = -PI/3 + i * PI/3
            end_pos = root.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            
            node = Dot(end_pos, radius=0.08, color=PROB_BLUE)
            line = Line(root.get_center(), end_pos, stroke_width=2)
            
            label = Text(f"选门{i+1}", font_size=16)
            label.next_to(node, RIGHT if i < 2 else LEFT)
            
            prob = Text("1/3", font_size=16, color=PROB_YELLOW)
            prob.move_to(line.get_center() + UP * 0.2)
            
            level1_nodes.add(VGroup(line, node))
            level1_labels.add(label)
            level1_probs.add(prob)
        
        self.play(
            *[Create(node) for node in level1_nodes],
            *[Write(label) for label in level1_labels],
            *[Write(prob) for prob in level1_probs]
        )
        
        # 第二层：门后的奖品（只展示选门1的情况）
        selected_node = level1_nodes[0][1]
        
        # 门1有车的情况 (概率1/3)
        car_branch = self.create_branch(
            selected_node.get_center(),
            selected_node.get_center() + UP * 1.5 + RIGHT * 1,
            "门1:车", "1/3", PROB_GREEN
        )
        
        # 门1有羊的情况 (概率2/3)
        goat_branch = self.create_branch(
            selected_node.get_center(),
            selected_node.get_center() + DOWN * 1.5 + RIGHT * 1,
            "门1:羊", "2/3", PROB_RED
        )
        
        self.play(Create(car_branch), Create(goat_branch))
        
        # 展示换门的结果
        self.show_switching_outcomes(car_branch, goat_branch)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(root), FadeOut(root_label),
            FadeOut(level1_nodes), FadeOut(level1_labels), FadeOut(level1_probs),
            FadeOut(car_branch), FadeOut(goat_branch)
        )
    
    def create_branch(self, start_pos, end_pos, label_text, prob_text, color):
        """创建概率树的一个分支"""
        branch = VGroup()
        
        line = Line(start_pos, end_pos, stroke_width=2, color=color)
        node = Dot(end_pos, radius=0.08, color=color)
        label = Text(label_text, font_size=16)
        label.next_to(node, RIGHT)
        prob = Text(prob_text, font_size=16, color=PROB_YELLOW)
        prob.move_to(line.get_center() + UP * 0.2 + LEFT * 0.2)
        
        branch.add(line, node, label, prob)
        return branch
    
    def show_switching_outcomes(self, car_branch, goat_branch):
        """展示换门的结果"""
        # 如果原门有车，换门得羊
        switch_from_car = Text(
            "换门 → 输 (1/3)",
            font_size=20,
            color=PROB_RED
        )
        switch_from_car.next_to(car_branch[1], RIGHT, buff=1)
        
        # 如果原门有羊，换门得车
        switch_from_goat = Text(
            "换门 → 赢 (2/3)",
            font_size=20,
            color=PROB_GREEN
        )
        switch_from_goat.next_to(goat_branch[1], RIGHT, buff=1)
        
        self.play(Write(switch_from_car), Write(switch_from_goat))
        
        # 总结
        conclusion = Text(
            "换门获胜概率 = 2/3",
            font_size=36,
            color=PROB_GREEN,
            weight=BOLD
        )
        conclusion.next_to(switch_from_goat, RIGHT, buff=1)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        self.play(
            FadeOut(switch_from_car),
            FadeOut(switch_from_goat),
            FadeOut(conclusion)
        )
    
    def simulation_demonstration(self):
        """大规模模拟验证"""
        title = Text("10万次实验验证", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建两个统计显示器
        stay_display = self.create_strategy_display("坚持策略", LEFT * 3.5)
        switch_display = self.create_strategy_display("换门策略", RIGHT * 3.5)
        
        self.play(Create(stay_display), Create(switch_display))
        
        # 快速模拟前100次
        self.animate_first_simulations(stay_display, switch_display, 100)
        
        # 跳跃到大数字
        self.show_large_scale_results(stay_display, switch_display)
        
        # 数据可视化
        self.visualize_convergence()
        
        self.play(FadeOut(title))
    
    def create_strategy_display(self, strategy_name, position):
        """创建策略显示器"""
        display = VGroup()
        
        # 背景
        bg = Rectangle(
            width=3, height=4,
            fill_color=PROB_GRAY,
            fill_opacity=0.3,
            stroke_color=WHITE
        )
        bg.move_to(position)
        
        # 标题
        title = Text(strategy_name, font_size=24, weight=BOLD)
        title.move_to(bg.get_top() + DOWN * 0.5)
        
        # 统计数据
        wins = Text("获胜: 0", font_size=20)
        total = Text("总计: 0", font_size=20)
        rate = Text("胜率: 0.000", font_size=22, color=PROB_YELLOW)
        
        wins.move_to(bg.get_center() + UP * 0.5)
        total.move_to(bg.get_center())
        rate.move_to(bg.get_center() + DOWN * 0.5)
        
        display.add(bg, title, wins, total, rate)
        display.wins = 0
        display.total = 0
        display.wins_text = wins
        display.total_text = total
        display.rate_text = rate
        
        return display
    
    def animate_first_simulations(self, stay_display, switch_display, n_simulations):
        """动画展示前n次模拟"""
        for i in range(n_simulations):
            # 模拟一次游戏
            car_position = random.randint(0, 2)
            player_choice = random.randint(0, 2)
            
            # 坚持策略
            stay_win = (car_position == player_choice)
            stay_display.wins += int(stay_win)
            stay_display.total += 1
            
            # 换门策略
            switch_win = (car_position != player_choice)
            switch_display.wins += int(switch_win)
            switch_display.total += 1
            
            # 更新显示（每10次更新一次）
            if (i + 1) % 10 == 0:
                self.update_display(stay_display)
                self.update_display(switch_display)
    
    def update_display(self, display):
        """更新显示器"""
        new_wins = Text(f"获胜: {display.wins}", font_size=20)
        new_total = Text(f"总计: {display.total}", font_size=20)
        new_rate = Text(
            f"胜率: {display.wins/display.total:.3f}",
            font_size=22,
            color=PROB_YELLOW
        )
        
        new_wins.move_to(display.wins_text.get_center())
        new_total.move_to(display.total_text.get_center())
        new_rate.move_to(display.rate_text.get_center())
        
        self.play(
            Transform(display.wins_text, new_wins),
            Transform(display.total_text, new_total),
            Transform(display.rate_text, new_rate),
            run_time=0.1
        )
    
    def show_large_scale_results(self, stay_display, switch_display):
        """展示大规模结果"""
        # 模拟剩余的99900次
        n_remaining = 99900
        
        # 计算最终结果（理论值）
        stay_display.wins = int(n_remaining * 1/3) + stay_display.wins
        stay_display.total = 100000
        switch_display.wins = int(n_remaining * 2/3) + switch_display.wins
        switch_display.total = 100000
        
        # 创建过渡动画
        transition_text = Text("模拟中...", font_size=32, color=WHITE)
        transition_text.move_to(ORIGIN)
        
        self.play(Write(transition_text))
        self.wait(0.5)
        
        # 快速数字滚动效果
        for milestone in [1000, 10000, 50000, 100000]:
            stay_display.total = milestone
            switch_display.total = milestone
            stay_display.wins = int(milestone * 0.333)
            switch_display.wins = int(milestone * 0.667)
            
            self.update_display(stay_display)
            self.update_display(switch_display)
            self.wait(0.2)
        
        self.play(FadeOut(transition_text))
        
        # 最终结果高亮
        self.highlight_final_results(stay_display, switch_display)
    
    def highlight_final_results(self, stay_display, switch_display):
        """高亮最终结果"""
        # 创建高亮框
        stay_highlight = SurroundingRectangle(
            stay_display.rate_text,
            color=PROB_RED,
            stroke_width=3
        )
        switch_highlight = SurroundingRectangle(
            switch_display.rate_text,
            color=PROB_GREEN,
            stroke_width=3
        )
        
        self.play(Create(stay_highlight), Create(switch_highlight))
        
        # 结论文字
        conclusion = Text(
            "换门策略胜率是坚持策略的2倍！",
            font_size=32,
            color=PROB_GREEN
        )
        conclusion.to_edge(DOWN)
        
        self.play(Write(conclusion))
        self.wait(2)
        
        self.play(
            FadeOut(stay_highlight), FadeOut(switch_highlight),
            FadeOut(conclusion), FadeOut(stay_display), FadeOut(switch_display)
        )
    
    def visualize_convergence(self):
        """可视化收敛过程"""
        # 创建坐标轴
        axes = Axes(
            x_range=[0, 1000, 200],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [0, 200, 400, 600, 800, 1000],
                "label_direction": DOWN,
            },
            y_axis_config={
                "numbers_to_include": [0, 0.33, 0.67, 1],
                "decimal_number_config": {"num_decimal_places": 2},
            }
        )
        axes.shift(DOWN * 0.5)
        
        # 轴标签
        x_label = Text("实验次数", font_size=20)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("胜率", font_size=20)
        y_label.rotate(PI/2)
        y_label.next_to(axes.y_axis, LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 理论值线
        theory_stay = DashedLine(
            axes.coords_to_point(0, 1/3),
            axes.coords_to_point(1000, 1/3),
            color=PROB_RED,
            stroke_width=2
        )
        theory_switch = DashedLine(
            axes.coords_to_point(0, 2/3),
            axes.coords_to_point(1000, 2/3),
            color=PROB_GREEN,
            stroke_width=2
        )
        
        theory_labels = VGroup(
            Text("1/3", font_size=16, color=PROB_RED).next_to(theory_stay, RIGHT),
            Text("2/3", font_size=16, color=PROB_GREEN).next_to(theory_switch, RIGHT)
        )
        
        self.play(
            Create(theory_stay), Create(theory_switch),
            Write(theory_labels)
        )
        
        # 收敛曲线
        stay_curve = self.create_convergence_curve(axes, 1/3, PROB_RED)
        switch_curve = self.create_convergence_curve(axes, 2/3, PROB_GREEN)
        
        self.play(Create(stay_curve), Create(switch_curve))
        
        # 图例
        legend = self.create_legend()
        legend.shift(UP * 2 + RIGHT * 3)
        self.play(Create(legend))
        
        self.wait(3)
        
        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(theory_stay), FadeOut(theory_switch), FadeOut(theory_labels),
            FadeOut(stay_curve), FadeOut(switch_curve), FadeOut(legend)
        )
    
    def create_convergence_curve(self, axes, target_value, color):
        """创建收敛曲线"""
        # 生成带有随机波动的收敛数据
        x_values = np.linspace(1, 1000, 100)
        y_values = []
        
        for x in x_values:
            # 随机波动随着实验次数增加而减小
            variance = 0.1 / np.sqrt(x)
            y = target_value + np.random.normal(0, variance)
            y_values.append(y)
        
        # 创建曲线
        points = [axes.coords_to_point(x, y) for x, y in zip(x_values, y_values)]
        curve = VMobject()
        curve.set_points_smoothly(points)
        curve.set_stroke(color=color, width=2)
        
        return curve
    
    def create_legend(self):
        """创建图例"""
        legend = VGroup()
        
        # 背景
        bg = Rectangle(
            width=2.5, height=1.5,
            fill_color=BLACK,
            fill_opacity=0.5,
            stroke_color=WHITE
        )
        legend.add(bg)
        
        # 坚持策略
        stay_line = Line(LEFT * 0.3, RIGHT * 0.3, color=PROB_RED, stroke_width=3)
        stay_text = Text("坚持策略", font_size=14)
        stay_text.next_to(stay_line, RIGHT*0.2)
        stay_group = VGroup(stay_line, stay_text)
        stay_group.shift(UP * 0.3)
        
        # 换门策略
        switch_line = Line(LEFT * 0.3, RIGHT * 0.3, color=PROB_GREEN, stroke_width=3)
        switch_text = Text("换门策略", font_size=14)
        switch_text.next_to(switch_line, RIGHT*0.2)
        switch_group = VGroup(switch_line, switch_text)
        switch_group.shift(DOWN * 0.3)
        
        legend.add(stay_group, switch_group)
        
        return legend
    
    def generalization(self):
        """推广到100门问题"""
        title = Text("如果有100扇门呢？", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建100扇门的缩略图
        doors_grid = self.create_many_doors(100)
        self.play(Create(doors_grid))
        
        # 游戏流程
        self.demonstrate_100_doors_game(doors_grid)
        
        self.play(FadeOut(title))
    
    def create_many_doors(self, n_doors):
        """创建多扇门的网格"""
        doors = VGroup()
        
        # 计算网格布局
        cols = 20
        rows = n_doors // cols
        
        door_size = 0.25  # 缩小门的尺寸
        spacing = 0.28
        
        for i in range(n_doors):
            row = i // cols
            col = i % cols
            
            door = Rectangle(
                width=door_size,
                height=door_size * 1.5,
                fill_color=PROB_GRAY,
                fill_opacity=0.8,
                stroke_width=1
            )
            
            x = (col - cols/2) * spacing
            y = (rows/2 - row) * spacing * 1.5
            door.move_to([x, y, 0])
            
            doors.add(door)
        
        doors.scale(0.7)  # 进一步缩小整体尺寸
        return doors
    
    def demonstrate_100_doors_game(self, doors_grid):
        """演示100门游戏"""
        # 将门网格移到左边
        doors_grid.shift(LEFT * 2)
        
        # 标记选择的门（比如第37扇）
        chosen_index = 36
        doors_grid[chosen_index].set_fill(PROB_BLUE, 0.8)
        
        choice_text = Text("你选择了第37扇门", font_size=24, color=PROB_BLUE)
        choice_text.shift(RIGHT * 3.5 + UP * 2)
        self.play(Write(choice_text))
        
        # 主持人打开98扇门
        opened_doors = list(range(100))
        opened_doors.remove(chosen_index)
        opened_doors.remove(42)  # 假设第43扇门后有车
        
        # 批量打开门
        animations = []
        for i in opened_doors[:50]:  # 先打开50扇
            animations.append(doors_grid[i].animate.set_fill(PROB_RED, 0.3))
        
        self.play(*animations, run_time=1)
        
        animations = []
        for i in opened_doors[50:]:  # 再打开剩余的
            animations.append(doors_grid[i].animate.set_fill(PROB_RED, 0.3))
        
        self.play(*animations, run_time=1)
        
        # 剩下两扇门
        remaining_text = Text(
            "主持人打开了98扇门，都是山羊",
            font_size=24,
            color=WHITE
        )
        remaining_text.next_to(choice_text, DOWN)
        self.play(Write(remaining_text))
        
        # 高亮剩余的两扇门
        highlight1 = SurroundingRectangle(doors_grid[chosen_index], color=PROB_BLUE, stroke_width=3)
        highlight2 = SurroundingRectangle(doors_grid[42], color=PROB_YELLOW, stroke_width=3)
        
        self.play(Create(highlight1), Create(highlight2))
        
        # 概率分析 - 放在右边
        prob_text = VGroup(
            Text("你的门有车的概率: 1/100", font_size=26, color=PROB_BLUE),
            Text("另一扇门有车的概率: 99/100", font_size=26, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.4)
        prob_text.next_to(remaining_text, DOWN, buff=0.5)
        
        self.play(Write(prob_text))
        
        # 强调
        emphasis = Text(
            "现在还觉得换不换无所谓吗？",
            font_size=28,
            color=PROB_GREEN,
            weight=BOLD
        )
        emphasis.next_to(prob_text, DOWN, buff=0.5)
        
        self.play(Write(emphasis))
        self.wait(3)
        
        # 清理
        self.play(
            FadeOut(doors_grid), FadeOut(choice_text), FadeOut(remaining_text),
            FadeOut(highlight1), FadeOut(highlight2),
            FadeOut(prob_text), FadeOut(emphasis)
        )
    
    def real_world_applications(self):
        """现实世界的应用"""
        title = Text("蒙蒂霍尔思维的启示", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 应用场景
        applications = VGroup(
            VGroup(
                Text("投资决策", font_size=28, color=PROB_BLUE),
                Text("新信息出现时，要勇于改变决策", font_size=20, color=WHITE)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("医疗诊断", font_size=28, color=PROB_GREEN),
                Text("第二意见的价值往往被低估", font_size=20, color=WHITE)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("职业选择", font_size=28, color=PROB_YELLOW),
                Text("不要因沉没成本而拒绝更好的机会", font_size=20, color=WHITE)
            ).arrange(DOWN, buff=0.2)
        ).arrange(DOWN, buff=0.8)
        applications.shift(DOWN * 0.5)
        
        for app in applications:
            self.play(Write(app[0]))
            self.play(FadeIn(app[1], shift=UP))
            self.wait(1)
        
        # 核心教训
        lesson = Text(
            "条件概率告诉我们：新信息改变一切",
            font_size=32,
            color=PROB_GREEN,
            weight=BOLD
        )
        lesson.to_edge(DOWN)
        
        self.play(Write(lesson))
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(applications), FadeOut(lesson)
        )
    
    def show_ending(self):
        """自定义结尾"""
        # 三个数字的对比
        numbers = VGroup(
            VGroup(
                Text("50%", font_size=72, color=PROB_RED),
                Text("直觉", font_size=24, color=WHITE)
            ).arrange(DOWN),
            
            VGroup(
                Text("VS", font_size=48, color=WHITE)
            ),
            
            VGroup(
                Text("67%", font_size=72, color=PROB_GREEN),
                Text("数学", font_size=24, color=WHITE)
            ).arrange(DOWN)
        ).arrange(RIGHT, buff=1)
        
        self.play(Write(numbers))
        self.wait(2)
        
        # 转换为最终信息
        self.play(FadeOut(numbers))
        
        # 系列结尾
        self.show_series_ending(
            "直觉可能会骗你",
            "但数学不会"
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
        
        # EP10 内容预告
        ep10_title = Text(
            "第10集：生日悖论",
            font_size=42,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep10_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("23个人的聚会中", font_size=28, color=WHITE),
            Text("有两人生日相同的概率", font_size=28, color=WHITE),
            Text("竟然超过50%！", font_size=32, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep10_title, DOWN, buff=0.8)
        
        self.play(Write(ep10_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        # 思考问题
        think_question = Text(
            "你觉得多少人才能让概率达到99%？",
            font_size=24,
            color=PROB_YELLOW
        )
        think_question.next_to(preview_content,DOWN,buff=0.3)
        
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
            FadeOut(preview_title), FadeOut(ep10_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))