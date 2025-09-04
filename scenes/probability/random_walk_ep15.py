"""
EP15: 随机漫步
醉汉能回家吗？股价真的随机吗？
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


class RandomWalkEP15(ThreeDScene):
    """随机漫步 - 概率论系列 EP15"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(15, "随机漫步")
        
        # 2. 什么是随机漫步？
        self.what_is_random_walk()
        
        # 3. 醉汉问题引入
        self.introduce_drunk_walk()
        
        # 4. 一维随机漫步演示
        self.one_dimensional_walk_demo()
        
        # 5. 神奇的发现
        self.amazing_discovery()
        
        # 6. 二维随机漫步
        self.two_dimensional_walk_simple()
        
        # 7. 三维随机漫步
        self.three_dimensional_walk()
        
        # 8. 生活中的例子
        self.real_life_examples()
        
        # 9. 股市应用
        self.stock_market_realistic()
        
        # 10. 结尾
        self.show_ending()
    
    def show_series_intro(self, episode_num: int, episode_title: str):
        """显示系列介绍动画"""
        series_title = Text(
            "概率论的反直觉世界",
            font_size=50,
            color=PROB_PURPLE,
            weight=BOLD
        )
        series_title.move_to([0, 1, 0])
        
        episode_text = Text(
            f"第{episode_num}集：{episode_title}",
            font_size=34,
            color=WHITE
        )
        episode_text.move_to([0, -1, 0])
        
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(series_title), FadeOut(episode_text))
    
    def what_is_random_walk(self):
        """什么是随机漫步？"""
        self.clear()
        
        title = Text("什么是随机漫步？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 用硬币来解释
        coin = Circle(radius=0.8, fill_color=PROB_YELLOW, fill_opacity=0.8)
        coin.move_to([0, 1, 0])
        
        heads_text = Text("正面", font_size=NORMAL_SIZE).move_to(coin)
        self.play(Create(coin), Write(heads_text))
        
        # 解释规则
        explanation = VGroup(
            Text("想象你在玩一个游戏：", font_size=NORMAL_SIZE, color=WHITE),
            Text("1. 抛硬币", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("2. 正面向右走一步", font_size=NORMAL_SIZE, color=PROB_GREEN),
            Text("3. 反面向左走一步", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("这就是随机漫步！", font_size=SUBTITLE_SIZE, color=PROB_PURPLE)
        ).arrange(DOWN, buff=0.4)
        explanation.move_to([0, -1.5, 0])
        
        # 翻转硬币动画
        self.play(Rotate(coin, PI, axis=RIGHT))
        tails_text = Text("反面", font_size=NORMAL_SIZE).move_to(coin)
        self.play(Transform(heads_text, tails_text))
        
        for line in explanation:
            self.play(Write(line), run_time=0.8)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(coin), FadeOut(heads_text), FadeOut(explanation))
    
    def introduce_drunk_walk(self):
        """引入醉汉问题"""
        self.clear()
        
        title = Text("一个有趣的故事", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建场景 - 调整位置避免与文字重叠
        street_lamp = self.create_street_lamp()
        street_lamp.move_to([-4, -0.5, 0])  # 下移
        
        home = self.create_home()
        home.move_to([4, -0.5, 0])  # 下移
        
        drunk = self.create_drunk_person()
        drunk.move_to([0, -1, 0])  # 下移
        
        street = Line([-6, -1.5, 0], [6, -1.5, 0], color=GRAY, stroke_width=3)  # 下移
        
        self.play(
            Create(street),
            FadeIn(street_lamp),
            FadeIn(home),
            FadeIn(drunk)
        )
        
        # 故事叙述 - 调整位置到场景上方
        story = VGroup(
            Text("深夜，一个醉汉站在路灯下", font_size=NORMAL_SIZE),
            Text("他想回家，但是...", font_size=NORMAL_SIZE),
            Text("每一步都是随机的！", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.3)  # 减小间距
        story.move_to([0, 2, 0])  # 调整到更合适的位置
        
        for line in story:
            self.play(Write(line), run_time=1)
        
        # 模拟醉汉走路
        step_count = Text("步数：0", font_size=SMALL_SIZE, color=WHITE)
        step_count.to_edge(RIGHT).shift(UP*3)  # 移到更高位置
        self.play(Write(step_count))
        
        # 走10步
        for i in range(10):
            direction = random.choice([-1, 1])
            self.play(
                drunk.animate.shift(RIGHT * direction * 0.4),
                run_time=0.5
            )
            new_count = Text(f"步数：{i+1}", font_size=SMALL_SIZE, color=WHITE)
            new_count.to_edge(RIGHT).shift(UP*3)  # 保持相同高度
            self.play(Transform(step_count, new_count), run_time=0.2)
        
        # 提出问题 - 确保在底部
        question = Text(
            "问题：他最终能回到家吗？",
            font_size=SUBTITLE_SIZE,
            color=PROB_RED
        )
        question.to_edge(DOWN, buff=0.8)  # 增加底部间距
        self.play(Write(question))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(story), FadeOut(street), 
            FadeOut(street_lamp), FadeOut(home), FadeOut(drunk),
            FadeOut(step_count), FadeOut(question)
        )
    
    def create_street_lamp(self):
        """创建路灯"""
        lamp = VGroup()
        pole = Rectangle(width=0.2, height=2, fill_color=GRAY, fill_opacity=0.8)
        pole.shift(DOWN * 0.5)
        light = Circle(radius=0.3, fill_color=PROB_YELLOW, fill_opacity=0.8)
        light.shift(UP * 0.5)
        halo = Circle(radius=0.5, fill_color=PROB_YELLOW, fill_opacity=0.3, stroke_width=0)
        halo.shift(UP * 0.5)
        lamp.add(pole, halo, light)
        return lamp
    
    def create_home(self):
        """创建家"""
        home = VGroup()
        house = Rectangle(width=1.5, height=1.2, fill_color=PROB_BLUE, fill_opacity=0.8)
        roof = Polygon(
            [-0.85, 0.6, 0], [0.85, 0.6, 0], [0, 1.2, 0],
            fill_color=PROB_RED, fill_opacity=0.8
        )
        door = Rectangle(width=0.4, height=0.6, fill_color=GRAY, fill_opacity=0.9)
        door.shift(DOWN * 0.3)
        home.add(house, roof, door)
        return home
    
    def create_drunk_person(self):
        """创建醉汉"""
        drunk = VGroup()
        head = Circle(radius=0.2, fill_color=WHITE, fill_opacity=0.9)
        head.shift(UP * 0.3)
        body = Rectangle(width=0.3, height=0.5, fill_color=PROB_GRAY, fill_opacity=0.8)
        body.shift(DOWN * 0.1)
        drunk.add(head, body)
        return drunk
    
    def one_dimensional_walk_demo(self):
        """一维随机漫步演示"""
        self.clear()
        
        title = Text("让我们做个实验", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建简单的数轴
        number_line = NumberLine(
            x_range=[-10, 10, 1],
            length=10,
            include_numbers=True,
            include_tip=True,
            font_size=16,
            decimal_number_config={"num_decimal_places": 0}
        )
        number_line.move_to([0, 0.5, 0])
        
        self.play(Create(number_line))
        
        # 起始点
        walker = Dot(number_line.n2p(0), color=PROB_YELLOW, radius=0.2)
        home_marker = Dot(number_line.n2p(0), color=PROB_GREEN, radius=0.1)
        
        start_label = Text("起点（家）", font_size=SMALL_SIZE, color=PROB_GREEN)
        start_label.next_to(home_marker, UP, buff=0.5)
        
        self.play(Create(home_marker), Create(walker), Write(start_label))
        
        # 实时显示位置
        position_text = Text("当前位置：0", font_size=NORMAL_SIZE, color=WHITE)
        position_text.move_to([0, -1.5, 0])
        self.play(Write(position_text))
        
        # 模拟100步
        position = 0
        path_points = [number_line.n2p(0)]
        
        explanation = Text(
            "看！虽然每步都是随机的，但他总在家附近徘徊",
            font_size=NORMAL_SIZE,
            color=PROB_YELLOW
        )
        explanation.to_edge(DOWN, buff=0.5)
        
        for i in range(50):
            # 抛硬币决定方向
            direction = random.choice([-1, 1])
            position += direction
            new_point = number_line.n2p(position)
            path_points.append(new_point)
            
            # 更新位置
            self.play(
                walker.animate.move_to(new_point),
                run_time=0.1
            )
            
            # 更新文字
            if i % 10 == 0:
                new_text = Text(f"当前位置：{position}", font_size=NORMAL_SIZE, color=WHITE)
                new_text.move_to([0, -1.5, 0])
                self.play(Transform(position_text, new_text), run_time=0.1)
            
            # 在第30步时显示解释
            if i == 30:
                self.play(Write(explanation))
        
        # 画出路径
        path = VMobject()
        path.set_points_smoothly(path_points)
        path.set_stroke(color=PROB_BLUE, width=2, opacity=0.5)
        self.play(Create(path))
        
        # 回到原点
        if position != 0:
            return_text = Text(
                f"最后位置：{position}，离家{abs(position)}步",
                font_size=NORMAL_SIZE,
                color=PROB_RED
            )
            return_text.move_to([0, -2.5, 0])
            self.play(Write(return_text))
        else:
            return_text = Text(
                "太神奇了！正好回到家！",
                font_size=NORMAL_SIZE,
                color=PROB_GREEN
            )
            return_text.move_to([0, -2.5, 0])
            self.play(Write(return_text))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(number_line), FadeOut(walker),
            FadeOut(home_marker), FadeOut(start_label), FadeOut(position_text),
            FadeOut(explanation), FadeOut(return_text), FadeOut(path)
        )
    
    def amazing_discovery(self):
        """神奇的发现"""
        self.clear()
        
        title = Text("数学家的神奇发现", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 波利亚的发现
        discovery = VGroup(
            Text("1921年，数学家波利亚发现：", font_size=NORMAL_SIZE),
            Text("一维随机漫步", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("100%会回到起点！", font_size=38, color=PROB_GREEN, weight=BOLD),
            Text("（只要时间足够长）", font_size=SMALL_SIZE, color=GRAY)
        ).arrange(DOWN, buff=0.5)
        discovery.move_to([0, 0, 0])
        
        for line in discovery:
            self.play(Write(line), run_time=0.8)
        
        # 用图示解释
        self.wait(1)
        self.play(FadeOut(discovery))
        
        # 直观解释
        intuition = VGroup(
            Text("为什么呢？想想看：", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("向右走了10步", font_size=NORMAL_SIZE),
            Text("↓", font_size=SUBTITLE_SIZE),
            Text("必须向左走10步才能回家", font_size=NORMAL_SIZE),
            Text("↓", font_size=SUBTITLE_SIZE),
            Text("时间足够长，总会发生！", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.3)
        intuition.move_to([0, -0.5, 0])
        
        for line in intuition:
            self.play(Write(line), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(intuition))
    
    def two_dimensional_walk_simple(self):
        """二维随机漫步（简化版）"""
        self.clear()
        
        title = Text("如果醉汉可以走四个方向呢？", font_size=36, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建网格
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        grid.move_to([0, -0.5, 0])
        self.play(Create(grid))
        
        # 起点
        home = Dot(ORIGIN, color=PROB_GREEN, radius=0.15)
        home_label = Text("家", font_size=SMALL_SIZE, color=PROB_GREEN)
        home_label.next_to(home, UP, buff=0.3)
        
        walker = Dot(ORIGIN, color=PROB_YELLOW, radius=0.1)
        
        self.play(Create(home), Write(home_label), Create(walker))
        
        # 方向说明
        directions = VGroup(
            Text("上", font_size=SMALL_SIZE).move_to([0, 1, 0]),
            Text("下", font_size=SMALL_SIZE).move_to([0, -1, 0]),
            Text("左", font_size=SMALL_SIZE).move_to([-1, 0, 0]),
            Text("右", font_size=SMALL_SIZE).move_to([1, 0, 0])
        )
        
        # 闪烁显示方向
        for d in directions:
            self.play(FadeIn(d, scale=1.5), run_time=0.3)
            self.play(FadeOut(d), run_time=0.3)
        
        # 模拟行走
        x, y = 0, 0
        path_points = [grid.c2p(x, y)]
        
        for _ in range(60):
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up' and y < 4:
                y += 1
            elif direction == 'down' and y > -4:
                y -= 1
            elif direction == 'left' and x > -4:
                x -= 1
            elif direction == 'right' and x < 4:
                x += 1
            
            new_point = grid.c2p(x, y)
            path_points.append(new_point)
            
            self.play(walker.animate.move_to(new_point), run_time=0.1)
        
        # 画出路径
        path = VMobject()
        path.set_points_smoothly(path_points)
        path.set_stroke(color=PROB_BLUE, width=2, opacity=0.6)
        self.play(Create(path))
        
        # 结论
        conclusion = Text(
            "二维随机漫步也会回家！",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN
        )
        conclusion.to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        # 但是三维...
        but_text = Text(
            "但如果醉汉能飞呢？让我们看看...",
            font_size=NORMAL_SIZE,
            color=PROB_RED
        )
        but_text.to_edge(DOWN, buff=1.5)
        self.play(Transform(conclusion, but_text))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(grid), FadeOut(home), FadeOut(home_label),
            FadeOut(walker), FadeOut(path), FadeOut(conclusion)
        )
    
    def three_dimensional_walk(self):
        """三维随机漫步演示"""
        self.clear()
        
        title = Text("三维随机漫步：醉鸟的困境", font_size=38, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建3D坐标系
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=5,
            y_length=5,
            z_length=5,
        )
        axes.move_to(ORIGIN)
        
        # 设置相机角度
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        self.play(Create(axes))
        
        # 起点（鸟巢）
        home = Sphere(radius=0.2, color=PROB_GREEN)
        home.move_to(axes.c2p(0, 0, 0))
        home_label = Text("鸟巢", font_size=SMALL_SIZE, color=PROB_GREEN)
        home_label.next_to(home, UP, buff=0.3)
        
        # 醉鸟
        bird = Sphere(radius=0.15, color=PROB_YELLOW)
        bird.move_to(axes.c2p(0, 0, 0))
        
        self.play(Create(home), Write(home_label), Create(bird))
        
        # 说明六个方向
        directions_text = Text(
            "鸟可以飞向6个方向：上下左右前后",
            font_size=NORMAL_SIZE,
            color=WHITE
        )
        directions_text.to_edge(DOWN, buff=0.8)
        self.play(Write(directions_text))
        
        # 开始随机飞行
        x, y, z = 0, 0, 0
        path_points = [axes.c2p(x, y, z)]
        
        # 记录路径
        path_lines = VGroup()
        
        for i in range(40):
            # 随机选择方向
            direction = random.choice(['x+', 'x-', 'y+', 'y-', 'z+', 'z-'])
            
            old_pos = axes.c2p(x, y, z)
            
            if direction == 'x+' and x < 3:
                x += 1
            elif direction == 'x-' and x > -3:
                x -= 1
            elif direction == 'y+' and y < 3:
                y += 1
            elif direction == 'y-' and y > -3:
                y -= 1
            elif direction == 'z+' and z < 3:
                z += 1
            elif direction == 'z-' and z > -3:
                z -= 1
            
            new_pos = axes.c2p(x, y, z)
            path_points.append(new_pos)
            
            # 创建路径线段
            path_segment = Line(
                old_pos, new_pos,
                color=PROB_BLUE,
                stroke_width=2,
                stroke_opacity=0.6
            )
            path_lines.add(path_segment)
            
            # 动画
            self.play(
                bird.animate.move_to(new_pos),
                Create(path_segment),
                run_time=0.2
            )
            
            # 旋转相机以更好地展示3D效果
            if i % 10 == 0:
                self.move_camera(
                    phi=60 * DEGREES,
                    theta=(self.camera.theta + 30 * DEGREES) % (360 * DEGREES),
                    run_time=1
                )
        
        # 计算距离
        distance = np.sqrt(x**2 + y**2 + z**2)
        distance_text = Text(
            f"离巢距离：{distance:.1f}",
            font_size=NORMAL_SIZE,
            color=PROB_YELLOW
        )
        distance_text.to_edge(LEFT).shift(UP*2)
        self.play(Write(distance_text))
        
        # 结论
        self.play(FadeOut(directions_text))
        
        conclusion = VGroup(
            Text("三维随机漫步的残酷真相：", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("回家概率 < 35%", font_size=SUBTITLE_SIZE, color=PROB_RED, weight=BOLD),
            Text("醉鸟可能永远找不到家！", font_size=NORMAL_SIZE, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.3)
        conclusion.to_edge(DOWN, buff=0.5)
        
        for line in conclusion:
            self.play(Write(line), run_time=0.8)
        
        # 最后旋转一圈展示全貌
        self.move_camera(
            phi=60 * DEGREES,
            theta=360 * DEGREES,
            run_time=3
        )
        
        self.wait(2)
        
        # 恢复2D视角
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(home), FadeOut(home_label),
            FadeOut(bird), FadeOut(path_lines), FadeOut(distance_text),
            FadeOut(conclusion)
        )
        self.wait(3)
    
    def real_life_examples(self):
        """生活中的例子"""
        self.clear()
        
        title = Text("随机漫步在生活中无处不在", font_size=38, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        examples = VGroup(
            VGroup(
                Text("花粉在水中", font_size=NORMAL_SIZE, color=PROB_YELLOW),
                Text("被水分子撞来撞去", font_size=SMALL_SIZE, color=GRAY),
                Text("→ 布朗运动", font_size=SMALL_SIZE, color=PROB_GREEN)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("股票价格", font_size=NORMAL_SIZE, color=PROB_YELLOW),
                Text("买卖力量的随机博弈", font_size=SMALL_SIZE, color=GRAY),
                Text("→ 金融市场", font_size=SMALL_SIZE, color=PROB_GREEN)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("动物觅食", font_size=NORMAL_SIZE, color=PROB_YELLOW),
                Text("在未知环境中寻找食物", font_size=SMALL_SIZE, color=GRAY),
                Text("→ 生态学", font_size=SMALL_SIZE, color=PROB_GREEN)
            ).arrange(DOWN, buff=0.2)
        ).arrange(DOWN, buff=0.8)
        examples.move_to([0, -0.5, 0])
        
        for example in examples:
            self.play(Write(example), run_time=1.2)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(examples))
    
    def stock_market_realistic(self):
        """更真实的股市应用"""
        self.clear()
        
        title = Text("股价真的是随机的吗？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建更真实的股价图
        axes = Axes(
            x_range=[0, 250, 50],
            y_range=[80, 120, 10],
            x_length=8,
            y_length=4,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 14
            }
        )
        axes.move_to([0, 0, 0])
        
        x_label = Text("交易日", font_size=SMALL_SIZE).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("价格", font_size=SMALL_SIZE).next_to(axes.y_axis, LEFT, buff=0.3).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 生成更真实的股价（有涨有跌）
        n_days = 250
        prices = [100]  # 起始价格
        
        # 模拟真实的涨跌
        for i in range(n_days):
            # 日收益率：平均值接近0，有正有负
            daily_return = random.gauss(0.0001, 0.02)  # 均值很小，波动率2%
            
            # 偶尔有大跌或大涨
            if random.random() < 0.05:  # 5%概率出现大波动
                daily_return = random.choice([-0.05, 0.04])  # 大跌5%或大涨4%
            
            new_price = prices[-1] * (1 + daily_return)
            prices.append(max(new_price, 50))  # 最低不低于50
        
        # 绘制股价曲线
        t = np.arange(0, n_days + 1)
        stock_path = axes.plot_line_graph(
            x_values=t,
            y_values=prices,
            line_color=PROB_BLUE,
            stroke_width=2,
            add_vertex_dots=False
        )
        
        self.play(Create(stock_path), run_time=3)
        
        # 标注一些特征
        # 找到最高点和最低点
        max_idx = prices.index(max(prices))
        min_idx = prices.index(min(prices))
        
        max_dot = Dot(axes.c2p(max_idx, prices[max_idx]), color=PROB_GREEN, radius=0.08)
        min_dot = Dot(axes.c2p(min_idx, prices[min_idx]), color=PROB_RED, radius=0.08)
        
        max_label = Text("高点", font_size=SMALL_SIZE, color=PROB_GREEN)
        max_label.next_to(max_dot, UP, buff=0.2)
        
        min_label = Text("低点", font_size=SMALL_SIZE, color=PROB_RED)
        min_label.next_to(min_dot, DOWN, buff=0.2)
        
        self.play(Create(max_dot), Write(max_label))
        self.play(Create(min_dot), Write(min_label))
        
        # 解释
        explanation = VGroup(
            Text("看起来很随机对吧？", font_size=NORMAL_SIZE),
            Text("但真的完全随机吗？", font_size=NORMAL_SIZE, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.3)
        explanation.to_edge(DOWN, buff=0.8)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 转场
        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(stock_path), FadeOut(max_dot), FadeOut(min_dot),
            FadeOut(max_label), FadeOut(min_label), FadeOut(explanation)
        )
        
        # 展示争议
        self.show_stock_controversy()
        
        self.play(FadeOut(title))
    
    def show_stock_controversy(self):
        """展示股市随机性的争议"""
        # 支持随机的观点
        random_view = VGroup(
            Text("支持随机漫步：", font_size=NORMAL_SIZE, color=PROB_GREEN),
            Text("• 短期价格无法预测", font_size=SMALL_SIZE),
            Text("• 消息瞬间反映在价格中", font_size=SMALL_SIZE),
            Text("• 技术分析常常失败", font_size=SMALL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        random_view.move_to([-3.5, 0.5, 0])
        
        # 反对随机的观点
        not_random_view = VGroup(
            Text("反对完全随机：", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("• 存在趋势和周期", font_size=SMALL_SIZE),
            Text("• 恐慌和贪婪造成极端", font_size=SMALL_SIZE),
            Text("• 价值投资确实有效", font_size=SMALL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        not_random_view.move_to([3.5, 0.5, 0])
        
        self.play(Write(random_view))
        self.play(Write(not_random_view))
        
        # 结论
        conclusion = Text(
            "真相：部分随机 + 部分规律",
            font_size=SUBTITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        conclusion.to_edge(DOWN, buff=0.8)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(FadeOut(random_view), FadeOut(not_random_view), FadeOut(conclusion))
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        # 核心要点回顾
        takeaways = VGroup(
            Text("今天我们学到了：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("1. 随机漫步 = 每步都是随机的运动", font_size=NORMAL_SIZE),
            Text("2. 一维必定回家，二维也会回家", font_size=NORMAL_SIZE),
            Text("3. 三维只有35%概率回家", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("4. 生活中到处都有随机漫步", font_size=NORMAL_SIZE),
            Text("5. 股市既随机又不完全随机", font_size=NORMAL_SIZE)
        ).arrange(DOWN, buff=0.4)
        
        for line in takeaways:
            self.play(Write(line), run_time=0.8)
        
        self.wait(3)
        self.play(FadeOut(takeaways))
        
        # 哲理总结
        philosophy = VGroup(
            Text("随机中有规律", font_size=42, color=PROB_PURPLE),
            Text("混沌中有秩序", font_size=42, color=PROB_PURPLE),
            Text("这就是数学的魅力！", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.8)
        
        for line in philosophy:
            self.play(Write(line), run_time=1.2)
        
        self.wait(3)
        self.play(FadeOut(philosophy))
        
        # 下期预告
        self.show_next_episode_preview()
    
    def show_next_episode_preview(self):
        """下期预告"""
        preview_title = Text("下期预告", font_size=38, color=PROB_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))
        
        ep16_title = Text(
            "第16集：马尔可夫链",
            font_size=TITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep16_title.move_to([0, 1.5, 0])
        
        preview_content = VGroup(
            Text("如果随机也有记忆...", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("天气预报是怎么做的？", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("Google如何给网页排名？", font_size=SUBTITLE_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.5)
        preview_content.move_to([0, -0.5, 0])
        
        self.play(Write(ep16_title))
        for line in preview_content:
            self.play(Write(line), run_time=0.8)
        
        think_question = Text(
            "思考：明天的天气只和今天有关吗？",
            font_size=24,
            color=PROB_YELLOW
        )
        think_question.to_edge(DOWN, buff=0.8)
        
        self.play(Write(think_question))
        self.wait(3)
        
        see_you = Text(
            "下期见！",
            font_size=38,
            color=WHITE
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title), FadeOut(ep16_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))