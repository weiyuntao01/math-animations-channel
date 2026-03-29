"""
数学之美系列 EP05 - 友谊悖论：为什么你的朋友总比你受欢迎？
7分钟深度科普
左图右字布局优化版 - 无重叠
1. 技术规范清单 ✅ ```python # MathTex绝对不能有中文 MathTex(r"P(\text{match})") # ✅ 正确 MathTex(r"P(\text{匹配})") # ❌ 错误 # 使用半角标点符号 Text("\"这是引号\"") # ✅ 正确 Text(""这是引号"") # ❌ 错误 # API准确使用 AnnularSector(...) # ✅ 正确 Sector(inner_radius=...) # ❌ 参数错误 # 左图右文标准布局 visual.shift(LEFT  3.5) text.shift(RIGHT  3.5) ``` 
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
BRAND_GRAY = "#6B7280"

class FriendshipParadoxEP05(Scene):
    """EP05: 友谊悖论的数学证明
    
    1080p优化版本：
    - 左图右字布局
    - 无元素重叠
    - 字体大小适配
    - 清晰的视觉层次
    """
    
    def construct(self):
        # 设置中文字体和背景
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#0A0E27"
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场：现象展示（30秒）
        self.show_opening()
        
        # 2. 友谊悖论的发现（60秒）
        self.introduce_paradox()
        
        # 3. 数学证明过程（180秒）
        self.prove_paradox()
        
        # 4. 幂律分布的影响（90秒）
        self.power_law_effect()
        
        # 5. 其他领域的类似悖论（60秒）
        self.other_paradoxes()
        
        # 6. 心理影响与应对（30秒）
        self.conclusion()
    
    def show_opening(self):
        """开场：你的朋友真的比你受欢迎"""
        # 痛点文字 - 居中显示
        hook = VGroup(
            Text("打开朋友圈", font_size=44, color=WHITE),
            Text("为什么总觉得", font_size=52, color=BRAND_YELLOW, weight=BOLD),
            Text("别人的生活更精彩？", font_size=60, color=BRAND_PINK)
        ).arrange(DOWN, buff=0.5)
        
        hook[1].set_stroke(color=BRAND_YELLOW, width=2)
        hook[2].set_stroke(color=BRAND_PINK, width=3)
        
        self.play(Write(hook[0], run_time=0.8))
        self.play(Write(hook[1], run_time=0.8))
        self.play(
            Write(hook[2], run_time=1),
            hook[2].animate.scale(1.05)
        )
        self.wait(1)
        
        # 转场到数学真相
        truth = Text(
            "这不是错觉，是数学！",
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
    
    def introduce_paradox(self):
        """友谊悖论的发现"""
        # 标题 - 固定在顶部
        title = Text("友谊悖论", font_size=40, color=BRAND_PURPLE, weight=BOLD)
        subtitle = Text("Friendship Paradox", font_size=24, color=BRAND_PURPLE, slant=ITALIC)
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.15)
        header.to_edge(UP, buff=0.3)
        
        self.play(Write(header))
        
        # 历史背景 - 中央区域
        history = VGroup(
            Text("1991年 社会学家Scott Feld发现：", font_size=26),
            Text("\"你的朋友平均拥有的朋友数", font_size=30, color=BRAND_YELLOW),
            Text("大于你拥有的朋友数\"", font_size=30, color=BRAND_YELLOW),
            Text("这对大多数人都成立！", font_size=32, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.25)
        history.move_to(ORIGIN)
        
        for line in history:
            self.play(Write(line), run_time=0.6)
        
        self.wait(1.5)
        
        # 简单示例网络
        self.play(FadeOut(history))
        
        example_text = Text("让我们看一个简单的例子", font_size=28)
        example_text.next_to(header, DOWN, buff=0.4)
        self.play(Write(example_text))
        
        # 创建网络 - 左侧
        network = self.create_simple_network()
        network.shift(LEFT * 3)
        
        # 统计信息 - 右侧
        stats = VGroup(
            Text("节点统计", font_size=28, color=BRAND_YELLOW, weight=BOLD),
            Text("A: 4个朋友", font_size=24),
            Text("B: 2个朋友", font_size=24),
            Text("C: 2个朋友", font_size=24),
            Text("D: 1个朋友", font_size=24),
            Text("E: 1个朋友", font_size=24),
            Text("─────────", font_size=24),
            Text("平均: 2.0", font_size=26, color=WHITE),
            Text("朋友的平均: 2.5", font_size=26, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        stats.shift(RIGHT * 3.5)
        
        self.play(Create(network))
        self.play(FadeIn(stats, shift=LEFT * 0.2))
        
        self.wait(2)
        self.play(
            FadeOut(network),
            FadeOut(stats),
            FadeOut(example_text),
            FadeOut(header)
        )
    
    def create_simple_network(self):
        """创建一个简单的社交网络示例"""
        network = VGroup()
        
        # 节点位置 - 缩小间距
        positions = [
            [0, 1.2, 0],      # A (中心)
            [-1.5, 0, 0],     # B
            [1.5, 0, 0],      # C
            [-0.8, -1.2, 0],  # D
            [0.8, -1.2, 0],   # E
        ]
        
        # 创建节点
        nodes = []
        labels = ["A", "B", "C", "D", "E"]
        colors = [BRAND_YELLOW, BRAND_BLUE, BRAND_BLUE, BRAND_GRAY, BRAND_GRAY]
        
        for i, (pos, label, color) in enumerate(zip(positions, labels, colors)):
            node = VGroup(
                Circle(radius=0.35, fill_color=color, fill_opacity=0.7, stroke_width=2),
                Text(label, font_size=22, color=WHITE)
            )
            node.move_to(pos)
            nodes.append(node)
            network.add(node)
        
        # 创建边
        edges = [
            (0, 1), (0, 2), (0, 3), (0, 4),  # A的连接
            (1, 3),  # B-D
            (2, 4),  # C-E
        ]
        
        for i, j in edges:
            edge = Line(
                nodes[i].get_center(),
                nodes[j].get_center(),
                stroke_width=2,
                color=WHITE
            )
            network.add(edge)
            edge.set_z_index(-1)
        
        return network
    
    def prove_paradox(self):
        """数学证明过程 - 核心部分"""
        # 证明标题
        proof_title = Text("严格的数学证明", font_size=36, color=BRAND_GREEN, weight=BOLD)
        proof_title.to_edge(UP, buff=0.25)
        self.play(Write(proof_title))
        
        # Step 1: 定义符号
        step1 = Text("Step 1: 定义符号", font_size=28, color=BRAND_YELLOW)
        step1.shift(UP * 1.8)
        
        # 左侧：数学符号
        math_defs = VGroup(
            MathTex(r"G = (V, E)", font_size=32),
            MathTex(r"d_i", font_size=32),
            MathTex(r"N = |V|", font_size=32),
            MathTex(r"M = |E|", font_size=32)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        math_defs.shift(LEFT * 4)
        
        # 右侧：中文解释
        text_defs = VGroup(
            Text("图 = (节点集, 边集)", font_size=26),
            Text("节点i的度数（朋友数）", font_size=26),
            Text("节点总数", font_size=26),
            Text("边总数", font_size=26)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        text_defs.shift(RIGHT * 2)
        
        self.play(Write(step1))
        self.play(
            Write(math_defs),
            Write(text_defs),
            run_time=2
        )
        
        self.wait(2)
        self.play(FadeOut(VGroup(step1, math_defs, text_defs)))
        
        # Step 2: 计算平均度数
        step2 = Text("Step 2: 平均朋友数", font_size=28, color=BRAND_YELLOW)
        step2.shift(UP * 1.8)
        
        # 左侧：公式
        avg_formula = VGroup(
            MathTex(r"\bar{d} = \frac{1}{N}\sum_{i=1}^{N} d_i", font_size=36),
            MathTex(r"= \frac{2M}{N}", font_size=36)
        ).arrange(DOWN, buff=0.4)
        avg_formula.shift(LEFT * 3.5)
        
        # 右侧：解释
        avg_explain = VGroup(
            Text("平均度数定义", font_size=26),
            Text("每条边贡献2个度", font_size=26, color=BRAND_GRAY)
        ).arrange(DOWN, buff=0.4)
        avg_explain.shift(RIGHT * 3)
        
        self.play(Write(step2))
        self.play(
            Write(avg_formula[0]),
            Write(avg_explain[0])
        )
        self.play(
            Write(avg_formula[1]),
            Write(avg_explain[1])
        )
        
        self.wait(2)
        self.play(FadeOut(VGroup(step2, avg_formula, avg_explain)))
        
        # Step 3: 朋友的平均度数
        step3 = Text("Step 3: 朋友的平均朋友数", font_size=28, color=BRAND_YELLOW)
        step3.shift(UP * 1.8)
        
        # 关键洞察 - 居中显示
        key_insight = Text(
            "关键：度数高的人被计算了更多次！",
            font_size=32,
            color=BRAND_PINK,
            weight=BOLD
        )
        key_insight.move_to(ORIGIN + UP * 0.8)
        
        self.play(Write(step3))
        self.play(Write(key_insight))
        
        # 公式推导
        friend_formula = VGroup(
            MathTex(r"\frac{\sum_{(i,j) \in E} (d_i + d_j)}{2M}", font_size=32),
            MathTex(r"= \frac{1}{2M}\sum_{i=1}^{N} d_i^2", font_size=32),
            MathTex(r"= \frac{\overline{d^2}}{\bar{d}}", font_size=36, color=BRAND_GREEN)
        ).arrange(DOWN, buff=0.3)
        friend_formula.shift(DOWN * 1.2)
        
        for eq in friend_formula:
            self.play(Write(eq), run_time=0.8)
        
        self.wait(2)
        self.play(FadeOut(VGroup(step3, key_insight, friend_formula)))
        
        # Step 4: 证明不等式
        step4 = Text("Step 4: 证明悖论", font_size=28, color=BRAND_YELLOW)
        step4.shift(UP * 1.8)
        
        # 左侧：数学推导
        math_proof = VGroup(
            MathTex(r"\text{Var}(d) = \overline{d^2} - \bar{d}^2", font_size=32),
            MathTex(r"\text{Var}(d) \geq 0", font_size=32),
            MathTex(r"\Rightarrow \overline{d^2} \geq \bar{d}^2", font_size=32),
            MathTex(r"\Rightarrow \frac{\overline{d^2}}{\bar{d}} \geq \bar{d}", font_size=36, color=BRAND_GREEN)
        ).arrange(DOWN, buff=0.3)
        math_proof.shift(LEFT * 3)
        
        # 右侧：文字结论
        conclusion = VGroup(
            Text("由方差公式", font_size=26),
            Text("方差非负", font_size=26),
            Text("移项得", font_size=26),
            Text("朋友的平均 ≥ 平均", font_size=28, color=BRAND_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.35)
        conclusion.shift(RIGHT * 3)
        
        self.play(Write(step4))
        for i in range(4):
            self.play(
                Write(math_proof[i]),
                Write(conclusion[i]),
                run_time=0.8
            )
        
        # 等号成立条件
        equality = Text(
            "等号成立当且仅当所有人朋友数相同",
            font_size=26,
            color=BRAND_BLUE
        )
        equality.shift(DOWN * 2.5)
        self.play(Write(equality))
        
        self.wait(3)
        self.play(FadeOut(VGroup(proof_title, step4, math_proof, conclusion, equality)))
    
    def power_law_effect(self):
        """幂律分布的影响"""
        # 标题
        title = Text("现实中：幂律分布放大了悖论", font_size=36, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.25)
        self.play(Write(title))
        
        # 左图：正态分布
        left_group = VGroup()
        
        left_title = Text("理想世界", font_size=26, color=BRAND_GRAY)
        left_title.shift(LEFT * 4.5 + UP * 1.8)
        
        left_axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 0.05, 0.01],
            x_length=3.5,
            y_length=2.5,
            axis_config={"include_numbers": False}
        ).shift(LEFT * 4.5 + DOWN * 0.3)
        
        normal_curve = left_axes.plot(
            lambda x: 0.04 * np.exp(-((x-50)**2)/(2*15**2)),
            color=BRAND_GRAY,
            stroke_width=3
        )
        
        left_group.add(left_title, left_axes, normal_curve)
        
        # 右图：幂律分布
        right_group = VGroup()
        
        right_title = Text("现实世界", font_size=26, color=BRAND_PINK)
        right_title.shift(LEFT * 0.5 + UP * 1.8)
        
        right_axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 0.2, 0.04],
            x_length=3.5,
            y_length=2.5,
            axis_config={"include_numbers": False}
        ).shift(LEFT * 0.5 + DOWN * 0.3)
        
        power_curve = right_axes.plot(
            lambda x: 5/(x+5)**1.5 if x > 0 else 0,
            color=BRAND_PINK,
            stroke_width=3
        )
        
        right_group.add(right_title, right_axes, power_curve)
        
        # 右侧文字说明
        stats_comparison = VGroup(
            Text("正态分布", font_size=26, color=BRAND_GRAY, weight=BOLD),
            Text("平均: 50", font_size=22),
            Text("朋友平均: 52", font_size=22),
            Text("差异: 4%", font_size=24, color=BRAND_GREEN),
            Text("─────────", font_size=22),
            Text("幂律分布", font_size=26, color=BRAND_PINK, weight=BOLD),
            Text("平均: 20", font_size=22),
            Text("朋友平均: 85", font_size=22),
            Text("差异: 325%!", font_size=24, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        stats_comparison.shift(RIGHT * 3.5)
        
        # 动画展示
        self.play(
            Create(left_group),
            Create(right_group)
        )
        self.play(FadeIn(stats_comparison, shift=LEFT * 0.2))
        
        # 底部解释
        explanation = Text(
            "少数超级节点极大扭曲了平均值",
            font_size=28,
            color=BRAND_YELLOW
        )
        explanation.shift(DOWN * 2.7)
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(
            FadeOut(VGroup(
                title, left_group, right_group,
                stats_comparison, explanation
            ))
        )
    
    def other_paradoxes(self):
        """其他领域的类似悖论"""
        title = Text("同样的数学，不同的故事", font_size=36, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.25)
        self.play(Write(title))
        
        # 2x2网格布局
        examples = VGroup()
        
        # 左上
        ex1 = VGroup(
            Text("📚 学术引用", font_size=28, color=BRAND_BLUE, weight=BOLD),
            Text("你引用的论文", font_size=22),
            Text("被引次数 > 你的", font_size=22, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.15)
        ex1.shift(LEFT * 3.5 + UP * 0.8)
        
        # 右上
        ex2 = VGroup(
            Text("💑 亲密关系", font_size=28, color=BRAND_PINK, weight=BOLD),
            Text("你的前任们", font_size=22),
            Text("交往人数 > 你的", font_size=22, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.15)
        ex2.shift(RIGHT * 3.5 + UP * 0.8)
        
        # 左下
        ex3 = VGroup(
            Text("📊 班级规模", font_size=28, color=BRAND_GREEN, weight=BOLD),
            Text("学生体验的", font_size=22),
            Text("班级 > 实际", font_size=22, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.15)
        ex3.shift(LEFT * 3.5 + DOWN * 0.8)
        
        # 右下
        ex4 = VGroup(
            Text("✈️ 航班延误", font_size=28, color=BRAND_PURPLE, weight=BOLD),
            Text("乘客经历的", font_size=22),
            Text("延误 > 平均", font_size=22, color=BRAND_YELLOW)
        ).arrange(DOWN, buff=0.15)
        ex4.shift(RIGHT * 3.5 + DOWN * 0.8)
        
        examples.add(ex1, ex2, ex3, ex4)
        
        # 逐个展示
        for ex in examples:
            self.play(FadeIn(ex, shift=UP * 0.2), run_time=0.5)
        
        # 核心原理
        principle = Text(
            "采样偏差：高连接度节点被过度采样",
            font_size=28,
            color=BRAND_GREEN,
            weight=BOLD
        )
        principle.shift(DOWN * 2.5)
        self.play(Write(principle))
        
        self.wait(2)
        self.play(FadeOut(VGroup(title, examples, principle)))
    
    def conclusion(self):
        """心理影响与应对"""
        # 心理影响
        title = Text("回到开头的问题", font_size=36, color=BRAND_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.25)
        self.play(Write(title))
        
        # 左侧：问题分析
        impacts = VGroup(
            Text("社交媒体焦虑来源", font_size=28, color=BRAND_YELLOW, weight=BOLD),
            Text("1. 友谊悖论", font_size=24),
            Text("   别人确实更受欢迎", font_size=22, color=BRAND_GRAY),
            Text("2. 展示偏差", font_size=24),
            Text("   只展示精彩瞬间", font_size=22, color=BRAND_GRAY),
            Text("3. 算法推荐", font_size=24),
            Text("   优先高互动内容", font_size=22, color=BRAND_GRAY)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        impacts.shift(LEFT * 3)
        
        # 右侧：理性认知
        solution = VGroup(
            Text("理性认知", font_size=28, color=BRAND_GREEN, weight=BOLD),
            Text("这是数学规律", font_size=24),
            Text("不是你的问题", font_size=24),
            Text("─────────", font_size=22),
            Text("你看到的平均", font_size=24),
            Text("从来都不是", font_size=24),
            Text("真正的平均", font_size=26, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        solution.shift(RIGHT * 3)
        
        self.play(
            FadeIn(impacts, shift=RIGHT * 0.2),
            FadeIn(solution, shift=LEFT * 0.2)
        )
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, impacts, solution)))
        
        # 结束语
        ending = VGroup(
            Text("友谊悖论告诉我们：", font_size=32),
            Text("你看到的平均", font_size=40, color=BRAND_YELLOW),
            Text("从来都不是真正的平均", font_size=44, color=BRAND_PINK, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(ending[0]))
        self.play(Write(ending[1]))
        self.play(
            Write(ending[2]),
            ending[2].animate.scale(1.05)
        )
        self.wait(2)
        
        self.play(FadeOut(ending))
        
        # 品牌结尾
        self.show_brand_ending()
    
    def show_brand_ending(self):
        """品牌结尾 - 保持系列一致性"""
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
            "EP05: 友谊悖论",
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
# manim -pql -r 1920,1080 math_magic_ep05.py FriendshipParadoxEP05

# 生产命令（1080p 60fps）：
# manim -pqh -r 1920,1080 --fps 60 math_magic_ep05.py FriendshipParadoxEP05