"""
Processing代码的Manim重现
原始效果：动态数学点云可视化
"""

from manim import *
import numpy as np

class ProcessingVisualization(Scene):
    def construct(self):
        # 设置背景为深色（对应background(9)）
        self.camera.background_color = "#090909"
        
        # 初始化时间变量
        self.t = 0
        
        # 创建点云容器
        dots_group = VGroup()
        
        # 创建初始点云
        dots = self.create_dot_pattern(self.t)
        dots_group.add(dots)
        self.add(dots_group)
        
        # 创建更新函数
        def update_dots(mob, dt):
            self.t += PI / 120  # 对应原始代码的 t+=PI/120
            mob.become(self.create_dot_pattern(self.t))
        
        # 添加更新器
        dots_group.add_updater(update_dots)
        
        # 运行动画
        self.wait(10)
        
    def create_dot_pattern(self, t):
        """创建点云图案"""
        dots = VGroup()
        
        # 对应原始代码的 i=1e4（10000个点）
        num_points = 10000
        
        for i in range(0, num_points, 10):  # 每10个点取1个以优化性能
            # 对应原始代码：a(i, i/235)
            x = i
            y = i / 235
            
            # 计算中间变量
            # k = (4 + cos(x/9 - t)) * cos(x/30)
            k = (4 + np.cos(x/9 - t)) * np.cos(x/30)
            
            # e = y/7 - 13
            e = y/7 - 13
            
            # d = mag(k, e) + sin(y/99 + t/2) - 4
            # mag是Processing中的magnitude函数，相当于sqrt(k^2 + e^2)
            d = np.sqrt(k**2 + e**2) + np.sin(y/99 + t/2) - 4
            
            # c = d - t
            c = d - t
            
            # 计算最终坐标
            # q = 3*sin(k*2) + sin(y/29)*k*(9 + 2*sin(cos(e)*9 - d*4 + t))
            q = 3*np.sin(k*2) + np.sin(y/29)*k*(9 + 2*np.sin(np.cos(e)*9 - d*4 + t))
            
            # 原始坐标：
            # x_pos = q + 40*cos(c) + 200
            # y_pos = q*sin(c) + d*35
            x_pos = q + 40*np.cos(c) + 200
            y_pos = q*np.sin(c) + d*35
            
            # 将Processing坐标转换为Manim坐标
            # Processing: (0,0)在左上角，y向下
            # Manim: (0,0)在中心，y向上
            manim_x = (x_pos - 200) / 50  # 归一化并居中
            manim_y = -(y_pos - 200) / 50  # 翻转y轴并归一化
            
            # 创建点
            if -8 < manim_x < 8 and -4 < manim_y < 4:  # 限制在屏幕范围内
                dot = Dot(
                    point=[manim_x, manim_y, 0],
                    radius=0.008,
                    color=WHITE,
                    fill_opacity=0.6  # 对应stroke(w, 96)的透明度
                )
                dots.add(dot)
        
        return dots


class ProcessingVisualizationEnhanced(Scene):
    """增强版本：添加了颜色变化和轨迹效果"""
    
    def construct(self):
        self.camera.background_color = "#090909"
        
        # 添加标题
        title = Text(
            "数学动态可视化",
            font="Microsoft YaHei",
            font_size=36
        ).to_edge(UP)
        title.set_color_by_gradient(BLUE_B, TEAL_C)
        
        # 显示核心公式
        formula = MathTex(
            r"d = \sqrt{k^2 + e^2} + \sin\left(\frac{y}{99} + \frac{t}{2}\right) - 4",
            font_size=24
        ).next_to(title, DOWN)
        formula.set_color(BLUE_C)
        
        self.add(title, formula)
        
        # 时间参数
        t_tracker = ValueTracker(0)
        
        # 创建动态点云
        def create_dots():
            t = t_tracker.get_value()
            dots = VGroup()
            
            # 使用更少的点以提高性能
            num_points = 2000
            
            for i in range(num_points):
                # 映射到原始范围
                orig_i = i * 5  # 相当于原始的10000个点
                x = orig_i
                y = orig_i / 235
                
                # 计算中间变量
                k = (4 + np.cos(x/9 - t)) * np.cos(x/30)
                e = y/7 - 13
                d = np.sqrt(k**2 + e**2) + np.sin(y/99 + t/2) - 4
                c = d - t
                
                # 计算q值
                q = 3*np.sin(k*2) + np.sin(y/29)*k*(9 + 2*np.sin(np.cos(e)*9 - d*4 + t))
                
                # 计算坐标
                x_pos = q + 40*np.cos(c) + 200
                y_pos = q*np.sin(c) + d*35
                
                # 转换为Manim坐标
                manim_x = (x_pos - 200) / 50
                manim_y = -(y_pos - 200) / 50
                
                if -8 < manim_x < 8 and -4 < manim_y < 4:
                    # 根据位置添加颜色变化
                    color_value = (d + 10) / 20  # 归一化到0-1
                    color_value = np.clip(color_value, 0, 1)
                    
                    # 创建渐变色
                    color = interpolate_color(BLUE_E, TEAL_A, color_value)
                    
                    dot = Dot(
                        point=[manim_x, manim_y, 0],
                        radius=0.01,
                        color=color,
                        fill_opacity=0.7
                    )
                    dots.add(dot)
            
            return dots
        
        # 创建初始点云
        dots_group = always_redraw(create_dots)
        self.add(dots_group)
        
        # 动画：改变时间参数
        self.play(
            t_tracker.animate.set_value(4 * PI),
            run_time=15,
            rate_func=linear
        )


class ProcessingVisualizationWithTrails(Scene):
    """带轨迹效果的版本"""
    
    def construct(self):
        self.camera.background_color = "#090909"
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建多层点云以产生轨迹效果
        layers = []
        opacities = [0.8, 0.5, 0.3, 0.15, 0.05]  # 逐渐降低的透明度
        
        for layer_idx, opacity in enumerate(opacities):
            def create_layer_dots(idx=layer_idx, op=opacity):
                # 使用稍微偏移的时间值创建轨迹效果
                t = t_tracker.get_value() - idx * 0.1
                dots = VGroup()
                
                # 每层使用不同数量的点
                num_points = 500 * (5 - idx)
                
                for i in range(0, num_points, 2):
                    orig_i = i * 20 / (5 - idx)
                    x = orig_i
                    y = orig_i / 235
                    
                    k = (4 + np.cos(x/9 - t)) * np.cos(x/30)
                    e = y/7 - 13
                    d = np.sqrt(k**2 + e**2) + np.sin(y/99 + t/2) - 4
                    c = d - t
                    
                    q = 3*np.sin(k*2) + np.sin(y/29)*k*(9 + 2*np.sin(np.cos(e)*9 - d*4 + t))
                    
                    x_pos = q + 40*np.cos(c) + 200
                    y_pos = q*np.sin(c) + d*35
                    
                    manim_x = (x_pos - 200) / 50
                    manim_y = -(y_pos - 200) / 50
                    
                    if -8 < manim_x < 8 and -4 < manim_y < 4:
                        dot = Dot(
                            point=[manim_x, manim_y, 0],
                            radius=0.008,
                            color=WHITE,
                            fill_opacity=op
                        )
                        dots.add(dot)
                
                return dots
            
            layer = always_redraw(create_layer_dots)
            layers.append(layer)
            self.add(layer)
        
        # 添加参数显示
        param_text = always_redraw(
            lambda: Text(
                f"t = {t_tracker.get_value():.2f}",
                font_size=24,
                color=BLUE_B
            ).to_corner(UR)
        )
        self.add(param_text)
        
        # 运行动画
        self.play(
            t_tracker.animate.set_value(6 * PI),
            run_time=20,
            rate_func=linear
        )


class ProcessingVisualizationInteractive(Scene):
    """交互式版本：展示参数变化的影响"""
    
    def construct(self):
        self.camera.background_color = "#090909"
        
        # 创建参数滑块
        amplitude_tracker = ValueTracker(4)  # 对应原始代码中的4
        frequency_tracker = ValueTracker(9)  # 对应原始代码中的x/9
        
        # 参数显示
        param_group = VGroup(
            Text("振幅 A:", font="Microsoft YaHei", font_size=20),
            DecimalNumber(
                amplitude_tracker.get_value(),
                num_decimal_places=1,
                font_size=20
            ),
            Text("频率 ω:", font="Microsoft YaHei", font_size=20),
            DecimalNumber(
                frequency_tracker.get_value(),
                num_decimal_places=1,
                font_size=20
            )
        ).arrange(RIGHT, buff=0.3)
        param_group.to_edge(UP).set_color(BLUE_B)
        
        # 更新数值显示
        param_group[1].add_updater(
            lambda m: m.set_value(amplitude_tracker.get_value())
        )
        param_group[3].add_updater(
            lambda m: m.set_value(frequency_tracker.get_value())
        )
        
        self.add(param_group)
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建动态点云
        def create_parameterized_dots():
            t = t_tracker.get_value()
            A = amplitude_tracker.get_value()
            omega = frequency_tracker.get_value()
            
            dots = VGroup()
            num_points = 1500
            
            for i in range(num_points):
                orig_i = i * 6
                x = orig_i
                y = orig_i / 235
                
                # 使用可调参数
                k = (A + np.cos(x/omega - t)) * np.cos(x/30)
                e = y/7 - 13
                d = np.sqrt(k**2 + e**2) + np.sin(y/99 + t/2) - 4
                c = d - t
                
                q = 3*np.sin(k*2) + np.sin(y/29)*k*(9 + 2*np.sin(np.cos(e)*9 - d*4 + t))
                
                x_pos = q + 40*np.cos(c) + 200
                y_pos = q*np.sin(c) + d*35
                
                manim_x = (x_pos - 200) / 50
                manim_y = -(y_pos - 200) / 50
                
                if -8 < manim_x < 8 and -4 < manim_y < 4:
                    # 颜色基于参数值
                    color = interpolate_color(
                        BLUE_E,
                        TEAL_A,
                        (A - 2) / 6  # 假设A在2-8范围内
                    )
                    
                    dot = Dot(
                        point=[manim_x, manim_y, 0],
                        radius=0.01,
                        color=color,
                        fill_opacity=0.6
                    )
                    dots.add(dot)
            
            return dots
        
        dots_group = always_redraw(create_parameterized_dots)
        self.add(dots_group)
        
        # 动画序列：展示参数变化的影响
        self.play(t_tracker.animate.set_value(PI), run_time=3)
        self.play(amplitude_tracker.animate.set_value(6), run_time=2)
        self.play(t_tracker.animate.set_value(2*PI), run_time=3)
        self.play(frequency_tracker.animate.set_value(15), run_time=2)
        self.play(t_tracker.animate.set_value(4*PI), run_time=5)
        
        # 同时改变多个参数
        self.play(
            amplitude_tracker.animate.set_value(3),
            frequency_tracker.animate.set_value(7),
            t_tracker.animate.set_value(6*PI),
            run_time=5
        )