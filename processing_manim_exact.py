"""
Processing代码的Manim精确还原
原始公式：
a=(x,y,d=mag(k=9*cos(x/8),e=y/8-12.5)**2/99+sin(t)/6+.5)=>
point((q=99-e*sin(atan2(k,e)*7)/d+k*(3+cos(d*d-t)*2))*sin(c=d/2+e/69-t/16)+200,
(q+19*d)*cos(c)+200)
"""

from manim import *
import numpy as np

class ProcessingExactReplication(Scene):
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
            self.t += PI / 45  # 对应原始代码的 t+=PI/45
            mob.become(self.create_dot_pattern(self.t))
        
        # 添加更新器
        dots_group.add_updater(update_dots)
        
        # 运行动画
        self.wait(15)
        
    def create_dot_pattern(self, t):
        """创建点云图案 - 精确还原Processing公式"""
        dots = VGroup()
        
        # 对应原始代码的 i=1e4（10000个点）
        num_points = 10000
        
        for i in range(num_points):
            # 对应原始代码：a(i%200, i/55)
            # 注意：Processing的循环是从9999递减到0
            idx = num_points - 1 - i
            x = idx % 200
            y = idx / 55
            
            # 计算中间变量
            # k = 9*cos(x/8)
            k = 9 * np.cos(x / 8)
            
            # e = y/8 - 12.5
            e = y / 8 - 12.5
            
            # d = mag(k,e)**2/99 + sin(t)/6 + 0.5
            # mag(k,e) 是 sqrt(k^2 + e^2)
            mag_ke = np.sqrt(k**2 + e**2)
            d = mag_ke**2 / 99 + np.sin(t) / 6 + 0.5
            
            # 避免除零错误
            if d == 0:
                d = 0.001
            
            # q = 99 - e*sin(atan2(k,e)*7)/d + k*(3+cos(d*d-t)*2)
            q = 99 - e * np.sin(np.arctan2(e, k) * 7) / d + k * (3 + np.cos(d*d - t) * 2)
            
            # c = d/2 + e/69 - t/16
            c = d / 2 + e / 69 - t / 16
            
            # 原始坐标（Processing坐标系）：
            # x_pos = q*sin(c) + 200
            # y_pos = (q + 19*d)*cos(c) + 200
            x_pos = q * np.sin(c) + 200
            y_pos = (q + 19 * d) * np.cos(c) + 200
            
            # 将Processing坐标转换为Manim坐标
            # Processing: 画布是400x400，(0,0)在左上角，y向下
            # Manim: (0,0)在中心，y向上
            manim_x = (x_pos - 200) / 50  # 归一化并居中
            manim_y = -(y_pos - 200) / 50  # 翻转y轴并归一化
            
            # 创建点，限制在屏幕范围内
            if -8 < manim_x < 8 and -4.5 < manim_y < 4.5:
                dot = Dot(
                    point=[manim_x, manim_y, 0],
                    radius=0.006,
                    color=WHITE,
                    fill_opacity=0.4  # 对应stroke(w, 66)的透明度 (66/255 ≈ 0.26)
                )
                dots.add(dot)
        
        return dots


class ProcessingOptimized(Scene):
    """性能优化版本 - 减少点数但保持视觉效果"""
    
    def construct(self):
        self.camera.background_color = "#090909"
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建动态点云
        def create_dots():
            t = t_tracker.get_value()
            dots = VGroup()
            
            # 使用较少的点以提高性能
            num_points = 2000
            
            for i in range(num_points):
                # 映射到原始范围
                idx = (num_points - 1 - i) * 5  # 相当于原始的10000个点
                x = idx % 200
                y = idx / 55
                
                # 计算中间变量
                k = 9 * np.cos(x / 8)
                e = y / 8 - 12.5
                
                # 计算magnitude
                mag_ke = np.sqrt(k**2 + e**2)
                d = mag_ke**2 / 99 + np.sin(t) / 6 + 0.5
                
                if d == 0:
                    d = 0.001
                
                # 计算q值
                q = 99 - e * np.sin(np.arctan2(e, k) * 7) / d + k * (3 + np.cos(d*d - t) * 2)
                
                # 计算c值
                c = d / 2 + e / 69 - t / 16
                
                # 计算坐标
                x_pos = q * np.sin(c) + 200
                y_pos = (q + 19 * d) * np.cos(c) + 200
                
                # 转换为Manim坐标
                manim_x = (x_pos - 200) / 50
                manim_y = -(y_pos - 200) / 50
                
                if -8 < manim_x < 8 and -4.5 < manim_y < 4.5:
                    dot = Dot(
                        point=[manim_x, manim_y, 0],
                        radius=0.008,
                        color=WHITE,
                        fill_opacity=0.35
                    )
                    dots.add(dot)
            
            return dots
        
        # 创建初始点云
        dots_group = always_redraw(create_dots)
        self.add(dots_group)
        
        # 动画：改变时间参数
        self.play(
            t_tracker.animate.set_value(4 * PI),
            run_time=12,
            rate_func=linear
        )


class ProcessingWithColors(Scene):
    """带颜色变化的增强版本"""
    
    def construct(self):
        self.camera.background_color = "#090909"
        
        # 添加标题和公式
        title = Text(
            "Processing数学可视化",
            font="Microsoft YaHei",
            font_size=32
        ).to_edge(UP)
        title.set_color_by_gradient(BLUE_B, TEAL_C)
        
        # 显示核心公式的一部分
        formula = MathTex(
            r"q = 99 - \frac{e \sin(7\arctan(e/k))}{d} + k(3 + 2\cos(d^2 - t))",
            font_size=20
        ).next_to(title, DOWN)
        formula.set_color(BLUE_C)
        
        self.add(title, formula)
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建动态点云
        def create_colored_dots():
            t = t_tracker.get_value()
            dots = VGroup()
            
            num_points = 3000
            
            for i in range(num_points):
                idx = (num_points - 1 - i) * 3.3
                x = idx % 200
                y = idx / 55
                
                k = 9 * np.cos(x / 8)
                e = y / 8 - 12.5
                
                mag_ke = np.sqrt(k**2 + e**2)
                d = mag_ke**2 / 99 + np.sin(t) / 6 + 0.5
                
                if d == 0:
                    d = 0.001
                
                q = 99 - e * np.sin(np.arctan2(e, k) * 7) / d + k * (3 + np.cos(d*d - t) * 2)
                c = d / 2 + e / 69 - t / 16
                
                x_pos = q * np.sin(c) + 200
                y_pos = (q + 19 * d) * np.cos(c) + 200
                
                manim_x = (x_pos - 200) / 50
                manim_y = -(y_pos - 200) / 50
                
                if -8 < manim_x < 8 and -4.5 < manim_y < 4.5:
                    # 根据d值添加颜色变化
                    color_value = (d - 0.5) / 5  # 归一化
                    color_value = np.clip(color_value, 0, 1)
                    
                    # 创建渐变色
                    color = interpolate_color(BLUE_E, TEAL_A, color_value)
                    
                    dot = Dot(
                        point=[manim_x, manim_y, 0],
                        radius=0.008,
                        color=color,
                        fill_opacity=0.5
                    )
                    dots.add(dot)
            
            return dots
        
        dots_group = always_redraw(create_colored_dots)
        self.add(dots_group)
        
        # 添加时间显示
        time_text = always_redraw(
            lambda: Text(
                f"t = {t_tracker.get_value():.2f}",
                font_size=24,
                color=BLUE_B
            ).to_corner(UR)
        )
        self.add(time_text)
        
        # 运行动画
        self.play(
            t_tracker.animate.set_value(6 * PI),
            run_time=15,
            rate_func=linear
        )


class ProcessingWithTrails(Scene):
    """带轨迹效果的版本"""
    
    def construct(self):
        self.camera.background_color = "#090909"
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建多层点云以产生轨迹效果
        layers = []
        opacities = [0.5, 0.3, 0.15, 0.08]  # 逐渐降低的透明度
        time_offsets = [0, 0.1, 0.2, 0.3]  # 时间偏移
        
        for layer_idx, (opacity, time_offset) in enumerate(zip(opacities, time_offsets)):
            def create_layer_dots(idx=layer_idx, op=opacity, t_off=time_offset):
                t = t_tracker.get_value() - t_off
                dots = VGroup()
                
                # 每层使用不同数量的点
                num_points = 800 * (4 - idx)
                
                for i in range(0, num_points, 2):
                    idx_val = (num_points - 1 - i) * 12 / (4 - idx)
                    x = idx_val % 200
                    y = idx_val / 55
                    
                    k = 9 * np.cos(x / 8)
                    e = y / 8 - 12.5
                    
                    mag_ke = np.sqrt(k**2 + e**2)
                    d = mag_ke**2 / 99 + np.sin(t) / 6 + 0.5
                    
                    if d == 0:
                        d = 0.001
                    
                    q = 99 - e * np.sin(np.arctan2(e, k) * 7) / d + k * (3 + np.cos(d*d - t) * 2)
                    c = d / 2 + e / 69 - t / 16
                    
                    x_pos = q * np.sin(c) + 200
                    y_pos = (q + 19 * d) * np.cos(c) + 200
                    
                    manim_x = (x_pos - 200) / 50
                    manim_y = -(y_pos - 200) / 50
                    
                    if -8 < manim_x < 8 and -4.5 < manim_y < 4.5:
                        dot = Dot(
                            point=[manim_x, manim_y, 0],
                            radius=0.007,
                            color=WHITE,
                            fill_opacity=op
                        )
                        dots.add(dot)
                
                return dots
            
            layer = always_redraw(create_layer_dots)
            layers.append(layer)
            self.add(layer)
        
        # 运行动画
        self.play(
            t_tracker.animate.set_value(8 * PI),
            run_time=20,
            rate_func=linear
        )