from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 信号 / 信息 / 正确
IT_RED = "#FF2A68"       # 噪音 / 熵 / 错误
IT_BLUE = "#00BFFF"      # 结构 / 编码 / 科技
IT_YELLOW = "#FFD700"    # 核心概念 / 强调
IT_PURPLE = "#8B5CF6"    # 哲学
IT_ORANGE = "#F97316"    # 警告 / 修正
IT_GRAY = "#333333"      # 背景细节
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP04(Scene):
    """信息论 EP04: 冗余的智慧 (本地化+布局修复版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：效率 vs 鲁棒性
        self.intro_redundancy()
        
        # 2. 语言中的冗余 (中文乱序实验)
        self.language_demo()
        
        # 3. 噪声通道模型
        self.noisy_channel_demo()
        
        # 4. 纠错码原理 (布局已修复)
        self.error_correction_logic()
        
        # 5. 哲学升华
        self.show_philosophy()

    def intro_redundancy(self):
        """开场：冗余不是浪费"""
        
        title = Text("EP04: 冗余的智慧", font_size=54, color=IT_ORANGE, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("The Wisdom of Redundancy", font_size=28, color=IT_GRAY).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 对比：压缩 vs 冗余
        # 左侧：压缩包
        zip_icon = VGroup(
            Square(side_length=2, color=IT_BLUE),
            Text("ZIP", font_size=36, color=IT_BLUE)
        ).move_to(LEFT * 3.5)
        
        label_zip = Text("追求效率 (压缩)", font_size=24, color=IT_BLUE).next_to(zip_icon, DOWN)
        
        # 右侧：备份盘
        backup_icon = VGroup(
            Square(side_length=2, color=IT_GREEN),
            Square(side_length=2, color=IT_GREEN).shift(RIGHT*0.3 + UP*0.3),
            Text("COPY", font_size=36, color=IT_GREEN).shift(RIGHT*0.15 + UP*0.15)
        ).move_to(RIGHT * 3.5)
        
        label_backup = Text("追求安全 (冗余)", font_size=24, color=IT_GREEN).next_to(backup_icon, DOWN)
        
        self.play(Create(zip_icon), Write(label_zip))
        self.play(Create(backup_icon), Write(label_backup))
        
        self.wait(1)
        
        question = Text("为什么我们要故意说废话？", font_size=32, color=IT_YELLOW).move_to(DOWN * 2.5)
        self.play(Write(question))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def language_demo(self):
        """语言中的冗余实验 (中文乱序版)"""
        
        title = Text("实验：你能读懂这句话吗？", font_size=36, color=IT_BLUE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 1. 乱序文本
        # "研表究明，汉字的序顺并不定一能影阅响读"
        scrambled_str = "研表究明，汉字的序顺\n并不定一能影阅响读"
        txt_obj = Text(scrambled_str, font_size=44, color=IT_GREEN, line_spacing=1.5)
        
        self.play(Write(txt_obj))
        self.wait(2)
        
        # 提问
        question = Text("虽然顺序乱了，但你依然读得懂", font_size=24, color=IT_YELLOW).next_to(txt_obj, DOWN, buff=1.0)
        self.play(FadeIn(question, shift=UP))
        self.wait(1)
        
        # 2. 还原文本
        correct_str = "研究表明，汉字的顺序\n并不一定能影响阅读"
        restored_obj = Text(correct_str, font_size=44, color=IT_BLUE, line_spacing=1.5)
        
        self.play(Transform(txt_obj, restored_obj))
        
        # 3. 解释
        # 中文冗余度很高
        expl = VGroup(
            Text("中文拥有极高的冗余度", font_size=28),
            Text("上下文限制了字符的可能性", font_size=28),
            Text("大脑会自动纠错！", font_size=32, color=IT_ORANGE, weight=BOLD)
        ).arrange(DOWN, buff=0.3).to_edge(DOWN, buff=1.0)
        
        self.play(FadeOut(question))
        self.play(Write(expl))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def noisy_channel_demo(self):
        """噪声通道模型"""
        
        title = Text("现实世界充满噪声", font_size=36, color=IT_RED).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # 布局
        alice = Text("发送者", font_size=24, color=IT_BLUE).move_to(LEFT * 5)
        bob = Text("接收者", font_size=24, color=IT_BLUE).move_to(RIGHT * 5)
        
        channel_line = Line(LEFT * 4, RIGHT * 4, color=IT_GRAY)
        
        self.play(Write(alice), Write(bob), Create(channel_line))
        
        # 发送
        bit = Text("0", font_size=36, color=IT_GREEN).next_to(alice, RIGHT)
        self.play(FadeIn(bit))
        
        # 传输
        self.play(bit.animate.move_to(ORIGIN), run_time=1)
        
        # 噪声
        noise = Text("⚡", font_size=60, color=IT_RED).move_to(UP * 1)
        self.play(FadeIn(noise, scale=0.5), run_time=0.2)
        
        # 翻转
        bit_corrupted = Text("1", font_size=36, color=IT_RED).move_to(ORIGIN)
        self.play(Transform(bit, bit_corrupted), run_time=0.2)
        self.play(FadeOut(noise), run_time=0.5)
        
        # 接收
        self.play(bit.animate.next_to(bob, LEFT), run_time=1)
        
        # 困惑
        confused = Text("?", font_size=36, color=IT_YELLOW).next_to(bob, UP)
        self.play(Write(confused))
        
        fail_text = Text("没有冗余，错误无法被发现！", font_size=28, color=IT_RED).move_to(DOWN * 1.5)
        self.play(Write(fail_text))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def error_correction_logic(self):
            """纠错码原理：重复码 (垂直压缩版)"""
            
            LEFT_ZONE = LEFT * 4.0
            RIGHT_ZONE = RIGHT * 2.5 
            
            title = Text("解决方案：重复 (Repetition Code)", font_size=36, color=IT_GREEN).to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            # 1. 左侧：编码过程 (保持不变)
            src_label = Text("原始信号:", font_size=24, color=IT_BLUE).move_to(LEFT_ZONE + UP * 1.5)
            src_bit = Text("0", font_size=48, color=IT_BLUE).next_to(src_label, DOWN)
            
            arrow_code = Arrow(UP, DOWN, color=IT_GRAY).next_to(src_bit, DOWN)
            
            code_label = Text("增加冗余 (编码):", font_size=24, color=IT_GREEN).next_to(arrow_code, DOWN)
            code_bits = Text("0 0 0", font_size=48, color=IT_GREEN).next_to(code_label, DOWN)
            
            self.play(Write(src_label), Write(src_bit))
            self.play(GrowArrow(arrow_code), Write(code_label))
            self.play(TransformFromCopy(src_bit, code_bits))
            
            # 2. 模拟传输与噪声
            trans_bits = code_bits.copy()
            
            # --- 修复核心：大幅上移起始点 ---
            # 移到屏幕上方 UP*2.5，给下面留出最大空间
            self.play(trans_bits.animate.move_to(RIGHT_ZONE + UP * 1.5))
            
            # 噪声攻击
            lightning = Text("⚡", font_size=40, color=IT_RED).move_to(trans_bits.get_center() + UP*0.5)
            self.play(FadeIn(lightning, scale=0.5))
            
            # 变成 "0 1 0"
            corrupted_bits = Text("0 1 0", font_size=48).move_to(trans_bits.get_center())
            corrupted_bits[0].set_color(IT_GREEN)
            corrupted_bits[1].set_color(IT_RED)
            corrupted_bits[2].set_color(IT_GREEN)
            
            self.play(Transform(trans_bits, corrupted_bits))
            self.play(FadeOut(lightning))
            
            # 3. 右侧：解码逻辑 (极度紧凑布局)
            
            # 箭头1 (缩短 + 紧贴)
            decode_arrow = Arrow(UP, DOWN, color=IT_GRAY).scale(0.5)
            decode_arrow.next_to(trans_bits, DOWN, buff=0.1)
            
            # 核心逻辑行：将标签和投票结果放在同一行！
            # 格式： [标签] [0] [1] [0]
            logic_label = Text("投票:", font_size=24, color=IT_YELLOW)
            v1 = Text("0", font_size=24, color=IT_GREEN)
            v2 = Text("1", font_size=24, color=IT_RED)
            v3 = Text("0", font_size=24, color=IT_GREEN)
            
            logic_row = VGroup(logic_label, v1, v2, v3).arrange(RIGHT, buff=0.2)
            logic_row.next_to(decode_arrow, DOWN, buff=0.1)
            
            # 箭头2 (缩短 + 紧贴)
            result_arrow = Arrow(UP, DOWN, color=IT_YELLOW).scale(0.5)
            result_arrow.next_to(logic_row, DOWN, buff=0.1)
            
            # 最终结果
            final_result = Text("0", font_size=48, color=IT_BLUE).next_to(result_arrow, DOWN, buff=0.1)
            
            # 标签放回右侧 (节省垂直空间，且现在右侧空间足够)
            final_tag = Text("✔ 修正成功", font_size=20, color=IT_GREEN).next_to(final_result, RIGHT, buff=0.2)
            
            self.play(GrowArrow(decode_arrow))
            self.play(Write(logic_row))
            self.play(GrowArrow(result_arrow), Write(final_result))
            self.play(Write(final_tag))
            
            # 4. 总结 (底部)
            # 此时上面的内容大约结束在 DOWN*0.5 左右，底部空间非常充裕
            summary = Text("牺牲效率(发3倍数据) -> 换取可靠性", font_size=28, color=IT_ORANGE).to_edge(DOWN, buff=0.5)
            self.play(Write(summary))
            
            self.wait(3)
            self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("冗余的人生哲学", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("我们总是追求极致的高效", font_size=28),
            Text("但生命系统充满了冗余 (双肾、双肺)", font_size=28, color=IT_GRAY),
            Text("效率不是一切，容错率才是关键", font_size=32, color=IT_ORANGE, weight=BOLD),
            Text("冗余是生存的护城河", font_size=36, color=IT_GREEN, weight=BOLD),
            Text("永远给自己留一个 Plan B", font_size=36, color=IT_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：信噪比", font_size=40, color=IT_BLUE).move_to(UP * 0.5)
        desc = Text("如何在一个喧嚣的世界中，听清真理的声音？\n专注力就是过滤器。", font_size=24, color=IT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))