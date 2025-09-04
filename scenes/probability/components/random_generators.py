"""
随机数生成器组件
提供各种概率分布的随机数生成和可视化
"""

import numpy as np
import random
from typing import List, Tuple, Callable
from manim import *


class RandomGenerators:
    """随机数生成器集合"""
    
    @staticmethod
    def uniform(low: float = 0, high: float = 1, size: int = 1) -> np.ndarray:
        """均匀分布"""
        return np.random.uniform(low, high, size)
    
    @staticmethod
    def normal(mean: float = 0, std: float = 1, size: int = 1) -> np.ndarray:
        """正态分布"""
        return np.random.normal(mean, std, size)
    
    @staticmethod
    def binomial(n: int, p: float, size: int = 1) -> np.ndarray:
        """二项分布"""
        return np.random.binomial(n, p, size)
    
    @staticmethod
    def poisson(lam: float, size: int = 1) -> np.ndarray:
        """泊松分布"""
        return np.random.poisson(lam, size)
    
    @staticmethod
    def exponential(scale: float = 1, size: int = 1) -> np.ndarray:
        """指数分布"""
        return np.random.exponential(scale, size)
    
    @staticmethod
    def generate_random_walk(steps: int, 
                           dim: int = 1,
                           step_size: float = 1) -> np.ndarray:
        """生成随机游走路径"""
        if dim == 1:
            steps_array = np.random.choice([-1, 1], size=steps) * step_size
            path = np.cumsum(steps_array)
            return np.column_stack([np.arange(steps), path])
        elif dim == 2:
            angles = np.random.uniform(0, 2*np.pi, steps)
            dx = step_size * np.cos(angles)
            dy = step_size * np.sin(angles)
            x = np.cumsum(dx)
            y = np.cumsum(dy)
            return np.column_stack([x, y])
        else:
            raise ValueError("Only 1D and 2D random walks are supported")
    
    @staticmethod
    def generate_markov_chain(transition_matrix: np.ndarray,
                            initial_state: int,
                            steps: int) -> List[int]:
        """生成马尔可夫链"""
        states = [initial_state]
        current_state = initial_state
        
        for _ in range(steps - 1):
            probs = transition_matrix[current_state]
            next_state = np.random.choice(len(probs), p=probs)
            states.append(next_state)
            current_state = next_state
        
        return states
    
    @staticmethod
    def generate_brownian_motion(n_points: int,
                               dt: float = 0.01,
                               sigma: float = 1) -> np.ndarray:
        """生成布朗运动轨迹"""
        dW = np.random.normal(0, np.sqrt(dt), n_points) * sigma
        W = np.cumsum(dW)
        t = np.arange(n_points) * dt
        return np.column_stack([t, W])


class RandomVisualizer:
    """随机过程可视化器"""
    
    @staticmethod
    def create_random_dots(n: int,
                          distribution: str = "uniform",
                          bounds: Tuple[float, float, float, float] = (-3, 3, -2, 2),
                          **kwargs) -> VGroup:
        """创建随机分布的点"""
        dots = VGroup()
        x_min, x_max, y_min, y_max = bounds
        
        if distribution == "uniform":
            x_coords = np.random.uniform(x_min, x_max, n)
            y_coords = np.random.uniform(y_min, y_max, n)
        elif distribution == "normal":
            mean_x = kwargs.get('mean_x', (x_min + x_max) / 2)
            mean_y = kwargs.get('mean_y', (y_min + y_max) / 2)
            std_x = kwargs.get('std_x', (x_max - x_min) / 6)
            std_y = kwargs.get('std_y', (y_max - y_min) / 6)
            x_coords = np.random.normal(mean_x, std_x, n)
            y_coords = np.random.normal(mean_y, std_y, n)
        else:
            raise ValueError(f"Unknown distribution: {distribution}")
        
        for x, y in zip(x_coords, y_coords):
            if x_min <= x <= x_max and y_min <= y <= y_max:
                dot = Dot(
                    point=[x, y, 0],
                    radius=kwargs.get('radius', 0.05),
                    color=kwargs.get('color', BLUE),
                    fill_opacity=kwargs.get('opacity', 0.8)
                )
                dots.add(dot)
        
        return dots
    
    @staticmethod
    def create_galton_board(rows: int = 10,
                           ball_radius: float = 0.05) -> VGroup:
        """创建高尔顿板（豆机）"""
        board = VGroup()
        
        # 创建钉子
        pegs = VGroup()
        peg_spacing = 0.5
        
        for row in range(rows):
            for col in range(row + 1):
                x = (col - row/2) * peg_spacing
                y = -row * peg_spacing * 0.866  # sqrt(3)/2
                peg = Dot(
                    point=[x, y, 0],
                    radius=0.08,
                    color=GRAY,
                    fill_opacity=1
                )
                pegs.add(peg)
        
        board.add(pegs)
        
        # 创建收集槽
        bins = VGroup()
        bin_width = peg_spacing * 0.8
        bin_height = 1
        
        for i in range(rows + 1):
            x = (i - rows/2) * peg_spacing
            y = -(rows + 1) * peg_spacing * 0.866
            bin_rect = Rectangle(
                width=bin_width,
                height=bin_height,
                stroke_color=WHITE,
                fill_opacity=0
            )
            bin_rect.move_to([x, y - bin_height/2, 0])
            bins.add(bin_rect)
        
        board.add(bins)
        
        return board
    
    @staticmethod
    def animate_galton_ball(scene: Scene,
                           board: VGroup,
                           start_pos: np.ndarray,
                           rows: int = 10) -> np.ndarray:
        """动画展示高尔顿板中球的运动"""
        ball = Dot(
            start_pos,
            radius=0.05,
            color=YELLOW,
            fill_opacity=1
        )
        
        scene.add(ball)
        current_pos = start_pos
        peg_spacing = 0.5
        
        # 球下落通过钉子
        for row in range(rows):
            # 随机选择左或右
            direction = random.choice([-1, 1])
            
            # 计算下一个位置
            next_x = current_pos[0] + direction * peg_spacing / 2
            next_y = current_pos[1] - peg_spacing * 0.866
            next_pos = np.array([next_x, next_y, 0])
            
            # 动画
            scene.play(
                ball.animate.move_to(next_pos),
                run_time=0.2,
                rate_func=linear
            )
            
            current_pos = next_pos
        
        # 落入收集槽
        final_y = -(rows + 1) * peg_spacing * 0.866 - 0.3
        final_pos = np.array([current_pos[0], final_y, 0])
        scene.play(
            ball.animate.move_to(final_pos),
            run_time=0.2,
            rate_func=linear
        )
        
        return final_pos