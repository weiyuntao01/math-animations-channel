from manim import *
import numpy as np

class ArchitectureMathematicsEP7(Scene):
    """建筑设计的数学美学 - 黄金分割系列 EP07"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：古埃及金字塔的数学
        self.show_pyramid_mathematics()
        
        # 第二部分：帕特农神庙的完美比例
        self.show_parthenon_proportions()
        
        # 第三部分：哥特式建筑的几何学
        self.show_gothic_geometry()
        
        # 第四部分：现代建筑的数学创新
        self.show_modern_architecture()
        
        # 第五部分：结构力学中的数学美
        self.show_structural_mathematics()
        
        # 结尾
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第七集：建筑设计的数学美学", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_pyramid_mathematics(self):
        """古埃及金字塔的数学 - 0:10-1:00"""
        title = Text("金字塔的数学密码", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建金字塔剖面图（基于胡夫金字塔的实际比例）
        # 原始高度：146.5米，底边：230.4米
        # 高度与半底边的比例 = 146.5 / 115.2 ≈ 1.272
        # 这个比例接近 4/π ≈ 1.273
        
        pyramid_height = 3
        pyramid_base = 4.7  # 保持实际比例
        
        # 金字塔三角形
        pyramid = Polygon(
            [-pyramid_base/2, 0, 0],  # 左下角
            [pyramid_base/2, 0, 0],   # 右下角
            [0, pyramid_height, 0],   # 顶点
            color=YELLOW,
            stroke_width=3,
            fill_opacity=0.1
        )
        pyramid.shift(DOWN * 0.5)
        
        self.play(Create(pyramid))
        
        # 标注尺寸
        # 高度标注
        height_line = Line(
            pyramid.get_bottom(),
            pyramid.get_top(),
            color=BLUE,
            stroke_width=2
        )
        height_label = Text("h", font_size=24, color=BLUE)
        height_label.next_to(height_line, RIGHT)
        
        # 底边标注
        base_line = Line(
            pyramid.get_corner(DL),
            pyramid.get_corner(DR),
            color=GREEN,
            stroke_width=2
        ).shift(DOWN * 0.3)
        base_label = Text("a", font_size=24, color=GREEN)
        base_label.next_to(base_line, DOWN)
        
        # 斜边标注
        slant_line = Line(
            pyramid.get_corner(DR),
            pyramid.get_top(),
            color=RED,
            stroke_width=2
        )
        
        self.play(
            Create(height_line), Write(height_label),
            Create(base_line), Write(base_label),
            Create(slant_line)
        )
        
        # 显示比例关系
        ratio_text = VGroup(
            MathTex(r"\frac{h}{a/2} = \frac{4}{\pi} \approx 1.273", font_size=28, color=WHITE),
            Text("斜边 : 高度 = φ : 1", font_size=24, color=GOLD),
            Text("底边周长 : 高度 = 2π : 1", font_size=24, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        ratio_text.shift(RIGHT * 4)
        
        self.play(Write(ratio_text[0]))
        self.wait(0.5)
        self.play(Write(ratio_text[1]))
        self.wait(0.5)
        self.play(Write(ratio_text[2]))
        
        # 说明文字
        explanation = Text(
            "金字塔蕴含π和φ，是巧合还是设计？",
            font_size=22,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(pyramid),
            FadeOut(height_line), FadeOut(height_label),
            FadeOut(base_line), FadeOut(base_label),
            FadeOut(slant_line), FadeOut(ratio_text),
            FadeOut(explanation)
        )
    
    def show_parthenon_proportions(self):
        """帕特农神庙的完美比例 - 1:00-1:50"""
        title = Text("帕特农神庙的黄金比例", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建简化的神庙正面图
        # 实际比例：宽30.88米，高13.72米（含基座）
        # 宽高比 ≈ 2.25，接近 9:4
        
        temple_width = 5
        temple_height = temple_width / 2.25
        
        # 基座
        base = Rectangle(
            width=temple_width + 0.4,
            height=0.3,
            color=GRAY,
            fill_opacity=0.5,
            stroke_width=2
        ).shift(DOWN * 1.5)
        
        # 主体矩形（代表立面）
        main_rect = Rectangle(
            width=temple_width,
            height=temple_height,
            color=WHITE,
            stroke_width=2
        ).shift(UP * (temple_height/2 - 1.35))
        
        # 三角形山花
        pediment = Polygon(
            main_rect.get_corner(UL) + LEFT * 0.2,
            main_rect.get_corner(UR) + RIGHT * 0.2,
            main_rect.get_top() + UP * 0.6,
            color=WHITE,
            stroke_width=2,
            fill_opacity=0.1
        )
        
        # 柱子（简化为线条）
        columns = VGroup()
        num_columns = 8  # 正面8根柱子
        column_spacing = temple_width / (num_columns - 1)
        
        for i in range(num_columns):
            column = Line(
                base.get_top() + LEFT * temple_width/2 + RIGHT * i * column_spacing,
                main_rect.get_bottom() + LEFT * temple_width/2 + RIGHT * i * column_spacing,
                color=WHITE,
                stroke_width=3
            )
            columns.add(column)
        
        temple = VGroup(base, columns, main_rect, pediment)
        
        self.play(Create(temple))
        
        # 黄金矩形叠加
        phi = (1 + np.sqrt(5)) / 2
        
        # 外部黄金矩形
        golden_rect_outer = Rectangle(
            width=temple_width + 0.4,
            height=(temple_width + 0.4) / phi,
            color=GOLD,
            stroke_width=2
        ).move_to(temple.get_center())
        
        # 内部黄金矩形（立面）
        golden_rect_inner = Rectangle(
            width=temple_width,
            height=temple_width / phi,
            color=GOLD,
            stroke_width=2,
            stroke_opacity=0.7
        ).move_to(main_rect.get_center())
        
        self.play(Create(golden_rect_outer), Create(golden_rect_inner))
        
        # 比例标注
        proportion_text = VGroup(
            Text("外轮廓：完美黄金矩形", font_size=20, color=GOLD),
            Text("立面比例：1 : φ", font_size=20, color=GOLD),
            Text("柱间距：遵循模数体系", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        proportion_text.shift(RIGHT * 4.5 + UP * 0.5)
        
        for text in proportion_text:
            self.play(Write(text), run_time=0.7)
        
        # 模数网格展示
        self.wait(1)
        
        # 显示网格
        grid_lines = VGroup()
        # 垂直线
        for i in range(5):
            line = DashedLine(
                golden_rect_inner.get_bottom() + RIGHT * (i - 2) * temple_width/4,
                golden_rect_inner.get_top() + RIGHT * (i - 2) * temple_width/4,
                color=BLUE,
                stroke_width=1,
                dash_length=0.1
            )
            grid_lines.add(line)
        
        # 水平线
        for i in range(3):
            line = DashedLine(
                golden_rect_inner.get_left() + UP * (i - 1) * temple_height/2,
                golden_rect_inner.get_right() + UP * (i - 1) * temple_height/2,
                color=BLUE,
                stroke_width=1,
                dash_length=0.1
            )
            grid_lines.add(line)
        
        self.play(Create(grid_lines))
        
        module_text = Text(
            "模数化设计：每个部分都是基本单位的倍数",
            font_size=22,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(module_text))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(temple),
            FadeOut(golden_rect_outer), FadeOut(golden_rect_inner),
            FadeOut(proportion_text), FadeOut(grid_lines),
            FadeOut(module_text)
        )
    
    def show_gothic_geometry(self):
        """哥特式建筑的几何学 - 1:50-2:30"""
        title = Text("哥特式建筑的几何密码", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建尖拱的几何构造
        arch_width = 3
        arch_center = ORIGIN + DOWN * 0.5
        
        # 基础圆
        left_circle = Circle(
            radius=arch_width/2,
            color=BLUE,
            stroke_width=2
        ).shift(arch_center + LEFT * arch_width/4)
        
        right_circle = Circle(
            radius=arch_width/2,
            color=BLUE,
            stroke_width=2
        ).shift(arch_center + RIGHT * arch_width/4)
        
        # 显示构造圆
        self.play(Create(left_circle), Create(right_circle))
        
        # 尖拱轮廓
        left_arc = Arc(
            radius=arch_width/2,
            start_angle=0,
            angle=PI/3,
            arc_center=left_circle.get_center(),
            color=RED,
            stroke_width=4
        )
        
        right_arc = Arc(
            radius=arch_width/2,
            start_angle=PI - PI/3,
            angle=PI/3,
            arc_center=right_circle.get_center(),
            color=RED,
            stroke_width=4
        )
        
        # 垂直支撑
        left_support = Line(
            arch_center + LEFT * arch_width/2 + DOWN * 0.5,
            arch_center + LEFT * arch_width/2,
            color=RED,
            stroke_width=4
        )
        
        right_support = Line(
            arch_center + RIGHT * arch_width/2 + DOWN * 0.5,
            arch_center + RIGHT * arch_width/2,
            color=RED,
            stroke_width=4
        )
        
        arch = VGroup(left_arc, right_arc, left_support, right_support)
        
        self.play(Create(arch))
        
        # 标注角度和比例
        # 尖拱顶点
        apex = arch_center + UP * (arch_width/2 * np.sin(PI/3))
        apex_dot = Dot(apex, color=YELLOW, radius=0.08)
        
        # 角度标注
        angle_arc = Arc(
            radius=0.5,
            start_angle=PI/6,
            angle=2*PI/3,
            arc_center=apex,
            color=YELLOW,
            stroke_width=2
        )
        angle_label = MathTex("120°", font_size=24, color=YELLOW)
        angle_label.next_to(apex, UP)
        
        self.play(
            Create(apex_dot),
            Create(angle_arc),
            Write(angle_label)
        )
        
        # 结构优势说明
        structure_text = VGroup(
            Text("尖拱的优势：", font_size=24, color=WHITE),
            Text("• 垂直传递荷载", font_size=20, color=WHITE),
            Text("• 减少侧推力", font_size=20, color=WHITE),
            Text("• 增加建筑高度", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        structure_text.shift(RIGHT * 3.5)
        
        self.play(Write(structure_text))
        
        # 力的传递示意
        force_arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                apex + DOWN * i * 0.3,
                apex + DOWN * (i + 1) * 0.3,
                color=GREEN,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.2
            )
            force_arrows.add(arrow)
        
        self.play(*[Create(arrow) for arrow in force_arrows])
        
        # 与半圆拱对比
        comparison_text = Text(
            "尖拱 vs 半圆拱：更高、更稳、更轻盈",
            font_size=22,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(comparison_text))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(left_circle), FadeOut(right_circle),
            FadeOut(arch), FadeOut(apex_dot), FadeOut(angle_arc),
            FadeOut(angle_label), FadeOut(structure_text),
            FadeOut(force_arrows), FadeOut(comparison_text)
        )
    
    def show_modern_architecture(self):
        """现代建筑的数学创新 - 2:30-3:20"""
        title = Text("现代建筑的数学创新", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 展示参数化设计
        subtitle = Text("参数化设计：数学方程生成形态", font_size=24, color=YELLOW)
        subtitle.shift(UP * 2)
        self.play(Write(subtitle))
        
        # 创建参数化曲面（简化版）
        def parametric_surface(u, v):
            """生成参数化曲面的点"""
            x = 2 * np.cos(u) * (1 + 0.3 * np.cos(v))
            y = 2 * np.sin(u) * (1 + 0.3 * np.cos(v))
            z = 0.5 * np.sin(v)
            return np.array([x, y, z])
        
        # 创建网格线
        grid_lines = VGroup()
        
        # U方向的线（经线）
        for v in np.linspace(0, 2*PI, 8):
            points = []
            for u in np.linspace(0, 2*PI, 20):
                point = parametric_surface(u, v)
                # 保持3D坐标，只是将z坐标投影到平面上
                points.append([point[0], point[1] - 0.5, 0])
            
            line = VMobject()
            line.set_points_smoothly(points)
            line.set_stroke(color=BLUE, width=1)
            grid_lines.add(line)
        
        # V方向的线（纬线）
        for u in np.linspace(0, 2*PI, 12):
            points = []
            for v in np.linspace(0, 2*PI, 20):
                point = parametric_surface(u, v)
                # 保持3D坐标，只是将z坐标投影到平面上
                points.append([point[0], point[1] - 0.5, 0])
            
            line = VMobject()
            line.set_points_smoothly(points)
            line.set_stroke(color=BLUE, width=1)
            grid_lines.add(line)
        
        grid_lines.scale(0.8)
        
        self.play(Create(grid_lines), run_time=2)
        
        # 参数方程
        equation = MathTex(
            r"\begin{cases} x = R\cos(u)(1 + a\cos(v)) \\ y = R\sin(u)(1 + a\cos(v)) \\ z = b\sin(v) \end{cases}",
            font_size=24,
            color=WHITE
        )
        equation.shift(RIGHT * 3.5 + UP * 0.5)
        
        self.play(Write(equation))
        
        # 实例说明
        examples = Text(
            "扎哈·哈迪德、盖里的流动建筑",
            font_size=20,
            color=WHITE
        ).shift(RIGHT * 4 + DOWN * 1)
        
        self.play(Write(examples))
        
        self.wait(1.5)
        
        # 转换到分形几何
        self.play(
            FadeOut(grid_lines), FadeOut(equation),
            FadeOut(examples), FadeOut(subtitle)
        )
        
        # 分形建筑
        fractal_subtitle = Text("分形几何：自相似的建筑美学", font_size=24, color=YELLOW)
        fractal_subtitle.shift(UP * 2)
        self.play(Write(fractal_subtitle))
        
        # 创建谢尔宾斯基三角形（3层）
        def create_sierpinski(level, size=3, position=ORIGIN):
            """创建谢尔宾斯基三角形"""
            if level == 0:
                triangle = Polygon(
                    position + UP * size * np.sqrt(3)/2,
                    position + DOWN * size * np.sqrt(3)/4 + LEFT * size/2,
                    position + DOWN * size * np.sqrt(3)/4 + RIGHT * size/2,
                    color=WHITE,
                    stroke_width=2,
                    fill_opacity=0.1
                )
                return VGroup(triangle)
            
            triangles = VGroup()
            # 递归创建三个子三角形
            new_size = size / 2
            positions = [
                position + UP * new_size * np.sqrt(3)/2,
                position + DOWN * new_size * np.sqrt(3)/4 + LEFT * new_size/2,
                position + DOWN * new_size * np.sqrt(3)/4 + RIGHT * new_size/2
            ]
            
            for pos in positions:
                triangles.add(*create_sierpinski(level - 1, new_size, pos))
            
            return triangles
        
        sierpinski = create_sierpinski(3).shift(LEFT * 2.5 + DOWN * 0.5)
        
        self.play(Create(sierpinski))
        
        # 分形维度说明
        dimension_text = VGroup(
            MathTex(r"D = \frac{\log N}{\log r}", font_size=24, color=WHITE),
            MathTex(r"D = \frac{\log 3}{\log 2} \approx 1.585", font_size=24, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        dimension_text.shift(RIGHT * 3 + UP * 0.5)
        
        self.play(Write(dimension_text))
        
        # 应用实例
        application = Text(
            "艾菲尔铁塔、悉尼歌剧院的分形特征",
            font_size=20,
            color=WHITE
        ).shift(RIGHT * 3 + DOWN * 1)
        
        self.play(Write(application))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(fractal_subtitle),
            FadeOut(sierpinski), FadeOut(dimension_text),
            FadeOut(application)
        )
    
    def show_structural_mathematics(self):
        """结构力学中的数学美 - 3:20-3:50"""
        title = Text("结构力学的数学优化", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 悬链线
        catenary_label = Text("悬链线：自然的完美曲线", font_size=24, color=YELLOW)
        catenary_label.shift(UP * 2)
        self.play(Write(catenary_label))
        
        # 绘制悬链线
        a = 1.5  # 悬链线参数
        catenary = FunctionGraph(
            lambda x: a * np.cosh(x/a) - a,
            x_range=[-2.5, 2.5],
            color=BLUE,
            stroke_width=3
        ).shift(DOWN * 0.5)
        
        # 支撑点
        left_support = Dot(catenary.get_start(), color=RED, radius=0.1)
        right_support = Dot(catenary.get_end(), color=RED, radius=0.1)
        
        self.play(Create(catenary), Create(left_support), Create(right_support))
        
        # 数学方程
        equation = MathTex(
            r"y = a\cosh\left(\frac{x}{a}\right)",
            font_size=28,
            color=WHITE
        )
        equation.shift(RIGHT * 3.5 + UP * 1)
        
        self.play(Write(equation))
        
        # 力的分布
        force_arrows = VGroup()
        num_arrows = 7
        for i in range(num_arrows):
            x = -2 + i * 4/(num_arrows-1)
            y = a * np.cosh(x/a) - a - 0.5
            arrow = Arrow(
                start=[x, y + 0.3, 0],
                end=[x, y, 0],
                color=GREEN,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.2
            )
            force_arrows.add(arrow)
        
        self.play(*[Create(arrow) for arrow in force_arrows])
        
        # 特性说明
        properties = VGroup(
            Text("• 纯张力，无弯矩", font_size=18, color=WHITE),
            Text("• 最小势能状态", font_size=18, color=WHITE),
            Text("• 倒置后成拱形", font_size=18, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        properties.shift(RIGHT * 3.5 + DOWN * 0.5)
        
        self.play(Write(properties))
        
        # 应用实例
        examples = Text(
            "圣路易斯拱门、高迪的圣家族大教堂",
            font_size=20,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(examples))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(catenary_label),
            FadeOut(catenary), FadeOut(left_support), FadeOut(right_support),
            FadeOut(equation), FadeOut(force_arrows),
            FadeOut(properties), FadeOut(examples)
        )
    
    def show_ending(self):
        """结尾 - 3:50-4:20"""
        # 总结
        summary_lines = [
            Text("建筑——凝固的数学诗篇", font_size=36, color=WHITE),
            Text("从金字塔到参数化设计", font_size=36, color=WHITE),
            Text("力与美的完美平衡", font_size=36, color=WHITE),
            Text("数学，建筑永恒的灵魂", font_size=42, color=GOLD)
        ]
        summary = VGroup(*summary_lines).arrange(DOWN, buff=0.5)
        
        for line in summary_lines:
            self.play(Write(line), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(summary))
        
        # 下期预告
        next_episode = VGroup(
            Text("下期预告", font_size=36, color=YELLOW),
            Text("股市技术分析中的斐波那契", font_size=32, color=WHITE),
            Text("当数学遇上金融", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(next_episode[0]), run_time=1)
        self.play(FadeIn(next_episode[1], shift=UP), run_time=1)
        self.play(FadeIn(next_episode[2], shift=UP), run_time=1)
        
        # 订阅提醒
        subscribe = Text("喜欢请三连支持！", font_size=32, color=RED)
        subscribe.next_to(next_episode, DOWN, buff=1)
        
        self.play(Write(subscribe))
        self.wait(3)