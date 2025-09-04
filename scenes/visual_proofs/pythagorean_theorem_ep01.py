"""
系列三：视觉化证明经典
EP01: 勾股定理的10种证明
从古巴比伦到现代的数学之美
"""

from manim import *
import numpy as np
from typing import List, Tuple

# 系列三配色方案
PROOF_BLUE = "#2563EB"      # 主色：证明蓝
PROOF_GREEN = "#059669"     # 辅助：推理绿  
PROOF_ORANGE = "#EA580C"    # 强调：关键橙
PROOF_PURPLE = "#7C3AED"    # 特殊：优雅紫
PROOF_GRAY = "#6B7280"      # 中性：背景灰
PROOF_YELLOW = "#FCD34D"    # 标记：重点黄

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class PythagoreanTheoremEP01(Scene):
    """勾股定理的10种证明 - 视觉化证明经典 EP01"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 0. 系列开场
        self.show_series_intro()
        
        # 1. 引入：最古老的定理
        self.introduce_pythagorean()
        
        # 2-11. 十种证明
        self.proof_1_chinese_ancient()     # 中国古代证明
        self.proof_2_euclid()              # 欧几里得证明
        self.proof_3_rearrangement()       # 拼图重排证明
        self.proof_4_similar_triangles()   # 相似三角形证明
        self.proof_5_algebraic()           # 代数证明
        self.proof_6_president_garfield()  # 总统证明
        self.proof_7_leonardo_da_vinci()   # 达芬奇证明
        self.proof_8_water_proof()         # 水箱证明
        self.proof_9_einstein()            # 爱因斯坦证明
        self.proof_10_complex_numbers()    # 复数证明
        
        # 12. 总结
        self.conclusion()
    
    def show_series_intro(self):
        """系列开场动画"""
        # 系列标题
        series_title = Text(
            "视觉化证明经典",
            font_size=50,
            color=PROOF_BLUE,
            weight=BOLD
        )
        
        # 副标题
        subtitle = Text(
            "看见数学之美",
            font_size=30,
            color=WHITE
        )
        subtitle.next_to(series_title, DOWN, buff=0.5)
        
        # 集数标题
        episode_text = Text(
            "第1集：勾股定理的10种证明",
            font_size=34,
            color=PROOF_GREEN
        )
        episode_text.next_to(subtitle, DOWN, buff=0.8)
        
        # 动画
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(
            FadeOut(series_title),
            FadeOut(subtitle),
            FadeOut(episode_text)
        )
    
    def introduce_pythagorean(self):
        """引入勾股定理"""
        self.clear()
        
        title = Text("人类最伟大的数学发现之一", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 基本公式
        theorem = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=72
        )
        theorem.set_color(PROOF_GREEN)
        self.play(Write(theorem))
        self.wait(1)
        
        # 历史
        history = VGroup(
            Text("巴比伦泥板：公元前1800年", font_size=NORMAL_SIZE),
            Text("中国《周髀算经》：公元前1000年", font_size=NORMAL_SIZE),
            Text("毕达哥拉斯：公元前500年", font_size=NORMAL_SIZE),
            Text("已知证明方法：超过400种！", font_size=NORMAL_SIZE, color=PROOF_ORANGE)
        ).arrange(DOWN, buff=0.3)
        history.shift(DOWN * 1.5)
        
        self.play(
            theorem.animate.scale(0.6).to_edge(UP).shift(DOWN * 0.5),
            FadeIn(history, shift=UP)
        )
        
        self.wait(2)
        
        # 过渡
        transition = Text(
            "让我们用10种方法证明这个永恒的真理",
            font_size=SUBTITLE_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        transition.move_to(ORIGIN)
        
        self.play(
            FadeOut(title),
            FadeOut(theorem),
            FadeOut(history),
            Write(transition)
        )
        self.wait(2)
        self.play(FadeOut(transition))
    
    def proof_1_chinese_ancient(self):
        """证明1：中国古代证明（赵爽弦图）"""
        self.clear()
        
        # 标题
        proof_num = Text("证明 #1", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("赵爽弦图（中国古代）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建直角三角形
        a, b, c = 3, 4, 5
        scale = 0.8
        
        # 四个直角三角形组成大正方形
        triangles = VGroup()
        colors = [PROOF_BLUE, PROOF_GREEN, PROOF_ORANGE, PROOF_PURPLE]
        
        # 定义四个三角形的位置和旋转
        configs = [
            (0, 0, 0),           # 右下
            (0, 0, PI/2),        # 左下
            (0, 0, PI),          # 左上
            (0, 0, 3*PI/2)       # 右上
        ]
        
        # 创建外部大正方形
        outer_square = Square(side_length=c*scale*2, stroke_color=WHITE, stroke_width=3)
        self.play(Create(outer_square))
        
        # 创建四个三角形
        for i, (x, y, angle) in enumerate(configs):
            triangle = Polygon(
                [0, 0, 0],
                [a*scale, 0, 0],
                [0, b*scale, 0],
                fill_color=colors[i],
                fill_opacity=0.7,
                stroke_color=WHITE,
                stroke_width=2
            )
            triangle.rotate(angle)
            
            # 根据旋转角度调整位置
            if angle == 0:
                triangle.shift(RIGHT*b*scale/2 + DOWN*a*scale/2)
            elif angle == PI/2:
                triangle.shift(LEFT*a*scale/2 + DOWN*b*scale/2)
            elif angle == PI:
                triangle.shift(LEFT*b*scale/2 + UP*a*scale/2)
            else:  # 3*PI/2
                triangle.shift(RIGHT*a*scale/2 + UP*b*scale/2)
            
            triangles.add(triangle)
        
        self.play(
            LaggedStart(*[Create(t) for t in triangles], lag_ratio=0.2)
        )
        
        # 显示内部小正方形
        inner_square = Square(
            side_length=(b-a)*scale*2,
            fill_color=PROOF_YELLOW,
            fill_opacity=0.5,
            stroke_color=WHITE,
            stroke_width=2
        )
        self.play(Create(inner_square))
        
        # 添加标注
        labels = VGroup(
            MathTex("a", font_size=32).next_to(triangles[0], DOWN, buff=0.1),
            MathTex("b", font_size=32).next_to(triangles[0], RIGHT, buff=0.1),
            MathTex("c", font_size=32).next_to(outer_square, LEFT, buff=0.2),
            MathTex("(b-a)", font_size=28).next_to(inner_square, DOWN, buff=0.1)
        )
        
        for label in labels:
            self.play(Write(label), run_time=0.5)
        
        # 推导过程
        derivation = VGroup(
            MathTex(r"c^2 = 4 \times \frac{1}{2}ab + (b-a)^2"),
            MathTex(r"c^2 = 2ab + b^2 - 2ab + a^2"),
            MathTex(r"c^2 = a^2 + b^2", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        derivation.shift(DOWN * 2.5)
        
        for step in derivation:
            self.play(Write(step), run_time=0.8)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(outer_square), FadeOut(triangles),
            FadeOut(inner_square), FadeOut(labels),
            FadeOut(derivation)
        )
    
    def proof_2_euclid(self):
        """证明2：欧几里得证明"""
        self.clear()
        
        proof_num = Text("证明 #2", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("欧几里得证明", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建直角三角形
        scale = 1.2
        a, b, c = 3*scale, 4*scale, 5*scale
        
        triangle = Polygon(
            [-a/2, -b/2, 0],
            [a/2, -b/2, 0],
            [a/2, b/2, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_opacity=0
        )
        self.play(Create(triangle))
        
        # 在每条边上构造正方形
        square_a = Square(side_length=a, fill_color=PROOF_BLUE, fill_opacity=0.5)
        square_a.next_to(triangle, DOWN, buff=0)
        
        square_b = Square(side_length=b, fill_color=PROOF_GREEN, fill_opacity=0.5)
        square_b.next_to(triangle, RIGHT, buff=0)
        
        # 斜边上的正方形（需要旋转）
        angle = np.arctan(b/a)
        square_c = Square(side_length=c, fill_color=PROOF_ORANGE, fill_opacity=0.5)
        square_c.rotate(-angle)
        square_c.move_to(triangle.get_vertices()[0] + 
                        np.array([-c/2 * np.sin(angle), c/2 * np.cos(angle), 0]))
        
        self.play(
            Create(square_a),
            Create(square_b),
            Create(square_c)
        )
        
        # 添加高线
        altitude = DashedLine(
            triangle.get_vertices()[2],
            triangle.get_vertices()[2] + DOWN * b,
            color=PROOF_PURPLE,
            stroke_width=2
        )
        self.play(Create(altitude))
        
        # 标注面积
        area_labels = VGroup(
            MathTex("a^2", font_size=36, color=PROOF_BLUE).move_to(square_a),
            MathTex("b^2", font_size=36, color=PROOF_GREEN).move_to(square_b),
            MathTex("c^2", font_size=36, color=PROOF_ORANGE).move_to(square_c)
        )
        
        for label in area_labels:
            self.play(Write(label), run_time=0.5)
        
        # 显示等式
        equation = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=48,
            color=PROOF_GREEN
        )
        equation.shift(DOWN * 2.5)
        self.play(Write(equation))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(triangle), FadeOut(square_a),
            FadeOut(square_b), FadeOut(square_c),
            FadeOut(altitude), FadeOut(area_labels),
            FadeOut(equation)
        )
    
    def proof_3_rearrangement(self):
        """证明3：拼图重排证明"""
        self.clear()
        
        proof_num = Text("证明 #3", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("拼图重排证明", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建两个相同的直角三角形
        scale = 1
        a, b = 3*scale, 4*scale
        c = 5*scale
        
        # 第一种排列：两个正方形
        square_a = Square(side_length=a, fill_color=PROOF_BLUE, fill_opacity=0.6)
        square_b = Square(side_length=b, fill_color=PROOF_GREEN, fill_opacity=0.6)
        
        square_a.shift(LEFT * 3 + UP * 0.5)
        square_b.shift(LEFT * 3 + DOWN * 1.5)
        
        self.play(Create(square_a), Create(square_b))
        
        # 标注
        label_a = MathTex("a^2", color=WHITE).move_to(square_a)
        label_b = MathTex("b^2", color=WHITE).move_to(square_b)
        self.play(Write(label_a), Write(label_b))
        
        # 分割成片段
        pieces = self.create_puzzle_pieces(a, b)
        pieces.shift(LEFT * 3 + DOWN * 0.5)
        
        # 动画：将正方形变成片段
        self.play(
            FadeOut(square_a), FadeOut(square_b),
            FadeOut(label_a), FadeOut(label_b),
            FadeIn(pieces)
        )
        
        # 重新排列成c²
        target_square = Square(side_length=c, fill_color=PROOF_ORANGE, fill_opacity=0.6)
        target_square.shift(RIGHT * 2)
        
        # 动画：片段飞到新位置
        self.play(
            pieces.animate.move_to(RIGHT * 2),
            run_time=2
        )
        
        self.play(
            Transform(pieces, target_square)
        )
        
        # 标注
        label_c = MathTex("c^2", font_size=48, color=WHITE).move_to(target_square)
        self.play(Write(label_c))
        
        # 显示等式
        final_equation = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=48,
            color=PROOF_GREEN
        )
        final_equation.shift(DOWN * 2.5)
        self.play(Write(final_equation))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(pieces), FadeOut(label_c),
            FadeOut(final_equation)
        )
    
    def create_puzzle_pieces(self, a, b):
        """创建拼图片段"""
        pieces = VGroup()
        
        # 创建几个三角形和矩形片段
        colors = [PROOF_BLUE, PROOF_GREEN, PROOF_ORANGE, PROOF_PURPLE]
        
        # 片段1：三角形
        piece1 = Polygon(
            [0, 0, 0], [a, 0, 0], [0, b, 0],
            fill_color=colors[0], fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        )
        piece1.scale(0.5)
        
        # 片段2：另一个三角形
        piece2 = piece1.copy()
        piece2.set_fill(colors[1])
        piece2.rotate(PI)
        piece2.shift(RIGHT * a * 0.5)
        
        # 片段3和4：矩形
        piece3 = Rectangle(
            width=a*0.3, height=b*0.3,
            fill_color=colors[2], fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        )
        piece3.shift(UP * b * 0.3)
        
        piece4 = Rectangle(
            width=b*0.3, height=a*0.3,
            fill_color=colors[3], fill_opacity=0.7,
            stroke_color=WHITE, stroke_width=2
        )
        piece4.shift(DOWN * a * 0.3)
        
        pieces.add(piece1, piece2, piece3, piece4)
        return pieces
    
    def proof_4_similar_triangles(self):
        """证明4：相似三角形证明"""
        self.clear()
        
        proof_num = Text("证明 #4", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("相似三角形证明", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建大三角形
        scale = 1.5
        vertices = [
            np.array([-2*scale, -1*scale, 0]),  # A
            np.array([2*scale, -1*scale, 0]),   # B
            np.array([0.5*scale, 1.5*scale, 0]) # C
        ]
        
        main_triangle = Polygon(
            *vertices,
            stroke_color=WHITE,
            stroke_width=3,
            fill_opacity=0
        )
        self.play(Create(main_triangle))
        
        # 添加高线
        altitude = Line(
            vertices[2],
            np.array([0.5*scale, -1*scale, 0]),
            stroke_color=PROOF_PURPLE,
            stroke_width=2
        )
        self.play(Create(altitude))
        
        # 标记三个相似三角形
        # 左边小三角形
        left_triangle = Polygon(
            vertices[0],
            np.array([0.5*scale, -1*scale, 0]),
            vertices[2],
            fill_color=PROOF_BLUE,
            fill_opacity=0.5,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        # 右边小三角形
        right_triangle = Polygon(
            np.array([0.5*scale, -1*scale, 0]),
            vertices[1],
            vertices[2],
            fill_color=PROOF_GREEN,
            fill_opacity=0.5,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        self.play(
            Create(left_triangle),
            Create(right_triangle)
        )
        
        # 标注边长
        labels = VGroup(
            MathTex("a", font_size=32).next_to(main_triangle, DOWN).shift(LEFT*1.5),
            MathTex("b", font_size=32).next_to(main_triangle, DOWN).shift(RIGHT*1.5),
            MathTex("c", font_size=32).next_to(main_triangle, LEFT),
            MathTex("p", font_size=28, color=PROOF_BLUE).next_to(altitude, DOWN).shift(LEFT*0.5),
            MathTex("q", font_size=28, color=PROOF_GREEN).next_to(altitude, DOWN).shift(RIGHT*0.5)
        )
        
        for label in labels:
            self.play(Write(label), run_time=0.3)
        
        # 相似关系推导
        similarity_relations = VGroup(
            MathTex(r"\frac{a}{c} = \frac{p}{a} \Rightarrow a^2 = cp"),
            MathTex(r"\frac{b}{c} = \frac{q}{b} \Rightarrow b^2 = cq"),
            MathTex(r"a^2 + b^2 = cp + cq = c(p+q) = c \cdot c = c^2", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        similarity_relations.shift(DOWN * 2)
        
        for relation in similarity_relations:
            self.play(Write(relation), run_time=0.8)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(main_triangle), FadeOut(altitude),
            FadeOut(left_triangle), FadeOut(right_triangle),
            FadeOut(labels), FadeOut(similarity_relations)
        )
    
    def proof_5_algebraic(self):
        """证明5：代数证明"""
        self.clear()
        
        proof_num = Text("证明 #5", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("代数证明", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 构造正方形
        big_square = Square(side_length=4, stroke_color=WHITE, stroke_width=3)
        self.play(Create(big_square))
        
        # 内部四个三角形
        a, b = 1.5, 2
        triangles = VGroup()
        triangle_positions = [
            (UP + RIGHT, 0),
            (UP + LEFT, PI/2),
            (DOWN + LEFT, PI),
            (DOWN + RIGHT, 3*PI/2)
        ]
        
        for pos, angle in triangle_positions:
            tri = Polygon(
                [0, 0, 0], [a, 0, 0], [0, b, 0],
                fill_color=PROOF_BLUE,
                fill_opacity=0.6,
                stroke_color=WHITE,
                stroke_width=2
            )
            tri.rotate(angle)
            tri.shift(pos * 1.2)
            triangles.add(tri)
        
        self.play(
            LaggedStart(*[Create(t) for t in triangles], lag_ratio=0.1)
        )
        
        # 代数推导
        algebraic_steps = VGroup(
            MathTex(r"(a+b)^2 = 4 \times \frac{1}{2}ab + c^2"),
            MathTex(r"a^2 + 2ab + b^2 = 2ab + c^2"),
            MathTex(r"a^2 + b^2 = c^2", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.4)
        algebraic_steps.shift(DOWN * 2)
        
        for step in algebraic_steps:
            self.play(Write(step), run_time=0.8)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(big_square), FadeOut(triangles),
            FadeOut(algebraic_steps)
        )
    
    def proof_6_president_garfield(self):
        """证明6：总统加菲尔德证明"""
        self.clear()
        
        proof_num = Text("证明 #6", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("总统加菲尔德证明（1876年）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建梯形
        a, b = 2, 1.5
        c = np.sqrt(a**2 + b**2)
        
        trapezoid = Polygon(
            [-a/2, -b/2, 0],
            [a/2, -b/2, 0],
            [b/2, b/2, 0],
            [-b/2, b/2, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_color=PROOF_GRAY,
            fill_opacity=0.3
        )
        self.play(Create(trapezoid))
        
        # 分割成三个三角形
        triangle1 = Polygon(
            [-a/2, -b/2, 0],
            [a/2, -b/2, 0],
            [-b/2, b/2, 0],
            fill_color=PROOF_BLUE,
            fill_opacity=0.6,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        triangle2 = Polygon(
            [a/2, -b/2, 0],
            [b/2, b/2, 0],
            [-b/2, b/2, 0],
            fill_color=PROOF_GREEN,
            fill_opacity=0.6,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        triangle3 = Polygon(
            [-b/2, b/2, 0],
            [a/2, -b/2, 0],
            [b/2, b/2, 0],
            fill_color=PROOF_ORANGE,
            fill_opacity=0.6,
            stroke_color=WHITE,
            stroke_width=2
        )
        
        self.play(
            Create(triangle1),
            Create(triangle2),
            Create(triangle3)
        )
        
        # 面积计算
        area_calc = VGroup(
            Text("梯形面积两种算法：", font_size=NORMAL_SIZE, color=PROOF_PURPLE),
            MathTex(r"S = \frac{1}{2}(a+b)^2"),
            MathTex(r"S = 2 \times \frac{1}{2}ab + \frac{1}{2}c^2"),
            MathTex(r"\frac{1}{2}(a^2 + 2ab + b^2) = ab + \frac{1}{2}c^2"),
            MathTex(r"a^2 + b^2 = c^2", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        area_calc.shift(DOWN * 1.5)
        
        for calc in area_calc:
            self.play(Write(calc), run_time=0.6)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(trapezoid), FadeOut(triangle1),
            FadeOut(triangle2), FadeOut(triangle3),
            FadeOut(area_calc)
        )
    
    def proof_7_leonardo_da_vinci(self):
        """证明7：达芬奇证明"""
        self.clear()
        
        proof_num = Text("证明 #7", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("达芬奇证明", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建初始配置
        a, b = 1.5, 2
        c = np.sqrt(a**2 + b**2)
        
        # 两个全等的直角三角形
        triangle1 = Polygon(
            [0, 0, 0], [a, 0, 0], [0, b, 0],
            fill_color=PROOF_BLUE,
            fill_opacity=0.6,
            stroke_color=WHITE,
            stroke_width=2
        )
        triangle1.shift(LEFT * 2)
        
        triangle2 = triangle1.copy()
        triangle2.set_fill(PROOF_GREEN)
        triangle2.rotate(PI)
        triangle2.shift(RIGHT * 2 + UP * b)
        
        self.play(Create(triangle1), Create(triangle2))
        
        # 构造对称图形
        quadrilateral = Polygon(
            triangle1.get_vertices()[0],
            triangle1.get_vertices()[1],
            triangle2.get_vertices()[0],
            triangle2.get_vertices()[1],
            stroke_color=PROOF_PURPLE,
            stroke_width=3,
            fill_opacity=0
        )
        self.play(Create(quadrilateral))
        
        # 翻转动画
        self.play(
            triangle2.animate.rotate(PI).shift(LEFT * 4),
            run_time=2
        )
        
        # 显示形成的正方形
        square_c = Square(side_length=c, stroke_color=PROOF_ORANGE, stroke_width=3)
        square_c.rotate(np.arctan(b/a))
        self.play(Transform(quadrilateral, square_c))
        
        # 标注
        label = MathTex("c^2", font_size=48, color=PROOF_ORANGE)
        label.move_to(square_c)
        self.play(Write(label))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(triangle1), FadeOut(triangle2),
            FadeOut(quadrilateral), FadeOut(label)
        )
    
    def proof_8_water_proof(self):
        """证明8：水箱证明（物理证明）"""
        self.clear()
        
        proof_num = Text("证明 #8", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("水箱证明（物理直观）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建三个水箱（正方形）
        a, b = 1.5, 2
        c = np.sqrt(a**2 + b**2)
        
        tank_a = Square(side_length=a, stroke_color=WHITE, stroke_width=3)
        tank_b = Square(side_length=b, stroke_color=WHITE, stroke_width=3)
        tank_c = Square(side_length=c, stroke_color=WHITE, stroke_width=3)
        
        tank_a.shift(LEFT * 4)
        tank_b.shift(LEFT * 1)
        tank_c.shift(RIGHT * 2.5)
        
        self.play(Create(tank_a), Create(tank_b), Create(tank_c))
        
        # 填充水（动画）
        water_a = Square(side_length=a, fill_color=PROOF_BLUE, fill_opacity=0.7)
        water_b = Square(side_length=b, fill_color=PROOF_GREEN, fill_opacity=0.7)
        water_c = Square(side_length=c, fill_color=PROOF_ORANGE, fill_opacity=0.7)
        
        water_a.move_to(tank_a)
        water_b.move_to(tank_b)
        water_c.move_to(tank_c)
        
        # 水位上升动画
        water_a.scale(0)
        water_b.scale(0)
        water_c.scale(0)
        
        self.play(
            water_a.animate.scale(a),
            water_b.animate.scale(b),
            run_time=2
        )
        
        # 标注体积
        volume_labels = VGroup(
            MathTex("a^2", font_size=32, color=PROOF_BLUE).next_to(tank_a, DOWN),
            MathTex("b^2", font_size=32, color=PROOF_GREEN).next_to(tank_b, DOWN),
            MathTex("c^2", font_size=32, color=PROOF_ORANGE).next_to(tank_c, DOWN)
        )
        
        for label in volume_labels:
            self.play(Write(label), run_time=0.3)
        
        # 倒水动画（概念性）
        arrow1 = CurvedArrow(tank_a.get_right(), tank_c.get_left() + UP*0.5, color=PROOF_BLUE)
        arrow2 = CurvedArrow(tank_b.get_right(), tank_c.get_left() + DOWN*0.5, color=PROOF_GREEN)
        
        self.play(Create(arrow1), Create(arrow2))
        self.play(water_c.animate.scale(c), run_time=2)
        
        # 等式
        equation = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=48,
            color=PROOF_GREEN
        )
        equation.shift(DOWN * 2.5)
        self.play(Write(equation))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(tank_a), FadeOut(tank_b), FadeOut(tank_c),
            FadeOut(water_a), FadeOut(water_b), FadeOut(water_c),
            FadeOut(volume_labels), FadeOut(arrow1), FadeOut(arrow2),
            FadeOut(equation)
        )
    
    def proof_9_einstein(self):
        """证明9：爱因斯坦证明（无字证明）"""
        self.clear()
        
        proof_num = Text("证明 #9", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("爱因斯坦证明（11岁）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 创建直角三角形
        a, b = 2, 1.5
        c = np.sqrt(a**2 + b**2)
        
        main_triangle = Polygon(
            [0, 0, 0], [a, 0, 0], [0, b, 0],
            stroke_color=WHITE,
            stroke_width=3,
            fill_opacity=0
        )
        self.play(Create(main_triangle))
        
        # 从斜边向下作垂线
        # 计算垂足位置
        h = (a * b) / c  # 高
        p = a**2 / c    # 垂足到左顶点的距离
        
        altitude = Line(
            [p, 0, 0],
            [p * a/c, p * b/c, 0],
            stroke_color=PROOF_PURPLE,
            stroke_width=2
        )
        self.play(Create(altitude))
        
        # 三个相似三角形动画
        small_triangle1 = Polygon(
            [0, 0, 0], [p, 0, 0], [p * a/c, p * b/c, 0],
            fill_color=PROOF_BLUE,
            fill_opacity=0.6
        )
        
        small_triangle2 = Polygon(
            [p, 0, 0], [a, 0, 0], [p * a/c, p * b/c, 0],
            fill_color=PROOF_GREEN,
            fill_opacity=0.6
        )
        
        self.play(
            Create(small_triangle1),
            Create(small_triangle2)
        )
        
        # 展示相似性
        similarity_text = Text(
            "三个相似三角形",
            font_size=NORMAL_SIZE,
            color=PROOF_ORANGE
        )
        similarity_text.shift(DOWN * 2)
        self.play(Write(similarity_text))
        
        # 面积关系
        area_relation = MathTex(
            r"\frac{S_1}{a^2} = \frac{S_2}{b^2} = \frac{S}{c^2}",
            font_size=36
        )
        area_relation.shift(DOWN * 2.5)
        self.play(Transform(similarity_text, area_relation))
        
        # 结论
        conclusion = MathTex(
            r"S_1 + S_2 = S \Rightarrow a^2 + b^2 = c^2",
            font_size=40,
            color=PROOF_GREEN
        )
        conclusion.shift(DOWN * 3)
        self.play(Write(conclusion))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(main_triangle), FadeOut(altitude),
            FadeOut(small_triangle1), FadeOut(small_triangle2),
            FadeOut(similarity_text), FadeOut(conclusion)
        )
    
    def proof_10_complex_numbers(self):
        """证明10：复数证明（最优雅）"""
        self.clear()
        
        proof_num = Text("证明 #10", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        proof_num.to_edge(UL)
        
        title = Text("复数证明（最优雅）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(proof_num), Write(title))
        
        # 复平面
        plane = ComplexPlane(
            x_range=[-1, 5],
            y_range=[-1, 5],
            x_length=6,
            y_length=6
        )
        plane.shift(LEFT * 1)
        self.play(Create(plane))
        
        # 复数点
        a, b = 3, 4
        z = complex(a, b)
        
        # 标记点
        point_z = Dot(plane.n2p(z), color=PROOF_ORANGE, radius=0.1)
        label_z = MathTex("z = a + bi", font_size=32, color=PROOF_ORANGE)
        label_z.next_to(point_z, UR)
        
        self.play(Create(point_z), Write(label_z))
        
        # 从原点到z的向量
        vector = Arrow(
            plane.n2p(0),
            plane.n2p(z),
            color=PROOF_GREEN,
            stroke_width=3
        )
        self.play(Create(vector))
        
        # 标注实部和虚部
        real_line = Line(
            plane.n2p(0),
            plane.n2p(a),
            color=PROOF_BLUE,
            stroke_width=2
        )
        imag_line = Line(
            plane.n2p(a),
            plane.n2p(z),
            color=PROOF_PURPLE,
            stroke_width=2
        )
        
        self.play(Create(real_line), Create(imag_line))
        
        # 标签
        label_a = MathTex("a", font_size=28, color=PROOF_BLUE)
        label_a.next_to(real_line, DOWN)
        label_b = MathTex("b", font_size=28, color=PROOF_PURPLE)
        label_b.next_to(imag_line, RIGHT)
        label_c = MathTex("|z| = c", font_size=32, color=PROOF_GREEN)
        label_c.next_to(vector, LEFT)
        
        self.play(Write(label_a), Write(label_b), Write(label_c))
        
        # 复数模的公式
        modulus_formula = VGroup(
            MathTex(r"|z|^2 = z \cdot \bar{z}"),
            MathTex(r"|a + bi|^2 = (a + bi)(a - bi)"),
            MathTex(r"c^2 = a^2 + b^2", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        modulus_formula.shift(RIGHT * 3)
        
        for formula in modulus_formula:
            self.play(Write(formula), run_time=0.8)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(proof_num), FadeOut(title),
            FadeOut(plane), FadeOut(point_z), FadeOut(label_z),
            FadeOut(vector), FadeOut(real_line), FadeOut(imag_line),
            FadeOut(label_a), FadeOut(label_b), FadeOut(label_c),
            FadeOut(modulus_formula)
        )
    
    def conclusion(self):
        """总结"""
        self.clear()
        
        # 标题
        title = Text("勾股定理：永恒的真理", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 10种证明方法回顾
        methods = VGroup(
            Text("1. 赵爽弦图", font_size=SMALL_SIZE),
            Text("2. 欧几里得", font_size=SMALL_SIZE),
            Text("3. 拼图重排", font_size=SMALL_SIZE),
            Text("4. 相似三角形", font_size=SMALL_SIZE),
            Text("5. 代数证明", font_size=SMALL_SIZE),
            Text("6. 总统证明", font_size=SMALL_SIZE),
            Text("7. 达芬奇", font_size=SMALL_SIZE),
            Text("8. 水箱证明", font_size=SMALL_SIZE),
            Text("9. 爱因斯坦", font_size=SMALL_SIZE),
            Text("10. 复数证明", font_size=SMALL_SIZE)
        ).arrange_in_grid(rows=2, cols=5, buff=0.5)
        methods.scale(0.8)
        
        for i, method in enumerate(methods):
            color = [PROOF_BLUE, PROOF_GREEN, PROOF_ORANGE, PROOF_PURPLE, PROOF_YELLOW][i % 5]
            method.set_color(color)
        
        self.play(
            LaggedStart(*[FadeIn(m, scale=0.5) for m in methods], lag_ratio=0.1)
        )
        
        self.wait(2)
        
        # 核心公式
        theorem = MathTex(
            r"a^2 + b^2 = c^2",
            font_size=72,
            color=PROOF_GREEN
        )
        
        self.play(
            FadeOut(methods),
            Write(theorem)
        )
        
        # 哲学意义
        philosophy = Text(
            "一个真理，无数条路径",
            font_size=SUBTITLE_SIZE,
            color=WHITE
        )
        philosophy.shift(DOWN * 2)
        self.play(Write(philosophy))
        
        self.wait(3)
        
        # 下集预告
        self.play(FadeOut(title), FadeOut(theorem), FadeOut(philosophy))
        
        next_episode = VGroup(
            Text("下集预告", font_size=38, color=PROOF_YELLOW),
            Text("第2集：圆周率π的5种推导", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD),
            Text("从阿基米德到蒙特卡洛", font_size=SUBTITLE_SIZE, color=WHITE),
            MathTex(r"\pi = 3.14159265...", font_size=48, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.5)
        
        for line in next_episode:
            self.play(Write(line), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(next_episode))