"""
系列三：视觉化证明经典
EP03: 黄金分割的几何构造
从正五边形到斐波那契螺旋
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
GOLDEN = "#FFD700"           # 黄金色

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20

# 黄金比例常数
PHI = (1 + np.sqrt(5)) / 2


class GoldenRatioEP03(Scene):
    """黄金分割的几何构造 - 视觉化证明经典 EP03"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 0. 系列开场
        self.show_series_intro()
        
        # 1. 引入：最美的比例
        self.introduce_golden_ratio()
        
        # 2. 黄金分割的定义
        self.golden_ratio_definition()
        
        # 3. 正五边形构造
        self.pentagon_construction()
        
        # 4. 黄金矩形构造
        self.golden_rectangle()
        
        # 5. 斐波那契数列与黄金比
        self.fibonacci_connection()
        
        # 6. 黄金螺旋
        self.golden_spiral()
        
        # 7. 自然界中的黄金比
        self.golden_ratio_in_nature()
        
        # 8. 艺术中的应用
        self.golden_ratio_in_art()
        
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
            "第3集：黄金分割的几何构造",
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
    
    def introduce_golden_ratio(self):
        """引入黄金比例"""
        self.clear()
        
        title = Text("最美的数学比例", font_size=TITLE_SIZE, color=GOLDEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 黄金比例的值
        phi_value = MathTex(
            r"\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618033988...",
            font_size=40,
            color=GOLDEN
        )
        self.play(Write(phi_value))
        
        # 历史背景
        history = VGroup(
            Text("古希腊：神圣比例", font_size=NORMAL_SIZE),
            Text("文艺复兴：黄金分割", font_size=NORMAL_SIZE),
            Text("开普勒：宇宙的珍宝", font_size=NORMAL_SIZE, color=PROOF_ORANGE),
            Text("达芬奇：完美比例", font_size=NORMAL_SIZE, color=PROOF_PURPLE)
        ).arrange(DOWN, buff=0.3)
        history.shift(DOWN * 2)
        
        self.play(
            phi_value.animate.shift(UP * 0.5),
            LaggedStart(*[Write(h) for h in history], lag_ratio=0.2)
        )
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(phi_value), FadeOut(history))
    
    def golden_ratio_definition(self):
        """黄金分割的定义"""
        self.clear()
        
        title = Text("黄金分割的定义", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 线段分割
        line = Line(LEFT * 4, RIGHT * 2, stroke_width=3)
        line.shift(UP * 1)
        
        # 分割点
        golden_point = Dot(LEFT * 1.5, radius=0.08, color=GOLDEN)
        
        # 标注
        label_a = Text("a", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        label_a.next_to(Line(LEFT * 4, LEFT * 1.5), DOWN)
        
        label_b = Text("b", font_size=NORMAL_SIZE, color=PROOF_ORANGE)
        label_b.next_to(Line(LEFT * 1.5, RIGHT * 2), DOWN)
        
        label_total = Text("a + b", font_size=NORMAL_SIZE, color=PROOF_PURPLE)
        label_total.next_to(line, UP)
        
        self.play(Create(line), Create(golden_point))
        self.play(Write(label_a), Write(label_b), Write(label_total))
        
        # 黄金比例关系
        relation = MathTex(
            r"\frac{a + b}{a} = \frac{a}{b} = \phi",
            font_size=48,
            color=GOLDEN
        )
        relation.shift(DOWN * 0.5)
        self.play(Write(relation))
        
        # 推导方程
        derivation = VGroup(
            MathTex(r"\text{设 } \frac{a}{b} = x"),
            MathTex(r"\frac{a+b}{a} = \frac{a}{b}"),
            MathTex(r"1 + \frac{b}{a} = x"),
            MathTex(r"1 + \frac{1}{x} = x"),
            MathTex(r"x^2 - x - 1 = 0", color=PROOF_RED),
            MathTex(r"x = \frac{1 + \sqrt{5}}{2} = \phi", color=GOLDEN)
        ).arrange(DOWN, buff=0.2)
        derivation.scale(0.8)
        derivation.shift(DOWN * 2.5)
        
        for step in derivation:
            self.play(Write(step), run_time=0.5)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(line), FadeOut(golden_point),
            FadeOut(label_a), FadeOut(label_b), FadeOut(label_total),
            FadeOut(relation), FadeOut(derivation)
        )
    
    def pentagon_construction(self):
        """正五边形构造"""
        self.clear()
        
        title = Text("正五边形中的黄金分割", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建正五边形
        pentagon = RegularPolygon(n=5, radius=2.5, color=WHITE, stroke_width=2)
        pentagon.shift(LEFT * 3)
        self.play(Create(pentagon))
        
        # 获取顶点
        vertices = [pentagon.point_from_proportion(i/5) for i in range(5)]
        
        # 画对角线（五角星）
        star_lines = VGroup()
        for i in range(5):
            line = Line(vertices[i], vertices[(i+2) % 5], stroke_color=GOLDEN, stroke_width=2)
            star_lines.add(line)
        
        self.play(LaggedStart(*[Create(l) for l in star_lines], lag_ratio=0.2))
        
        # 标注黄金比例
        # 对角线与边的比例
        diagonal = Line(vertices[0], vertices[2], stroke_color=PROOF_ORANGE, stroke_width=3)
        side = Line(vertices[0], vertices[1], stroke_color=PROOF_GREEN, stroke_width=3)
        
        self.play(
            Create(diagonal),
            Create(side)
        )
        
        # 比例说明
        ratio_text = VGroup(
            Text("对角线长度", font_size=NORMAL_SIZE, color=PROOF_ORANGE),
            Text("边长", font_size=NORMAL_SIZE, color=PROOF_GREEN),
            MathTex(r"\frac{\text{对角线}}{\text{边}} = \phi", font_size=36, color=GOLDEN)
        ).arrange(DOWN, buff=0.3)
        ratio_text.shift(RIGHT * 3)
        
        for text in ratio_text:
            self.play(Write(text), run_time=0.5)
        
        # 内部小五边形
        inner_pentagon = RegularPolygon(
            n=5, 
            radius=2.5/PHI, 
            color=PROOF_CYAN, 
            stroke_width=2
        )
        inner_pentagon.shift(LEFT * 3)
        inner_pentagon.rotate(PI/5)
        
        self.play(Create(inner_pentagon))
        
        # 递归性质
        recursive_text = Text(
            "五角星内部又是正五边形！",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        recursive_text.shift(DOWN * 3)
        self.play(Write(recursive_text))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(pentagon), FadeOut(star_lines),
            FadeOut(diagonal), FadeOut(side), FadeOut(ratio_text),
            FadeOut(inner_pentagon), FadeOut(recursive_text)
        )
    
    def golden_rectangle(self):
        """黄金矩形构造"""
        self.clear()
        
        title = Text("黄金矩形的构造", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 步骤1：正方形
        square = Square(side_length=3, stroke_color=WHITE, stroke_width=2)
        square.shift(LEFT * 3)
        self.play(Create(square))
        
        step1 = Text("1. 从正方形开始", font_size=NORMAL_SIZE, color=PROOF_YELLOW)
        step1.shift(RIGHT * 3 + UP * 2)
        self.play(Write(step1))
        
        # 步骤2：找中点
        midpoint = Dot(LEFT * 3 + DOWN * 1.5, radius=0.08, color=PROOF_RED)
        self.play(Create(midpoint))
        
        step2 = Text("2. 找底边中点", font_size=NORMAL_SIZE, color=PROOF_YELLOW)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        
        # 步骤3：画圆弧
        arc_radius = np.sqrt(1.5**2 + 1.5**2)
        arc = Arc(
            radius=arc_radius,
            start_angle=-PI/2,
            angle=np.arctan(1),
            arc_center=LEFT * 3 + DOWN * 1.5,
            color=PROOF_GREEN,
            stroke_width=2
        )
        self.play(Create(arc))
        
        step3 = Text("3. 以对角线为半径画弧", font_size=NORMAL_SIZE, color=PROOF_YELLOW)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        
        # 步骤4：延长底边
        extension = Line(
            LEFT * 1.5 + DOWN * 1.5,
            LEFT * 1.5 + DOWN * 1.5 + RIGHT * (arc_radius - 1.5),
            stroke_color=WHITE,
            stroke_width=2
        )
        self.play(Create(extension))
        
        # 完成黄金矩形
        golden_rect = Rectangle(
            width=3 * PHI,
            height=3,
            stroke_color=GOLDEN,
            stroke_width=3
        )
        golden_rect.shift(LEFT * 3 + RIGHT * (3 * PHI - 3) / 2)
        
        self.play(Create(golden_rect))
        
        step4 = Text("4. 得到黄金矩形", font_size=NORMAL_SIZE, color=GOLDEN)
        step4.next_to(step3, DOWN, buff=0.3)
        self.play(Write(step4))
        
        # 显示比例
        ratio = MathTex(
            r"\frac{\text{长}}{\text{宽}} = \phi",
            font_size=40,
            color=GOLDEN
        )
        ratio.shift(DOWN * 3)
        self.play(Write(ratio))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(square), FadeOut(midpoint),
            FadeOut(arc), FadeOut(extension), FadeOut(golden_rect),
            FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(step4),
            FadeOut(ratio)
        )
    
    def fibonacci_connection(self):
        """斐波那契数列与黄金比"""
        self.clear()
        
        title = Text("斐波那契数列的秘密", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 斐波那契数列
        fib_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        
        # 显示数列
        sequence_text = Text(
            "1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...",
            font_size=NORMAL_SIZE
        )
        sequence_text.shift(UP * 2)
        self.play(Write(sequence_text))
        
        # 递推关系
        recurrence = MathTex(
            r"F_{n+1} = F_n + F_{n-1}",
            font_size=36,
            color=PROOF_GREEN
        )
        recurrence.shift(UP * 0.5)
        self.play(Write(recurrence))
        
        # 比值表格
        ratio_table = VGroup()
        headers = ["n", "F(n)", "F(n+1)", "F(n+1)/F(n)"]
        
        # 表头
        for i, header in enumerate(headers):
            text = Text(header, font_size=SMALL_SIZE, color=PROOF_YELLOW)
            text.shift(LEFT * 3 + RIGHT * i * 1.5 + DOWN * 0.5)
            ratio_table.add(text)
        
        # 数据行
        for j in range(6):
            n = j + 5
            fn = fib_sequence[n]
            fn1 = fib_sequence[n+1]
            ratio = fn1 / fn
            
            row_data = [str(n), str(fn), str(fn1), f"{ratio:.6f}"]
            for i, data in enumerate(row_data):
                color = GOLDEN if i == 3 else WHITE
                text = Text(data, font_size=SMALL_SIZE, color=color)
                text.shift(LEFT * 3 + RIGHT * i * 1.5 + DOWN * (1 + j * 0.4))
                ratio_table.add(text)
        
        self.play(
            LaggedStart(*[Write(cell) for cell in ratio_table], lag_ratio=0.05)
        )
        
        # 极限
        limit = MathTex(
            r"\lim_{n \to \infty} \frac{F_{n+1}}{F_n} = \phi",
            font_size=40,
            color=GOLDEN
        )
        limit.shift(DOWN * 3.5)
        self.play(Write(limit))
        
        # 斐波那契矩形
        self.wait(1)
        self.play(
            FadeOut(sequence_text), FadeOut(recurrence),
            FadeOut(ratio_table), FadeOut(limit)
        )
        
        # 创建斐波那契矩形
        self.create_fibonacci_rectangles()
        
        self.wait(2)
        self.play(FadeOut(title))
    
    def create_fibonacci_rectangles(self):
        """创建斐波那契矩形"""
        # 斐波那契数
        fibs = [1, 1, 2, 3, 5, 8]
        colors = [PROOF_BLUE, PROOF_GREEN, PROOF_ORANGE, PROOF_PURPLE, PROOF_CYAN, PROOF_RED]
        
        rectangles = VGroup()
        current_pos = ORIGIN
        
        # 创建矩形序列
        for i, (size, color) in enumerate(zip(fibs, colors)):
            rect = Square(side_length=size * 0.3, stroke_color=color, stroke_width=2, fill_color=color, fill_opacity=0.3)
            
            # 定位矩形
            if i == 0:
                rect.move_to(current_pos)
            elif i == 1:
                rect.next_to(rectangles[0], RIGHT, buff=0)
            elif i == 2:
                rect.next_to(rectangles[0], UP, buff=0)
            elif i == 3:
                rect.next_to(rectangles[2], LEFT, buff=0)
            elif i == 4:
                rect.next_to(rectangles[3], DOWN, buff=0)
            elif i == 5:
                rect.next_to(rectangles[4], RIGHT, buff=0)
            
            rectangles.add(rect)
        
        # 居中
        rectangles.move_to(ORIGIN)
        
        # 动画创建
        for rect in rectangles:
            self.play(Create(rect), run_time=0.5)
        
        # 添加数字标签
        for i, (rect, fib) in enumerate(zip(rectangles, fibs)):
            label = Text(str(fib), font_size=20, color=WHITE)
            label.move_to(rect)
            self.play(Write(label), run_time=0.3)
    
    def golden_spiral(self):
        """黄金螺旋"""
        self.clear()
        
        title = Text("黄金螺旋", font_size=TITLE_SIZE, color=GOLDEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建黄金矩形序列
        rectangles = VGroup()
        current_width = 3
        current_height = 3 / PHI
        current_pos = ORIGIN
        
        for i in range(6):
            rect = Rectangle(
                width=current_width,
                height=current_height,
                stroke_color=PROOF_GRAY,
                stroke_width=1
            )
            rect.move_to(current_pos)
            rectangles.add(rect)
            
            # 下一个矩形的参数
            if i % 4 == 0:
                current_pos += RIGHT * current_height / 2 + UP * (current_width - current_height) / 2
                current_width, current_height = current_height, current_width - current_height
            elif i % 4 == 1:
                current_pos += UP * current_height / 2 + LEFT * (current_width - current_height) / 2
                current_width, current_height = current_height, current_width - current_height
            elif i % 4 == 2:
                current_pos += LEFT * current_height / 2 + DOWN * (current_width - current_height) / 2
                current_width, current_height = current_height, current_width - current_height
            else:
                current_pos += DOWN * current_height / 2 + RIGHT * (current_width - current_height) / 2
                current_width, current_height = current_height, current_width - current_height
        
        self.play(LaggedStart(*[Create(r) for r in rectangles], lag_ratio=0.2))
        
        # 创建螺旋
        spiral = self.create_golden_spiral_curve()
        spiral.set_color(GOLDEN)
        spiral.set_stroke(width=3)
        
        self.play(Create(spiral), run_time=3)
        
        # 数学表达式
        equation = MathTex(
            r"r = ae^{b\theta}",
            font_size=36,
            color=GOLDEN
        )
        equation.shift(RIGHT * 4 + UP * 1)
        
        explanation = Text(
            "对数螺旋\n自相似性",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE
        )
        explanation.next_to(equation, DOWN, buff=0.5)
        
        self.play(Write(equation), Write(explanation))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(rectangles),
            FadeOut(spiral), FadeOut(equation),
            FadeOut(explanation)
        )
    
    def create_golden_spiral_curve(self):
        """创建黄金螺旋曲线"""
        theta = np.linspace(0, 4 * PI, 200)
        a = 0.1
        b = np.log(PHI) / (PI / 2)
        
        r = a * np.exp(b * theta)
        
        points = []
        for t, radius in zip(theta, r):
            x = radius * np.cos(t)
            y = radius * np.sin(t)
            points.append([x, y, 0])
        
        spiral = VMobject()
        spiral.set_points_smoothly(points)
        return spiral
    
    def golden_ratio_in_nature(self):
        """自然界中的黄金比"""
        self.clear()
        
        title = Text("自然界的黄金分割", font_size=TITLE_SIZE, color=PROOF_GREEN)
        title.to_edge(UP)
        self.play(Write(title))
        
        examples = VGroup(
            Text("向日葵种子排列", font_size=NORMAL_SIZE),
            Text("鹦鹉螺壳螺旋", font_size=NORMAL_SIZE),
            Text("松果的鳞片", font_size=NORMAL_SIZE),
            Text("花瓣数量（3, 5, 8, 13...）", font_size=NORMAL_SIZE),
            Text("树枝分叉模式", font_size=NORMAL_SIZE),
            Text("DNA双螺旋", font_size=NORMAL_SIZE, color=PROOF_ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        # 创建示意图
        # 向日葵螺旋
        sunflower = self.create_sunflower_pattern()
        sunflower.scale(0.5)
        sunflower.shift(RIGHT * 3)
        
        self.play(
            LaggedStart(*[Write(ex) for ex in examples], lag_ratio=0.2),
            Create(sunflower)
        )
        
        # 说明
        explanation = Text(
            "效率最优的排列方式",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        explanation.shift(DOWN * 3)
        self.play(Write(explanation))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(examples),
            FadeOut(sunflower), FadeOut(explanation)
        )
    
    def create_sunflower_pattern(self):
        """创建向日葵图案"""
        pattern = VGroup()
        n_seeds = 100
        golden_angle = 2 * PI / (PHI ** 2)
        
        for i in range(n_seeds):
            angle = i * golden_angle
            radius = 0.05 * np.sqrt(i)
            
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            seed = Dot([x, y, 0], radius=0.02, color=PROOF_YELLOW)
            pattern.add(seed)
        
        return pattern
    
    def golden_ratio_in_art(self):
        """艺术中的应用"""
        self.clear()
        
        title = Text("艺术中的黄金分割", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        artworks = VGroup(
            Text("• 帕特农神殿", font_size=NORMAL_SIZE),
            Text("• 蒙娜丽莎", font_size=NORMAL_SIZE),
            Text("• 维特鲁威人", font_size=NORMAL_SIZE),
            Text("• 最后的晚餐", font_size=NORMAL_SIZE),
            Text("• 金字塔", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        artworks.shift(LEFT * 3)
        
        # 黄金矩形框架
        frame = Rectangle(
            width=4,
            height=4 / PHI,
            stroke_color=GOLDEN,
            stroke_width=3
        )
        frame.shift(RIGHT * 2)
        
        # 分割线
        vertical = Line(
            frame.get_top() + LEFT * (4 - 4/PHI),
            frame.get_bottom() + LEFT * (4 - 4/PHI),
            stroke_color=GOLDEN,
            stroke_width=2
        )
        
        horizontal = Line(
            frame.get_left() + UP * (2/PHI - 2/PHI**2),
            frame.get_right() + UP * (2/PHI - 2/PHI**2),
            stroke_color=GOLDEN,
            stroke_width=2
        )
        
        self.play(
            LaggedStart(*[Write(art) for art in artworks], lag_ratio=0.2),
            Create(frame)
        )
        self.play(Create(vertical), Create(horizontal))
        
        # 构图原则
        principle = Text(
            "完美的视觉平衡",
            font_size=SUBTITLE_SIZE,
            color=GOLDEN,
            weight=BOLD
        )
        principle.shift(DOWN * 3)
        self.play(Write(principle))
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(artworks), FadeOut(frame),
            FadeOut(vertical), FadeOut(horizontal), FadeOut(principle)
        )
    
    def conclusion(self):
        """总结"""
        self.clear()
        
        title = Text("黄金分割：自然与艺术的桥梁", font_size=TITLE_SIZE, color=GOLDEN, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 核心要点
        key_points = VGroup(
            Text("• 数学定义：φ = (1+√5)/2", font_size=NORMAL_SIZE),
            Text("• 几何构造：正五边形、黄金矩形", font_size=NORMAL_SIZE),
            Text("• 斐波那契：相邻项比值趋向φ", font_size=NORMAL_SIZE),
            Text("• 自然规律：最优排列", font_size=NORMAL_SIZE),
            Text("• 美学原则：和谐比例", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        for point in key_points:
            self.play(Write(point), run_time=0.5)
        
        # 哲学意义
        philosophy = Text(
            "数学之美，无处不在",
            font_size=SUBTITLE_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        philosophy.shift(DOWN * 2.5)
        self.play(Write(philosophy))
        
        self.wait(3)
        
        # 下集预告
        self.play(FadeOut(title), FadeOut(key_points), FadeOut(philosophy))
        
        next_episode = VGroup(
            Text("下集预告", font_size=38, color=PROOF_YELLOW),
            Text("第4集：欧几里得第五公设", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD),
            Text("平行线的千年争议", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("非欧几何的诞生", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.5)
        
        for line in next_episode:
            self.play(Write(line), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(next_episode))