from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 秩序 / 信息
IT_RED = "#FF2A68"       # 混乱 / 热 / 错误
IT_BLUE = "#00BFFF"      # 冷 / 结构
IT_YELLOW = "#FFD700"    # 能量 / 妖 / 核心
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题
IT_ORANGE = "#F97316"    # 警告 / 重点 / 擦除
IT_GRAY = "#333333"      # 仅用于背景线条/容器 (文字已弃用此色)
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP08(Scene):
    """信息论 EP08: 麦克斯韦妖 (高对比度字体版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：永动机的梦想
        self.intro_perpetual()
        
        # 2. 实验：麦克斯韦妖的操作
        self.demon_experiment()
        
        # 3. 悖论：第二定律失效了？
        self.state_paradox()
        
        # 4. 驱魔：西拉德与兰道尔 (信息即物理)
        self.exorcism_resolution()
        
        # 5. 哲学升华
        self.show_philosophy()

    def intro_perpetual(self):
        """开场：挑战热力学第二定律"""
        
        title = Text("EP08: 麦克斯韦妖", font_size=54, color=IT_RED, weight=BOLD).to_edge(UP, buff=1.0)
        # 修改：IT_GRAY -> WHITE
        subtitle = Text("Maxwell's Demon: Information is Energy", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 引用
        quote = Text("“只要有信息，\n我就能逆转宇宙的热寂。”", font_size=32, color=IT_YELLOW, slant=ITALIC)
        quote.move_to(UP * 0.5)
        self.play(Write(quote))
        self.wait(2)
        
        # 核心问题
        question = Text("信息能转化为能量吗？", font_size=36, color=IT_BLUE).next_to(quote, DOWN, buff=1.0)
        self.play(Write(question))
        self.wait(2)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def demon_experiment(self):
        """实验：演示妖如何分类粒子"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("思想实验：智能分拣", font_size=36, color=IT_YELLOW).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 左侧：气体容器
        box_width = 6
        box_height = 4
        box = Rectangle(width=box_width, height=box_height, color=WHITE).move_to(LEFT_ZONE + DOWN*0.5)
        
        # 中间隔板 (线条保持灰色 IT_GRAY，因为是背景结构)
        wall_top = Line(box.get_top(), box.get_center() + UP*0.5, color=IT_GRAY, stroke_width=4)
        wall_bottom = Line(box.get_bottom(), box.get_center() + DOWN*0.5, color=IT_GRAY, stroke_width=4)
        door = Line(box.get_center() + UP*0.5, box.get_center() + DOWN*0.5, color=IT_YELLOW, stroke_width=6)
        
        # 妖 (位于上方)
        demon_icon = VGroup(
            Circle(radius=0.4, color=IT_YELLOW, fill_opacity=0.2),
            Text("😈", font_size=32).move_to(ORIGIN) 
        ).next_to(wall_top, UP, buff=0.2)
        demon_icon[1].move_to(demon_icon[0])
        
        self.play(Create(box), Create(wall_top), Create(wall_bottom), Create(door), FadeIn(demon_icon))
        
        # 2. 粒子初始化 (混合状态)
        fast_particles = VGroup()
        slow_particles = VGroup()
        
        for _ in range(6):
            # 随机分布
            p_fast = Dot(point=box.get_center() + np.array([random.uniform(-2.5, 2.5), random.uniform(-1.5, 1.5), 0]), color=IT_RED)
            p_slow = Dot(point=box.get_center() + np.array([random.uniform(-2.5, 2.5), random.uniform(-1.5, 1.5), 0]), color=IT_BLUE)
            fast_particles.add(p_fast)
            slow_particles.add(p_slow)
            
        self.play(FadeIn(fast_particles), FadeIn(slow_particles))
        
        # 3. 右侧：状态说明
        state_title = Text("初始状态：混合", font_size=28, color=WHITE).move_to(RIGHT_ZONE + UP * 1.5)
        
        temp_left = Text("左室：温 (25°C)", font_size=24, color=IT_GREEN).next_to(state_title, DOWN, buff=0.5)
        temp_right = Text("右室：温 (25°C)", font_size=24, color=IT_GREEN).next_to(temp_left, DOWN, buff=0.3)
        
        entropy_text = Text("熵：最大 (无序)", font_size=24, color=IT_RED).next_to(temp_right, DOWN, buff=0.5)
        
        self.play(Write(state_title), Write(temp_left), Write(temp_right), Write(entropy_text))
        self.wait(1)
        
        # 4. 动画：妖的操作 (分类)
        action_text = Text("妖的操作：\n看见快分子 -> 开门去右\n看见慢分子 -> 开门去左", font_size=24, color=IT_YELLOW).move_to(RIGHT_ZONE + DOWN * 1.5)
        self.play(Write(action_text))
        
        # 模拟分类后的位置
        anims = []
        
        # 红色粒子移动到右侧
        for i, p in enumerate(fast_particles):
            target = box.get_center() + np.array([random.uniform(0.2, 2.5), random.uniform(-1.5, 1.5), 0])
            anims.append(p.animate.move_to(target))
            
        # 蓝色粒子移动到左侧
        for i, p in enumerate(slow_particles):
            target = box.get_center() + np.array([random.uniform(-2.5, -0.2), random.uniform(-1.5, 1.5), 0])
            anims.append(p.animate.move_to(target))
            
        # 门闪烁模拟开关
        self.play(
            door.animate.set_opacity(0.1), # 开门
            *anims,
            run_time=2
        )
        self.play(door.animate.set_opacity(1)) # 关门
        
        # 5. 更新状态
        new_state_title = Text("最终状态：分离", font_size=28, color=IT_YELLOW).move_to(state_title)
        
        new_temp_left = Text("左室：冷 (0°C)", font_size=24, color=IT_BLUE).move_to(temp_left)
        new_temp_right = Text("右室：热 (50°C)", font_size=24, color=IT_RED).move_to(temp_right)
        
        new_entropy = Text("熵：减小 (有序!)", font_size=24, color=IT_GREEN).move_to(entropy_text)
        
        self.play(
            Transform(state_title, new_state_title),
            Transform(temp_left, new_temp_left),
            Transform(temp_right, new_temp_right),
            Transform(entropy_text, new_entropy)
        )
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def state_paradox(self):
        """陈述悖论"""
        
        title = Text("为什么这是个悖论？", font_size=36, color=IT_RED).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 逻辑链
        step1 = Text("1. 气体自动分离 (冷热分开)", font_size=28).move_to(LEFT * 3 + UP * 0.5)
        step2 = Text("2. 温差产生能量 (永动机)", font_size=28, color=IT_YELLOW).next_to(step1, DOWN, buff=0.5)
        
        step3 = Text("3. 妖没有做功 (只是开关门)", font_size=28).move_to(RIGHT * 3 + UP * 0.5)
        step4 = Text("4. 熵减少了 (违反第二定律)", font_size=28, color=IT_RED).next_to(step3, DOWN, buff=0.5)
        
        self.play(Write(step1))
        self.play(Write(step3))
        self.play(Write(step2))
        self.play(Write(step4))
        
        # 大大的问号
        q_mark = Text("?", font_size=96, color=IT_RED).move_to(DOWN * 2)
        self.play(FadeIn(q_mark))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def exorcism_resolution(self):
        """驱魔：信息的物理代价"""
        
        title = Text("驱魔：信息的代价", font_size=36, color=IT_GREEN).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 布局
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 1. 左侧：妖的大脑 (存储设备)
        brain = Square(side_length=2.5, color=IT_BLUE, fill_opacity=0.2).move_to(LEFT_ZONE + UP * 0.5)
        brain_label = Text("妖的大脑 (记忆)", font_size=24, color=IT_BLUE).next_to(brain, UP)
        
        # 记忆位 (Bits)
        bits = VGroup(*[Text("0", font_size=20) for _ in range(8)]).arrange_in_grid(2, 4, buff=0.4).move_to(brain)
        
        self.play(Create(brain), Write(brain_label), FadeIn(bits))
        
        # 2. 右侧：兰道尔原理
        principle = Text("兰道尔原理 (Landauer's Principle)", font_size=26, color=IT_YELLOW).move_to(RIGHT_ZONE + UP * 2)
        self.play(Write(principle))
        
        desc = VGroup(
            Text("1. 妖必须观测粒子 (获取信息)", font_size=22),
            Text("2. 妖必须记录信息 (存储)", font_size=22),
            Text("3. 大脑容量有限，必须擦除旧记忆", font_size=22, color=IT_ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(principle, DOWN, buff=0.5)
        
        self.play(Write(desc))
        
        # 3. 动画：擦除产生热量
        erase_text = Text("擦除信息...", font_size=24, color=IT_RED).next_to(brain, DOWN, buff=0.5)
        self.play(Write(erase_text))
        
        # 比特混乱变化
        new_bits = VGroup(*[Text(str(random.choice([0,1])), font_size=20, color=IT_RED) for _ in range(8)]).arrange_in_grid(2, 4, buff=0.4).move_to(brain)
        
        self.play(Transform(bits, new_bits))
        
        # 散热动画
        heat_waves = VGroup(*[
            Arc(radius=r, start_angle=0, angle=PI, color=IT_RED).move_to(brain.get_top())
            for r in [0.5, 1.0, 1.5]
        ])
        
        self.play(Create(heat_waves))
        
        # 4. 能量公式
        formula = MathTex(r"E \ge k_B T \ln 2", font_size=40, color=IT_RED).move_to(RIGHT_ZONE + DOWN * 1.5)
        formula_desc = Text("擦除 1 bit 信息产生的最小热量", font_size=20, color=IT_RED).next_to(formula, DOWN)
        
        self.play(Write(formula), Write(formula_desc))
        
        # 总结
        summary = Text("系统的熵减 = 妖大脑的熵增 + 散热", font_size=26, color=IT_GREEN).to_edge(DOWN, buff=0.5)
        self.play(Write(summary))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("认知差就是能量差", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            # 修改：IT_GRAY -> WHITE
            Text("麦克斯韦妖告诉我们：", font_size=28, color=WHITE),
            Text("信息不是虚拟的，信息是物理的 (It from Bit)", font_size=32, color=IT_BLUE, weight=BOLD),
            Text("拥有信息，就能在无序中创造有序", font_size=28, color=IT_GREEN),
            Text("你的认知水平，决定了你对能量的调动能力", font_size=28, color=IT_YELLOW),
            Text("遗忘是需要代价的，放下比记住更难", font_size=28, color=IT_RED)
        ).arrange(DOWN, buff=0.5)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：兰道尔原理", font_size=40, color=IT_RED).move_to(UP * 0.5)
        # 修改：IT_GRAY -> WHITE
        desc = Text("为什么电脑会发热？\n不可逆计算与热力学的深层联系。", font_size=24, color=WHITE).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))