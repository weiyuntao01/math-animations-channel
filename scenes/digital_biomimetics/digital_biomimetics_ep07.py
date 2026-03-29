"""
数字仿生系列 第7集：大脑的电光火花
Digital Biomimetics EP07: Sparks of the Brain

从神经元到神经网络 - 大脑如何思考？
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple


# 系列通用色彩
BIO_CYAN = ManimColor("#00FFE5")
BIO_PURPLE = ManimColor("#8B5CF6")
BIO_GREEN = ManimColor("#00FF88")
BIO_BLUE = ManimColor("#007EFF")
BIO_YELLOW = ManimColor("#FFE500")
BIO_RED = ManimColor("#FF0066")
BIO_WHITE = ManimColor("#FFFFFF")
BIO_GRAY = ManimColor("#303030")

# EP07 主题色
NEURAL_GREEN = ManimColor("#32CD32")
ELECTRIC_BLUE = ManimColor("#00BFFF")
SPARK_YELLOW = ManimColor("#FFD700")

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class DigitalBiomimeticsEP07(Scene):
    """数字仿生系列 第7集"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        # 1. 系列开场
        self.show_series_intro()

        # 2. 回应EP06预告
        self.answer_preview_question()

        # 3. 数学本质：大脑的电学原理
        self.brain_mathematics()

        # 4. 生命形态 I：神经元的电脉冲
        self.neuron_pulse_scene()

        # 5. 生命形态 II：神经网络传播
        self.neural_network_scene()

        # 6. 结尾与预告
        self.show_ending()

    def show_series_intro(self):
        """系列开场动画 - 电光火花背景 + 标题"""
        bg = self.create_brain_spark_background()
        bg.set_opacity(0.2)
        self.play(Create(bg), run_time=2)

        series_title = Text("数字仿生", font_size=60, color=BIO_CYAN, weight=BOLD).move_to([0, 1, 0])
        subtitle = Text("DIGITAL BIOMIMETICS", font_size=24, color=BIO_WHITE, font="Arial").next_to(series_title, DOWN, buff=0.3)
        episode_text = Text("第7集：大脑的电光火花", font_size=34, color=ELECTRIC_BLUE).move_to([0, -1.5, 0])

        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.play(Write(episode_text), run_time=1.5)
        self.play(series_title.animate.scale(1.1).set_color(SPARK_YELLOW), rate_func=there_and_back, run_time=1)
        self.wait(2)
        self.play(FadeOut(series_title), FadeOut(subtitle), FadeOut(episode_text), FadeOut(bg))

    def create_brain_spark_background(self):
        """创建电光火花背景"""
        group = VGroup()
        
        # 创建放射状的电光效果
        for i in range(12):
            angle = i * 2 * PI / 12
            for j in range(3):
                radius = 1 + j * 1.5
                x = radius * np.cos(angle)
                y = radius * np.sin(angle) * 0.7
                
                # 电光线条
                spark = Line(
                    [0, 0, 0],
                    [x, y, 0],
                    color=interpolate_color(ELECTRIC_BLUE, SPARK_YELLOW, j/3),
                    stroke_width=2,
                    stroke_opacity=0.3
                )
                group.add(spark)
                
                # 闪光点
                dot = Dot(
                    [x, y, 0],
                    radius=0.05,
                    color=SPARK_YELLOW,
                    fill_opacity=0.6
                )
            group.add(dot)
        
        return group

    def answer_preview_question(self):
        """回应EP06预告：真实大脑与AI的'智能'，有何不同？"""
        title = Text("大脑 vs 人工智能", font_size=TITLE_SIZE, color=ELECTRIC_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 创建对比表格
        left_side = VGroup(
            Text("真实大脑", font_size=SUBTITLE_SIZE, color=NEURAL_GREEN, weight=BOLD),
            Text("• 1000亿个神经元", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("• 电脉冲信号", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("• 生物化学反应", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("• 自我学习", font_size=NORMAL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        left_side.move_to([-3, 0, 0])
        
        right_side = VGroup(
            Text("人工智能", font_size=SUBTITLE_SIZE, color=BIO_PURPLE, weight=BOLD),
            Text("• 数百万个节点", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("• 数字信号", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("• 数学计算", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("• 训练学习", font_size=NORMAL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        right_side.move_to([3, 0, 0])
        
        vs_arrow = Text("VS", font_size=40, color=SPARK_YELLOW, weight=BOLD)
        vs_arrow.move_to([0, 0.5, 0])
        
        self.play(Write(left_side))
        self.play(Write(vs_arrow))
        self.play(Write(right_side))
        
        insight = Text("都在模拟智能，但原理截然不同", font_size=SUBTITLE_SIZE, color=BIO_CYAN)
        insight.to_edge(DOWN, buff=0.8)
        self.play(Write(insight))
        
        self.wait(3)
        self.play(
            FadeOut(title),
            FadeOut(left_side),
            FadeOut(right_side),
            FadeOut(vs_arrow),
            FadeOut(insight)
        )

    def brain_mathematics(self):
        """大脑的电学原理 - 简化版"""
        title = Text("大脑的数学密码", font_size=TITLE_SIZE, color=ELECTRIC_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 神经元的核心公式
        formula_title = Text("神经元的电学原理", font_size=SUBTITLE_SIZE, color=NEURAL_GREEN)
        formula_title.move_to([0, 1.5, 0])
        
        # 简化的电容充电公式
        main_formula = MathTex(
            r"V = V_0 \cdot e^{-t/\tau}",
            font_size=40,
            color=BIO_CYAN
        )
        main_formula.move_to([0, 0.5, 0])
        
        # 解释
        explanation = VGroup(
            Text("V = 神经元电压", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("τ = 时间常数", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("当V达到阈值，神经元放电！", font_size=NORMAL_SIZE, color=SPARK_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        explanation.move_to([0, -1.5, 0])
        
        self.play(Write(formula_title))
        self.play(Write(main_formula))
        for line in explanation:
            self.play(Write(line), run_time=0.8)
        
        # 核心洞察
        insight = Text("大脑 = 千亿个小电容的协调放电", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        insight.to_edge(DOWN, buff=0.8)
        self.play(Write(insight))
        
        self.wait(3)
        self.play(
            FadeOut(title),
            FadeOut(formula_title),
            FadeOut(main_formula),
            FadeOut(explanation),
            FadeOut(insight)
        )

    def neuron_pulse_scene(self):
        """神经元电脉冲 - 简化可视化"""
        self.clear()

        title = Text("生命形态 I：神经元的电脉冲", font_size=SUBTITLE_SIZE, color=ELECTRIC_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建神经元形状
        def create_neuron():
            t = t_tracker.get_value()
            neuron = VGroup()
            
            # 神经元细胞体
            cell_body = Circle(radius=0.5, color=NEURAL_GREEN, fill_opacity=0.3)
            cell_body.move_to([0, 0, 0])
            
            # 根据时间调整发光强度
            pulse = np.sin(t * 3) * 0.5 + 0.5  # 0到1之间的脉动
            glow_intensity = 0.3 + pulse * 0.7
            cell_body.set_fill_opacity(glow_intensity)
            
            neuron.add(cell_body)
            
            # 神经元轴突（突起）
            for i in range(6):
                angle = i * PI / 3
                axon = Line(
                    [0, 0, 0],
                    [2 * np.cos(angle), 2 * np.sin(angle), 0],
                    color=NEURAL_GREEN,
                    stroke_width=3
                )
                neuron.add(axon)
                
                # 电脉冲沿轴突传播
                pulse_pos = (t * 0.5) % 2  # 脉冲位置
                if pulse_pos < 1.8:
                    spark = Dot(
                        [pulse_pos * np.cos(angle), pulse_pos * np.sin(angle), 0],
                        radius=0.1,
                        color=SPARK_YELLOW,
                        fill_opacity=0.9
                    )
                    neuron.add(spark)
            
            return neuron
        
        neuron = always_redraw(create_neuron)
        
        # 说明文字
        description = Text("神经元通过电脉冲传递信息", font_size=SMALL_SIZE, color=BIO_WHITE)
        description.to_edge(DOWN, buff=0.5)
        
        self.add(neuron)
        self.play(Write(description))
        
        # 动画：电脉冲传播
        self.play(
            t_tracker.animate.set_value(8 * PI),
            run_time=12,
            rate_func=linear
        )
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(neuron),
            FadeOut(description)
        )

    def neural_network_scene(self):
        """神经网络传播 - 信息在网络中的传播"""
        self.clear()

        title = Text("生命形态 II：神经网络传播", font_size=SUBTITLE_SIZE, color=BIO_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建神经网络
        def create_network():
            t = t_tracker.get_value()
            network = VGroup()
            
            # 创建神经元节点
            neurons = []
            for layer in range(4):
                layer_neurons = []
                for node in range(5):
                    x = -4 + layer * 2.5
                    y = -2 + node * 1
                    neuron = Circle(
                        radius=0.15,
                        color=NEURAL_GREEN,
                        fill_opacity=0.5
                    )
                    neuron.move_to([x, y, 0])
                    
                    # 添加激活效果
                    activation_time = t + layer * 0.5 + node * 0.2
                    if np.sin(activation_time * 2) > 0.5:
                        neuron.set_fill_color(SPARK_YELLOW)
                        neuron.set_fill_opacity(0.9)
                        # 添加发光效果
                        glow = Circle(
                            radius=0.25,
                            color=SPARK_YELLOW,
                            fill_opacity=0.2,
                            stroke_opacity=0
                        )
                        glow.move_to([x, y, 0])
                        network.add(glow)
                    
                    network.add(neuron)
                    layer_neurons.append([x, y, 0])
                neurons.append(layer_neurons)
            
            # 创建连接线（使用确定性模式，避免random）
            for layer in range(3):
                for from_node in range(5):
                    for to_node in range(5):
                        from_pos = neurons[layer][from_node]
                        to_pos = neurons[layer + 1][to_node]
                        
                        # 使用确定性条件激活连接
                        connection_id = layer * 25 + from_node * 5 + to_node
                        signal_time = t + layer * 0.3 + connection_id * 0.1
                        
                        # 用sin函数代替random，使某些连接周期性激活
                        if np.sin(signal_time * 2 + connection_id) > 0.3:
                            connection = Line(
                                from_pos,
                                to_pos,
                                color=ELECTRIC_BLUE,
                                stroke_width=2,
                                stroke_opacity=0.3 + 0.4 * np.sin(signal_time * 3)
                            )
                            network.add(connection)
            
            # 添加传播粒子
            for layer in range(3):
                for particle_id in range(8):
                    # 粒子在连接间移动
                    progress = (t * 0.5 + particle_id * 0.2) % 2
                    if progress < 1:
                        from_pos = neurons[layer][particle_id % 5]
                        to_pos = neurons[layer + 1][(particle_id + 1) % 5]
                        
                        particle_x = from_pos[0] + progress * (to_pos[0] - from_pos[0])
                        particle_y = from_pos[1] + progress * (to_pos[1] - from_pos[1])
                        
                        particle = Dot(
                            [particle_x, particle_y, 0],
                            radius=0.05,
                            color=SPARK_YELLOW,
                            fill_opacity=0.8
                        )
                        network.add(particle)
            
            return network
        
        network = always_redraw(create_network)
        
        # 说明文字
        description = Text("信息像波浪一样在神经网络中传播", font_size=SMALL_SIZE, color=BIO_WHITE)
        description.to_edge(DOWN, buff=0.5)
        
        self.add(network)
        self.play(Write(description))
        
        # 动画：网络信号传播
        self.play(
            t_tracker.animate.set_value(6 * PI),
            run_time=15,
            rate_func=linear
        )
        
        self.wait(2)
        self.play(
            FadeOut(title),
            FadeOut(network),
            FadeOut(description)
        )



    def show_ending(self):
        """结尾与下期预告"""
        self.clear()

        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=ELECTRIC_BLUE)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))

        recap = VGroup(
            Text("✓ 大脑的电学原理", font_size=NORMAL_SIZE),
            Text("✓ 神经元的电脉冲传播", font_size=NORMAL_SIZE),
            Text("✓ 神经网络的信息流动", font_size=NORMAL_SIZE),
            Text("✓ 数学让我们理解思维", font_size=NORMAL_SIZE, color=SPARK_YELLOW, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        recap.move_to([0, 0.5, 0])

        for line in recap:
            self.play(Write(line), run_time=0.6)

        self.wait(2)
        self.play(FadeOut(recap_title), FadeOut(recap))

        philosophy = VGroup(
            Text("思维的电光火花", font_size=38, color=NEURAL_GREEN),
            Text("源自数学的精密设计", font_size=38, color=BIO_PURPLE),
            Text("大脑，是自然界最美的方程", font_size=SUBTITLE_SIZE, color=SPARK_YELLOW)
        ).arrange(DOWN, buff=0.6)

        for line in philosophy:
            self.play(Write(line), run_time=1)

        self.wait(2)
        self.play(FadeOut(philosophy))

        self.show_next_episode_preview()

    def show_next_episode_preview(self):
        """下期预告：DNA的信息宇宙（EP08）"""
        preview_title = Text("下期预告", font_size=38, color=BIO_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))

        ep8_title = Text(
            "第8集：DNA的信息宇宙",
            font_size=TITLE_SIZE,
            color=BIO_PURPLE,
            weight=BOLD
        )
        ep8_title.move_to([0, 1.5, 0])

        preview_content = VGroup(
            Text("双螺旋的几何美学", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("遗传密码的信息论", font_size=SUBTITLE_SIZE, color=BIO_GREEN),
            Text("从分子到生命的奇迹", font_size=SUBTITLE_SIZE, color=BIO_PURPLE)
        ).arrange(DOWN, buff=0.5)
        preview_content.move_to([0, -0.5, 0])

        self.play(Write(ep8_title))
        for line in preview_content:
            self.play(Write(line), run_time=0.8)

        think_question = Text(
            "思考：4个字母如何编写生命的全部故事？",
            font_size=20,
            color=BIO_YELLOW
        )
        think_question.to_edge(DOWN, buff=0.5)
        self.play(Write(think_question))

        self.wait(3)

        see_you = Text(
            "下期再见！",
            font_size=38,
            color=BIO_WHITE
        )
        see_you.move_to(ORIGIN)

        self.play(
            FadeOut(preview_title),
            FadeOut(ep8_title),
            FadeOut(preview_content),
            FadeOut(think_question),
            Write(see_you)
        )

        # 最后的电光火花动画
        final_spark = self.create_brain_spark_background()
        final_spark.scale(0.5).set_opacity(0.3)
        self.play(Create(final_spark), run_time=2)

        self.wait(2)
        self.play(FadeOut(see_you), FadeOut(final_spark))




