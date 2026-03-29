# manim -pqh information_theory_ep11.py InformationTheoryEP11
from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 明文 / 正确 / 匹配
IT_RED = "#FF2A68"       # 密文 / 错误 / 偏移
IT_BLUE = "#00BFFF"      # 统计 / 结构
IT_YELLOW = "#FFD700"    # 密钥 / 核心发现
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题
IT_ORANGE = "#F97316"    # 警告
IT_GRAY = "#333333"      # 仅用于背景线条
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP11(Scene):
    """信息论 EP11: 频率分析 (Frequency Analysis)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：凯撒密码的原理
        self.intro_caesar()
        
        # 2. 挑战：如何破解一堆乱码？
        self.show_challenge()
        
        # 3. 核心：频率指纹对比
        self.frequency_fingerprint()
        
        # 4. 解密演示：动态替换
        self.decryption_demo()
        
        # 5. 哲学升华：习惯即漏洞
        self.show_philosophy()

    def intro_caesar(self):
        """开场：简单的凯撒位移"""
        
        title = Text("EP11: 频率分析", font_size=54, color=IT_BLUE, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("Cracking the Code with Statistics", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 演示凯撒密码原理
        # A -> D (Shift +3)
        
        # 原盘
        circle_group = VGroup()
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        radius = 2.5
        
        # 简化的圆盘，只显示部分字母
        shown_indices = [0, 1, 2, 3, 4, 5] # A, B, C, D, E, F
        
        p1_group = VGroup() # 内圈（明文）
        p2_group = VGroup() # 外圈（密文）
        
        for i in shown_indices:
            angle = i * TAU / 26
            # 内圈
            char_in = Text(letters[i], font_size=36, color=IT_GREEN)
            char_in.move_to(np.array([radius * np.cos(PI/2 - angle), radius * np.sin(PI/2 - angle), 0]))
            p1_group.add(char_in)
            
            # 外圈
            char_out = Text(letters[i], font_size=36, color=IT_RED)
            char_out.move_to(np.array([(radius+0.8) * np.cos(PI/2 - angle), (radius+0.8) * np.sin(PI/2 - angle), 0]))
            p2_group.add(char_out)
            
        # 绘制中心和指针
        center = Dot(color=WHITE)
        arrow = Arrow(center.get_center(), UP*(radius-0.5), color=IT_YELLOW, buff=0)
        
        self.play(Write(p1_group), Write(p2_group), Create(center), Create(arrow))
        
        label = Text("凯撒密码 (Caesar Cipher)", font_size=24, color=IT_YELLOW).to_edge(DOWN, buff=1.5)
        self.play(Write(label))
        
        # 旋转动画
        # 外圈旋转 3 格 (3 * TAU / 26)
        shift_angle = -3 * TAU / 26
        
        action_text = Text("密钥：偏移 +3", font_size=32, color=IT_RED).next_to(center, DOWN, buff=0.5)
        self.play(Write(action_text))
        
        self.play(
            Rotate(p2_group, angle=shift_angle, about_point=ORIGIN),
            run_time=2
        )
        
        # 强调对应关系
        # A(Green) 对应 D(Red)
        line = DashedLine(p1_group[0].get_center(), p2_group[3].get_center(), color=IT_YELLOW)
        mapping = Text("A -> D", font_size=40, color=IT_YELLOW).move_to(RIGHT * 4)
        
        self.play(Create(line), Write(mapping))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_challenge(self):
        """展示挑战：一封无法阅读的信"""
        
        title = Text("如果不知道密钥怎么办？", font_size=36, color=IT_RED).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 生成一段密文
        # 原文: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
        # 密文 (+3): WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
        ciphertext_str = "WKH TXLFN EURZQ IRA\nMXPSV RYHU WKH ODCB GRJ"
        
        code_block = Text(ciphertext_str, font_size=48, color=IT_RED, font="Consolas").move_to(UP * 0.5)
        
        self.play(AddTextLetterByLetter(code_block, time_per_char=0.1))
        
        # 困惑
        confused = Text("看起来像是随机乱码...", font_size=24, color=WHITE).next_to(code_block, DOWN, buff=0.5)
        self.play(Write(confused))
        self.wait(1)
        
        # 转折
        insight = Text("但它保留了原始语言的指纹！", font_size=32, color=IT_GREEN, weight=BOLD).next_to(confused, DOWN, buff=0.8)
        self.play(Write(insight))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def frequency_fingerprint(self):
        """核心：频率指纹对比"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("语言的指纹：频率分布", font_size=36, color=IT_BLUE).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # 1. 辅助函数：绘制简易直方图
        def create_histogram(data, color, label_text):
            # data: [(Letter, Height), ...]
            bars = VGroup()
            labels = VGroup()
            
            # 坐标轴
            axis = Line(LEFT*2.5, RIGHT*2.5, color=WHITE)
            
            for i, (char, h) in enumerate(data):
                bar = Rectangle(
                    width=0.6, height=h*3, 
                    fill_color=color, fill_opacity=0.8, stroke_width=1
                )
                # 位置
                x_pos = (i - 2) * 0.8
                bar.move_to(RIGHT * x_pos + UP * (h*3)/2)
                
                char_lbl = Text(char, font_size=20, color=WHITE).next_to(axis, DOWN).set_x(bar.get_x())
                
                bars.add(bar)
                labels.add(char_lbl)
                
            bars.next_to(axis, UP, buff=0)
            group = VGroup(axis, bars, labels)
            
            title = Text(label_text, font_size=24, color=color).next_to(group, UP, buff=0.5)
            return VGroup(group, title)

        # 2. 左侧：标准英语频率 (E T A O I)
        # E: 12.7%, T: 9.1%, A: 8.2%, O: 7.5%, I: 7.0%
        std_data = [('A', 0.8), ('E', 1.2), ('I', 0.7), ('O', 0.75), ('T', 0.9)]
        # 为了视觉清晰，我们按字母顺序排列 A E I O T
        
        left_chart = create_histogram(std_data, IT_GREEN, "标准英语频率")
        left_chart.move_to(LEFT_ZONE)
        
        self.play(FadeIn(left_chart))
        
        # 强调 E
        arrow_e = Arrow(UP, DOWN, color=IT_YELLOW).next_to(left_chart[0][1][1], UP) # 指向E的柱子
        label_e = Text("E 最高", font_size=20, color=IT_YELLOW).next_to(arrow_e, UP)
        self.play(GrowArrow(arrow_e), Write(label_e))
        
        # 3. 右侧：密文频率
        # 假设密文是凯撒+3，那么 E -> H
        # A->D, E->H, I->L, O->R, T->W
        # 密文里 H 应该是最高的
        
        # 为了演示“形状匹配”，我们画一组形状相似但位置偏移的数据
        # 显示 D H L R W (对应 A E I O T)
        cipher_data = [('D', 0.8), ('H', 1.2), ('L', 0.7), ('R', 0.75), ('W', 0.9)]
        
        right_chart = create_histogram(cipher_data, IT_RED, "密文频率统计")
        right_chart.move_to(RIGHT_ZONE)
        
        self.play(FadeIn(right_chart))
        
        # 强调 H
        arrow_h = Arrow(UP, DOWN, color=IT_YELLOW).next_to(right_chart[0][1][1], UP) # 指向H
        label_h = Text("H 最高", font_size=20, color=IT_YELLOW).next_to(arrow_h, UP)
        self.play(GrowArrow(arrow_h), Write(label_h))
        
        # 4. 匹配过程
        # 文字说明
        match_text = Text("形状相似，只是发生了位移！", font_size=28, color=IT_BLUE).move_to(DOWN * 1.5)
        self.play(Write(match_text))
        
        # 动画：将右侧图表平移与左侧重叠 (示意)
        # 计算位移量
        shift_vec = left_chart.get_center() - right_chart.get_center()
        
        self.play(
            FadeOut(arrow_e), FadeOut(label_e), FadeOut(arrow_h), FadeOut(label_h),
            right_chart.animate.shift(shift_vec + DOWN * 0.5).set_opacity(0.7)
        )
        
        # 结论
        conclusion = Text("H - E = 3 (偏移量)", font_size=32, color=IT_YELLOW, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def decryption_demo(self):
        """解密演示：动态替换"""
        
        title = Text("破解时刻", font_size=40, color=IT_GREEN).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 密文
        cipher_str = "WKH  TXLFN  EURZQ  IRA"
        plain_str =  "THE  QUICK  BROWN  FOX"
        
        # 显示密文 (红色)
        cipher_mob = Text(cipher_str, font_size=60, color=IT_RED, font="Consolas")
        cipher_mob.move_to(UP * 0.5)
        self.play(FadeIn(cipher_mob))
        
        # 提示
        hint = Text("尝试规则：每个字母 -3", font_size=24, color=IT_YELLOW).next_to(cipher_mob, UP, buff=1.0)
        self.play(Write(hint))
        
        # 逐个字母变换
        # 创建明文对象 (绿色)
        plain_mob = Text(plain_str, font_size=60, color=IT_GREEN, font="Consolas")
        plain_mob.move_to(cipher_mob.get_center())
        
        # 为了效果，我们只变换前几个字母，然后整体变换
        # W -> T
        self.play(Transform(cipher_mob[0], plain_mob[0]), run_time=0.5)
        # K -> H
        self.play(Transform(cipher_mob[1], plain_mob[1]), run_time=0.5)
        # H -> E
        self.play(Transform(cipher_mob[2], plain_mob[2]), run_time=0.5)
        
        # 剩下的全部变换
        self.play(Transform(cipher_mob, plain_mob), run_time=1.5)
        
        success = Text("解密成功！", font_size=36, color=IT_GREEN, weight=BOLD).next_to(cipher_mob, DOWN, buff=1.0)
        self.play(Write(success))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("数据隐私的哲学", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("你以为你隐藏得很好", font_size=28, color=WHITE),
            Text("但你的习惯、偏好、频率", font_size=28, color=IT_BLUE),
            Text("都是无法消除的指纹", font_size=32, color=IT_RED, weight=BOLD),
            Text("在大数据面前，没有秘密", font_size=32, color=IT_YELLOW),
            Text("除非你变得像噪声一样完全随机 (熵最大化)", font_size=28, color=IT_GRAY) # 修改为白色
        ).arrange(DOWN, buff=0.6)
        
        # 修复最后一行颜色 IT_GRAY -> WHITE，以便看清
        lines[4].set_color(WHITE)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：公钥密码", font_size=40, color=IT_GREEN).move_to(UP * 0.5)
        desc = Text("如何在不信任的世界里建立信任？\nDiffie-Hellman 密钥交换的颜色游戏。", font_size=24, color=WHITE).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))