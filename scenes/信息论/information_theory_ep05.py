from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 信号 / 信息 / 正确
IT_RED = "#FF2A68"       # 噪音 / 熵 / 错误
IT_BLUE = "#00BFFF"      # 结构 / 编码 / 科技
IT_YELLOW = "#FFD700"    # 核心概念 / 强调
IT_PURPLE = "#8B5CF6"    # 哲学
IT_ORANGE = "#F97316"    # 警告
IT_GRAY = "#333333"      # 背景细节
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP05(Scene):
    """信息论 EP05: 信噪比 (修复报错版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：鸡尾酒会效应
        self.intro_cocktail_party()
        
        # 2. 视觉拆解：信号 vs 噪音
        self.visualize_snr()
        
        # 3. 核心定理：香农极限
        self.shannon_limit()
        
        # 4. 哲学升华：专注力
        self.show_philosophy()

    def intro_cocktail_party(self):
        """开场：鸡尾酒会效应 (修复 ConcentricCircles 报错)"""
        
        title = Text("EP05: 信噪比 (SNR)", font_size=54, color=IT_BLUE, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("如何在噪音中听到声音？", font_size=28, color=IT_GRAY).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 场景：嘈杂的聚会
        # 中心：目标说话者
        speaker = Dot(color=IT_GREEN, radius=0.2).move_to(LEFT * 2)
        speaker_label = Text("说话者", font_size=20, color=IT_GREEN).next_to(speaker, DOWN)
        
        # 听众
        listener = Dot(color=IT_BLUE, radius=0.2).move_to(RIGHT * 2)
        listener_label = Text("听众", font_size=20, color=IT_BLUE).next_to(listener, DOWN)
        
        # 噪音源 (周围随机分布的点)
        noise_sources = VGroup()
        for _ in range(15):
            pos = np.array([random.uniform(-5, 5), random.uniform(-3, 2), 0])
            # 避开中间区域
            if np.linalg.norm(pos) > 1.5:
                d = Dot(pos, color=IT_RED, radius=0.1)
                noise_sources.add(d)
                
        self.play(
            FadeIn(speaker), Write(speaker_label),
            FadeIn(listener), Write(listener_label),
            FadeIn(noise_sources)
        )
        
        # 动画：声波
        # --- 修复核心：手动创建同心圆 ---
        signal_wave = VGroup(*[
            Circle(radius=r, color=IT_GREEN, stroke_width=2).move_to(speaker.get_center())
            for r in np.linspace(0.5, 4, 4) # 生成4个半径递增的圆
        ])
        
        # 2. 红色的干扰波 (杂乱)
        noise_waves = VGroup()
        for ns in noise_sources:
            circ = Circle(radius=0.5, color=IT_RED, stroke_opacity=0.5, stroke_width=1).move_to(ns)
            noise_waves.add(circ)
            
        self.play(
            Create(signal_wave, lag_ratio=0.3), # 增加 lag_ratio 让波纹有扩散感
            FadeIn(noise_waves, lag_ratio=0.1),
            run_time=2
        )
        
        # 核心问题
        question = Text("为什么背景太吵，我们就听不清？", font_size=32, color=IT_YELLOW).move_to(DOWN * 2.5)
        self.play(Write(question))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def visualize_snr(self):
        """视觉拆解：波形的叠加"""
        
        LEFT_ZONE = LEFT * 4.0
        RIGHT_ZONE = RIGHT * 2.5
        
        title = Text("解构：信号与噪音", font_size=36, color=IT_BLUE).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # --- 左侧：三个波形图 (垂直排列) ---
        
        # 1. 纯净信号 (Signal)
        ax1 = Axes(x_range=[0, 6], y_range=[-2, 2], x_length=5, y_length=1.2, tips=False).move_to(LEFT_ZONE + UP * 1.5)
        sig_graph = ax1.plot(lambda x: np.sin(2*x), color=IT_GREEN)
        label1 = Text("纯净信号 (S)", font_size=20, color=IT_GREEN).next_to(ax1, UP, buff=0.1)
        
        # 2. 噪音 (Noise)
        ax2 = Axes(x_range=[0, 6], y_range=[-2, 2], x_length=5, y_length=1.2, tips=False).move_to(LEFT_ZONE)
        # 模拟随机噪音
        def noise_func(x):
            return 0.8 * np.sin(10*x) * np.sin(3*x) # 伪随机高频波
        noise_graph = ax2.plot(noise_func, color=IT_RED)
        label2 = Text("环境噪音 (N)", font_size=20, color=IT_RED).next_to(ax2, UP, buff=0.1)
        
        # 3. 接收到的信号 (S + N)
        ax3 = Axes(x_range=[0, 6], y_range=[-3, 3], x_length=5, y_length=1.2, tips=False).move_to(LEFT_ZONE + DOWN * 1.5)
        combined_graph = ax3.plot(lambda x: np.sin(2*x) + 0.8 * np.sin(10*x) * np.sin(3*x), color=IT_BLUE)
        label3 = Text("实际接收 (S+N)", font_size=20, color=IT_BLUE).next_to(ax3, UP, buff=0.1)
        
        # 动画展示
        self.play(Create(ax1), Create(sig_graph), Write(label1))
        self.play(Create(ax2), Create(noise_graph), Write(label2))
        
        # 合成动画
        plus = MathTex("+").move_to((ax1.get_center() + ax2.get_center()) / 2)
        arrow_down = Arrow(ax2.get_bottom(), ax3.get_top(), buff=0.1)
        
        self.play(Write(plus), GrowArrow(arrow_down))
        self.play(Create(ax3), Create(combined_graph), Write(label3))
        
        # --- 右侧：SNR 定义 ---
        
        def_title = Text("信噪比定义", font_size=28, color=IT_YELLOW).move_to(RIGHT_ZONE + UP * 1.5)
        
        # 公式
        formula = MathTex(
            r"SNR = \frac{P_{signal}}{P_{noise}}",
            font_size=48
        ).next_to(def_title, DOWN, buff=0.5)
        
        formula[0][:3].set_color(IT_YELLOW) # SNR
        formula[0][4:11].set_color(IT_GREEN) # Signal
        formula[0][12:].set_color(IT_RED)   # Noise
        
        # dB 公式
        formula_db = MathTex(
            r"SNR_{dB} = 10 \log_{10}(SNR)",
            font_size=36, color=IT_GRAY
        ).next_to(formula, DOWN, buff=0.5)
        
        desc = VGroup(
            Text("信号越强 (S↑)", font_size=24, color=IT_GREEN),
            Text("或者", font_size=20),
            Text("噪音越弱 (N↓)", font_size=24, color=IT_RED),
            Text("信息传输越可靠", font_size=24, color=IT_BLUE)
        ).arrange(DOWN, buff=0.2).next_to(formula_db, DOWN, buff=0.8)
        
        self.play(Write(def_title), Write(formula))
        self.play(Write(formula_db))
        self.play(Write(desc))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def shannon_limit(self):
            """核心定理：香农极限 (布局优化版)"""
            
            title = Text("香农极限 (Shannon Limit)", font_size=36, color=IT_PURPLE).to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            # 1. 核心公式 (位置大幅上移，留出下方空间)
            # 原来是 UP * 1.5，现在上移到 UP * 2.5
            formula = MathTex(
                r"C = B \cdot \log_2(1 + \frac{S}{N})",
                font_size=60
            ).move_to(UP * 2)
            
            formula.set_color_by_tex("C", IT_BLUE)
            formula.set_color_by_tex("B", IT_ORANGE)
            formula.set_color_by_tex("S", IT_GREEN)
            formula.set_color_by_tex("N", IT_RED)
            
            self.play(Write(formula))
            
            # 解释变量 (放在公式下方，紧凑一点)
            explanations = VGroup(
                VGroup(MathTex("C", color=IT_BLUE), Text(": 信道容量 (最大网速)", font_size=24)).arrange(RIGHT),
                VGroup(MathTex("B", color=IT_ORANGE), Text(": 带宽 (路有多宽)", font_size=24)).arrange(RIGHT),
                VGroup(MathTex("S/N", color=IT_YELLOW), Text(": 信噪比 (路况好坏)", font_size=24)).arrange(RIGHT)
            ).arrange(RIGHT, buff=0.5).next_to(formula, DOWN, buff=0.4) # buff减小，贴紧公式
            
            self.play(FadeIn(explanations, shift=UP))
            
            # 2. 视觉隐喻：管道模型 (位置保持不变，或者稍微下移)
            # 左侧：宽管道，多噪音
            LEFT_POS = LEFT * 3.5 + DOWN * 1.5
            RIGHT_POS = RIGHT * 3.5 + DOWN * 1.5
            
            # 管道 A (带宽大，但噪音大)
            pipe_a_outer = Rectangle(width=3, height=2, color=IT_ORANGE)
            pipe_a_label = Text("宽带 (大B)", font_size=24, color=IT_ORANGE).next_to(pipe_a_outer, UP)
            
            # 填充噪音 (红色圆点)
            noise_a = VGroup(*[Dot(point=pipe_a_outer.get_center() + np.array([random.uniform(-1.4,1.4), random.uniform(-0.9,0.9), 0]), color=IT_RED, radius=0.08) for _ in range(30)])
            # 填充信号 (绿色方块 - 只有少量空间)
            signal_a = VGroup(*[Square(side_length=0.2, color=IT_GREEN, fill_opacity=1).move_to(pipe_a_outer.get_center() + np.array([random.uniform(-1.4,1.4), random.uniform(-0.9,0.9), 0])) for _ in range(10)])
            
            group_a = VGroup(pipe_a_outer, pipe_a_label, noise_a, signal_a).move_to(LEFT_POS)
            
            self.play(Create(pipe_a_outer), Write(pipe_a_label))
            self.play(FadeIn(noise_a))
            self.play(FadeIn(signal_a))
            
            # 管道 B (带宽小，但噪音小)
            pipe_b_outer = Rectangle(width=3, height=1, color=IT_ORANGE)
            pipe_b_label = Text("窄带 (小B)", font_size=24, color=IT_ORANGE).next_to(pipe_b_outer, UP)
            
            # 填充噪音 (很少)
            noise_b = VGroup(*[Dot(point=pipe_b_outer.get_center() + np.array([random.uniform(-1.4,1.4), random.uniform(-0.4,0.4), 0]), color=IT_RED, radius=0.08) for _ in range(5)])
            # 填充信号 (很多)
            signal_b = VGroup(*[Square(side_length=0.2, color=IT_GREEN, fill_opacity=1).move_to(pipe_b_outer.get_center() + np.array([random.uniform(-1.4,1.4), random.uniform(-0.4,0.4), 0])) for _ in range(20)])
            
            group_b = VGroup(pipe_b_outer, pipe_b_label, noise_b, signal_b).move_to(RIGHT_POS)
            
            self.play(Create(pipe_b_outer), Write(pipe_b_label))
            self.play(FadeIn(noise_b))
            self.play(FadeIn(signal_b))
            
            # 结论
            conclusion = Text("如果噪音太大(N↑)，即使路很宽(B↑)，也传不了多少信息！", font_size=26, color=IT_YELLOW)
            conclusion.move_to(DOWN * 3.5)
            self.play(Write(conclusion))
            
            self.wait(3)
            self.play(FadeOut(Group(*self.mobjects)))
    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("信噪比的人生哲学", font_size=40, color=IT_BLUE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("这是一个信息过载，但智慧稀缺的时代", font_size=28),
            Text("垃圾信息 (噪音) 淹没了 有效知识 (信号)", font_size=28, color=IT_RED),
            Text("提高人生的信噪比：", font_size=32, color=IT_YELLOW),
            Text("1. 增强信号 (深度学习，核心技能)", font_size=28, color=IT_GREEN),
            Text("2. 屏蔽噪音 (减少刷屏，拒绝无效社交)", font_size=28, color=IT_GREEN),
            Text("专注力，是你最强大的过滤器", font_size=36, color=IT_BLUE, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：纠错码", font_size=40, color=IT_ORANGE).move_to(UP * 0.5)
        desc = Text("完美的系统不是不出错，而是能改错。\n汉明码的几何之美。", font_size=24, color=IT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))