from manim import *
import numpy as np
import random

# --- 配色方案 (已补全 LA_GREEN) ---
LA_TEAL = "#2DD4BF"      # 权重 / 正向
LA_PINK = "#F472B6"      # 偏置 / 负向
LA_YELLOW = "#FACC15"    # 激活 / 信号
LA_PURPLE = "#A855F7"    # 矩阵 / 网络结构
LA_RED = "#F87171"       # 错误 / 截止
LA_GREEN = "#4ADE80"     # 成功 / 可分 (新增)
LA_GRAY = "#475569"      # 背景 / 连线
BG_COLOR = "#0F172A"     # 深蓝黑底色

class LinearAlgebraEP05(Scene):
    """线性代数 EP05：神经网络 (修复版)"""
    
    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：打开黑盒
        self.intro_black_box()
        
        # 2. 微观视角：神经元与点积
        self.neuron_geometry()
        
        # 3. 宏观视角：层即矩阵
        self.layer_as_matrix()
        
        # 4. 灵魂注入：非线性激活 (空间扭曲)
        self.activation_magic()
        
        # 5. 系列大结局与预告
        self.show_series_finale()

    def intro_black_box(self):
        """开场：AI 不是魔法，是数学"""
        
        # 标题
        title = Text("EP05: 神经网络", font_size=48, color=LA_PURPLE, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("Matrices in Deep Learning", font_size=28, color=LA_GRAY).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 黑盒隐喻
        box = Square(side_length=3, fill_color=BLACK, stroke_color=LA_TEAL, stroke_width=4)
        box_label = Text("AI 黑盒", font_size=32, color=LA_TEAL).move_to(box)
        
        # 输入数据
        input_data = MathTex(r"\vec{x}", color=WHITE, font_size=48).next_to(box, LEFT, buff=2)
        arrow_in = Arrow(input_data.get_right(), box.get_left(), color=WHITE)
        
        # 输出结果
        output_data = MathTex(r"\vec{y}", color=LA_YELLOW, font_size=48).next_to(box, RIGHT, buff=2)
        arrow_out = Arrow(box.get_right(), output_data.get_left(), color=LA_YELLOW)
        
        self.play(Create(box), Write(box_label))
        self.play(Write(input_data), GrowArrow(arrow_in))
        self.play(GrowArrow(arrow_out), Write(output_data))
        
        # 揭秘
        self.wait(1)
        reveal_text = Text("里面全是矩阵乘法！", font_size=36, color=LA_PINK, weight=BOLD).move_to(DOWN * 2.5)
        self.play(Write(reveal_text))
        self.wait(1)
        
        # 破碎动画 (模拟打开)
        self.play(
            box.animate.scale(3).set_opacity(0),
            FadeOut(box_label),
            FadeOut(input_data), FadeOut(arrow_in),
            FadeOut(output_data), FadeOut(arrow_out),
            FadeOut(reveal_text),
            FadeOut(title), FadeOut(subtitle)
        )

    def neuron_geometry(self):
        """微观：单个神经元 = 空间切割"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 1. 标题
        title = Text("微观：单个神经元", font_size=32, color=LA_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 2. 左侧：神经元结构图
        # 输入节点
        x1 = Circle(radius=0.3, color=WHITE).move_to(LEFT_ZONE + UP + LEFT)
        x2 = Circle(radius=0.3, color=WHITE).move_to(LEFT_ZONE + DOWN + LEFT)
        inputs = VGroup(x1, x2)
        
        # 标签
        l1 = MathTex("x_1").move_to(x1)
        l2 = MathTex("x_2").move_to(x2)
        
        # 输出节点 (神经元)
        neuron = Circle(radius=0.5, color=LA_TEAL, fill_opacity=0.2).move_to(LEFT_ZONE + RIGHT)
        n_label = MathTex("\Sigma").move_to(neuron)
        
        # 连线 (权重)
        w1 = Line(x1.get_right(), neuron.get_left(), color=LA_GRAY)
        w2 = Line(x2.get_right(), neuron.get_left(), color=LA_GRAY)
        
        # 权重文字
        w1_txt = MathTex("w_1", color=LA_TEAL, font_size=24).next_to(w1, UP, buff=0)
        w2_txt = MathTex("w_2", color=LA_TEAL, font_size=24).next_to(w2, DOWN, buff=0)
        
        # 组合
        diagram = VGroup(inputs, l1, l2, neuron, n_label, w1, w2, w1_txt, w2_txt)
        
        self.play(Create(diagram))
        
        # 3. 右侧：数学公式
        math_group = VGroup()
        
        # 公式
        eq1 = MathTex(r"z = w_1 x_1 + w_2 x_2 + b", font_size=36)
        eq2 = MathTex(r"z = \vec{w} \cdot \vec{x} + b", font_size=40, color=LA_TEAL)
        
        desc = Text("本质：向量点积", font_size=24, color=LA_YELLOW)
        
        math_group.add(eq1, eq2, desc).arrange(DOWN, buff=0.5).move_to(RIGHT_ZONE + UP)
        
        self.play(Write(eq1))
        self.play(TransformFromCopy(eq1, eq2))
        self.play(Write(desc))
        
        # 4. 几何意义演示 (左侧变换为坐标系)
        self.play(FadeOut(diagram), run_time=0.5)
        
        # 2D 平面
        plane = NumberPlane(
            x_range=[-3,3], y_range=[-3,3], x_length=5, y_length=5,
            background_line_style={"stroke_opacity": 0.3}
        ).move_to(LEFT_ZONE + DOWN * 0.5)
        
        self.play(Create(plane))
        
        # 绘制决策边界 (w*x + b = 0)
        # 假设 w=[1, 1], b=0 -> x+y=0 -> y=-x
        line = Line(plane.c2p(-2, 2), plane.c2p(2, -2), color=LA_TEAL, stroke_width=4)
        line_label = Text("决策边界", font_size=20, color=LA_TEAL).next_to(line, UR, buff=0.1)
        
        # 两个类别的数据点
        dots_a = VGroup(*[Dot(plane.c2p(r, r+1), color=LA_YELLOW) for r in np.linspace(-1, 1, 5)])
        dots_b = VGroup(*[Dot(plane.c2p(r, r-1), color=LA_PINK) for r in np.linspace(-1, 1, 5)])
        
        self.play(Create(line), Write(line_label))
        self.play(FadeIn(dots_a), FadeIn(dots_b))
        
        # 结论
        conclusion = Text("神经元在空间中切了一刀", font_size=24, color=LA_TEAL).move_to(RIGHT_ZONE + DOWN * 1.5)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def layer_as_matrix(self):
        """宏观：层即矩阵"""
        
        # 布局
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("宏观：层即矩阵", font_size=36, color=LA_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 左侧：简单的神经网络图 (2输入 -> 3隐藏 -> 2输出)
        layers = [2, 3, 2]
        network = VGroup()
        
        # 节点坐标计算
        node_radius = 0.2
        layer_gap = 1.5
        
        # 存储节点位置以便连线
        layer_coords = []
        
        for i, num_nodes in enumerate(layers):
            layer_nodes = []
            x = (i - 1) * layer_gap
            y_start = (num_nodes - 1) * 0.5
            
            for j in range(num_nodes):
                y = y_start - j
                pos = LEFT_ZONE + np.array([x, y, 0])
                
                # 颜色区分
                col = LA_PINK if i==0 else (LA_TEAL if i==1 else LA_YELLOW)
                node = Circle(radius=node_radius, color=col, fill_opacity=0.5).move_to(pos)
                network.add(node)
                layer_nodes.append(node)
            layer_coords.append(layer_nodes)
            
        # 连线
        lines = VGroup()
        for i in range(len(layers) - 1):
            curr_layer = layer_coords[i]
            next_layer = layer_coords[i+1]
            for n1 in curr_layer:
                for n2 in next_layer:
                    line = Line(n1.get_right(), n2.get_left(), color=LA_GRAY, stroke_width=1, stroke_opacity=0.5)
                    lines.add(line)
        
        # 先画线后画点，保证层次
        network_grp = VGroup(lines, network)
        # 整体下移一点
        network_grp.shift(DOWN * 0.5)
        
        self.play(Create(network_grp), run_time=2)
        
        # 2. 右侧：矩阵公式推导
        
        # 这里的关键是展示连线变成了矩阵
        text_layer1 = Text("输入层 -> 隐藏层", font_size=24, color=LA_TEAL)
        
        # 矩阵形式: h = Wx + b
        # W 是 (3x2) 矩阵
        matrix_eq = MathTex(
            r"\vec{h} = ", 
            r"\begin{bmatrix} w_{11} & w_{12} \\ w_{21} & w_{22} \\ w_{31} & w_{32} \end{bmatrix}",
            r"\vec{x} + \vec{b}"
        ).scale(0.8)
        
        matrix_eq[1].set_color(LA_TEAL) # 权重矩阵
        
        matrix_label = Text("权重矩阵 W", font_size=20, color=LA_TEAL).next_to(matrix_eq[1], UP)
        
        text_space = Text("矩阵变换 = 空间映射", font_size=24, color=LA_YELLOW)
        
        # 布局
        right_content = VGroup(text_layer1, matrix_eq, matrix_label, text_space).arrange(DOWN, buff=0.8)
        right_content.move_to(RIGHT_ZONE)
        
        self.play(Write(text_layer1))
        self.play(Write(matrix_eq))
        self.play(Write(matrix_label))
        self.play(Write(text_space))
        
        # 3. 强调：每一层都是一次空间变换
        # 高亮中间的线
        self.play(lines.animate.set_color(LA_TEAL).set_opacity(1), run_time=0.5)
        self.play(lines.animate.set_color(LA_GRAY).set_opacity(0.5), run_time=0.5)
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def activation_magic(self):
        """非线性激活：空间的扭曲 (修复 LA_GREEN 报错)"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("灵魂注入：非线性激活", font_size=36, color=LA_YELLOW).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 线性局限性展示 (左侧)
        # 无法用直线分开的数据 (XOR 问题示意)
        ax = Axes(x_range=[-2, 2], y_range=[-2, 2], x_length=4, y_length=4).move_to(LEFT_ZONE + DOWN * 0.5)
        
        # 四个点：左上/右下是A类，左下/右上是B类
        p1 = Dot(ax.c2p(-1, 1), color=LA_TEAL)
        p2 = Dot(ax.c2p(1, -1), color=LA_TEAL)
        p3 = Dot(ax.c2p(-1, -1), color=LA_PINK)
        p4 = Dot(ax.c2p(1, 1), color=LA_PINK)
        
        dots = VGroup(p1, p2, p3, p4)
        
        self.play(Create(ax), FadeIn(dots))
        
        label_linear = Text("线性变换只能拉伸/旋转", font_size=20, color=LA_GRAY).next_to(ax, UP)
        self.play(Write(label_linear))
        
        # 尝试用直线切分 (失败演示)
        line = Line(ax.c2p(-2, 0), ax.c2p(2, 0), color=WHITE)
        self.play(Create(line))
        self.play(Rotate(line, angle=PI/2), run_time=1)
        self.play(Rotate(line, angle=PI/4), run_time=1)
        
        fail_text = Text("无法线性分类！", font_size=24, color=LA_RED).move_to(LEFT_ZONE + DOWN * 2.5)
        self.play(Write(fail_text))
        
        # 2. 激活函数的作用 (右侧)
        
        # 标题
        act_title = Text("激活函数 (Activation)", font_size=28, color=LA_YELLOW).move_to(RIGHT_ZONE + UP * 2.0)
        self.play(Write(act_title))
        
        # 公式：ReLU
        relu_eq = MathTex(r"\sigma(x) = \max(0, x)", color=LA_YELLOW).next_to(act_title, DOWN, buff=0.5)
        self.play(Write(relu_eq))
        
        # 文字描述
        desc = VGroup(
            Text("它提供了\"弯曲\"空间的能力", font_size=22),
            Text("就像折纸一样", font_size=22, color=LA_PINK),
            Text("让数据变得可分", font_size=22, color=LA_TEAL)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        desc.next_to(relu_eq, DOWN, buff=0.5)
        self.play(Write(desc))
        
        # 3. 扭曲空间动画 (左侧)
        # 移除旧的直线和文字
        self.play(FadeOut(line), FadeOut(label_linear), FadeOut(fail_text))
        
        # 演示空间折叠：把左下角和右上角的粉色点“折”到一边去
        
        # 移动点的位置，模拟经过了非线性变换
        # 目标：让粉色点在一起，青色点在一起
        target_p3 = Dot(ax.c2p(2, 2), color=LA_PINK) # p3 移动到右上
        # p4 不动 (1,1)
        # p1 (-1, 1), p2 (1, -1) -> 移动到左下
        target_p1 = Dot(ax.c2p(-1, -1), color=LA_TEAL)
        target_p2 = Dot(ax.c2p(-0.5, -0.5), color=LA_TEAL)
        
        # 变形！
        self.play(
            Transform(p3, target_p3),
            Transform(p1, target_p1),
            Transform(p2, target_p2),
            run_time=2
        )
        
        # 现在可以用直线分开了 (使用 LA_GREEN)
        success_line = Line(ax.c2p(-2, 2), ax.c2p(2, -2), color=LA_GREEN)
        success_label = Text("现在可分了！", font_size=24, color=LA_GREEN).move_to(LEFT_ZONE + DOWN * 2.5)
        
        self.play(Create(success_line), Write(success_label))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_series_finale(self):
        """系列大结局"""
        
        # 标题
        title = Text("线性代数系列 (完)", font_size=48, color=LA_PURPLE).to_edge(UP, buff=1.0)
        
        # 总结
        points = VGroup(
            Text("矩阵是空间的变换", font_size=26),
            Text("特征值是变换的骨架", font_size=26),
            Text("SVD 是信息的拆解", font_size=26),
            Text("神经网络是矩阵的交响乐", font_size=26, color=LA_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), Write(points))
        self.wait(2)
        
        self.play(FadeOut(title), FadeOut(points))
        
        # 混沌理论预告
        next_series = VGroup(
            Text("下一季预告：", font_size=28, color=LA_TEAL),
            Text("信息论：宇宙的底层代码", font_size=56, color=WHITE, weight=BOLD),
            Text(" 熵增定律· 信噪比 · 冗余的智慧", font_size=28, color=LA_GRAY)
        ).arrange(DOWN, buff=0.4)
        
        next_series.move_to(ORIGIN)
        
        self.play(FadeIn(next_series, shift=UP))
        self.wait(3)
        
        self.play(FadeOut(Group(*self.mobjects)))