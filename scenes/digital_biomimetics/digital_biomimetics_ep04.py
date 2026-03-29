"""
数字仿生系列 第4集：心脏的混沌节律
Digital Biomimetics EP04: Chaotic Rhythm of the Heart

非线性振荡、螺旋波传播与心律失常的数学可视化
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple


# 复用系列通用色彩（与EP01-EP03保持一致）
BIO_CYAN = ManimColor("#00FFE5")
BIO_PURPLE = ManimColor("#8B5CF6")
BIO_GREEN = ManimColor("#00FF88")
BIO_BLUE = ManimColor("#007EFF")
BIO_YELLOW = ManimColor("#FFE500")
BIO_RED = ManimColor("#FF0066")
BIO_WHITE = ManimColor("#FFFFFF")
BIO_GRAY = ManimColor("#303030")

# EP04 专属色彩
HEART_RED = ManimColor("#FF2D55")
BLOOD_RED = ManimColor("#D7263D")
HEART_PINK = ManimColor("#FF7A8A")
ECG_GREEN = ManimColor("#00FF88")


# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class DigitalBiomimeticsEP04(Scene):
    """数字仿生系列 第4集"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        self.show_series_intro()
        self.answer_preview_question()
        self.cardiac_mathematics()
        self.heartbeat_visualization()
        self.spiral_wave_propagation()
        self.arrhythmia_chaos_transition()
        self.show_ending()

    def show_series_intro(self):
        """系列开场动画 - 心形背景 + 标题"""
        heart_bg = self.create_heart_background()
        heart_bg.set_opacity(0.18)
        self.play(Create(heart_bg), run_time=2)

        series_title = Text(
            "数字仿生",
            font_size=60,
            color=BIO_CYAN,
            weight=BOLD
        ).move_to([0, 1, 0])

        subtitle = Text(
            "DIGITAL BIOMIMETICS",
            font_size=24,
            color=BIO_WHITE,
            font="Arial"
        ).next_to(series_title, DOWN, buff=0.3)

        episode_text = Text(
            "第4集：心脏的混沌节律",
            font_size=34,
            color=HEART_RED
        ).move_to([0, -1.5, 0])

        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.play(Write(episode_text), run_time=1.5)

        self.play(
            series_title.animate.scale(1.1).set_color(HEART_PINK),
            rate_func=there_and_back,
            run_time=1
        )

        self.wait(5)
        self.play(
            FadeOut(series_title),
            FadeOut(subtitle),
            FadeOut(episode_text),
            FadeOut(heart_bg)
        )

    def create_heart_background(self):
        """创建由多层心形曲线组成的背景"""
        bg = VGroup()
        for i in range(6):
            scale = 0.5 + i * 0.25
            color = interpolate_color(HEART_PINK, BLOOD_RED, i/5)
            curve = ParametricFunction(
                lambda t: np.array(self._heart_param(t)) * scale,
                t_range=[0, 2*np.pi],
                color=color,
                stroke_width=2
            )
            curve.set_stroke(color=color, width=2, opacity=0.5 - i*0.06)
            bg.add(curve)
        return bg

    def answer_preview_question(self):
        """回应EP03预告：为何心律失常可用混沌理论解释"""
        title = Text("心律失常与混沌", font_size=TITLE_SIZE, color=HEART_RED)
        title.to_edge(UP, buff=0.5)

        q = Text(
            "为什么心律失常可以用混沌理论解释？",
            font_size=SUBTITLE_SIZE,
            color=BIO_YELLOW
        ).next_to(title, DOWN, buff=0.5)

        a = Text(
            "答案：心肌细胞是非线性耦合振荡器，",
            font_size=NORMAL_SIZE,
            color=BIO_WHITE
        )
        a2 = Text(
            "时空耦合与反馈可导致螺旋波、周期倍增与混沌。",
            font_size=NORMAL_SIZE,
            color=BIO_CYAN
        ).next_to(a, DOWN, buff=0.2)

        self.play(Write(title))
        self.play(Write(q))
        self.play(Write(a), Write(a2))
        self.wait(5)
        self.play(FadeOut(title), FadeOut(q), FadeOut(a), FadeOut(a2))

    def cardiac_mathematics(self):
        """展示核心方程：FitzHugh–Nagumo、扩散反应、混沌指标"""
        title = Text("心脏的数学密码", font_size=TITLE_SIZE, color=HEART_PINK)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        left = VGroup(
            Text("离子通道振荡 (FHN)", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"\dot v = v - \frac{v^3}{3} - w + I", font_size=28, color=BIO_CYAN),
            MathTex(r"\dot w = \frac{v + a - b w}{\tau}", font_size=28, color=BIO_CYAN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        right = VGroup(
            Text("螺旋波与扩散反应", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"\partial_t u = D \nabla^2 u + f(u)", font_size=28, color=BIO_GREEN),
            Text("混沌指标：Lyapunov λ > 0", font_size=SMALL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        cols = VGroup(left, right).arrange(RIGHT, buff=2.5)
        cols.next_to(title, DOWN, buff=0.6)

        for grp in [left, right]:
            for item in grp:
                self.play(Write(item), run_time=0.6)

        self.wait(5)
        self.play(FadeOut(title), FadeOut(cols))

    def heartbeat_visualization(self):
        """可视化：心形脉动 + ECG曲线同步"""
        self.clear()

        title = Text("生命形态 I：心跳与心电图", font_size=SUBTITLE_SIZE, color=HEART_RED)
        title.to_edge(UP, buff=0.5)

        # 时间追踪器
        t_tracker = ValueTracker(0.0)

        # 心形轮廓（脉动）
        def create_heart():
            t = t_tracker.get_value()
            base = ParametricFunction(
                lambda s: np.array(self._heart_param(s)),
                t_range=[0, 2*np.pi],
                color=HEART_RED,
                stroke_width=6
            )
            scale = 0.9 + 0.07 * np.sin(2*np.pi * (t * 1.1))
            base.scale(scale)
            base.set_sheen(0.5)
            base.set_sheen_direction(UP)
            return base

        heart = always_redraw(create_heart)

        # ECG 曲线（同步脉动）
        x_min, x_max = -6.5, 6.5
        baseline_y = -2.0

        def ecg_wave(x):
            period = 2.4
            x_mod = (x % period)
            p = 0.25 * np.exp(-((x_mod - 0.3) / 0.08) ** 2)
            q = -0.35 * np.exp(-((x_mod - 1.0) / 0.04) ** 2)
            r = 1.2 * np.exp(-((x_mod - 1.07) / 0.03) ** 2)
            s = -0.5 * np.exp(-((x_mod - 1.12) / 0.03) ** 2)
            t = 0.5 * np.exp(-((x_mod - 1.6) / 0.12) ** 2)
            return p + q + r + s + t

        def create_ecg_path():
            t = t_tracker.get_value()
            speed = 1.4
            xs = np.linspace(x_min, x_max, 600)
            points = []
            for x in xs:
                y = baseline_y + 0.7 * ecg_wave(x - speed * t)
                points.append([x, y, 0])
            path = VMobject()
            path.set_points_smoothly(points)
            path.set_stroke(ECG_GREEN, width=3)
            return path

        ecg = always_redraw(create_ecg_path)

        info = VGroup(
            Text("电活动 → 机械收缩", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("ECG与心肌脉动同步", font_size=SMALL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.2)
        info.to_edge(DOWN, buff=0.5)

        self.play(Write(title))
        self.add(heart, ecg)
        self.play(Write(info))

        self.play(
            t_tracker.animate.set_value(6 * np.pi),
            run_time=10,
            rate_func=linear
        )

        self.wait(5)
        self.play(FadeOut(title), FadeOut(heart), FadeOut(ecg), FadeOut(info))

    def spiral_wave_propagation(self):
        """可视化：心肌组织的螺旋波传播"""
        self.clear()

        title = Text("生命形态 II：心肌螺旋波", font_size=SUBTITLE_SIZE, color=BIO_CYAN)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        t_tracker = ValueTracker(0.0)

        def create_spiral_wave():
            t = t_tracker.get_value()
            num_points = 1400
            cx, cy = -1.0, -0.2
            particles = VGroup()
            for i in range(num_points):
                a = 2*np.pi * (i / 280) + 0.3 * np.sin(i * 0.013)
                r = 0.15 * (i / 30) + 0.2 * np.sin(i * 0.021)
                x = cx + r * np.cos(a + 0.5*t)
                y = cy + 0.7 * r * np.sin(a + 0.5*t)
                phase = a + r * 3.0 - 1.2 * t
                excite = 0.5 * (1 + np.sin(phase))
                excite = np.clip(excite, 0, 1)
                color = interpolate_color(BIO_BLUE, HEART_RED, excite)
                dot = Dot(point=[x, y, 0], radius=0.012, color=color, fill_opacity=0.55 + 0.35*excite)
                particles.add(dot)
            return particles

        spiral = always_redraw(create_spiral_wave)

        note = Text("螺旋波 = 再入性激动的空间图案", font_size=SMALL_SIZE, color=BIO_WHITE)
        note.to_edge(DOWN, buff=0.5)

        self.add(spiral)
        self.play(Write(note))
        self.play(
            t_tracker.animate.set_value(4*np.pi),
            run_time=10,
            rate_func=linear
        )

        self.wait(5)
        self.play(FadeOut(title), FadeOut(spiral), FadeOut(note))

    def arrhythmia_chaos_transition(self):
        """展示：从规则心律到混沌心律的过渡（对数映射示意）"""
        self.clear()

        title = Text("从规律到混沌：心律过渡", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        title.to_edge(UP, buff=0.5)

        axes = Axes(
            x_range=[3.2, 3.95, 0.25],
            y_range=[0, 1.0, 0.5],
            x_length=8,
            y_length=3.5,
            axis_config={"color": BIO_WHITE}
        ).move_to([0, -0.2, 0])

        x_label = Text("参数 r (兴奋性)", font_size=SMALL_SIZE, color=BIO_WHITE).next_to(axes, DOWN, buff=0.3)
        y_label = Text("稳态/周期点", font_size=SMALL_SIZE, color=BIO_WHITE).next_to(axes, LEFT, buff=0.3)

        self.play(Write(title))
        self.play(Create(axes), Write(x_label), Write(y_label))

        r_tracker = ValueTracker(3.2)

        def create_bifurcation_points():
            r = r_tracker.get_value()
            n_iter = 260
            x = 0.5
            pts = []
            for i in range(n_iter):
                x = r * x * (1 - x)
                if i > 160:
                    pts.append([r, x, 0])
            vg = VGroup()
            for p in pts:
                d = Dot(axes.c2p(p[0], p[1]), radius=0.015, color=interpolate_color(BIO_CYAN, HEART_RED, (p[1]))
                       ).set_opacity(0.8)
                vg.add(d)
            return vg

        bifurcation = always_redraw(create_bifurcation_points)

        caption = VGroup(
            Text("r↑ → 周期倍增 → 混沌 (λ > 0)", font_size=SMALL_SIZE, color=BIO_YELLOW),
            Text("对应心律：规整 → 早搏/室速 → 纤颤", font_size=SMALL_SIZE, color=BIO_CYAN)
        ).arrange(DOWN, buff=0.2)
        caption.to_edge(DOWN, buff=0.5)

        self.add(bifurcation)
        self.play(Write(caption))
        self.play(r_tracker.animate.set_value(3.92), run_time=8, rate_func=linear)

        self.wait(5)
        self.play(FadeOut(title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(bifurcation), FadeOut(caption))

    def show_ending(self):
        """结尾与下期预告"""
        self.clear()

        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=HEART_PINK)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))

        recap = VGroup(
            Text("✓ 心肌振荡的数学模型", font_size=NORMAL_SIZE),
            Text("✓ 螺旋波传播的可视化", font_size=NORMAL_SIZE),
            Text("✓ 从规律到混沌的过渡", font_size=NORMAL_SIZE),
            Text("✓ 心脏，是非线性之心", font_size=NORMAL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, 0.5, 0])

        for line in recap:
            self.play(Write(line), run_time=0.6)

        self.wait(5)
        self.play(FadeOut(recap_title), FadeOut(recap))

        philosophy = VGroup(
            Text("节律源自非线性", font_size=38, color=HEART_RED),
            Text("混沌孕育生命", font_size=38, color=BIO_PURPLE),
            Text("数学，倾听心跳", font_size=SUBTITLE_SIZE, color=BIO_CYAN)
        ).arrange(DOWN, buff=0.6)

        for line in philosophy:
            self.play(Write(line), run_time=1)

        self.wait(5)
        self.play(FadeOut(philosophy))

        self.show_next_episode_preview()

    def show_next_episode_preview(self):
        """下期预告"""
        preview_title = Text("下期预告", font_size=38, color=BIO_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))

        ep5_title = Text(
            "第5集：植物的分形密码",
            font_size=TITLE_SIZE,
            color=BIO_GREEN,
            weight=BOLD
        ).move_to([0, 1.5, 0])

        preview_content = VGroup(
            Text("L-System的生命生长", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("黄金角度与分形几何", font_size=SUBTITLE_SIZE, color=BIO_YELLOW),
            Text("从种子到森林的诗意", font_size=SUBTITLE_SIZE, color=BIO_GREEN)
        ).arrange(DOWN, buff=0.5).move_to([0, -0.5, 0])

        self.play(Write(ep5_title))
        for line in preview_content:
            self.play(Write(line), run_time=0.8)

        think_question = Text(
            "思考：一片叶子的角度，如何决定整棵树的命运？",
            font_size=20,
            color=BIO_YELLOW
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(think_question))

        self.wait(5)

        see_you = Text("下期再见！", font_size=38, color=BIO_WHITE).move_to(ORIGIN)

        # 最后的心形淡入
        final_heart = ParametricFunction(
            lambda s: np.array(self._heart_param(s)) * 0.6,
            t_range=[0, 2*np.pi],
            color=HEART_PINK,
            stroke_width=4
        ).set_opacity(0.35)

        self.play(
            FadeOut(preview_title),
            FadeOut(ep5_title),
            FadeOut(preview_content),
            FadeOut(think_question),
            Write(see_you)
        )
        self.play(Create(final_heart), run_time=1.5)
        self.wait(5)
        self.play(FadeOut(see_you), FadeOut(final_heart))

    def _heart_param(self, t: float) -> Tuple[float, float, float]:
        """标准心形参数方程，返回坐标三元组"""
        x = 16 * np.sin(t) ** 3
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
        x *= 0.06
        y *= 0.06
        return (x, y, 0.0)


