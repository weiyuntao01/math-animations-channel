"""
数字仿生系列 第3集：涌现的智慧
Digital Biomimetics EP03: Emergent Intelligence

简单规则创造复杂行为 - 鱼群与蚁群的集体智慧
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple, Dict
from dataclasses import dataclass, field
from scipy.spatial import KDTree

# 数字仿生系列颜色主题 - 保持与前两集一致
BIO_CYAN = ManimColor("#00FFE5")      # 生命青
BIO_PURPLE = ManimColor("#8B5CF6")    # 神经紫
BIO_GREEN = ManimColor("#00FF88")     # 细胞绿
BIO_BLUE = ManimColor("#007EFF")      # 深海蓝
BIO_YELLOW = ManimColor("#FFE500")    # 能量黄
BIO_RED = ManimColor("#FF0066")       # 血液红
BIO_WHITE = ManimColor("#FFFFFF")     # 纯白
BIO_GRAY = ManimColor("#303030")      # 深灰背景

# EP03特殊颜色 - 群体智慧主题
SWARM_BLUE = ManimColor("#00BFFF")    # 鱼群蓝
SWARM_GOLD = ManimColor("#FFD700")    # 蚁群金
EMERGE_PURPLE = ManimColor("#9370DB")  # 涌现紫
NEURAL_GREEN = ManimColor("#32CD32")   # 神经绿

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


@dataclass
class Boid:
    """增强版Boid个体 - 包含记忆和学习能力"""
    position: np.ndarray = None
    velocity: np.ndarray = None
    acceleration: np.ndarray = None
    max_speed: float = 2.0
    max_force: float = 0.05
    perception_radius: float = 1.5
    memory: List[np.ndarray] = None
    behavior_weights: Dict[str, float] = None
    
    def __post_init__(self):
        """初始化Boid对象"""
        if self.position is None:
            # 如果没有提供位置，随机生成
            x = random.uniform(-6, 6)
            y = random.uniform(-3, 3)
            self.position = np.array([x, y, 0.0])
        
        if self.velocity is None:
            angle = random.uniform(0, 2 * PI)
            self.velocity = np.array([np.cos(angle), np.sin(angle), 0]) * self.max_speed
        
        if self.acceleration is None:
            self.acceleration = np.zeros(3)
        
        if self.memory is None:
            self.memory = []
        
        if self.behavior_weights is None:
            self.behavior_weights = {
                'separation': 1.5,
                'alignment': 1.0,
                'cohesion': 1.0,
                'emergence': 0.5
            }
    
    def update(self, dt=0.016):
        """更新位置和速度"""
        self.velocity += self.acceleration * dt * 60
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity = (self.velocity / speed) * self.max_speed
        self.position += self.velocity * dt
        self.acceleration *= 0
        
        # 更新记忆
        if len(self.memory) > 10:
            self.memory.pop(0)
        self.memory.append(self.position.copy())


class SwarmSystem:
    """群体系统 - 实现增强版Boids算法"""
    
    def __init__(self, num_boids=100, boundary=7):
        self.boids = []
        self.boundary = boundary
        self.time = 0
        self.emergence_field = None
        
        # 初始化群体
        for _ in range(num_boids):
            x = random.uniform(-boundary + 1, boundary - 1)
            y = random.uniform(-boundary/2 + 1, boundary/2 - 1)
            boid = Boid(position=np.array([x, y, 0.0]))
            self.boids.append(boid)
        
        # 构建空间索引
        self.update_spatial_index()
    
    def update_spatial_index(self):
        """更新KD树以加速邻居查找"""
        positions = np.array([b.position[:2] for b in self.boids])
        self.kdtree = KDTree(positions)
    
    def find_neighbors(self, boid, radius):
        """高效查找邻居"""
        indices = self.kdtree.query_ball_point(boid.position[:2], radius)
        return [self.boids[i] for i in indices if id(self.boids[i]) != id(boid)]
    
    def separation(self, boid, neighbors):
        """分离力 - 避免碰撞"""
        if not neighbors:
            return np.zeros(3)
        
        steer = np.zeros(3)
        for other in neighbors:
            diff = boid.position - other.position
            dist = np.linalg.norm(diff)
            if dist > 0 and dist < 0.5:  # 近距离强斥力
                steer += (diff / dist) / (dist + 0.01)  # 反平方律
        
        if np.linalg.norm(steer) > 0:
            steer = (steer / np.linalg.norm(steer)) * boid.max_speed
            steer -= boid.velocity
            if np.linalg.norm(steer) > boid.max_force:
                steer = (steer / np.linalg.norm(steer)) * boid.max_force
        
        return steer
    
    def alignment(self, boid, neighbors):
        """对齐力 - 速度同步"""
        if not neighbors:
            return np.zeros(3)
        
        avg_vel = np.mean([n.velocity for n in neighbors], axis=0)
        avg_vel = (avg_vel / np.linalg.norm(avg_vel)) * boid.max_speed
        steer = avg_vel - boid.velocity
        
        if np.linalg.norm(steer) > boid.max_force:
            steer = (steer / np.linalg.norm(steer)) * boid.max_force
        
        return steer
    
    def cohesion(self, boid, neighbors):
        """凝聚力 - 群体聚集"""
        if not neighbors:
            return np.zeros(3)
        
        center = np.mean([n.position for n in neighbors], axis=0)
        desired = center - boid.position
        
        if np.linalg.norm(desired) > 0:
            desired = (desired / np.linalg.norm(desired)) * boid.max_speed
            steer = desired - boid.velocity
            if np.linalg.norm(steer) > boid.max_force:
                steer = (steer / np.linalg.norm(steer)) * boid.max_force
            return steer
        
        return np.zeros(3)
    
    def emergence_force(self, boid, t):
        """涌现力 - 产生集体模式"""
        # 基于全局相位的协同行为
        global_phase = t * 2
        local_phase = np.arctan2(boid.position[1], boid.position[0])
        
        # 创造螺旋涌现模式
        spiral_force = np.array([
            -boid.position[1] * 0.1,
            boid.position[0] * 0.1,
            0
        ]) * np.sin(global_phase + local_phase)
        
        # 添加脉动效果
        pulse = np.sin(global_phase * 3) * 0.5 + 0.5
        center_force = -boid.position * 0.05 * pulse
        
        return spiral_force + center_force
    
    def update(self, t, dt=0.016):
        """更新整个群体"""
        self.time = t
        self.update_spatial_index()
        
        forces = []
        for boid in self.boids:
            neighbors = self.find_neighbors(boid, boid.perception_radius)
            
            # 计算各种力
            sep = self.separation(boid, neighbors) * boid.behavior_weights['separation']
            ali = self.alignment(boid, neighbors) * boid.behavior_weights['alignment']
            coh = self.cohesion(boid, neighbors) * boid.behavior_weights['cohesion']
            eme = self.emergence_force(boid, t) * boid.behavior_weights['emergence']
            
            # 边界回弹
            boundary_force = self.boundary_force(boid)
            
            total_force = sep + ali + coh + eme + boundary_force
            forces.append(total_force)
        
        # 应用力并更新
        for boid, force in zip(self.boids, forces):
            boid.acceleration = force
            boid.update(dt)
    
    def boundary_force(self, boid):
        """边界排斥力"""
        force = np.zeros(3)
        margin = 1.0
        
        if boid.position[0] < -self.boundary + margin:
            force[0] = (margin - (boid.position[0] + self.boundary)) * 0.5
        elif boid.position[0] > self.boundary - margin:
            force[0] = -(margin - (self.boundary - boid.position[0])) * 0.5
        
        if boid.position[1] < -self.boundary/2 + margin:
            force[1] = (margin - (boid.position[1] + self.boundary/2)) * 0.5
        elif boid.position[1] > self.boundary/2 - margin:
            force[1] = -(margin - (self.boundary/2 - boid.position[1])) * 0.5
        
        return force


class DigitalBiomimeticsEP03(Scene):
    """数字仿生系列 第3集"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置背景色
        self.camera.background_color = "#090909"
        
        # 1. 系列开场
        self.show_series_intro()
        
        # 2. 回应EP02的预告
        self.answer_preview_question()
        
        # 3. 涌现现象的数学本质
        self.emergence_mathematics()
        
        # 4. 第一个展示：鱼群的流体智慧
        self.fish_swarm_intelligence()
        
        # 5. 第二个展示：蚁群的信息网络
        self.ant_colony_optimization()
        
        # 6. 涌现的哲学意义
        self.emergence_philosophy()
        
        # 7. 对比展示：个体vs群体
        self.individual_vs_collective()
        
        # 8. 结尾与预告
        self.show_ending()
    
    def show_series_intro(self):
        """系列开场动画 - 保持风格一致性"""
        # 群体粒子背景
        swarm_bg = self.create_swarm_background()
        swarm_bg.set_opacity(0.2)
        self.play(Create(swarm_bg), run_time=2)
        
        # 系列标题
        series_title = Text(
            "数字仿生",
            font_size=60,
            color=BIO_CYAN,
            weight=BOLD
        )
        series_title.move_to([0, 1, 0])
        
        subtitle = Text(
            "DIGITAL BIOMIMETICS",
            font_size=24,
            color=BIO_WHITE,
            font="Arial"
        )
        subtitle.next_to(series_title, DOWN, buff=0.3)
        
        # 第3集标题
        episode_text = Text(
            "第3集：涌现的智慧",
            font_size=34,
            color=EMERGE_PURPLE
        )
        episode_text.move_to([0, -1.5, 0])
        
        # 动画序列
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.wait(0.5)
        self.play(Write(episode_text), run_time=1.5)
        
        # 脉动效果
        self.play(
            series_title.animate.scale(1.1).set_color(SWARM_BLUE),
            rate_func=there_and_back,
            run_time=1
        )
        
        self.wait(2)
        self.play(
            FadeOut(series_title),
            FadeOut(subtitle),
            FadeOut(episode_text),
            FadeOut(swarm_bg)
        )
    
    def create_swarm_background(self):
        """创建群体运动背景"""
        bg = VGroup()
        
        # 创建流动的点阵
        for i in range(30):
            for j in range(15):
                x = -7 + i * 0.5
                y = -3.5 + j * 0.5
                
                # 添加随机偏移
                x += 0.2 * np.sin(i * 0.5)
                y += 0.2 * np.cos(j * 0.5)
                
                dot = Dot(
                    point=[x, y, 0],
                    radius=0.02,
                    color=SWARM_BLUE,
                    fill_opacity=0.3
                )
                
                # 创建连线
                if i > 0 and j > 0:
                    if random.random() > 0.7:
                        line = Line(
                            [x, y, 0],
                            [x - 0.5, y - 0.5, 0],
                            stroke_width=0.5,
                            color=EMERGE_PURPLE,
                            stroke_opacity=0.2
                        )
                        bg.add(line)
                
                bg.add(dot)
        
        return bg
    
    def answer_preview_question(self):
        """回应EP02的预告问题"""
        title = Text(
            "个体的简单规则",
            font_size=TITLE_SIZE,
            color=SWARM_GOLD
        )
        title.to_edge(UP, buff=0.5)
        
        question = Text(
            "如何产生群体的复杂智慧？",
            font_size=TITLE_SIZE,
            color=EMERGE_PURPLE
        )
        question.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(question))
        
        # 三个核心规则
        rules = VGroup(
            Text("分离 Separation", font_size=NORMAL_SIZE, color=BIO_RED),
            Text("对齐 Alignment", font_size=NORMAL_SIZE, color=BIO_GREEN),
            Text("凝聚 Cohesion", font_size=NORMAL_SIZE, color=BIO_BLUE)
        ).arrange(RIGHT, buff=1.5)
        rules.move_to([0, -1, 0])
        
        # 可视化三个规则
        for rule in rules:
            self.play(FadeIn(rule, scale=0.8), run_time=0.8)
        
        # 涌现箭头
        emerge_arrow = Arrow(
            start=[0, -1.8, 0],
            end=[0, -2.8, 0],
            color=EMERGE_PURPLE,
            stroke_width=8
        )
        emerge_text = Text(
            "涌现",
            font_size=SUBTITLE_SIZE,
            color=EMERGE_PURPLE,
            weight=BOLD
        )
        emerge_text.next_to(emerge_arrow, RIGHT)
        
        self.play(
            GrowArrow(emerge_arrow),
            Write(emerge_text)
        )
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(question),
            FadeOut(rules),
            FadeOut(emerge_arrow),
            FadeOut(emerge_text)
        )
    
    def emergence_mathematics(self):
        """涌现现象的数学本质"""
        title = Text("涌现的数学密码", font_size=TITLE_SIZE, color=EMERGE_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 左列：Boids 三力
        left_header = Text("核心算法：Boids Model", font_size=SUBTITLE_SIZE, color=BIO_WHITE)
        sep_eq = MathTex(
            r"F_{sep} = -k_1 \sum_{j} \frac{\vec{p}_i - \vec{p}_j}{|\vec{p}_i - \vec{p}_j|^2}",
            font_size=30,
            color=BIO_RED
        )
        ali_eq = MathTex(
            r"F_{ali} = k_2 (\vec{v}_{avg} - \vec{v}_i)",
            font_size=30,
            color=BIO_GREEN
        )
        coh_eq = MathTex(
            r"F_{coh} = k_3 (\vec{p}_{center} - \vec{p}_i)",
            font_size=30,
            color=BIO_BLUE
        )
        left_col = VGroup(left_header, sep_eq, ali_eq, coh_eq).arrange(DOWN, aligned_edge=LEFT, buff=0.6)

        # 右列：涌现方程 + 洞察
        right_header = Text("涌现方程", font_size=SUBTITLE_SIZE, color=BIO_WHITE)
        emerge_eq = MathTex(
            r"F_{emerge} = k_4 \sin(\phi_{global} + \phi_{local}) \cdot \nabla \Psi",
            font_size=30,
            color=EMERGE_PURPLE
        )
        insight_group = VGroup(
            Text("1 + 1 > 2", font_size=48, color=SWARM_GOLD),
            Text("整体大于部分之和", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        right_col = VGroup(right_header, emerge_eq, insight_group).arrange(DOWN, aligned_edge=LEFT, buff=0.6)

        columns = VGroup(left_col, right_col).arrange(RIGHT, buff=3.0, aligned_edge=UP)
        columns.next_to(title, DOWN, buff=0.6)

        # 逐步呈现，减少同屏拥挤
        self.play(Write(left_header))
        for eq in [sep_eq, ali_eq, coh_eq]:
            self.play(Write(eq), run_time=0.6)
        self.play(Write(right_header))
        self.play(Write(emerge_eq), run_time=0.8)
        self.play(Write(insight_group))
        self.wait(2)

        self.play(
            FadeOut(title),
            FadeOut(columns)
        )
    
    def fish_swarm_intelligence(self):
        """鱼群的流体智慧 - 核心展示"""
        self.clear()
        
        title = Text("生命形态 I：深海鱼群", font_size=SUBTITLE_SIZE, color=SWARM_BLUE)
        title.to_edge(UP, buff=0.5)
        
        # 显示参数
        params = VGroup(
            MathTex(r"N = 500", font_size=20, color=BIO_WHITE),
            MathTex(r"v_{max} = 2.0", font_size=20, color=BIO_WHITE),
            MathTex(r"r_{perception} = 1.5", font_size=20, color=BIO_WHITE)
        ).arrange(RIGHT, buff=1)
        params.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(params))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建鱼群系统
        swarm = SwarmSystem(num_boids=500, boundary=7)
        
        def create_fish_swarm():
            t = t_tracker.get_value()
            swarm.update(t)
            
            fish_group = VGroup()
            
            # 计算群体中心和平均速度用于着色
            center = np.mean([b.position for b in swarm.boids], axis=0)
            
            for i, boid in enumerate(swarm.boids):
                # 计算到中心的距离
                dist_to_center = np.linalg.norm(boid.position - center)
                
                # 根据位置和速度创建颜色梯度
                speed = np.linalg.norm(boid.velocity)
                color_factor = (speed / boid.max_speed) * 0.7 + dist_to_center * 0.1
                color_factor = np.clip(color_factor, 0, 1)
                
                # 鱼的颜色：从深蓝到亮青
                fish_color = interpolate_color(BIO_BLUE, SWARM_BLUE, color_factor)
                
                # 创建鱼形（简化的三角形）
                heading = np.arctan2(boid.velocity[1], boid.velocity[0])
                
                # 鱼身
                fish = Polygon(
                    boid.position + rotate_vector(np.array([0.08, 0, 0]), heading),
                    boid.position + rotate_vector(np.array([-0.04, 0.03, 0]), heading),
                    boid.position + rotate_vector(np.array([-0.04, -0.03, 0]), heading),
                    color=fish_color,
                    fill_opacity=0.8,
                    stroke_width=0
                )
                
                # 添加发光效果（领头鱼）
                if i < 10:  # 前10条鱼作为领导者
                    glow = Dot(
                        point=boid.position,
                        radius=0.15,
                        color=SWARM_GOLD,
                        fill_opacity=0.2
                    )
                    fish_group.add(glow)
                
                fish_group.add(fish)
            
            # 添加流场可视化
            if int(t * 10) % 5 == 0:  # 每0.5秒更新一次
                for _ in range(20):
                    x = random.uniform(-6, 6)
                    y = random.uniform(-3, 3)
                    flow_line = Line(
                        [x, y, 0],
                        [x - 0.2, y - 0.1, 0],
                        stroke_width=0.5,
                        color=BIO_CYAN,
                        stroke_opacity=0.1
                    )
                    fish_group.add(flow_line)
            
            return fish_group
        
        # 创建鱼群动画
        fish_swarm = always_redraw(create_fish_swarm)
        
        # 信息面板
        info_text = VGroup(
            Text("观察：个体遵循简单规则", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("涌现：群体形成复杂模式", font_size=SMALL_SIZE, color=EMERGE_PURPLE)
        ).arrange(DOWN, buff=0.2)
        info_text.to_edge(DOWN, buff=0.5)
        
        self.add(fish_swarm)
        self.play(Write(info_text))
        
        # 动画
        self.play(
            t_tracker.animate.set_value(8),
            run_time=20,
            rate_func=linear
        )
        
        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(params),
            FadeOut(info_text),
            FadeOut(fish_swarm)
        )
    
    def ant_colony_optimization(self):
        """蚁群优化算法展示"""
        self.clear()
        
        title = Text("生命形态 II：蚁群觅食", font_size=SUBTITLE_SIZE, color=SWARM_GOLD)
        title.to_edge(UP, buff=0.5)
        
        # 信息素方程
        formula = MathTex(
            r"p_{ij}^k = \frac{[\tau_{ij}]^\alpha \cdot [\eta_{ij}]^\beta}{\sum_{l \in N_i^k} [\tau_{il}]^\alpha \cdot [\eta_{il}]^\beta}",
            font_size=22,
            color=SWARM_GOLD
        )
        formula.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(formula))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建蚁群环境
        def create_ant_colony():
            t = t_tracker.get_value()
            colony = VGroup()
            
            # 巢穴
            nest = Circle(
                radius=0.3,
                color=SWARM_GOLD,
                fill_opacity=0.5
            )
            nest.move_to([-4, 0, 0])
            colony.add(nest)
            
            # 食物源
            food_sources = [
                [3, 1.5, 0],
                [4, -1, 0],
                [2, 0, 0]
            ]
            for food_pos in food_sources:
                food = Circle(
                    radius=0.2,
                    color=BIO_GREEN,
                    fill_opacity=0.6
                )
                food.move_to(food_pos)
                colony.add(food)
            
            # 信息素轨迹（使用贝塞尔曲线）
            pheromone_trails = VGroup()
            
            # 主路径
            main_path = CubicBezier(
                [-4, 0, 0],
                [-2, 0.5, 0],
                [0, 0.3, 0],
                [2, 0, 0],
                color=SWARM_GOLD,
                stroke_width=3,
                stroke_opacity=0.3 + 0.2 * np.sin(t * 2)
            )
            pheromone_trails.add(main_path)
            
            # 分支路径
            for food_pos in food_sources:
                branch = CubicBezier(
                    [2, 0, 0],
                    [(2 + food_pos[0])/2, food_pos[1]/2, 0],
                    food_pos,
                    food_pos,
                    color=SWARM_GOLD,
                    stroke_width=2,
                    stroke_opacity=0.2 + 0.1 * np.sin(t * 3 + food_pos[0])
                )
                pheromone_trails.add(branch)
            
            colony.add(pheromone_trails)
            
            # 蚂蚁个体
            num_ants = 100
            for i in range(num_ants):
                # 沿路径分布
                path_t = (i / num_ants + t * 0.2) % 1
                
                if i < 60:  # 主路径上的蚂蚁
                    pos = main_path.point_from_proportion(path_t)
                else:  # 分支路径上的蚂蚁
                    branch_idx = (i - 60) % 3
                    branch_t = ((i - 60) / 40 + t * 0.3) % 1
                    if branch_idx < len(pheromone_trails) - 1:
                        pos = pheromone_trails[branch_idx + 1].point_from_proportion(branch_t)
                    else:
                        pos = main_path.point_from_proportion(path_t)
                
                # 添加随机扰动
                noise = np.array([
                    0.1 * np.sin(i * 0.5 + t * 5),
                    0.1 * np.cos(i * 0.7 + t * 4),
                    0
                ])
                
                ant = Dot(
                    point=pos + noise,
                    radius=0.02,
                    color=BIO_YELLOW if i % 10 == 0 else BIO_WHITE,
                    fill_opacity=0.8
                )
                colony.add(ant)
            
            # 添加信息流动效果
            for _ in range(10):
                info_particle = Dot(
                    point=main_path.point_from_proportion(random.random()),
                    radius=0.01,
                    color=EMERGE_PURPLE,
                    fill_opacity=0.3 + 0.3 * np.sin(t * 10)
                )
                colony.add(info_particle)
            
            return colony
        
        # 创建蚁群
        ant_colony = always_redraw(create_ant_colony)
        
        # 算法说明
        algo_text = VGroup(
            Text("信息素通信", font_size=SMALL_SIZE, color=SWARM_GOLD),
            Text("路径优化", font_size=SMALL_SIZE, color=BIO_GREEN),
            Text("集体决策", font_size=SMALL_SIZE, color=EMERGE_PURPLE)
        ).arrange(RIGHT, buff=1)
        algo_text.to_edge(DOWN, buff=0.5)
        
        self.add(ant_colony)
        self.play(Write(algo_text))
        
        # 动画
        self.play(
            t_tracker.animate.set_value(4 * PI),
            run_time=15,
            rate_func=linear
        )
        
        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(algo_text),
            FadeOut(ant_colony)
        )
    
    def emergence_philosophy(self):
        """涌现的哲学意义"""
        self.clear()
        
        title = Text("涌现：从量变到质变", font_size=TITLE_SIZE, color=EMERGE_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 层级展示
        levels = VGroup()
        
        # 第一层：个体
        level1 = VGroup(
            Text("个体", font_size=NORMAL_SIZE, color=BIO_WHITE),
            MathTex(r"f(x) = ax + b", font_size=20, color=BIO_CYAN)
        ).arrange(DOWN, buff=0.2)
        level1.move_to([-4, 1, 0])
        
        # 第二层：局部交互
        level2 = VGroup(
            Text("局部交互", font_size=NORMAL_SIZE, color=BIO_WHITE),
            MathTex(r"g(x,y) = f(x) \otimes f(y)", font_size=20, color=BIO_GREEN)
        ).arrange(DOWN, buff=0.2)
        level2.move_to([0, 1, 0])
        
        # 第三层：全局涌现
        level3 = VGroup(
            Text("全局涌现", font_size=NORMAL_SIZE, color=BIO_WHITE),
            MathTex(r"\Phi = \int\int g(x,y) \, dx \, dy", font_size=20, color=EMERGE_PURPLE)
        ).arrange(DOWN, buff=0.2)
        level3.move_to([4, 1, 0])
        
        # 箭头连接
        arrow1 = Arrow(
            level1.get_right(),
            level2.get_left(),
            color=BIO_YELLOW
        )
        arrow2 = Arrow(
            level2.get_right(),
            level3.get_left(),
            color=BIO_YELLOW
        )
        
        # 动画展示
        self.play(Write(level1))
        self.play(GrowArrow(arrow1))
        self.play(Write(level2))
        self.play(GrowArrow(arrow2))
        self.play(Write(level3))
        
        # 哲学观点
        philosophy = VGroup(
            Text("简单规则 × 大量个体 = 复杂智慧", font_size=SUBTITLE_SIZE, color=SWARM_GOLD),
            Text("这就是生命的奇迹", font_size=NORMAL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.5)
        philosophy.to_edge(DOWN, buff=0.8)
        
        self.play(Write(philosophy))
        self.wait(3)
        
        self.play(
            FadeOut(title),
            FadeOut(level1),
            FadeOut(level2),
            FadeOut(level3),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(philosophy)
        )
    
    def individual_vs_collective(self):
        """个体vs群体的对比展示"""
        self.clear()
        
        title = Text("个体智慧 vs 群体智慧", font_size=TITLE_SIZE, color=EMERGE_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 左侧：单个个体
        individual_title = Text("单个个体", font_size=NORMAL_SIZE, color=BIO_CYAN)
        individual_title.move_to([-3.5, 2, 0])
        
        # 单个粒子的随机运动
        t_tracker = ValueTracker(0)
        
        def create_individual():
            t = t_tracker.get_value()
            pos = np.array([
                -3.5 + 0.5 * np.sin(t * 2),
                0.5 * np.cos(t * 3),
                0
            ])
            return Dot(point=pos, radius=0.1, color=BIO_CYAN)
        
        individual = always_redraw(create_individual)
        
        # 右侧：群体
        collective_title = Text("群体智慧", font_size=NORMAL_SIZE, color=EMERGE_PURPLE)
        collective_title.move_to([3.5, 2, 0])
        
        # 群体的协调运动
        def create_collective():
            t = t_tracker.get_value()
            group = VGroup()
            
            # 创造一个动态图案
            for i in range(50):
                angle = i * 2 * PI / 50
                r = 1 + 0.3 * np.sin(5 * angle + t * 2)
                
                x = 3.5 + r * np.cos(angle + t)
                y = r * np.sin(angle + t) * 0.7
                
                dot = Dot(
                    point=[x, y, 0],
                    radius=0.03,
                    color=interpolate_color(SWARM_BLUE, EMERGE_PURPLE, i/50),
                    fill_opacity=0.8
                )
                group.add(dot)
                
                # 添加连线
                if i % 5 == 0 and i > 0:
                    prev_angle = (i-5) * 2 * PI / 50
                    prev_r = 1 + 0.3 * np.sin(5 * prev_angle + t * 2)
                    prev_x = 3.5 + prev_r * np.cos(prev_angle + t)
                    prev_y = prev_r * np.sin(prev_angle + t) * 0.7
                    
                    line = Line(
                        [x, y, 0],
                        [prev_x, prev_y, 0],
                        stroke_width=0.5,
                        color=EMERGE_PURPLE,
                        stroke_opacity=0.3
                    )
                    group.add(line)
            
            return group
        
        collective = always_redraw(create_collective)
        
        # 中间分隔线
        divider = DashedLine(
            [0, 2.5, 0],
            [0, -2.5, 0],
            color=BIO_WHITE,
            stroke_opacity=0.3
        )
        
        # 特性对比
        individual_traits = VGroup(
            Text("• 有限感知", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("• 简单行为", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("• 局部信息", font_size=SMALL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        individual_traits.move_to([-3.5, -1.5, 0])
        
        collective_traits = VGroup(
            Text("• 全局模式", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("• 自组织", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("• 适应性强", font_size=SMALL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        collective_traits.move_to([3.5, -1.5, 0])
        
        # 展示所有元素
        self.play(
            Write(individual_title),
            Write(collective_title),
            Create(divider)
        )
        self.add(individual, collective)
        self.play(
            Write(individual_traits),
            Write(collective_traits)
        )
        
        # 动画
        self.play(
            t_tracker.animate.set_value(2 * PI),
            run_time=8,
            rate_func=linear
        )
        
        # 总结
        conclusion = Text(
            "整体 > 部分之和",
            font_size=SUBTITLE_SIZE,
            color=SWARM_GOLD,
            weight=BOLD
        )
        conclusion.to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(individual_title),
            FadeOut(collective_title),
            FadeOut(individual),
            FadeOut(collective),
            FadeOut(divider),
            FadeOut(individual_traits),
            FadeOut(collective_traits),
            FadeOut(conclusion)
        )
    
    def show_ending(self):
        """结尾与下期预告"""
        self.clear()
        
        # 本集回顾
        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=EMERGE_PURPLE)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))
        
        recap = VGroup(
            Text("✓ Boids算法的数学原理", font_size=NORMAL_SIZE),
            Text("✓ 鱼群的流体智慧", font_size=NORMAL_SIZE),
            Text("✓ 蚁群的信息网络", font_size=NORMAL_SIZE),
            Text("✓ 涌现：生命的集体智慧", font_size=NORMAL_SIZE, color=SWARM_GOLD, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        recap.move_to([0, 0.5, 0])
        
        for line in recap:
            self.play(Write(line), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(recap_title), FadeOut(recap))
        
        # 哲学思考
        philosophy = VGroup(
            Text("智慧不在个体", font_size=38, color=SWARM_BLUE),
            Text("而在连接之中", font_size=38, color=EMERGE_PURPLE),
            Text("这就是涌现的魔力", font_size=SUBTITLE_SIZE, color=SWARM_GOLD)
        ).arrange(DOWN, buff=0.6)
        
        for line in philosophy:
            self.play(Write(line), run_time=1)
        
        self.wait(2)
        self.play(FadeOut(philosophy))
        
        # 下期预告
        self.show_next_episode_preview()
    
    def show_next_episode_preview(self):
        """下期预告"""
        preview_title = Text("下期预告", font_size=38, color=BIO_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))
        
        ep4_title = Text(
            "第4集：心脏的混沌节律",
            font_size=TITLE_SIZE,
            color=BIO_RED,
            weight=BOLD
        )
        ep4_title.move_to([0, 1.5, 0])
        
        preview_content = VGroup(
            Text("心跳的非线性动力学", font_size=SUBTITLE_SIZE, color=BIO_RED),
            Text("从规律到混沌的相变", font_size=SUBTITLE_SIZE, color=BIO_PURPLE),
            Text("生命节律的数学密码", font_size=SUBTITLE_SIZE, color=BIO_CYAN)
        ).arrange(DOWN, buff=0.5)
        preview_content.move_to([0, -0.5, 0])
        
        self.play(Write(ep4_title))
        for line in preview_content:
            self.play(Write(line), run_time=0.8)
        
        # 思考题
        think_question = Text(
            "思考：为什么心律失常可以用混沌理论解释？",
            font_size=20,
            color=BIO_YELLOW
        )
        think_question.to_edge(DOWN, buff=0.5)
        self.play(Write(think_question))
        
        self.wait(3)
        
        # 结束语
        see_you = Text(
            "下期再见！",
            font_size=38,
            color=BIO_WHITE
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title),
            FadeOut(ep4_title),
            FadeOut(preview_content),
            FadeOut(think_question),
            Write(see_you)
        )
        
        # 最后的群体动画
        final_swarm = self.create_swarm_background()
        final_swarm.scale(0.5).set_opacity(0.3)
        self.play(Create(final_swarm), run_time=2)
        
        self.wait(2)
        self.play(FadeOut(see_you), FadeOut(final_swarm))


def rotate_vector(vec, angle):
    """旋转2D向量"""
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    return np.array([
        vec[0] * cos_a - vec[1] * sin_a,
        vec[0] * sin_a + vec[1] * cos_a,
        vec[2]
    ])