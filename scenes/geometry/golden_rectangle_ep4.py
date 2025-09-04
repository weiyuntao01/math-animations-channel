from manim import *
import numpy as np

class GoldenRectangleEP4(Scene):
    """黄金矩形与艺术构图 - 黄金分割系列 EP04"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：黄金分割的几何构造
        self.show_golden_ratio_construction()
        
        # 第二部分：黄金矩形的嵌套
        self.show_golden_rectangles_nesting()
        
        # 第三部分：艺术作品中的黄金分割
        self.show_art_examples()
        
        # 第四部分：摄影构图法则
        self.show_photography_composition()
        
        # 第五部分：创造你的黄金构图
        self.show_practical_application()
        
        # 结尾
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第四集：黄金矩形与艺术构图", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_golden_ratio_construction(self):
        """黄金分割的几何构造 - 0:10-0:50"""
        title = Text("黄金分割的几何构造", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建正方形
        square = Square(side_length=3, color=BLUE, stroke_width=3)
        square.shift(LEFT*2)
        square_label = Text("1", font_size=24, color=WHITE)
        square_label.move_to(square.get_center())
        
        self.play(Create(square), Write(square_label))
        self.wait(1)
        
        # 找到中点
        midpoint = square.get_right() + DOWN * 1.5
        midpoint_dot = Dot(midpoint, color=RED)
        midline = Line(square.get_right(), square.get_right() + DOWN * 3, 
                       color=GRAY, stroke_width=2)
        
        self.play(Create(midline), Create(midpoint_dot))
        
        # 画圆弧
        arc_radius = np.sqrt(1.5**2 + 1.5**2)  # 从中点到左下角的距离
        arc = Arc(
            radius=arc_radius,
            start_angle=-PI/2,
            angle=PI/4,
            arc_center=midpoint,
            color=GREEN,
            stroke_width=3
        )
        
        self.play(Create(arc))
        
        # 延长底边
        bottom_line = Line(
            square.get_corner(DL),
            square.get_corner(DR) + RIGHT * (arc_radius - 1.5),
            color=BLUE,
            stroke_width=3
        )
        
        # 计算黄金矩形
        phi = (1 + np.sqrt(5)) / 2
        golden_rect = Rectangle(
            width=3 * phi,
            height=3,
            color=GOLD,
            stroke_width=4
        )
        golden_rect.move_to(square.get_center() + RIGHT * 3 * (phi - 1) / 2)
        
        self.play(
            Create(bottom_line),
            run_time=0.5
        )
        
        # 创建完整的黄金矩形并替换
        self.play(
            ReplacementTransform(VGroup(square, bottom_line), golden_rect),
            FadeOut(square_label),
            run_time=1.5
        )
        
        # 显示比例
        ratio_text = MathTex(
            r"\frac{L}{W} = \varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618",
            font_size=36,
            color=YELLOW
        )
        ratio_text.next_to(golden_rect, DOWN, buff=0.8)
        
        # 添加中文说明
        ratio_label = Text("长 : 宽", font_size=24, color=WHITE)
        ratio_label.next_to(ratio_text, UP, buff=0.3)
        
        self.play(Write(ratio_text))
        self.play(Write(ratio_label))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(golden_rect),
            FadeOut(ratio_text),
            FadeOut(ratio_label),
            FadeOut(midpoint_dot),
            FadeOut(midline),
            FadeOut(arc)
        )
    
    def show_golden_rectangles_nesting(self):
        """黄金矩形的嵌套 - 0:50-1:40"""
        title = Text("黄金矩形的无限嵌套", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建初始黄金矩形
        phi = (1 + np.sqrt(5)) / 2
        scale = 4
        
        # 存储所有矩形和正方形
        rectangles = VGroup()
        squares = VGroup()
        spirals = VGroup()
        
        # 初始矩形
        rect = Rectangle(
            width=scale * phi,
            height=scale,
            color=BLUE_E,
            stroke_width=2
        )
        rectangles.add(rect)
        
        self.play(Create(rect))
        
        # 创建嵌套结构
        current_rect = rect
        current_scale = scale
        colors = [BLUE_D, BLUE_C, BLUE_B, GREEN_E, GREEN_D, GREEN_C, GREEN_B, YELLOW_E]
        
        for i in range(8):
            # 在当前矩形中切出正方形
            square_size = current_scale
            
            # 确定正方形位置（交替方向）
            if i % 4 == 0:  # 左侧
                square = Square(
                    side_length=square_size,
                    color=colors[i % len(colors)],
                    fill_opacity=0.3,
                    stroke_width=2
                )
                square.move_to(current_rect.get_left() + RIGHT * square_size / 2)
            elif i % 4 == 1:  # 上侧
                square = Square(
                    side_length=square_size,
                    color=colors[i % len(colors)],
                    fill_opacity=0.3,
                    stroke_width=2
                )
                square.move_to(current_rect.get_top() + DOWN * square_size / 2)
            elif i % 4 == 2:  # 右侧
                square = Square(
                    side_length=square_size,
                    color=colors[i % len(colors)],
                    fill_opacity=0.3,
                    stroke_width=2
                )
                square.move_to(current_rect.get_right() + LEFT * square_size / 2)
            else:  # 下侧
                square = Square(
                    side_length=square_size,
                    color=colors[i % len(colors)],
                    fill_opacity=0.3,
                    stroke_width=2
                )
                square.move_to(current_rect.get_bottom() + UP * square_size / 2)
            
            squares.add(square)
            
            # 在正方形中画四分之一圆
            if i % 4 == 0:
                arc = Arc(
                    radius=square_size,
                    start_angle=0,
                    angle=PI/2,
                    arc_center=square.get_corner(DR),
                    color=GOLD,
                    stroke_width=3
                )
            elif i % 4 == 1:
                arc = Arc(
                    radius=square_size,
                    start_angle=PI/2,
                    angle=PI/2,
                    arc_center=square.get_corner(DL),
                    color=GOLD,
                    stroke_width=3
                )
            elif i % 4 == 2:
                arc = Arc(
                    radius=square_size,
                    start_angle=PI,
                    angle=PI/2,
                    arc_center=square.get_corner(UL),
                    color=GOLD,
                    stroke_width=3
                )
            else:
                arc = Arc(
                    radius=square_size,
                    start_angle=-PI/2,
                    angle=PI/2,
                    arc_center=square.get_corner(UR),
                    color=GOLD,
                    stroke_width=3
                )
            
            spirals.add(arc)
            
            # 动画
            self.play(
                Create(square),
                Create(arc),
                run_time=0.8
            )
            
            # 更新scale
            current_scale = current_scale / phi
            
            # 为下一次迭代设置current_rect
            if i < 7:
                if i % 4 == 0:
                    next_rect = Rectangle(
                        width=square_size / phi,
                        height=square_size,
                        stroke_width=1,
                        color=GRAY
                    )
                    next_rect.next_to(square, RIGHT, buff=0)
                elif i % 4 == 1:
                    next_rect = Rectangle(
                        width=square_size,
                        height=square_size / phi,
                        stroke_width=1,
                        color=GRAY
                    )
                    next_rect.next_to(square, DOWN, buff=0)
                elif i % 4 == 2:
                    next_rect = Rectangle(
                        width=square_size / phi,
                        height=square_size,
                        stroke_width=1,
                        color=GRAY
                    )
                    next_rect.next_to(square, LEFT, buff=0)
                else:
                    next_rect = Rectangle(
                        width=square_size,
                        height=square_size / phi,
                        stroke_width=1,
                        color=GRAY
                    )
                    next_rect.next_to(square, UP, buff=0)
                
                current_rect = next_rect
        
        # 展示完整的黄金螺线
        self.wait(1)
        
        explanation = Text(
            "每个矩形都是黄金矩形，螺线永无止境",
            font_size=24,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rect),  # 确保清理初始矩形
            FadeOut(squares),
            FadeOut(spirals),
            FadeOut(explanation)
        )
    
    def show_art_examples(self):
        """艺术作品中的黄金分割 - 1:40-2:20"""
        title = Text("经典艺术中的黄金分割", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建画框（代表蒙娜丽莎）
        painting = Rectangle(
            width=4,
            height=5.5,
            color=MAROON,
            fill_opacity=0.2,
            stroke_width=3
        )
        painting.shift(LEFT*3)
        
        # 添加简化的人物轮廓
        face = Circle(radius=0.5, color=WHITE, fill_opacity=0.3)
        face.move_to(painting.get_center() + UP*0.8)
        
        # 添加两只眼睛
        left_eye = Dot(radius=0.05, color=BLACK)
        right_eye = Dot(radius=0.05, color=BLACK)
        left_eye.move_to(face.get_center() + LEFT*0.15 + UP*0.05)
        right_eye.move_to(face.get_center() + RIGHT*0.15 + UP*0.05)
        
        # 添加微笑
        smile = Arc(
            radius=0.2,
            start_angle=-2*PI/3,
            angle=PI/3,
            color=BLACK,
            stroke_width=2
        )
        smile.move_to(face.get_center() + DOWN*0.15)
        
        body = Ellipse(width=1.5, height=2, color=WHITE, fill_opacity=0.3)
        body.move_to(painting.get_center() + DOWN*0.5)
        
        portrait = VGroup(painting, face, left_eye, right_eye, smile, body)
        
        painting_label = Text("《蒙娜丽莎》", font_size=20, color=WHITE)
        painting_label.next_to(painting, DOWN, buff=0.3)
        
        self.play(Create(portrait), Write(painting_label))
        
        # 显示黄金分割线
        phi = (1 + np.sqrt(5)) / 2
        
        # 垂直黄金分割线
        v_line1 = DashedLine(
            painting.get_corner(UL) + RIGHT * 4 / phi,
            painting.get_corner(DL) + RIGHT * 4 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.1
        )
        v_line2 = DashedLine(
            painting.get_corner(UR) + LEFT * 4 / phi,
            painting.get_corner(DR) + LEFT * 4 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.1
        )
        
        # 水平黄金分割线
        h_line1 = DashedLine(
            painting.get_corner(UL) + DOWN * 5.5 / phi,
            painting.get_corner(UR) + DOWN * 5.5 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.1
        )
        h_line2 = DashedLine(
            painting.get_corner(DL) + UP * 5.5 / phi,
            painting.get_corner(DR) + UP * 5.5 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.1
        )
        
        golden_lines = VGroup(v_line1, v_line2, h_line1, h_line2)
        
        # 标记眼睛位于黄金点
        eye_markers = VGroup()
        left_eye_marker = Circle(radius=0.1, color=RED, stroke_width=2)
        left_eye_marker.move_to(left_eye.get_center())
        right_eye_marker = Circle(radius=0.1, color=RED, stroke_width=2)
        right_eye_marker.move_to(right_eye.get_center())
        eye_markers.add(left_eye_marker, right_eye_marker)
        
        self.play(Create(golden_lines))
        self.play(Create(eye_markers))
        
        # 说明文字
        explanation = VGroup(
            Text("双眼位于黄金分割线上", font_size=22, color=YELLOW),
            Text("面部中心符合黄金比例", font_size=22, color=YELLOW),
            Text("构图平衡遵循黄金法则", font_size=22, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(RIGHT*2.5)
        
        for exp in explanation:
            self.play(Write(exp), run_time=0.8)
        
        self.wait(2)
        
        # 第二个例子：帕特农神庙
        self.play(
            FadeOut(portrait),
            FadeOut(painting_label),
            FadeOut(golden_lines),
            FadeOut(eye_markers),
            FadeOut(explanation)
        )
        
        # 创建神庙简化图
        temple_base = Rectangle(width=6, height=0.3, color=GRAY, fill_opacity=0.5)
        temple_base.shift(DOWN * 2.5)
        
        temple_roof = Polygon(
            [-3.2, -0.8, 0],
            [3.2, -0.8, 0],
            [0, 0.5, 0],
            color=GRAY,
            fill_opacity=0.5
        )
        
        # 柱子
        columns = VGroup()
        for i in range(8):
            column = Rectangle(
                width=0.3,
                height=2.5,
                color=GRAY_B,
                fill_opacity=0.7,
                stroke_width=1
            )
            column.shift(LEFT*2.8 + RIGHT*i*0.8 + DOWN*1.65)
            columns.add(column)
        
        temple = VGroup(temple_base, columns, temple_roof)
        
        temple_label = Text("帕特农神庙", font_size=20, color=WHITE)
        temple_label.next_to(temple_base, DOWN, buff=0.5)
        
        self.play(Create(temple), Write(temple_label))
        
        # 黄金矩形框架
        golden_rect = Rectangle(
            width=6,
            height=6/phi,
            color=GOLD,
            stroke_width=3
        )
        golden_rect.move_to(temple.get_center())
        
        self.play(Create(golden_rect))
        
        proportion_text = Text(
            "完美的黄金矩形比例",
            font_size=24,
            color=YELLOW
        ).to_edge(DOWN).shift(UP * 0.5)
        
        self.play(Write(proportion_text))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(temple),
            FadeOut(temple_label),
            FadeOut(golden_rect),
            FadeOut(proportion_text)
        )
    
    def show_photography_composition(self):
        """摄影构图法则 - 2:20-3:00"""
        title = Text("摄影中的黄金构图", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建相机取景框
        viewfinder = Rectangle(
            width=6,
            height=4,
            color=WHITE,
            stroke_width=3
        )
        
        # 创建简洁的风景场景
        # 天空背景
        sky = Rectangle(
            width=6,
            height=4,
            color=BLUE_E,
            fill_opacity=0.2,
            stroke_width=0
        )
        sky.move_to(viewfinder.get_center())
        
        # 地面
        ground = Polygon(
            viewfinder.get_corner(DL),
            viewfinder.get_corner(DR),
            viewfinder.get_corner(DR) + UP * 1.2,
            viewfinder.get_corner(DL) + UP * 1.2,
            color=GREEN,
            fill_opacity=0.4,
            stroke_width=0
        )
        
        # 山脉（简化版）
        mountain = Polygon(
            viewfinder.get_corner(DL) + RIGHT * 1,
            viewfinder.get_corner(DL) + RIGHT * 2.5 + UP * 1.8,
            viewfinder.get_corner(DL) + RIGHT * 4 + UP * 0.8,
            viewfinder.get_corner(DL) + RIGHT * 5.5 + UP * 1.5,
            viewfinder.get_corner(DR),
            viewfinder.get_corner(DL) + RIGHT * 6,
            viewfinder.get_corner(DL) + RIGHT * 1,
            color=GRAY_D,
            fill_opacity=0.6,
            stroke_width=0
        )
        
        # 太阳（主体元素）
        sun = Circle(
            radius=0.25,
            color=YELLOW,
            fill_opacity=1
        )
        sun.move_to(viewfinder.get_center())  # 初始在中心
        
        # 组装场景
        scene_elements = VGroup(sky, ground, mountain, sun)
        
        self.play(Create(viewfinder))
        self.play(FadeIn(scene_elements))
        
        # 步骤1：展示三分法
        step1_text = Text("步骤1：三分法构图", font_size=24, color=WHITE)
        step1_text.next_to(viewfinder, RIGHT, buff=0.8)
        self.play(Write(step1_text))
        
        # 三分法网格
        third_lines = VGroup()
        for i in [1, 2]:
            v_line = DashedLine(
                viewfinder.get_corner(UL) + RIGHT * i * 2,
                viewfinder.get_corner(DL) + RIGHT * i * 2,
                color=GRAY,
                stroke_width=1,
                dash_length=0.05
            )
            h_line = DashedLine(
                viewfinder.get_corner(UL) + DOWN * i * 4/3,
                viewfinder.get_corner(UR) + DOWN * i * 4/3,
                color=GREY,
                stroke_width=1,
                dash_length=0.05
            )
            third_lines.add(v_line, h_line)
        
        self.play(Create(third_lines))
        
        # 移动太阳到三分点
        third_point = viewfinder.get_corner(UL) + RIGHT * 4 + DOWN * 4/3
        self.play(sun.animate.move_to(third_point))
        self.wait(1)
        
        # 步骤2：黄金分割更精确
        self.play(FadeOut(step1_text))
        step2_text = Text("步骤2：黄金分割更精确", font_size=24, color=WHITE)
        step2_text.next_to(viewfinder, RIGHT, buff=0.8)
        self.play(Write(step2_text))
        
        # 黄金分割网格
        phi = (1 + np.sqrt(5)) / 2
        golden_lines = VGroup()
        
        # 垂直黄金线
        golden_v1 = DashedLine(
            viewfinder.get_corner(UL) + RIGHT * 6 / phi,
            viewfinder.get_corner(DL) + RIGHT * 6 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.05
        )
        golden_v2 = DashedLine(
            viewfinder.get_corner(UR) + LEFT * 6 / phi,
            viewfinder.get_corner(DR) + LEFT * 6 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.05
        )
        
        # 水平黄金线
        golden_h1 = DashedLine(
            viewfinder.get_corner(UL) + DOWN * 4 / phi,
            viewfinder.get_corner(UR) + DOWN * 4 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.05
        )
        golden_h2 = DashedLine(
            viewfinder.get_corner(DL) + UP * 4 / phi,
            viewfinder.get_corner(DR) + UP * 4 / phi,
            color=GOLD,
            stroke_width=2,
            dash_length=0.05
        )
        
        golden_lines = VGroup(golden_v1, golden_v2, golden_h1, golden_h2)
        
        self.play(
            Transform(third_lines, golden_lines),
            run_time=1
        )
        
        # 标记四个黄金点
        golden_points = VGroup()
        golden_positions = [
            viewfinder.get_corner(UL) + RIGHT * 6 / phi + DOWN * 4 / phi,
            viewfinder.get_corner(UR) + LEFT * 6 / phi + DOWN * 4 / phi,
            viewfinder.get_corner(DL) + RIGHT * 6 / phi + UP * 4 / phi,
            viewfinder.get_corner(DR) + LEFT * 6 / phi + UP * 4 / phi
        ]
        
        for pos in golden_positions:
            point = Dot(pos, radius=0.08, color=RED)
            golden_points.add(point)
        
        self.play(Create(golden_points))
        
        # 移动太阳到黄金点
        golden_point = golden_positions[1]  # 右上黄金点
        self.play(sun.animate.move_to(golden_point))
        
        # 调整地平线到黄金分割线
        new_ground = Polygon(
            viewfinder.get_corner(DL),
            viewfinder.get_corner(DR),
            viewfinder.get_corner(DR) + UP * 4 * (1 - 1/phi),
            viewfinder.get_corner(DL) + UP * 4 * (1 - 1/phi),
            color=GREEN,
            fill_opacity=0.4,
            stroke_width=0
        )
        
        self.play(Transform(ground, new_ground))
        self.wait(1)
        
        # 步骤3：黄金螺旋引导
        self.play(
            FadeOut(step2_text),
            FadeOut(golden_points),
            FadeOut(third_lines)
        )
        
        step3_text = Text("步骤3：螺旋引导视线", font_size=24, color=WHITE)
        step3_text.next_to(viewfinder, RIGHT, buff=0.8)
        self.play(Write(step3_text))
        
        # 清理场景，准备螺旋演示
        self.play(FadeOut(scene_elements))
        
        # 创建新的构图示例
        spiral = self.create_golden_spiral()
        spiral.move_to(viewfinder.get_center())
        spiral.scale(0.8)
        
        # 螺旋引导线演示 - 纯净的螺旋效果
        
        # 创建引导线（简洁的连接线）
        river_points = []
        for i in range(4):
            if i < 3:
                river_points.append(spiral[i].get_center())
            else:
                river_points.append(spiral[3].get_end())
        
        # 简单的连接线
        river = VMobject()
        river.set_points_smoothly(river_points)
        river.set_stroke(color=BLUE_C, width=3, opacity=0.6)
        
        self.play(Create(spiral))
        self.play(Create(river))
        
        # 演示螺旋引导作用
        eye_dot = Dot(radius=0.08, color=RED)
        eye_dot.move_to(spiral[0].get_start())
        
        spiral_text = Text("螺旋引导视线流动", font_size=24, color=YELLOW)
        spiral_text.next_to(viewfinder, DOWN, buff=0.3)
        
        self.play(
            FadeIn(eye_dot),
            Write(spiral_text)
        )
        
        # 视线沿螺旋移动
        for i in range(1, 4):
            target_point = spiral[i].get_center()
            self.play(
                eye_dot.animate.move_to(target_point),
                run_time=0.8
            )
        
        # 到达螺旋终点
        self.play(
            eye_dot.animate.move_to(spiral[3].get_end()),
            run_time=0.8
        )
        
        # 最终效果
        self.play(
            eye_dot.animate.scale(2).set_opacity(0),
            spiral_text.animate.set_color(GOLD),
            run_time=1
        )
        
        final_text = Text(
            "黄金螺旋自然引导视线流动",
            font_size=28,
            color=GOLD
        ).next_to(viewfinder, DOWN, buff=0.8)
        
        self.play(Write(final_text))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(viewfinder),
            FadeOut(spiral),
            FadeOut(river),
            FadeOut(step3_text),
            FadeOut(spiral_text),
            FadeOut(final_text)
        )
    
    def show_practical_application(self):
        """实践应用 - 3:00-3:30"""
        title = Text("创造你的黄金构图", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建更直观的设计示例
        examples = VGroup()
        
        # 1. Logo设计 - 苹果Logo风格
        logo_frame = Square(side_length=2.5, color=BLUE, stroke_width=2)
        
        # 黄金分割辅助线
        phi = (1 + np.sqrt(5)) / 2
        logo_v_line = DashedLine(
            logo_frame.get_top() + LEFT * 2.5 / phi,
            logo_frame.get_bottom() + LEFT * 2.5 / phi,
            color=BLUE_E,
            stroke_width=1,
            dash_length=0.05
        )
        logo_h_line = DashedLine(
            logo_frame.get_left() + UP * 2.5 / phi,
            logo_frame.get_right() + UP * 2.5 / phi,
            color=BLUE_E,
            stroke_width=1,
            dash_length=0.05
        )
        
        # 在黄金点放置主要元素
        apple_shape = Circle(radius=0.4, color=BLUE, fill_opacity=0.8)
        apple_shape.move_to(logo_frame.get_center() + RIGHT * 1.25 / phi + UP * 1.25 / phi)
        
        # 文字放在另一个黄金区域
        logo_text = Text("Brand", font_size=16, color=BLUE)
        logo_text.move_to(logo_frame.get_center() + LEFT * 0.8 + DOWN * 0.8)
        
        logo_group = VGroup(logo_frame, logo_v_line, logo_h_line, apple_shape, logo_text)
        logo_group.shift(LEFT * 4.5 + UP * 1)
        logo_label = Text("Logo设计", font_size=16, color=WHITE)
        logo_desc = Text("主元素在黄金点", font_size=12, color=GRAY)
        logo_label.next_to(logo_group, DOWN, buff=0.2)
        logo_desc.next_to(logo_label, DOWN, buff=0.1)
        examples.add(VGroup(logo_group, logo_label, logo_desc))
        
        # 2. 网页布局 - 黄金分割布局
        web_frame = Rectangle(width=3.5, height=2.5, color=GREEN, stroke_width=2)
        
        # 头部 - 黄金分割
        header = Rectangle(
            width=3.5, 
            height=2.5/phi, 
            color=GREEN, 
            fill_opacity=0.3,
            stroke_width=1
        )
        header.move_to(web_frame.get_top() + DOWN * 1.25/phi)
        header_text = Text("Header", font_size=12, color=WHITE)
        header_text.move_to(header.get_center())
        
        # 侧边栏 - 黄金分割
        sidebar = Rectangle(
            width=3.5/phi, 
            height=2.5*(1-1/phi), 
            color=GREEN_E, 
            fill_opacity=0.3,
            stroke_width=1
        )
        sidebar.move_to(web_frame.get_left() + RIGHT * 1.75/phi + DOWN * (1.25/phi + 1.25*(1-1/phi)/2))
        sidebar_text = Text("Menu", font_size=10, color=WHITE)
        sidebar_text.move_to(sidebar.get_center())
        
        # 主内容区
        content = Rectangle(
            width=3.5*(1-1/phi),
            height=2.5*(1-1/phi),
            color=GREEN_C,
            fill_opacity=0.2,
            stroke_width=1
        )
        content.next_to(sidebar, RIGHT, buff=0)
        content_text = Text("Content", font_size=10, color=WHITE)
        content_text.move_to(content.get_center())
        
        web_group = VGroup(web_frame, header, header_text, sidebar, sidebar_text, content, content_text)
        web_group.shift(UP * 1)
        web_label = Text("网页布局", font_size=16, color=WHITE)
        web_desc = Text("1:0.618 完美比例", font_size=12, color=GRAY)
        web_label.next_to(web_group, DOWN, buff=0.2)
        web_desc.next_to(web_label, DOWN, buff=0.1)
        examples.add(VGroup(web_group, web_label, web_desc))
        
        # 3. 海报设计 - 视觉焦点
        poster_frame = Rectangle(width=2.5, height=3.5, color=ORANGE, stroke_width=2)
        
        # 黄金螺旋
        poster_spiral = self.create_golden_spiral()
        poster_spiral.scale(0.3)
        poster_spiral.move_to(poster_frame.get_center())
        poster_spiral.set_color(ORANGE)
        
        # 标题在上方黄金位置
        poster_title = Rectangle(
            width=2,
            height=0.3,
            color=ORANGE,
            fill_opacity=0.5
        )
        poster_title.move_to(poster_frame.get_center() + UP * 3.5 / phi / 2)
        title_text = Text("TITLE", font_size=12, color=WHITE)
        title_text.move_to(poster_title.get_center())
        
        # 主视觉元素在螺旋中心
        focal_star = Star(
            outer_radius=0.4, 
            color=ORANGE, 
            fill_opacity=0.8,
            n=5
        )
        focal_star.move_to(poster_frame.get_center() + RIGHT * 0.3 + DOWN * 0.2)
        
        # 文字信息在下方
        info_box = Rectangle(
            width=1.5,
            height=0.8,
            color=ORANGE,
            fill_opacity=0.2
        )
        info_box.move_to(poster_frame.get_bottom() + UP * 0.6)
        
        poster_group = VGroup(poster_frame, poster_spiral, poster_title, title_text, focal_star, info_box)
        poster_group.shift(RIGHT * 4.5 + UP * 0.5)
        poster_label = Text("海报设计", font_size=16, color=WHITE)
        poster_desc = Text("螺旋聚焦视线", font_size=12, color=GRAY)
        poster_label.next_to(poster_group, DOWN, buff=0.2)
        poster_desc.next_to(poster_label, DOWN, buff=0.1)
        examples.add(VGroup(poster_group, poster_label, poster_desc))
        
        # 动画展示
        for i, example in enumerate(examples):
            self.play(
                Create(example[0][0]),  # 外框
                run_time=0.5
            )
            # 展示内部元素
            for element in example[0][1:]:
                self.play(FadeIn(element), run_time=0.3)
            # 展示标签
            self.play(Write(example[1]), Write(example[2]), run_time=0.5)
        
        self.wait(2)
        
        # 设计原则总结
        self.play(FadeOut(examples))
        
        principles = VGroup(
            Text("黄金分割不是规则，而是工具", font_size=24, color=YELLOW),
            Text("平衡、和谐、引导视线", font_size=24, color=YELLOW),
            Text("数学之美，艺术之魂", font_size=28, color=GOLD)
        ).arrange(DOWN, buff=0.4)
        principles.move_to(ORIGIN)
        
        for principle in principles:
            self.play(Write(principle), run_time=1)
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(principles)
        )
    
    def create_golden_spiral(self):
        """创建黄金螺旋辅助函数"""
        phi = (1 + np.sqrt(5)) / 2
        spiral_parts = VGroup()
        
        # 创建由多个四分之一圆组成的螺旋
        radii = [2, 2/phi, 2/phi**2, 2/phi**3, 2/phi**4]
        centers = [
            ORIGIN,
            RIGHT * 2 * (1 - 1/phi),
            RIGHT * 2 * (1 - 1/phi) + UP * 2 * (1/phi - 1/phi**2),
            RIGHT * 2 * (1 - 1/phi - 1/phi**2) + UP * 2 * (1/phi - 1/phi**2),
            RIGHT * 2 * (1 - 1/phi - 1/phi**2) + UP * 2 * (1/phi - 1/phi**2 - 1/phi**3)
        ]
        start_angles = [0, PI/2, PI, -PI/2, 0]
        
        for radius, center, start_angle in zip(radii, centers, start_angles):
            arc = Arc(
                radius=radius,
                start_angle=start_angle,
                angle=PI/2,
                arc_center=center,
                color=GOLD,
                stroke_width=3
            )
            spiral_parts.add(arc)
        
        return spiral_parts
    
    def show_ending(self):
        """结尾 - 3:30-4:00"""
        # 总结
        summary_lines = [
            Text("黄金矩形——几何之美", font_size=36, color=WHITE),
            Text("从古典艺术到现代设计", font_size=36, color=WHITE),
            Text("数学法则创造视觉和谐", font_size=36, color=WHITE),
            Text("美，有规律可循", font_size=42, color=GOLD)
        ]
        summary = VGroup(*summary_lines).arrange(DOWN, buff=0.5)
        
        for line in summary_lines:
            self.play(Write(line), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(summary))
        
        # 下期预告
        next_episode = VGroup(
            Text("下期预告", font_size=36, color=YELLOW),
            Text("人体比例中的1.618", font_size=32, color=WHITE),
            Text("探索完美身材的数学密码", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(next_episode[0]), run_time=1)
        self.play(FadeIn(next_episode[1], shift=UP), run_time=1)
        self.play(FadeIn(next_episode[2], shift=UP), run_time=1)
        
        # 订阅提醒
        subscribe = Text("喜欢请三连支持！", font_size=32, color=RED)
        subscribe.next_to(next_episode, DOWN, buff=1)
        
        self.play(Write(subscribe))
        self.wait(3)