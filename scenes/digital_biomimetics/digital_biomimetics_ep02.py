"""
数字仿生系列 第2集：龙的飞行曲线
Digital Biomimetics EP02: Dragon Flight Curves

东方龙的S形波动与空气动力学
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple

# 数字仿生系列颜色主题 - 保持与EP01一致
BIO_CYAN = ManimColor("#00FFE5")      # 生命青
BIO_PURPLE = ManimColor("#8B5CF6")    # 神经紫
BIO_GREEN = ManimColor("#00FF88")     # 细胞绿
BIO_BLUE = ManimColor("#007EFF")      # 深海蓝
BIO_YELLOW = ManimColor("#FFE500")    # 能量黄
BIO_RED = ManimColor("#FF0066")       # 血液红
BIO_WHITE = ManimColor("#FFFFFF")     # 纯白
BIO_GRAY = ManimColor("#303030")      # 深灰背景

# 龙的特殊颜色
DRAGON_GOLD = ManimColor("#FFD700")   # 龙鳞金
DRAGON_JADE = ManimColor("#00CED1")   # 青玉色
DRAGON_PEARL = ManimColor("#FFF8DC")  # 龙珠白
CLOUD_WHITE = ManimColor("#F0F8FF")   # 云雾白

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class DigitalBiomimeticsEP02(Scene):
    """数字仿生系列 第2集"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置背景色
        self.camera.background_color = "#090909"
        
        # 1. 系列开场（与EP01保持一致的风格）
        self.show_series_intro()
        
        # 2. 回应EP01的预告问题
        self.answer_preview_question()
        
        # 3. 东方龙的数学模型
        self.dragon_mathematics()
        
        # 4. 第一个展示：龙身的S形波动
        self.dragon_body_wave()
        
        # 5. 第二个展示：龙的粒子化飞行
        self.dragon_particle_flight()
        
        # 6. 空气动力学原理
        self.aerodynamics_principle()
        
        # 7. 龙与云的互动
        self.dragon_cloud_interaction()
        
        # 8. 结尾与预告
        self.show_ending()
    
    def show_series_intro(self):
        """系列开场动画 - 与EP01风格一致"""
        # 龙纹背景
        dragon_pattern = self.create_dragon_pattern()
        dragon_pattern.set_opacity(0.2)
        self.play(Create(dragon_pattern), run_time=2)
        
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
        
        # 第2集标题
        episode_text = Text(
            "第2集：龙的飞行曲线",
            font_size=34,
            color=DRAGON_GOLD
        )
        episode_text.move_to([0, -1.5, 0])
        
        # 动画序列
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.wait(0.5)
        self.play(Write(episode_text), run_time=1.5)
        
        # 脉动效果
        self.play(
            series_title.animate.scale(1.1).set_color(DRAGON_JADE),
            rate_func=there_and_back,
            run_time=1
        )
        
        self.wait(2)
        self.play(
            FadeOut(series_title),
            FadeOut(subtitle),
            FadeOut(episode_text),
            FadeOut(dragon_pattern)
        )
    
    def create_dragon_pattern(self):
        """创建龙纹装饰"""
        pattern = VGroup()
        
        # 创建云纹螺旋
        for i in range(5):
            spiral = ParametricFunction(
                lambda t: np.array([
                    (2 + 0.5*t) * np.cos(t + i*PI/2.5),
                    (2 + 0.5*t) * np.sin(t + i*PI/2.5),
                    0
                ]),
                t_range=[0, 4*PI],
                color=DRAGON_GOLD,
                stroke_width=1
            )
            spiral.scale(0.3)
            spiral.shift([
                3 * np.cos(i * 2*PI/5),
                3 * np.sin(i * 2*PI/5),
                0
            ])
            pattern.add(spiral)
        
        return pattern
    
    def answer_preview_question(self):
        """回应EP01的预告问题：龙真的能飞吗？"""
        title = Text(
            "龙真的能飞吗？",
            font_size=TITLE_SIZE,
            color=DRAGON_GOLD
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 问题展开
        questions = VGroup(
            Text("如果能飞", font_size=NORMAL_SIZE, color=BIO_CYAN),
            Text("需要什么样的", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("数学模型？", font_size=NORMAL_SIZE, color=BIO_YELLOW, weight=BOLD)
        ).arrange(RIGHT, buff=0.3)
        questions.move_to([0, 1, 0])
        
        for q in questions:
            self.play(Write(q), run_time=0.5)
        
        # 答案预览
        answer = Text(
            "让我们用数学，重新定义龙的飞行",
            font_size=SUBTITLE_SIZE,
            color=DRAGON_JADE
        )
        answer.move_to([0, -1, 0])
        self.play(Write(answer))
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(questions),
            FadeOut(answer)
        )
    
    def dragon_mathematics(self):
        """东方龙的数学模型"""
        title = Text("龙的数学密码", font_size=TITLE_SIZE, color=DRAGON_GOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 核心方程组
        equations = VGroup(
            Text("龙身曲线：", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(
                r"S(s,t) = A_1\sin(k_1 s - \omega_1 t) + A_2\sin(k_2 s - \omega_2 t)",
                font_size=28,
                color=DRAGON_JADE
            ),
            Text("升力方程：", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(
                r"L = \frac{1}{2}\rho v^2 S C_L \sin(\alpha)",
                font_size=28,
                color=BIO_CYAN
            ),
            Text("推进力：", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(
                r"F = \int_0^L f(s) \cdot \sin(\phi(s,t)) \, ds",
                font_size=28,
                color=BIO_YELLOW
            )
        ).arrange(DOWN, buff=0.4)
        equations.move_to([0, -0.5, 0])
        
        for i in range(0, len(equations), 2):
            self.play(
                Write(equations[i]),
                Write(equations[i+1]) if i+1 < len(equations) else Wait(0),
                run_time=1.5
            )
        
        # 关键insight
        insight = Text(
            "S形波动 + 空气动力 = 飞行奇迹",
            font_size=SUBTITLE_SIZE,
            color=DRAGON_GOLD,
            weight=BOLD
        )
        insight.to_edge(DOWN, buff=0.8)
        self.play(Write(insight))
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(equations),
            FadeOut(insight)
        )
    
    def dragon_body_wave(self):
        """龙身的S形波动 - 核心展示"""
        self.clear()
        
        title = Text("生命形态 I：龙身波动", font_size=SUBTITLE_SIZE, color=DRAGON_GOLD)
        title.to_edge(UP, buff=0.5)
        
        # 波动方程
        formula = MathTex(
            r"y(s,t) = A \sin(2\pi(s/\lambda - ft)) \cdot e^{-s/L}",
            font_size=20,
            color=DRAGON_JADE
        )
        formula.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(formula))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建龙身的基础曲线
        def create_dragon_curve():
            t = t_tracker.get_value()
            
            # 参数设置
            num_segments = 50
            length = 12
            
            points = []
            for i in range(num_segments):
                s = i * length / num_segments - 6
                
                # S形波动方程
                A1, A2 = 0.8, 0.4
                k1, k2 = 0.5, 1.2
                omega1, omega2 = 1.2, 2.4
                
                x = s
                y = A1 * np.sin(k1 * s - omega1 * t) + \
                    A2 * np.sin(k2 * s - omega2 * t)
                
                # 头部和尾部的缩放
                scale = np.exp(-abs(s) / 8)
                y *= scale
                
                points.append([x, y, 0])
            
            # 创建平滑曲线
            curve = VMobject()
            curve.set_points_smoothly(points)
            curve.set_stroke(
                color=DRAGON_GOLD,
                width=8,
                opacity=0.9
            )
            
            # 添加渐变效果
            curve.set_sheen_direction(RIGHT)
            curve.set_sheen(0.5)
            
            return curve
        
        # 创建龙身
        dragon_body = always_redraw(create_dragon_curve)
        
        # 创建龙鳞粒子系统
        def create_scales():
            t = t_tracker.get_value()
            scales = VGroup()
            
            num_scales = 200
            for i in range(num_scales):
                s = (i / num_scales) * 12 - 6
                
                # 使用相同的波动方程
                A1, A2 = 0.8, 0.4
                k1, k2 = 0.5, 1.2
                omega1, omega2 = 1.2, 2.4
                
                x = s
                y = A1 * np.sin(k1 * s - omega1 * t) + \
                    A2 * np.sin(k2 * s - omega2 * t)
                
                scale = np.exp(-abs(s) / 8)
                y *= scale
                
                # 添加垂直偏移制造厚度
                offset = 0.2 * np.sin(i * 0.5 + t * 2)
                
                # 鳞片大小变化
                radius = 0.02 + 0.01 * np.sin(i * 0.3 + t)
                
                # 颜色渐变
                color = interpolate_color(
                    DRAGON_GOLD,
                    DRAGON_JADE,
                    (i / num_scales)
                )
                
                scale_dot = Dot(
                    point=[x, y + offset, 0],
                    radius=radius,
                    color=color,
                    fill_opacity=0.8
                )
                scales.add(scale_dot)
            
            return scales
        
        # 创建鳞片系统
        scales = always_redraw(create_scales)
        
        # 说明文字
        description = Text(
            "东方龙的S形波动，源自流体力学的智慧",
            font_size=SMALL_SIZE,
            color=BIO_WHITE
        )
        description.to_edge(DOWN, buff=0.5)
        
        self.add(dragon_body, scales)
        self.play(Write(description))
        
        # 龙身游动动画
        self.play(
            t_tracker.animate.set_value(4 * PI),
            run_time=15,
            rate_func=linear
        )
        
        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(description),
            FadeOut(dragon_body),
            FadeOut(scales)
        )
    
    def dragon_particle_flight(self):
        """龙的粒子化飞行 - 基于yuruyurau美学"""
        self.clear()
        
        title = Text("生命形态 II：粒子化飞龙", font_size=SUBTITLE_SIZE, color=DRAGON_JADE)
        title.to_edge(UP, buff=0.5)
        
        # 核心公式
        formula = MathTex(
            r"p_i = \text{body}(s_i, t) + \text{cloud}(\theta_i, r_i) + \text{chaos}(\xi_i)",
            font_size=25,
            color=BIO_CYAN
        )
        formula.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(formula))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        def create_particle_dragon():
            t = t_tracker.get_value()
            particles = VGroup()
            
            # 龙身主体粒子
            num_body_particles = 800
            for i in range(num_body_particles):
                # 沿龙身分布
                s = (i / num_body_particles) * 10 - 5
                
                # 主波动
                k = 3 * np.cos(s / 2 + t)
                e = s / 3 - 2
                d = np.sqrt(k**2 + e**2) + np.sin(s * 2 + t) / 2
                
                # yuruyurau风格的变换
                q = 5 * np.sin(k * 1.5) + np.sin(s / 7) * k * (4 + np.cos(d - t))
                c = d - t / 2
                
                x = q * np.cos(c) / 5
                y = q * np.sin(c) / 5 + np.sin(s + t) * 0.5
                
                # 添加云雾效果的粒子
                noise_x = 0.1 * np.sin(i * 0.1 + t * 3)
                noise_y = 0.1 * np.cos(i * 0.15 + t * 2)
                
                # 深度和颜色
                depth = (d + 5) / 10
                depth = np.clip(depth, 0, 1)
                
                # 龙的颜色：金色到青玉色渐变
                if i < num_body_particles / 3:
                    color = interpolate_color(DRAGON_GOLD, BIO_YELLOW, depth)
                elif i < 2 * num_body_particles / 3:
                    color = interpolate_color(DRAGON_JADE, BIO_CYAN, depth)
                else:
                    color = interpolate_color(BIO_BLUE, DRAGON_JADE, depth)
                
                particle = Dot(
                    point=[x + noise_x, y + noise_y, 0],
                    radius=0.01,
                    color=color,
                    fill_opacity=0.6 + 0.3 * np.sin(t + i/50)
                )
                particles.add(particle)
            
            # 云雾粒子
            num_cloud_particles = 400
            for i in range(num_cloud_particles):
                theta = i * 2 * PI / num_cloud_particles
                r = 2 + 0.5 * np.sin(theta * 3 + t)
                
                # 螺旋云雾
                x = r * np.cos(theta + t / 2) + 0.3 * np.sin(t * 2 + i)
                y = r * np.sin(theta + t / 2) + 0.2 * np.cos(t * 3 + i)
                
                # 云雾的透明度变化
                opacity = 0.2 + 0.1 * np.sin(t + i / 30)
                
                cloud_particle = Dot(
                    point=[x, y * 0.5, 0],
                    radius=0.015,
                    color=CLOUD_WHITE,
                    fill_opacity=opacity
                )
                particles.add(cloud_particle)
            
            return particles
        
        # 创建粒子龙
        particle_dragon = always_redraw(create_particle_dragon)
        
        # 说明文字
        description = Text(
            "数千粒子的协同舞蹈，展现龙的灵动之美",
            font_size=SMALL_SIZE,
            color=BIO_WHITE
        )
        description.to_edge(DOWN, buff=0.5)
        
        self.add(particle_dragon)
        self.play(Write(description))
        
        # 飞行动画
        self.play(
            t_tracker.animate.set_value(3 * PI),
            run_time=18,
            rate_func=linear
        )
        
        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(description),
            FadeOut(particle_dragon)
        )
    
    def aerodynamics_principle(self):
        """空气动力学原理可视化"""
        self.clear()
        
        title = Text("空气动力学揭秘", font_size=TITLE_SIZE, color=BIO_CYAN)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建龙身截面和气流
        dragon_section = Ellipse(
            width=3,
            height=1,
            color=DRAGON_GOLD,
            fill_opacity=0.5
        )
        dragon_section.rotate(PI/6)
        
        # 气流线
        flow_lines = VGroup()
        for i in range(10):
            y_pos = -2 + i * 0.4
            flow_line = ParametricFunction(
                lambda t: np.array([
                    t - 4,
                    y_pos + 0.3 * np.sin(2 * t) * np.exp(-abs(t)/3),
                    0
                ]),
                t_range=[-3, 3],
                color=BIO_BLUE,
                stroke_width=2
            )
            flow_lines.add(flow_line)
        
        # 力的箭头
        lift_arrow = Arrow(
            start=ORIGIN,
            end=UP * 2,
            color=BIO_GREEN,
            stroke_width=6
        )
        lift_label = Text("升力", font_size=SMALL_SIZE, color=BIO_GREEN)
        lift_label.next_to(lift_arrow, RIGHT)
        
        drag_arrow = Arrow(
            start=ORIGIN,
            end=LEFT * 1.5,
            color=BIO_RED,
            stroke_width=4
        )
        drag_label = Text("阻力", font_size=SMALL_SIZE, color=BIO_RED)
        drag_label.next_to(drag_arrow, DOWN)
        
        # 组装
        aero_group = VGroup(
            dragon_section,
            flow_lines,
            lift_arrow,
            lift_label,
            drag_arrow,
            drag_label
        )
        aero_group.move_to(ORIGIN)
        
        self.play(
            Create(dragon_section),
            Create(flow_lines),
            run_time=2
        )
        self.play(
            GrowArrow(lift_arrow),
            Write(lift_label),
            GrowArrow(drag_arrow),
            Write(drag_label)
        )
        
        # 关键公式
        key_formula = VGroup(
            MathTex(r"\frac{L}{D} > 10", font_size=30, color=BIO_YELLOW),
            MathTex(r"\Rightarrow", font_size=30, color=BIO_YELLOW),
            Text("可以飞行", font_size=24, color=BIO_YELLOW)
        ).arrange(RIGHT, buff=0.3)
        key_formula.to_edge(DOWN, buff=0.8)
        self.play(Write(key_formula))
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, aero_group, key_formula)))
    
    def dragon_cloud_interaction(self):
        """龙与云的互动 - 诗意展示"""
        self.clear()
        
        title = Text("龙腾云起", font_size=TITLE_SIZE, color=DRAGON_GOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        def create_dragon_and_clouds():
            t = t_tracker.get_value()
            scene = VGroup()
            
            # 简化的龙形
            dragon_points = []
            for i in range(30):
                s = i / 5 - 3
                x = s
                y = 0.5 * np.sin(s - t) + 0.3 * np.sin(2*s - 2*t)
                dragon_points.append([x, y, 0])
            
            dragon = VMobject()
            dragon.set_points_smoothly(dragon_points)
            dragon.set_stroke(DRAGON_GOLD, width=6)
            scene.add(dragon)
            
            # 动态云朵
            for i in range(5):
                cloud = Circle(
                    radius=0.3 + 0.1 * np.sin(t + i),
                    color=CLOUD_WHITE,
                    fill_opacity=0.3
                )
                cloud.shift([
                    2 * np.cos(i * PI/2.5 + t/3),
                    np.sin(i * PI/2.5 + t/3),
                    0
                ])
                scene.add(cloud)
            
            return scene
        
        dragon_cloud_scene = always_redraw(create_dragon_and_clouds)
        
        # 诗句
        poem = VGroup(
            Text("云从龙", font_size=NORMAL_SIZE, color=DRAGON_JADE),
            Text("风从虎", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("数学让传说成真", font_size=SMALL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.5)
        poem.to_edge(DOWN, buff=0.8)
        
        self.add(dragon_cloud_scene)
        self.play(Write(poem))
        
        # 动画
        self.play(
            t_tracker.animate.set_value(2 * PI),
            run_time=8,
            rate_func=smooth
        )
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(dragon_cloud_scene),
            FadeOut(poem)
        )
    
    def show_ending(self):
        """结尾与下期预告"""
        self.clear()
        
        # 本集回顾
        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=DRAGON_GOLD)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))
        
        recap = VGroup(
            Text("✓ 东方龙的S形波动原理", font_size=NORMAL_SIZE),
            Text("✓ 空气动力学的数学模型", font_size=NORMAL_SIZE),
            Text("✓ 粒子系统的生命美学", font_size=NORMAL_SIZE),
            Text("✓ 龙真的能飞！", font_size=NORMAL_SIZE, color=DRAGON_GOLD, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        recap.move_to([0, 0.5, 0])
        
        for line in recap:
            self.play(Write(line), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(recap_title), FadeOut(recap))
        
        # 哲学思考
        philosophy = VGroup(
            Text("传说不是幻想", font_size=38, color=DRAGON_JADE),
            Text("而是尚未被理解的科学", font_size=38, color=BIO_PURPLE),
            Text("数学，让神话照进现实", font_size=SUBTITLE_SIZE, color=DRAGON_GOLD)
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
        
        ep3_title = Text(
            "第3集：涌现的智慧",
            font_size=TITLE_SIZE,
            color=BIO_PURPLE,
            weight=BOLD
        )
        ep3_title.move_to([0, 1.5, 0])
        
        preview_content = VGroup(
            Text("千条鱼的集体智慧", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("万只蚂蚁的超级大脑", font_size=SUBTITLE_SIZE, color=BIO_GREEN),
            Text("简单规则创造复杂行为", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.5)
        preview_content.move_to([0, -0.5, 0])
        
        self.play(Write(ep3_title))
        for line in preview_content:
            self.play(Write(line), run_time=0.8)
        
        # 思考题
        think_question = Text(
            "思考：个体的简单规则，如何产生群体的复杂智慧？",
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
            FadeOut(ep3_title),
            FadeOut(preview_content),
            FadeOut(think_question),
            Write(see_you)
        )
        
        # 最后的龙纹动画
        dragon_pattern = self.create_dragon_pattern()
        dragon_pattern.scale(0.5).set_opacity(0.3)
        self.play(Create(dragon_pattern), run_time=2)
        
        self.wait(2)
        self.play(FadeOut(see_you), FadeOut(dragon_pattern))