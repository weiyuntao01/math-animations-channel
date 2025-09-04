"""
统计显示组件
提供实时统计数据的可视化显示
"""

from manim import *
import numpy as np
from typing import List, Dict, Optional


class StatisticsDisplay:
    """统计数据显示器"""
    
    @staticmethod
    def create_counter_display(title: str = "Statistics",
                             position: np.ndarray = UP * 3,
                             font_size: int = 24) -> Dict:
        """创建计数器显示"""
        display = VGroup()
        
        # 标题
        title_text = Text(title, font_size=font_size + 4, weight=BOLD)
        title_text.move_to(position)
        display.add(title_text)
        
        # 数据行
        data_text = Text("Trials: 0 | Success: 0 | Rate: 0.000", 
                        font_size=font_size)
        data_text.next_to(title_text, DOWN, buff=0.3)
        display.add(data_text)
        
        return {
            'display': display,
            'title': title_text,
            'data': data_text
        }
    
    @staticmethod
    def update_counter(display_dict: Dict,
                      trials: int,
                      success: int,
                      scene: Scene,
                      animation_time: float = 0.1) -> None:
        """更新计数器显示"""
        rate = success / trials if trials > 0 else 0
        new_text = Text(
            f"Trials: {trials} | Success: {success} | Rate: {rate:.3f}",
            font_size=display_dict['data'].font_size
        )
        new_text.move_to(display_dict['data'].get_center())
        
        scene.play(
            Transform(display_dict['data'], new_text),
            run_time=animation_time
        )
    
    @staticmethod
    def create_statistics_panel(stats: Dict[str, float],
                              position: np.ndarray = RIGHT * 4,
                              width: float = 3,
                              height: float = 4) -> VGroup:
        """创建统计面板"""
        panel = VGroup()
        
        # 背景
        bg = Rectangle(
            width=width,
            height=height,
            fill_color=DARK_GRAY,
            fill_opacity=0.8,
            stroke_color=WHITE
        )
        bg.move_to(position)
        panel.add(bg)
        
        # 标题
        title = Text("Statistics", font_size=24, weight=BOLD)
        title.move_to(bg.get_top() + DOWN * 0.5)
        panel.add(title)
        
        # 统计数据
        y_offset = 1
        for key, value in stats.items():
            stat_text = Text(
                f"{key}: {value:.3f}",
                font_size=18
            )
            stat_text.move_to(
                bg.get_center() + UP * y_offset
            )
            panel.add(stat_text)
            y_offset -= 0.5
        
        return panel
    
    @staticmethod
    def create_live_histogram(data: List[float],
                            bins: int = 20,
                            width: float = 6,
                            height: float = 3,
                            position: np.ndarray = ORIGIN) -> VGroup:
        """创建实时更新的直方图"""
        histogram = VGroup()
        
        # 计算直方图数据
        if len(data) > 0:
            hist, bin_edges = np.histogram(data, bins=bins)
            max_count = max(hist) if max(hist) > 0 else 1
            
            # 创建条形
            bar_width = width / bins
            for i, count in enumerate(hist):
                if count > 0:
                    bar_height = (count / max_count) * height
                    bar = Rectangle(
                        width=bar_width * 0.9,
                        height=bar_height,
                        fill_color=BLUE,
                        fill_opacity=0.8,
                        stroke_width=1
                    )
                    bar.move_to(
                        position + 
                        LEFT * width/2 + 
                        RIGHT * (i + 0.5) * bar_width + 
                        UP * (bar_height/2 - height/2)
                    )
                    histogram.add(bar)
        
        # 坐标轴
        x_axis = Line(
            position + LEFT * width/2 + DOWN * height/2,
            position + RIGHT * width/2 + DOWN * height/2,
            color=WHITE
        )
        y_axis = Line(
            position + LEFT * width/2 + DOWN * height/2,
            position + LEFT * width/2 + UP * height/2,
            color=WHITE
        )
        
        histogram.add(x_axis, y_axis)
        
        return histogram
    
    @staticmethod
    def create_confidence_interval(mean: float,
                                 std_error: float,
                                 confidence: float = 0.95,
                                 width: float = 4,
                                 position: np.ndarray = ORIGIN) -> VGroup:
        """创建置信区间可视化"""
        ci_group = VGroup()
        
        # 计算置信区间
        z_score = 1.96 if confidence == 0.95 else 2.58  # 简化处理
        lower = mean - z_score * std_error
        upper = mean + z_score * std_error
        
        # 中心线（均值）
        mean_line = Line(
            position + UP * 0.3,
            position + DOWN * 0.3,
            color=GREEN,
            stroke_width=4
        )
        ci_group.add(mean_line)
        
        # 置信区间
        ci_line = Line(
            position + LEFT * width/2,
            position + RIGHT * width/2,
            color=YELLOW,
            stroke_width=2
        )
        ci_group.add(ci_line)
        
        # 端点标记
        left_cap = Line(
            position + LEFT * width/2 + UP * 0.2,
            position + LEFT * width/2 + DOWN * 0.2,
            color=YELLOW,
            stroke_width=2
        )
        right_cap = Line(
            position + RIGHT * width/2 + UP * 0.2,
            position + RIGHT * width/2 + DOWN * 0.2,
            color=YELLOW,
            stroke_width=2
        )
        ci_group.add(left_cap, right_cap)
        
        # 标签
        ci_label = Text(
            f"{confidence*100}% CI: [{lower:.3f}, {upper:.3f}]",
            font_size=16
        )
        ci_label.next_to(ci_line, DOWN, buff=0.3)
        ci_group.add(ci_label)
        
        return ci_group
    
    @staticmethod
    def create_probability_meter(probability: float,
                               radius: float = 1.5,
                               position: np.ndarray = ORIGIN) -> VGroup:
        """创建概率仪表盘"""
        meter = VGroup()
        
        # 外圈
        outer_circle = Circle(
            radius=radius,
            color=WHITE,
            stroke_width=3
        )
        outer_circle.move_to(position)
        meter.add(outer_circle)
        
        # 刻度
        for i in range(11):
            angle = PI - i * PI / 10
            start = position + radius * 0.9 * np.array([
                np.cos(angle), np.sin(angle), 0
            ])
            end = position + radius * np.array([
                np.cos(angle), np.sin(angle), 0
            ])
            tick = Line(start, end, color=WHITE, stroke_width=2)
            meter.add(tick)
            
            # 刻度标签
            if i % 2 == 0:
                label = Text(f"{i/10:.1f}", font_size=14)
                label.move_to(
                    position + radius * 1.2 * np.array([
                        np.cos(angle), np.sin(angle), 0
                    ])
                )
                meter.add(label)
        
        # 指针
        pointer_angle = PI - probability * PI
        pointer = Arrow(
            start=position,
            end=position + radius * 0.8 * np.array([
                np.cos(pointer_angle), np.sin(pointer_angle), 0
            ]),
            color=RED,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        meter.add(pointer)
        
        # 中心点
        center_dot = Dot(position, radius=0.1, color=RED)
        meter.add(center_dot)
        
        # 概率值显示
        prob_text = Text(f"{probability:.2f}", font_size=24, weight=BOLD)
        prob_text.next_to(outer_circle, DOWN, buff=0.3)
        meter.add(prob_text)
        
        return meter
    
    @staticmethod
    def create_comparison_bars(data: Dict[str, float],
                             colors: Optional[List[str]] = None,
                             width: float = 6,
                             height: float = 4,
                             position: np.ndarray = ORIGIN) -> VGroup:
        """创建比较条形图"""
        if colors is None:
            colors = [BLUE, RED, GREEN, YELLOW, PURPLE]
        
        bars = VGroup()
        n_bars = len(data)
        bar_width = width / (n_bars * 1.5)
        max_value = max(data.values()) if data else 1
        
        for i, (label, value) in enumerate(data.items()):
            # 条形
            bar_height = (value / max_value) * height
            bar = Rectangle(
                width=bar_width,
                height=bar_height,
                fill_color=colors[i % len(colors)],
                fill_opacity=0.8,
                stroke_width=2
            )
            bar.move_to(
                position + 
                LEFT * width/2 + 
                RIGHT * (i + 0.5) * bar_width * 1.5 +
                UP * (bar_height/2 - height/2)
            )
            bars.add(bar)
            
            # 标签
            label_text = Text(label, font_size=16)
            label_text.next_to(bar, DOWN, buff=0.1)
            bars.add(label_text)
            
            # 数值
            value_text = Text(f"{value:.2f}", font_size=14)
            value_text.next_to(bar, UP, buff=0.1)
            bars.add(value_text)
        
        # 坐标轴
        x_axis = Line(
            position + LEFT * width/2 + DOWN * height/2,
            position + RIGHT * width/2 + DOWN * height/2,
            color=WHITE
        )
        bars.add(x_axis)
        
        return bars