"""
数字仿生系列 第5集：植物的分形密码
Digital Biomimetics EP05: Fractal Codes of Plants

L-System 生长与黄金角度密植（Phyllotaxis）的高级可视化
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple, Dict


# 系列通用色彩
BIO_CYAN = ManimColor("#00FFE5")
BIO_PURPLE = ManimColor("#8B5CF6")
BIO_GREEN = ManimColor("#00FF88")
BIO_BLUE = ManimColor("#007EFF")
BIO_YELLOW = ManimColor("#FFE500")
BIO_RED = ManimColor("#FF0066")
BIO_WHITE = ManimColor("#FFFFFF")
BIO_GRAY = ManimColor("#303030")

# EP05 主题色
LEAF_GREEN = ManimColor("#36D399")
STEM_GREEN = ManimColor("#22A669")
FLOWER_GOLD = ManimColor("#F6C945")
EARTH_BROWN = ManimColor("#6B4F3A")

# 字体尺寸
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class DigitalBiomimeticsEP05(Scene):
    """数字仿生系列 第5集"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        self.show_series_intro()
        self.answer_preview_question()
        self.plant_mathematics()
        self.lsystem_growth_scene()
        self.phyllotaxis_scene()
        self.show_ending()

    def show_series_intro(self):
        """植物纹理背景 + 标题"""
        bg = self.create_leaf_background()
        bg.set_opacity(0.18)
        self.play(Create(bg), run_time=2)

        series_title = Text("数字仿生", font_size=60, color=BIO_CYAN, weight=BOLD).move_to([0, 1, 0])
        subtitle = Text("DIGITAL BIOMIMETICS", font_size=24, color=BIO_WHITE, font="Arial").next_to(series_title, DOWN, buff=0.3)
        episode_text = Text("第5集：植物的分形密码", font_size=34, color=LEAF_GREEN).move_to([0, -1.5, 0])

        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.play(Write(episode_text), run_time=1.5)
        self.play(series_title.animate.scale(1.1).set_color(STEM_GREEN), rate_func=there_and_back, run_time=1)
        self.wait(3)
        self.play(FadeOut(series_title), FadeOut(subtitle), FadeOut(episode_text), FadeOut(bg))

    def create_leaf_background(self):
        """叶脉样式的线性网络"""
        group = VGroup()
        rng = np.random.default_rng(7)
        for i in range(60):
            x = rng.uniform(-6.5, 6.5)
            y = rng.uniform(-3.5, 3.5)
            theta = rng.uniform(0, 2*np.pi)
            r = rng.uniform(0.8, 2.2)
            p1 = np.array([x, y, 0])
            p2 = p1 + r*np.array([np.cos(theta), np.sin(theta), 0])
            line = Line(p1, p2, color=STEM_GREEN, stroke_width=1, stroke_opacity=0.35)
            group.add(line)
            if rng.random() > 0.5:
                p3 = p1 + 0.6*r*np.array([np.cos(theta+0.6), np.sin(theta+0.6), 0])
                group.add(Line(p1, p3, color=LEAF_GREEN, stroke_width=0.8, stroke_opacity=0.25))
        return group

    def answer_preview_question(self):
        """承接EP04：叶序如何来自一个角度？"""
        title = Text("从心跳到生长：自然的几何", font_size=TITLE_SIZE, color=LEAF_GREEN)
        title.to_edge(UP, buff=0.5)
        q = Text("一片叶子的角度，如何决定一株植物的一生？", font_size=SUBTITLE_SIZE, color=BIO_YELLOW).next_to(title, DOWN, buff=0.5)
        self.play(Write(title))
        self.play(Write(q))
        a = Text("答案：黄金角度与分形生长。", font_size=NORMAL_SIZE, color=BIO_CYAN).next_to(q, DOWN, buff=0.4)
        self.play(Write(a))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(q), FadeOut(a))

    def plant_mathematics(self):
        """L-System 与 Phyllotaxis 数学本质"""
        title = Text("植物的数学密码", font_size=TITLE_SIZE, color=LEAF_GREEN)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        left = VGroup(
            Text("L-System：形式文法", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"G=(V,\omega,P)", font_size=30, color=BIO_CYAN),
            MathTex(r"\omega \Rightarrow P(\omega) \Rightarrow P^2(\omega) \dots", font_size=28, color=BIO_CYAN),
            Text("F: 前进, +α: 左转, -α: 右转", font_size=26, color=BIO_CYAN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        right = VGroup(
            Text("Phyllotaxis：黄金角度", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"\theta_k = k\, \alpha,\quad r_k = c\sqrt{k}", font_size=28, color=BIO_GREEN),
            MathTex(r"\alpha \approx 137.5^{\circ} = 2\pi\left(1-\frac{1}{\varphi}\right)", font_size=28, color=BIO_GREEN),
            MathTex(r"\varphi = \frac{1+\sqrt{5}}{2}", font_size=28, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        cols = VGroup(left, right).arrange(RIGHT, buff=2.2)
        cols.next_to(title, DOWN, buff=0.6)

        for grp in [left, right]:
            for item in grp:
                self.play(Write(item), run_time=0.5)

        insight = Text("分形规则 × 黄金角度 = 最优填充与输运", font_size=SUBTITLE_SIZE, color=FLOWER_GOLD)
        insight.to_edge(DOWN, buff=0.8)
        self.play(Write(insight))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(cols), FadeOut(insight))

    def lsystem_growth_scene(self):
        """L-System 植株生长：分支、叶片、风摆"""
        self.clear()
        title = Text("生命形态 I：分形生长", font_size=SUBTITLE_SIZE, color=LEAF_GREEN)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        t_tracker = ValueTracker(0.0)

        # L-system 规则（简单可视版）：
        # Axiom: F
        # Rules: F -> F[+F]F[-F]F
        # Angle: 22.5°
        axiom = "F"
        rules: Dict[str, str] = {"F": "F[+F]F[-F]F"}
        angle_deg = 22.5
        iterations = 4

        def rewrite(s: str) -> str:
            out = []
            for ch in s:
                out.append(rules.get(ch, ch))
            return "".join(out)

        seq = axiom
        for _ in range(iterations):
            seq = rewrite(seq)

        # 解释并生成几何（带风摆与叶片）
        step = 0.28
        base_angle = np.deg2rad(angle_deg)

        def build_geometry(progress: float) -> VGroup:
            stack = []
            pos = np.array([0.0, -3.0, 0.0])
            heading = np.array([0.0, 1.0, 0.0])
            group = VGroup()
            wind = 0.12 * np.sin(1.5 * t_tracker.get_value())

            max_draw = int(len(seq) * progress)
            for i, ch in enumerate(seq[:max_draw]):
                if ch == 'F':
                    new_pos = pos + step * heading
                    seg = Line(pos, new_pos, color=STEM_GREEN, stroke_width=3)
                    group.add(seg)
                    # 偶尔长叶
                    if i % 11 == 0:
                        leaf_dir = rotate_vector(heading, np.pi/2 + 0.5*wind)
                        leaf = VMobject(stroke_width=0)
                        p0 = new_pos
                        p1 = new_pos + 0.18 * heading + 0.10 * leaf_dir
                        p2 = new_pos + 0.28 * heading
                        p3 = new_pos + 0.18 * heading - 0.10 * leaf_dir
                        leaf.set_points_smoothly([p0, p1, p2, p3, p0])
                        leaf.set_fill(LEAF_GREEN, opacity=0.8)
                        group.add(leaf)
                    pos = new_pos
                elif ch == '+':
                    theta = base_angle + wind
                    heading = rotate_vector(heading, theta)
                elif ch == '-':
                    theta = -base_angle + wind
                    heading = rotate_vector(heading, theta)
                elif ch == '[':
                    stack.append((pos.copy(), heading.copy()))
                elif ch == ']':
                    if stack:
                        pos, heading = stack.pop()
            return group

        plant = always_redraw(lambda: build_geometry(progress=np.clip(t_tracker.get_value()/6.0, 0, 1)))

        ground = Line([-6.5, -3.0, 0], [6.5, -3.0, 0], color=EARTH_BROWN, stroke_width=4)
        self.add(plant, ground)
        self.play(t_tracker.animate.set_value(6.0), run_time=10, rate_func=lambda t: smooth(t))

        info = Text("分形规则 + 环境风摆 = 拟真生长", font_size=SMALL_SIZE, color=BIO_WHITE)
        info.to_edge(DOWN, buff=0.5)
        self.play(Write(info))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(info), FadeOut(plant), FadeOut(ground))

    def phyllotaxis_scene(self):
        """黄金角度密植可视化（动态参数 + 色彩分级 + 景深）"""
        self.clear()
        title = Text("生命形态 II：黄金角度密植", font_size=SUBTITLE_SIZE, color=FLOWER_GOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        t_tracker = ValueTracker(0.0)

        def create_phyllotaxis():
            t = t_tracker.get_value()
            n_points = 1600
            alpha = np.deg2rad(137.5 + 3.0*np.sin(0.3*t))  # 微调角度，展现鲁棒性
            c = 0.06
            vg = VGroup()
            for k in range(n_points):
                theta = k * alpha
                r = c * np.sqrt(k)
                x = r * np.cos(theta)
                y = r * np.sin(theta)
                depth = np.clip(k / n_points, 0, 1)
                color = interpolate_color(LEAF_GREEN, FLOWER_GOLD, depth)
                radius = 0.018 + 0.012*np.sin(0.8*t + k*0.03)
                dot = Dot(point=[x, y, 0], radius=radius, color=color, fill_opacity=0.85)
                vg.add(dot)
            # 外层花托柔光
            halo = Circle(radius=c*np.sqrt(n_points)+0.15, color=FLOWER_GOLD, stroke_width=2)
            halo.set_opacity(0.15)
            vg.add(halo)
            return vg

        phyl = always_redraw(create_phyllotaxis)
        subtitle = Text("鲁棒最优填充：角度扰动下依然均匀", font_size=SMALL_SIZE, color=BIO_WHITE)
        subtitle.to_edge(DOWN, buff=0.5)

        self.add(phyl)
        self.play(Write(subtitle))
        self.play(t_tracker.animate.set_value(8*np.pi), run_time=20, rate_func=linear)
        self.wait(3)
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(phyl))

    def show_ending(self):
        """结尾与下期预告"""
        self.clear()
        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=LEAF_GREEN)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))

        recap = VGroup(
            Text("✓ L-System 形式文法与分形生长", font_size=NORMAL_SIZE),
            Text("✓ 黄金角度密植（Phyllotaxis）", font_size=NORMAL_SIZE),
            Text("✓ 美学与最优化的统一", font_size=NORMAL_SIZE, color=FLOWER_GOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, 0.5, 0])

        for line in recap:
            self.play(Write(line), run_time=0.6)

        self.wait(3)
        self.play(FadeOut(recap_title), FadeOut(recap))

        philosophy = VGroup(
            Text("自然在最简单的规则里，藏着最高级的秩序", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("分形，是生命的语言", font_size=SUBTITLE_SIZE, color=LEAF_GREEN)
        ).arrange(DOWN, buff=0.6)

        for line in philosophy:
            self.play(Write(line), run_time=1)

        self.wait(3)
        self.play(FadeOut(philosophy))

        # 下期预告（与规划一致：蝴蝶效应/洛伦兹）
        preview_title = Text("下期预告", font_size=38, color=BIO_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))
        ep6_title = Text("第6集：蝴蝶效应的数学可视化", font_size=TITLE_SIZE, color=BIO_PURPLE, weight=BOLD).move_to([0, 1.5, 0])
        bullets = VGroup(
            Text("洛伦兹吸引子相空间", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("微扰如何放大成风暴", font_size=SUBTITLE_SIZE, color=BIO_YELLOW),
            Text("混沌的美学", font_size=SUBTITLE_SIZE, color=BIO_PURPLE)
        ).arrange(DOWN, buff=0.5).move_to([0, -0.5, 0])
        self.play(Write(ep6_title))
        for line in bullets:
            self.play(Write(line), run_time=0.8)
        q = Text("思考：你能预测下一刻的天气吗？", font_size=20, color=BIO_YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(q))
        self.wait(3)
        self.play(FadeOut(preview_title), FadeOut(ep6_title), FadeOut(bullets), FadeOut(q))


def rotate_vector(vec: np.ndarray, angle: float) -> np.ndarray:
    """旋转2D向量（z恒为0）"""
    c = np.cos(angle)
    s = np.sin(angle)
    return np.array([vec[0]*c - vec[1]*s, vec[0]*s + vec[1]*c, 0.0])


