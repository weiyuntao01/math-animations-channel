"""
数学之美系列 EP06 - 谣言传播的SIR模型
为什么谣言传这么快？流行病学模型的数学真相
6分钟深度科普
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple

# 品牌色彩系统
BRAND_PURPLE = "#8B5CF6"
BRAND_PINK = "#FF006E"
BRAND_BLUE = "#00F5FF"
BRAND_YELLOW = "#FFD60A"
BRAND_GREEN = "#06FFB4"
BRAND_RED = "#FF4444"
BRAND_GRAY = "#6B7280"

class RumorSIRModelEP06(Scene):
    """EP06: 谣言传播的SIR模型
    
    用真实的流行病学数学模型解释信息传播
    包含微分方程、R₀计算、网络效应等核心概念
    """
    
    def construct(self):
        # 设置中文字体和背景
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#0A0E27"
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场：一条谣言毁掉一家店（30秒）
        self.show_opening()
        
        # 2. SIR模型的建立（90秒）
        self.introduce_sir_model()
        
        # 3. R₀与传播临界值（120秒）
        self.r_naught_analysis()
        
        # 4. 网络拓扑的作用（90秒）
        self.network_topology_effect()
        
        # 5. 辟谣的数学策略（60秒）
        self.debunking_strategies()
        
        # 6. 信息疫苗的设计（30秒）
        self.information_vaccine()
    
    def show_opening(self):
        """开场：一条谣言毁掉一家店"""
        # 痛点展示
        hook = VGroup(
            Text("某餐厅用地沟油", font_size=44, color=BRAND_RED),
            Text("3小时后...", font_size=36, color=WHITE),
            Text("10万人转发", font_size=52, color=BRAND_YELLOW, weight=BOLD),
            Text("店铺永久关闭", font_size=60, color=BRAND_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(hook[0], run_time=0.6))
        self.wait(0.5)
        self.play(Write(hook[1], run_time=0.4))
        self.play(
            Write(hook[2], run_time=0.6),
            hook[2].animate.scale(1.1)
        )
        self.play(
            Write(hook[3], run_time=0.8),
            hook[3].animate.set_color(BRAND_RED)
        )
        self.wait(1)
        
        # 转场到科学解释
        truth = Text(
            "谣言传播遵循数学规律",
            font_size=44,
            color=BRAND_GREEN,
            weight=BOLD
        )
        truth.set_stroke(color=BRAND_GREEN, width=2)
        
        self.play(
            FadeOut(hook, shift=UP),
            FadeIn(truth, shift=UP)
        )
        self.wait(1)
        self.play(FadeOut(truth))
    
    def introduce_sir_model(self):
        """SIR模型的建立"""
        # 标题
        title = Text("SIR模型：流行病学的经典", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 采用上下分层布局，而不是左右布局
        
        # 第一层：SIR状态定义 - 水平排列在上方
        states_row = VGroup()
        
        # S - 易感者
        s_group = VGroup(
            Circle(radius=0.5, fill_color=BRAND_BLUE, fill_opacity=0.7, stroke_width=3),
            Text("S", font_size=36, color=WHITE, weight=BOLD)
        )
        s_label = Text("Susceptible", font_size=24, color=BRAND_BLUE, weight=BOLD)
        s_desc = Text("未接触谣言的人", font_size=22, color=WHITE)
        s_complete = VGroup(s_group, s_label, s_desc).arrange(DOWN, buff=0.2)
        s_complete.shift(LEFT * 4)
        
        # I - 感染者
        i_group = VGroup(
            Circle(radius=0.5, fill_color=BRAND_RED, fill_opacity=0.7, stroke_width=3),
            Text("I", font_size=36, color=WHITE, weight=BOLD)
        )
        i_label = Text("Infected", font_size=24, color=BRAND_RED, weight=BOLD)
        i_desc = Text("正在传播谣言的人", font_size=22, color=WHITE)
        i_complete = VGroup(i_group, i_label, i_desc).arrange(DOWN, buff=0.2)
        i_complete.shift(ORIGIN)
        
        # R - 恢复者
        r_group = VGroup(
            Circle(radius=0.5, fill_color=BRAND_GREEN, fill_opacity=0.7, stroke_width=3),
            Text("R", font_size=36, color=WHITE, weight=BOLD)
        )
        r_label = Text("Recovered", font_size=24, color=BRAND_GREEN, weight=BOLD)
        r_desc = Text("不再传播的人", font_size=22, color=WHITE)
        r_complete = VGroup(r_group, r_label, r_desc).arrange(DOWN, buff=0.2)
        r_complete.shift(RIGHT * 4)
        
        states_row.add(s_complete, i_complete, r_complete)
        states_row.shift(UP * 1.5)
        
        # 显示状态
        for state in [s_complete, i_complete, r_complete]:
            self.play(FadeIn(state), run_time=0.6)
        
        # 第二层：转移箭头和参数 - 在状态圆圈之间
        arrows = VGroup()
        
        # S -> I 箭头
        arrow1 = CurvedArrow(
            s_group.get_right() + RIGHT * 0.3,
            i_group.get_left() + LEFT * 0.3,
            color=BRAND_YELLOW,
            angle=-TAU/8,
            stroke_width=4
        )
        beta_group = VGroup(
            MathTex(r"\beta", font_size=32, color=BRAND_YELLOW),
            Text("接触率", font_size=20, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.1)
        beta_group.next_to(arrow1, UP, buff=0.3)
        
        # I -> R 箭头
        arrow2 = CurvedArrow(
            i_group.get_right() + RIGHT * 0.3,
            r_group.get_left() + LEFT * 0.3,
            color=BRAND_YELLOW,
            angle=-TAU/8,
            stroke_width=4
        )
        gamma_group = VGroup(
            MathTex(r"\gamma", font_size=32, color=BRAND_YELLOW),
            Text("恢复率", font_size=20, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.1)
        gamma_group.next_to(arrow2, UP, buff=0.3)
        
        arrows.add(arrow1, beta_group, arrow2, gamma_group)
        
        self.play(Create(arrow1), Write(beta_group), run_time=0.8)
        self.play(Create(arrow2), Write(gamma_group), run_time=0.8)
        
        # 第三层：微分方程组 - 底部居中
        equations_section = VGroup()
        
        equations_title = Text("SIR微分方程组", font_size=32, color=BRAND_PURPLE, weight=BOLD)
        
        equations = VGroup(
            MathTex(r"\frac{dS}{dt} = -\beta \frac{SI}{N}", font_size=36),
            MathTex(r"\frac{dI}{dt} = \beta \frac{SI}{N} - \gamma I", font_size=36),
            MathTex(r"\frac{dR}{dt} = \gamma I", font_size=36)
        ).arrange(DOWN, buff=0.4)
        
        # 参数说明
        params = VGroup(
            Text("N = 总人口", font_size=22, color=BRAND_GRAY),
            Text("β = 传播率", font_size=22, color=BRAND_GRAY),
            Text("γ = 恢复率", font_size=22, color=BRAND_GRAY)
        ).arrange(RIGHT, buff=1.0)
        
        equations_section.add(equations_title, equations, params)
        equations_section.arrange(DOWN, buff=0.5)
        equations_section.shift(DOWN * 2.2)
        
        self.play(Write(equations_title))
        self.wait(0.3)
        for eq in equations:
            self.play(Write(eq), run_time=0.7)
        self.play(FadeIn(params))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, states_row, arrows, equations_section)))
    
    def r_naught_analysis(self):
        """R₀与传播临界值"""
        # 标题
        title = Text("R₀：传播的关键数字", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # R₀的定义 - 顶部中央
        r0_def = VGroup(
            MathTex(r"R_0 = \frac{\beta}{\gamma}", font_size=48, color=BRAND_YELLOW),
            Text("基本再生数", font_size=24, color=BRAND_YELLOW),
            Text("一个感染者平均传染的人数", font_size=22, color=WHITE)
        ).arrange(DOWN, buff=0.2)
        r0_def.shift(UP * 1.2)
        
        self.play(Write(r0_def[0]))
        self.play(Write(r0_def[1]))
        self.play(Write(r0_def[2]))
        
        # 左侧：R₀ < 1 的情况
        left_title = Text("R₀ < 1：谣言消亡", font_size=26, color=BRAND_GREEN, weight=BOLD)
        left_title.shift(LEFT * 3.5 + DOWN * 0.3)
        
        # 创建消亡动画
        extinction_graph = self.create_extinction_graph()
        extinction_graph.shift(LEFT * 3.5 + DOWN * 1.8)
        
        self.play(Write(left_title))
        self.play(Create(extinction_graph))
        
        # 右侧：R₀ > 1 的情况
        right_title = Text("R₀ > 1：谣言爆发", font_size=26, color=BRAND_RED, weight=BOLD)
        right_title.shift(RIGHT * 3.5 + DOWN * 0.3)
        
        # 创建爆发动画
        outbreak_graph = self.create_outbreak_graph()
        outbreak_graph.shift(RIGHT * 3.5 + DOWN * 1.8)
        
        self.play(Write(right_title))
        self.play(Create(outbreak_graph))
        
        # 临界条件
        critical = Text(
            "临界点：R₀ = 1",
            font_size=32,
            color=BRAND_PURPLE,
            weight=BOLD
        )
        critical.shift(DOWN * 2.8)
        self.play(Write(critical))
        
        self.wait(2)
        
        # 转场到具体数值
        self.play(FadeOut(VGroup(title, r0_def, left_title, extinction_graph, 
                                right_title, outbreak_graph, critical)))
        
        # 展示不同谣言的R₀值
        self.show_r0_examples()
    
    def create_extinction_graph(self):
        """创建消亡曲线"""
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 0.2, 0.05],
            x_length=3,
            y_length=2,
            axis_config={"include_numbers": False}
        )
        
        # R₀ = 0.5的曲线
        t = np.linspace(0, 10, 100)
        I = 0.1 * np.exp(-0.5 * t)  # 指数衰减
        
        curve = axes.plot_line_graph(
            x_values=t,
            y_values=I,
            line_color=BRAND_GREEN,
            stroke_width=3,
            add_vertex_dots=False
        )
        
        # 标签
        x_label = Text("时间", font_size=16).next_to(axes.x_axis, DOWN, buff=0.1)
        y_label = Text("感染率", font_size=16).next_to(axes.y_axis, LEFT, buff=0.1)
        
        return VGroup(axes, curve, x_label, y_label)
    
    def create_outbreak_graph(self):
        """创建爆发曲线"""
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 0.8, 0.2],
            x_length=3,
            y_length=2,
            axis_config={"include_numbers": False}
        )
        
        # R₀ = 3的SIR曲线
        t = np.linspace(0, 10, 100)
        # 简化的logistic增长曲线
        I = 0.8 / (1 + 50 * np.exp(-3 * (t - 2)))
        
        curve = axes.plot_line_graph(
            x_values=t,
            y_values=I,
            line_color=BRAND_RED,
            stroke_width=3,
            add_vertex_dots=False
        )
        
        # 标签
        x_label = Text("时间", font_size=16).next_to(axes.x_axis, DOWN, buff=0.1)
        y_label = Text("感染率", font_size=16).next_to(axes.y_axis, LEFT, buff=0.1)
        
        return VGroup(axes, curve, x_label, y_label)
    
    def show_r0_examples(self):
        """展示不同谣言的R₀值"""
        title = Text("真实世界的R₀值", font_size=36, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 创建对比表格 - 重新设计布局避免重叠
        examples = VGroup()
        
        # 表头
        header = VGroup(
            Text("谣言类型", font_size=22, color=BRAND_GRAY, weight=BOLD),
            Text("R₀值", font_size=22, color=BRAND_GRAY, weight=BOLD),
            Text("传播特征", font_size=22, color=BRAND_GRAY, weight=BOLD)
        )
        header[0].shift(LEFT * 4 + UP * 1.8)
        header[1].shift(LEFT * 0.8 + UP * 1.8)
        header[2].shift(RIGHT * 3.2 + UP * 1.8)
        
        self.play(Write(header))
        
        # 数据 - 调整间距和位置
        rumor_data = [
            ("普通八卦", "1.5-2", BRAND_GRAY, "小范围传播"),
            ("明星绯闻", "3-5", BRAND_YELLOW, "快速扩散"),
            ("食品安全", "5-8", BRAND_RED, "爆炸传播"),
            ("政治谣言", "8-12", BRAND_PURPLE, "病毒式传播")
        ]
        
        # 增加行间距，从1.2开始
        start_y = 1.2
        row_spacing = 0.7
        
        for i, (name, r0, color, spread) in enumerate(rumor_data):
            y_pos = start_y - (i * row_spacing)
            
            # 谣言类型 - 左列
            type_text = Text(name, font_size=22, color=color, weight=BOLD)
            type_text.shift(LEFT * 4 + DOWN * y_pos)
            
            # R₀值 - 中列
            r0_text = Text(f"R₀ = {r0}", font_size=24, color=color, weight=BOLD)
            r0_text.shift(LEFT * 0.8 + DOWN * y_pos)
            
            # 传播特征 - 右列
            spread_text = Text(spread, font_size=20, color=WHITE)
            spread_text.shift(RIGHT * 3.2 + DOWN * y_pos)
            
            # 添加分隔线
            if i > 0:
                line = Line(
                    LEFT * 5.5 + DOWN * (y_pos + 0.35),
                    RIGHT * 5.5 + DOWN * (y_pos + 0.35),
                    stroke_width=1,
                    color=BRAND_GRAY,
                    stroke_opacity=0.3
                )
                examples.add(line)
                self.play(Create(line), run_time=0.2)
            
            example = VGroup(type_text, r0_text, spread_text)
            examples.add(example)
            
            self.play(FadeIn(example, shift=UP * 0.1), run_time=0.5)
        
        # 关键洞察 - 调整位置避免与表格重叠
        insight_bg = Rectangle(
            width=8, height=0.8,
            fill_color=BRAND_PINK, fill_opacity=0.1,
            stroke_color=BRAND_PINK, stroke_width=2
        )
        insight_bg.shift(DOWN * 3.2)
        
        insight = Text(
            "情绪越强烈，R₀越大",
            font_size=28,
            color=BRAND_PINK,
            weight=BOLD
        )
        insight.shift(DOWN * 3.2)
        
        self.play(Create(insight_bg))
        self.play(Write(insight))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, header, examples, insight_bg, insight)))
    
    def network_topology_effect(self):
        """网络拓扑的作用"""
        title = Text("网络结构决定传播速度", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 三种网络结构对比
        networks = VGroup()
        
        # 1. 规则网络（慢传播）
        regular_net = self.create_regular_network()
        regular_net.shift(LEFT * 5)
        regular_label = Text("规则网络", font_size=22, color=BRAND_GRAY)
        regular_speed = Text("传播速度：慢", font_size=20, color=BRAND_GREEN)
        regular_label.next_to(regular_net, UP, buff=0.3)
        regular_speed.next_to(regular_net, DOWN, buff=0.3)
        
        # 2. 随机网络（中等传播）
        random_net = self.create_random_network()
        random_net.shift(ORIGIN)
        random_label = Text("随机网络", font_size=22, color=BRAND_YELLOW)
        random_speed = Text("传播速度：中", font_size=20, color=BRAND_YELLOW)
        random_label.next_to(random_net, UP, buff=0.3)
        random_speed.next_to(random_net, DOWN, buff=0.3)
        
        # 3. 无标度网络（快速传播）
        scale_free_net = self.create_scale_free_network()
        scale_free_net.shift(RIGHT * 5)
        scale_free_label = Text("无标度网络", font_size=22, color=BRAND_RED)
        scale_free_speed = Text("传播速度：快", font_size=20, color=BRAND_RED)
        scale_free_label.next_to(scale_free_net, UP, buff=0.3)
        scale_free_speed.next_to(scale_free_net, DOWN, buff=0.3)
        
        networks.add(
            VGroup(regular_net, regular_label, regular_speed),
            VGroup(random_net, random_label, random_speed),
            VGroup(scale_free_net, scale_free_label, scale_free_speed)
        )
        
        for net in networks:
            self.play(Create(net[0]), Write(net[1]), Write(net[2]), run_time=0.8)
        
        # 模拟传播
        self.simulate_spread_on_networks(regular_net, random_net, scale_free_net)
        
        # 核心洞察
        insight = VGroup(
            Text("社交媒体 = 无标度网络", font_size=28, color=BRAND_PINK),
            Text("超级传播者决定一切", font_size=32, color=BRAND_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        insight.shift(DOWN * 2.2)
        
        self.play(Write(insight[0]))
        self.play(Write(insight[1]))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, networks, insight)))
    
    def create_regular_network(self):
        """创建规则网络"""
        network = VGroup()
        nodes = []
        
        # 3x3网格
        for i in range(3):
            for j in range(3):
                node = Circle(radius=0.12, fill_color=BRAND_BLUE, fill_opacity=0.7)
                node.move_to([i * 0.5 - 0.5, j * 0.5 - 0.5, 0])
                nodes.append(node)
                network.add(node)
        
        # 添加边（只连接相邻节点）
        for i in range(3):
            for j in range(3):
                idx = i * 3 + j
                # 右边
                if j < 2:
                    edge = Line(nodes[idx].get_center(), nodes[idx + 1].get_center(),
                              stroke_width=1, color=BRAND_GRAY)
                    network.add(edge)
                    edge.set_z_index(-1)
                # 下边
                if i < 2:
                    edge = Line(nodes[idx].get_center(), nodes[idx + 3].get_center(),
                              stroke_width=1, color=BRAND_GRAY)
                    network.add(edge)
                    edge.set_z_index(-1)
        
        return network
    
    def create_random_network(self):
        """创建随机网络"""
        network = VGroup()
        nodes = []
        
        # 9个随机分布的节点
        np.random.seed(42)
        positions = []
        for _ in range(9):
            angle = np.random.uniform(0, TAU)
            radius = np.random.uniform(0.2, 0.7)
            pos = [radius * np.cos(angle), radius * np.sin(angle), 0]
            positions.append(pos)
            
            node = Circle(radius=0.12, fill_color=BRAND_YELLOW, fill_opacity=0.7)
            node.move_to(pos)
            nodes.append(node)
            network.add(node)
        
        # 随机连接
        for i in range(9):
            for j in range(i + 1, 9):
                if np.random.random() < 0.3:  # 30%概率连接
                    edge = Line(nodes[i].get_center(), nodes[j].get_center(),
                              stroke_width=1, color=BRAND_GRAY)
                    network.add(edge)
                    edge.set_z_index(-1)
        
        return network
    
    def create_scale_free_network(self):
        """创建无标度网络（hub结构）"""
        network = VGroup()
        
        # 中心节点（超级传播者）
        hub = Circle(radius=0.2, fill_color=BRAND_RED, fill_opacity=0.9)
        hub.move_to(ORIGIN)
        network.add(hub)
        
        # 周围节点
        nodes = []
        for i in range(8):
            angle = i * TAU / 8
            radius = 0.7
            pos = [radius * np.cos(angle), radius * np.sin(angle), 0]
            
            node = Circle(radius=0.12, fill_color=BRAND_PINK, fill_opacity=0.7)
            node.move_to(pos)
            nodes.append(node)
            network.add(node)
            
            # 连接到中心
            edge = Line(hub.get_center(), node.get_center(),
                       stroke_width=2, color=BRAND_RED)
            network.add(edge)
            edge.set_z_index(-1)
        
        # 少量节点间连接
        for i in range(8):
            if np.random.random() < 0.2:  # 20%概率
                j = (i + 1) % 8
                edge = Line(nodes[i].get_center(), nodes[j].get_center(),
                          stroke_width=1, color=BRAND_GRAY)
                network.add(edge)
                edge.set_z_index(-1)
        
        return network
    
    def simulate_spread_on_networks(self, regular, random_net, scale_free):
        """模拟在不同网络上的传播"""
        # 为每个网络添加感染动画
        # 这里简化处理，只展示感染扩散的视觉效果
        
        # 规则网络：慢速逐个感染
        regular_infection = Circle(radius=0.12, fill_color=BRAND_RED, fill_opacity=0.8)
        regular_infection.move_to(regular[0].get_center())
        self.play(Create(regular_infection), run_time=0.2)
        self.play(regular_infection.animate.scale(3).set_opacity(0), run_time=0.5)
        
        # 随机网络：中速传播
        random_infection = Circle(radius=0.12, fill_color=BRAND_RED, fill_opacity=0.8)
        random_infection.move_to(random_net[4].get_center())
        self.play(Create(random_infection), run_time=0.2)
        self.play(random_infection.animate.scale(5).set_opacity(0), run_time=0.5)
        
        # 无标度网络：爆炸式传播
        scale_infection = Circle(radius=0.2, fill_color=BRAND_RED, fill_opacity=0.8)
        scale_infection.move_to(scale_free[0].get_center())
        self.play(Create(scale_infection), run_time=0.2)
        self.play(scale_infection.animate.scale(8).set_opacity(0), run_time=0.5)
    
    def debunking_strategies(self):
        """辟谣的数学策略"""
        title = Text("辟谣策略：数学给出答案", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 策略对比
        strategies = VGroup()
        
        # 策略1：降低β（减少接触率）
        strat1 = VGroup(
            Text("策略1：限制传播", font_size=26, color=BRAND_BLUE, weight=BOLD),
            MathTex(r"\beta \downarrow", font_size=32, color=BRAND_BLUE),
            Text("• 限流关键节点", font_size=20),
            Text("• 延迟转发功能", font_size=20),
            Text("效果：中等", font_size=22, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.2)
        strat1.shift(LEFT * 4 + DOWN * 0.5)
        
        # 策略2：增加γ（加快恢复）
        strat2 = VGroup(
            Text("策略2：快速辟谣", font_size=26, color=BRAND_GREEN, weight=BOLD),
            MathTex(r"\gamma \uparrow", font_size=32, color=BRAND_GREEN),
            Text("• 官方快速回应", font_size=20),
            Text("• 事实核查机制", font_size=20),
            Text("效果：良好", font_size=22, color=BRAND_GREEN)
        ).arrange(DOWN, buff=0.2)
        strat2.shift(DOWN * 0.5)
        
        # 策略3：预防接种
        strat3 = VGroup(
            Text("策略3：预防接种", font_size=26, color=BRAND_PINK, weight=BOLD),
            MathTex(r"S \rightarrow R", font_size=32, color=BRAND_PINK),
            Text("• 媒体素养教育", font_size=20),
            Text("• 预警机制", font_size=20),
            Text("效果：最佳", font_size=22, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.2)
        strat3.shift(RIGHT * 4 + DOWN * 0.5)
        
        strategies.add(strat1, strat2, strat3)
        
        for strat in strategies:
            self.play(FadeIn(strat, shift=UP * 0.2), run_time=0.6)
        
        # 数学结论
        conclusion = Text(
            "关键：让 R₀ < 1",
            font_size=36,
            color=BRAND_RED,
            weight=BOLD
        )
        conclusion.shift(DOWN * 2.5)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, strategies, conclusion)))
    
    def information_vaccine(self):
        """信息疫苗的设计"""
        # 标题
        title = Text("信息疫苗：主动免疫", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        
        # 疫苗原理
        vaccine_principle = VGroup(
            Text("预先接种弱化版信息", font_size=28, color=BRAND_GREEN),
            Text("建立批判性思维", font_size=28, color=BRAND_YELLOW),
            Text("形成群体免疫", font_size=32, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(vaccine_principle[0]))
        self.play(Write(vaccine_principle[1]))
        self.play(
            Write(vaccine_principle[2]),
            vaccine_principle[2].animate.scale(1.1)
        )
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, vaccine_principle)))
        
        # 结束语
        self.show_conclusion()
    
    def show_conclusion(self):
        """展示结论"""
        # 核心洞察
        conclusion = VGroup(
            Text("谣言传播的数学真相：", font_size=36),
            Text("不是信息本身", font_size=40, color=BRAND_YELLOW),
            Text("而是网络结构和情绪强度", font_size=44, color=BRAND_RED, weight=BOLD),
            Text("决定了传播速度", font_size=44, color=BRAND_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(conclusion[0]))
        self.play(Write(conclusion[1]))
        self.play(
            Write(conclusion[2]),
            Write(conclusion[3]),
            conclusion[2].animate.scale(1.05),
            conclusion[3].animate.scale(1.05)
        )
        self.wait(2)
        
        self.play(FadeOut(conclusion))
        
        # 实用建议
        advice = VGroup(
            Text("记住三个数字：", font_size=32, color=BRAND_PURPLE),
            Text("R₀ < 1 = 谣言消亡", font_size=28, color=BRAND_GREEN),
            Text("48小时 = 黄金辟谣期", font_size=28, color=BRAND_YELLOW),
            Text("6个节点 = 超级传播者", font_size=28, color=BRAND_RED)
        ).arrange(DOWN, buff=0.4)
        
        for line in advice:
            self.play(Write(line), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(advice))
        
        # 品牌结尾
        self.show_brand_ending()
    
    def show_brand_ending(self):
        """品牌结尾"""
        # 品牌标识
        brand_main = Text(
            "数学之美",
            font_size=64,
            color=BRAND_PINK,
            weight=BOLD
        )
        brand_sub = Text(
            "Math Magic",
            font_size=38,
            color=BRAND_BLUE,
            slant=ITALIC
        )
        brand = VGroup(brand_main, brand_sub).arrange(DOWN, buff=0.25)
        brand.set_stroke(width=3)
        
        # 本集信息
        episode_info = Text(
            "EP06: 谣言传播的SIR模型",
            font_size=28,
            color=WHITE
        )
        episode_info.next_to(brand, DOWN, buff=0.6)
        
        # 关注引导
        cta = Text(
            "用真实的数学，理解真实的世界",
            font_size=32,
            color=BRAND_YELLOW
        )
        cta.next_to(episode_info, DOWN, buff=0.4)
        
        # 装饰粒子
        particles = VGroup()
        for i in range(20):
            particle = Dot(
                radius=0.05,
                color=random.choice([BRAND_PINK, BRAND_BLUE, BRAND_YELLOW, BRAND_GREEN]),
                fill_opacity=random.uniform(0.5, 1)
            )
            angle = (i / 20) * TAU
            radius = random.uniform(2.2, 3.5)
            particle.move_to([
                radius * np.cos(angle),
                radius * np.sin(angle),
                0
            ])
            particles.add(particle)
        
        # 动画
        self.play(
            Write(brand, run_time=1),
            FadeIn(particles, lag_ratio=0.1),
            run_time=1.5
        )
        self.play(
            Write(episode_info),
            Write(cta),
            Rotate(particles, angle=PI/6, about_point=ORIGIN),
            run_time=1.5
        )
        
        self.wait(3)

# 测试命令（1080p预览）：
# manim -pql -r 1920,1080 math_magic_ep06.py RumorSIRModelEP06

# 生产命令（1080p 60fps）：
# manim -pqh -r 1920,1080 --fps 60 math_magic_ep06.py RumorSIRModelEP06