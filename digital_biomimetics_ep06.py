"""
数字仿生系列 第6集：蝴蝶效应的数学可视化
Digital Biomimetics EP06: Visualization of the Butterfly Effect

洛伦兹吸引子（2D相图）、对初值敏感性与混沌之美
"""

from manim import *
import numpy as np
from typing import List, Tuple


# 系列通用色彩
BIO_CYAN = ManimColor("#00FFE5")
BIO_PURPLE = ManimColor("#8B5CF6")
BIO_GREEN = ManimColor("#00FF88")
BIO_BLUE = ManimColor("#007EFF")
BIO_YELLOW = ManimColor("#FFE500")
BIO_RED = ManimColor("#FF0066")
BIO_WHITE = ManimColor("#FFFFFF")
BIO_GRAY = ManimColor("#303030")

# EP06 主题色
CHAOS_PURPLE = ManimColor("#9B59B6")
BUTTERFLY_ORANGE = ManimColor("#FFA64D")

# 字体尺寸
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class DigitalBiomimeticsEP06(Scene):
    """数字仿生系列 第6集"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        # 1. 系列开场
        self.show_series_intro()

        # 2. 回应EP05预告
        self.answer_preview_question()

        # 3. 混沌系统的数学本质
        self.chaos_mathematics()

        # 4. 生命形态 I：三维洛伦兹吸引子
        self.lorenz_attractor_scene()

        # 5. 生命形态 II：对初值敏感性的可视化
        self.sensitivity_scene()

        # 6. 结尾与预告
        self.show_ending()

    def show_series_intro(self):
        """系列开场动画 - 双翼光轨背景 + 标题"""
        bg = self.create_butterfly_background()
        bg.set_opacity(0.22)
        self.play(Create(bg), run_time=2)

        series_title = Text("数字仿生", font_size=60, color=BIO_CYAN, weight=BOLD).move_to([0, 1, 0])
        subtitle = Text("DIGITAL BIOMIMETICS", font_size=24, color=BIO_WHITE, font="Arial").next_to(series_title, DOWN, buff=0.3)
        episode_text = Text("第6集：蝴蝶效应的数学可视化", font_size=34, color=CHAOS_PURPLE).move_to([0, -1.5, 0])

        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.play(Write(episode_text), run_time=1.5)
        self.play(series_title.animate.scale(1.1).set_color(BUTTERFLY_ORANGE), rate_func=there_and_back, run_time=1)
        self.wait(4)
        self.play(FadeOut(series_title), FadeOut(subtitle), FadeOut(episode_text), FadeOut(bg))

    def create_butterfly_background(self) -> VGroup:
        """创建抽象蝴蝶翼状光轨背景（由两侧对称的曲线组成）"""
        group = VGroup()
        for side in [-1, 1]:
            for i in range(18):
                t = np.linspace(0, 2*np.pi, 200)
                a = 1.0 + 0.06 * i
                r = a * (1 + 0.4*np.sin(6*t))
                x = side * r * np.cos(t) * 0.35
                y = r * np.sin(t) * 0.22
                z = 0*t
                pts = np.vstack([x, y, z]).T
                curve = VMobject()
                curve.set_points_smoothly(pts)
                color = interpolate_color(CHAOS_PURPLE, BUTTERFLY_ORANGE, i/18)
                curve.set_stroke(color, width=1.2, opacity=0.35)
                group.add(curve)
        return group

    def answer_preview_question(self):
        """回应EP05预告：为何微小扰动能引发风暴？"""
        title = Text("蝴蝶效应：微小扰动，巨大差异", font_size=TITLE_SIZE, color=BUTTERFLY_ORANGE)
        title.to_edge(UP, buff=0.5)
        q = Text("为什么微小的初始差别会导致完全不同的结果？", font_size=SUBTITLE_SIZE, color=BIO_YELLOW).next_to(title, DOWN, buff=0.5)
        a = Text("答案：混沌系统对初值极端敏感 (Sensitive Dependence).", font_size=NORMAL_SIZE, color=BIO_CYAN).next_to(q, DOWN, buff=0.4)
        self.play(Write(title))
        self.play(Write(q))
        self.play(Write(a))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(q), FadeOut(a))

    def chaos_mathematics(self):
        """展示洛伦兹系统核心方程与典型参数"""
        title = Text("混沌的数学密码", font_size=TITLE_SIZE, color=CHAOS_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        left = VGroup(
            Text("洛伦兹系统", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"\dot x = \sigma (y - x)", font_size=30, color=BIO_CYAN),
            MathTex(r"\dot y = x(\rho - z) - y", font_size=30, color=BIO_CYAN),
            MathTex(r"\dot z = xy - \beta z", font_size=30, color=BIO_CYAN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        right = VGroup(
            Text("典型参数", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"\sigma = 10", font_size=28, color=BIO_GREEN),
            MathTex(r"\rho = 28", font_size=28, color=BIO_GREEN),
            MathTex(r"\beta = 8/3", font_size=28, color=BIO_GREEN),
            Text("特征：对初值敏感、轨道有界、非周期", font_size=SMALL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        cols = VGroup(left, right).arrange(RIGHT, buff=2.0)
        cols.next_to(title, DOWN, buff=0.6)

        for grp in [left, right]:
            for item in grp:
                self.play(Write(item), run_time=0.5)

        self.wait(4)
        self.play(FadeOut(title), FadeOut(cols))

    def lorenz_attractor_scene(self):
        """洛伦兹吸引子（2D相图 x-z）：相空间中的蝴蝶"""
        self.clear()

        title = Text("生命形态 I：洛伦兹吸引子（x-z相图）", font_size=SUBTITLE_SIZE, color=CHAOS_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 4.5, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": BIO_WHITE}
        )
        axes.shift(DOWN*0.2)
        self.play(Create(axes))

        # 生成洛伦兹轨迹点
        points = self._generate_lorenz_points(num_steps=3500, dt=0.01,
                                              sigma=10.0, rho=28.0, beta=8/3,
                                              start=np.array([0.1, 0.0, 0.0]))
        # 以 (x,z) 作二维相图
        scale = 0.08
        points2d = [axes.c2p(p[0]*scale, p[2]*scale) for p in points]

        t_tracker = ValueTracker(0.0)

        def partial_curve() -> VMobject:
            alpha = np.clip(t_tracker.get_value(), 0.0, 1.0)
            n = max(5, int(alpha * len(points2d)))
            curve = VMobject()
            curve.set_points_smoothly(points2d[:n])
            curve.set_stroke(color=CHAOS_PURPLE, width=2.5, opacity=0.9)
            curve.set_color_by_gradient(CHAOS_PURPLE, BIO_CYAN)
            return curve

        curve_obj = always_redraw(partial_curve)

        # 运动粒子（2D）
        def moving_dot():
            alpha = np.clip(t_tracker.get_value(), 0.0, 1.0)
            idx = int(alpha * (len(points2d)-1))
            d = Dot(points2d[idx], radius=0.05, color=BUTTERFLY_ORANGE, fill_opacity=1.0)
            return d

        dot_obj = always_redraw(moving_dot)

        info = Text("相空间中的‘蝴蝶’", font_size=SMALL_SIZE, color=BIO_WHITE)
        info.to_edge(DOWN, buff=0.5)

        self.add(curve_obj, dot_obj)
        self.play(Write(info))
        self.play(t_tracker.animate.set_value(1.0), run_time=12, rate_func=linear)
        self.wait(4)
        self.play(FadeOut(title), FadeOut(axes), FadeOut(info), FadeOut(curve_obj), FadeOut(dot_obj))

    def sensitivity_scene(self):
        """对初值敏感性：两条相近初值轨迹快速分离"""
        self.clear()

        title = Text("生命形态 II：对初值敏感性", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 4.5, 1],
            x_length=8,
            y_length=4,
            axis_config={"color": BIO_WHITE}
        )
        axes.shift(DOWN*0.2)
        self.play(Create(axes))

        base = np.array([0.1, 0.0, 0.0])
        eps = np.array([1e-6, 0.0, 0.0])
        p1 = self._generate_lorenz_points(2200, 0.01, 10.0, 28.0, 8/3, base)
        p2 = self._generate_lorenz_points(2200, 0.01, 10.0, 28.0, 8/3, base + eps)
        scale = 0.08
        # 使用 (x,z) 作二维相图
        p1v = [axes.c2p(px*scale, pz*scale) for (px, py, pz) in p1]
        p2v = [axes.c2p(px*scale, pz*scale) for (px, py, pz) in p2]

        t_tracker = ValueTracker(0.0)

        def curve_pair():
            alpha = np.clip(t_tracker.get_value(), 0.0, 1.0)
            n = max(5, int(alpha * len(p1v)))
            c1 = VMobject().set_points_smoothly(p1v[:n]).set_stroke(BIO_CYAN, width=2.2, opacity=0.95)
            c2 = VMobject().set_points_smoothly(p2v[:n]).set_stroke(BIO_RED, width=2.2, opacity=0.95)
            return VGroup(c1, c2)

        curves = always_redraw(curve_pair)

        def dots():
            alpha = np.clip(t_tracker.get_value(), 0.0, 1.0)
            i = int(alpha * (len(p1v)-1))
            d1 = Dot(p1v[i], radius=0.05, color=BIO_CYAN)
            d2 = Dot(p2v[i], radius=0.05, color=BIO_RED)
            return VGroup(d1, d2)

        moving_dots = always_redraw(dots)

        # 动态显示两条轨迹之间的距离（文本）
        def create_distance_text():
            alpha = np.clip(t_tracker.get_value(), 0.0, 1.0)
            idx = int(alpha * (len(p1) - 1))
            d = np.linalg.norm(np.array(p1[idx]) - np.array(p2[idx]))
            return Text(f"距离≈{d:.3f}", font_size=SMALL_SIZE, color=BIO_WHITE).to_edge(DOWN, buff=0.5)

        distance_text = always_redraw(create_distance_text)

        insight = Text("微小差异 → 巨大结果", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        insight.move_to([0, -2.3, 0])

        self.add(curves, moving_dots)
        self.play(Write(distance_text), Write(insight))
        self.play(t_tracker.animate.set_value(1.0), run_time=10, rate_func=linear)
        self.wait(4)
        self.play(FadeOut(title), FadeOut(axes), FadeOut(curves), FadeOut(moving_dots), FadeOut(distance_text), FadeOut(insight))

    def show_ending(self):
        """结尾与下期预告"""
        self.clear()

        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=CHAOS_PURPLE)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))

        recap = VGroup(
            Text("✓ 混沌：对初值敏感", font_size=NORMAL_SIZE),
            Text("✓ 洛伦兹吸引子的相图美学", font_size=NORMAL_SIZE),
            Text("✓ 蝴蝶效应：从微扰到风暴", font_size=NORMAL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, 0.5, 0])

        for line in recap:
            self.play(Write(line), run_time=0.6)

        self.wait(4)
        self.play(FadeOut(recap_title), FadeOut(recap))

        philosophy = VGroup(
            Text("规律之外，仍有秩序", font_size=38, color=BIO_PURPLE),
            Text("混沌，也是一种美", font_size=38, color=BIO_CYAN),
            Text("数学，捕捉不可预测的优雅", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.6)

        for line in philosophy:
            self.play(Write(line), run_time=1)

        self.wait(4)
        self.play(FadeOut(philosophy))

        self.show_next_episode_preview()

    def show_next_episode_preview(self):
        """下期预告：大脑的电光火花（EP07）"""
        preview_title = Text("下期预告", font_size=38, color=BIO_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))

        ep7_title = Text("第7集：大脑的电光火花", font_size=TITLE_SIZE, color=BIO_PURPLE, weight=BOLD).move_to([0, 1.5, 0])
        bullets = VGroup(
            Text("生物神经 × 人工神经", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("突触可塑性与学习", font_size=SUBTITLE_SIZE, color=BIO_GREEN),
            Text("脑电节律的可视化", font_size=SUBTITLE_SIZE, color=BIO_PURPLE)
        ).arrange(DOWN, buff=0.5).move_to([0, -0.5, 0])
        self.play(Write(ep7_title))
        for line in bullets:
            self.play(Write(line), run_time=0.8)

        q = Text("思考：真实大脑与AI的‘智能’，有何不同？", font_size=20, color=BIO_YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(q))
        self.wait(4)
        self.play(FadeOut(preview_title), FadeOut(ep7_title), FadeOut(bullets), FadeOut(q))

    # ---------- 工具函数 ----------
    def _generate_lorenz_points(self, num_steps: int, dt: float, sigma: float, rho: float, beta: float, start: np.ndarray) -> List[np.ndarray]:
        """欧拉法积分生成洛伦兹轨迹点（简单稳定，足够可视化）"""
        x, y, z = start.astype(float)
        pts: List[np.ndarray] = []
        for _ in range(num_steps):
            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z
            x += dx * dt
            y += dy * dt
            z += dz * dt
            pts.append(np.array([x, y, z]))
        return pts


