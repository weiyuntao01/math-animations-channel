"""
EP14: 贝叶斯思维
如何像侦探一样思考 - 用证据更新信念
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple

# 概率系列颜色主题
PROB_PURPLE = "#8B5CF6"    # 主色：概率紫
PROB_GREEN = "#10B981"     # 成功绿
PROB_RED = "#EF4444"       # 失败红
PROB_BLUE = "#3B82F6"      # 数据蓝
PROB_YELLOW = "#F59E0B"    # 警告黄
PROB_GRAY = "#6B7280"      # 中性灰

# 字体大小调整（比之前大2号）
TITLE_SIZE = 44        # 原42
SUBTITLE_SIZE = 30     # 原28
NORMAL_SIZE = 24       # 原22
SMALL_SIZE = 20        # 原18


class BayesianThinkingEP14(Scene):
    """贝叶斯思维 - 概率论系列 EP14"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(14, "贝叶斯思维")
        
        # 2. 问题引入 - 医疗诊断
        self.introduce_medical_diagnosis()
        
        # 3. 贝叶斯定理推导
        self.derive_bayes_theorem()
        
        # 4. 直观理解 - 频率图解
        self.frequency_visualization()
        
        # 5. 经典案例 - 检测悖论
        self.testing_paradox()
        
        # 6. 贝叶斯更新过程
        self.bayesian_updating()
        
        # 7. 现实应用
        self.real_world_applications()
        
        # 8. 结尾
        self.show_ending()
    
    def show_series_intro(self, episode_num: int, episode_title: str):
        """显示系列介绍动画"""
        # 系列标题
        series_title = Text(
            "概率论的反直觉世界",
            font_size=50,  # 原48
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 集数标题
        episode_text = Text(
            f"第{episode_num}集：{episode_title}",
            font_size=34,  # 原32
            color=WHITE
        )
        episode_text.next_to(series_title, DOWN, buff=0.8)
        
        # 动画效果
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(series_title), FadeOut(episode_text))
    
    def introduce_medical_diagnosis(self):
        """引入问题 - 医疗诊断"""
        title = Text("一个让人焦虑的问题", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 场景设置（左侧）
        doctor_scene = self.create_doctor_scene()
        doctor_scene.shift(LEFT * 4)
        self.play(FadeIn(doctor_scene))
        
        # 对话（右侧）
        dialogue = VGroup(
            Text("医生：", font_size=SUBTITLE_SIZE, color=PROB_BLUE),
            Text("您的检测结果呈阳性", font_size=NORMAL_SIZE, color=WHITE),
            Text("这种检测的准确率是99%", font_size=NORMAL_SIZE, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        dialogue.shift(RIGHT * 3.5 + UP * 0.5)
        
        for line in dialogue:
            self.play(Write(line), run_time=0.8)
        
        # 患者的问题
        patient_question = Text(
            "我真的有99%的概率患病吗？",
            font_size=SUBTITLE_SIZE,
            color=PROB_YELLOW
        )
        patient_question.shift(DOWN * 2)
        self.play(Write(patient_question))
        
        # 答案预告
        answer_preview = Text(
            "答案可能出乎你的意料...",
            font_size=NORMAL_SIZE,
            color=PROB_RED
        )
        answer_preview.shift(DOWN * 2.8)
        self.play(Write(answer_preview))
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(doctor_scene),
            FadeOut(dialogue), FadeOut(patient_question),
            FadeOut(answer_preview)
        )
    
    def create_doctor_scene(self):
        """创建医生场景"""
        scene = VGroup()
        
        # 简化的医生图标
        doctor = VGroup(
            Circle(radius=0.5, fill_color=PROB_BLUE, fill_opacity=0.8),
            Text("医", font_size=30, color=WHITE)
        )
        
        # 病历本
        clipboard = Rectangle(
            width=1.5, height=2,
            fill_color=WHITE,
            fill_opacity=0.9,
            stroke_color=GRAY
        )
        clipboard.next_to(doctor, DOWN, buff=0.5)
        
        # 检测结果
        result = Text("阳性", font_size=24, color=PROB_RED)
        result.move_to(clipboard.get_center())
        
        scene.add(doctor, clipboard, result)
        return scene
    
    def derive_bayes_theorem(self):
        """推导贝叶斯定理"""
        title = Text("贝叶斯定理：理性的基石", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 第一步：条件概率
        self.show_conditional_probability()
        
        # 第二步：贝叶斯公式
        self.show_bayes_formula()
        
        self.play(FadeOut(title))
    
    def show_conditional_probability(self):
        """展示条件概率"""
        # 清屏
        self.clear()
        
        # 从联合概率开始
        joint_title = Text("从联合概率开始", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        joint_title.move_to([0, 3, 0])  # 固定位置
        self.play(Write(joint_title))
        
        # 左侧：公式推导
        # 两种表达方式
        formula1 = MathTex(r"P(A \cap B) = P(A|B) \cdot P(B)")
        formula2 = MathTex(r"P(A \cap B) = P(B|A) \cdot P(A)")
        
        formulas = VGroup(formula1, formula2).arrange(DOWN, buff=0.5)
        formulas.move_to([-3.5, 1, 0])  # 左侧固定位置
        
        # 因此
        therefore = Text("因此：", font_size=NORMAL_SIZE, color=WHITE)
        therefore.move_to([-3.5, -0.5, 0])  # 固定位置
        
        conclusion = MathTex(r"P(A|B) \cdot P(B) = P(B|A) \cdot P(A)")
        conclusion.move_to([-3.5, -1.5, 0])  # 固定位置
        
        # 右侧：图解说明
        # 创建两个圆形表示集合
        circle_a = Circle(radius=0.8, color=PROB_BLUE, fill_opacity=0.3)
        circle_b = Circle(radius=0.8, color=PROB_GREEN, fill_opacity=0.3)
        circle_a.move_to([3, 1, 0])
        circle_b.move_to([3.8, 1, 0])
        
        # 标签
        label_a = Text("A", font_size=NORMAL_SIZE, color=PROB_BLUE)
        label_a.move_to([2.5, 1, 0])
        label_b = Text("B", font_size=NORMAL_SIZE, color=PROB_GREEN)
        label_b.move_to([4.3, 1, 0])
        
        # 交集标记
        intersection = Text("A∩B", font_size=SMALL_SIZE, color=WHITE)
        intersection.move_to([3.4, 1, 0])
        
        # 说明文字
        explanation = VGroup(
            Text("联合概率", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("可以从两个", font_size=SMALL_SIZE),
            Text("方向计算", font_size=SMALL_SIZE)
        ).arrange(DOWN, buff=0.2)
        explanation.move_to([3.5, -1, 0])  # 固定位置
        
        # 动画
        self.play(Write(formula1))
        self.wait(0.5)
        self.play(Create(circle_a), Create(circle_b), Write(label_a), Write(label_b))
        self.wait(0.5)
        self.play(Write(formula2))
        self.wait(0.5)
        self.play(Write(intersection), Write(explanation))
        self.wait(0.5)
        self.play(Write(therefore), Write(conclusion))
        self.wait(2)
        
        self.play(
            FadeOut(joint_title), FadeOut(formulas), FadeOut(therefore), FadeOut(conclusion),
            FadeOut(circle_a), FadeOut(circle_b), FadeOut(label_a), FadeOut(label_b),
            FadeOut(intersection), FadeOut(explanation)
        )
    
    def show_bayes_formula(self):
        """展示贝叶斯公式"""
        # 清屏
        self.clear()
        
        # 标题
        formula_title = Text("贝叶斯定理", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        formula_title.move_to([0, 3, 0])  # 固定在顶部
        self.play(Write(formula_title))
        
        # 左侧：主公式
        bayes = MathTex(
            r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}"
        ).scale(1.3)
        bayes.move_to([-3.5, 0.5, 0])  # 左侧中间位置
        
        # 核心思想
        core_idea = Text(
            "新信念 = 旧信念 × 证据强度",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        core_idea.move_to([-3.5, -1.5, 0])  # 左侧下方
        
        # 右侧：各部分解释
        exp1 = VGroup(
            MathTex(r"P(A|B)", color=PROB_GREEN).scale(0.9),
            Text("后验概率", font_size=SMALL_SIZE),
            Text("更新后的信念", font_size=16, color=GRAY)
        ).arrange(DOWN, buff=0.1)
        exp1.move_to([3.5, 2, 0])  # 右侧顶部
        
        exp2 = VGroup(
            MathTex(r"P(B|A)", color=PROB_BLUE).scale(0.9),
            Text("似然度", font_size=SMALL_SIZE),
            Text("证据的强度", font_size=16, color=GRAY)
        ).arrange(DOWN, buff=0.1)
        exp2.move_to([3.5, 0.5, 0])  # 右侧中上
        
        exp3 = VGroup(
            MathTex(r"P(A)", color=PROB_YELLOW).scale(0.9),
            Text("先验概率", font_size=SMALL_SIZE),
            Text("初始信念", font_size=16, color=GRAY)
        ).arrange(DOWN, buff=0.1)
        exp3.move_to([3.5, -1, 0])  # 右侧中下
        
        exp4 = VGroup(
            MathTex(r"P(B)", color=PROB_RED).scale(0.9),
            Text("边际概率", font_size=SMALL_SIZE),
            Text("归一化因子", font_size=16, color=GRAY)
        ).arrange(DOWN, buff=0.1)
        exp4.move_to([3.5, -2.5, 0])  # 右侧底部
        
        # 动画
        self.play(Write(bayes))
        self.wait(0.5)
        
        # 逐个显示解释
        self.play(Write(exp1))
        self.play(Write(exp2))
        self.play(Write(exp3))
        self.play(Write(exp4))
        
        self.wait(1)
        self.play(Write(core_idea))
        self.wait(2)
        
        self.play(
            FadeOut(formula_title), FadeOut(bayes), FadeOut(core_idea),
            FadeOut(exp1), FadeOut(exp2), FadeOut(exp3), FadeOut(exp4)
        )
    
    def frequency_visualization(self):
        """频率图解法理解贝叶斯"""
        title = Text("1000人中的真相", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 设置参数
        total = 1000
        disease_rate = 0.001  # 0.1%的人有病
        test_accuracy = 0.99  # 99%准确率
        
        # 创建人群图标
        self.visualize_population(total, disease_rate, test_accuracy)
        
        self.play(FadeOut(title))
    
    def visualize_population(self, total, disease_rate, test_accuracy):
        """可视化人群分布"""
        # 清屏
        self.clear()
        
        # 计算各类人数
        sick = int(total * disease_rate)  # 1人
        healthy = total - sick  # 999人
        
        # 真阳性和假阳性
        true_positive = sick  # 1人（假设都检出）
        false_positive = int(healthy * (1 - test_accuracy))  # 约10人
        
        # 左侧：图示
        population_viz = self.create_population_diagram(
            sick, healthy, true_positive, false_positive
        )
        population_viz.move_to([-3.5, 0.5, 0])  # 固定位置
        self.play(Create(population_viz))
        
        # 右侧：计算展示
        # 分步显示数据
        line1 = Text(f"总人数：{total}人", font_size=NORMAL_SIZE)
        line1.move_to([3.5, 2.5, 0])
        
        line2 = Text(f"实际患病：{sick}人", font_size=NORMAL_SIZE, color=PROB_RED)
        line2.move_to([3.5, 2, 0])
        
        line3 = Text(f"健康人数：{healthy}人", font_size=NORMAL_SIZE, color=PROB_GREEN)
        line3.move_to([3.5, 1.5, 0])
        
        line4 = Text(f"检测阳性：{true_positive + false_positive}人", font_size=NORMAL_SIZE, color=PROB_YELLOW)
        line4.move_to([3.5, 1, 0])
        
        line5 = Text("其中：", font_size=SMALL_SIZE, color=GRAY)
        line5.move_to([3.5, 0.5, 0])
        
        line6 = Text(f"  真阳性：{true_positive}人", font_size=SMALL_SIZE)
        line6.move_to([3.5, 0.1, 0])
        
        line7 = Text(f"  假阳性：{false_positive}人", font_size=SMALL_SIZE)
        line7.move_to([3.5, -0.3, 0])
        
        line8 = Text("阳性预测值：", font_size=NORMAL_SIZE, color=PROB_GREEN)
        line8.move_to([3.5, -1, 0])
        
        line9 = Text(f"{true_positive}/{true_positive + false_positive} ≈ 9.1%", 
                    font_size=SUBTITLE_SIZE, color=PROB_GREEN, weight=BOLD)
        line9.move_to([3.5, -1.6, 0])
        
        # 动画显示
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(line5))
        self.play(Write(line6))
        self.play(Write(line7))
        self.play(Write(line8))
        self.play(Write(line9))
        
        # 强调框
        emphasis = SurroundingRectangle(
            line9, 
            color=PROB_GREEN, 
            stroke_width=3,
            buff=0.15
        )
        self.play(Create(emphasis))
        
        # 底部震撼文字
        shock_text = Text(
            "不是99%，而是9.1%！",
            font_size=SUBTITLE_SIZE,
            color=PROB_RED,
            weight=BOLD
        )
        shock_text.move_to([0, -3, 0])  # 固定在底部中央
        self.play(Write(shock_text))
        
        self.wait(3)
        self.play(
            FadeOut(population_viz), 
            FadeOut(line1), FadeOut(line2), FadeOut(line3), FadeOut(line4),
            FadeOut(line5), FadeOut(line6), FadeOut(line7), FadeOut(line8), FadeOut(line9),
            FadeOut(emphasis), FadeOut(shock_text)
        )
    
    def create_population_diagram(self, sick, healthy, true_positive, false_positive):
        """创建人群分布图"""
        diagram = VGroup()
        
        # 总人群框架
        total_rect = Rectangle(
            width=5, height=3.5,
            fill_color=PROB_GRAY,
            fill_opacity=0.3,
            stroke_color=WHITE
        )
        total_label = Text("1000人", font_size=SMALL_SIZE, color=WHITE)
        total_label.next_to(total_rect, UP, buff=0.2)
        
        # 患病组（很小的竖条）
        sick_width = 0.1  # 0.1%的宽度
        sick_rect = Rectangle(
            width=sick_width * 5,
            height=3.2,
            fill_color=PROB_RED,
            fill_opacity=0.8,
            stroke_color=PROB_RED
        )
        sick_rect.align_to(total_rect, LEFT).align_to(total_rect, DOWN)
        sick_rect.shift(RIGHT * 0.15 + UP * 0.15)
        
        # 健康组
        healthy_rect = Rectangle(
            width=(1 - sick_width) * 5 - 0.3,
            height=3.2,
            fill_color=PROB_GREEN,
            fill_opacity=0.3,
            stroke_color=PROB_GREEN
        )
        healthy_rect.next_to(sick_rect, RIGHT, buff=0.1)
        healthy_rect.align_to(sick_rect, DOWN)
        
        # 组标签
        sick_label = Text("患病\n1人", font_size=12, color=PROB_RED, line_spacing=0.5)
        sick_label.next_to(sick_rect, DOWN, buff=0.2)
        
        healthy_label = Text("健康\n999人", font_size=12, color=PROB_GREEN, line_spacing=0.5)
        healthy_label.next_to(healthy_rect, DOWN, buff=0.2)
        
        # 检测结果标记
        # 真阳性（患病组内的点）
        tp_dot = Circle(
            radius=0.12,
            fill_color=PROB_YELLOW,
            fill_opacity=1,
            stroke_color=PROB_YELLOW,
            stroke_width=2
        )
        tp_dot.move_to(sick_rect.get_center())
        tp_text = Text("1", font_size=10, color=BLACK, weight=BOLD)
        tp_text.move_to(tp_dot.get_center())
        
        # 假阳性（健康组内的点阵）
        fp_dots = VGroup()
        # 创建2行5列的点阵
        start_x = healthy_rect.get_left()[0] + 0.4
        start_y = healthy_rect.get_center()[1] + 0.4
        
        for row in range(2):
            for col in range(5):
                if row * 5 + col < false_positive:
                    x = start_x + col * 0.7
                    y = start_y - row * 0.8
                    dot = Circle(
                        radius=0.1,
                        fill_color=PROB_YELLOW,
                        fill_opacity=1,
                        stroke_color=PROB_YELLOW,
                        stroke_width=1
                    )
                    dot.move_to([x, y, 0])
                    fp_dots.add(dot)
        
        # 图例
        legend_title = Text("黄色 = 检测阳性", font_size=14, color=PROB_YELLOW)
        legend_title.next_to(total_rect, DOWN, buff=0.5)
        
        diagram.add(
            total_rect, total_label,
            sick_rect, healthy_rect,
            sick_label, healthy_label,
            tp_dot, tp_text, fp_dots,
            legend_title
        )
        
        return diagram
    
    def testing_paradox(self):
        """检测悖论的深入分析"""
        title = Text("为什么会这样？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 关键因素
        factors = VGroup(
            Text("关键因素：基础概率", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("• 疾病很罕见（0.1%）", font_size=NORMAL_SIZE),
            Text("• 健康人太多（99.9%）", font_size=NORMAL_SIZE),
            Text("• 1%的误报率 × 999人 = 10个假阳性", font_size=NORMAL_SIZE),
            Text("• 假阳性淹没了真阳性！", font_size=NORMAL_SIZE, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        factors.shift(LEFT * 2)
        
        for factor in factors:
            self.play(Write(factor), run_time=0.8)
        
        # 图示对比
        comparison = self.create_base_rate_comparison()
        comparison.shift(RIGHT * 3.5)
        self.play(Create(comparison))
        
        # 教训
        lesson = Text(
            "忽视基础概率是人类的通病",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        lesson.shift(DOWN * 2.5)
        self.play(Write(lesson))
        
        self.wait(3)
        self.play(
            FadeOut(title), FadeOut(factors),
            FadeOut(comparison), FadeOut(lesson)
        )
    
    def create_base_rate_comparison(self):
        """创建基础概率对比图"""
        comparison = VGroup()
        
        # 罕见病 vs 常见病
        rare_disease = VGroup(
            Text("罕见病", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("发病率 0.1%", font_size=SMALL_SIZE),
            Text("阳性预测值 9%", font_size=SMALL_SIZE, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.2)
        
        common_disease = VGroup(
            Text("常见病", font_size=NORMAL_SIZE, color=PROB_GREEN),
            Text("发病率 10%", font_size=SMALL_SIZE),
            Text("阳性预测值 91%", font_size=SMALL_SIZE, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.2)
        
        rare_disease.shift(UP * 1)
        common_disease.shift(DOWN * 1)
        
        comparison.add(rare_disease, common_disease)
        
        # 连接箭头
        arrow = Arrow(
            rare_disease.get_bottom(),
            common_disease.get_top(),
            color=WHITE,
            stroke_width=2
        )
        comparison.add(arrow)
        
        return comparison
    
    def bayesian_updating(self):
        """贝叶斯更新过程"""
        title = Text("贝叶斯更新：逐步接近真相", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建更新可视化
        self.show_updating_process()
        
        self.play(FadeOut(title))
    
    def show_updating_process(self):
        """展示更新过程"""
        # 初始信念
        prior = 0.5  # 50%概率
        
        # 证据序列
        evidence_sequence = [
            ("证据1：支持", 0.8, PROB_GREEN),
            ("证据2：反对", 0.3, PROB_RED),
            ("证据3：强烈支持", 0.9, PROB_GREEN),
            ("证据4：支持", 0.7, PROB_GREEN)
        ]
        
        # 创建概率条
        prob_bar = self.create_probability_bar(prior)
        prob_bar.shift(UP * 1)
        self.play(Create(prob_bar))
        
        # 逐步更新
        current_prob = prior
        for i, (desc, likelihood, color) in enumerate(evidence_sequence):
            # 显示证据
            evidence_text = Text(desc, font_size=NORMAL_SIZE, color=color)
            evidence_text.shift(DOWN * 0.5)
            self.play(Write(evidence_text))
            
            # 计算新概率（简化的贝叶斯更新）
            if "支持" in desc:
                current_prob = current_prob * likelihood / (
                    current_prob * likelihood + (1 - current_prob) * (1 - likelihood)
                )
            else:
                current_prob = current_prob * likelihood / (
                    current_prob * likelihood + (1 - current_prob) * (1 - likelihood)
                )
            
            # 更新概率条
            new_bar = self.create_probability_bar(current_prob)
            new_bar.shift(UP * 1)
            self.play(Transform(prob_bar, new_bar))
            
            # 显示当前概率
            prob_text = Text(
                f"当前信念：{current_prob:.1%}",
                font_size=NORMAL_SIZE,
                color=PROB_YELLOW
            )
            prob_text.shift(DOWN * 1.5)
            
            if i == 0:
                self.play(Write(prob_text))
                self.prob_text = prob_text
            else:
                new_prob_text = Text(
                    f"当前信念：{current_prob:.1%}",
                    font_size=NORMAL_SIZE,
                    color=PROB_YELLOW
                )
                new_prob_text.shift(DOWN * 1.5)
                self.play(Transform(self.prob_text, new_prob_text))
            
            self.wait(1)
            self.play(FadeOut(evidence_text))
        
        # 总结
        summary = Text(
            "每个证据都在塑造我们的信念",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        summary.shift(DOWN * 3)
        self.play(Write(summary))
        self.wait(2)
        
        self.play(FadeOut(prob_bar), FadeOut(self.prob_text), FadeOut(summary))
    
    def create_probability_bar(self, probability):
        """创建概率条"""
        bar = VGroup()
        
        # 背景
        bg = Rectangle(
            width=8, height=0.8,
            fill_color=GRAY,
            fill_opacity=0.3,
            stroke_color=WHITE
        )
        
        # 填充部分
        fill_width = 8 * probability
        if fill_width > 0:
            fill = Rectangle(
                width=fill_width,
                height=0.8,
                fill_color=PROB_GREEN if probability > 0.5 else PROB_RED,
                fill_opacity=0.8,
                stroke_width=0
            )
            fill.align_to(bg, LEFT)
            bar.add(fill)
        
        bar.add(bg)
        
        # 刻度
        for i in range(11):
            x = -4 + i * 0.8
            tick = Line(
                [x, -0.4, 0],
                [x, -0.5, 0],
                color=WHITE,
                stroke_width=1
            )
            bar.add(tick)
            
            if i % 5 == 0:
                label = Text(f"{i*10}%", font_size=14)
                label.next_to(tick, DOWN, buff=0.1)
                bar.add(label)
        
        # 当前值标记
        marker_x = -4 + probability * 8
        marker = Triangle(
            fill_color=PROB_YELLOW,
            fill_opacity=1,
            stroke_width=0
        ).scale(0.15)
        marker.move_to([marker_x, 0.5, 0])
        marker.rotate(PI)
        bar.add(marker)
        
        return bar
    
    def real_world_applications(self):
        """现实应用"""
        title = Text("贝叶斯思维的力量", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 应用领域
        applications = VGroup()
        
        # 1. 垃圾邮件过滤
        spam_filter = self.create_application_card(
            "垃圾邮件过滤",
            PROB_BLUE,
            [
                "学习词汇模式",
                "更新垃圾概率",
                "个性化过滤"
            ]
        )
        spam_filter.shift(LEFT * 5 + UP * 1)
        
        # 2. 机器学习
        ml = self.create_application_card(
            "机器学习",
            PROB_GREEN,
            [
                "模型参数更新",
                "不确定性量化",
                "在线学习"
            ]
        )
        ml.shift(LEFT * 1.7 + UP * 1)
        
        # 3. 医疗诊断
        medical = self.create_application_card(
            "医疗决策",
            PROB_YELLOW,
            [
                "综合多项检查",
                "考虑患病率",
                "个体化评估"
            ]
        )
        medical.shift(RIGHT * 1.7 + UP * 1)
        
        # 4. 金融风控
        finance = self.create_application_card(
            "金融风控",
            PROB_RED,
            [
                "欺诈检测",
                "信用评估",
                "风险定价"
            ]
        )
        finance.shift(RIGHT * 5 + UP * 1)
        
        applications.add(spam_filter, ml, medical, finance)
        
        # 逐个显示
        for app in applications:
            self.play(FadeIn(app, shift=UP), run_time=0.5)
        
        # 核心理念
        core_principle = Text(
            "用证据不断更新认知，这就是理性",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        core_principle.shift(DOWN * 2.5)
        self.play(Write(core_principle))
        self.wait(3)
        
        self.play(FadeOut(title), FadeOut(applications), FadeOut(core_principle))
    
    def create_application_card(self, title: str, color, points: List[str]):
        """创建应用卡片"""
        card = VGroup()
        
        # 背景
        bg = RoundedRectangle(
            width=3, height=2.5,
            corner_radius=0.2,
            fill_color=color,
            fill_opacity=0.2,
            stroke_color=color,
            stroke_width=2
        )
        
        # 标题
        title_text = Text(title, font_size=NORMAL_SIZE, color=color, weight=BOLD)
        title_text.shift(UP * 0.8)
        
        # 要点
        points_text = VGroup()
        for point in points:
            point_text = Text(f"• {point}", font_size=SMALL_SIZE, color=WHITE)
            points_text.add(point_text)
        points_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        points_text.shift(DOWN * 0.2)
        
        card.add(bg, title_text, points_text)
        return card
    
    def show_ending(self):
        """结尾"""
        # 核心总结
        summary = VGroup(
            Text("贝叶斯定理告诉我们：", font_size=38, color=WHITE),  # 原36
            Text("永远不要忽视基础概率", font_size=TITLE_SIZE, color=PROB_PURPLE, weight=BOLD),
            Text("让证据引导信念", font_size=34, color=PROB_YELLOW)  # 原32
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 系列结尾
        self.show_series_ending(
            "理性思考的本质",
            "就是正确处理不确定性"
        )
    
    def show_series_ending(self, main_message: str, sub_message: str):
        """显示系列结尾动画"""
        # 主信息
        main_text = Text(
            main_message,
            font_size=50,  # 原48
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 副信息
        sub_text = Text(
            sub_message,
            font_size=30,  # 原28
            color=WHITE
        )
        sub_text.next_to(main_text, DOWN, buff=0.8)
        
        # 动画
        self.play(Write(main_text), run_time=2)
        self.play(Write(sub_text), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(main_text), FadeOut(sub_text))
        
        # 下期预告
        self.show_next_episode_preview()
    
    def show_next_episode_preview(self):
        """下期预告"""
        # 预告标题
        preview_title = Text("下期预告", font_size=38, color=PROB_YELLOW)  # 原36
        preview_title.to_edge(UP)
        self.play(Write(preview_title))
        
        # EP15 内容预告
        ep15_title = Text(
            "第15集：随机漫步",
            font_size=TITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep15_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("醉汉能回家吗？", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("股价真的随机吗？", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("布朗运动的秘密", font_size=34, color=PROB_GREEN, weight=BOLD)  # 原32
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep15_title, DOWN, buff=0.8)
        
        self.play(Write(ep15_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "随机中有规律吗？",
            font_size=26,  # 原24
            color=PROB_YELLOW
        )
        think_question.next_to(preview_content, DOWN, buff=0.3)
        
        self.play(Write(think_question))
        self.wait(3)
        
        # 期待语
        see_you = Text(
            "下期见！",
            font_size=38,  # 原36
            color=WHITE
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title), FadeOut(ep15_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))