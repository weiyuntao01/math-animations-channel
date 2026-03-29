from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 信号 / 正确 / 偶校验成功
IT_RED = "#FF2A68"       # 噪音 / 错误 / 奇校验报警
IT_BLUE = "#00BFFF"      # 数据位
IT_YELLOW = "#FFD700"    # 校验位 / 核心概念
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题
IT_GRAY = "#333333"      # 辅助线 / 背景 (已补全此变量)
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP06(Scene):
    """信息论 EP06: 纠错码 (全量修复版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：脆弱的数据
        self.intro_fragility()
        
        # 2. 基础：奇偶校验 (Parity Bit)
        self.parity_concept()
        
        # 3. 核心：汉明圆可视化 (已修复布局和变量报错)
        self.hamming_circles_demo()
        
        # 4. 哲学升华
        self.show_philosophy()

    def intro_fragility(self):
        """开场：数据很脆弱，重复很昂贵"""
        
        title = Text("EP06: 纠错码 (ECC)", font_size=54, color=IT_BLUE, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("Error Correction Code", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        last_recap = Text("上一集：重复码 (Repetition)", font_size=24, color=WHITE).move_to(UP * 0.5)
        
        data_src = Text("1", font_size=48, color=IT_GREEN).move_to(LEFT * 2)
        arrow = Arrow(LEFT, RIGHT, color=WHITE).next_to(data_src, RIGHT)
        data_coded = Text("1 1 1", font_size=48, color=IT_GREEN).next_to(arrow, RIGHT)
        
        self.play(Write(last_recap))
        self.play(FadeIn(data_src), GrowArrow(arrow), FadeIn(data_coded))
        
        waste_label = Text("效率太低！(浪费 200%)", font_size=28, color=IT_RED).next_to(data_coded, DOWN)
        self.play(Write(waste_label))
        
        self.wait(1)
        
        question = Text("能不能只增加一点点冗余，\n就能定位并修正错误？", font_size=32, color=IT_YELLOW).move_to(DOWN * 2.5)
        self.play(Write(question))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def parity_concept(self):
        """基础概念：奇偶校验"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("基础：奇偶校验 (Parity Check)", font_size=36, color=IT_GREEN).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # 1. 左侧：数据块
        d1 = Square(side_length=1, fill_color=IT_BLUE, fill_opacity=0.5).move_to(LEFT_ZONE + LEFT*1.1)
        d2 = Square(side_length=1, fill_color=IT_BLUE, fill_opacity=0.5).move_to(LEFT_ZONE)
        d3 = Square(side_length=1, fill_color=IT_BLUE, fill_opacity=0.5).move_to(LEFT_ZONE + RIGHT*1.1)
        
        t1 = Text("1", font_size=40).move_to(d1)
        t2 = Text("0", font_size=40).move_to(d2)
        t3 = Text("1", font_size=40).move_to(d3)
        
        data_group = VGroup(d1, d2, d3, t1, t2, t3)
        label_data = Text("数据位", font_size=24, color=IT_BLUE).next_to(d2, UP)
        
        self.play(FadeIn(data_group), Write(label_data))
        
        # 2. 右侧：校验逻辑
        logic_title = Text("规则：1 的总数必须是偶数", font_size=28, color=WHITE).move_to(RIGHT_ZONE + UP)
        self.play(Write(logic_title))
        
        current_sum = Text("当前有 2 个 1 (偶数)", font_size=24, color=WHITE).next_to(logic_title, DOWN, buff=0.5)
        self.play(Write(current_sum))
        
        # 添加校验位
        p_box = Square(side_length=1, fill_color=IT_YELLOW, fill_opacity=0.5).next_to(d3, RIGHT, buff=0.1)
        p_val = Text("0", font_size=40, color=BLACK).move_to(p_box)
        p_label = Text("校验位", font_size=24, color=IT_YELLOW).next_to(p_box, UP)
        
        self.play(Create(p_box), Write(p_val), Write(p_label))
        
        final_check = Text("总和 = 2 (通过)", font_size=24, color=IT_GREEN).next_to(current_sum, DOWN, buff=0.5)
        self.play(Write(final_check))
        
        # 3. 模拟错误
        self.play(t2.animate.become(Text("1", font_size=40, color=IT_RED).move_to(d2)))
        
        error_msg = Text("总和 = 3 (奇数!) -> 报错", font_size=28, color=IT_RED).move_to(RIGHT_ZONE + DOWN * 1.5)
        self.play(Transform(final_check, error_msg))
        
        limit_text = Text("局限：知道错了，但不知道错在哪", font_size=24, color=WHITE).to_edge(DOWN, buff=1.0)
        self.play(Write(limit_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def hamming_circles_demo(self):
            """核心：汉明圆可视化 (坐标精修版)"""
            
            # 布局定义
            LEFT_ZONE = LEFT * 3.5
            RIGHT_ZONE = RIGHT * 3.5
            
            title = Text("汉明码 (Hamming Code)：精确定位", font_size=36, color=IT_PURPLE).to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            # --- 1. 绘制左侧汉明圆 (基于几何中心微调) ---
            # 设定整体的中心点，稍微下移一点以保持视觉平衡
            CENTER_POS = LEFT_ZONE + DOWN * 0.2
            R = 1.6 # 圆半径
            OFFSET = 0.9 # 圆心偏移量
            
            # 三个圆心位置
            c1_pos = CENTER_POS + UP * OFFSET           # 上 (黄)
            c2_pos = CENTER_POS + DOWN * 0.6 + LEFT * OFFSET  # 左下 (蓝)
            c3_pos = CENTER_POS + DOWN * 0.6 + RIGHT * OFFSET # 右下 (红)
            
            circle1 = Circle(radius=R, color=IT_YELLOW, stroke_width=4).move_to(c1_pos)
            circle2 = Circle(radius=R, color=IT_BLUE, stroke_width=4).move_to(c2_pos)
            circle3 = Circle(radius=R, color=IT_RED, stroke_width=4).move_to(c3_pos)
            
            # --- 关键修改：手动指定7个数字的精确位置，防止压线 ---
            
            # d4: 正中心 (三个圆交集)
            pos_d4 = CENTER_POS + UP * 0.1 
            
            # d1: 上左交集 (黄+蓝) -> 往左上方移
            pos_d1 = CENTER_POS + UP * 0.8 + LEFT * 0.6
            
            # d2: 上右交集 (黄+红) -> 往右上方移
            pos_d2 = CENTER_POS + UP * 0.8 + RIGHT * 0.6
            
            # d3: 下方交集 (蓝+红) -> 往正下方移
            pos_d3 = CENTER_POS + DOWN * 0.8
            
            # p1: 上方独占区域 (校验位1)
            pos_p1 = c1_pos + UP * 0.8
            
            # p2: 左下独占区域 (校验位2)
            pos_p2 = c2_pos + LEFT * 0.6 + DOWN * 0.4
            
            # p3: 右下独占区域 (校验位3)
            pos_p3 = c3_pos + RIGHT * 0.6 + DOWN * 0.4
            
            # 初始正确数据: 1 0 1 1
            # 字体稍微缩小一点，避免拥挤
            NUM_SIZE = 32
            txt_d1 = Text("1", font_size=NUM_SIZE).move_to(pos_d1)
            txt_d2 = Text("0", font_size=NUM_SIZE).move_to(pos_d2)
            txt_d3 = Text("1", font_size=NUM_SIZE).move_to(pos_d3)
            txt_d4 = Text("1", font_size=NUM_SIZE).move_to(pos_d4)
            
            txt_p1 = Text("0", font_size=NUM_SIZE, color=IT_YELLOW).move_to(pos_p1)
            txt_p2 = Text("1", font_size=NUM_SIZE, color=IT_BLUE).move_to(pos_p2)
            txt_p3 = Text("0", font_size=NUM_SIZE, color=IT_RED).move_to(pos_p3)
            
            circles = VGroup(circle1, circle2, circle3)
            numbers = VGroup(txt_d1, txt_d2, txt_d3, txt_d4, txt_p1, txt_p2, txt_p3)
            
            self.play(Create(circles), Write(numbers))
            
            # --- 阶段一：规则介绍 ---
            rule_title = Text("规则：", font_size=28, color=IT_GREEN)
            rule_desc1 = Text("每个圆圈内的数字之和", font_size=24, color=WHITE)
            rule_desc2 = Text("必须是偶数 (Even)", font_size=24, color=WHITE)
            
            rule_group = VGroup(rule_title, rule_desc1, rule_desc2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            rule_group.move_to(RIGHT_ZONE + UP * 1.5)
            
            self.play(Write(rule_group))
            
            status_text = Text("当前状态：完美平衡", font_size=24, color=IT_GREEN).next_to(rule_group, DOWN, buff=0.5)
            self.play(Write(status_text))
            self.wait(1)
            
            # --- 2. 模拟错误 ---
            self.play(
                txt_d1.animate.become(Text("0", font_size=NUM_SIZE, color=IT_RED).move_to(pos_d1)),
                FadeOut(status_text)
            )
            
            # --- 阶段二：诊断模式 ---
            self.play(FadeOut(rule_group))
            
            diag_title = Text("⚠️ 检测到错误", font_size=32, color=IT_RED).move_to(RIGHT_ZONE + UP * 2.5)
            self.play(Write(diag_title))
            
            # --- 3. 逐个圆圈检查 ---
            self.play(circle1.animate.set_color(IT_RED).set_stroke(width=8))
            res1 = VGroup(
                Text("黄圆:", font_size=24, color=IT_YELLOW),
                Text("和为奇数 -> 异常!", font_size=24, color=IT_RED)
            ).arrange(RIGHT).next_to(diag_title, DOWN, buff=0.5).align_to(diag_title, LEFT)
            self.play(Write(res1))
            
            self.play(circle2.animate.set_color(IT_RED).set_stroke(width=8))
            res2 = VGroup(
                Text("蓝圆:", font_size=24, color=IT_BLUE),
                Text("和为奇数 -> 异常!", font_size=24, color=IT_RED)
            ).arrange(RIGHT).next_to(res1, DOWN, buff=0.3).align_to(res1, LEFT)
            self.play(Write(res2))
            
            self.play(circle3.animate.set_color(IT_GREEN))
            res3 = VGroup(
                Text("红圆:", font_size=24, color=IT_RED),
                Text("和为偶数 -> 正常", font_size=24, color=IT_GREEN)
            ).arrange(RIGHT).next_to(res2, DOWN, buff=0.3).align_to(res1, LEFT)
            self.play(Write(res3))
            
            # --- 4. 逻辑推理 ---
            logic_line = Line(
                start=LEFT*2, end=RIGHT*2, 
                color=IT_GRAY, 
                stroke_width=4
            ).next_to(res3, DOWN, buff=0.3).move_to(RIGHT_ZONE + DOWN * 0.5)
            
            self.play(Create(logic_line))
            
            logic_text = Text("位置在：黄圆内 & 蓝圆内 & 红圆外", font_size=22, color=WHITE).next_to(logic_line, DOWN, buff=0.3)
            self.play(Write(logic_text))
            
            # --- 5. 视觉聚焦与修正 ---
            target_circle = Circle(radius=0.4, color=WHITE, stroke_width=5).move_to(pos_d1)
            self.play(Create(target_circle))
            
            found_text = Text("锁定位置：d1", font_size=28, color=IT_GREEN, weight=BOLD).next_to(logic_text, DOWN, buff=0.3)
            self.play(Write(found_text))
            
            self.play(
                Transform(txt_d1, Text("1", font_size=NUM_SIZE, color=IT_GREEN).move_to(pos_d1)),
                FadeOut(target_circle)
            )
            
            self.play(
                circle1.animate.set_color(IT_YELLOW).set_stroke(width=4),
                circle2.animate.set_color(IT_BLUE).set_stroke(width=4),
                circle3.animate.set_color(IT_RED).set_stroke(width=4),
                FadeOut(diag_title), FadeOut(res1), FadeOut(res2), FadeOut(res3), FadeOut(logic_line), FadeOut(logic_text), FadeOut(found_text)
            )
            
            final_ok = Text("系统恢复正常", font_size=32, color=IT_GREEN).move_to(RIGHT_ZONE)
            self.play(Write(final_ok))
            self.wait(2)
            
            self.play(FadeOut(Group(*self.mobjects)))
    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("完美的系统", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("世界是不完美的，噪声无处不在", font_size=28, color=WHITE),
            Text("脆弱的系统试图\"避免\"错误", font_size=28, color=IT_RED),
            Text("强大的系统能够\"修正\"错误", font_size=32, color=IT_GREEN, weight=BOLD),
            Text("真正的完美，不是不犯错", font_size=36, color=IT_YELLOW, weight=BOLD),
            Text("而是拥有自我修复的能力", font_size=36, color=WHITE, weight=BOLD)
        ).arrange(DOWN, buff=0.6)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        next_ep = Text("下期预告：霍夫曼编码", font_size=40, color=IT_BLUE).move_to(UP * 0.5)
        desc = Text("如何用最短的符号表达最多的信息？\n精力的最优分配学。", font_size=24, color=WHITE).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))