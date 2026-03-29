from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 秩序 / 低熵 / 过去
IT_RED = "#FF2A68"       # 混乱 / 高熵 / 未来
IT_BLUE = "#00BFFF"      # 物理定律
IT_YELLOW = "#FFD700"    # 能量 / 记忆
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题
IT_ORANGE = "#F97316"    # 警告 / 不可逆
IT_GRAY = "#333333"      # 仅用于背景线条
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP10(Scene):
    """信息论 EP10: 时间之箭 (Time's Arrow)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：覆水难收
        self.intro_irreversibility()
        
        # 2. 矛盾：微观可逆 vs 宏观不可逆
        self.micro_vs_macro()
        
        # 3. 宇宙视角：大爆炸到热寂
        self.cosmic_timeline()
        
        # 4. 记忆与时间：为什么我们只记得过去？
        self.memory_entropy()
        
        # 5. 哲学升华
        self.show_philosophy()

    def intro_irreversibility(self):
        """开场：破碎的杯子"""
        
        title = Text("EP10: 时间之箭", font_size=54, color=IT_ORANGE, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("Why Time Flies One Way?", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 模拟杯子
        glass = Square(side_length=2, color=IT_BLUE, fill_opacity=0.5).move_to(UP * 0.5)
        label = Text("完整的杯子", font_size=24, color=IT_BLUE).next_to(glass, UP)
        
        self.play(Create(glass), Write(label))
        self.wait(1)
        
        # 破碎动画
        # 将杯子替换为4个碎片并飞散
        fragments = VGroup(
            Square(side_length=1, color=IT_BLUE, fill_opacity=0.5).move_to(glass.get_center() + UL*0.5),
            Square(side_length=1, color=IT_BLUE, fill_opacity=0.5).move_to(glass.get_center() + UR*0.5),
            Square(side_length=1, color=IT_BLUE, fill_opacity=0.5).move_to(glass.get_center() + DL*0.5),
            Square(side_length=1, color=IT_BLUE, fill_opacity=0.5).move_to(glass.get_center() + DR*0.5),
        )
        
        self.play(FadeOut(glass), FadeIn(fragments))
        
        # 碎片飞散 + 旋转
        self.play(
            fragments[0].animate.shift(UL*2).rotate(PI/3),
            fragments[1].animate.shift(UR*2 + UP).rotate(-PI/4),
            fragments[2].animate.shift(DL*2).rotate(PI/2),
            fragments[3].animate.shift(DR*2 + RIGHT).rotate(-PI/6),
            run_time=1.5
        )
        
        broken_label = Text("破碎的杯子", font_size=24, color=IT_RED).move_to(label)
        self.play(Transform(label, broken_label))
        
        # 尝试倒放
        reverse_text = Text("倒放：看起来很假", font_size=32, color=IT_YELLOW).move_to(DOWN * 2.5)
        self.play(Write(reverse_text))
        
        # 倒放动画
        self.play(
            fragments[0].animate.move_to(glass.get_center() + UL*0.5).rotate(-PI/3),
            fragments[1].animate.move_to(glass.get_center() + UR*0.5).rotate(PI/4),
            fragments[2].animate.move_to(glass.get_center() + DL*0.5).rotate(-PI/2),
            fragments[3].animate.move_to(glass.get_center() + DR*0.5).rotate(PI/6),
            run_time=2,
            rate_func=lambda t: 1-t # 简单的倒放效果
        )
        
        # 结论
        conclusion = Text("有些过程是不可逆的！", font_size=36, color=IT_RED, weight=BOLD).move_to(DOWN * 2.5)
        self.play(ReplacementTransform(reverse_text, conclusion))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def micro_vs_macro(self):
        """微观可逆 vs 宏观不可逆"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("矛盾：微观 vs 宏观", font_size=36, color=IT_PURPLE).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # --- 左侧：微观粒子碰撞 (可逆) ---
        box_left = Square(side_length=3, color=IT_GRAY).move_to(LEFT_ZONE)
        label_left = Text("微观世界", font_size=24, color=IT_BLUE).next_to(box_left, UP)
        
        p1 = Dot(point=box_left.get_center() + LEFT, color=IT_BLUE, radius=0.15)
        p2 = Dot(point=box_left.get_center() + RIGHT, color=IT_RED, radius=0.15)
        
        self.play(Create(box_left), Write(label_left), FadeIn(p1), FadeIn(p2))
        
        # 碰撞动画
        self.play(
            p1.animate.move_to(box_left.get_center() + LEFT*0.15),
            p2.animate.move_to(box_left.get_center() + RIGHT*0.15),
            run_time=0.8
        )
        self.play(
            p1.animate.move_to(box_left.get_center() + UL),
            p2.animate.move_to(box_left.get_center() + DR),
            run_time=0.8
        )
        
        # 倒放说明
        rev_text = Text("倒放符合物理定律", font_size=20, color=IT_GREEN).next_to(box_left, DOWN)
        self.play(Write(rev_text))
        
        # 倒放动画
        self.play(
            p1.animate.move_to(box_left.get_center() + LEFT*0.15),
            p2.animate.move_to(box_left.get_center() + RIGHT*0.15),
            run_time=0.8
        )
        self.play(
            p1.animate.move_to(box_left.get_center() + LEFT),
            p2.animate.move_to(box_left.get_center() + RIGHT),
            run_time=0.8
        )
        
        # --- 右侧：宏观扩散 (不可逆) ---
        box_right = Square(side_length=3, color=IT_GRAY).move_to(RIGHT_ZONE)
        label_right = Text("宏观世界", font_size=24, color=IT_RED).next_to(box_right, UP)
        
        # 很多粒子
        particles = VGroup(*[
            Dot(point=box_right.get_center() + np.array([random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), 0]), 
                color=IT_YELLOW, radius=0.05)
            for _ in range(30)
        ])
        
        self.play(Create(box_right), Write(label_right), FadeIn(particles))
        
        # 扩散动画
        diffused_positions = []
        for p in particles:
            diffused_positions.append(
                box_right.get_center() + np.array([random.uniform(-1.4, 1.4), random.uniform(-1.4, 1.4), 0])
            )
            
        self.play(
            *[p.animate.move_to(pos) for p, pos in zip(particles, diffused_positions)],
            run_time=2
        )
        
        # 倒放说明
        rev_text_macro = Text("倒放是概率极小的奇迹", font_size=20, color=IT_RED).next_to(box_right, DOWN)
        self.play(Write(rev_text_macro))
        
        # 尝试倒放 (聚集)
        self.play(
            *[p.animate.move_to(box_right.get_center()) for p in particles],
            run_time=2,
            rate_func=there_and_back # 聚一下又散开，暗示无法保持
        )
        
        # 总结
        summary = Text("时间之箭源于概率统计", font_size=32, color=IT_YELLOW).move_to(DOWN * 2.5)
        self.play(Write(summary))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def cosmic_timeline(self):
        """宇宙时间轴"""
        
        title = Text("宇宙的终极命运", font_size=36, color=IT_BLUE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 时间轴
        timeline = Arrow(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=4).shift(DOWN * 0.5)
        time_label = Text("时间 t", font_size=24, color=WHITE).next_to(timeline, RIGHT)
        
        self.play(Create(timeline), Write(time_label))
        
        # 起点：大爆炸
        start_point = Dot(timeline.get_start(), color=IT_GREEN, radius=0.2)
        start_label = Text("大爆炸", font_size=24, color=IT_GREEN).next_to(start_point, UP)
        start_desc = Text("极低熵\n高度有序", font_size=20, color=IT_GREEN).next_to(start_point, DOWN)
        
        self.play(FadeIn(start_point), Write(start_label), Write(start_desc))
        
        # 终点：热寂
        end_point = Dot(timeline.get_end(), color=IT_RED, radius=0.2)
        end_label = Text("热寂", font_size=24, color=IT_RED).next_to(end_point, UP)
        end_desc = Text("极高熵\n完全混乱", font_size=20, color=IT_RED).next_to(end_point, DOWN)
        
        self.play(FadeIn(end_point), Write(end_label), Write(end_desc))
        
        # 熵增曲线
        # 简单的S形或线性上升
        entropy_curve = FunctionGraph(
            lambda x: 0.1 * (x + 5)**2 - 2, # 抛物线示意
            x_range=[-5, 5],
            color=IT_YELLOW
        ).move_to(UP * 0.5) # 稍微上移
        
        curve_label = Text("熵 S (混乱度)", font_size=24, color=IT_YELLOW).next_to(entropy_curve, UP, buff=0.2)
        
        self.play(Create(entropy_curve), Write(curve_label))
        
        # 结论
        law_text = Text("热力学第二定律：孤立系统熵永不减少", font_size=28, color=IT_ORANGE).to_edge(DOWN, buff=1.0)
        self.play(Write(law_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def memory_entropy(self):
        """记忆与时间"""
        
        # 布局
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("为什么我们只记得过去？", font_size=36, color=IT_GREEN).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # 左侧：大脑/硬盘 (记录信息)
        brain = Square(side_length=2.5, color=IT_BLUE, fill_opacity=0.2).move_to(LEFT_ZONE + UP * 0.5)
        brain_label = Text("大脑/记忆体", font_size=24, color=IT_BLUE).next_to(brain, UP)
        
        # 初始：混乱状态 (未知)
        bits_start = VGroup(*[Text("?", font_size=24, color=IT_GRAY) for _ in range(4)]).arrange(RIGHT).move_to(brain)
        
        self.play(Create(brain), Write(brain_label), FadeIn(bits_start))
        
        # 右侧：环境 (宇宙)
        env = Cloud(height=2, width=3, color=IT_RED, fill_opacity=0.2).move_to(RIGHT_ZONE + UP * 0.5)
        env_label = Text("外部环境", font_size=24, color=IT_RED).next_to(env, UP)
        
        self.play(Create(env), Write(env_label))
        
        # 动作：写入记忆 (有序化)
        action_arrow = Arrow(LEFT, RIGHT, color=IT_YELLOW).move_to(ORIGIN + UP * 0.5)
        action_text = Text("记录信息", font_size=20, color=IT_YELLOW).next_to(action_arrow, UP)
        
        self.play(GrowArrow(action_arrow), Write(action_text))
        
        # 大脑内部变有序
        bits_end = VGroup(*[Text("1", font_size=24, color=IT_GREEN) for _ in range(4)]).arrange(RIGHT).move_to(brain)
        self.play(Transform(bits_start, bits_end))
        
        # 右侧环境：熵增 (发热)
        heat = VGroup(*[
            Circle(radius=0.2 + i*0.2, color=IT_RED, stroke_width=2).move_to(env)
            for i in range(5)
        ])
        self.play(ShowPassingFlash(heat, time_width=0.5, run_time=2))
        
        env_state = Text("熵增加 ΔS > 0", font_size=24, color=IT_RED).move_to(env)
        self.play(Write(env_state))
        
        # 逻辑推导 (放在下方)
        logic = VGroup(
            Text("1. 记录记忆 = 局部熵减 (大脑变有序)", font_size=24),
            Text("2. 代价 = 全局熵增 (发热/消耗能量)", font_size=24, color=IT_RED),
            Text("3. 只有熵增的方向，才能形成记忆", font_size=28, color=IT_YELLOW, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(DOWN, buff=1.0)
        
        self.play(Write(logic))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("时间的人生哲学", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("我们总是为过去后悔，为未来焦虑", font_size=28, color=WHITE),
            Text("但后悔是无效的，因为时间不可逆", font_size=28, color=IT_RED),
            Text("焦虑是徒劳的，因为未来是概率分布", font_size=28, color=IT_BLUE),
            Text("你唯一能拥有的", font_size=32, color=WHITE),
            Text("是在当下这个瞬间，对抗熵增", font_size=36, color=IT_GREEN, weight=BOLD),
            Text("去创造、去爱、去建立秩序", font_size=36, color=IT_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.5)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告 (进入密码篇)
        next_ep = Text("下期预告：频率分析", font_size=40, color=IT_BLUE).move_to(UP * 0.5)
        desc = Text("密码学篇开启！\n你以为你隐藏得很好，但数据出卖了你。", font_size=24, color=WHITE).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

class Cloud(VMobject):
    """自定义简单的云形状 (用于表示环境)"""
    def __init__(self, width=3, height=2, **kwargs):
        super().__init__(**kwargs)
        self.add(Ellipse(width=width, height=height, color=kwargs.get("color", WHITE)))
        for _ in range(5):
            self.add(Ellipse(
                width=width*0.6, height=height*0.6, 
                color=kwargs.get("color", WHITE)
            ).shift(np.array([
                random.uniform(-width/3, width/3),
                random.uniform(-height/3, height/3),
                0
            ])))