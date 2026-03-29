from manim import *
import numpy as np
import random

# --- 信息论系列配色 (已补全 IT_PURPLE) ---
IT_GREEN = "#00FF41"     # 信号 / 信息 / 有效
IT_RED = "#FF2A68"       # 排除 / 错误 / 噪音
IT_BLUE = "#00BFFF"      # 结构 / 问题
IT_YELLOW = "#FFD700"    # 目标 / 答案 / 强调
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题 / 升华 (新增)
IT_GRAY = "#333333"      # 被排除的背景
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP02(Scene):
    """信息论 EP02: 比特的诞生 (修复版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：莎士比亚的比特
        self.intro_choice()
        
        # 2. 游戏演示：20个问题 (猜数字)
        self.game_of_20_questions()
        
        # 3. 原理揭秘：二分查找与对数
        self.explain_logarithm()
        
        # 4. 物理本质：为什么是二进制？
        self.why_binary()
        
        # 5. 哲学升华
        self.show_philosophy()

    def intro_choice(self):
        """开场：To be or not to be"""
        
        # 引用
        quote = Text("To be, or not to be?", font_size=48, color=IT_GREEN)
        quote.move_to(UP * 0.5)
        
        translation = Text("生存还是毁灭，这是一个(二进制)问题。", font_size=24, color=IT_BLUE)
        translation.next_to(quote, DOWN, buff=0.5)
        
        self.play(Write(quote), FadeIn(translation))
        self.wait(1)
        
        # 视觉化：0 和 1 的闪烁
        binary_zero = Text("0", font_size=96, color=IT_RED).move_to(LEFT * 3)
        binary_one = Text("1", font_size=96, color=IT_GREEN).move_to(RIGHT * 3)
        
        self.play(
            FadeOut(quote), FadeOut(translation),
            FadeIn(binary_zero), FadeIn(binary_one)
        )
        
        # 标题
        title = Text("EP02: 比特的诞生", font_size=54, color=IT_YELLOW, weight=BOLD).set_z_index(10)
        subtitle = Text("The Birth of the Bit", font_size=32, color=IT_GRAY).next_to(title, DOWN, buff=0.3).set_z_index(10)
        
        # 0/1 变淡作为背景
        self.play(
            binary_zero.animate.set_opacity(0.2),
            binary_one.animate.set_opacity(0.2),
            Write(title),
            FadeIn(subtitle, shift=UP)
        )
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def game_of_20_questions(self):
        """核心演示：猜数字游戏 (16格)"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("游戏：猜出我心中的数字 (1-16)", font_size=32, color=IT_BLUE).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # 1. 左侧：16个数字网格
        grid = VGroup()
        cells = [] # 存储引用
        target_num = 11 # 假设目标是11
        
        for i in range(16):
            num = i + 1
            square = Square(side_length=1.0, color=IT_GREEN, stroke_width=2)
            label = Integer(num, font_size=32, color=WHITE).move_to(square)
            
            # 如果是目标，标记一下(演示时不显示，逻辑里用)
            is_target = (num == target_num)
            
            cell = VGroup(square, label)
            cells.append(cell)
            grid.add(cell)
            
        grid.arrange_in_grid(rows=4, cols=4, buff=0.1)
        grid.move_to(LEFT_ZONE + DOWN * 0.5)
        
        self.play(FadeIn(grid, lag_ratio=0.05))
        
        # 2. 右侧：提问过程
        q_label = Text("提问过程：", font_size=24, color=IT_YELLOW)
        
        questions = VGroup(
            Text("1. 在前 8 个吗？", font_size=20),
            Text("2. 在 9-12 之间吗？", font_size=20),
            Text("3. 在 9-10 之间吗？", font_size=20),
            Text("4. 是 11 吗？", font_size=20, color=IT_GREEN, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        
        answers = VGroup(
            Text("NO (排除前8)", font_size=20, color=IT_RED),
            Text("YES (排除后4)", font_size=20, color=IT_GREEN),
            Text("NO (排除9,10)", font_size=20, color=IT_RED),
            Text("YES (找到目标!)", font_size=20, color=IT_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        
        # 组合布局
        q_layout = VGroup()
        for q, a in zip(questions, answers):
            row = VGroup(q, a).arrange(RIGHT, buff=0.3)
            q_layout.add(row)
        q_layout.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        q_layout.move_to(RIGHT_ZONE)
        
        q_label.next_to(q_layout, UP, buff=0.5, aligned_edge=LEFT)
        self.play(Write(q_label))
        
        # --- 互动动画 ---
        
        # 第一轮：问前8个 (1-8)
        self.play(Write(questions[0]))
        
        # 高亮前8个
        highlight_1 = SurroundingRectangle(grid[:8], color=IT_BLUE)
        self.play(Create(highlight_1))
        self.wait(0.5)
        
        # 答案 NO -> 排除 1-8
        self.play(Write(answers[0]))
        self.play(
            grid[:8].animate.set_color(IT_GRAY).set_opacity(0.3),
            FadeOut(highlight_1)
        )
        
        # 第二轮：问 9-12
        self.play(Write(questions[1]))
        
        # 高亮 9-12 (索引 8-11)
        # 注意：VGroup切片
        target_subset = grid[8:12]
        highlight_2 = SurroundingRectangle(target_subset, color=IT_BLUE)
        self.play(Create(highlight_2))
        self.wait(0.5)
        
        # 答案 YES -> 排除 13-16
        self.play(Write(answers[1]))
        self.play(
            grid[12:].animate.set_color(IT_GRAY).set_opacity(0.3),
            FadeOut(highlight_2)
        )
        
        # 第三轮：问 9-10
        self.play(Write(questions[2]))
        highlight_3 = SurroundingRectangle(grid[8:10], color=IT_BLUE)
        self.play(Create(highlight_3))
        
        # 答案 NO -> 排除 9-10
        self.play(Write(answers[2]))
        self.play(
            grid[8:10].animate.set_color(IT_GRAY).set_opacity(0.3),
            FadeOut(highlight_3)
        )
        
        # 第四轮：剩下 11, 12。问是 11 吗？
        self.play(Write(questions[3]))
        target_cell = cells[10] # 数字11
        self.play(target_cell.animate.scale(1.2).set_color(IT_YELLOW))
        
        self.play(Write(answers[3]))
        
        # 排除 12
        self.play(cells[11].animate.set_color(IT_GRAY).set_opacity(0.3))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def explain_logarithm(self):
        """数学原理：对数的意义"""
        
        title = Text("二分查找 (Binary Search)", font_size=40, color=IT_BLUE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 1. 核心公式
        formula = MathTex(
            r"\text{Steps} = \log_2 N",
            font_size=60
        )
        formula.set_color_by_tex("Steps", IT_YELLOW)
        formula.set_color_by_tex("N", IT_GREEN)
        
        self.play(Write(formula))
        self.play(formula.animate.shift(UP * 2))
        
        # 2. 算式演示 (左右分栏文字)
        
        # 例子 1
        ex1_left = Text("16 个数字", font_size=28)
        ex1_arrow = Arrow(LEFT, RIGHT, color=IT_GRAY)
        ex1_right = MathTex(r"\log_2 16 = 4 \text{ bits}", font_size=32, color=IT_GREEN)
        row1 = VGroup(ex1_left, ex1_arrow, ex1_right).arrange(RIGHT, buff=0.5)
        
        # 例子 2
        ex2_left = Text("1000 个数字", font_size=28)
        ex2_arrow = Arrow(LEFT, RIGHT, color=IT_GRAY)
        ex2_right = MathTex(r"\log_2 1000 \approx 10 \text{ bits}", font_size=32, color=IT_GREEN)
        row2 = VGroup(ex2_left, ex2_arrow, ex2_right).arrange(RIGHT, buff=0.5)
        
        # 例子 3 (爆炸增长)
        ex3_left = Text("地球所有沙子 (10^19)", font_size=28)
        ex3_arrow = Arrow(LEFT, RIGHT, color=IT_GRAY)
        ex3_right = MathTex(r"\log_2 10^{19} \approx 64 \text{ bits}", font_size=32, color=IT_YELLOW)
        row3 = VGroup(ex3_left, ex3_arrow, ex3_right).arrange(RIGHT, buff=0.5)
        
        examples = VGroup(row1, row2, row3).arrange(DOWN, buff=1.0).next_to(formula, DOWN, buff=1.0)
        
        self.play(FadeIn(row1, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(row2, shift=UP))
        self.wait(0.5)
        self.play(FadeIn(row3, shift=UP))
        
        # 核心结论
        conclusion = Text("比特是能够将不确定性减半的单位", font_size=28, color=IT_BLUE)
        conclusion.to_edge(DOWN, buff=1.0)
        self.play(Write(conclusion))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def why_binary(self):
        """为什么选择二进制？(物理鲁棒性)"""
        
        title = Text("为什么不是 10 进制？", font_size=36, color=IT_RED).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 布局
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 1. 左侧：10进制的电压 (容易混淆)
        # 画一个数轴，分10格
        axis_10 = NumberLine(x_range=[0, 10, 1], length=5, include_ticks=True).move_to(LEFT_ZONE)
        label_10 = Text("10 种电压状态", font_size=24).next_to(axis_10, UP)
        
        # 模拟干扰
        signal_dot = Dot(axis_10.n2p(5), color=IT_YELLOW) # 原始信号 5
        signal_label = Text("5", font_size=20, color=IT_YELLOW).next_to(signal_dot, DOWN)
        
        self.play(Create(axis_10), Write(label_10))
        self.play(FadeIn(signal_dot), Write(signal_label))
        
        # 干扰动画：点在 4.5 到 5.5 之间晃动
        self.play(signal_dot.animate.move_to(axis_10.n2p(5.4)), run_time=0.2)
        self.play(signal_dot.animate.move_to(axis_10.n2p(4.7)), run_time=0.2)
        
        error_text = Text("微小干扰 = 读错数字", font_size=24, color=IT_RED).next_to(axis_10, DOWN, buff=0.8)
        self.play(Write(error_text))
        
        # 2. 右侧：2进制的电压 (鲁棒性)
        # 画一个开关
        switch_off = Circle(radius=0.5, color=IT_RED).move_to(RIGHT_ZONE + DOWN)
        switch_on = Circle(radius=0.5, color=IT_GREEN, fill_opacity=1).move_to(RIGHT_ZONE + UP)
        
        label_0 = Text("0 (0V)", font_size=24).next_to(switch_off, RIGHT)
        label_1 = Text("1 (5V)", font_size=24).next_to(switch_on, RIGHT)
        
        wire = Line(switch_off.get_top(), switch_on.get_bottom(), color=IT_GRAY)
        
        label_2 = Text("2 种极端状态", font_size=24).next_to(switch_on, UP, buff=0.5)
        
        self.play(
            Create(switch_off), Write(label_0),
            Create(switch_on), Write(label_1),
            Create(wire), Write(label_2)
        )
        
        # 鲁棒性说明
        robust_text = Text("哪怕有干扰，\n开依然是开，关依然是关", font_size=24, color=IT_GREEN).next_to(switch_off, DOWN, buff=0.8)
        self.play(Write(robust_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("比特的人生哲学", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("人生就是一连串的二分查找", font_size=28),
            Text("每一次选择 (Yes/No)", font_size=28, color=IT_BLUE),
            Text("都在排除一半的可能性", font_size=28, color=IT_RED),
            Text("选择即放弃", font_size=36, color=IT_YELLOW, weight=BOLD),
            Text("智慧，就是排除错误选项的速度", font_size=32, color=IT_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：熵增定律", font_size=40, color=IT_RED).move_to(UP * 0.5)
        desc = Text("为什么房间会自动变乱？\n自律的本质是逆熵。", font_size=24, color=IT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))