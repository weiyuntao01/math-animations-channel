from manim import *
import numpy as np

# --- 配色方案 ---
LA_TEAL = "#2DD4BF"      # 特征向量 v1 (青色)
LA_PINK = "#F472B6"      # 特征向量 v2 (粉色)
LA_YELLOW = "#FACC15"    # 特征值 / 强调
LA_PURPLE = "#A855F7"    # 矩阵 / 标题
LA_RED = "#F87171"       # 警告 / 错误 / 变化
LA_GRAY = "#475569"      # 普通向量 / 背景
BG_COLOR = "#0F172A"     # 深蓝黑底色

class LinearAlgebraEP02(Scene):
    """线性代数 EP02：特征值与特征向量 (最终防重叠版)"""
    
    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场
        self.intro_series()
        
        # 2. 视觉实验
        self.visual_experiment()
        
        # 3. 概念定义 (重点修复此处)
        self.define_eigen_concept()
        
        # 4. 计算原理
        self.explain_characteristic_eq()
        
        # 5. 结尾
        self.show_ending()

    def intro_series(self):
        CENTER_Y = UP * 1.5
        
        series_title = Text("线性代数：AI的几何学", font_size=32, color=LA_GRAY).move_to(CENTER_Y)
        ep_title = Text("EP02: 特征值与特征向量", font_size=48, color=LA_TEAL, weight=BOLD).next_to(series_title, DOWN, buff=0.3)
        subtitle = Text("Eigenvalues & Eigenvectors", font_size=24, color=LA_TEAL).next_to(ep_title, DOWN, buff=0.1)
        
        self.play(Write(series_title), FadeIn(ep_title), Write(subtitle))
        self.wait(1)
        
        metaphor = Text("寻找旋转世界中的\"定海神针\"", font_size=32, color=LA_YELLOW).next_to(subtitle, DOWN, buff=1.0)
        self.play(Write(metaphor))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def visual_experiment(self):
        """视觉实验：普通向量 vs 特征向量"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        grid = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": LA_GRAY, "stroke_opacity": 0.3},
            axis_config={"color": WHITE}
        ).move_to(LEFT_ZONE)
        
        self.play(Create(grid))
        
        matrix = np.array([[3, 1], [0, 2]])
        
        title = Text("线性变换实验", font_size=32, color=LA_PURPLE, weight=BOLD)
        matrix_tex = MathTex(
            r"M = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}", 
            font_size=40
        )
        
        right_group = VGroup(title, matrix_tex).arrange(DOWN, buff=0.5).move_to(RIGHT_ZONE + UP*2)
        self.play(Write(right_group))
        
        # --- 实验 A ---
        vec_a_start = np.array([1, 1, 0])
        vec_a_end = np.dot(matrix, vec_a_start[:2])
        vec_a_end = np.array([vec_a_end[0], vec_a_end[1], 0])
        
        arrow_a = Arrow(grid.c2p(0,0), grid.c2p(*vec_a_start[:2]), color=LA_GRAY, buff=0, stroke_width=4)
        label_a = Text("普通向量", font_size=20, color=LA_GRAY).next_to(arrow_a, UP, buff=0.1)
        
        self.play(GrowArrow(arrow_a), Write(label_a))
        
        arrow_a_new = Arrow(grid.c2p(0,0), grid.c2p(*vec_a_end[:2]), color=WHITE, buff=0, stroke_width=4)
        
        exp_text_1 = Text("方向改变了！", font_size=24, color=LA_RED).next_to(matrix_tex, DOWN, buff=1.0)
        exp_text_1.set_x(RIGHT_ZONE[0])
        
        self.play(
            TransformFromCopy(arrow_a, arrow_a_new),
            Write(exp_text_1)
        )
        self.wait(1)
        self.play(FadeOut(arrow_a), FadeOut(label_a), FadeOut(arrow_a_new), FadeOut(exp_text_1))
        
        # --- 实验 B ---
        vec_v1_start = np.array([1, 0, 0])
        vec_v1_end = np.array([3, 0, 0])
        
        arrow_v1 = Arrow(grid.c2p(0,0), grid.c2p(*vec_v1_start[:2]), color=LA_TEAL, buff=0, stroke_width=6)
        label_v1 = MathTex(r"\vec{v}_1", color=LA_TEAL).next_to(arrow_v1, DOWN, buff=0.1)
        
        self.play(GrowArrow(arrow_v1), Write(label_v1))
        
        arrow_v1_new = Arrow(grid.c2p(0,0), grid.c2p(*vec_v1_end[:2]), color=LA_TEAL, buff=0, stroke_width=6)
        
        exp_text_2 = VGroup(
            Text("方向没变！", font_size=24, color=LA_TEAL),
            Text("只是拉长了 3 倍", font_size=24, color=LA_YELLOW)
        ).arrange(DOWN).next_to(matrix_tex, DOWN, buff=1.0)
        exp_text_2.set_x(RIGHT_ZONE[0])
        
        self.play(
            TransformFromCopy(arrow_v1, arrow_v1_new),
            Write(exp_text_2)
        )
        
        span_line = Line(grid.c2p(-5, 0), grid.c2p(5, 0), color=LA_TEAL, stroke_opacity=0.3)
        self.play(Create(span_line), rate_func=there_and_back, run_time=1)
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def define_eigen_concept(self):
            """概念定义页面 (上下分层布局，彻底防重叠)"""
            
            # 1. 标题上移
            title = Text("核心公式", font_size=40, color=LA_PURPLE).to_edge(UP, buff=1.0)
            
            # 2. 公式
            # formula[0]=A, [1]=v, [2]==, [3]=lambda, [4]=v
            formula = MathTex(
                r"A", r"\vec{v}", r"=", r"\lambda", r"\vec{v}",
                font_size=80
            )
            formula[0].set_color(WHITE)
            formula[1].set_color(LA_TEAL)
            formula[3].set_color(LA_YELLOW)
            formula[4].set_color(LA_TEAL)
            
            formula.next_to(title, DOWN, buff=1.5) # 增加间距，给上方标签留位置
            
            # 3. 解释标签 (上下错开)
            ARROW_LEN = 0.6
            
            # --- 下方组 ---
            
            # 1. 矩阵变换 (指向 A, 下方)
            arrow_A = Arrow(start=DOWN*ARROW_LEN, end=ORIGIN, color=GRAY, buff=0).next_to(formula[0], DOWN, buff=0.1)
            desc_A = Text("矩阵变换", font_size=24, color=GRAY).next_to(arrow_A, DOWN, buff=0.1)
            
            # 3. 特征向量 (指向右边的 v, 下方)
            arrow_v = Arrow(start=DOWN*ARROW_LEN, end=ORIGIN, color=LA_TEAL, buff=0).next_to(formula[4], DOWN, buff=0.1)
            desc_v = Text("特征向量", font_size=24, color=LA_TEAL).next_to(arrow_v, DOWN, buff=0.1)
            
            # --- 上方组 ---
            
            # 2. 特征值 (指向 lambda, 上方!)
            # 注意箭头方向是 start(上) -> end(下，指向公式)
            arrow_lambda = Arrow(start=UP*ARROW_LEN, end=ORIGIN, color=LA_YELLOW, buff=0).next_to(formula[3], UP, buff=0.1)
            desc_lambda = Text("特征值 (缩放)", font_size=24, color=LA_YELLOW).next_to(arrow_lambda, UP, buff=0.1)
            
            # 动画
            self.play(Write(title))
            self.play(Write(formula))
            
            self.play(
                GrowArrow(arrow_A), FadeIn(desc_A),
                GrowArrow(arrow_v), FadeIn(desc_v),
                GrowArrow(arrow_lambda), FadeIn(desc_lambda)
            )
            
            self.wait(3)
            self.play(FadeOut(Group(*self.mobjects)))

    def explain_characteristic_eq(self):
        """几何解释特征方程"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        grid = NumberPlane(
            x_range=[-4, 4], y_range=[-4, 4],
            background_line_style={"stroke_opacity": 0.2}
        ).move_to(LEFT_ZONE)
        
        self.play(Create(grid))
        
        title = Text("如何找到它们？", font_size=28, color=LA_PURPLE, weight=BOLD)
        
        eq1 = MathTex(r"A\vec{v} = \lambda I \vec{v}")
        eq2 = MathTex(r"(A - \lambda I)\vec{v} = \vec{0}")
        
        text_desc = Text("要让非零向量 v 变成 0", font_size=24, color=LA_PINK)
        text_desc2 = Text("矩阵必须把空间压缩(降维)", font_size=24, color=LA_PINK)
        
        eq3 = MathTex(r"\det(A - \lambda I) = 0", color=LA_YELLOW, font_size=48)
        
        right_content = VGroup(
            title, eq1, eq2, text_desc, text_desc2, eq3
        ).arrange(DOWN, buff=0.5).move_to(RIGHT_ZONE)
        
        self.play(Write(title))
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(1)
        
        squash_matrix = [[1, 1], [0.5, 0.5]] 
        
        self.play(
            Write(text_desc),
            Write(text_desc2),
            grid.animate.apply_matrix(squash_matrix, about_point=grid.c2p(0,0)),
            run_time=2
        )
        
        self.play(Write(eq3))
        self.play(Indicate(eq3))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_ending(self):
        title = Text("总结", font_size=40, color=LA_PURPLE).to_edge(UP, buff=1.0)
        
        summary = VGroup(
            Text("1. 特征向量：变换后方向不变的向量", font_size=26),
            Text("2. 特征值：该向量被拉伸或缩短的倍数", font_size=26),
            Text("3. 它们是矩阵的\"骨架\"，描述了变换的核心特征", font_size=26, color=LA_TEAL)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), Write(summary))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(summary))
        
        next_ep = Text("下期预告：降维打击 (PCA)", font_size=40, color=LA_YELLOW).move_to(UP * 0.5)
        desc = Text("如何利用特征值，扔掉无用的数据？\n从3D到2D的最优投影。", font_size=24, color=LA_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))