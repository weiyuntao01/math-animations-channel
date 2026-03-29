"""
数字仿生系列 第1集：生命的数学之舞
Digital Biomimetics EP01: Mathematical Dance of Life

通过数学公式创造有机的生命形态
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple

# 数字仿生系列颜色主题 - 使用ManimColor对象
BIO_CYAN = ManimColor("#00FFE5")      # 生命青
BIO_PURPLE = ManimColor("#8B5CF6")    # 神经紫
BIO_GREEN = ManimColor("#00FF88")     # 细胞绿
BIO_BLUE = ManimColor("#007EFF")      # 深海蓝
BIO_YELLOW = ManimColor("#FFE500")    # 能量黄
BIO_RED = ManimColor("#FF0066")       # 血液红
BIO_WHITE = ManimColor("#FFFFFF")     # 纯白
BIO_GRAY = ManimColor("#303030")      # 深灰背景

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class DigitalBiomimeticsEP01(Scene):
    """数字仿生系列 第1集"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置背景色
        self.camera.background_color = "#090909"
        
        # 1. 系列开场
        self.show_series_intro()
        
        # 2. 什么是数字仿生？
        self.what_is_digital_biomimetics()
        
        # 3. 第一个生命形态：水母舞动
        self.jellyfish_dance()
        
        # 4. 第二个生命形态：细胞呼吸
        self.cellular_breathing()
        
        # 5. 数学与生命的联系
        self.math_life_connection()
        
        # 6. 结尾与预告
        self.show_ending()
    
    def show_series_intro(self):
        """系列开场动画"""
        # DNA双螺旋背景
        dna_helix = self.create_dna_helix()
        dna_helix.set_opacity(0.2)
        self.play(Create(dna_helix), run_time=2)
        
        # 系列标题
        series_title = Text(
            "数字仿生",
            font_size=60,
            color=BIO_CYAN,
            weight=BOLD
        )
        series_title.move_to([0, 1, 0])
        
        # 英文副标题
        subtitle = Text(
            "DIGITAL BIOMIMETICS",
            font_size=24,
            color=BIO_WHITE,
            font="Arial"
        )
        subtitle.next_to(series_title, DOWN, buff=0.3)
        
        # 第1集标题
        episode_text = Text(
            "第1集：生命的数学之舞",
            font_size=34,
            color=BIO_GREEN
        )
        episode_text.move_to([0, -1.5, 0])
        
        # 动画序列
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.wait(0.5)
        self.play(Write(episode_text), run_time=1.5)
        
        # 脉动效果
        self.play(
            series_title.animate.scale(1.1).set_color(BIO_PURPLE),
            rate_func=there_and_back,
            run_time=1
        )
        
        self.wait(2)
        self.play(
            FadeOut(series_title),
            FadeOut(subtitle),
            FadeOut(episode_text),
            FadeOut(dna_helix)
        )
    
    def create_dna_helix(self):
        """创建DNA双螺旋"""
        helix = VGroup()
        num_points = 50
        
        for i in range(num_points):
            t = i * 0.2
            # 第一条链
            x1 = 2 * np.cos(t)
            y1 = t - 5
            z1 = 2 * np.sin(t)
            
            # 第二条链
            x2 = 2 * np.cos(t + PI)
            y2 = t - 5
            z2 = 2 * np.sin(t + PI)
            
            # 碱基对连接
            if i % 3 == 0:
                line = Line(
                    [x1, y1, 0],
                    [x2, y2, 0],
                    stroke_width=1,
                    color=BIO_CYAN
                )
                helix.add(line)
            
            # 主链点
            dot1 = Dot([x1, y1, 0], radius=0.05, color=BIO_BLUE)
            dot2 = Dot([x2, y2, 0], radius=0.05, color=BIO_GREEN)
            helix.add(dot1, dot2)
        
        return helix
    
    def what_is_digital_biomimetics(self):
        """介绍数字仿生概念"""
        title = Text("什么是数字仿生？", font_size=TITLE_SIZE, color=BIO_CYAN)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 定义
        definition = VGroup(
            Text("用数学公式", font_size=NORMAL_SIZE, color=BIO_YELLOW),
            Text("+", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("计算机图形", font_size=NORMAL_SIZE, color=BIO_PURPLE),
            Text("=", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("人工生命", font_size=NORMAL_SIZE, color=BIO_GREEN, weight=BOLD)
        ).arrange(RIGHT, buff=0.3)
        definition.move_to([0, 1, 0])
        
        for part in definition:
            self.play(Write(part), run_time=0.5)
        
        # 示例
        examples = VGroup(
            Text("• 水母的优雅游动", font_size=SMALL_SIZE, color=BIO_CYAN),
            Text("• 细胞的有机呼吸", font_size=SMALL_SIZE, color=BIO_GREEN),
            Text("• 神经元的电光传递", font_size=SMALL_SIZE, color=BIO_PURPLE),
            Text("• 鱼群的集体智慧", font_size=SMALL_SIZE, color=BIO_BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.move_to([0, -1.5, 0])
        
        self.play(Write(examples), run_time=2)
        
        # 核心理念
        core_idea = Text(
            "让冰冷的数学公式，绽放出生命的温度",
            font_size=SUBTITLE_SIZE,
            color=BIO_YELLOW
        )
        core_idea.to_edge(DOWN, buff=0.8)
        self.play(Write(core_idea))
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(examples),
            FadeOut(core_idea)
        )
    
    def jellyfish_dance(self):
        """第一个生命形态：水母舞动 - 基于processing_visualization.py"""
        self.clear()
        
        # 标题
        title = Text("生命形态 I：水母之舞", font_size=SUBTITLE_SIZE, color=BIO_CYAN)
        title.to_edge(UP, buff=0.5)
        
        # 显示核心公式
        formula = MathTex(
            r"d = \sqrt{k^2 + e^2} + \sin\left(\frac{y}{99} + \frac{t}{2}\right)",
            font_size=20,
            color=BIO_BLUE
        )
        formula.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(formula))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建水母形态的点云
        def create_jellyfish():
            t = t_tracker.get_value()
            dots = VGroup()
            
            num_points = 1500  # 优化性能
            
            for i in range(num_points):
                orig_i = i * 6
                x = orig_i
                y = orig_i / 235
                
                # 核心数学变换
                k = (4 + np.cos(x/9 - t)) * np.cos(x/30)
                e = y/7 - 13
                d = np.sqrt(k**2 + e**2) + np.sin(y/99 + t/2) - 4
                c = d - t
                
                # 确保np.cos(e)的值在[-1, 1]范围内，虽然它本来就应该在这个范围
                q = 3*np.sin(k*2) + np.sin(y/29)*k*(9 + 2*np.sin(np.cos(e)*9 - d*4 + t))
                
                x_pos = q + 40*np.cos(c) + 200
                y_pos = q*np.sin(c) + d*35
                
                # 转换坐标
                manim_x = (x_pos - 200) / 60
                manim_y = -(y_pos - 200) / 60
                
                if -7 < manim_x < 7 and -3.5 < manim_y < 3.5:
                    # 创建发光效果
                    depth = (d + 10) / 20
                    depth = np.clip(depth, 0, 1)
                    
                    # 水母般的青蓝色调
                    color = interpolate_color(BIO_WHITE, BIO_CYAN, depth* 0.3)
                    
                    dot = Dot(
                        point=[manim_x, manim_y+0.3, 0],  # 移除了-0.5的偏移，让动画居中
                        radius=0.008,
                        color=color,
                        fill_opacity=0.8 + 0.2 * np.sin(t + i/100)  # 脉动效果
                    )
                    dots.add(dot)
            
            return dots
        
        # 创建水母
        jellyfish = always_redraw(create_jellyfish)
        
        # 添加说明文字
        description = Text(
            "数千个数学点，构成了水母优雅的舞姿",
            font_size=SMALL_SIZE,
            color=BIO_WHITE
        )
        description.to_edge(DOWN, buff=0.5)
        
        self.add(jellyfish)
        self.play(Write(description))
        
        # 动画：水母游动
        self.play(
            t_tracker.animate.set_value(3 * PI),
            run_time=20,
            rate_func=linear
        )
        
        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(description),
            FadeOut(jellyfish)
        )
    
    def cellular_breathing(self):
        """第二个生命形态：细胞呼吸 - 使用Processing精确公式"""
        self.clear()
        
        title = Text("生命形态 II：细胞呼吸", font_size=SUBTITLE_SIZE, color=BIO_GREEN)
        title.to_edge(UP, buff=0.5)
        
        # 显示核心公式 - 修正为正确的数学表示
        formula = MathTex(
            r"q = 99 - \frac{e \sin(7\arctan(k, e))}{d} + k(3 + 2\cos(d^2 - t))",
            font_size=30,
            color=BIO_GREEN
        )
        formula.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(formula))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        def create_cells():
            t = t_tracker.get_value()
            dots = VGroup()
            
            # 使用精确的Processing公式
            num_points = 2000
            
            for i in range(num_points):
                # 映射到原始范围
                idx = (num_points - 1 - i) * 5  # 相当于原始的10000个点
                x = idx % 200
                y = idx / 55
                
                # 计算中间变量 - 精确的Processing公式
                k = 9 * np.cos(x / 8)
                e = y / 8 - 12.5
                
                # 优化：直接计算平方和，避免开方再平方
                d = (k**2 + e**2) / 99 + np.sin(t) / 6 + 0.5
                
                # 避免除零
                if d < 0.001:
                    d = 0.001
                
                # 计算q值 - 修正：使用正确的arctan2参数顺序
                # Processing的atan2(k,e)对应numpy的arctan2(k,e)
                q = 99 - e * np.sin(np.arctan2(k, e) * 7) / d + k * (3 + np.cos(d*d - t) * 2)
                
                # 计算c值
                c = d / 2 + e / 69 - t / 16
                
                # 计算坐标
                x_pos = q * np.sin(c) + 200
                y_pos = (q + 19 * d) * np.cos(c) + 200
                
                # 转换为Manim坐标
                manim_x = (x_pos - 200) / 50
                manim_y = -(y_pos - 200) / 50
                
                if -8 < manim_x < 8 and -4 < manim_y < 4:
                    # 根据d值创建细胞般的颜色效果
                    life = (d - 0.5) / 5  # 归一化
                    life = np.clip(life, 0, 1)
                    
                    # 使用生命色彩渐变
                    color = interpolate_color(BIO_GREEN, BIO_YELLOW, life)
                    
                    # 添加脉动效果
                    pulse = 0.4 + 0.3 * np.sin(t + i/200)
                    
                    dot = Dot(
                        point=[manim_x, manim_y+1, 0],  # 移除了-0.5的偏移，让动画居中
                        radius=0.01,
                        color=color,
                        fill_opacity=pulse
                    )
                    dots.add(dot)
            
            return dots
        
        # 创建细胞群
        cells = always_redraw(create_cells)
        
        # 添加说明
        description = Text(
            "每个点都在呼吸，像活着的细胞",
            font_size=SMALL_SIZE,
            color=BIO_WHITE
        )
        description.to_edge(DOWN, buff=0.5)
        
        self.add(cells)
        self.play(Write(description))
        
        # 动画：细胞呼吸 - 使用Processing的时间增量
        self.play(
            t_tracker.animate.set_value(4 * PI),
            run_time=20,
            rate_func=linear
        )
        
        self.wait(1)
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(description),
            FadeOut(cells)
        )
    
    def math_life_connection(self):
        """展示数学与生命的联系"""
        self.clear()
        
        title = Text("数学与生命的奇妙联系", font_size=TITLE_SIZE, color=BIO_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建对比展示
        math_side = VGroup(
            Text("冰冷的公式", font_size=NORMAL_SIZE, color=BIO_BLUE),
            MathTex(r"x = r\cos(\theta)", font_size=20),
            MathTex(r"y = r\sin(\theta)", font_size=20),
            MathTex(r"z = at", font_size=20)
        ).arrange(DOWN, buff=0.3)
        math_side.move_to([-3.5, 0, 0])
        
        arrow = Arrow(
            LEFT * 0.5,
            RIGHT * 0.5,
            color=BIO_YELLOW,
            stroke_width=8
        )
        arrow.move_to(ORIGIN)
        
        life_side = VGroup(
            Text("活着的形态", font_size=NORMAL_SIZE, color=BIO_GREEN),
            Text("• 螺旋生长", font_size=SMALL_SIZE),
            Text("• DNA双链", font_size=SMALL_SIZE),
            Text("• 贝壳纹理", font_size=SMALL_SIZE)
        ).arrange(DOWN, buff=0.3)
        life_side.move_to([3.5, 0, 0])
        
        self.play(Write(math_side))
        self.play(Create(arrow))
        self.play(Write(life_side))
        
        # 核心观点
        key_point = VGroup(
            Text("自然界的美，都可以用数学描述", font_size=NORMAL_SIZE, color=BIO_YELLOW),
            Text("而数学的美，能创造出新的生命形态", font_size=NORMAL_SIZE, color=BIO_CYAN)
        ).arrange(DOWN, buff=0.4)
        key_point.to_edge(DOWN, buff=0.8)
        
        self.play(Write(key_point))
        self.wait(3)
        
        self.play(
            FadeOut(title),
            FadeOut(math_side),
            FadeOut(arrow),
            FadeOut(life_side),
            FadeOut(key_point)
        )
    
    def show_ending(self):
        """结尾与下期预告"""
        self.clear()
        
        # 本集回顾
        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=BIO_CYAN)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))
        
        recap = VGroup(
            Text("✓ 用数学公式创造生命形态", font_size=NORMAL_SIZE),
            Text("✓ 水母之舞：流体与波动", font_size=NORMAL_SIZE),
            Text("✓ 细胞呼吸：有机的脉动", font_size=NORMAL_SIZE),
            Text("✓ 数学是生命的语言", font_size=NORMAL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        recap.move_to([0, 0.5, 0])
        
        for line in recap:
            self.play(Write(line), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(recap_title), FadeOut(recap))
        
        # 哲学思考
        philosophy = VGroup(
            Text("当数学遇见生命", font_size=38, color=BIO_PURPLE),
            Text("代码成为了造物主", font_size=38, color=BIO_GREEN),
            Text("这就是数字仿生的魅力", font_size=SUBTITLE_SIZE, color=BIO_CYAN)
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
        
        ep2_title = Text(
            "第2集：龙的飞行曲线",
            font_size=TITLE_SIZE,
            color=BIO_PURPLE,
            weight=BOLD
        )
        ep2_title.move_to([0, 1.5, 0])
        
        preview_content = VGroup(
            Text("东方龙的S形波动", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("空气动力学的数学原理", font_size=SUBTITLE_SIZE, color=BIO_BLUE),
            Text("从传说到科学的转化", font_size=SUBTITLE_SIZE, color=BIO_GREEN)
        ).arrange(DOWN, buff=0.5)
        preview_content.move_to([0, -0.5, 0])
        
        self.play(Write(ep2_title))
        for line in preview_content:
            self.play(Write(line), run_time=0.8)
        
        # 思考题
        think_question = Text(
            "思考：龙真的能飞吗？如果能，它需要什么样的数学模型？",
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
            FadeOut(ep2_title),
            FadeOut(preview_content),
            FadeOut(think_question),
            Write(see_you)
        )
        
        # 最后的DNA动画
        dna = self.create_dna_helix()
        dna.scale(0.5).set_opacity(0.3)
        self.play(Create(dna), run_time=2)
        
        self.wait(2)
        self.play(FadeOut(see_you), FadeOut(dna))