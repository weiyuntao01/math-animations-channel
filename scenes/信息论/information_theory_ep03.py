from manim import *
import numpy as np
import random

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 秩序 / 生命 / 负熵
IT_RED = "#FF2A68"       # 混乱 / 熵增 / 热寂
IT_BLUE = "#00BFFF"      # 结构 / 物理法则
IT_YELLOW = "#FFD700"    # 能量 / 核心概念
IT_PURPLE = "#8B5CF6"    # 哲学 / 标题 / 公式
IT_GRAY = "#333333"      # 背景容器
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP03(Scene):
    """信息论 EP03: 熵增定律 (逻辑修正+分页优化版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：房间为什么会变乱？
        self.intro_chaos()
        
        # 2. 微观视角：玻尔兹曼的骰子
        self.microstate_demo()
        
        # 3. 核心公式：S = k ln W
        self.boltzmann_formula()
        
        # 4. 香农熵：信息的不确定性 (已修复概率和为1)
        self.shannon_entropy_connection()
        
        # 5. 哲学升华：生命即逆熵 (已修复重叠，改为分页展示)
        self.show_life_philosophy()

    def intro_chaos(self):
        """开场：从生活现象引入"""
        
        title = Text("EP03: 熵增定律", font_size=54, color=IT_RED, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("The Second Law of Thermodynamics", font_size=28, color=IT_GRAY).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        question = Text("为什么你的房间总是自动变乱？", font_size=32, color=WHITE).move_to(UP * 0.5)
        self.play(Write(question))
        self.wait(1)
        
        # 视觉演示：整齐 -> 混乱
        squares = VGroup(*[
            Square(side_length=0.4, fill_color=IT_BLUE, fill_opacity=0.8, stroke_width=1)
            for _ in range(16)
        ]).arrange_in_grid(4, 4, buff=0.1).move_to(DOWN * 1.5)
        
        label_order = Text("有序 (Order)", font_size=24, color=IT_BLUE).next_to(squares, DOWN)
        
        self.play(FadeIn(squares), Write(label_order))
        self.wait(1)
        
        random_positions = []
        for _ in range(16):
            x = random.uniform(-4, 4)
            y = random.uniform(-3.5, -0.5)
            random_positions.append([x, y, 0])
            
        anims = []
        for sq, pos in zip(squares, random_positions):
            anims.append(sq.animate.move_to(pos).rotate(random.uniform(0, PI)))
            
        self.play(
            *anims,
            Transform(label_order, Text("混乱 (Chaos)", font_size=24, color=IT_RED).move_to(DOWN * 3.8)),
            run_time=2
        )
        
        answer = Text("因为\"乱\"的方式比\"整齐\"多得多！", font_size=28, color=IT_YELLOW).move_to(DOWN * 0.5)
        self.play(Transform(question, answer))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def microstate_demo(self):
        """微观视角：粒子分布实验"""
        
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("微观视角：粒子的选择", font_size=36, color=IT_BLUE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        box = Rectangle(width=5, height=4, color=WHITE)
        box.move_to(LEFT_ZONE)
        divider = DashedLine(box.get_top(), box.get_bottom(), color=IT_GRAY)
        
        self.play(Create(box), Create(divider))
        
        particles = VGroup()
        colors = [IT_GREEN, IT_BLUE, IT_YELLOW, IT_RED]
        for i in range(4):
            x = random.uniform(-2.3, -0.2) + LEFT_ZONE[0]
            y = random.uniform(-1.8, 1.8) + LEFT_ZONE[1]
            p = Dot(point=[x, y, 0], color=colors[i], radius=0.15)
            label = Integer(i+1, font_size=20, color=BLACK).move_to(p)
            particles.add(VGroup(p, label))
            
        self.play(FadeIn(particles))
        
        count_title = Text("微观状态数 (Microstates)", font_size=24, color=IT_YELLOW).move_to(RIGHT_ZONE + UP * 2)
        self.play(Write(count_title))
        
        case_a = VGroup(
            Text("情况 A: 全部在左", font_size=20),
            MathTex(r"\Omega = 1", color=IT_BLUE),
            Text("(只有 1 种排列)", font_size=18, color=IT_GRAY)
        ).arrange(DOWN).next_to(count_title, DOWN, buff=0.5)
        
        self.play(Write(case_a))
        self.wait(1)
        
        p3_target = [random.uniform(0.2, 2.3) + LEFT_ZONE[0], random.uniform(-1.8, 1.8) + LEFT_ZONE[1], 0]
        p4_target = [random.uniform(0.2, 2.3) + LEFT_ZONE[0], random.uniform(-1.8, 1.8) + LEFT_ZONE[1], 0]
        
        self.play(
            particles[2].animate.move_to(p3_target),
            particles[3].animate.move_to(p4_target),
            run_time=1.5
        )
        
        case_b = VGroup(
            Text("情况 B: 2左 2右", font_size=20),
            MathTex(r"\Omega = C(4,2) = 6", color=IT_RED),
            Text("(有 6 种排列!)", font_size=18, color=IT_GRAY)
        ).arrange(DOWN).next_to(case_a, DOWN, buff=0.5)
        
        self.play(Write(case_b))
        
        conclusion = VGroup(
            Text("混乱的状态数 >> 有序的状态数", font_size=22, color=IT_RED),
            Text("自然界倾向于高概率状态", font_size=22, color=IT_GREEN)
        ).arrange(DOWN).move_to(RIGHT_ZONE + DOWN * 2)
        
        self.play(Write(conclusion))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def boltzmann_formula(self):
        """核心公式：S = k ln W"""
        
        title = Text("物理学最性感的公式", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        formula = MathTex(
            r"S", r"=", r"k", r"\cdot", r"\ln", r"\Omega",
            font_size=80
        )
        formula[0].set_color(IT_RED)    # S
        formula[2].set_color(IT_GRAY)   # k
        formula[5].set_color(IT_YELLOW) # Omega
        
        formula.shift(UP * 0.5)
        self.play(Write(formula))
        
        arrow_s = Arrow(formula[0].get_bottom() + DOWN*0.5, formula[0].get_bottom(), color=IT_RED).shift(DOWN*0.2)
        label_s = Text("熵 (混乱度)", font_size=24, color=IT_RED).next_to(arrow_s, DOWN)
        
        arrow_w = Arrow(formula[5].get_bottom() + DOWN*0.5, formula[5].get_bottom(), color=IT_YELLOW).shift(DOWN*0.2)
        label_w = Text("微观状态数量\n(可能性)", font_size=24, color=IT_YELLOW).next_to(arrow_w, DOWN)
        
        self.play(
            GrowArrow(arrow_s), Write(label_s),
            GrowArrow(arrow_w), Write(label_w)
        )
        
        logic_text = Text(
            "可能性越多 (Ω大) -> 熵越高 (S大) -> 越混乱", 
            font_size=32, 
            gradient=(IT_YELLOW, IT_RED)
        ).to_edge(DOWN, buff=1.5)
        
        self.play(Write(logic_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def shannon_entropy_connection(self):
            """连接香农熵 (图表重绘版)"""
            
            LEFT_ZONE = LEFT * 3.5
            RIGHT_ZONE = RIGHT * 3.5
            
            title = Text("从物理熵到信息熵", font_size=36, color=IT_BLUE).to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            # 辅助函数：创建标准柱状图
            def create_chart(probabilities, color, title_str, sub_str):
                # 1. 坐标轴
                ax = Axes(
                    x_range=[0, 5, 1],  # 0~5, 步长1
                    y_range=[0, 1, 0.25], # 0~1, 步长0.25
                    x_length=4, y_length=3,
                    axis_config={"color": WHITE, "include_numbers": True, "font_size": 16},
                    tips=False
                )
                
                # 2. 柱状图
                bars = VGroup()
                for i, p in enumerate(probabilities):
                    # 计算柱子高度和位置
                    # x 坐标：i+1 (1, 2, 3, 4)
                    # y 坐标：p
                    
                    # bar_height = p * (y_axis_length / y_range_span)
                    # 更简单的方法：用 c2p 计算顶点和底点距离
                    p_top = ax.c2p(i+1, p)
                    p_bottom = ax.c2p(i+1, 0)
                    height = p_top[1] - p_bottom[1]
                    
                    bar = Rectangle(
                        width=0.6, height=height,
                        fill_color=color, fill_opacity=0.8,
                        stroke_color=WHITE, stroke_width=1
                    )
                    # 底部对齐 X 轴
                    bar.move_to(ax.c2p(i+1, 0), aligned_edge=DOWN)
                    bars.add(bar)
                    
                    # 添加柱顶数值
                    val_text = DecimalNumber(p, num_decimal_places=2, font_size=14, color=color)
                    val_text.next_to(bar, UP, buff=0.1)
                    bars.add(val_text)

                # 3. 标签
                chart_title = Text(title_str, font_size=24, color=color).next_to(ax, UP, buff=0.5)
                chart_sub = Text(sub_str, font_size=18, color=IT_GRAY).next_to(ax, DOWN, buff=0.7)
                
                return VGroup(ax, bars, chart_title, chart_sub)

            # --- 1. 左侧：均匀分布 (High Entropy) ---
            # 概率分布：均等
            probs_uniform = [0.25, 0.25, 0.25, 0.25]
            chart_left = create_chart(
                probs_uniform, 
                IT_RED, 
                "均匀分布 (高熵)", 
                "完全不可预测\n信息量最大"
            )
            chart_left.move_to(LEFT_ZONE)
            
            self.play(FadeIn(chart_left))
            
            # --- 2. 右侧：确定分布 (Low Entropy) ---
            # 概率分布：极度集中 (概率和严格为 1.0)
            probs_peaked = [0.05, 0.80, 0.10, 0.05]
            chart_right = create_chart(
                probs_peaked, 
                IT_GREEN, 
                "尖峰分布 (低熵)", 
                "高度可预测\n信息量很小"
            )
            chart_right.move_to(RIGHT_ZONE)
            
            self.play(FadeIn(chart_right))
            
            # --- 总结文字 ---
            summary = Text("要想获得信息，必须消除这种混乱", font_size=28, color=IT_YELLOW)
            # 放在两个图表中间下方，或者屏幕底部
            summary.to_edge(DOWN, buff=0.5)
            
            self.play(Write(summary))
            
            self.wait(3)
            self.play(FadeOut(Group(*self.mobjects)))

    def show_life_philosophy(self):
        """哲学升华：生命即逆熵 (分页展示，防止重叠)"""
        
        title = Text("生命的本质", font_size=40, color=IT_GREEN).to_edge(UP, buff=1.0)
        
        # 1. 薛定谔名言
        quote = Text("“生命以负熵为食。”\n—— 薛定谔", font_size=32, color=IT_BLUE, slant=ITALIC)
        quote.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), Write(quote))
        
        # 2. 视觉演示：对抗
        life_core = Circle(radius=1.0, color=IT_GREEN, fill_opacity=0.5).move_to(DOWN * 0.5)
        life_label = Text("生命/自律", font_size=24).move_to(life_core)
        
        self.play(FadeIn(life_core), Write(life_label))
        
        chaos_particles = VGroup()
        for _ in range(50):
            angle = random.uniform(0, TAU)
            dist = random.uniform(1.5, 3.5)
            pos = np.array([dist*np.cos(angle), dist*np.sin(angle) - 0.5, 0])
            p = Dot(pos, color=IT_RED, radius=0.05)
            chaos_particles.add(p)
            
        self.play(FadeIn(chaos_particles))
        
        # 动画：抵抗熵增
        self.play(
            chaos_particles.animate.scale(0.8), # 混乱逼近
            life_core.animate.set_color(IT_YELLOW).scale(1.1), # 生命反抗
            run_time=1.5
        )
        self.play(
            chaos_particles.animate.scale(1.2), # 混乱被推开
            life_core.animate.set_color(IT_GREEN).scale(1/1.1),
            run_time=1.5
        )
        
        self.wait(2)
        
        # --- 核心修改：清场换页 ---
        self.play(
            FadeOut(title), FadeOut(quote), 
            FadeOut(life_core), FadeOut(life_label), 
            FadeOut(chaos_particles)
        )
        
        # 3. 金句 (在干净的页面展示)
        lines = VGroup(
            Text("宇宙的趋势是变乱 (熵增)", font_size=28, color=IT_RED),
            Text("房间不理会乱，关系不维系会散", font_size=28, color=IT_GRAY),
            Text("自律的本质，就是向系统注入能量", font_size=36, color=IT_YELLOW, weight=BOLD),
            Text("在这个走向热寂的宇宙中，维持秩序", font_size=36, color=IT_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.6).move_to(ORIGIN) # 居中展示
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(3)
        self.play(FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：冗余的智慧", font_size=40, color=IT_BLUE).move_to(UP * 0.5)
        desc = Text("为什么重要的话要说三遍？\n容错率是生存的护城河。", font_size=24, color=IT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))