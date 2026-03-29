from manim import *
import numpy as np
import random

# --- 配色方案 ---
LA_TEAL = "#2DD4BF"      # U / 竖纹
LA_PINK = "#F472B6"      # V / 横纹
LA_YELLOW = "#FACC15"    # Sigma / 能量
LA_PURPLE = "#A855F7"    # 矩阵 A / 合成结果
LA_RED = "#F87171"       # 噪音 / 舍弃
LA_GRAY = "#475569"      # 背景
BG_COLOR = "#0F172A"     # 深蓝黑底色

class LinearAlgebraEP04(Scene):
    """线性代数 EP04：奇异值分解 (SVD) - 易懂优化版"""
    
    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 哲学开场 (修复重叠)
        self.intro_decomposition()
        
        # 2. 几何直观 (保持原好评布局)
        self.geometric_interpretation()
        
        # 3. 核心应用 (重构：更直观的视觉逻辑)
        self.matrix_atoms_demo()
        
        # 4. 升华结尾
        self.show_deep_ending()

    def intro_decomposition(self):
        """开场：从物理原子到数学原子 (布局修复)"""
        
        # 引用
        quote = Text("“我们可以把世界拆解为原子，\n也可以把数据拆解为奇异值。”", font_size=32, color=LA_TEAL)
        quote.move_to(UP * 0.5)
        self.play(Write(quote))
        self.wait(2)
        self.play(FadeOut(quote))
        
        # 标题 (位置上移)
        title = Text("EP04: 奇异值分解 (SVD)", font_size=48, color=LA_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=1.0)
        
        subtitle = Text("The Atoms of Linear Algebra", font_size=28, color=LA_GRAY).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # --- 视觉区域 (整体下移 + 拉开间距) ---
        VISUAL_Y = DOWN * 0.5
        
        # 左侧：复杂物体 (向左移至 4.5)
        complex_shape = Square(side_length=2, color=LA_PURPLE, fill_opacity=0.5).move_to(LEFT * 4.5 + VISUAL_Y)
        label_complex = Text("复杂矩阵", font_size=24).next_to(complex_shape, UP)
        
        # 中间：箭头
        arrow = Arrow(LEFT, RIGHT, color=WHITE).move_to(VISUAL_Y)
        
        # 右侧：积木块 (向右移至 4.5)
        blocks = VGroup(
            Square(side_length=1, color=LA_YELLOW, fill_opacity=0.8),
            Square(side_length=0.8, color=LA_TEAL, fill_opacity=0.8),
            Square(side_length=0.5, color=LA_PINK, fill_opacity=0.8)
        ).arrange(RIGHT, buff=0.2).move_to(RIGHT * 4.5 + VISUAL_Y)
        
        label_simple = Text("简单成分", font_size=24).next_to(blocks, UP)
        
        self.play(
            FadeIn(complex_shape), Write(label_complex),
            GrowArrow(arrow),
            FadeIn(blocks, lag_ratio=0.2), Write(label_simple)
        )
        
        # 底部文字
        text = Text("任何矩阵 = 简单矩阵的叠加", font_size=28, color=LA_YELLOW).to_edge(DOWN, buff=1.0)
        self.play(Write(text))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def geometric_interpretation(self):
        """几何解释：A = U Σ V^T (保留之前的稳定布局)"""
        
        LEFT_ZONE = LEFT * 4.0
        RIGHT_ZONE = RIGHT * 4.0
        
        title = Text("几何本质：三步走", font_size=32, color=LA_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        formula = MathTex(
            r"A", r"=", r"U", r"\Sigma", r"V^T",
            font_size=60
        )
        formula[2].set_color(LA_TEAL)   # U
        formula[3].set_color(LA_YELLOW) # Sigma
        formula[4].set_color(LA_PINK)   # V^T
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))
        
        # 左侧演示
        grid = NumberPlane(
            x_range=[-3, 3], y_range=[-3, 3],
            x_length=5, y_length=5,
            background_line_style={"stroke_opacity": 0.3}
        ).scale(0.8).move_to(LEFT_ZONE + DOWN * 1.0)
        
        circle = Circle(radius=0.8, color=WHITE, stroke_opacity=0.5).move_to(grid.c2p(0,0))
        unit_len = 0.8 
        
        v1 = Arrow(grid.get_center(), grid.get_center() + RIGHT*unit_len, color=LA_PINK, buff=0)
        v2 = Arrow(grid.get_center(), grid.get_center() + UP*unit_len, color=LA_PINK, buff=0)
        
        label_start = Text("原始空间", font_size=20, color=LA_PINK).next_to(grid, UP, buff=0.2)
        
        self.play(
            Create(grid), Create(circle),
            GrowArrow(v1), GrowArrow(v2),
            Write(label_start)
        )
        
        # 右侧文字
        step1_text = Text("1. 旋转 (Rotate)", font_size=24, color=LA_PINK)
        step2_text = Text("2. 拉伸 (Stretch)", font_size=24, color=LA_YELLOW)
        step3_text = Text("3. 再旋转 (Rotate)", font_size=24, color=LA_TEAL)
        
        steps_group = VGroup(step1_text, step2_text, step3_text).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        steps_group.move_to(RIGHT_ZONE + DOWN * 0.5)
        
        # 1. 旋转
        self.play(FadeIn(step1_text, shift=RIGHT))
        self.play(Indicate(formula[4], color=LA_PINK))
        self.play(
            Rotate(v1, angle=PI/4, about_point=grid.get_center()),
            Rotate(v2, angle=PI/4, about_point=grid.get_center()),
            Rotate(circle, angle=PI/4, about_point=grid.get_center()),
            run_time=1.0
        )
        
        # 2. 拉伸
        self.play(FadeIn(step2_text, shift=RIGHT))
        self.play(Indicate(formula[3], color=LA_YELLOW))
        
        v1_stretched = Arrow(grid.get_center(), grid.get_center() + (RIGHT+UP)/np.sqrt(2)*unit_len*2, color=LA_YELLOW, buff=0)
        v2_stretched = Arrow(grid.get_center(), grid.get_center() + (UP-RIGHT)/np.sqrt(2)*unit_len*0.5, color=LA_YELLOW, buff=0)
        ellipse_rot = Ellipse(width=2*unit_len*2, height=2*unit_len*0.5, color=LA_YELLOW).move_to(grid.get_center()).rotate(PI/4)
        
        self.play(
            Transform(circle, ellipse_rot),
            Transform(v1, v1_stretched),
            Transform(v2, v2_stretched),
            run_time=1.0
        )
        
        # 3. 再旋转
        self.play(FadeIn(step3_text, shift=RIGHT))
        self.play(Indicate(formula[2], color=LA_TEAL))
        
        self.play(
            Rotate(circle, angle=PI/6, about_point=grid.get_center()),
            Rotate(v1, angle=PI/6, about_point=grid.get_center()),
            Rotate(v2, angle=PI/6, about_point=grid.get_center()),
            v1.animate.set_color(LA_TEAL),
            v2.animate.set_color(LA_TEAL),
            circle.animate.set_color(LA_TEAL),
            run_time=1.0
        )
        
        self.wait(1)
        self.play(FadeOut(Group(*self.mobjects)))

    def matrix_atoms_demo(self):
        """核心应用：矩阵拆解 (重构版：条纹叠加)"""
        
        # 1. 标题
        title = Text("SVD 的魔法：层层叠加", font_size=36, color=LA_PURPLE).to_edge(UP, buff=0.5)
        
        # 公式
        math_expansion = MathTex(
            r"A \approx \text{Layer}_1 + \text{Layer}_2 + \dots",
            font_size=36
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), Write(math_expansion))
        
        # 布局定义
        LEFT_CENTER = LEFT * 3.5 + DOWN * 0.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 2. 左侧：最终目标 (Target Image)
        # 用一个简单的 4x4 网格图案 (条纹交织)
        target_group = VGroup()
        bg = Square(side_length=3, fill_color=BLACK, stroke_color=WHITE, stroke_width=2)
        
        # 绘制网格线 (这是我们的目标图案)
        grid_lines = VGroup()
        for i in range(5):
            # 竖线
            l = Line(UP*1.5 + LEFT*1.5 + RIGHT*i*0.75, DOWN*1.5 + LEFT*1.5 + RIGHT*i*0.75, color=LA_TEAL, stroke_opacity=0.5)
            # 横线
            h = Line(LEFT*1.5 + UP*1.5 + DOWN*i*0.75, RIGHT*1.5 + UP*1.5 + DOWN*i*0.75, color=LA_PINK, stroke_opacity=0.5)
            grid_lines.add(l, h)
            
        target_image = VGroup(bg, grid_lines).move_to(LEFT_CENTER)
        
        label_target = Text("原始数据 A", font_size=24, color=WHITE).next_to(target_image, UP)
        
        # 初始状态：空框
        canvas_bg = Square(side_length=3, fill_color=BLACK, stroke_color=GRAY, stroke_width=1).move_to(LEFT_CENTER)
        
        self.play(Create(canvas_bg), Write(label_target))
        
        # 3. 右侧：三个层级 (Stripes)
        
        # Layer 1: 竖条纹 (Vertical Structure)
        layer1_viz = VGroup(
            Square(side_length=1.5, stroke_color=GRAY),
            # 竖线示意
            *[Line(UP*0.75 + LEFT*0.75 + RIGHT*i*0.375, DOWN*0.75 + LEFT*0.75 + RIGHT*i*0.375, color=LA_TEAL) for i in range(5)]
        )
        layer1_label = Text("第1层: 竖直骨架", font_size=20, color=LA_TEAL)
        layer1_group = VGroup(layer1_viz, layer1_label).arrange(RIGHT, buff=0.3)
        
        # Layer 2: 横条纹 (Horizontal Structure)
        layer2_viz = VGroup(
            Square(side_length=1.2, stroke_color=GRAY),
            # 横线示意
            *[Line(LEFT*0.6 + UP*0.6 + DOWN*i*0.3, RIGHT*0.6 + UP*0.6 + DOWN*i*0.3, color=LA_PINK) for i in range(5)]
        )
        layer2_label = Text("第2层: 水平细节", font_size=20, color=LA_PINK)
        layer2_group = VGroup(layer2_viz, layer2_label).arrange(RIGHT, buff=0.3)
        
        # Layer 3: 噪点 (Noise)
        layer3_viz = VGroup(
            Square(side_length=0.8, stroke_color=GRAY),
            # 随机点
            *[Dot(np.array([random.uniform(-0.3,0.3), random.uniform(-0.3,0.3), 0]), radius=0.03, color=LA_RED) for _ in range(20)]
        )
        layer3_label = Text("第3层: 无用噪音", font_size=20, color=LA_RED)
        layer3_group = VGroup(layer3_viz, layer3_label).arrange(RIGHT, buff=0.3)
        
        # 统一右侧布局
        layers = VGroup(layer1_group, layer2_group, layer3_group).arrange(DOWN, buff=1.0, aligned_edge=LEFT)
        layers.move_to(RIGHT_ZONE + DOWN * 0.5)
        
        # 4. 动画：叠加 (Synthesis)
        
        # --- 添加第1层 ---
        self.play(FadeIn(layer1_group, shift=LEFT))
        
        # 左侧出现竖线
        canvas_lines_v = VGroup(*[Line(UP*1.5 + LEFT*1.5 + RIGHT*i*0.75, DOWN*1.5 + LEFT*1.5 + RIGHT*i*0.75, color=LA_TEAL) for i in range(5)])
        canvas_lines_v.move_to(LEFT_CENTER)
        
        arrow1 = Arrow(layer1_viz.get_left(), canvas_bg.get_right(), color=LA_TEAL, buff=0.2)
        self.play(GrowArrow(arrow1))
        self.play(Create(canvas_lines_v))
        self.wait(0.5)
        self.play(FadeOut(arrow1))
        
        # --- 添加第2层 ---
        self.play(FadeIn(layer2_group, shift=LEFT))
        
        # 左侧叠加横线 -> 变成网格
        canvas_lines_h = VGroup(*[Line(LEFT*1.5 + UP*1.5 + DOWN*i*0.75, RIGHT*1.5 + UP*1.5 + DOWN*i*0.75, color=LA_PINK) for i in range(5)])
        canvas_lines_h.move_to(LEFT_CENTER)
        
        arrow2 = Arrow(layer2_viz.get_left(), canvas_bg.get_right(), color=LA_PINK, buff=0.2)
        self.play(GrowArrow(arrow2))
        self.play(Create(canvas_lines_h))
        self.wait(0.5)
        self.play(FadeOut(arrow2))
        
        # 此时左侧已经是完美的网格了
        
        # --- 添加第3层 (噪音) ---
        self.play(FadeIn(layer3_group, shift=LEFT))
        
        # 左侧出现噪点
        noise_dots = VGroup(*[Dot(np.array([random.uniform(-1.4,1.4), random.uniform(-1.4,1.4), 0]) + LEFT_CENTER, radius=0.05, color=LA_RED) for _ in range(50)])
        
        arrow3 = Arrow(layer3_viz.get_left(), canvas_bg.get_right(), color=LA_RED, buff=0.2)
        self.play(GrowArrow(arrow3))
        self.play(FadeIn(noise_dots))
        
        # 提示变脏了
        dirty_label = Text("图像变脏了！", font_size=24, color=LA_RED, weight=BOLD).next_to(canvas_bg, DOWN)
        self.play(Write(dirty_label))
        self.wait(1)
        
        # --- 舍弃噪音 ---
        cross = Cross(layer3_group, color=LA_RED)
        self.play(Create(cross))
        
        self.play(
            FadeOut(arrow3), 
            FadeOut(noise_dots), # 移除左侧噪点
            FadeOut(dirty_label),
            Transform(label_target, Text("还原清晰图像", font_size=24, color=LA_TEAL).next_to(canvas_bg, UP))
        )
        
        # 5. 结论
        conclusion = Text("只保留大奇异值 = 信号降噪", font_size=28, color=LA_YELLOW)
        conclusion.move_to(DOWN * 3.5)
        self.play(Write(conclusion))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_deep_ending(self):
        """升华结尾"""
        
        title = Text("SVD 的哲学", font_size=40, color=LA_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("不是所有信息都是平等的", font_size=28),
            Text("有些是信号，有些只是噪音", font_size=28),
            Text("抓住最大的奇异值 (σ)", font_size=32, color=LA_YELLOW, weight=BOLD),
            Text("就抓住了事物的灵魂", font_size=32, color=LA_TEAL, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        next_ep = Text("下期预告：神经网络", font_size=40, color=LA_TEAL).move_to(UP * 0.5)
        desc = Text("当无数个简单矩阵连接在一起...\n线性代数如何涌现出智能？", font_size=24, color=LA_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))