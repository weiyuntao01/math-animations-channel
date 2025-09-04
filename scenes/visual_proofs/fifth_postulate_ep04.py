"""
系列三：视觉化证明经典
EP04: 欧几里得第五公设
平行线的千年争议与非欧几何的诞生
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


class FifthPostulateEP04(Scene):
    """欧几里得第五公设 - 视觉化证明经典 EP04"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 0. 系列开场
        self.show_series_intro()
        
        # 1. 引入：《几何原本》
        self.introduce_elements()
        
        # 2. 前四条公设
        self.first_four_postulates()
        
        # 3. 第五公设的表述
        self.fifth_postulate_statement()
        
        # 4. 等价命题：平行公设
        self.parallel_postulate()
        
        # 5. 两千年的证明尝试
        self.proof_attempts()
        
        # 6. 非欧几何的诞生
        self.non_euclidean_birth()
        
        # 7. 球面几何
        self.spherical_geometry()
        
        # 8. 双曲几何
        self.hyperbolic_geometry()
        
        # 9. 现代意义
        self.modern_significance()
        
        # 10. 总结
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
            "第4集：欧几里得第五公设",
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
    
    def introduce_elements(self):
        """引入《几何原本》"""
        self.clear()
        
        title = Text("改变数学历史的一条公设", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 《几何原本》介绍
        elements = VGroup(
            Text("欧几里得《几何原本》", font_size=SUBTITLE_SIZE, color=PROOF_ORANGE),
            Text("公元前300年", font_size=NORMAL_SIZE),
            Text("23个定义，5条公设，5条公理", font_size=NORMAL_SIZE),
            Text("建立了整个几何学体系", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.4)
        
        for line in elements:
            self.play(Write(line), run_time=0.6)
        
        self.wait(1)
        
        # 过渡
        question = Text(
            "为什么第五公设如此特殊？",
            font_size=SUBTITLE_SIZE,
            color=PROOF_YELLOW,
            weight=BOLD
        )
        question.shift(DOWN * 2.5)
        self.play(Write(question))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(elements), FadeOut(question))
    
    def first_four_postulates(self):
        """前四条公设"""
        self.clear()
        
        title = Text("前四条公设（显而易见）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 公设1：两点确定一条直线
        postulate1 = VGroup(
            Text("公设1：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("过两点可作一条直线", font_size=NORMAL_SIZE)
        ).arrange(RIGHT)
        postulate1.shift(UP * 2 + LEFT * 3)
        
        # 演示
        point1 = Dot(LEFT * 2 + UP * 2, color=PROOF_RED)
        point2 = Dot(RIGHT * 1 + UP * 2, color=PROOF_RED)
        line1 = Line(point1.get_center(), point2.get_center(), color=WHITE)
        
        self.play(Write(postulate1))
        self.play(Create(point1), Create(point2))
        self.play(Create(line1))
        
        # 公设2：线段可以延长
        postulate2 = VGroup(
            Text("公设2：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("线段可以无限延长", font_size=NORMAL_SIZE)
        ).arrange(RIGHT)
        postulate2.shift(UP * 0.5 + LEFT * 3)
        
        # 演示
        segment = Line(LEFT * 2 + UP * 0.5, RIGHT * 0 + UP * 0.5, color=WHITE)
        extension1 = DashedLine(RIGHT * 0 + UP * 0.5, RIGHT * 2 + UP * 0.5, color=PROOF_GREEN)
        extension2 = DashedLine(LEFT * 2 + UP * 0.5, LEFT * 4 + UP * 0.5, color=PROOF_GREEN)
        
        self.play(Write(postulate2))
        self.play(Create(segment))
        self.play(Create(extension1), Create(extension2))
        
        # 公设3：以任意点为圆心可作圆
        postulate3 = VGroup(
            Text("公设3：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("以任意点为圆心、任意长为半径作圆", font_size=NORMAL_SIZE)
        ).arrange(RIGHT)
        postulate3.shift(DOWN * 1 + LEFT * 3)
        
        # 演示
        center = Dot(LEFT * 1 + DOWN * 1, color=PROOF_RED)
        circle = Circle(radius=1, color=WHITE).move_to(center)
        
        self.play(Write(postulate3))
        self.play(Create(center))
        self.play(Create(circle))
        
        # 公设4：所有直角都相等
        postulate4 = VGroup(
            Text("公设4：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("所有直角都相等", font_size=NORMAL_SIZE)
        ).arrange(RIGHT)
        postulate4.shift(DOWN * 2.5 + LEFT * 3)
        
        # 演示
        angle1 = RightAngle(Line(ORIGIN, RIGHT), Line(ORIGIN, UP), length=0.3, color=PROOF_ORANGE)
        angle2 = RightAngle(Line(RIGHT * 2, RIGHT * 3), Line(RIGHT * 2, RIGHT * 2 + UP), length=0.3, color=PROOF_ORANGE)
        angle1.shift(RIGHT * 2 + DOWN * 2.5)
        angle2.shift(RIGHT * 4 + DOWN * 2.5)
        
        self.play(Write(postulate4))
        self.play(Create(angle1), Create(angle2))
        
        # 评价
        comment = Text(
            "简洁、直观、自明",
            font_size=SUBTITLE_SIZE,
            color=PROOF_GREEN,
            weight=BOLD
        )
        comment.shift(RIGHT * 3)
        self.play(Write(comment))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(postulate1), FadeOut(postulate2),
            FadeOut(postulate3), FadeOut(postulate4), FadeOut(comment),
            FadeOut(point1), FadeOut(point2), FadeOut(line1),
            FadeOut(segment), FadeOut(extension1), FadeOut(extension2),
            FadeOut(center), FadeOut(circle), FadeOut(angle1), FadeOut(angle2)
        )
    
    def fifth_postulate_statement(self):
        """第五公设的表述"""
        self.clear()
        
        title = Text("第五公设（原始表述）", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 原始表述
        original = Text(
            "若一直线与两直线相交，\n"
            "且同侧内角之和小于两直角，\n"
            "则两直线在该侧必相交。",
            font_size=NORMAL_SIZE
        )
        original.shift(UP * 1.5)
        self.play(Write(original))
        
        # 几何演示
        # 横线（切线）
        transversal = Line(LEFT * 3 + UP * 0, RIGHT * 3 + DOWN * 1, color=PROOF_YELLOW, stroke_width=3)
        
        # 两条被切的线
        line1 = Line(LEFT * 3 + UP * 2, RIGHT * 2 + UP * 0.5, color=WHITE, stroke_width=2)
        line2 = Line(LEFT * 3 + DOWN * 2, RIGHT * 2 + DOWN * 1, color=WHITE, stroke_width=2)
        
        self.play(Create(transversal))
        self.play(Create(line1), Create(line2))
        
        # 标记内角
        angle1 = Arc(
            radius=0.5, start_angle=0, angle=PI/6,
            arc_center=LEFT * 0.5 + UP * 0.25,
            color=PROOF_ORANGE
        )
        angle2 = Arc(
            radius=0.5, start_angle=0, angle=PI/3,
            arc_center=LEFT * 0.5 + DOWN * 0.5,
            color=PROOF_ORANGE
        )
        
        angle1_label = MathTex(r"\alpha", font_size=24, color=PROOF_ORANGE)
        angle1_label.next_to(angle1, RIGHT, buff=0.1)
        
        angle2_label = MathTex(r"\beta", font_size=24, color=PROOF_ORANGE)
        angle2_label.next_to(angle2, RIGHT, buff=0.1)
        
        self.play(Create(angle1), Create(angle2))
        self.play(Write(angle1_label), Write(angle2_label))
        
        # 条件
        condition = MathTex(
            r"\alpha + \beta < 180°",
            font_size=32,
            color=PROOF_RED
        )
        condition.shift(LEFT * 3 + DOWN * 1)
        self.play(Write(condition))
        
        # 延长线相交
        intersection = Dot(RIGHT * 4 + DOWN * 0.2, color=PROOF_GREEN, radius=0.1)
        extended1 = DashedLine(RIGHT * 2 + UP * 0.5, RIGHT * 4 + DOWN * 0.2, color=PROOF_GREEN)
        extended2 = DashedLine(RIGHT * 2 + DOWN * 1, RIGHT * 4 + DOWN * 0.2, color=PROOF_GREEN)
        
        self.play(Create(extended1), Create(extended2))
        self.play(Create(intersection))
        
        # 结论
        conclusion_text = Text(
            "则两线必相交",
            font_size=NORMAL_SIZE,
            color=PROOF_GREEN
        )
        conclusion_text.next_to(intersection, DOWN, buff=0.5)
        self.play(Write(conclusion_text))
        
        # 问题
        problem = Text(
            "太复杂！不够自明！",
            font_size=SUBTITLE_SIZE,
            color=PROOF_RED,
            weight=BOLD
        )
        problem.shift(DOWN * 3)
        self.play(Write(problem))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(original), FadeOut(transversal),
            FadeOut(line1), FadeOut(line2), FadeOut(angle1), FadeOut(angle2),
            FadeOut(angle1_label), FadeOut(angle2_label), FadeOut(condition),
            FadeOut(intersection), FadeOut(extended1), FadeOut(extended2),
            FadeOut(conclusion_text), FadeOut(problem)
        )
    
    def parallel_postulate(self):
        """等价命题：平行公设"""
        self.clear()
        
        title = Text("等价命题：平行公设", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 平行公设表述
        parallel_statement = Text(
            "过直线外一点，\n"
            "有且仅有一条直线与已知直线平行",
            font_size=SUBTITLE_SIZE,
            color=PROOF_GREEN
        )
        parallel_statement.shift(UP * 1)
        self.play(Write(parallel_statement))
        
        # 几何演示
        # 已知直线
        given_line = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=3)
        given_line.shift(DOWN * 1)
        
        # 直线外一点
        point = Dot(UP * 1, color=PROOF_RED, radius=0.1)
        point_label = Text("P", font_size=24, color=PROOF_RED)
        point_label.next_to(point, UP, buff=0.1)
        
        self.play(Create(given_line))
        self.play(Create(point), Write(point_label))
        
        # 唯一平行线
        parallel_line = Line(LEFT * 4, RIGHT * 4, color=PROOF_GREEN, stroke_width=3)
        parallel_line.shift(UP * 1)
        
        self.play(Create(parallel_line))
        
        # 强调唯一性
        uniqueness = Text(
            "有且仅有一条",
            font_size=NORMAL_SIZE,
            color=PROOF_YELLOW,
            weight=BOLD
        )
        uniqueness.next_to(parallel_line, UP, buff=0.3)
        self.play(Write(uniqueness))
        
        # 其他尝试的线（会相交）
        other_line1 = Line(LEFT * 4, RIGHT * 4, color=PROOF_GRAY, stroke_width=1)
        other_line1.rotate(0.1)
        other_line1.shift(UP * 1)
        
        other_line2 = Line(LEFT * 4, RIGHT * 4, color=PROOF_GRAY, stroke_width=1)
        other_line2.rotate(-0.1)
        other_line2.shift(UP * 1)
        
        self.play(Create(other_line1), Create(other_line2))
        
        # 显示相交
        cross1 = Cross(scale_factor=0.2, color=PROOF_RED)
        cross2 = Cross(scale_factor=0.2, color=PROOF_RED)
        cross1.move_to(RIGHT * 3.5 + DOWN * 0.2)
        cross2.move_to(LEFT * 3.5 + DOWN * 0.2)
        
        self.play(Create(cross1), Create(cross2))
        
        # 等价性
        equivalence = VGroup(
            Text("平行公设", font_size=NORMAL_SIZE, color=PROOF_GREEN),
            Text("⇔", font_size=32),
            Text("第五公设", font_size=NORMAL_SIZE, color=PROOF_PURPLE)
        ).arrange(RIGHT, buff=0.5)
        equivalence.shift(DOWN * 3)
        
        self.play(Write(equivalence))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(parallel_statement), FadeOut(given_line),
            FadeOut(point), FadeOut(point_label), FadeOut(parallel_line),
            FadeOut(uniqueness), FadeOut(other_line1), FadeOut(other_line2),
            FadeOut(cross1), FadeOut(cross2), FadeOut(equivalence)
        )
    
    def proof_attempts(self):
        """两千年的证明尝试"""
        self.clear()
        
        title = Text("2000年的证明尝试", font_size=TITLE_SIZE, color=PROOF_ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 历史上的尝试者
        attempts = VGroup(
            Text("托勒密（公元150年）", font_size=NORMAL_SIZE),
            Text("普罗克洛斯（公元450年）", font_size=NORMAL_SIZE),
            Text("纳西尔丁（1250年）", font_size=NORMAL_SIZE),
            Text("萨凯里（1733年）", font_size=NORMAL_SIZE),
            Text("兰伯特（1766年）", font_size=NORMAL_SIZE),
            Text("勒让德（1794年）", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        attempts.shift(LEFT * 3)
        
        for attempt in attempts:
            self.play(Write(attempt), run_time=0.3)
        
        # 所有尝试的结果
        result = VGroup(
            Text("所有证明尝试都失败了", font_size=SUBTITLE_SIZE, color=PROOF_RED),
            Text("要么循环论证", font_size=NORMAL_SIZE),
            Text("要么引入等价假设", font_size=NORMAL_SIZE),
            Text("要么推出矛盾", font_size=NORMAL_SIZE)
        ).arrange(DOWN, buff=0.3)
        result.shift(RIGHT * 2)
        
        for line in result:
            self.play(Write(line), run_time=0.5)
        
        # 转折
        breakthrough = Text(
            "直到有人想到：\n也许第五公设根本无法证明？",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        breakthrough.shift(DOWN * 2.5)
        self.play(Write(breakthrough))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(attempts), FadeOut(result), FadeOut(breakthrough))
    
    def non_euclidean_birth(self):
        """非欧几何的诞生"""
        self.clear()
        
        title = Text("非欧几何的诞生", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 三位先驱
        pioneers = VGroup(
            VGroup(
                Text("高斯", font_size=SUBTITLE_SIZE, color=PROOF_ORANGE),
                Text("（1777-1855）", font_size=SMALL_SIZE),
                Text("秘密研究，未发表", font_size=SMALL_SIZE, color=PROOF_GRAY)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("罗巴切夫斯基", font_size=SUBTITLE_SIZE, color=PROOF_GREEN),
                Text("（1792-1856）", font_size=SMALL_SIZE),
                Text("1829年发表", font_size=SMALL_SIZE)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("鲍耶", font_size=SUBTITLE_SIZE, color=PROOF_CYAN),
                Text("（1802-1860）", font_size=SMALL_SIZE),
                Text("1832年发表", font_size=SMALL_SIZE)
            ).arrange(DOWN, buff=0.2)
        ).arrange(RIGHT, buff=1.5)
        pioneers.shift(UP * 0.5)
        
        for pioneer in pioneers:
            self.play(FadeIn(pioneer, shift=UP), run_time=0.6)
        
        # 核心思想
        idea = VGroup(
            Text("革命性想法：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("否定第五公设，建立新几何", font_size=SUBTITLE_SIZE, color=PROOF_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        idea.shift(DOWN * 1.5)
        
        self.play(Write(idea))
        
        # 两种非欧几何
        geometries = VGroup(
            VGroup(
                Text("双曲几何", font_size=NORMAL_SIZE, color=PROOF_BLUE),
                Text("无穷多条平行线", font_size=SMALL_SIZE)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("球面几何", font_size=NORMAL_SIZE, color=PROOF_ORANGE),
                Text("没有平行线", font_size=SMALL_SIZE)
            ).arrange(DOWN, buff=0.2)
        ).arrange(RIGHT, buff=3)
        geometries.shift(DOWN * 3)
        
        self.play(Write(geometries))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(pioneers), FadeOut(idea), FadeOut(geometries))
    
    def spherical_geometry(self):
        """球面几何"""
        self.clear()
        
        title = Text("球面几何：没有平行线", font_size=TITLE_SIZE, color=PROOF_ORANGE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建球面
        sphere = Sphere(radius=2, resolution=(20, 20))
        sphere.set_color(PROOF_BLUE)
        sphere.set_opacity(0.3)
        sphere.shift(LEFT * 3)
        
        self.play(Create(sphere))
        
        # 大圆作为"直线"
        great_circle1 = Circle(radius=2, color=WHITE, stroke_width=3)
        great_circle1.shift(LEFT * 3)
        
        great_circle2 = Circle(radius=2, color=PROOF_GREEN, stroke_width=3)
        great_circle2.rotate(PI/3, axis=RIGHT)
        great_circle2.shift(LEFT * 3)
        
        self.play(Create(great_circle1), Create(great_circle2))
        
        # 交点
        intersection1 = Dot(LEFT * 3 + UP * 2, color=PROOF_RED, radius=0.1)
        intersection2 = Dot(LEFT * 3 + DOWN * 2, color=PROOF_RED, radius=0.1)
        
        self.play(Create(intersection1), Create(intersection2))
        
        # 性质说明
        properties = VGroup(
            Text("球面几何性质：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("• "直线"是大圆", font_size=SMALL_SIZE),
            Text("• 任意两条"直线"都相交", font_size=SMALL_SIZE),
            Text("• 没有平行线", font_size=SMALL_SIZE, color=PROOF_RED),
            Text("• 三角形内角和 > 180°", font_size=SMALL_SIZE, color=PROOF_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        properties.shift(RIGHT * 2)
        
        for prop in properties:
            self.play(Write(prop), run_time=0.4)
        
        # 球面三角形
        triangle_points = [
            LEFT * 3 + UP * 1.5,
            LEFT * 3 + LEFT * 1.5 + DOWN * 0.5,
            LEFT * 3 + RIGHT * 1.5 + DOWN * 0.5
        ]
        
        # 绘制球面三角形的边（弧线）
        triangle = VMobject()
        triangle.set_points_as_corners(triangle_points + [triangle_points[0]])
        triangle.set_color(PROOF_PURPLE)
        triangle.set_stroke(width=3)
        
        self.play(Create(triangle))
        
        # 内角和
        angle_sum = MathTex(
            r"\alpha + \beta + \gamma > 180°",
            font_size=32,
            color=PROOF_PURPLE
        )
        angle_sum.shift(RIGHT * 2 + DOWN * 2)
        self.play(Write(angle_sum))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(sphere), FadeOut(great_circle1),
            FadeOut(great_circle2), FadeOut(intersection1), FadeOut(intersection2),
            FadeOut(properties), FadeOut(triangle), FadeOut(angle_sum)
        )
    
    def hyperbolic_geometry(self):
        """双曲几何"""
        self.clear()
        
        title = Text("双曲几何：无穷多条平行线", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 庞加莱圆盘模型
        disk = Circle(radius=2.5, color=WHITE, stroke_width=2)
        disk.shift(LEFT * 3)
        self.play(Create(disk))
        
        # 双曲"直线"（圆弧）
        def create_hyperbolic_line(start_angle, end_angle, radius, center):
            arc = Arc(
                radius=radius,
                start_angle=start_angle,
                angle=end_angle - start_angle,
                arc_center=center,
                color=PROOF_CYAN,
                stroke_width=2
            )
            return arc
        
        # 一条双曲直线
        h_line1 = create_hyperbolic_line(PI/6, 5*PI/6, 3, LEFT * 3 + DOWN * 2)
        self.play(Create(h_line1))
        
        # 点P
        point_p = Dot(LEFT * 3 + UP * 1, color=PROOF_RED, radius=0.08)
        point_label = Text("P", font_size=24, color=PROOF_RED)
        point_label.next_to(point_p, UP, buff=0.1)
        self.play(Create(point_p), Write(point_label))
        
        # 多条不相交的线（平行线）
        parallel_lines = VGroup()
        for i in range(5):
            angle_offset = -PI/12 + i * PI/24
            h_line = create_hyperbolic_line(
                PI/6 + angle_offset,
                5*PI/6 + angle_offset,
                3 + i * 0.5,
                LEFT * 3 + DOWN * (2 + i * 0.8)
            )
            h_line.set_color(PROOF_GREEN)
            parallel_lines.add(h_line)
        
        self.play(LaggedStart(*[Create(line) for line in parallel_lines], lag_ratio=0.2))
        
        # 性质说明
        properties = VGroup(
            Text("双曲几何性质：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("• 过一点有无穷多条平行线", font_size=SMALL_SIZE, color=PROOF_GREEN),
            Text("• 平行线会"发散"", font_size=SMALL_SIZE),
            Text("• 三角形内角和 < 180°", font_size=SMALL_SIZE, color=PROOF_RED),
            Text("• 空间呈负曲率", font_size=SMALL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        properties.shift(RIGHT * 2.5)
        
        for prop in properties:
            self.play(Write(prop), run_time=0.4)
        
        # 双曲三角形
        h_triangle = VMobject()
        h_triangle.set_points_smoothly([
            LEFT * 3 + UP * 0.5,
            LEFT * 4 + DOWN * 0.5,
            LEFT * 2 + DOWN * 0.5,
            LEFT * 3 + UP * 0.5
        ])
        h_triangle.set_color(PROOF_PURPLE)
        h_triangle.set_stroke(width=3)
        
        self.play(Create(h_triangle))
        
        # 内角和
        angle_sum = MathTex(
            r"\alpha + \beta + \gamma < 180°",
            font_size=32,
            color=PROOF_PURPLE
        )
        angle_sum.shift(RIGHT * 2.5 + DOWN * 2)
        self.play(Write(angle_sum))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(disk), FadeOut(h_line1),
            FadeOut(point_p), FadeOut(point_label), FadeOut(parallel_lines),
            FadeOut(properties), FadeOut(h_triangle), FadeOut(angle_sum)
        )
    
    def modern_significance(self):
        """现代意义"""
        self.clear()
        
        title = Text("第五公设的现代意义", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 数学影响
        math_impact = VGroup(
            Text("数学影响：", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW),
            Text("• 公理化方法的发展", font_size=NORMAL_SIZE),
            Text("• 数学基础的重新审视", font_size=NORMAL_SIZE),
            Text("• 相容性与独立性概念", font_size=NORMAL_SIZE),
            Text("• 多种几何学并存", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        math_impact.shift(LEFT * 3 + UP * 0.5)
        
        for line in math_impact:
            self.play(Write(line), run_time=0.4)
        
        # 物理应用
        physics_impact = VGroup(
            Text("物理应用：", font_size=SUBTITLE_SIZE, color=PROOF_CYAN),
            Text("• 广义相对论", font_size=NORMAL_SIZE, color=PROOF_ORANGE),
            Text("• 宇宙几何学", font_size=NORMAL_SIZE),
            Text("• 时空弯曲", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        physics_impact.shift(RIGHT * 3 + UP * 0.5)
        
        for line in physics_impact:
            self.play(Write(line), run_time=0.4)
        
        # 哲学意义
        philosophy = Text(
            "真理不是唯一的\n数学可以有多种可能",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        philosophy.shift(DOWN * 2.5)
        self.play(Write(philosophy))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(math_impact), FadeOut(physics_impact), FadeOut(philosophy))
    
    def conclusion(self):
        """总结"""
        self.clear()
        
        title = Text("第五公设：数学史的转折点", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 三种几何对比
        comparison = VGroup(
            VGroup(
                Text("欧氏几何", font_size=NORMAL_SIZE, color=PROOF_GREEN),
                Text("平行线：1条", font_size=SMALL_SIZE),
                Text("曲率：0", font_size=SMALL_SIZE),
                Text("三角形：Σ = 180°", font_size=SMALL_SIZE)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("球面几何", font_size=NORMAL_SIZE, color=PROOF_ORANGE),
                Text("平行线：0条", font_size=SMALL_SIZE),
                Text("曲率：正", font_size=SMALL_SIZE),
                Text("三角形：Σ > 180°", font_size=SMALL_SIZE)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("双曲几何", font_size=NORMAL_SIZE, color=PROOF_BLUE),
                Text("平行线：∞条", font_size=SMALL_SIZE),
                Text("曲率：负", font_size=SMALL_SIZE),
                Text("三角形：Σ < 180°", font_size=SMALL_SIZE)
            ).arrange(DOWN, buff=0.2)
        ).arrange(RIGHT, buff=1.5)
        
        for geom in comparison:
            self.play(FadeIn(geom, shift=UP), run_time=0.5)
        
        # 历史意义
        significance = Text(
            "从绝对真理到多元真理\n"
            "数学的一次解放",
            font_size=SUBTITLE_SIZE,
            color=PROOF_YELLOW
        )
        significance.shift(DOWN * 2)
        self.play(Write(significance))
        
        # 爱因斯坦的评价
        einstein_quote = Text(
            ""欧几里得的第五公设问题\n是数学史上最富有成果的问题"",
            font_size=NORMAL_SIZE,
            color=WHITE
        )
        einstein_quote.shift(DOWN * 3.5)
        self.play(Write(einstein_quote))
        
        self.wait(3)
        
        # 下集预告
        self.play(FadeOut(title), FadeOut(comparison), FadeOut(significance), FadeOut(einstein_quote))
        
        next_episode = VGroup(
            Text("下集预告", font_size=38, color=PROOF_YELLOW),
            Text("第5集：海伦公式", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD),
            Text("只用三边求三角形面积", font_size=SUBTITLE_SIZE, color=WHITE),
            MathTex(r"S = \sqrt{s(s-a)(s-b)(s-c)}", font_size=40, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.5)
        
        for line in next_episode:
            self.play(Write(line), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(next_episode))