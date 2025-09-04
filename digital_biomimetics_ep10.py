"""
数字仿生系列 第10集：生物钟的数学节律
Digital Biomimetics EP10: Mathematical Rhythms of Biological Clock

针对视频号优化：极简视觉、超大字体、科学准确
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

# EP10 主题色
SLEEP_PURPLE = ManimColor("#9333EA")    # 褪黑素
AWAKE_ORANGE = ManimColor("#FB923C")    # 皮质醇
TEMP_RED = ManimColor("#EF4444")        # 体温
CLOCK_BLUE = ManimColor("#0EA5E9")      # 生物钟
NIGHT_DARK = ManimColor("#1E293B")      # 夜晚

# 视频号优化字体大小
TITLE_SIZE = 52       # 超大标题
SUBTITLE_SIZE = 40    # 大标题
NORMAL_SIZE = 32      # 正常文字
SMALL_SIZE = 28       # 最小文字


class DigitalBiomimeticsEP10(Scene):
    """数字仿生系列 第10集 - 生物钟的数学节律"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        # 1. 快速开场（5秒）
        self.show_series_intro()
        
        # 2. 问题钩子（10秒）
        self.jetlag_question()
        
        # 3. 生物钟三曲线（30秒）
        self.biological_rhythms()
        
        # 4. 时差错位演示（20秒）
        self.jetlag_disruption()
        
        # 5. 实用调节法（15秒）
        self.practical_solutions()
        
        # 6. 结尾总结（10秒）
        self.show_ending()

    def show_series_intro(self):
        """快速系列开场 - 5秒"""
        series_title = Text("数字仿生", font_size=60, color=BIO_CYAN, weight=BOLD)
        episode_text = Text("第10集：生物钟的数学节律", font_size=36, color=CLOCK_BLUE)
        episode_text.next_to(series_title, DOWN, buff=0.5)
        
        self.play(Write(series_title), run_time=1)
        self.play(FadeIn(episode_text), run_time=0.8)
        self.wait(0.7)
        self.play(FadeOut(series_title), FadeOut(episode_text), run_time=0.5)

    def jetlag_question(self):
        """问题钩子 - 10秒"""
        # 大字提问
        question = Text(
            "为什么倒时差",
            font_size=TITLE_SIZE,
            color=BIO_YELLOW
        )
        question2 = Text(
            "这么痛苦？",
            font_size=TITLE_SIZE,
            color=BIO_YELLOW
        )
        question2.next_to(question, DOWN, buff=0.3)
        
        self.play(Write(question), run_time=1)
        self.play(Write(question2), run_time=1)
        self.wait(1)
        
        # 准确的时差展示：北京早上9点，纽约晚上8点（13小时时差）
        beijing_group = VGroup()
        beijing_clock = self.create_simple_clock(9, 0)  # 9:00
        beijing_clock.scale(0.8)
        beijing_label = Text("北京 9:00", font_size=SMALL_SIZE, color=BIO_WHITE)
        beijing_sun = Circle(radius=0.15, fill_color=AWAKE_ORANGE, fill_opacity=1)
        beijing_sun.next_to(beijing_clock, UP, buff=0.2)
        beijing_label.next_to(beijing_clock, DOWN, buff=0.3)
        beijing_group.add(beijing_clock, beijing_label, beijing_sun)
        beijing_group.shift(LEFT * 3)
        
        newyork_group = VGroup()
        newyork_clock = self.create_simple_clock(20, 0)  # 20:00 (8PM)
        newyork_clock.scale(0.8)
        newyork_label = Text("纽约 20:00", font_size=SMALL_SIZE, color=BIO_WHITE)
        newyork_moon = self.create_moon_shape()
        newyork_moon.next_to(newyork_clock, UP, buff=0.2)
        newyork_label.next_to(newyork_clock, DOWN, buff=0.3)
        newyork_group.add(newyork_clock, newyork_label, newyork_moon)
        newyork_group.shift(RIGHT * 3)
        
        self.play(
            FadeIn(beijing_group, shift=UP*0.2),
            FadeIn(newyork_group, shift=UP*0.2),
            run_time=1
        )
        
        # 身体混乱图标
        confusion = Text("😵‍💫", font_size=60)
        confusion.move_to(ORIGIN + DOWN * 0.5)
        self.play(FadeIn(confusion, scale=0.5), run_time=0.5)
        
        self.wait(1)
        self.play(
            FadeOut(question), FadeOut(question2),
            FadeOut(beijing_group), FadeOut(newyork_group),
            FadeOut(confusion),
            run_time=1
        )

    def create_simple_clock(self, hour, minute):
        """创建准确的时钟"""
        circle = Circle(radius=0.6, stroke_color=CLOCK_BLUE, stroke_width=3)
        
        # 时针（短）
        hour_angle = PI/2 - (hour % 12 + minute/60) * TAU/12
        hour_hand = Line(
            ORIGIN,
            0.35 * np.array([np.cos(hour_angle), np.sin(hour_angle), 0]),
            stroke_width=5,
            color=BIO_WHITE
        )
        
        # 分针（长）
        minute_angle = PI/2 - minute * TAU/60
        minute_hand = Line(
            ORIGIN,
            0.5 * np.array([np.cos(minute_angle), np.sin(minute_angle), 0]),
            stroke_width=3,
            color=BIO_WHITE
        )
        
        # 中心点
        center = Dot(radius=0.05, color=BIO_WHITE)
        
        return VGroup(circle, hour_hand, minute_hand, center)

    def create_moon_shape(self):
        """创建月亮形状"""
        moon = Circle(radius=0.15, fill_color=SLEEP_PURPLE, fill_opacity=0.8)
        crescent = Circle(radius=0.12, fill_color="#090909", fill_opacity=1)
        crescent.shift(RIGHT * 0.08)
        return VGroup(moon, crescent)

    def biological_rhythms(self):
        """生物钟三曲线 - 30秒"""
        title = Text("身体的3个节律曲线", font_size=SUBTITLE_SIZE, color=CLOCK_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        
        # 创建坐标轴
        axes = Axes(
            x_range=[0, 24, 6],
            y_range=[0, 100, 25],
            x_length=10,
            y_length=4,
            axis_config={"color": BIO_GRAY, "stroke_width": 2},
            tips=False
        )
        axes.shift(DOWN * 0.5)
        
        # X轴标签（时间）
        x_labels = VGroup()
        for hour in [0, 6, 12, 18, 24]:
            label = Text(f"{hour}", font_size=20, color=BIO_WHITE)
            label.next_to(axes.c2p(hour, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        self.play(Create(axes), FadeIn(x_labels), run_time=1)
        
        # 褪黑素曲线（晚上高，21点开始上升，凌晨3点峰值）
        melatonin_func = lambda t: 50 + 40 * np.sin((t - 15) * TAU/24) if t > 20 or t < 7 else 10
        melatonin_curve = axes.plot(
            lambda t: 50 + 40 * np.cos((t - 3) * TAU/24) if 21 <= t or t <= 7 else 20,
            x_range=[0, 24],
            color=SLEEP_PURPLE,
            stroke_width=4
        )
        melatonin_label = Text("褪黑素", font_size=SMALL_SIZE, color=SLEEP_PURPLE)
        melatonin_label.next_to(axes.c2p(2, 85), RIGHT, buff=0.2)
        
        # 皮质醇曲线（早上高，6-8点峰值）
        cortisol_curve = axes.plot(
            lambda t: 50 + 40 * np.cos((t - 7) * TAU/24),
            x_range=[0, 24],
            color=AWAKE_ORANGE,
            stroke_width=4
        )
        cortisol_label = Text("皮质醇", font_size=SMALL_SIZE, color=AWAKE_ORANGE)
        cortisol_label.next_to(axes.c2p(7, 85), RIGHT, buff=0.2)
        
        # 体温曲线（下午高，16-18点峰值，凌晨4点最低）
        temp_curve = axes.plot(
            lambda t: 50 + 30 * np.sin((t - 10) * TAU/24),
            x_range=[0, 24],
            color=TEMP_RED,
            stroke_width=4
        )
        temp_label = Text("体温", font_size=SMALL_SIZE, color=TEMP_RED)
        temp_label.next_to(axes.c2p(16, 75), RIGHT, buff=0.2)
        
        # 逐个显示曲线
        self.play(
            Create(melatonin_curve),
            FadeIn(melatonin_label),
            run_time=1.5
        )
        self.play(
            Create(cortisol_curve),
            FadeIn(cortisol_label),
            run_time=1.5
        )
        self.play(
            Create(temp_curve),
            FadeIn(temp_label),
            run_time=1.5
        )
        
        # 关键时间点标注
        sleep_zone = Rectangle(
            width=axes.c2p(7, 0)[0] - axes.c2p(22, 0)[0],
            height=4,
            fill_color=NIGHT_DARK,
            fill_opacity=0.2,
            stroke_width=0
        )
        sleep_zone.move_to(axes.c2p(1.5, 50))
        
        night_label = Text("睡眠时间", font_size=SMALL_SIZE, color=SLEEP_PURPLE)
        night_label.next_to(axes.c2p(2, 10), DOWN, buff=0.5)
        
        self.play(
            FadeIn(sleep_zone),
            Write(night_label),
            run_time=1
        )
        
        self.wait(2)
        
        # 清理场景
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(x_labels),
            FadeOut(melatonin_curve), FadeOut(melatonin_label),
            FadeOut(cortisol_curve), FadeOut(cortisol_label),
            FadeOut(temp_curve), FadeOut(temp_label),
            FadeOut(sleep_zone), FadeOut(night_label),
            run_time=1
        )

    def jetlag_disruption(self):
        """时差错位演示 - 20秒"""
        title = Text("飞行13小时后", font_size=TITLE_SIZE, color=BIO_RED, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        
        # 创建两个时间轴对比
        # 身体时间（内部）
        body_label = Text("身体感觉", font_size=NORMAL_SIZE, color=SLEEP_PURPLE)
        body_label.move_to([-3.5, 2, 0])
        
        body_timeline = Rectangle(width=6, height=0.8, stroke_color=SLEEP_PURPLE, stroke_width=2)
        body_timeline.move_to([-3.5, 1, 0])
        
        body_night = Rectangle(
            width=2, height=0.8,
            fill_color=NIGHT_DARK, fill_opacity=0.7,
            stroke_width=0
        )
        body_night.move_to([-3.5, 1, 0])
        body_time = Text("晚上该睡觉", font_size=SMALL_SIZE, color=BIO_WHITE)
        body_time.move_to([-3.5, 0.2, 0])
        
        # 环境时间（外部）
        env_label = Text("环境时间", font_size=NORMAL_SIZE, color=AWAKE_ORANGE)
        env_label.move_to([-3.5, -1, 0])
        
        env_timeline = Rectangle(width=6, height=0.8, stroke_color=AWAKE_ORANGE, stroke_width=2)
        env_timeline.move_to([-3.5, -2, 0])
        
        env_day = Rectangle(
            width=2, height=0.8,
            fill_color=AWAKE_ORANGE, fill_opacity=0.5,
            stroke_width=0
        )
        env_day.move_to([-3.5, -2, 0])
        env_time = Text("早上该起床", font_size=SMALL_SIZE, color=BIO_WHITE)
        env_time.move_to([-3.5, -2.8, 0])
        
        self.play(
            FadeIn(body_label), Create(body_timeline),
            FadeIn(body_night), Write(body_time),
            run_time=1.5
        )
        
        self.play(
            FadeIn(env_label), Create(env_timeline),
            FadeIn(env_day), Write(env_time),
            run_time=1.5
        )
        
        # 冲突箭头
        conflict_arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                start=body_timeline.get_bottom() + DOWN * 0.1,
                end=env_timeline.get_top() + UP * 0.1,
                color=BIO_RED,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15
            )
            arrow.shift(RIGHT * (i - 1) * 1.5)
            conflict_arrows.add(arrow)
        
        self.play(Create(conflict_arrows), run_time=1)
        
        # 症状列表
        symptoms = VGroup(
            Text("😫 疲劳", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("🤯 头痛", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("😔 情绪低落", font_size=SMALL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, buff=0.3)
        symptoms.move_to([3, 0, 0])
        
        self.play(FadeIn(symptoms, shift=LEFT*0.3), run_time=1)
        
        self.wait(2)
        
        # 关键信息
        key_info = Text(
            "激素分泌时间错乱",
            font_size=SUBTITLE_SIZE,
            color=BIO_YELLOW,
            weight=BOLD
        )
        key_info.to_edge(DOWN, buff=0.5)
        self.play(Write(key_info), run_time=1)
        self.wait(1)
        
        self.play(
            FadeOut(title), FadeOut(body_label), FadeOut(body_timeline),
            FadeOut(body_night), FadeOut(body_time),
            FadeOut(env_label), FadeOut(env_timeline),
            FadeOut(env_day), FadeOut(env_time),
            FadeOut(conflict_arrows), FadeOut(symptoms),
            FadeOut(key_info),
            run_time=1
        )

    def practical_solutions(self):
        """实用调节法 - 15秒"""
        title = Text("快速调节3步法", font_size=SUBTITLE_SIZE, color=BIO_GREEN)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)
        
        # 三个方法，垂直排列避免重叠
        methods = VGroup()
        
        # 1. 光照调节
        method1 = VGroup()
        sun_icon = Circle(radius=0.25, fill_color=AWAKE_ORANGE, fill_opacity=1)
        sun_rays = VGroup()
        for i in range(8):
            angle = i * TAU / 8
            ray = Line(
                0.3 * np.array([np.cos(angle), np.sin(angle), 0]),
                0.45 * np.array([np.cos(angle), np.sin(angle), 0]),
                stroke_width=3,
                color=AWAKE_ORANGE
            )
            sun_rays.add(ray)
        sun_group = VGroup(sun_icon, sun_rays)
        sun_group.scale(0.8)
        
        text1 = VGroup(
            Text("到达后立即", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("晒太阳30分钟", font_size=NORMAL_SIZE, color=AWAKE_ORANGE, weight=BOLD)
        ).arrange(DOWN, buff=0.15)
        
        method1.add(sun_group, text1)
        method1.arrange(RIGHT, buff=0.5)
        method1.shift(UP * 1.5)
        
        # 2. 饮食调节
        method2 = VGroup()
        meal_icon = Text("🍽️", font_size=40)
        
        text2 = VGroup(
            Text("按当地时间", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("规律进餐", font_size=NORMAL_SIZE, color=BIO_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.15)
        
        method2.add(meal_icon, text2)
        method2.arrange(RIGHT, buff=0.5)
        
        # 3. 褪黑素补充
        method3 = VGroup()
        pill_icon = Ellipse(width=0.4, height=0.25, fill_color=SLEEP_PURPLE, fill_opacity=0.8)
        
        text3 = VGroup(
            Text("当地晚上9点", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("褪黑素3mg", font_size=NORMAL_SIZE, color=SLEEP_PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0.15)
        
        method3.add(pill_icon, text3)
        method3.arrange(RIGHT, buff=0.5)
        method3.shift(DOWN * 1.5)
        
        methods.add(method1, method2, method3)
        
        for method in methods:
            self.play(FadeIn(method, scale=0.9), run_time=0.8)
        
        self.wait(2)
        
        # 恢复时间
        recovery = Text(
            "完全适应需要：每时区1天",
            font_size=SMALL_SIZE,
            color=BIO_CYAN
        )
        recovery.to_edge(DOWN, buff=0.5)
        self.play(Write(recovery), run_time=1)
        self.wait(1)
        
        self.play(
            FadeOut(title), FadeOut(methods), FadeOut(recovery),
            run_time=1
        )

    def show_ending(self):
        """结尾总结 - 10秒"""
        # 金句
        quote = VGroup(
            Text("生物钟是", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("写在基因里的", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("数学方程", font_size=TITLE_SIZE, color=CLOCK_BLUE, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(quote[0]), run_time=0.8)
        self.play(Write(quote[1]), run_time=0.8)
        self.play(Write(quote[2]), run_time=1)
        self.wait(1.5)
        
        self.play(FadeOut(quote), run_time=1)
        
        # 下期预告
        preview = VGroup(
            Text("下期预告", font_size=NORMAL_SIZE, color=BIO_YELLOW),
            Text("第11集：共生的博弈论", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("合作背后的数学密码", font_size=NORMAL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(preview[0]), run_time=0.5)
        self.play(Write(preview[1]), run_time=0.8)
        self.play(Write(preview[2]), run_time=0.7)
        self.wait(1)
        
        self.play(FadeOut(preview), run_time=1)