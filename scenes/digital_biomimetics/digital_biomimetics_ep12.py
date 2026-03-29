"""
数字仿生系列 第12集：生命的数学定理
Digital Biomimetics EP12: Mathematical Theorems of Life

系列终章 - 情感升华版：超大字体、诗意表达、哲学共鸣
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

# EP12 终章主题色
LIFE_GOLD = ManimColor("#FFD700")      # 生命金
UNIVERSE_PURPLE = ManimColor("#9333EA")  # 宇宙紫
BEAUTY_CYAN = ManimColor("#06B6D4")     # 美学青
WISDOM_AMBER = ManimColor("#F59E0B")    # 智慧琥珀
LOVE_ROSE = ManimColor("#F472B6")       # 爱意玫瑰

# 视频号超大字体
EPIC_TITLE_SIZE = 72      # 史诗标题
MEGA_TITLE_SIZE = 64      # 超超大标题
TITLE_SIZE = 52           # 超大标题
SUBTITLE_SIZE = 40        # 大标题
NORMAL_SIZE = 32          # 正常文字
SMALL_SIZE = 28           # 最小文字


class DigitalBiomimeticsEP12(Scene):
    """数字仿生系列 第12集 - 生命的数学定理（终章）"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        # 1. 系列开场（8秒）
        self.show_series_finale_intro()
        
        # 2. 回顾之旅（20秒）
        self.journey_flashback()
        
        # 3. 统一公式展示（30秒）
        self.unified_equation()
        
        # 4. 三个层次的美（45秒）
        self.three_levels_of_beauty()
        
        # 5. 哲学升华（15秒）
        self.philosophical_elevation()
        
        # 6. 温情结尾（12秒）
        self.heartfelt_ending()

    def show_series_finale_intro(self):
        """系列终章开场 - 8秒"""
        # 特殊的终章标识
        series_title = Text("数字仿生", font_size=64, color=BIO_CYAN, weight=BOLD)
        
        finale_badge = Text("终章", font_size=36, color=LIFE_GOLD, weight=BOLD)
        finale_badge.next_to(series_title, RIGHT, buff=0.5)
        
        episode_text = Text("第12集：生命的数学定理", font_size=40, color=UNIVERSE_PURPLE)
        episode_text.next_to(series_title, DOWN, buff=0.6)
        
        # 史诗感的进入动画
        self.play(
            Write(series_title),
            FadeIn(finale_badge, scale=0.5),
            run_time=2
        )
        self.play(FadeIn(episode_text, shift=UP*0.3), run_time=1.5)
        
        # 特殊的光效
        glow = Circle(radius=4, stroke_color=LIFE_GOLD, stroke_width=2, stroke_opacity=0.3)
        glow.surround(VGroup(series_title, finale_badge, episode_text))
        self.play(Create(glow), run_time=1)
        self.play(FadeOut(glow), run_time=0.5)
        
        self.wait(1)
        self.play(
            FadeOut(series_title), FadeOut(finale_badge), FadeOut(episode_text),
            run_time=1
        )

    def journey_flashback(self):
        """回顾之旅 - 20秒"""
        # 开启回忆
        memory_title = Text(
            "这一路，我们见证了...",
            font_size=TITLE_SIZE,
            color=BEAUTY_CYAN
        )
        self.play(Write(memory_title), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(memory_title), run_time=0.5)
        
        # 快速闪回经典场景（用抽象符号代替复杂动画）
        memories = VGroup()
        
        # 记忆1：水母之舞
        memory1 = VGroup(
            Text("~", font_size=80, color=BIO_CYAN),  # 波浪代表水母
            Text("水母之舞", font_size=SMALL_SIZE, color=BIO_CYAN)
        ).arrange(DOWN, buff=0.2)
        
        # 记忆2：心跳节律
        memory2 = VGroup(
            Text("♡", font_size=80, color=BIO_RED),  # 心形
            Text("心跳节律", font_size=SMALL_SIZE, color=BIO_RED)
        ).arrange(DOWN, buff=0.2)
        
        # 记忆3：DNA密码
        memory3 = VGroup(
            Text("⚬⚬", font_size=80, color=BIO_GREEN),  # 双螺旋抽象
            Text("遗传密码", font_size=SMALL_SIZE, color=BIO_GREEN)
        ).arrange(DOWN, buff=0.2)
        
        # 记忆4：群体智慧
        memory4 = VGroup(
            Text("◦◦◦", font_size=80, color=BIO_YELLOW),  # 群集
            Text("群体智慧", font_size=SMALL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.2)
        
        # 记忆5：博弈合作
        memory5 = VGroup(
            Text("⚬⚬", font_size=80, color=LIFE_GOLD),  # 合作符号
            Text("共生合作", font_size=SMALL_SIZE, color=LIFE_GOLD)
        ).arrange(DOWN, buff=0.2)
        
        memories.add(memory1, memory2, memory3, memory4, memory5)
        
        # 水平排列
        memories.arrange(RIGHT, buff=1.5)
        memories.scale(0.8)
        
        # 快速闪现
        for i, memory in enumerate(memories):
            self.play(FadeIn(memory, scale=0.7), run_time=0.6)
        
        self.wait(1)
        
        # 汇聚成一体
        convergence_text = Text(
            "所有的美，都指向同一个真理",
            font_size=SUBTITLE_SIZE,
            color=UNIVERSE_PURPLE,
            weight=BOLD
        )
        convergence_text.shift(DOWN * 2.5)
        self.play(Write(convergence_text), run_time=2)
        
        self.wait(1)
        self.play(
            FadeOut(memories), FadeOut(convergence_text),
            run_time=1
        )

    def unified_equation(self):
        """统一公式展示 - 30秒"""
        title = Text(
            "生命的统一方程",
            font_size=TITLE_SIZE,
            color=LIFE_GOLD,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.8)
        self.play(Write(title), run_time=1.5)
        
        # 不是真正的数学公式，而是诗意的概念表达
        equation_parts = VGroup()
        
        # 第一行：生命 =
        life_equals = Text(
            "生命 =",
            font_size=MEGA_TITLE_SIZE,
            color=BIO_WHITE,
            weight=BOLD
        )
        life_equals.move_to([0, 1.5, 0])
        
        # 四个核心要素
        elements = VGroup(
            Text("能量流动", font_size=SUBTITLE_SIZE, color=BIO_RED),
            Text("×", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("信息处理", font_size=SUBTITLE_SIZE, color=BIO_BLUE),
            Text("×", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("自我组织", font_size=SUBTITLE_SIZE, color=BIO_GREEN),
            Text("×", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("适应进化", font_size=SUBTITLE_SIZE, color=BIO_PURPLE)
        ).arrange(RIGHT, buff=0.3)
        elements.move_to([0, 0.3, 0])
        
        # 加号
        plus_sign = Text("+", font_size=SUBTITLE_SIZE, color=WISDOM_AMBER, weight=BOLD)
        plus_sign.move_to([0, -0.5, 0])
        
        # 最终的升华
        transcendence = Text(
            "爱与美的涌现",
            font_size=SUBTITLE_SIZE,
            color=LOVE_ROSE,
            weight=BOLD
        )
        transcendence.move_to([0, -1.2, 0])
        
        # 逐步显示公式
        self.play(Write(life_equals), run_time=1.5)
        
        # 逐个显示元素
        for i in range(0, len(elements), 2):  # 只显示文字，跳过乘号
            if i < len(elements):
                self.play(FadeIn(elements[i], shift=DOWN*0.3), run_time=0.8)
            if i + 1 < len(elements):
                self.play(FadeIn(elements[i+1], scale=0.5), run_time=0.3)
        
        self.play(Write(plus_sign), run_time=0.8)
        self.play(
            Write(transcendence), 
            transcendence.animate.scale(1.1),
            run_time=2
        )
        
        # 简单的视觉效果：流动光线
        for _ in range(3):
            light = Dot(radius=0.05, color=LIFE_GOLD, fill_opacity=0.8)
            light.move_to([-6, 0, 0])
            self.play(light.animate.move_to([6, 0, 0]), run_time=1, rate_func=linear)
            self.remove(light)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(life_equals), FadeOut(elements),
            FadeOut(plus_sign), FadeOut(transcendence),
            run_time=1.5
        )

    def three_levels_of_beauty(self):
        """三个层次的美 - 45秒"""
        title = Text(
            "生命之美的三重境界",
            font_size=TITLE_SIZE,
            color=BEAUTY_CYAN,
            weight=BOLD
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.5)
        
        # 第一层：微观美
        self.show_beauty_level(
            "第一重：微观美",
            "分子的精密舞蹈",
            BIO_BLUE,
            self.create_molecular_dance(),
            position=UP * 1.5
        )
        
        self.wait(2)
        
        # 第二层：宏观美  
        self.show_beauty_level(
            "第二重：宏观美",
            "生态的和谐网络", 
            BIO_GREEN,
            self.create_ecological_network(),
            position=ORIGIN
        )
        
        self.wait(2)
        
        # 第三层：系统美
        self.show_beauty_level(
            "第三重：系统美",
            "智慧的涌现奇迹",
            UNIVERSE_PURPLE,
            self.create_emergence_visual(),
            position=DOWN * 1.5
        )
        
        self.wait(3)
        
        # 三层合一的视觉效果
        unity_text = Text(
            "三美合一，生命绽放",
            font_size=SUBTITLE_SIZE,
            color=LIFE_GOLD,
            weight=BOLD
        )
        unity_text.shift(DOWN * 3)
        
        self.play(Write(unity_text), run_time=2)
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)), run_time=1.5)

    def show_beauty_level(self, level_title, description, color, visual, position):
        """显示美的层次"""
        level_group = VGroup()
        
        title = Text(level_title, font_size=NORMAL_SIZE, color=color, weight=BOLD)
        desc = Text(description, font_size=SMALL_SIZE, color=BIO_WHITE)
        
        text_group = VGroup(title, desc).arrange(DOWN, buff=0.2)
        text_group.shift(LEFT * 3)
        
        visual.shift(RIGHT * 3)
        visual.scale(0.6)
        
        level_group.add(text_group, visual)
        level_group.move_to(position)
        
        self.play(
            FadeIn(text_group, shift=RIGHT*0.5),
            FadeIn(visual, shift=LEFT*0.5),
            run_time=1.5
        )

    def create_molecular_dance(self):
        """创建分子舞蹈视觉"""
        dance = VGroup()
        
        # 简化的分子运动
        for i in range(5):
            angle = i * TAU / 5
            molecule = Circle(
                radius=0.15,
                fill_color=BIO_BLUE,
                fill_opacity=0.7
            )
            molecule.move_to(0.8 * np.array([np.cos(angle), np.sin(angle), 0]))
            dance.add(molecule)
        
        # 中心连接
        center = Dot(radius=0.1, color=BIO_CYAN)
        dance.add(center)
        
        return dance

    def create_ecological_network(self):
        """创建生态网络视觉"""
        network = VGroup()
        
        # 节点
        nodes = []
        for i in range(6):
            angle = i * TAU / 6
            node = Circle(
                radius=0.12,
                fill_color=BIO_GREEN,
                fill_opacity=0.8
            )
            pos = 1.2 * np.array([np.cos(angle), np.sin(angle), 0])
            node.move_to(pos)
            nodes.append(node)
            network.add(node)
        
        # 连接线
        for i in range(6):
            for j in range(i+1, 6):
                if j - i <= 2:  # 只连接相邻的节点
                    line = Line(
                        nodes[i].get_center(),
                        nodes[j].get_center(),
                        stroke_width=1,
                        color=BIO_GREEN,
                        stroke_opacity=0.5
                    )
                    network.add(line)
        
        return network

    def create_emergence_visual(self):
        """创建涌现视觉"""
        emergence = VGroup()
        
        # 从简单到复杂的视觉变换
        simple_parts = VGroup(
            *[Dot(radius=0.05, color=UNIVERSE_PURPLE).shift(
                0.3 * np.array([np.cos(i*TAU/8), np.sin(i*TAU/8), 0])
            ) for i in range(8)]
        )
        
        # 复杂整体（星形）
        complex_whole = RegularPolygon(
            n=8, 
            radius=1,
            stroke_color=LIFE_GOLD,
            stroke_width=3,
            fill_opacity=0.2,
            fill_color=UNIVERSE_PURPLE
        )
        
        emergence.add(simple_parts, complex_whole)
        return emergence

    def philosophical_elevation(self):
        """哲学升华 - 15秒"""
        # 三句递进的哲学金句
        philosophy = VGroup()
        
        line1 = Text(
            "数学不仅是",
            font_size=SUBTITLE_SIZE,
            color=BIO_WHITE
        )
        
        line2 = Text(
            "科学的语言",
            font_size=SUBTITLE_SIZE,
            color=BIO_CYAN
        )
        
        line3 = Text(
            "更是生命的诗歌",
            font_size=MEGA_TITLE_SIZE,
            color=LOVE_ROSE,
            weight=BOLD
        )
        
        philosophy.add(line1, line2, line3)
        philosophy.arrange(DOWN, buff=0.5)
        
        # 逐句显示，营造诗意感
        self.play(Write(line1), run_time=1.5)
        self.play(Write(line2), run_time=1.5)
        self.play(
            Write(line3),
            line3.animate.scale(1.1),
            run_time=2.5
        )
        
        # 最终升华
        ultimate_truth = Text(
            "宇宙的美，写在方程里",
            font_size=TITLE_SIZE,
            color=LIFE_GOLD,
            weight=BOLD
        )
        ultimate_truth.shift(DOWN * 2.5)
        
        self.play(Write(ultimate_truth), run_time=2)
        self.wait(2)
        
        self.play(
            FadeOut(philosophy), FadeOut(ultimate_truth),
            run_time=1.5
        )

    def heartfelt_ending(self):
        """温情结尾 - 12秒"""
        # 感谢语
        gratitude = VGroup(
            Text("感谢陪伴", font_size=SUBTITLE_SIZE, color=BIO_WHITE),
            Text("这场数学与生命的", font_size=NORMAL_SIZE, color=BIO_CYAN),
            Text("美丽对话", font_size=SUBTITLE_SIZE, color=LOVE_ROSE, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        self.play(
            Write(gratitude[0]),
            run_time=1.5
        )
        self.play(
            Write(gratitude[1]),
            run_time=1.5
        )
        self.play(
            Write(gratitude[2]),
            gratitude[2].animate.scale(1.1),
            run_time=2
        )
        
        self.wait(1)
        
        # 系列完结标识
        finale_text = Text(
            "数字仿生系列 完",
            font_size=NORMAL_SIZE,
            color=BIO_PURPLE
        )
        finale_text.shift(DOWN * 2.5)
        
        self.play(Write(finale_text), run_time=1.5)
        
        # 最后的心跳动画（简单的缩放脉动）
        heart = Text("♡", font_size=60, color=LOVE_ROSE)
        heart.shift(DOWN * 1.5)
        
        self.play(FadeIn(heart, scale=0.5), run_time=1)
        
        # 心跳脉动
        for _ in range(3):
            self.play(
                heart.animate.scale(1.2),
                rate_func=there_and_back,
                run_time=0.6
            )
        
        self.wait(1)
        
        # 温柔淡出
        self.play(
            FadeOut(gratitude),
            FadeOut(finale_text), 
            FadeOut(heart),
            run_time=2
        )
        
        # 最终黑屏
        final_message = Text(
            "愿数学之美，与你同在",
            font_size=NORMAL_SIZE,
            color=WISDOM_AMBER
        )
        
        self.play(FadeIn(final_message), run_time=2)
        self.wait(2)
        self.play(FadeOut(final_message), run_time=2)