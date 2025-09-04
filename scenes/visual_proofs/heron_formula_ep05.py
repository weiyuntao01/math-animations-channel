"""
系列三：视觉化证明经典
EP05: 海伦公式 - 三角形面积
只用三边求面积的优雅公式
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
PROOF_RED = "#DC2626"       # 警告：矛盾红
PROOF_CYAN = "#06B6D4"      # 清新：对比青

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class HeronFormulaEP05(ThreeDScene):
    """海伦公式 - 视觉化证明经典 EP05"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 0. 系列开场
        self.show_series_intro()
        
        # 1. 引入：三角形面积的难题
        self.introduce_problem()
        
        # 2. 海伦公式的表述
        self.heron_formula_statement()
        
        # 3. 历史背景
        self.historical_background()
        
        # 4. 几何证明
        self.geometric_proof()
        
        # 5. 代数证明
        self.algebraic_proof()
        
        # 6. 3D立体演示
        self.three_d_demonstration()
        
        # 7. 与其他公式的联系
        self.formula_connections()
        
        # 8. 实际应用
        self.practical_applications()
        
        # 9. 总结
        self.conclusion()
    
    def show_series_intro(self):
        """系列开场动画"""
        series_title = Text(
            "视觉化证明经典",
            font_size=50,
            color=PROOF_BLUE,
            weight=BOLD
        )
        
        subtitle = Text(
            "看见数学之美",
            font_size=30,
            color=WHITE
        )
        subtitle.next_to(series_title, DOWN, buff=0.5)
        
        episode_text = Text(
            "第5集：海伦公式",
            font_size=34,
            color=PROOF_GREEN
        )
        episode_text.next_to(subtitle, DOWN, buff=0.8)
        
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(
            FadeOut(series_title),
            FadeOut(subtitle),
            FadeOut(episode_text)
        )
    
    def introduce_problem(self):
        """引入三角形面积的难题"""
        self.clear()
        
        title = Text("一个古老的问题", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建三角形
        triangle = Polygon(
            [-2, -1, 0],
            [2, -1, 0],
            [0.5, 2, 0],
            stroke_color=WHITE,
            stroke_width=3
        )
        self.play(Create(triangle))
        
        # 标注三边
        a_label = Text("a = 5", font_size=NORMAL_SIZE, color=PROOF_ORANGE)
        b_label = Text("b = 6", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        c_label = Text("c = 7", font_size=NORMAL_SIZE, color=PROOF_BLUE)
        
        a_label.next_to(Line(triangle.get_vertices()[1], triangle.get_vertices()[2]), RIGHT)
        b_label.next_to(Line(triangle.get_vertices()[0], triangle.get_vertices()[2]), LEFT)
        c_label.next_to(Line(triangle.get_vertices()[0], triangle.get_vertices()[1]), DOWN)
        
        self.play(Write(a_label), Write(b_label), Write(c_label))
        
        # 问题
        question = VGroup(
            Text("只知道三边长度", font_size=NORMAL_SIZE),
            Text("如何求面积？", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        question.shift(DOWN * 2.5)
        
        self.play(Write(question))
        
        # 常规方法的困难
        difficulty = Text(
            "不知道高，无法用 S = ½ × 底 × 高",
            font_size=NORMAL_SIZE,
            color=PROOF_RED
        )
        difficulty.shift(RIGHT * 2 + UP * 1)
        self.play(Write(difficulty))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(triangle), FadeOut(a_label),
            FadeOut(b_label), FadeOut(c_label), FadeOut(question),
            FadeOut(difficulty)
        )
    
    def heron_formula_statement(self):
        """海伦公式的表述"""
        self.clear()
        
        title = Text("海伦公式", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 公式主体
        main_formula = MathTex(
            r"S = \sqrt{s(s-a)(s-b)(s-c)}",
            font_size=60,
            color=PROOF_GREEN
        )
        self.play(Write(main_formula))
        
        # 半周长定义
        semi_perimeter = MathTex(
            r"s = \frac{a + b + c}{2}",
            font_size=40,
            color=PROOF_ORANGE
        )
        semi_perimeter.shift(DOWN * 1.5)
        
        semi_label = Text("（半周长）", font_size=NORMAL_SIZE, color=PROOF_GRAY)
        semi_label.next_to(semi_perimeter, RIGHT)
        
        self.play(Write(semi_perimeter), Write(semi_label))
        
        # 优雅之处
        elegance = VGroup(
            Text("优雅之处：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("• 只需要三边长度", font_size=SMALL_SIZE),
            Text("• 对称性完美", font_size=SMALL_SIZE),
            Text("• 计算简单", font_size=SMALL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        elegance.shift(DOWN * 3)
        
        for line in elegance:
            self.play(Write(line), run_time=0.4)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(main_formula), FadeOut(semi_perimeter),
            FadeOut(semi_label), FadeOut(elegance)
        )
    
    def historical_background(self):
        """历史背景"""
        self.clear()
        
        title = Text("历史渊源", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 时间线
        timeline = Arrow(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=2)
        timeline.shift(UP * 1)
        self.play(Create(timeline))
        
        # 历史节点
        events = [
            ("古埃及", -3000, "土地测量", PROOF_ORANGE),
            ("阿基米德", -250, "最早记录", PROOF_GREEN),
            ("海伦", 60, "《度量论》", PROOF_BLUE),
            ("秦九韶", 1247, "《数书九章》", PROOF_RED),
            ("现代", 2000, "GPS定位", PROOF_CYAN)
        ]
        
        for name, year, desc, color in events:
            # 计算位置
            x_pos = year / 500  # 缩放年份到坐标
            if x_pos < -5:
                x_pos = -4.5
            if x_pos > 5:
                x_pos = 4.5
            
            # 创建标记
            dot = Dot([x_pos, 1, 0], color=color, radius=0.08)
            
            # 创建标签
            label = VGroup(
                Text(name, font_size=SMALL_SIZE, color=color),
                Text(desc, font_size=16, color=PROOF_GRAY)
            ).arrange(DOWN, buff=0.1)
            
            if year < 0:
                label.next_to(dot, DOWN, buff=0.3)
            else:
                label.next_to(dot, UP, buff=0.3)
            
            self.play(Create(dot), Write(label), run_time=0.5)
        
        # 海伦的贡献
        heron_contribution = Text(
            "海伦：亚历山大港的数学家\n系统证明并推广了这个公式",
            font_size=NORMAL_SIZE,
            color=PROOF_BLUE
        )
        heron_contribution.shift(DOWN * 2)
        self.play(Write(heron_contribution))
        
        self.wait(2)
        # 清理
        self.clear()
    
    def geometric_proof(self):
        """几何证明"""
        self.clear()
        
        title = Text("几何证明", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建三角形
        vertices = [
            np.array([-2.5, -1.5, 0]),
            np.array([2, -1.5, 0]),
            np.array([0, 1.5, 0])
        ]
        triangle = Polygon(*vertices, stroke_color=WHITE, stroke_width=3)
        self.play(Create(triangle))
        
        # 计算边长
        a = np.linalg.norm(vertices[1] - vertices[2])
        b = np.linalg.norm(vertices[0] - vertices[2])
        c = np.linalg.norm(vertices[0] - vertices[1])
        s = (a + b + c) / 2
        
        # 内切圆
        # 计算内心（简化：使用重心近似）
        incenter = (vertices[0] + vertices[1] + vertices[2]) / 3
        
        # 计算内切圆半径（使用海伦公式反推）
        area = np.sqrt(s * (s-a) * (s-b) * (s-c))
        r = area / s
        
        incircle = Circle(radius=r, color=PROOF_YELLOW, stroke_width=2)
        incircle.move_to(incenter)
        self.play(Create(incircle))
        
        # 标注内切圆半径
        radius_line = Line(incenter, incenter + np.array([r, 0, 0]), color=PROOF_YELLOW)
        radius_label = MathTex("r", font_size=24, color=PROOF_YELLOW)
        radius_label.next_to(radius_line, UP, buff=0.1)
        
        self.play(Create(radius_line), Write(radius_label))
        
        # 连接内心到顶点
        lines_to_vertices = VGroup()
        for vertex in vertices:
            line = DashedLine(incenter, vertex, color=PROOF_GRAY, stroke_width=1)
            lines_to_vertices.add(line)
        
        self.play(Create(lines_to_vertices))
        
        # 推导步骤
        steps = VGroup(
            MathTex(r"S = S_1 + S_2 + S_3"),
            MathTex(r"S = \frac{1}{2}ar + \frac{1}{2}br + \frac{1}{2}cr"),
            MathTex(r"S = \frac{r}{2}(a + b + c) = rs"),
            MathTex(r"r = \frac{S}{s}", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        steps.scale(0.8)
        steps.shift(RIGHT * 3.5)
        
        for step in steps:
            self.play(Write(step), run_time=0.6)
        
        # 使用余弦定理推导
        self.wait(1)
        self.play(FadeOut(steps))
        
        # 最终公式
        final_formula = MathTex(
            r"S = \sqrt{s(s-a)(s-b)(s-c)}",
            font_size=48,
            color=PROOF_GREEN
        )
        final_formula.shift(DOWN * 2.5)
        self.play(Write(final_formula))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(triangle), FadeOut(incircle),
            FadeOut(radius_line), FadeOut(radius_label),
            FadeOut(lines_to_vertices), FadeOut(final_formula)
        )
    
    def algebraic_proof(self):
        """代数证明"""
        self.clear()
        
        title = Text("代数证明（余弦定理法）", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 余弦定理
        cosine_law = MathTex(
            r"\cos C = \frac{a^2 + b^2 - c^2}{2ab}",
            font_size=36
        )
        cosine_law.shift(UP * 2)
        self.play(Write(cosine_law))
        
        # 面积公式
        area_formula = MathTex(
            r"S = \frac{1}{2}ab\sin C",
            font_size=36
        )
        area_formula.shift(UP * 0.5)
        self.play(Write(area_formula))
        
        # 恒等式
        identity = MathTex(
            r"\sin^2 C = 1 - \cos^2 C",
            font_size=32
        )
        identity.shift(DOWN * 0.5)
        self.play(Write(identity))
        
        # 代入展开
        expansion = VGroup(
            MathTex(r"S^2 = \frac{1}{4}a^2b^2\sin^2 C"),
            MathTex(r"= \frac{1}{4}a^2b^2(1 - \cos^2 C)"),
            MathTex(r"= \frac{1}{4}a^2b^2\left(1 - \left(\frac{a^2+b^2-c^2}{2ab}\right)^2\right)"),
            MathTex(r"= \frac{1}{16}[4a^2b^2 - (a^2+b^2-c^2)^2]")
        ).arrange(DOWN, buff=0.2)
        expansion.scale(0.7)
        expansion.shift(DOWN * 2)
        
        for step in expansion:
            self.play(Write(step), run_time=0.8)
        
        self.wait(1)
        self.play(FadeOut(cosine_law), FadeOut(area_formula), FadeOut(identity), FadeOut(expansion))
        
        # 因式分解
        factorization = VGroup(
            Text("经过因式分解：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            MathTex(r"16S^2 = 2(a+b+c) \cdot 2(b+c-a) \cdot 2(a+c-b) \cdot 2(a+b-c)"),
            MathTex(r"16S^2 = 16s \cdot (s-a) \cdot (s-b) \cdot (s-c)"),
            MathTex(r"S = \sqrt{s(s-a)(s-b)(s-c)}", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        factorization.scale(0.8)
        
        for step in factorization:
            self.play(Write(step), run_time=0.7)
        
        # 强调结果
        self.play(factorization[-1].animate.scale(1.5).set_color(PROOF_GREEN))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(factorization))
    
    def three_d_demonstration(self):
        """3D立体演示"""
        self.clear()
        
        title = Text("3D立体演示", font_size=TITLE_SIZE, color=PROOF_CYAN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 设置3D相机
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        # 创建三角形的三维表示
        vertices_3d = [
            np.array([-2, -1, 0]),
            np.array([2, -1, 0]),
            np.array([0, 2, 0])
        ]
        
        # 三角形平面
        triangle_3d = Polygon(
            *vertices_3d,
            fill_color=PROOF_BLUE,
            fill_opacity=0.3,
            stroke_color=WHITE,
            stroke_width=3
        )
        self.play(Create(triangle_3d))
        
        # 从三角形构造四面体
        apex = np.array([0, 0, 2.5])
        
        # 四面体的边（使用Line代替Line3D）
        edges = VGroup()
        for vertex in vertices_3d:
            edge = Line(vertex, apex, color=PROOF_ORANGE, stroke_width=2)
            edges.add(edge)
        
        self.play(Create(edges))
        
        # 四面体的面
        faces = VGroup()
        face_colors = [PROOF_RED, PROOF_GREEN, PROOF_PURPLE]
        
        for i in range(3):
            face = Polygon(
                vertices_3d[i],
                vertices_3d[(i+1)%3],
                apex,
                fill_color=face_colors[i],
                fill_opacity=0.2,
                stroke_color=face_colors[i],
                stroke_width=1
            )
            faces.add(face)
        
        self.play(Create(faces))
        
        # 体积与面积的关系说明（移到2D位置）
        self.move_camera(phi=0, theta=-90 * DEGREES)
        
        explanation = VGroup(
            Text("四面体体积法：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            MathTex(r"V = \frac{1}{3} \cdot S_{base} \cdot h"),
            Text("当h→0时，四面体退化为三角形", font_size=SMALL_SIZE),
            MathTex(r"S = \sqrt{s(s-a)(s-b)(s-c)}", color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(DOWN * 2)
        
        for line in explanation:
            self.play(Write(line), run_time=0.5)
        
        # 旋转展示
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        # 恢复2D视角
        self.move_camera(phi=0, theta=-90 * DEGREES)
        
        self.wait(1)
        self.play(
            FadeOut(title), FadeOut(triangle_3d), FadeOut(edges),
            FadeOut(faces), FadeOut(explanation)
        )
    
    def formula_connections(self):
        """与其他公式的联系"""
        self.clear()
        
        title = Text("与其他公式的联系", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 中心：海伦公式
        heron = MathTex(
            r"S = \sqrt{s(s-a)(s-b)(s-c)}",
            font_size=36,
            color=PROOF_GREEN
        )
        heron.move_to(ORIGIN)
        self.play(Write(heron))
        
        # 相关公式
        formulas = [
            (r"S = \frac{1}{2}ab\sin C", "正弦公式", UP + LEFT * 3, PROOF_BLUE),
            (r"S = \frac{abc}{4R}", "外接圆半径", UP + RIGHT * 3, PROOF_ORANGE),
            (r"S = rs", "内切圆半径", DOWN + LEFT * 3, PROOF_YELLOW),
            (r"S = \frac{1}{2}bh", "底×高", DOWN + RIGHT * 3, PROOF_RED)
        ]
        
        connections = VGroup()
        for formula_tex, name, position, color in formulas:
            formula = MathTex(formula_tex, font_size=28, color=color)
            label = Text(name, font_size=20, color=color)
            group = VGroup(formula, label).arrange(DOWN, buff=0.2)
            group.move_to(position)
            
            # 连线
            line = Line(
                heron.get_center(),
                group.get_center(),
                color=PROOF_GRAY,
                stroke_width=1
            )
            
            connections.add(line, group)
            self.play(Create(line), Write(group), run_time=0.5)
        
        # 统一性说明
        unity = Text(
            "海伦公式：最通用的面积公式",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        unity.shift(DOWN * 3)
        self.play(Write(unity))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(heron), FadeOut(connections), FadeOut(unity))
    
    def practical_applications(self):
        """实际应用"""
        self.clear()
        
        title = Text("实际应用", font_size=TITLE_SIZE, color=PROOF_GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 应用场景
        applications = VGroup(
            VGroup(
                Text("测量学", font_size=SUBTITLE_SIZE, color=PROOF_ORANGE),
                Text("• 土地面积测量", font_size=SMALL_SIZE),
                Text("• 不规则地块分割", font_size=SMALL_SIZE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            VGroup(
                Text("GPS定位", font_size=SUBTITLE_SIZE, color=PROOF_BLUE),
                Text("• 三角测量法", font_size=SMALL_SIZE),
                Text("• 位置计算", font_size=SMALL_SIZE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            VGroup(
                Text("工程设计", font_size=SUBTITLE_SIZE, color=PROOF_PURPLE),
                Text("• 结构分析", font_size=SMALL_SIZE),
                Text("• 材料计算", font_size=SMALL_SIZE)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        ).arrange(RIGHT, buff=2)
        
        for app in applications:
            self.play(FadeIn(app, shift=UP), run_time=0.5)
        
        # 实例计算
        example = VGroup(
            Text("实例：三边长 3, 4, 5 的三角形", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            MathTex(r"s = \frac{3+4+5}{2} = 6"),
            MathTex(r"S = \sqrt{6 \times 3 \times 2 \times 1} = \sqrt{36} = 6"),
            Text("正好是直角三角形！", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        example.shift(DOWN * 2)
        
        for line in example:
            self.play(Write(line), run_time=0.5)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(applications), FadeOut(example))
    
    def conclusion(self):
        """总结"""
        self.clear()
        
        title = Text("海伦公式：简洁与深刻", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 公式回顾
        formula = MathTex(
            r"S = \sqrt{s(s-a)(s-b)(s-c)}",
            font_size=48,
            color=PROOF_GREEN
        )
        formula.shift(UP * 0.5)
        self.play(Write(formula))
        
        # 要点总结
        summary = VGroup(
            Text("• 2000年历史的经典公式", font_size=NORMAL_SIZE),
            Text("• 只需三边，无需角度和高", font_size=NORMAL_SIZE),
            Text("• 完美的对称性", font_size=NORMAL_SIZE),
            Text("• 连接多个几何概念", font_size=NORMAL_SIZE),
            Text("• 广泛的实际应用", font_size=NORMAL_SIZE, color=PROOF_ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.shift(DOWN * 1.5)
        
        for point in summary:
            self.play(Write(point), run_time=0.4)
        
        # 数学之美
        beauty = Text(
            "简单的表达，深刻的内涵",
            font_size=SUBTITLE_SIZE,
            color=PROOF_YELLOW,
            weight=BOLD
        )
        beauty.shift(DOWN * 3.5)
        self.play(Write(beauty))
        
        self.wait(3)
        
        # 下集预告
        self.play(FadeOut(title), FadeOut(formula), FadeOut(summary), FadeOut(beauty))
        
        next_episode = VGroup(
            Text("下集预告", font_size=38, color=PROOF_YELLOW),
            Text("第6集：莫比乌斯带与克莱因瓶", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD),
            Text("单侧曲面的奇迹", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("4D投影的视觉盛宴", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.5)
        
        for line in next_episode:
            self.play(Write(line), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(next_episode))