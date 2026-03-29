from manim import *
import numpy as np

# --- 线性代数系列配色 (Cyberpunk Style) ---
LA_TEAL = "#2DD4BF"      # 主向量 / 变换后 i_hat
LA_PINK = "#F472B6"      # 特征向量 / 变换后 j_hat
LA_YELLOW = "#FACC15"    # 强调 / 核心概念 / 面积
LA_PURPLE = "#A855F7"    # 矩阵 / 空间 / 标题
LA_GRAY = "#475569"      # 网格 / 背景线
BG_COLOR = "#0F172A"     # 深蓝黑底色

class LinearAlgebraEP01(Scene):
    """线性代数 EP01：矩阵的本质 (修复版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：新系列启航
        self.intro_series()
        
        # 2. 基础：基向量 i 和 j
        # 返回 grid_group, basis_vectors 用于后续变换
        grid_group, basis_vectors = self.setup_basis_vectors()
        
        # 3. 核心：矩阵变换演示 (修复超出屏幕问题)
        self.apply_matrix_transformation(grid_group, basis_vectors)
        
        # 4. 原理：列向量的秘密 (修复文字重叠)
        self.explain_column_vectors()
        
        # 5. 进阶：行列式的几何意义 (面积)
        self.visualize_determinant()
        
        # 6. 结尾
        self.show_ending()

    def intro_series(self):
        """系列开场"""
        series_title = Text("线性代数：AI的几何学", font_size=54, color=LA_TEAL, weight=BOLD)
        subtitle = Text("EP01: 矩阵的本质", font_size=32, color=LA_PURPLE).next_to(series_title, DOWN, buff=0.5)
        
        self.play(DrawBorderThenFill(series_title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)
        
        question = VGroup(
            Text("矩阵到底是什么？", font_size=28, color=WHITE),
            Text("只是一个数字方块吗？", font_size=28, color=LA_GRAY)
        ).arrange(DOWN, buff=0.3).next_to(subtitle, DOWN, buff=1.0)
        
        self.play(Write(question))
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def setup_basis_vectors(self):
        """建立坐标系和基向量"""
        
        LEFT_ZONE = LEFT * 3.5
        
        # 1. 创建网格 (缩小尺寸以适应后续拉伸)
        # scale=0.65 是关键，防止后续拉伸出屏幕
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=7,
            y_length=6,
            background_line_style={
                "stroke_color": LA_GRAY,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            },
            axis_config={"stroke_color": WHITE, "include_numbers": False}
        ).scale(0.65).move_to(LEFT_ZONE)
        
        # 2. 定义基向量 i_hat (1, 0) 和 j_hat (0, 1)
        # 注意：使用 c2p 确保向量跟随网格的缩放
        origin = grid.c2p(0, 0)
        p_i = grid.c2p(1, 0)
        p_j = grid.c2p(0, 1)
        
        i_hat = Arrow(start=origin, end=p_i, color=LA_TEAL, buff=0, stroke_width=6)
        j_hat = Arrow(start=origin, end=p_j, color=LA_PINK, buff=0, stroke_width=6)
        
        label_i = MathTex(r"\hat{i}", color=LA_TEAL).next_to(i_hat, DOWN, buff=0.1)
        label_j = MathTex(r"\hat{j}", color=LA_PINK).next_to(j_hat, LEFT, buff=0.1)
        
        # 3. 右侧说明文字
        RIGHT_ZONE = RIGHT * 3.5
        title = Text("空间的基础：基向量", font_size=32, color=LA_PURPLE, weight=BOLD)
        title.move_to(RIGHT_ZONE + UP * 2.5)
        
        desc = VGroup(
            Text("二维空间由两个向量定义：", font_size=22),
            VGroup(
                MathTex(r"\hat{i} = [1, 0]^T", color=LA_TEAL),
                Text(" (向右 1 单位)", font_size=20, color=LA_GRAY)
            ).arrange(RIGHT),
            VGroup(
                MathTex(r"\hat{j} = [0, 1]^T", color=LA_PINK),
                Text(" (向上 1 单位)", font_size=20, color=LA_GRAY)
            ).arrange(RIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        desc.next_to(title, DOWN, buff=0.8)
        
        self.play(Create(grid), run_time=1.5)
        self.play(GrowArrow(i_hat), Write(label_i))
        self.play(GrowArrow(j_hat), Write(label_j))
        self.play(Write(title), Write(desc))
        self.wait(2)
        
        # 清理右侧，保留左侧
        self.play(FadeOut(title), FadeOut(desc))
        
        i_group = VGroup(i_hat, label_i)
        j_group = VGroup(j_hat, label_j)
        
        return grid, (i_group, j_group)

    def apply_matrix_transformation(self, grid, basis_vectors):
        """核心：矩阵变换动画 (修复飞出屏幕问题)"""
        
        i_group, j_group = basis_vectors
        RIGHT_ZONE = RIGHT * 3.5
        
        # 1. 引入矩阵
        title = Text("施加一个矩阵变换", font_size=32, color=LA_YELLOW, weight=BOLD)
        title.move_to(RIGHT_ZONE + UP * 2.5)
        
        matrix_tex = MathTex(
            r"M = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}",
            color=WHITE, font_size=48
        )
        matrix_tex.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), Write(matrix_tex))
        self.wait(1)
        
        # 2. 变换动画
        matrix = [[3, 1], [0, 2]]
        
        action_text = Text("空间开始拉伸...", font_size=24, color=LA_GRAY).next_to(matrix_tex, DOWN, buff=1.0)
        self.play(Write(action_text))
        
        # --- 核心修复：指定 about_point ---
        # 默认 ApplyMatrix 是相对于屏幕原点变换，会导致左侧网格飞得更远。
        # 我们需要相对于网格自己的原点进行变换。
        grid_origin = grid.c2p(0, 0)
        
        self.play(
            # ApplyMatrix(matrix, mobj) 的 about_point 参数控制变换中心
            grid.animate.apply_matrix(matrix, about_point=grid_origin),
            i_group.animate.apply_matrix(matrix, about_point=grid_origin),
            j_group.animate.apply_matrix(matrix, about_point=grid_origin),
            run_time=3
        )
        
        self.wait(1)
        
        result_text = Text("这就是线性变换！", font_size=28, color=LA_TEAL, weight=BOLD).next_to(action_text, DOWN, buff=0.5)
        self.play(ReplacementTransform(action_text, result_text))
        self.wait(2)
        
        # 清场
        self.play(FadeOut(Group(*self.mobjects)))

    def explain_column_vectors(self):
        """原理：列向量就是基向量的新位置 (修复重叠布局)"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 1. 复现变换后的状态 (静态)
        # 这里需要手动构建变换后的网格
        grid = NumberPlane(
            x_range=[-5, 5, 1], y_range=[-4, 4, 1],
            x_length=7, y_length=6,
            background_line_style={"stroke_color": LA_GRAY, "stroke_opacity": 0.5},
            axis_config={"include_numbers": False}
        ).scale(0.65).move_to(LEFT_ZONE)
        
        # 应用变换，保持原点不动
        matrix_val = [[3, 1], [0, 2]]
        grid.apply_matrix(matrix_val, about_point=grid.c2p(0,0))
        
        # 手动计算变换后的向量位置
        origin = grid.c2p(0, 0)
        # 获取 grid 当前的单位长度向量
        # 注意：经过 apply_matrix 后，grid 的坐标系已经变了
        # 直接使用 transform 后的坐标点
        p_i_new = grid.c2p(1, 0)
        p_j_new = grid.c2p(0, 1)
        
        i_arrow = Arrow(origin, p_i_new, color=LA_TEAL, buff=0, stroke_width=6)
        j_arrow = Arrow(origin, p_j_new, color=LA_PINK, buff=0, stroke_width=6)
        
        label_i = MathTex(r"\hat{i}_{new}", color=LA_TEAL).next_to(i_arrow, DOWN)
        label_j = MathTex(r"\hat{j}_{new}", color=LA_PINK).next_to(j_arrow, UP)
        
        self.play(FadeIn(grid), GrowArrow(i_arrow), GrowArrow(j_arrow), Write(label_i), Write(label_j))
        
        # 2. 右侧核心揭秘 (使用 VGroup 自动布局防重叠)
        
        # 标题
        title = Text("核心秘密：看列向量", font_size=32, color=LA_YELLOW, weight=BOLD)
        
        # 矩阵 (使用 Matrix 类)
        matrix_mobj = Matrix(
            [[3, 1], [0, 2]],
            left_bracket="[", right_bracket="]",
            element_to_mobject_config={"font_size": 42}
        )
        # 上色
        ents = matrix_mobj.get_entries()
        ents[0].set_color(LA_TEAL); ents[2].set_color(LA_TEAL) # 第一列
        ents[1].set_color(LA_PINK); ents[3].set_color(LA_PINK) # 第二列
        
        # 拆分列向量
        col1 = Matrix([[3], [0]], left_bracket="[", right_bracket="]").set_color(LA_TEAL).scale(1.1)
        col2 = Matrix([[1], [2]], left_bracket="[", right_bracket="]").set_color(LA_PINK).scale(1.1)
        
        cols_group = VGroup(col1, col2).arrange(RIGHT, buff=1.0)
        
        # 解释文字
        text_i = Text("第一列 = i 的新坐标", font_size=22, color=LA_TEAL)
        text_j = Text("第二列 = j 的新坐标", font_size=22, color=LA_PINK)
        
        # 将文字放在对应列向量下方
        text_i.next_to(col1, DOWN, buff=0.2)
        text_j.next_to(col2, DOWN, buff=0.2)
        
        # 打包文字组
        cols_with_text = VGroup(
            VGroup(col1, text_i), 
            VGroup(col2, text_j)
        ).arrange(RIGHT, buff=0.5)
        
        # 总结
        summary = Text("矩阵就是告诉基向量\n\"你们该去哪里\"", font_size=24, color=WHITE)
        
        # --- 终极布局 ---
        # 将所有右侧元素放入一个大的 VGroup，统一 arrange
        right_content = VGroup(
            title,
            matrix_mobj,
            cols_with_text,
            summary
        ).arrange(DOWN, buff=0.6).move_to(RIGHT_ZONE)
        
        # 动画流程
        self.play(Write(title))
        self.play(FadeIn(matrix_mobj))
        self.wait(1)
        
        # 变换：矩阵 -> 列向量
        self.play(
            Transform(matrix_mobj, cols_with_text[0][0]), # 矩阵变为左列(视觉暂留)
            FadeIn(cols_with_text) # 显示完整列向量组
        )
        self.remove(matrix_mobj) # 移除旧对象
        
        # 连接线
        line1 = DashedLine(col1.get_left(), i_arrow.get_end(), color=LA_TEAL)
        line2 = DashedLine(col2.get_left(), j_arrow.get_end(), color=LA_PINK)
        
        self.play(Create(line1), Create(line2))
        self.wait(1)
        self.play(FadeOut(line1), FadeOut(line2))
        
        self.play(Write(summary))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def visualize_determinant(self):
        """进阶：行列式与面积"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("行列式 (Determinant)", font_size=36, color=LA_YELLOW).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 初始单位正方形
        grid_mini = NumberPlane(
            x_range=[-2, 4], y_range=[-2, 4],
            x_length=5, y_length=5
        ).move_to(LEFT_ZONE)
        
        square = Square(side_length=grid_mini.x_axis.unit_size, color=LA_YELLOW, fill_opacity=0.5)
        square.move_to(grid_mini.c2p(0.5, 0.5))
        
        area_label = Text("面积 = 1", font_size=24, color=LA_YELLOW).next_to(square, UP)
        
        self.play(FadeIn(grid_mini), FadeIn(square), Write(area_label))
        
        # 2. 变换
        p0 = grid_mini.c2p(0, 0)
        p1 = grid_mini.c2p(3, 0)
        p2 = grid_mini.c2p(4, 2) 
        p3 = grid_mini.c2p(1, 2)
        
        new_quad = Polygon(p0, p1, p2, p3, color=LA_YELLOW, fill_opacity=0.5)
        
        self.play(
            Transform(square, new_quad),
            FadeOut(area_label)
        )
        
        # 3. 右侧计算 (VGroup 布局)
        calc_title = Text("面积扩大了多少？", font_size=28, color=WHITE)
        
        det_tex = MathTex(
            r"\det(M) = \begin{vmatrix} 3 & 1 \\ 0 & 2 \end{vmatrix}",
            font_size=40
        )
        
        calc_step = MathTex(
            r"= (3 \times 2) - (1 \times 0) = 6",
            font_size=40, color=LA_YELLOW
        )
        
        final_text = Text("行列式的值 = 面积缩放比例", font_size=26, color=LA_TEAL)
        
        right_content = VGroup(calc_title, det_tex, calc_step, final_text).arrange(DOWN, buff=0.5).move_to(RIGHT_ZONE)
        
        self.play(Write(calc_title))
        self.play(Write(det_tex))
        self.play(Write(calc_step))
        
        new_area_label = Text("新面积 = 6", font_size=24, color=LA_YELLOW).next_to(square, UP)
        self.play(Write(new_area_label))
        
        self.play(Write(final_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_ending(self):
        """结尾与预告"""
        
        title = Text("总结：矩阵的本质", font_size=40, color=LA_PURPLE).to_edge(UP, buff=1.0)
        
        points = VGroup(
            Text("1. 矩阵是空间的变换（拉伸、旋转、剪切）", font_size=24),
            Text("2. 列向量告诉我们要把基向量送到哪里", font_size=24),
            Text("3. 行列式告诉我们面积/体积缩放了多少", font_size=24, color=LA_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), Write(points))
        self.wait(2)
        
        self.play(FadeOut(title), FadeOut(points))
        
        next_ep = Text("下期预告：特征值与特征向量", font_size=40, color=LA_TEAL).move_to(UP * 0.5)
        desc = Text("在旋转的世界中，寻找那根不变的\"定海神针\"", font_size=24, color=LA_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))