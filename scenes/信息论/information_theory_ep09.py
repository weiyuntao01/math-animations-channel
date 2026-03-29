from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 信号 / 低熵
IT_RED = "#FF2A68"       # 热量 / 擦除 / 熵增
IT_BLUE = "#00BFFF"      # 冷 / 结构 / 0
IT_YELLOW = "#FFD700"    # 能量 / 1
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题
IT_ORANGE = "#F97316"    # 警告 / 压缩
IT_GRAY = "#333333"      # 仅用于背景线条 (文字已弃用此色)
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP09(Scene):
    """信息论 EP09: 兰道尔原理 (高对比度字体版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：电脑为什么会发热？
        self.intro_heat()
        
        # 2. 逻辑门对比：可逆 vs 不可逆
        self.logic_gates_demo()
        
        # 3. 物理本质：压缩相空间
        self.physics_of_erasure()
        
        # 4. 兰道尔极限公式
        self.landauer_limit()
        
        # 5. 哲学升华
        self.show_philosophy()

    def intro_heat(self):
        """开场：发热的芯片"""
        
        title = Text("EP09: 兰道尔原理", font_size=54, color=IT_RED, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("The Cost of Forgetting (遗忘的代价)", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 绘制芯片
        chip_body = Square(side_length=3, color=IT_BLUE, fill_opacity=0.2)
        chip_label = Text("CPU", font_size=36).move_to(chip_body)
        
        # 管脚
        pins = VGroup()
        for i in range(4):
            pins.add(Line(chip_body.get_top() + RIGHT*(i-1.5)*0.6, chip_body.get_top() + RIGHT*(i-1.5)*0.6 + UP*0.3, color=IT_GRAY))
            pins.add(Line(chip_body.get_bottom() + RIGHT*(i-1.5)*0.6, chip_body.get_bottom() + RIGHT*(i-1.5)*0.6 + DOWN*0.3, color=IT_GRAY))
        
        chip = VGroup(chip_body, chip_label, pins).move_to(ORIGIN)
        self.play(Create(chip))
        
        # 提问
        q1 = Text("为什么电脑会发热？", font_size=32, color=IT_YELLOW).next_to(chip, DOWN, buff=1.0)
        self.play(Write(q1))
        
        # 常见回答 (修改：IT_GRAY -> WHITE)
        a1 = Text("电阻？电流？摩擦？", font_size=24, color=WHITE).next_to(q1, DOWN, buff=0.3)
        self.play(Write(a1))
        self.wait(1)
        
        # 否定并变红
        self.play(
            FadeOut(a1),
            chip_body.animate.set_fill(IT_RED, opacity=0.6).set_stroke(IT_RED),
            chip_label.animate.set_color(IT_RED)
        )
        
        # 散热波纹
        heat_waves = VGroup(*[
            Circle(radius=2 + i*0.5, color=IT_RED, stroke_opacity=1 - i*0.2).move_to(chip)
            for i in range(3)
        ])
        self.play(ShowPassingFlash(heat_waves, time_width=0.5, run_time=1.5))
        
        truth = Text("是因为我们在\"删除\"信息！", font_size=32, color=IT_RED, weight=BOLD).next_to(q1, DOWN, buff=0.3)
        self.play(Write(truth))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def logic_gates_demo(self):
        """对比可逆逻辑与不可逆逻辑"""
        
        title = Text("逻辑的物理代价", font_size=36, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # --- 左侧：NOT 门 (可逆) ---
        not_title = Text("NOT 门 (取反)", font_size=28, color=IT_GREEN).move_to(LEFT_ZONE + UP * 2.0)
        
        not_box = Square(side_length=1.5, color=IT_GREEN)
        not_label = Text("NOT", font_size=24).move_to(not_box)
        not_group = VGroup(not_box, not_label).move_to(LEFT_ZONE)
        
        in_0 = Text("0", color=IT_BLUE).next_to(not_box, LEFT)
        out_1 = Text("1", color=IT_YELLOW).next_to(not_box, RIGHT)
        arrow = Arrow(LEFT, RIGHT, color=IT_GRAY).move_to(not_box) 
        
        logic_desc1 = Text("输入 0 -> 输出 1", font_size=20).next_to(not_box, DOWN)
        logic_desc2 = Text("输入 1 -> 输出 0", font_size=20).next_to(logic_desc1, DOWN)
        
        rev_tag = Text("可逆 (无信息丢失)", font_size=24, color=IT_GREEN).next_to(logic_desc2, DOWN, buff=0.5)
        
        self.play(Write(not_title))
        self.play(Create(not_group))
        self.play(FadeIn(in_0), FadeIn(out_1))
        self.play(Write(logic_desc1), Write(logic_desc2))
        self.play(Write(rev_tag))
        
        # --- 右侧：RESET 操作 (不可逆) ---
        reset_title = Text("RESET (擦除)", font_size=28, color=IT_RED).move_to(RIGHT_ZONE + UP * 2.0)
        
        reset_box = Square(side_length=1.5, color=IT_RED)
        reset_label = Text("SET 0", font_size=24).move_to(reset_box)
        reset_group = VGroup(reset_box, reset_label).move_to(RIGHT_ZONE)
        
        in_unknown = Text("0 或 1 ?", font_size=24, color=WHITE).next_to(reset_box, LEFT, buff=1.0)
        out_zero = Text("0", font_size=36, color=IT_BLUE).next_to(reset_box, RIGHT)
        
        arrow_top = Arrow(in_unknown.get_right() + UP*0.2, reset_box.get_left(), color=IT_YELLOW)
        arrow_btm = Arrow(in_unknown.get_right() + DOWN*0.2, reset_box.get_left(), color=IT_BLUE)
        
        logic_desc3 = Text("无论输入啥 -> 都输出 0", font_size=20).next_to(reset_box, DOWN)
        
        irrev_tag = Text("不可逆 (信息丢失!)", font_size=24, color=IT_RED).next_to(logic_desc3, DOWN, buff=0.5)
        
        heat_text = Text("热量产生 🔥", font_size=24, color=IT_ORANGE).next_to(irrev_tag, DOWN)
        
        self.play(Write(reset_title))
        self.play(Create(reset_group))
        self.play(FadeIn(in_unknown), GrowArrow(arrow_top), GrowArrow(arrow_btm), FadeIn(out_zero))
        self.play(Write(logic_desc3))
        self.play(Write(irrev_tag))
        self.play(Write(heat_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def physics_of_erasure(self):
        """物理本质：压缩相空间"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("物理本质：压缩相空间", font_size=36, color=IT_YELLOW).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # --- 左侧：1 bit 的物理状态 ---
        box_width = 4
        box_height = 2
        box = Rectangle(width=box_width, height=box_height, color=WHITE).move_to(LEFT_ZONE)
        
        divider = DashedLine(box.get_top(), box.get_bottom(), color=IT_GRAY)
        
        state_0 = Text("0", color=IT_BLUE).move_to(LEFT_ZONE + LEFT * 1)
        state_1 = Text("1", color=IT_YELLOW).move_to(LEFT_ZONE + RIGHT * 1)
        
        particle = Dot(color=WHITE, radius=0.15)
        particle.move_to(LEFT_ZONE + RIGHT * 1) 
        
        self.play(Create(box), Create(divider))
        self.play(Write(state_0), Write(state_1))
        self.play(FadeIn(particle))
        
        info_status = Text("状态：不确定 (1 bit)", font_size=24, color=IT_GREEN).next_to(box, UP)
        self.play(Write(info_status))
        
        self.play(particle.animate.move_to(LEFT_ZONE + RIGHT*1.5 + UP*0.5), run_time=0.5)
        self.play(particle.animate.move_to(LEFT_ZONE + RIGHT*0.5 + DOWN*0.5), run_time=0.5)
        
        # --- 右侧：擦除过程 ---
        
        step_title = Text("执行擦除操作 (Set to 0)", font_size=28, color=IT_RED).move_to(RIGHT_ZONE + UP * 1.5)
        self.play(Write(step_title))
        
        action_text = VGroup(
            Text("为了把状态强制归 0", font_size=24),
            Text("必须推动活塞压缩空间", font_size=24),
            Text("这是对粒子做功 W", font_size=24, color=IT_ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(RIGHT_ZONE)
        
        self.play(Write(action_text))
        
        piston = Line(box.get_top() + RIGHT*2, box.get_bottom() + RIGHT*2, color=IT_ORANGE, stroke_width=8)
        self.play(FadeIn(piston))
        
        self.play(
            piston.animate.move_to(LEFT_ZONE), 
            particle.animate.move_to(LEFT_ZONE + LEFT * 0.5), 
            run_time=2
        )
        
        new_status = Text("状态：确定为 0 (0 bit)", font_size=24, color=IT_BLUE).next_to(box, UP)
        self.play(Transform(info_status, new_status))
        
        heat_text = Text("做功转化为了热量 Q", font_size=28, color=IT_RED).move_to(RIGHT_ZONE + DOWN * 1.5)
        self.play(Write(heat_text))
        
        self.play(particle.animate.set_color(IT_RED), run_time=0.5)
        self.play(Wiggle(particle, scale_value=1.5, rotation_angle=0.1*TAU), run_time=1)
        
        heat_waves = VGroup(*[
            Circle(radius=0.5 + i*0.3, color=IT_RED, stroke_opacity=1-i*0.2).move_to(particle)
            for i in range(4)
        ])
        self.play(ShowPassingFlash(heat_waves, time_width=0.5, run_time=2))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def landauer_limit(self):
        """兰道尔极限公式"""
        
        title = Text("兰道尔极限 (Landauer Limit)", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        formula = MathTex(
            r"E \ge k_B T \ln 2",
            font_size=80
        )
        formula.set_color_by_tex("E", IT_RED)
        formula.set_color_by_tex("T", IT_YELLOW)
        formula.set_color_by_tex("ln", IT_BLUE)
        
        self.play(Write(formula))
        
        param_y = DOWN * 1.5
        
        p1 = VGroup(
            MathTex("E", color=IT_RED),
            Text("最小能耗", font_size=24)
        ).arrange(DOWN)
        
        p2 = VGroup(
            # 修改：IT_GRAY -> WHITE (k_B)
            MathTex("k_B", color=WHITE),
            Text("玻尔兹曼常数", font_size=24)
        ).arrange(DOWN)
        
        p3 = VGroup(
            MathTex("T", color=IT_YELLOW),
            Text("环境温度", font_size=24)
        ).arrange(DOWN)
        
        params = VGroup(p1, p2, p3).arrange(RIGHT, buff=1.5).move_to(param_y)
        
        self.play(FadeIn(params, shift=UP))
        
        meaning = Text("擦除 1 bit 信息，必然释放这么多热量", font_size=28, color=IT_ORANGE)
        meaning.to_edge(DOWN, buff=0.8)
        self.play(Write(meaning))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("遗忘的代价", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("获取信息需要能量 (观测)", font_size=28, color=WHITE),
            # 修改：IT_GRAY -> WHITE
            Text("但这通常是可逆的", font_size=28, color=WHITE),
            Text("真正昂贵的是遗忘 (擦除)", font_size=32, color=IT_ORANGE, weight=BOLD),
            Text("要让系统变得有序，必须向环境排放热量", font_size=28, color=IT_RED),
            Text("记住过去很容易，放下过去很费力", font_size=36, color=IT_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.6)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：时间之箭", font_size=40, color=IT_BLUE).move_to(UP * 0.5)
        # 修改：IT_GRAY -> WHITE
        desc = Text("为什么时间不能倒流？\n熵、信息与宇宙的终局。", font_size=24, color=WHITE).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))