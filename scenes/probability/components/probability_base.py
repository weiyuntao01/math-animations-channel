"""
概率论系列动画基础类
提供概率动画的通用功能和组件
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple, Optional

# 概率系列颜色主题
PROB_PURPLE = "#8B5CF6"    # 主色：概率紫
PROB_GREEN = "#10B981"     # 成功绿
PROB_RED = "#EF4444"       # 失败红
PROB_BLUE = "#3B82F6"      # 数据蓝
PROB_YELLOW = "#F59E0B"    # 警告黄
PROB_GRAY = "#6B7280"      # 中性灰
PROB_DARK = "#1F2937"      # 深色背景
PROB_LIGHT = "#F3F4F6"     # 浅色背景


class ProbabilityBase(Scene):
    """概率系列的基础场景类"""
    
    def __init__(self):
        super().__init__()
        # 设置默认字体
        Text.set_default(font="Microsoft YaHei")
        
        # 概率系列配色
        self.colors = {
            'primary': PROB_PURPLE,
            'success': PROB_GREEN,
            'failure': PROB_RED,
            'data': PROB_BLUE,
            'warning': PROB_YELLOW,
            'neutral': PROB_GRAY,
            'bg_dark': PROB_DARK,
            'bg_light': PROB_LIGHT
        }
        
        # 动画速度控制
        self.speed_factor = 1.0
    
    def show_series_intro(self, episode_num: int, episode_title: str):
        """显示系列介绍动画"""
        # 系列标题
        series_title = Text(
            "概率论的反直觉世界",
            font_size=48,
            color=self.colors['primary'],
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
        self.play(
            Write(series_title),
            run_time=2 * self.speed_factor
        )
        self.play(
            FadeIn(episode_text, shift=UP),
            run_time=1.5 * self.speed_factor
        )
        
        self.wait(2.5 * self.speed_factor)
        
        self.play(
            FadeOut(series_title),
            FadeOut(episode_text),
            run_time=1 * self.speed_factor
        )
    
    def create_probability_bar(self, 
                             probability: float,
                             width: float = 6,
                             height: float = 0.8,
                             show_percentage: bool = True,
                             label: str = "") -> VGroup:
        """创建概率条形图"""
        # 背景条
        bg_bar = Rectangle(
            width=width,
            height=height,
            fill_color=self.colors['neutral'],
            fill_opacity=0.3,
            stroke_color=self.colors['neutral']
        )
        
        # 概率条
        prob_bar = Rectangle(
            width=width * probability,
            height=height,
            fill_color=self.colors['primary'],
            fill_opacity=0.8,
            stroke_width=0
        )
        prob_bar.align_to(bg_bar, LEFT)
        
        # 百分比文字
        elements = VGroup(bg_bar, prob_bar)
        
        if show_percentage:
            percentage_text = Text(
                f"{probability*100:.1f}%",
                font_size=24,
                color=WHITE
            )
            percentage_text.move_to(bg_bar.get_center())
            elements.add(percentage_text)
        
        # 标签
        if label:
            label_text = Text(label, font_size=20, color=WHITE)
            label_text.next_to(bg_bar, LEFT, buff=0.3)
            elements.add(label_text)
        
        return elements
    
    def animate_coin_flip(self, 
                         position: np.ndarray = ORIGIN,
                         result: Optional[bool] = None) -> Tuple[VGroup, bool]:
        """硬币抛掷动画"""
        if result is None:
            result = random.random() < 0.5
        
        # 创建硬币
        coin = Circle(radius=0.5, fill_opacity=1)
        
        if result:  # 正面
            coin.set_fill(self.colors['success'])
            symbol = Text("H", font_size=36, color=WHITE)
        else:  # 反面
            coin.set_fill(self.colors['failure'])
            symbol = Text("T", font_size=36, color=WHITE)
        
        symbol.move_to(coin.get_center())
        coin_group = VGroup(coin, symbol)
        coin_group.move_to(position)
        
        # 抛掷动画
        self.play(
            coin_group.animate.shift(UP * 2),
            rate_func=there_and_back,
            run_time=1 * self.speed_factor
        )
        
        # 旋转动画
        self.play(
            Rotate(coin_group, angle=PI * 4, run_time=0.5 * self.speed_factor)
        )
        
        return coin_group, result
    
    def create_probability_tree(self, 
                              root_pos: np.ndarray = ORIGIN,
                              branches: List[Dict] = None) -> VGroup:
        """创建概率树"""
        if branches is None:
            branches = [
                {"prob": 0.5, "label": "A", "color": self.colors['success']},
                {"prob": 0.5, "label": "B", "color": self.colors['failure']}
            ]
        
        tree = VGroup()
        
        # 根节点
        root = Dot(root_pos, radius=0.1, color=WHITE)
        tree.add(root)
        
        # 分支
        angle_step = PI / (len(branches) + 1)
        for i, branch in enumerate(branches):
            angle = PI - angle_step * (i + 1)
            end_pos = root_pos + np.array([
                2 * np.cos(angle),
                2 * np.sin(angle),
                0
            ])
            
            # 分支线
            line = Line(
                root_pos, end_pos,
                stroke_color=branch['color'],
                stroke_width=3
            )
            tree.add(line)
            
            # 终点
            end_dot = Dot(end_pos, radius=0.08, color=branch['color'])
            tree.add(end_dot)
            
            # 概率标签
            prob_label = Text(
                f"{branch['prob']:.2f}",
                font_size=20,
                color=branch['color']
            )
            prob_label.next_to(line.get_center(), UP, buff=0.1)
            tree.add(prob_label)
            
            # 事件标签
            event_label = Text(
                branch['label'],
                font_size=24,
                color=WHITE
            )
            event_label.next_to(end_dot, DOWN, buff=0.2)
            tree.add(event_label)
        
        return tree
    
    def simulate_random_experiments(self,
                                  n_trials: int,
                                  success_prob: float,
                                  batch_size: int = 100,
                                  show_animation: bool = True) -> Dict:
        """模拟随机实验并可视化"""
        results = []
        success_count = 0
        
        # 创建显示区域
        counter_text = Text(
            f"实验次数: 0 | 成功: 0 | 概率: 0.000",
            font_size=24,
            color=WHITE
        ).to_edge(UP)
        
        if show_animation:
            self.play(Write(counter_text))
        
        # 分批模拟
        for batch_start in range(0, n_trials, batch_size):
            batch_end = min(batch_start + batch_size, n_trials)
            batch_results = []
            
            for i in range(batch_start, batch_end):
                result = random.random() < success_prob
                results.append(result)
                batch_results.append(result)
                if result:
                    success_count += 1
            
            # 更新显示
            current_prob = success_count / (batch_end) if batch_end > 0 else 0
            new_text = Text(
                f"实验次数: {batch_end} | 成功: {success_count} | 概率: {current_prob:.3f}",
                font_size=24,
                color=WHITE
            ).to_edge(UP)
            
            if show_animation and batch_end <= 1000:  # 只动画显示前1000次
                self.play(
                    Transform(counter_text, new_text),
                    run_time=0.1 * self.speed_factor
                )
            elif batch_end % 1000 == 0:  # 每1000次更新一次
                self.play(
                    Transform(counter_text, new_text),
                    run_time=0.1 * self.speed_factor
                )
        
        if show_animation:
            self.play(FadeOut(counter_text))
        
        return {
            'results': results,
            'success_count': success_count,
            'success_rate': success_count / n_trials,
            'theoretical_prob': success_prob
        }
    
    def create_data_visualization(self,
                                data: List[float],
                                viz_type: str = "histogram",
                                **kwargs) -> VGroup:
        """创建数据可视化"""
        if viz_type == "histogram":
            return self._create_histogram(data, **kwargs)
        elif viz_type == "line":
            return self._create_line_chart(data, **kwargs)
        elif viz_type == "scatter":
            return self._create_scatter_plot(data, **kwargs)
        else:
            raise ValueError(f"Unknown visualization type: {viz_type}")
    
    def _create_histogram(self, 
                         data: List[float],
                         bins: int = 20,
                         width: float = 8,
                         height: float = 4) -> VGroup:
        """创建直方图"""
        # 计算直方图数据
        hist, bin_edges = np.histogram(data, bins=bins)
        max_count = max(hist)
        
        histogram = VGroup()
        bar_width = width / bins
        
        for i, count in enumerate(hist):
            if count > 0:
                bar_height = (count / max_count) * height
                bar = Rectangle(
                    width=bar_width * 0.9,
                    height=bar_height,
                    fill_color=self.colors['data'],
                    fill_opacity=0.8,
                    stroke_width=1
                )
                bar.move_to(
                    LEFT * width/2 + RIGHT * (i + 0.5) * bar_width + UP * bar_height/2
                )
                histogram.add(bar)
        
        # 添加坐标轴
        x_axis = Line(
            LEFT * width/2 + DOWN * 0.1,
            RIGHT * width/2 + DOWN * 0.1,
            color=WHITE
        )
        y_axis = Line(
            LEFT * width/2 + DOWN * 0.1,
            LEFT * width/2 + UP * height,
            color=WHITE
        )
        
        histogram.add(x_axis, y_axis)
        histogram.move_to(ORIGIN)
        
        return histogram
    
    def create_probability_cloud(self,
                               center: np.ndarray = ORIGIN,
                               n_particles: int = 100,
                               radius: float = 2,
                               color_map: Dict[str, float] = None) -> VGroup:
        """创建概率云效果"""
        if color_map is None:
            color_map = {
                self.colors['success']: 0.5,
                self.colors['failure']: 0.5
            }
        
        particles = VGroup()
        
        for _ in range(n_particles):
            # 随机位置（高斯分布）
            r = np.random.normal(0, radius/3)
            theta = random.uniform(0, TAU)
            pos = center + np.array([r * np.cos(theta), r * np.sin(theta), 0])
            
            # 随机颜色（根据概率）
            rand = random.random()
            cumsum = 0
            particle_color = WHITE
            for color, prob in color_map.items():
                cumsum += prob
                if rand < cumsum:
                    particle_color = color
                    break
            
            # 创建粒子
            particle = Dot(
                pos,
                radius=random.uniform(0.02, 0.05),
                color=particle_color,
                fill_opacity=random.uniform(0.3, 0.8)
            )
            particles.add(particle)
        
        return particles
    
    def animate_data_stream(self,
                          data_points: List[float],
                          duration: float = 3,
                          color_func=None) -> None:
        """数据流动画效果"""
        if color_func is None:
            color_func = lambda x: self.colors['success'] if x > 0.5 else self.colors['failure']
        
        stream = VGroup()
        
        for i, value in enumerate(data_points[:100]):  # 限制显示数量
            dot = Dot(
                radius=0.05,
                color=color_func(value),
                fill_opacity=0.8
            )
            
            # 起始位置
            start_pos = LEFT * 7 + UP * random.uniform(-2, 2)
            end_pos = RIGHT * 7 + UP * random.uniform(-2, 2)
            
            dot.move_to(start_pos)
            stream.add(dot)
            
            # 创建路径
            path = ParametricFunction(
                lambda t: start_pos + t * (end_pos - start_pos) + 
                         UP * 0.5 * np.sin(PI * t),
                t_range=[0, 1]
            )
            
            self.play(
                MoveAlongPath(dot, path),
                run_time=duration * self.speed_factor,
                rate_func=linear
            )
    
    def show_series_ending(self,
                          main_message: str = "直觉可能会骗你",
                          sub_message: str = "但数学不会"):
        """显示系列结尾动画"""
        # 主信息
        main_text = Text(
            main_message,
            font_size=48,
            color=self.colors['primary'],
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
        self.play(
            Write(main_text),
            run_time=2 * self.speed_factor
        )
        self.play(
            Write(sub_text),
            run_time=1.5 * self.speed_factor
        )
        
        self.wait(3 * self.speed_factor)
        
        self.play(
            FadeOut(main_text),
            FadeOut(sub_text),
            run_time=1 * self.speed_factor
        )