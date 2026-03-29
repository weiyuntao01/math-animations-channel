from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 信号 / 高频 / 短码
IT_RED = "#FF2A68"       # 噪音 / 低频 / 长码
IT_BLUE = "#00BFFF"      # 结构 / 中频
IT_YELLOW = "#FFD700"    # 核心概念 / 强调
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题
IT_GRAY = "#333333"      # 背景细节
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP07(Scene):
    """信息论 EP07: 霍夫曼编码 (修复 CENTER 报错版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：莫尔斯电码的启示
        self.intro_morse()
        
        # 2. 问题：等长 vs 变长
        self.problem_statement()
        
        # 3. 核心：霍夫曼树构建动画
        self.build_huffman_tree()
        
        # 4. 结果对比：压缩了多少？
        self.compare_results()
        
        # 5. 哲学升华：精力管理
        self.show_philosophy()

    def intro_morse(self):
        """开场：从莫尔斯电码说起"""
        
        title = Text("EP07: 霍夫曼编码", font_size=54, color=IT_BLUE, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("The Art of Compression (压缩的艺术)", font_size=28, color=IT_GRAY).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 莫尔斯电码示例
        # E (.) vs Q (--.-)
        
        # 左侧 E
        e_group = VGroup()
        e_char = Text("E", font_size=80, color=IT_GREEN)
        e_code = Text("●", font_size=60, color=IT_GREEN).next_to(e_char, DOWN)
        e_label = Text("高频 (11%)", font_size=24, color=IT_GRAY).next_to(e_code, DOWN)
        e_group.add(e_char, e_code, e_label).move_to(LEFT * 3.5)
        
        # 右侧 Q
        q_group = VGroup()
        q_char = Text("Q", font_size=80, color=IT_RED)
        q_code = Text("— — ● —", font_size=60, color=IT_RED).next_to(q_char, DOWN)
        q_label = Text("低频 (0.1%)", font_size=24, color=IT_GRAY).next_to(q_code, DOWN)
        q_group.add(q_char, q_code, q_label).move_to(RIGHT * 3.5)
        
        self.play(FadeIn(e_group, shift=RIGHT))
        self.wait(0.5)
        self.play(FadeIn(q_group, shift=LEFT))
        
        # 核心法则
        rule = Text("法则：常用的短一点，不常用的长一点", font_size=32, color=IT_YELLOW).move_to(DOWN * 2.5)
        self.play(Write(rule))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def problem_statement(self):
        """问题：如何给 ABCD 编码？"""
        
        title = Text("任务：传输字符串 \"A A A B C D\"", font_size=36, color=IT_BLUE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 统计频率
        # A: 50%, B: 25%, C: 12.5%, D: 12.5%
        
        freq_box = VGroup(
            Text("符号频率分布：", font_size=28, color=IT_YELLOW),
            Text("A: 50% (高频)", font_size=24, color=IT_GREEN),
            Text("B: 25% (中频)", font_size=24, color=IT_BLUE),
            Text("C: 12.5% (低频)", font_size=24, color=IT_RED),
            Text("D: 12.5% (低频)", font_size=24, color=IT_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(LEFT * 3.5)
        
        self.play(FadeIn(freq_box, shift=RIGHT))
        
        # 方案1：等长编码
        fixed_plan = VGroup(
            Text("方案一：等长编码", font_size=28, color=IT_GRAY),
            MathTex(r"A \to 00", color=IT_GRAY),
            MathTex(r"B \to 01", color=IT_GRAY),
            MathTex(r"C \to 10", color=IT_GRAY),
            MathTex(r"D \to 11", color=IT_GRAY),
            Text("平均长度 = 2 bits", font_size=24, color=IT_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(RIGHT * 3.5)
        
        self.play(Write(fixed_plan))
        self.wait(1)
        
        # 提出挑战
        challenge = Text("能不能把平均长度压缩到 2 bits 以下？", font_size=32, color=IT_GREEN).move_to(DOWN * 2.5)
        self.play(Write(challenge))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def build_huffman_tree(self):
        """核心：构建霍夫曼树"""
        
        title = Text("霍夫曼树构建算法", font_size=36, color=IT_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 定义节点样式 helper
        def create_node(label, prob, color, pos):
            circle = Circle(radius=0.5, color=color, fill_opacity=0.2)
            txt = Text(label, font_size=32, color=WHITE).move_to(circle)
            p_txt = Text(str(prob), font_size=20, color=color).next_to(circle, DOWN, buff=0.1)
            grp = VGroup(circle, txt, p_txt).move_to(pos)
            return grp
        
        # 初始位置 (底部)
        BASE_Y = DOWN * 2.5
        node_a = create_node("A", "0.5", IT_GREEN, LEFT * 4 + BASE_Y)
        node_b = create_node("B", "0.25", IT_BLUE, LEFT * 1.5 + BASE_Y)
        node_c = create_node("C", "0.125", IT_RED, RIGHT * 1 + BASE_Y)
        node_d = create_node("D", "0.125", IT_RED, RIGHT * 3.5 + BASE_Y)
        
        self.play(FadeIn(node_a), FadeIn(node_b), FadeIn(node_c), FadeIn(node_d))
        
        # 说明文字
        step_text = Text("步骤：每次找出概率最小的两个合并", font_size=24, color=IT_YELLOW).to_edge(UP, buff=1.5)
        self.play(Write(step_text))
        
        # --- 第一轮合并：C 和 D ---
        self.play(
            node_c.animate.scale(1.1).set_color(IT_YELLOW), 
            node_d.animate.scale(1.1).set_color(IT_YELLOW)
        )
        self.wait(0.5)
        
        # 生成父节点 CD
        pos_cd = (node_c.get_center() + node_d.get_center()) / 2 + UP * 1.5
        node_cd = create_node("Sum", "0.25", IT_BLUE, pos_cd) 
        
        line_c = Line(node_cd[0].get_bottom(), node_c[0].get_top(), color=IT_GRAY)
        line_d = Line(node_cd[0].get_bottom(), node_d[0].get_top(), color=IT_GRAY)
        
        label_0_cd = Text("0", font_size=20, color=IT_BLUE).next_to(line_c, LEFT, buff=0)
        label_1_cd = Text("1", font_size=20, color=IT_BLUE).next_to(line_d, RIGHT, buff=0)
        
        self.play(
            Create(line_c), Create(line_d),
            FadeIn(node_cd),
            Write(label_0_cd), Write(label_1_cd),
            node_c.animate.scale(1/1.1).set_color(IT_RED), 
            node_d.animate.scale(1/1.1).set_color(IT_RED)
        )
        self.wait(1)
        
        # --- 第二轮合并：B 和 CD ---
        self.play(
            node_b.animate.scale(1.1).set_color(IT_YELLOW),
            node_cd.animate.scale(1.1).set_color(IT_YELLOW)
        )
        
        # 父节点 BCD
        pos_bcd = (node_b.get_center() + node_cd.get_center()) / 2 + UP * 1.5
        node_bcd = create_node("Sum", "0.5", IT_GREEN, pos_bcd) 
        
        line_b = Line(node_bcd[0].get_bottom(), node_b[0].get_top(), color=IT_GRAY)
        line_cd = Line(node_bcd[0].get_bottom(), node_cd[0].get_top(), color=IT_GRAY)
        
        label_0_bcd = Text("0", font_size=20, color=IT_GREEN).next_to(line_b, LEFT, buff=0)
        label_1_bcd = Text("1", font_size=20, color=IT_GREEN).next_to(line_cd, RIGHT, buff=0)
        
        self.play(
            Create(line_b), Create(line_cd),
            FadeIn(node_bcd),
            Write(label_0_bcd), Write(label_1_bcd),
            node_b.animate.scale(1/1.1).set_color(IT_BLUE), 
            node_cd.animate.scale(1/1.1).set_color(IT_BLUE)
        )
        self.wait(1)
        
        # --- 第三轮合并：A 和 BCD ---
        self.play(
            node_a.animate.scale(1.1).set_color(IT_YELLOW),
            node_bcd.animate.scale(1.1).set_color(IT_YELLOW)
        )
        
        # 根节点
        pos_root = (node_a.get_center() + node_bcd.get_center()) / 2 + UP * 1.5
        node_root = create_node("Root", "1.0", IT_YELLOW, pos_root)
        
        line_a = Line(node_root[0].get_bottom(), node_a[0].get_top(), color=IT_GRAY)
        line_bcd = Line(node_root[0].get_bottom(), node_bcd[0].get_top(), color=IT_GRAY)
        
        label_0_root = Text("0", font_size=20, color=IT_YELLOW).next_to(line_a, LEFT, buff=0.1)
        label_1_root = Text("1", font_size=20, color=IT_YELLOW).next_to(line_bcd, RIGHT, buff=0.1)
        
        self.play(
            Create(line_a), Create(line_bcd),
            FadeIn(node_root),
            Write(label_0_root), Write(label_1_root),
            node_a.animate.scale(1/1.1).set_color(IT_GREEN), 
            node_bcd.animate.scale(1/1.1).set_color(IT_GREEN)
        )
        
        final_text = Text("路径长度 = 编码长度", font_size=28, color=IT_YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(final_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def compare_results(self):
        """对比：霍夫曼 vs 等长"""
        
        title = Text("编码结果对比", font_size=36, color=IT_BLUE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 1. 左侧：霍夫曼编码表
        table_title = Text("霍夫曼编码表", font_size=24, color=IT_YELLOW).move_to(LEFT * 3.5 + UP * 1.5)
        
        rows = VGroup(
            Text("A (50%)  -> 0     (1 bit)", font_size=24, color=IT_GREEN),
            Text("B (25%)  -> 10    (2 bits)", font_size=24, color=IT_BLUE),
            Text("C (12.5%)-> 110   (3 bits)", font_size=24, color=IT_RED),
            Text("D (12.5%)-> 111   (3 bits)", font_size=24, color=IT_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(table_title, DOWN, buff=0.5)
        
        self.play(Write(table_title), Write(rows))
        
        # 2. 右侧：计算平均长度
        calc_title = Text("平均长度计算", font_size=24, color=IT_BLUE).move_to(RIGHT * 3.5 + UP * 1.5)
        
        # Avg = 1*0.5 + 2*0.25 + 3*0.125 + 3*0.125
        calc_steps = VGroup(
            MathTex(r"L = 1 \times 0.5 + 2 \times 0.25"),
            MathTex(r"+ 3 \times 0.125 + 3 \times 0.125"),
            MathTex(r"= 0.5 + 0.5 + 0.375 + 0.375"),
            MathTex(r"= 1.75 \text{ bits}", color=IT_GREEN, font_size=40)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(calc_title, DOWN, buff=0.5)
        
        self.play(Write(calc_title), Write(calc_steps))
        
        # 3. 结论对比
        # 修复：移除 aligned_edge=CENTER，arrange默认居中
        comparison = VGroup(
            Text("等长编码: 2.00 bits", font_size=24, color=IT_GRAY),
            Text("霍夫曼码: 1.75 bits", font_size=24, color=IT_GREEN),
            Text("节省空间: 12.5%", font_size=28, color=IT_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 2.5)
        
        self.play(Write(comparison))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("精力的最优分配", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        # 核心逻辑
        lines = VGroup(
            Text("生活也是一种编码", font_size=28),
            Text("时间和精力是有限的带宽", font_size=28, color=IT_GRAY),
            Text("把最短的路径(低成本)", font_size=32, color=IT_GREEN, weight=BOLD),
            Text("留给最高频的习惯(读书、运动)", font_size=32, color=IT_GREEN, weight=BOLD),
            Text("把高成本留给低频的意外", font_size=28, color=IT_RED)
        ).arrange(DOWN, buff=0.5)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：麦克斯韦妖", font_size=40, color=IT_RED).move_to(UP * 0.5)
        desc = Text("信息能转化为能量吗？\n物理学与信息论的惊天连接。", font_size=24, color=IT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))