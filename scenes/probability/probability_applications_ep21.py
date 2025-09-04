"""
EP21: 概率思维的终极应用
系列大总结 - 从理论到实践的完整框架
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple
from scipy import stats

# 概率系列颜色主题
PROB_PURPLE = "#8B5CF6"    # 主色：概率紫
PROB_GREEN = "#10B981"     # 成功绿
PROB_RED = "#EF4444"       # 失败红
PROB_BLUE = "#3B82F6"      # 数据蓝
PROB_YELLOW = "#F59E0B"    # 警告黄
PROB_GRAY = "#6B7280"      # 中性灰

# 字体大小调整
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class ProbabilityUltimateEP21(Scene):
    """概率思维的终极应用 - 概率论系列 EP21（系列完结）"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 史诗级开场 - 回顾20集旅程
        self.epic_series_opening()
        
        # 2. 知识体系总览 - 完整框架图
        self.complete_knowledge_framework()
        
        # 3-12. 十大终极应用（融合所有核心概念）
        self.application_1_financial_kelly_martingale()     # 金融：凯利公式+鞅论
        self.application_2_medical_bayes_poisson()          # 医疗：贝叶斯+泊松
        self.application_3_insurance_expectation_clt()      # 保险：期望值+CLT
        self.application_4_career_optimal_stopping()        # 职业：最优停止理论
        self.application_5_social_birthday_network()        # 社交：生日悖论+网络
        self.application_6_game_theory_paradoxes()         # 博弈：囚徒困境+悖论
        self.application_7_learning_markov_spaced()        # 学习：马尔可夫+间隔
        self.application_8_sports_gambler_statistics()     # 体育：赌徒谬误+统计
        self.application_9_startup_random_walk_survival()  # 创业：随机漫步+生存
        self.application_10_life_philosophy_all()          # 人生：所有概念的融合
        
        # 13. 数学之美 - 公式总览
        self.mathematical_beauty_showcase()
        
        # 14. 终极总结 - 概率思维的本质
        self.ultimate_philosophical_summary()
        
        # 15. 完整的哲学体系
        self.series_philosophy_complete()
        
        # 16. 系列告别
        self.series_grand_finale()
    
    def epic_series_opening(self):
        """史诗级开场 - 完整回顾"""
        # 主标题组
        title_group = VGroup(
            Text(
                "【系列终章】",
                font_size=28,
                color=PROB_YELLOW,
                weight=BOLD
            ),
            Text(
                "概率论的反直觉世界",
                font_size=48,
                color=PROB_PURPLE,
                weight=BOLD
            ),
            Text(
                "第21集：概率思维的终极应用",
                font_size=30,
                color=WHITE
            )
        ).arrange(DOWN, buff=0.4)
        
        # 数据统计组
        stats_group = VGroup(
            Text("20集精华", font_size=24, color=PROB_BLUE),
            Text("15个悖论", font_size=24, color=PROB_RED),
            Text("10大定律", font_size=24, color=PROB_GREEN),
            Text("∞种应用", font_size=24, color=PROB_YELLOW)
        ).arrange(RIGHT, buff=1.0)
        
        # 整体布局
        opening_content = VGroup(title_group, stats_group).arrange(DOWN, buff=1.2)
        opening_content.move_to(ORIGIN)
        
        # 依次显示
        for element in title_group:
            self.play(Write(element), run_time=1.5)
        
        self.wait(1)
        
        for stat in stats_group:
            self.play(FadeIn(stat, shift=UP), run_time=0.6)
        
        self.wait(4)
        self.play(FadeOut(opening_content))
    
    def complete_knowledge_framework(self):
        """完整知识框架图"""
        self.clear()
        
        title = Text("概率论知识宇宙", font_size=TITLE_SIZE, color=PROB_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        
        # 创建完整的知识网络
        network = self.create_knowledge_network()
        network.scale(0.75)
        network.next_to(title, DOWN, buff=0.8)
        
        # 整体内容组
        framework_content = VGroup(title, network)
        
        self.play(Write(title), run_time=2)
        self.play(Create(network), run_time=3)
        
        # 核心连接动画
        self.animate_knowledge_connections(network)
        
        self.wait(4)
        self.play(FadeOut(framework_content))
    
    def create_knowledge_network(self):
        """创建知识网络图"""
        network = VGroup()
        
        # 中心核心
        core = Circle(radius=0.8, color=PROB_PURPLE, fill_opacity=0.3)
        core_text = Text("概率\n思维", font_size=20, color=WHITE)
        core_text.move_to(core.get_center())
        
        # 四大支柱
        pillars = []
        pillar_data = [
            ("经典悖论", PROB_RED, UP * 2.5, 
             ["蒙提霍尔", "生日悖论", "辛普森", "伯特兰"]),
            ("概率定律", PROB_BLUE, RIGHT * 2.5,
             ["大数定律", "中心极限", "贝叶斯", "马尔可夫"]),
            ("分布模型", PROB_GREEN, DOWN * 2.5,
             ["正态", "泊松", "指数", "二项"]),
            ("决策理论", PROB_YELLOW, LEFT * 2.5,
             ["期望值", "效用", "博弈", "最优停止"])
        ]
        
        for name, color, pos, concepts in pillar_data:
            # 支柱节点
            pillar = Circle(radius=0.6, color=color, fill_opacity=0.3)
            pillar_text = Text(name, font_size=16, color=color, weight=BOLD)
            pillar_text.move_to(pillar.get_center())
            pillar_group = VGroup(pillar, pillar_text)
            pillar_group.move_to(pos)
            
            # 连接线
            connection = Line(ORIGIN, pos, color=color, stroke_opacity=0.5)
            
            # 子概念（文字沿径向向外偏移，避免与圆点重叠）
            for i, concept in enumerate(concepts):
                angle = TAU * i / len(concepts)
                concept_pos = pos + 0.8 * np.array([np.cos(angle), np.sin(angle), 0])
                concept_dot = Dot(concept_pos, radius=0.05, color=color)
                concept_text = Text(concept, font_size=10, color=WHITE)
                offset = 0.22 * np.array([np.cos(angle), np.sin(angle), 0])
                concept_text.move_to(concept_pos + offset)
                network.add(concept_dot, concept_text)
            
            pillars.append(pillar_group)
            network.add(connection, pillar_group)
        
        network.add(core, core_text)
        return network
    
    def animate_knowledge_connections(self, network):
        """动画展示知识连接"""
        # 创建脉冲效果
        pulse = Circle(radius=0.8, color=PROB_PURPLE, stroke_opacity=0)
        self.play(
            pulse.animate.scale(4).set_stroke(opacity=0.5),
            run_time=1.5
        )
        self.play(FadeOut(pulse))
    
    def application_1_financial_kelly_martingale(self):
        """应用1：金融投资 - 凯利公式与鞅论"""
        self.clear()
        header = self.show_application_header(1, "金融投资：数学化决策")
        
        # 左列：投资策略可视化（适配左半屏）
        strategy_viz = self.create_investment_strategy_viz()
        
        # 右列：概念要点（更大字号）
        right_text = VGroup(
            VGroup(
                Text("凯利公式", font_size=28, color=PROB_BLUE, weight=BOLD),
                MathTex(r"f^* = \frac{p(b+1)-1}{b}")
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("鞅理论", font_size=28, color=PROB_GREEN, weight=BOLD),
                MathTex(r"E[X_{t+1}|X_t] = X_t")
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("大数定律", font_size=28, color=PROB_YELLOW, weight=BOLD),
                MathTex(r"\bar{X}_n \xrightarrow{P} \mu")
            ).arrange(DOWN, buff=0.2),
            Text("要义：正期望 + 控制仓位 + 长期主义", font_size=22, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # 横向排列为一组，整体置于标题下，确保充分利用屏幕空间
        content = VGroup(strategy_viz, right_text).arrange(RIGHT, buff=1.5, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.9)  # 适当缩放以适应屏幕
        
        self.play(Create(strategy_viz), Write(right_text))
        
        self.wait(4.5)
        self.clear()
    
    def create_investment_strategy_viz(self):
        """创建投资策略可视化"""
        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 10, 2],
            x_length=2.8,  # 进一步缩小图表
            y_length=2.0,  # 进一步缩小图表
            axis_config={"include_numbers": True, "font_size": 10}
        )
        
        # 三种策略曲线
        t = np.linspace(0, 100, 100)
        
        # 凯利策略（稳健增长）
        kelly_curve = axes.plot(
            lambda x: np.exp(0.03 * x),
            color=PROB_GREEN,
            stroke_width=3
        )
        
        # 保守策略（线性增长）
        conservative_curve = axes.plot(
            lambda x: 1 + 0.02 * x,
            color=PROB_BLUE,
            stroke_width=2
        )
        
        # 激进策略（高风险）
        aggressive_curve = axes.plot(
            lambda x: np.exp(0.05 * x) * (0.2 if x > 60 else 1),
            color=PROB_RED,
            stroke_width=2
        )
        
        # 标签
        labels = VGroup(
            Text("凯利最优", font_size=14, color=PROB_GREEN).next_to(kelly_curve, UR),
            Text("保守", font_size=14, color=PROB_BLUE).next_to(conservative_curve, RIGHT),
            Text("激进", font_size=14, color=PROB_RED).next_to(aggressive_curve, RIGHT)
        )
        
        return VGroup(axes, kelly_curve, conservative_curve, aggressive_curve, labels)
    
    def application_2_medical_bayes_poisson(self):
        """应用2：医疗诊断 - 贝叶斯推断与泊松过程"""
        self.clear()
        header = self.show_application_header(2, "医疗诊断：生命的概率")
        
        # 左列：贝叶斯网络
        bayes_network = self.create_medical_bayes_network()
        
        # 右列：泊松与案例
        poisson_model = VGroup(
            Text("流行病模型", font_size=26, color=PROB_RED),
            MathTex(r"P(k) = \frac{\lambda^k e^{-\lambda}}{k!}"),
            Text("λ = 感染率", font_size=20, color=GRAY)
        ).arrange(DOWN, buff=0.25)
        
        case_data = VGroup(
            Text("COVID-19检测", font_size=22, color=PROB_YELLOW),
            Text("灵敏度: 98%", font_size=20),
            Text("特异度: 99.5%", font_size=20),
            Text("患病率: 1%", font_size=20),
            Text("阳性预测值: 66.9%", font_size=22, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.15)
        
        right_col = VGroup(poisson_model, case_data).arrange(DOWN, buff=0.5)
        content = VGroup(bayes_network, right_col).arrange(RIGHT, buff=1.8, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.85)  # 适当缩放以适应屏幕
        
        self.play(Create(bayes_network), Write(right_col))
        
        self.wait(4.5)
        self.clear()
    
    def create_medical_bayes_network(self):
        """创建医疗贝叶斯网络"""
        network = VGroup()
        
        # 节点
        disease = Circle(radius=0.4, color=PROB_RED, fill_opacity=0.3)
        disease_text = Text("疾病", font_size=16)
        disease_group = VGroup(disease, disease_text)
        disease_group.shift(UP * 1.5)
        
        test = Circle(radius=0.4, color=PROB_BLUE, fill_opacity=0.3)
        test_text = Text("检测", font_size=16)
        test_group = VGroup(test, test_text)
        test_group.shift(LEFT * 1)
        
        symptom = Circle(radius=0.4, color=PROB_GREEN, fill_opacity=0.3)
        symptom_text = Text("症状", font_size=16)
        symptom_group = VGroup(symptom, symptom_text)
        symptom_group.shift(RIGHT * 1)
        
        # 连接
        edges = VGroup(
            Arrow(disease_group.get_bottom(), test_group.get_top(), buff=0.1),
            Arrow(disease_group.get_bottom(), symptom_group.get_top(), buff=0.1)
        )
        
        network.add(disease_group, test_group, symptom_group, edges)
        return network
    
    def application_3_insurance_expectation_clt(self):
        """应用3：保险精算 - 期望值与中心极限定理"""
        self.clear()
        header = self.show_application_header(3, "保险精算：大数法则的胜利")
        
        # 左列：CLT可视化
        clt_viz = self.create_clt_visualization()
        
        # 右列：定价与示例
        expectation_calc = VGroup(
            Text("保险定价模型", font_size=26, color=PROB_BLUE),
            MathTex(r"P = E[L] + \sigma\sqrt{n} + M"),
            Text("n → ∞ 时风险趋零", font_size=20, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.25)
        
        insurance_data = VGroup(
            Text("车险实例", font_size=22, color=PROB_YELLOW),
            Text("平均赔付: $5,000", font_size=20),
            Text("事故概率: 5%", font_size=20),
            Text("期望损失: $250", font_size=20),
            Text("保费定价: $400", font_size=22, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.15)
        
        right_col = VGroup(expectation_calc, insurance_data).arrange(DOWN, buff=0.5)
        content = VGroup(clt_viz, right_col).arrange(RIGHT, buff=1.6, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.9)  # 适当缩放以适应屏幕
        
        self.play(Create(clt_viz), Write(right_col))
        
        self.wait(4.5)
        self.clear()
    
    def create_clt_visualization(self):
        """创建中心极限定理可视化"""
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 0.5, 0.1],
            x_length=4.5,
            y_length=3,
            axis_config={"include_numbers": True, "font_size": 12}
        )
        
        # 正态曲线
        x = np.linspace(-3, 3, 100)
        y = stats.norm.pdf(x, 0, 1)
        
        normal_curve = axes.plot_line_graph(
            x_values=x,
            y_values=y,
            line_color=PROB_PURPLE,
            stroke_width=3,
            add_vertex_dots=False
        )
        
        # 标签
        label = Text("N(0,1)", font_size=16, color=PROB_PURPLE)
        label.next_to(normal_curve, UR)
        
        return VGroup(axes, normal_curve, label)
    
    def application_4_career_optimal_stopping(self):
        """应用4：职业选择 - 最优停止理论"""
        self.clear()
        header = self.show_application_header(4, "职业选择：37%法则")
        
        # 左列：秘书问题可视化
        secretary_viz = self.create_secretary_problem_viz()
        
        # 右列：数学推导
        math_derivation = VGroup(
            Text("最优停止策略", font_size=26, color=PROB_BLUE),
            MathTex(r"k^* = \frac{n}{e} \approx 0.37n"),
            MathTex(r"P(success) = \frac{1}{e} \approx 0.37"),
            Text("策略：先观察约37%，再选后续第一个更优者", font_size=20, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.3)
        content = VGroup(secretary_viz, math_derivation).arrange(RIGHT, buff=1.8, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.85)  # 适当缩放以适应屏幕
        
        self.play(Create(secretary_viz), Write(math_derivation))
        
        self.wait(4.5)
        self.clear()
    
    def create_secretary_problem_viz(self):
        """创建秘书问题可视化"""
        viz = VGroup()
        
        # 候选人序列
        candidates = VGroup()
        for i in range(8):
            quality = random.uniform(0.3, 1.0)
            bar = Rectangle(
                width=0.5,
                height=quality * 2,
                fill_color=PROB_BLUE if i < 4 else PROB_GRAY,
                fill_opacity=0.7
            )
            bar.shift(RIGHT * (i - 3.5) * 0.6 + UP * quality)
            candidates.add(bar)
        
        # 分界线
        divider = DashedLine(
            UP * 2.5 + RIGHT * (-1.05),
            DOWN * 0.5 + RIGHT * (-1.05),
            color=PROB_YELLOW,
            stroke_width=2
        )
        
        # 标签
        explore_label = Text("探索期", font_size=16, color=PROB_BLUE)
        explore_label.shift(LEFT * 3 + DOWN * 1)
        
        decide_label = Text("决策期", font_size=16, color=PROB_GRAY)
        decide_label.shift(RIGHT * 1 + DOWN * 1)
        
        viz.add(candidates, divider, explore_label, decide_label)
        return viz
    
    def application_5_social_birthday_network(self):
        """应用5：社交网络 - 生日悖论与小世界"""
        self.clear()
        header = self.show_application_header(5, "社交网络：概率的连接")
        
        # 左列：小世界网络
        network_viz = self.create_social_network()
        
        # 右列：生日悖论
        birthday_calc = VGroup(
            Text("生日悖论", font_size=26, color=PROB_YELLOW),
            MathTex(r"P(m) = 1 - \frac{365!}{365^n(365-n)!}"),
            Text("23人 → 50.7%", font_size=20, color=PROB_GREEN),
            Text("50人 → 97.0%", font_size=20, color=PROB_RED)
        ).arrange(DOWN, buff=0.25)
        content = VGroup(network_viz, birthday_calc).arrange(RIGHT, buff=2.0, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.9)  # 适当缩放以适应屏幕
        
        self.play(Create(network_viz), Write(birthday_calc))
        
        self.wait(4.5)
        self.clear()
    
    def create_social_network(self):
        """创建社交网络图"""
        network = VGroup()
        
        # 创建节点
        nodes = []
        for i in range(12):
            angle = TAU * i / 12
            pos = 1.6 * np.array([np.cos(angle), np.sin(angle), 0])
            node = Dot(pos, radius=0.1, color=PROB_BLUE)
            nodes.append(node)
            network.add(node)
        
        # 创建连接
        for i in range(12):
            for j in range(i+1, min(i+3, 12)):
                edge = Line(
                    nodes[i].get_center(),
                    nodes[j % 12].get_center(),
                    stroke_width=1,
                    stroke_opacity=0.3
                )
                network.add(edge)
        
        # 中心节点
        center = Dot(ORIGIN, radius=0.15, color=PROB_YELLOW)
        network.add(center)
        
        # 中心连接
        for node in nodes[::3]:
            edge = Line(
                center.get_center(),
                node.get_center(),
                stroke_width=2,
                stroke_opacity=0.5,
                color=PROB_YELLOW
            )
            network.add(edge)
        
        return network
    
    def application_6_game_theory_paradoxes(self):
        """应用6：博弈论 - 囚徒困境与合作演化"""
        self.clear()
        header = self.show_application_header(6, "博弈论：理性的悖论")
        
        # 左列：囚徒困境矩阵
        payoff_matrix = self.create_payoff_matrix()
        
        # 右列：重复博弈策略
        strategies = VGroup(
            Text("演化策略", font_size=26, color=PROB_GREEN),
            Text("• 以牙还牙 (TFT)", font_size=20),
            Text("• 宽容TFT", font_size=20),
            Text("• 逐步升级", font_size=20),
            Text("合作涌现条件:", font_size=22, color=PROB_YELLOW),
            MathTex(r"\delta > \frac{T-R}{T-P}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        content = VGroup(payoff_matrix, strategies).arrange(RIGHT, buff=2.2, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.85)  # 适当缩放以适应屏幕
        
        self.play(Create(payoff_matrix), Write(strategies))
        
        self.wait(4.5)
        self.clear()
    
    def create_payoff_matrix(self):
        """创建简洁清晰的博弈论收益矩阵"""
        matrix = VGroup()
        
        # 创建主矩阵表格
        table_data = [
            ["", "合作", "背叛"],
            ["合作", "(3,3)", "(0,5)"],
            ["背叛", "(5,0)", "(1,1)"]
        ]
        
        # 创建表格
        table = VGroup()
        
        # 表格边框和单元格
        for i in range(3):
            row = VGroup()
            for j in range(3):
                if i == 0 and j == 0:
                    # 左上角空白
                    cell = Rectangle(width=1.0, height=0.6, stroke_width=1, stroke_color=GRAY)
                    cell_text = Text("", font_size=12)
                elif i == 0:
                    # 第一行标题（玩家2策略）
                    cell = Rectangle(width=1.0, height=0.6, fill_color=PROB_BLUE, fill_opacity=0.3, stroke_width=2)
                    cell_text = Text(table_data[i][j], font_size=14, color=WHITE, weight=BOLD)
                elif j == 0:
                    # 第一列标题（玩家1策略）
                    cell = Rectangle(width=1.0, height=0.6, fill_color=PROB_GREEN, fill_opacity=0.3, stroke_width=2)
                    cell_text = Text(table_data[i][j], font_size=14, color=WHITE, weight=BOLD)
                else:
                    # 收益单元格
                    cell = Rectangle(width=1.0, height=0.6, stroke_width=2)
                    if table_data[i][j] == "(3,3)":
                        cell.set_fill(PROB_GREEN, opacity=0.2)
                        cell_text = Text(table_data[i][j], font_size=14, color=PROB_GREEN, weight=BOLD)
                    elif table_data[i][j] == "(1,1)":
                        cell.set_fill(PROB_RED, opacity=0.2)
                        cell_text = Text(table_data[i][j], font_size=14, color=PROB_RED, weight=BOLD)
                    else:
                        cell.set_fill(PROB_YELLOW, opacity=0.2)
                        cell_text = Text(table_data[i][j], font_size=14, color=PROB_YELLOW, weight=BOLD)
                
                cell_with_text = VGroup(cell, cell_text)
                cell.move_to(RIGHT * j * 1.1 + DOWN * i * 0.7)
                cell_text.move_to(cell.get_center())
                row.add(cell_with_text)
            table.add(row)
        
        # 玩家标签
        player1_label = Text("玩家1", font_size=16, color=PROB_GREEN, weight=BOLD)
        player1_label.next_to(table, LEFT, buff=0.5).shift(DOWN * 0.35)
        
        player2_label = Text("玩家2", font_size=16, color=PROB_BLUE, weight=BOLD)
        player2_label.next_to(table, UP, buff=0.3)
        
        # 说明文字
        explanation = VGroup(
            Text("• (3,3) 双方合作：双赢", font_size=12, color=PROB_GREEN),
            Text("• (0,5) (5,0) 一方背叛：零和", font_size=12, color=PROB_YELLOW),
            Text("• (1,1) 双方背叛：双输", font_size=12, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanation.next_to(table, DOWN, buff=0.8)
        
        matrix.add(table, player1_label, player2_label, explanation)
        return matrix
    
    def application_7_learning_markov_spaced(self):
        """应用7：学习优化 - 马尔可夫链与间隔重复"""
        self.clear()
        header = self.show_application_header(7, "学习科学：记忆的数学")
        
        # 左列：遗忘曲线
        forgetting_curve = self.create_forgetting_curve()
        
        # 右列：马尔可夫与复习间隔
        markov_model = VGroup(
            Text("知识状态转移", font_size=26, color=PROB_BLUE),
            MathTex(r"P = \begin{bmatrix} 0.7 & 0.3 \\ 0.1 & 0.9 \end{bmatrix}"),
            Text("稳态: [0.25, 0.75]", font_size=20, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.25)
        
        optimal_intervals = VGroup(
            Text("最优间隔", font_size=22, color=PROB_YELLOW),
            Text("1天→3天→7天→14天→30天", font_size=20)
        ).arrange(DOWN, buff=0.15)
        
        right_col = VGroup(markov_model, optimal_intervals).arrange(DOWN, buff=0.5)
        content = VGroup(forgetting_curve, right_col).arrange(RIGHT, buff=1.8, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.85)  # 适当缩放以适应屏幕
        
        self.play(Create(forgetting_curve), Write(right_col))
        
        self.wait(4.5)
        self.clear()
    
    def create_forgetting_curve(self):
        """创建遗忘曲线"""
        axes = Axes(
            x_range=[0, 30, 5],
            y_range=[0, 100, 20],
            x_length=5,
            y_length=3,
            axis_config={"include_numbers": True, "font_size": 12}
        )
        
        # 自然遗忘
        natural_curve = axes.plot(
            lambda t: 100 * np.exp(-t/5),
            color=PROB_RED,
            stroke_width=2
        )
        
        # 间隔重复
        spaced_curve = axes.plot(
            lambda t: 100 * (0.9 ** (t/10)) * (1 + 0.1 * np.sin(t)),
            color=PROB_GREEN,
            stroke_width=2
        )
        
        # 标签
        labels = VGroup(
            Text("自然遗忘", font_size=14, color=PROB_RED).next_to(natural_curve, RIGHT),
            Text("间隔重复", font_size=14, color=PROB_GREEN).next_to(spaced_curve, UR)
        )
        
        return VGroup(axes, natural_curve, spaced_curve, labels)
    
    def application_8_sports_gambler_statistics(self):
        """应用8：体育统计 - 赌徒谬误与热手效应"""
        self.clear()
        header = self.show_application_header(8, "体育统计：随机中的模式")
        
        # 左列：赌徒谬误
        gambler_fallacy = VGroup(
            Text("赌徒谬误", font_size=26, color=PROB_BLUE),
            Text("连续10次红色后...", font_size=20),
            MathTex(r"P(Black) = \frac{18}{37} \approx 48.6\%"),
            Text("概率不变！", font_size=22, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.25)
        
        # 右列：独立性检验
        independence_test = VGroup(
            Text("篮球投篮数据", font_size=26, color=PROB_YELLOW),
            Text("连续命中后:", font_size=20),
            Text("下次命中率: 46.0%", font_size=20),
            Text("整体命中率: 46.4%", font_size=20),
            Text("结论: 无热手效应", font_size=22, color=PROB_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.2)
        content = VGroup(gambler_fallacy, independence_test).arrange(RIGHT, buff=2.0, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.85)  # 适当缩放以适应屏幕
        
        self.play(Write(gambler_fallacy), Write(independence_test))
        
        self.wait(4.5)
        self.clear()
    
    def application_9_startup_random_walk_survival(self):
        """应用9：创业生存 - 随机漫步与生存分析"""
        self.clear()
        header = self.show_application_header(9, "创业生存：有偏的随机")
        
        # 左列：随机漫步模拟
        random_walk_viz = self.create_startup_random_walk()
        
        # 右列：生存函数与成功因素
        survival_analysis = VGroup(
            Text("创业生存率", font_size=26, color=PROB_RED),
            MathTex(r"S(t) = e^{-\lambda t}"),
            Text("1年: 65%", font_size=20),
            Text("3年: 35%", font_size=20),
            Text("5年: 18%", font_size=20, color=PROB_RED)
        ).arrange(DOWN, buff=0.2)
        
        success_factors = VGroup(
            Text("成功关键", font_size=22, color=PROB_GREEN),
            Text("• 正向漂移 (学习)", font_size=18),
            Text("• 降低波动 (专注)", font_size=18),
            Text("• 延长时间 (坚持)", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        right_col = VGroup(survival_analysis, success_factors).arrange(DOWN, buff=0.5)
        content = VGroup(random_walk_viz, right_col).arrange(RIGHT, buff=1.6, aligned_edge=UP)
        content.next_to(header, DOWN, buff=0.8)
        content.scale(0.85)  # 适当缩放以适应屏幕
        
        self.play(Create(random_walk_viz), Write(right_col))
        
        self.wait(4.5)
        self.clear()
    
    def create_startup_random_walk(self):
        """创建创业随机漫步"""
        axes = Axes(
            x_range=[0, 50, 10],
            y_range=[-50, 100, 50],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 12}
        )
        
        # 三条路径
        paths = VGroup()
        colors = [PROB_GREEN, PROB_YELLOW, PROB_RED]
        drifts = [0.5, 0, -0.3]
        
        for color, drift in zip(colors, drifts):
            path_points = []
            value = 50
            for t in range(51):
                path_points.append(axes.c2p(t, value))
                value += np.random.normal(drift, 5)
                value = max(0, value)
            
            path = VMobject(color=color, stroke_width=2)
            path.set_points_smoothly(path_points)
            paths.add(path)
        
        # 标签
        labels = VGroup(
            Text("成功", font_size=14, color=PROB_GREEN),
            Text("生存", font_size=14, color=PROB_YELLOW),
            Text("失败", font_size=14, color=PROB_RED)
        ).arrange(DOWN, buff=0.2)
        labels.next_to(axes, RIGHT)
        
        return VGroup(axes, paths, labels)
    
    def application_10_life_philosophy_all(self):
        """应用10：人生哲学 - 所有概念的终极融合"""
        self.clear()
        header = self.show_application_header(10, "人生哲学：概率的智慧")
        
        # 核心标题 - 放大并居中
        main_title = Text("概率思维的人生应用", font_size=32, color=PROB_PURPLE, weight=BOLD)
        main_title.move_to(UP * 2.5)
        
        # 八条应用 - 放大字体并居中排列
        left_principles = VGroup(
            Text("期望值思维：长期主义", font_size=22, color=PROB_BLUE),
            Text("贝叶斯更新：终身学习", font_size=22, color=PROB_GREEN),
            Text("大数定律：坚持的力量", font_size=22, color=PROB_YELLOW),
            Text("最优停止：适时决策", font_size=22, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        right_principles = VGroup(
            Text("独立性：理性判断", font_size=22, color=PROB_GRAY),
            Text("正态分布：接受平凡", font_size=22, color=PROB_PURPLE),
            Text("概率思维：拥抱不确定", font_size=22, color=PROB_YELLOW),
            Text("数学工具：量化世界", font_size=22, color=PROB_BLUE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        principles_content = VGroup(left_principles, right_principles).arrange(RIGHT, buff=3.0)
        full_content = VGroup(main_title, principles_content).arrange(DOWN, buff=1.5)
        full_content.move_to(ORIGIN)
        
        self.play(Write(main_title), run_time=2)
        self.wait(1)
        self.play(Write(left_principles), run_time=2.5)
        self.wait(1)
        self.play(Write(right_principles), run_time=2.5)
        
        self.wait(6)  # 增加停留时间
        
        # 转换到终极感悟
        self.play(FadeOut(full_content))
        
        # 终极感悟 - 调整大小和布局，增加间距避免重叠
        ultimate_wisdom = VGroup(
            Text("如果人生是一场概率游戏", font_size=26, color=WHITE),
            Text("那么概率思维就是攻略", font_size=28, color=PROB_PURPLE, weight=BOLD),
            Text("拥抱不确定性 · 理性决策", font_size=22, color=PROB_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=1.0)
        ultimate_wisdom.move_to(ORIGIN)
        
        for line in ultimate_wisdom:
            if line.text:  # 跳过空行
                self.play(Write(line), run_time=1.2)
        
        self.wait(5)
        self.clear()
    
    def mathematical_beauty_showcase(self):
        """数学之美 - 核心公式展览"""
        self.clear()
        
        title = Text("概率论的数学之美", font_size=TITLE_SIZE, color=PROB_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        
        # 重新组织公式为更清晰的布局
        formulas = [
            (r"P(A|B) = \frac{P(B|A)P(A)}{P(B)}", "贝叶斯定理", PROB_BLUE),
            (r"E[X] = \sum_i x_i p_i", "期望值", PROB_GREEN),
            (r"\bar{X}_n \xrightarrow{P} \mu", "大数定律", PROB_YELLOW),
            (r"P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}", "泊松分布", PROB_RED),
            (r"\frac{\sum X_i - n\mu}{\sigma\sqrt{n}} \sim N(0,1)", "中心极限定理", PROB_PURPLE),
            (r"f^* = \frac{p(b+1)-1}{b}", "凯利公式", PROB_BLUE)
        ]
        
        # 创建三行两列的布局
        formula_groups = []
        for i, (formula, name, color) in enumerate(formulas):
            formula_group = VGroup(
                MathTex(formula).scale(0.8).set_color(color),
                Text(name, font_size=18, color=color, weight=BOLD)
            ).arrange(DOWN, buff=0.2)
            formula_groups.append(formula_group)
        
        # 安排为三行两列
        row1 = VGroup(formula_groups[0], formula_groups[1]).arrange(RIGHT, buff=3.0)
        row2 = VGroup(formula_groups[2], formula_groups[3]).arrange(RIGHT, buff=3.0)
        row3 = VGroup(formula_groups[4], formula_groups[5]).arrange(RIGHT, buff=3.0)
        
        formula_grid = VGroup(row1, row2, row3).arrange(DOWN, buff=1.2)
        formula_grid.next_to(title, DOWN, buff=1.0)
        
        # 整体内容组
        content = VGroup(title, formula_grid)
        content.scale(0.85)
        content.move_to(ORIGIN)
        
        self.play(Write(title), run_time=2)
        
        # 逐行显示公式
        for row in [row1, row2, row3]:
            for formula in row:
                self.play(Write(formula), run_time=1)
            self.wait(0.5)
        
        self.wait(5)
        self.clear()
    
    def ultimate_philosophical_summary(self):
        """终极哲学总结"""
        self.clear()
        
        # 主标题
        title = Text("概率思维的三重境界", font_size=38, color=PROB_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        
        # 三层境界 - 重新布局为更紧凑的形式
        levels = VGroup(
            VGroup(
                Text("第一层：认识随机", font_size=26, color=PROB_BLUE, weight=BOLD),
                Text("接受世界的不确定性", font_size=20, color=GRAY)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("第二层：计算概率", font_size=26, color=PROB_YELLOW, weight=BOLD),
                Text("用数学量化不确定性", font_size=20, color=GRAY)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("第三层：概率思维", font_size=26, color=PROB_GREEN, weight=BOLD),
                Text("在不确定中做出最优决策", font_size=20, color=GRAY)
            ).arrange(DOWN, buff=0.2)
        ).arrange(DOWN, buff=0.8)
        
        levels_content = VGroup(title, levels).arrange(DOWN, buff=1.0)
        levels_content.move_to(ORIGIN)
        
        self.play(Write(title), run_time=2)
        for level in levels:
            self.play(Write(level), run_time=1.2)
        
        self.wait(3)
        self.play(FadeOut(levels_content))
        
        # 终极真理 - 调整大小和布局，避免重叠
        ultimate_truth = VGroup(
            Text("概率论告诉我们", font_size=28, color=WHITE),
            Text("世界是随机的", font_size=30, color=PROB_RED, weight=BOLD),
            Text("但不是任意的", font_size=30, color=PROB_GREEN, weight=BOLD),
            Text("这就是数学的力量", font_size=32, color=PROB_PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0.8)
        ultimate_truth.move_to(ORIGIN)
        
        for line in ultimate_truth:
            if line.text:  # 跳过空行
                self.play(Write(line), run_time=1.2)
        
        self.wait(5)
        self.clear()
    
    def series_philosophy_complete(self):
        """完整的哲学体系呈现"""
        self.clear()
        
        # 标题 - 放大并居中
        title = Text("概率思维的人生智慧", font_size=36, color=PROB_PURPLE, weight=BOLD)
        title.move_to(UP * 3)
        
        # 20条智慧 - 放大字体并居中
        wisdom_groups = [
            # 第一组：悖论教会我们
            VGroup(
                Text("悖论教会我们", font_size=26, color=PROB_YELLOW, weight=BOLD),
                Text("1. 直觉常常欺骗我们", font_size=18),
                Text("2. 巧合比想象中常见", font_size=18),
                Text("3. 同样的数据可以得出相反结论", font_size=18),
                Text("4. 问题的定义决定答案", font_size=18),
                Text("5. 赌场永远是赢家", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25),
            
            # 第二组：定律告诉我们
            VGroup(
                Text("定律告诉我们", font_size=26, color=PROB_BLUE, weight=BOLD),
                Text("6. 长期来看，平均值总会实现", font_size=18),
                Text("7. 极端事件终将回归正常", font_size=18),
                Text("8. 大量随机汇聚成确定", font_size=18),
                Text("9. 新信息应该改变信念", font_size=18),
                Text("10. 未来只取决于现在", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25),
            
            # 第三组：决策教会我们
            VGroup(
                Text("决策教会我们", font_size=26, color=PROB_GREEN, weight=BOLD),
                Text("11. 不要赌上全部", font_size=18),
                Text("12. 探索后再决定", font_size=18),
                Text("13. 合作优于背叛", font_size=18),
                Text("14. 稀有事件会发生", font_size=18),
                Text("15. 独立事件没有记忆", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25),
            
            # 第四组：人生的概率哲学
            VGroup(
                Text("人生的概率哲学", font_size=26, color=PROB_RED, weight=BOLD),
                Text("16. 接受平凡是常态", font_size=18),
                Text("17. 坚持让小概率变大概率", font_size=18),
                Text("18. 多样化降低风险", font_size=18),
                Text("19. 短期随机，长期有序", font_size=18),
                Text("20. 基础概率决定一切", font_size=18)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        ]
        
        self.play(Write(title), run_time=2.5)
        self.wait(1)
        
        # 重新布局为两列显示 - 放大并居中，整体向上移动
        left_column = VGroup(wisdom_groups[0], wisdom_groups[1]).arrange(DOWN, buff=0.8)
        right_column = VGroup(wisdom_groups[2], wisdom_groups[3]).arrange(DOWN, buff=0.8)
        
        content_layout = VGroup(left_column, right_column).arrange(RIGHT, buff=2.5)
        content_layout.next_to(title, DOWN, buff=0.3)  # 缩小与标题的距离
        content_layout.scale(0.85)  # 适当缩放
        
        # 逐列显示
        self.play(FadeIn(left_column, shift=UP), run_time=3)
        self.wait(1.5)
        self.play(FadeIn(right_column, shift=UP), run_time=3)
        
        self.wait(7)  # 大幅增加停留时间
        
        # 最终智慧
        self.clear()
        final_wisdom = VGroup(
            Text("第21条 - 终极智慧", font_size=30, color=PROB_PURPLE, weight=BOLD),
            Text("", font_size=10),
            Text("拥抱不确定性", font_size=34, color=PROB_YELLOW, weight=BOLD),
            Text("但理性决策", font_size=34, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.6)
        final_wisdom.move_to(ORIGIN)
        
        for line in final_wisdom:
            if line.text:  # 跳过空行
                self.play(Write(line), run_time=1.2)
        
        self.wait(4)
        
        # 三个终极领悟
        self.clear()
        
        title = Text("三个终极领悟", font_size=28, color=PROB_PURPLE, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        
        insight1 = VGroup(
            Text("一、世界的本质", font_size=20, color=PROB_BLUE, weight=BOLD),
            Text("随机性是世界的特征，不是缺陷", font_size=16),
            Text("概率是理解世界的语言", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        insight2 = VGroup(
            Text("二、决策的智慧", font_size=20, color=PROB_GREEN, weight=BOLD),
            Text("不追求确定的结果", font_size=16),
            Text("追求正确的过程", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        insight3 = VGroup(
            Text("三、人生的态度", font_size=20, color=PROB_YELLOW, weight=BOLD),
            Text("理性面对不确定性", font_size=16),
            Text("在概率中寻找意义", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        insights_content = VGroup(insight1, insight2, insight3).arrange(DOWN, buff=0.6)
        insights_content.next_to(title, DOWN, buff=0.8)
        
        full_content = VGroup(title, insights_content)
        full_content.scale(0.9)
        full_content.move_to(ORIGIN)
        
        self.play(Write(title), run_time=2)
        
        for insight in [insight1, insight2, insight3]:
            self.play(Write(insight), run_time=1.2)
        
        self.wait(3)
        
        # 最终的三句话
        self.clear()
        
        title = Text("如果只能留下三句话", font_size=26, color=GRAY, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        
        three_sentences = VGroup(
            Text("用概率的眼光看世界", font_size=28, color=PROB_BLUE, weight=BOLD),
            Text("用理性的方式做决策", font_size=28, color=PROB_GREEN, weight=BOLD),
            Text("用平和的心态接受结果", font_size=28, color=PROB_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.8)
        
        essence = Text("这就是概率思维的精髓", font_size=24, color=PROB_PURPLE, weight=BOLD)
        
        content = VGroup(title, three_sentences, essence).arrange(DOWN, buff=1.0)
        content.move_to(ORIGIN)
        
        self.play(Write(title), run_time=2)
        
        for sentence in three_sentences:
            self.play(Write(sentence), run_time=1.5)
        
        self.wait(1)
        self.play(Write(essence), run_time=2)
        
        self.wait(3)
        self.clear()
    
    def series_grand_finale(self):
        """系列大结局"""
        self.clear()
        
        # 感谢
        thanks = Text(
            "感谢同行21集",
            font_size=56,
            color=PROB_PURPLE,
            weight=BOLD
        )
        self.play(Write(thanks), run_time=2.5)
        self.wait(1)
        self.play(FadeOut(thanks))
        
        # 数据回顾
        title = Text("21集旅程", font_size=30, color=PROB_YELLOW, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        
        statistics = VGroup(
            Text("15个经典悖论", font_size=24),
            Text("10大概率定律", font_size=24),
            Text("∞种实际应用", font_size=24)
        ).arrange(DOWN, buff=0.5)
        
        core_idea = VGroup(
            Text("1个核心思想：", font_size=26, color=PROB_GREEN),
            Text("在不确定性中寻找确定性", font_size=28, color=PROB_PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        
        journey_content = VGroup(title, statistics, core_idea).arrange(DOWN, buff=1.0)
        journey_content.move_to(ORIGIN)
        
        self.play(Write(title), run_time=2)
        
        for stat in statistics:
            self.play(Write(stat), run_time=1)
        
        self.wait(1)
        
        for idea in core_idea:
            self.play(Write(idea), run_time=1.5)
        
        self.wait(3)
        self.play(FadeOut(journey_content))
        
        # 最后的话
        series_title = Text("概率论的反直觉世界", font_size=36, color=PROB_PURPLE, weight=BOLD)
        series_title.to_edge(UP, buff=0.8)
        
        end_mark = Text("— 完 —", font_size=30, color=WHITE)
        blessing = Text("愿概率与你同在", font_size=26, color=PROB_YELLOW, weight=BOLD)
        
        final_content = VGroup(series_title, end_mark, blessing).arrange(DOWN, buff=1.5)
        final_content.move_to(ORIGIN)
        
        self.play(Write(series_title), run_time=2)
        self.wait(1)
        self.play(Write(end_mark), run_time=1.5)
        self.wait(1)
        self.play(Write(blessing), run_time=2)
        
        # 彩蛋
        easter_egg = Text(
            "Life is probabilistic, not deterministic",
            font_size=18,
            color=PROB_GRAY,
            slant=ITALIC
        )
        easter_egg.to_edge(DOWN, buff=0.5)
        self.play(Write(easter_egg))
        
        self.wait(5)
    
    def show_application_header(self, number: int, title: str):
        """显示应用标题"""
        app_number = Text(f"应用 #{number}", font_size=26, color=PROB_YELLOW)
        app_number.to_edge(UL, buff=0.5)
        
        app_title = Text(title, font_size=36, color=PROB_PURPLE)
        app_title.to_edge(UP, buff=0.5)
        
        self.play(Write(app_number), Write(app_title))
        header_group = VGroup(app_number, app_title)
        return header_group