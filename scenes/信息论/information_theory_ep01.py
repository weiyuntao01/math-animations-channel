from manim import *
import numpy as np
import random

# --- 信息论系列配色 (Matrix/Cyberpunk) ---
IT_GREEN = "#00FF41"     # 信号 / 信息 / 正确 (Matrix Green)
IT_RED = "#FF2A68"       # 噪音 / 熵 / 错误
IT_BLUE = "#00BFFF"      # 结构 / 编码 / 科技
IT_YELLOW = "#FFD700"    # 核心概念 / 强调
IT_GRAY = "#333333"      # 背景细节 / 辅助线
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP01(Scene):
    """信息论 EP01: 信息即意外 (最终修复版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：黑客帝国风格
        self.intro_matrix()
        
        # 2. 概念引入：太阳 vs 外星人
        self.compare_surprise()
        
        # 3. 核心公式：I = -log P (已修复中文报错)
        self.derive_formula()
        
        # 4. 原理深化：比特的本质 (可加性)
        self.explain_additivity()
        
        # 5. 哲学升华
        self.show_philosophy()

    def intro_matrix(self):
        """开场：信息流"""
        
        # 模拟 Matrix 代码雨
        code_stream = VGroup()
        for i in range(25):
            col_x = random.uniform(-7, 7)
            col_len = random.randint(5, 15)
            # 生成一列随机字符 (0/1)
            chars = VGroup(*[
                Text(str(random.choice([0, 1])), font_size=20, color=IT_GREEN, fill_opacity=random.uniform(0.3, 1))
                for _ in range(col_len)
            ]).arrange(DOWN, buff=0.1)
            chars.move_to(RIGHT * col_x + UP * random.uniform(0, 4))
            code_stream.add(chars)
            
        self.play(FadeIn(code_stream, lag_ratio=0.1), run_time=2)
        
        # 标题
        title = Text("信息论：宇宙的底层代码", font_size=54, color=IT_GREEN, weight=BOLD).set_z_index(10)
        subtitle = Text("EP01: 信息即意外 (Information is Surprise)", font_size=32, color=WHITE).next_to(title, DOWN, buff=0.5).set_z_index(10)
        
        # 背景变暗以突出标题
        bg_rect = Rectangle(width=16, height=9, color=BLACK, fill_opacity=0.8).set_z_index(5)
        
        self.play(
            FadeIn(bg_rect),
            Write(title),
            run_time=1.5
        )
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        
        # 清场
        self.play(FadeOut(Group(*self.mobjects)))

    def compare_surprise(self):
        """对比：必然事件 vs 意外事件"""
        
        LEFT_ZONE = LEFT * 4.0
        RIGHT_ZONE = RIGHT * 4.0
        
        # 1. 左侧：太阳升起 (高概率)
        sun_icon = VGroup(
            Circle(radius=0.8, color=IT_YELLOW, fill_opacity=0.8),
            *[Line(UP*0.9, UP*1.2, color=IT_YELLOW).rotate(angle) for angle in np.linspace(0, TAU, 8, endpoint=False)]
        ).move_to(LEFT_ZONE + UP * 1.5)
        
        label_sun = Text("明天太阳升起", font_size=24, color=IT_YELLOW).next_to(sun_icon, DOWN)
        
        # 2. 左侧：外星人 (低概率)
        alien_icon = VGroup(
            Ellipse(width=1.2, height=1.5, color=IT_GREEN, fill_opacity=0.8),
            Ellipse(width=0.4, height=0.2, color=BLACK, fill_opacity=1).move_to(UP*0.2 + LEFT*0.3), # 左眼
            Ellipse(width=0.4, height=0.2, color=BLACK, fill_opacity=1).move_to(UP*0.2 + RIGHT*0.3), # 右眼
        ).move_to(LEFT_ZONE + DOWN * 1.5)
        
        label_alien = Text("明天外星人降临", font_size=24, color=IT_GREEN).next_to(alien_icon, DOWN)
        
        self.play(FadeIn(sun_icon), Write(label_sun))
        self.play(FadeIn(alien_icon), Write(label_alien))
        
        # 3. 右侧：信息量分析 (流式布局)
        title = Text("什么是\"信息\"？", font_size=36, color=IT_BLUE, weight=BOLD).move_to(RIGHT_ZONE + UP * 2.5)
        self.play(Write(title))
        
        # 分析太阳
        # 概率 P -> 1, 惊讶度 -> 0
        info_sun = VGroup(
            Text("太阳升起：", font_size=24, color=IT_YELLOW),
            Text("概率 P ≈ 100%", font_size=20),
            Text("废话，完全意料之中", font_size=20),
            Text("信息量 = 0", font_size=24, color=IT_RED, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        info_sun.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(info_sun))
        self.wait(1)
        
        # 分析外星人
        # 概率 P -> 0, 惊讶度 -> 无穷大
        info_alien = VGroup(
            Text("外星人降临：", font_size=24, color=IT_GREEN),
            Text("概率 P ≈ 0%", font_size=20),
            Text("极其震惊，颠覆认知", font_size=20),
            Text("信息量 = 巨大", font_size=24, color=IT_BLUE, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        info_alien.next_to(info_sun, DOWN, buff=0.8)
        
        self.play(Write(info_alien))
        
        # 核心定义
        definition = Text("信息是对不确定性的消除", font_size=32, color=WHITE).to_edge(DOWN, buff=1.0)
        self.play(Write(definition))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def derive_formula(self):
        """推导核心公式 (修复 MathTex 中文报错)"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("香农信息量公式", font_size=40, color=IT_BLUE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 1. 公式展示
        formula = MathTex(
            r"I(x) = -\log_2 P(x)",
            font_size=60
        )
        formula[0][:4].set_color(IT_BLUE)   # I(x)
        formula[0][5:9].set_color(IT_GREEN) # log P
        
        formula.move_to(RIGHT_ZONE + UP * 0.5)
        
        # 2. 左侧：函数图像
        ax = Axes(
            x_range=[0, 1.2, 0.2],
            y_range=[0, 5, 1],
            x_length=5,
            y_length=4,
            axis_config={"color": IT_GRAY, "include_numbers": True},
            tips=False
        ).move_to(LEFT_ZONE + DOWN * 0.5)
        
        # 绘制 -log2(x)
        graph = ax.plot(lambda x: -np.log2(x), x_range=[0.03125, 1], color=IT_GREEN, stroke_width=4)
        
        # --- 修复核心：手动创建 Text 标签 ---
        x_label = Text("概率 P", font_size=20, color=IT_GRAY).next_to(ax.x_axis, DOWN, buff=0.2)
        y_label = Text("信息 I", font_size=20, color=IT_GRAY).next_to(ax.y_axis, LEFT, buff=0.2)
        
        self.play(Create(ax), Write(x_label), Write(y_label))
        self.play(Create(graph), Write(formula))
        
        # 3. 动态演示点
        
        # 点1：必然事件 (P=1, I=0)
        dot1 = Dot(ax.c2p(1, 0), color=IT_YELLOW, radius=0.1)
        label1 = Text("必然 (P=1, I=0)", font_size=20, color=IT_YELLOW).next_to(dot1, UR, buff=0.1)
        
        self.play(FadeIn(dot1), Write(label1))
        
        # 点2：抛硬币 (P=0.5, I=1)
        dot2 = Dot(ax.c2p(0.5, 1), color=IT_BLUE, radius=0.1)
        # 用虚线连接
        lines2 = ax.get_lines_to_point(ax.c2p(0.5, 1), color=IT_BLUE)
        label2 = Text("硬币 (P=0.5, I=1 bit)", font_size=20, color=IT_BLUE).next_to(dot2, UR, buff=0.1)
        
        self.play(FadeIn(dot2), Create(lines2), Write(label2))
        
        # 点3：小概率 (P=0.125, I=3)
        dot3 = Dot(ax.c2p(0.125, 3), color=IT_RED, radius=0.1)
        lines3 = ax.get_lines_to_point(ax.c2p(0.125, 3), color=IT_RED)
        label3 = Text("意外 (P小, I大)", font_size=20, color=IT_RED).next_to(dot3, RIGHT, buff=0.1)
        
        self.play(FadeIn(dot3), Create(lines3), Write(label3))
        
        # 4. 右侧文字总结
        summary = VGroup(
            Text("概率越低，信息量越大", font_size=24, color=IT_RED),
            Text("概率越高，信息量越小", font_size=24, color=IT_YELLOW),
            Text("单位：比特 (Bit)", font_size=24, color=IT_BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        summary.next_to(formula, DOWN, buff=1.0)
        
        self.play(Write(summary))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def explain_additivity(self):
        """为什么要用对数？(可加性)"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("为什么是 Log？(对数)", font_size=36, color=IT_YELLOW).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 1. 左侧：硬币实验
        coin1 = Circle(radius=0.5, color=IT_BLUE).move_to(LEFT_ZONE + UP * 1.0)
        text1 = Text("1", font_size=32).move_to(coin1)
        
        coin2 = Circle(radius=0.5, color=IT_BLUE).move_to(LEFT_ZONE + DOWN * 1.0)
        text2 = Text("0", font_size=32).move_to(coin2)
        
        coins = VGroup(coin1, text1, coin2, text2)
        self.play(FadeIn(coins))
        
        # 2. 右侧：推导
        # 两个独立事件 A 和 B
        eq_prob = MathTex(r"P(A \text{ and } B) = P(A) \times P(B)", font_size=32)
        eq_prob.move_to(RIGHT_ZONE + UP * 1.5)
        
        desc_prob = Text("概率是相乘的", font_size=20, color=IT_GRAY).next_to(eq_prob, DOWN, buff=0.1)
        
        self.play(Write(eq_prob), Write(desc_prob))
        
        # 想要信息量相加
        target_text = Text("但我们希望信息量是相加的：", font_size=24, color=IT_GREEN)
        target_text.next_to(desc_prob, DOWN, buff=0.8)
        
        eq_info = MathTex(r"I(A \text{ and } B) = I(A) + I(B)", font_size=32, color=IT_GREEN)
        eq_info.next_to(target_text, DOWN, buff=0.3)
        
        self.play(Write(target_text), Write(eq_info))
        
        # 只有对数能做到
        magic_eq = MathTex(
            r"\log(P_A \cdot P_B) = \log(P_A) + \log(P_B)",
            font_size=36, color=IT_YELLOW
        ).next_to(eq_info, DOWN, buff=1.0)
        
        self.play(Write(magic_eq))
        self.play(Indicate(magic_eq))
        
        # 3. 左侧视觉配合
        # 1个硬币 = 1 bit
        brace1 = Brace(coin1, RIGHT, buff=0.2)
        bit1 = Text("1 bit", font_size=24, color=IT_BLUE).next_to(brace1, RIGHT)
        
        self.play(Create(brace1), Write(bit1))
        
        # 2个硬币 = 2 bits
        group_coins = VGroup(coin1, coin2)
        brace2 = Brace(group_coins, LEFT, buff=0.2)
        bit2 = Text("2 bits", font_size=24, color=IT_BLUE).next_to(brace2, LEFT)
        
        self.play(Create(brace2), Write(bit2))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("信息论的哲学", font_size=40, color=IT_BLUE).to_edge(UP, buff=1.5)
        
        # 金句流
        lines = VGroup(
            Text("在这个信息爆炸的时代", font_size=28),
            Text("大家都喜欢说重复的废话 (P -> 1)", font_size=28, color=IT_GRAY),
            Text("随波逐流的人，信息量为 0", font_size=32, color=IT_RED),
            Text("越稀缺，越有价值", font_size=36, color=IT_GREEN, weight=BOLD),
            Text("做一个\"意外\"的人", font_size=36, color=IT_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.6)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：比特的诞生", font_size=40, color=IT_GREEN).move_to(UP * 0.5)
        desc = Text("为什么是二进制？\n20个问题游戏与二分查找的智慧。", font_size=24, color=IT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))