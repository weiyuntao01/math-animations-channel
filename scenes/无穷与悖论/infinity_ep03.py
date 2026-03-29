"""
INF_EP03: 加百列的号角 (Gabriel's Horn) / 托里拆利小号
体积有限 vs 表面积无限：画家的悖论
"""

from manim import *
import numpy as np

# --- 颜色定义 ---
INF_PURPLE = "#7C3AED"   # 神秘紫
INF_GOLD = "#FBBF24"     # 无穷金
INF_BLUE = "#3B82F6"     # 体积 (油漆)
INF_RED = "#EF4444"      # 表面积 (刷墙)
INF_GREEN = "#10B981"    # 数学解
INF_GRAY = "#6B7280"     # 坐标轴/背景
BG_COLOR = "#0F172A"     # 深蓝灰背景

class InfinityEP03(Scene):
    """无穷系列 EP03：加百列的号角"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场
        self.intro_transition()
        
        # 2. 形状构建：从双曲线到号角
        # 返回 axes_group 用于后续操作
        axes_group, horn_curves = self.construct_the_horn()
        
        # 3. 计算体积：收敛的积分
        self.calculate_volume(axes_group, horn_curves)
        
        # 4. 计算表面积：发散的积分
        self.calculate_surface_area(axes_group, horn_curves)
        
        # 5. 悖论解析：油漆悖论
        self.resolve_paradox()
        
        # 6. 结尾
        self.show_ending()

    def intro_transition(self):
        old_series = Text("EP02: 芝诺悖论 (无穷分割)", font_size=32, color=INF_GRAY).to_edge(UP)
        new_series = Text("EP03: 加百列的号角", font_size=54, color=INF_GOLD, weight=BOLD)
        subtitle = Text("Torricelli's Trumpet (托里拆利小号)", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        question = VGroup(
            Text("有没有一种物体...", font_size=24, color=WHITE),
            Text("你可以填满它，却永远刷不完它？", font_size=32, color=INF_PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0.3).next_to(subtitle, DOWN, buff=0.8)
        
        self.play(Write(question))
        self.wait(2)
        
        self.play(FadeOut(new_series), FadeOut(subtitle), FadeOut(question))

    def construct_the_horn(self):
        """构建号角的几何形状 (2D 剖面)"""
        
        # 左侧区域
        LEFT_ZONE = LEFT * 3.5
        
        title = Text("构造：旋转体", font_size=36, color=INF_GOLD).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 坐标系
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=5,
            axis_config={"color": INF_GRAY, "include_numbers": False},
            tips=False
        ).move_to(LEFT_ZONE)
        
        # 标记起点 x=1
        start_line = DashedLine(
            axes.c2p(1, -2), axes.c2p(1, 2), color=INF_GRAY
        )
        label_1 = MathTex("x=1").next_to(start_line, UP)
        
        self.play(Create(axes), Create(start_line), Write(label_1))
        
        # 2. 绘制曲线 y = 1/x
        curve_top = axes.plot(lambda x: 1/x, x_range=[1, 10], color=WHITE, stroke_width=3)
        func_label = MathTex("y = \\frac{1}{x}").next_to(curve_top, UP, buff=0.1).shift(RIGHT*1)
        
        self.play(Create(curve_top), Write(func_label))
        
        # 3. 旋转生成号角 (镜像曲线)
        curve_bottom = axes.plot(lambda x: -1/x, x_range=[1, 10], color=WHITE, stroke_width=3)
        
        rotate_text = Text("绕 X 轴旋转", font_size=24, color=INF_PURPLE).move_to(LEFT_ZONE + DOWN * 2.5)
        rotation_arrow = Arrow(
            start=UP, end=DOWN, path_arc=PI, color=INF_PURPLE
        ).move_to(axes.c2p(2, 0))
        
        self.play(Write(rotate_text), Create(rotation_arrow))
        self.play(TransformFromCopy(curve_top, curve_bottom))
        
        # 椭圆口 (模拟3D感)
        ellipse = Ellipse(width=0.2, height=axes.y_length/3 * (1/1)*2, color=WHITE) # height based on y=1 at x=1
        ellipse.move_to(axes.c2p(1, 0))
        
        self.play(Create(ellipse), FadeOut(rotation_arrow))
        
        # 打包
        axes_group = VGroup(axes, start_line, label_1, func_label, rotate_text, ellipse)
        horn_curves = VGroup(curve_top, curve_bottom)
        
        self.wait(1)
        
        # 清理标题，保留图形
        self.play(FadeOut(title))
        
        return axes_group, horn_curves

    def calculate_volume(self, axes_group, horn_curves):
        """计算体积：证明是有限的"""
        
        # 右侧逻辑区
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("计算体积 (Volume)", font_size=28, color=INF_BLUE, weight=BOLD)
        title.move_to(RIGHT_ZONE + UP * 2.5)
        
        # 1. 积分公式
        # V = integral (pi * y^2) dx
        formula_v = MathTex(
            r"V = \int_{1}^{\infty} \pi y^2 dx",
            r"= \int_{1}^{\infty} \pi \left(\frac{1}{x}\right)^2 dx"
        ).scale(0.8)
        formula_v.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(title))
        self.play(Write(formula_v))
        
        # 2. 填充动画 (模拟倒油漆)
        axes = axes_group[0]
        # 获取上下曲线之间的区域
        area = axes.get_area(horn_curves[0], x_range=[1, 10], bounded_graph=horn_curves[1], color=INF_BLUE, opacity=0.5)
        
        fill_text = Text("注入油漆...", font_size=20, color=INF_BLUE).next_to(axes, DOWN)
        
        self.play(Write(fill_text))
        self.play(Create(area), run_time=2)
        
        # 3. 计算结果
        calc_steps = VGroup(
            MathTex(r"= \pi \int_{1}^{\infty} x^{-2} dx"),
            MathTex(r"= \pi \left[ -\frac{1}{x} \right]_{1}^{\infty}"),
            MathTex(r"= \pi (0 - (-1))"),
            MathTex(r"= \pi", color=INF_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        
        calc_steps.next_to(formula_v, DOWN, buff=0.3)
        # 确保整体居中对齐
        calc_steps.shift(RIGHT * 0.5) 
        
        for step in calc_steps:
            self.play(Write(step), run_time=0.8)
            
        result_text = Text("体积是有限的！(π)", font_size=24, color=INF_GREEN)
        result_text.next_to(calc_steps, DOWN, buff=0.4)
        
        self.play(Write(result_text))
        self.wait(2)
        
        # 清理右侧，保留左侧图形（去掉填充，准备演示表面积）
        self.play(
            FadeOut(title), FadeOut(formula_v), FadeOut(calc_steps), FadeOut(result_text),
            FadeOut(area), FadeOut(fill_text)
        )

    def calculate_surface_area(self, axes_group, horn_curves):
        """计算表面积：证明是无限的"""
        
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("计算表面积 (Area)", font_size=28, color=INF_RED, weight=BOLD)
        title.move_to(RIGHT_ZONE + UP * 2.5)
        
        # 1. 积分公式
        # A = integral (2 * pi * y) * sqrt(1+y'^2) dx
        # 近似为 integral (2 * pi / x) dx
        formula_a = MathTex(
            r"A = \int_{1}^{\infty} 2\pi y \sqrt{1+(y')^2} dx"
        ).scale(0.7)
        formula_a.next_to(title, DOWN, buff=0.4)
        
        approx = MathTex(
            r"\approx \int_{1}^{\infty} \frac{2\pi}{x} dx"
        ).scale(0.8)
        approx.next_to(formula_a, DOWN, buff=0.2)
        
        self.play(Write(title))
        self.play(Write(formula_a))
        self.play(Write(approx))
        
        # 2. 描边动画 (模拟刷漆)
        axes = axes_group[0]
        paint_brush = Circle(radius=0.1, color=INF_RED, fill_opacity=1).move_to(axes.c2p(1, 1))
        
        trace_top = horn_curves[0].copy().set_color(INF_RED).set_stroke(width=4)
        trace_bottom = horn_curves[1].copy().set_color(INF_RED).set_stroke(width=4)
        
        paint_text = Text("尝试刷漆...", font_size=20, color=INF_RED).next_to(axes, DOWN)
        self.play(Write(paint_text), FadeIn(paint_brush))
        
        # 笔刷沿曲线运动
        self.play(
            Create(trace_top), 
            Create(trace_bottom),
            MoveAlongPath(paint_brush, horn_curves[0]),
            run_time=2,
            rate_func=linear
        )
        
        # 3. 计算结果
        calc_steps = VGroup(
            MathTex(r"= 2\pi [\ln x]_{1}^{\infty}"),
            MathTex(r"= 2\pi (\infty - 0)"),
            MathTex(r"= \infty", color=INF_RED)
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)
        
        calc_steps.next_to(approx, DOWN, buff=0.3)
        calc_steps.shift(RIGHT * 0.2)
        
        for step in calc_steps:
            self.play(Write(step), run_time=0.8)
            
        result_text = Text("表面积是无穷大！", font_size=24, color=INF_RED)
        result_text.next_to(calc_steps, DOWN, buff=0.4)
        
        self.play(Write(result_text))
        self.wait(2)
        
        # 清理所有
        self.play(FadeOut(Group(*self.mobjects)))

    def resolve_paradox(self):
            """解析悖论：画家的绝望 (布局重构版)"""
            
            # 1. 标题 (置顶)
            title = Text("画家的悖论 (Painter's Paradox)", font_size=36, color=INF_PURPLE).to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            # --- 视觉区域 (整体上移至 UP * 0.5) ---
            VISUAL_Y = UP * 0.5
            
            # 左边：桶装油漆
            bucket = VGroup(
                Rectangle(width=1.5, height=2, color=WHITE),
                Rectangle(width=1.5, height=1.8, fill_color=INF_BLUE, fill_opacity=0.8, stroke_width=0).shift(DOWN*0.1),
                Text("π", font_size=30).move_to(ORIGIN) # 简化内部文字，防止重叠
            )
            
            label_vol = Text("体积有限\n(装得满)", font_size=20, color=INF_BLUE).next_to(bucket, DOWN, buff=0.2)
            
            left_group = VGroup(bucket, label_vol).move_to(LEFT * 3.5 + VISUAL_Y)
            
            # 右边：刷子
            wall = Line(UP, DOWN, color=INF_RED, stroke_width=4)
            brush = Square(side_length=0.5, fill_color=INF_RED, fill_opacity=1).next_to(wall, RIGHT, buff=0)
            
            label_area = Text("表面积无限\n(刷不完)", font_size=20, color=INF_RED).next_to(wall, DOWN, buff=0.2)
            
            right_group = VGroup(wall, brush, label_area).move_to(RIGHT * 3.5 + VISUAL_Y)
            
            self.play(FadeIn(left_group), FadeIn(right_group))
            
            # --- 文字解释区域 (放置在底部) ---
            # 使用 arrange(DOWN) 默认居中，不使用 aligned_edge 参数
            explanation = VGroup(
                Text("为什么装满油漆却不能覆盖表面？", font_size=24, color=INF_GOLD),
                Text("1. 填满体积时，油漆层厚度随着变细也在变薄", font_size=20),
                Text("2. 刷漆意味着必须有固定厚度 (原子尺寸)", font_size=20),
                Text("3. 数学上厚度可无穷小，物理上不行", font_size=20, color=INF_GREEN)
            ).arrange(DOWN, buff=0.2)
            
            # 强制放在屏幕底部，留出 buff
            explanation.to_edge(DOWN, buff=0.5)
            
            self.play(Write(explanation))
            self.wait(4)
            
            self.play(FadeOut(Group(*self.mobjects)))
    def show_ending(self):
        summary = VGroup(
            Text("1. 收敛级数 vs 发散级数 的几何体现", font_size=26),
            Text("2. 1/x² 的下降速度够快，体积收敛", font_size=26),
            Text("3. 1/x 的下降速度太慢，面积发散", font_size=26, color=INF_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
        
        # 预告
        next_ep = Text("下期预告：分形几何", font_size=40, color=INF_GOLD)
        desc = Text("英国的海岸线到底有多长？\n有限面积内的无限周长。", font_size=24, color=INF_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)

