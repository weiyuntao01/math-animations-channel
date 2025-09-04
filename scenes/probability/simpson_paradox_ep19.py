"""
EP19: 辛普森悖论
数据会撒谎 - 统计中最反直觉的陷阱
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

# 字体大小调整
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class SimpsonParadoxEP19(Scene):
    """辛普森悖论 - 概率论系列 EP19（特别篇）"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(19, "辛普森悖论")
        
        # 2. 震撼引入 - 药物实验悖论
        self.introduce_medical_paradox()
        
        # 3. 伯克利大学录取案例
        self.berkeley_admission_case()
        
        # 4. 数学原理解释
        self.mathematical_explanation()
        
        # 5. 棒球打击率悖论
        self.baseball_batting_average()
        
        # 6. 可视化本质
        self.visualize_the_essence()
        
        # 7. 现实世界的陷阱
        self.real_world_traps()
        
        # 8. 如何避免被误导
        self.how_to_avoid_misleading()
        
        # 9. 结尾
        self.show_ending()
    
    def show_series_intro(self, episode_num: int, episode_title: str):
        """显示系列介绍动画"""
        # 系列标题
        series_title = Text(
            "概率论的反直觉世界",
            font_size=50,
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 特别篇标记
        special_mark = Text(
            "【特别篇】",
            font_size=28,
            color=PROB_YELLOW
        )
        special_mark.next_to(series_title, UP, buff=0.3)
        
        # 集数标题
        episode_text = Text(
            f"第{episode_num}集：{episode_title}",
            font_size=34,
            color=WHITE
        )
        episode_text.next_to(series_title, DOWN, buff=0.8)
        
        # 动画效果
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(special_mark, shift=DOWN), run_time=1)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(series_title), FadeOut(special_mark), FadeOut(episode_text))
    
    def introduce_medical_paradox(self):
        """引入药物实验悖论"""
        self.clear()
        
        title = Text("一个致命的统计陷阱", font_size=TITLE_SIZE, color=PROB_RED)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 场景设置
        scenario = VGroup(
            Text("新药测试结果：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("总体看：新药效果更差", font_size=NORMAL_SIZE),
            Text("分组看：新药在每组都更好", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.5)
        scenario.move_to(ORIGIN + UP * 0.5)
        
        for line in scenario:
            self.play(Write(line), run_time=0.8)
        
        # 困惑的问号
        question = Text(
            "这怎么可能？！",
            font_size=SUBTITLE_SIZE,
            color=PROB_RED,
            weight=BOLD
        )
        question.move_to(DOWN * 2)
        self.play(Write(question), question.animate.scale(1.2))
        
        self.wait(2)
        
        # 揭示
        reveal = Text(
            "欢迎来到辛普森悖论的世界",
            font_size=SUBTITLE_SIZE,
            color=PROB_PURPLE
        )
        reveal.move_to(DOWN * 2)
        self.play(Transform(question, reveal))
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(scenario), FadeOut(question))
    
    def berkeley_admission_case(self):
        """伯克利大学录取案例"""
        self.clear()
        
        title = Text("1973年伯克利大学性别歧视案", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 第一部分：总体数据
        self.show_overall_data()
        
        # 第二部分：分院系数据
        self.show_department_data()
        
        # 第三部分：悖论解释
        self.explain_berkeley_paradox()
        
        self.wait(2)
        self.play(FadeOut(title))
    
    def show_overall_data(self):
        """展示总体数据"""
        # 总体录取率标题
        overall_title = Text("总体录取率", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        overall_title.move_to(UP * 2.5)
        self.play(Write(overall_title))
        
        # 创建条形图
        male_bar = self.create_percentage_bar("男性", 44, PROB_BLUE, LEFT * 2 + ORIGIN)
        female_bar = self.create_percentage_bar("女性", 35, PROB_RED, RIGHT * 2 + ORIGIN)
        
        self.play(Create(male_bar), Create(female_bar))
        
        # 结论
        conclusion = Text(
            "看起来存在性别歧视！",
            font_size=NORMAL_SIZE,
            color=PROB_RED,
            weight=BOLD
        )
        conclusion.move_to(DOWN * 2.5)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(FadeOut(overall_title), FadeOut(male_bar), 
                 FadeOut(female_bar), FadeOut(conclusion))
    
    def create_percentage_bar(self, label: str, percentage: float, color, position):
        """创建百分比条形图"""
        bar_group = VGroup()
        
        # 标签
        label_text = Text(label, font_size=NORMAL_SIZE)
        label_text.move_to(position + UP * 1.5)
        
        # 条形
        bar = Rectangle(
            width=1.5,
            height=percentage * 0.03,
            fill_color=color,
            fill_opacity=0.7,
            stroke_color=color,
            stroke_width=2
        )
        bar.move_to(position)
        
        # 百分比
        percent_text = Text(f"{percentage}%", font_size=NORMAL_SIZE, color=color)
        percent_text.next_to(bar, UP, buff=0.2)
        
        bar_group.add(label_text, bar, percent_text)
        return bar_group
    
    def show_department_data(self):
        """展示分院系数据"""
        dept_title = Text("分院系录取率", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        dept_title.move_to(UP * 2)
        self.play(Write(dept_title))
        
        # 院系数据
        departments = [
            ("A系", 62, 82, 825, 108),
            ("B系", 63, 68, 560, 25),
            ("C系", 37, 34, 325, 593),
            ("D系", 33, 35, 417, 375),
            ("E系", 28, 24, 191, 393),
            ("F系", 6, 7, 373, 341)
        ]
        
        # 创建表格
        table = self.create_department_table(departments)
        table.move_to(ORIGIN)
        self.play(Create(table))
        
        # 重要发现
        finding = Text(
            "女性在4个系录取率更高！",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        finding.move_to(DOWN * 2)
        self.play(Write(finding))
        
        self.wait(3)
        self.play(FadeOut(dept_title), FadeOut(table), FadeOut(finding))
    
    def create_department_table(self, departments):
        """创建院系数据表格"""
        table = VGroup()
        
        # 表头
        headers = ["院系", "男性", "女性", "优势"]
        header_row = VGroup()
        for i, header in enumerate(headers):
            cell = Text(header, font_size=SMALL_SIZE, color=PROB_YELLOW)
            cell.move_to(LEFT * 3 + RIGHT * i * 2 + UP * 2)
            header_row.add(cell)
        table.add(header_row)
        
        # 数据行
        for j, (dept, male_rate, female_rate, male_n, female_n) in enumerate(departments):
            row = VGroup()
            
            # 院系名
            dept_cell = Text(dept, font_size=SMALL_SIZE)
            dept_cell.move_to(LEFT * 3 + UP * (1.5 - j * 0.5))
            
            # 男性录取率
            male_cell = Text(f"{male_rate}%", font_size=SMALL_SIZE, color=PROB_BLUE)
            male_cell.move_to(LEFT * 1 + UP * (1.5 - j * 0.5))
            
            # 女性录取率
            female_cell = Text(f"{female_rate}%", font_size=SMALL_SIZE, color=PROB_RED)
            female_cell.move_to(RIGHT * 1 + UP * (1.5 - j * 0.5))
            
            # 优势标记
            if female_rate > male_rate:
                advantage = Text("女↑", font_size=SMALL_SIZE, color=PROB_GREEN)
            else:
                advantage = Text("男↑", font_size=SMALL_SIZE, color=PROB_BLUE)
            advantage.move_to(RIGHT * 3 + UP * (1.5 - j * 0.5))
            
            row.add(dept_cell, male_cell, female_cell, advantage)
            table.add(row)
        
        return table
    
    def explain_berkeley_paradox(self):
        """解释伯克利悖论"""
        explanation_title = Text("悖论的关键：申请分布不同", font_size=SUBTITLE_SIZE, color=PROB_PURPLE)
        explanation_title.move_to(UP * 2) 
        self.play(Write(explanation_title))
        
        # 关键洞察
        insights = VGroup(
            Text("女性更多申请竞争激烈的院系", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("男性更多申请容易录取的院系", font_size=NORMAL_SIZE, color=PROB_BLUE),
            Text("↓", font_size=TITLE_SIZE, color=PROB_YELLOW),
            Text("总体数据产生误导！", font_size=SUBTITLE_SIZE, color=PROB_PURPLE, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        insights.move_to(ORIGIN)
        
        for insight in insights:
            self.play(Write(insight), run_time=0.7)
        
        self.wait(2)
        self.play(FadeOut(explanation_title), FadeOut(insights))
    
    def mathematical_explanation(self):
        """数学原理解释 - 使用正确的数学例子"""
        self.clear()
        
        title = Text("辛普森悖论的数学本质", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 关键概念
        key_concept = Text(
            "加权平均的陷阱",
            font_size=SUBTITLE_SIZE,
            color=PROB_YELLOW
        )
        key_concept.move_to(UP * 2)
        self.play(Write(key_concept))
        
        # 数学原理
        principle = VGroup(
            Text("即使在每个分组中 A > B", font_size=NORMAL_SIZE),
            Text("合并后可能出现 A < B", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("原因：不同分组的权重不同", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.3)
        principle.move_to(ORIGIN + UP * 0.5)
        
        for line in principle:
            self.play(Write(line), run_time=0.7)
        
        # 数学表达式 - 避免在MathTex中使用中文
        math_formula = VGroup(
            Text("总体比率 = Σ(权重 × 分组比率)", font_size=NORMAL_SIZE),
            Text("其中权重决定了各组的影响力", font_size=SMALL_SIZE, color=PROB_GRAY)
        ).arrange(DOWN, buff=0.2)
        math_formula.move_to(DOWN * 1.5)
        
        self.play(Write(math_formula))
        
        self.wait(2)
        
        # 转到具体例子
        self.play(FadeOut(key_concept), FadeOut(principle), FadeOut(math_formula))
        
        # 展示一个简单但正确的数值例子
        self.show_correct_numerical_example()
    
    def show_correct_numerical_example(self):
        """展示正确的数值例子"""
        simple_example_title = Text("具体数值例子", font_size=SUBTITLE_SIZE, color=PROB_YELLOW)
        simple_example_title.move_to(UP * 2)
        self.play(Write(simple_example_title))
        
        # 创建一个医疗例子的表格 - 使用Text而不是MathTex
        example = VGroup(
            Text("治疗成功率比较", font_size=NORMAL_SIZE, color=WHITE),
            Text("─" * 40, font_size=SMALL_SIZE, color=PROB_GRAY),
            Text("轻症患者组：", font_size=SMALL_SIZE, color=PROB_BLUE),
            Text("新药: 81/87 = 93.1% > 旧药: 234/270 = 86.7%", font_size=18),
            Text("重症患者组：", font_size=SMALL_SIZE, color=PROB_RED),
            Text("新药: 192/263 = 73.0% > 旧药: 55/80 = 68.8%", font_size=18),
            Text("─" * 40, font_size=SMALL_SIZE, color=PROB_GRAY),
            Text("总体结果：", font_size=SMALL_SIZE, color=PROB_YELLOW),
            Text("新药: 273/350 = 78.0% < 旧药: 289/350 = 82.6%", font_size=18)
        ).arrange(DOWN, buff=0.25)
        example.move_to(ORIGIN + DOWN * 0.3)
        
        # 逐行显示
        for i, line in enumerate(example):
            if i == len(example) - 1:  # 最后一行用红色强调
                line.set_color(PROB_RED)
                self.play(Write(line), line.animate.scale(1.1), run_time=0.8)
            else:
                self.play(Write(line), run_time=0.5)
        
        # 解释原因
        explanation = Text(
            "关键：新药组有75%是重症患者，旧药组只有23%！",
            font_size=20,
            color=PROB_GREEN,
            weight=BOLD
        )
        explanation.to_edge(DOWN, buff=0.3)
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(FadeOut(simple_example_title), FadeOut(example), FadeOut(explanation))
    
    def baseball_batting_average(self):
        """棒球打击率悖论 - 使用正确展示悖论的例子"""
        self.clear()
        
        title = Text("体育案例：打击率悖论", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 设计一个清晰展示辛普森悖论的例子
        baseball_data = VGroup(
            Text("球员A vs 球员B 两个赛季对比", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("─" * 35, font_size=SMALL_SIZE, color=PROB_GRAY),
            Text("上半赛季（少量比赛）：", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("球员A: 12/20 = .600", font_size=SMALL_SIZE, color=PROB_GREEN),
            Text("球员B: 4/10 = .400", font_size=SMALL_SIZE),
            Text("下半赛季（大量比赛）：", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("球员A: 60/180 = .333", font_size=SMALL_SIZE, color=PROB_GREEN),
            Text("球员B: 78/240 = .325", font_size=SMALL_SIZE),
            Text("─" * 35, font_size=SMALL_SIZE, color=PROB_GRAY),
            Text("整个赛季：", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("球员A: 72/200 = .360", font_size=SMALL_SIZE),
            Text("球员B: 82/250 = .328", font_size=SMALL_SIZE, color=PROB_RED)
        ).arrange(DOWN, buff=0.25)
        baseball_data.move_to(ORIGIN)
        
        # 验证数学：
        # A总计：12+60=72, 20+180=200, 72/200=0.36 ✓
        # B总计：4+78=82, 10+240=250, 82/250=0.328 ✓
        # 上半：0.6 > 0.4 ✓
        # 下半：0.333 > 0.325 ✓
        # 总体：0.36 > 0.328 ✗ 这不是悖论！
        
        # 重新设计正确的例子
        baseball_data = VGroup(
            Text("球员甲 vs 球员乙 两个时期对比", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("─" * 35, font_size=SMALL_SIZE, color=PROB_GRAY),
            Text("对弱队（少场次）：", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("球员甲: 10/10 = 1.000", font_size=SMALL_SIZE, color=PROB_GREEN),
            Text("球员乙: 90/100 = .900", font_size=SMALL_SIZE),
            Text("对强队（多场次）：", font_size=NORMAL_SIZE, color=PROB_YELLOW),
            Text("球员甲: 30/90 = .333", font_size=SMALL_SIZE, color=PROB_GREEN),
            Text("球员乙: 10/100 = .100", font_size=SMALL_SIZE),
            Text("─" * 35, font_size=SMALL_SIZE, color=PROB_GRAY),
            Text("整个赛季：", font_size=NORMAL_SIZE, color=PROB_RED),
            Text("球员甲: 40/100 = .400", font_size=SMALL_SIZE),
            Text("球员乙: 100/200 = .500", font_size=SMALL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.25)
        baseball_data.move_to(ORIGIN)
        
        # 验证：
        # 甲总计：10+30=40, 10+90=100, 40/100=0.4 ✓
        # 乙总计：90+10=100, 100+100=200, 100/200=0.5 ✓
        # 对弱队：1.0 > 0.9 ✓
        # 对强队：0.333 > 0.1 ✓
        # 总体：0.4 < 0.5 ✓ 这是正确的悖论！
        
        # 逐行显示，强调反转
        for i, line in enumerate(baseball_data):
            if i in [3, 6]:  # 甲单项领先的行
                self.play(Write(line), line.animate.set_color(PROB_BLUE), run_time=0.6)
            elif i == 11:  # 乙总体领先
                self.play(Write(line), line.animate.scale(1.15), run_time=0.8)
            else:
                self.play(Write(line), run_time=0.5)
        
        # 解释原因
        explanation = Text(
            "关键：甲主要对强队，乙主要对弱队！",
            font_size=NORMAL_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        explanation.to_edge(DOWN, buff=0.5)
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(baseball_data), FadeOut(explanation))
    
    def visualize_the_essence(self):
        """可视化本质"""
        self.clear()
        
        title = Text("辛普森悖论的几何直观", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=5,
            y_length=5,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "font_size": 14
            }
        )
        axes.move_to(ORIGIN + DOWN * 0.3)
        
        x_label = Text("申请人数", font_size=16).next_to(axes.x_axis, DOWN, buff=0.3)
        y_label = Text("录取人数", font_size=16).next_to(axes.y_axis, LEFT, buff=0.3).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 绘制两组数据点
        # 组1：男性（更多申请容易的系）
        male_points = [
            (2, 1.6, "A系"),  # 高录取率系但人少
            (7, 2.1, "C系")   # 低录取率系但人多
        ]
        
        # 组2：女性（更多申请困难的系）
        female_points = [
            (1, 0.8, "A系"),  # 高录取率系但人很少
            (8, 2.4, "C系")   # 低录取率系但人很多
        ]
        
        # 绘制点
        male_dots = VGroup()
        for x, y, label in male_points:
            dot = Dot(axes.c2p(x, y), color=PROB_BLUE, radius=0.08)
            label_text = Text(label, font_size=12, color=PROB_BLUE)
            label_text.next_to(dot, UR, buff=0.1)
            male_dots.add(dot, label_text)
        
        female_dots = VGroup()
        for x, y, label in female_points:
            dot = Dot(axes.c2p(x, y), color=PROB_RED, radius=0.08)
            label_text = Text(label, font_size=12, color=PROB_RED)
            label_text.next_to(dot, UR, buff=0.1)
            female_dots.add(dot, label_text)
        
        self.play(Create(male_dots), Create(female_dots))
        
        # 绘制总体斜率线
        male_total = (9, 3.7)  # 总申请和总录取
        female_total = (9, 3.2)  # 总申请和总录取
        
        male_line = Line(
            axes.c2p(0, 0),
            axes.c2p(*male_total),
            color=PROB_BLUE,
            stroke_width=2
        )
        
        female_line = Line(
            axes.c2p(0, 0),
            axes.c2p(*female_total),
            color=PROB_RED,
            stroke_width=2
        )
        
        # 显示斜率
        male_slope_text = Text(f"男性总体: {3.7/9:.1%}", font_size=14, color=PROB_BLUE)
        male_slope_text.next_to(male_line.get_end(), RIGHT, buff=0.1)
        
        female_slope_text = Text(f"女性总体: {3.2/9:.1%}", font_size=14, color=PROB_RED)
        female_slope_text.next_to(female_line.get_end(), RIGHT, buff=0.1)
        
        self.play(Create(male_line), Create(female_line))
        self.play(Write(male_slope_text), Write(female_slope_text))
        
        # 说明
        explanation = Text(
            "各系内女性录取率更高，但总体更低！",
            font_size=NORMAL_SIZE,
            color=PROB_YELLOW,
            weight=BOLD
        )
        explanation.move_to(DOWN * 3.5)
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
                 FadeOut(male_dots), FadeOut(female_dots), 
                 FadeOut(male_line), FadeOut(female_line),
                 FadeOut(male_slope_text), FadeOut(female_slope_text),
                 FadeOut(explanation))
    
    def real_world_traps(self):
        """现实世界的陷阱"""
        self.clear()
        
        title = Text("辛普森悖论无处不在", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建应用场景
        applications = VGroup()
        
        # 1. 医疗
        medical = self.create_trap_card(
            "医疗研究",
            PROB_RED,
            ["药物效果评估", "治疗方案比较", "疫苗有效性"]
        )
        medical.move_to(LEFT * 4 + UP * 0.3)
        
        # 2. 教育
        education = self.create_trap_card(
            "教育评估",
            PROB_BLUE,
            ["学校排名", "教学方法效果", "标准化考试"]
        )
        education.move_to(ORIGIN + UP * 0.3)
        
        # 3. 商业
        business = self.create_trap_card(
            "商业决策",
            PROB_GREEN,
            ["市场营销效果", "产品质量分析", "客户满意度"]
        )
        business.move_to(RIGHT * 4 + UP * 0.3)
        
        applications.add(medical, education, business)
        
        for app in applications:
            self.play(FadeIn(app, shift=UP * 0.5), run_time=0.5)
        
        # 警告
        warning = Text(
            "⚠️ 数据分组可能完全改变结论！",
            font_size=SUBTITLE_SIZE,
            color=PROB_YELLOW,
            weight=BOLD
        )
        warning.to_edge(DOWN, buff=0.5)
        self.play(Write(warning))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(applications), FadeOut(warning))
    
    def create_trap_card(self, title: str, color, examples: List[str]):
        """创建陷阱卡片"""
        card = VGroup()
        
        # 背景
        bg = RoundedRectangle(
            width=2.5, height=2.5,
            corner_radius=0.2,
            fill_color=color,
            fill_opacity=0.2,
            stroke_color=color,
            stroke_width=2
        )
        
        # 标题
        title_text = Text(title, font_size=20, color=color, weight=BOLD)
        title_text.move_to(bg.get_top() + DOWN * 0.4)
        
        # 例子
        examples_text = VGroup()
        for example in examples:
            ex_text = Text(f"• {example}", font_size=14, color=WHITE)
            examples_text.add(ex_text)
        examples_text.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        examples_text.move_to(bg.get_center() + DOWN * 0.2)
        
        card.add(bg, title_text, examples_text)
        return card
    
    def how_to_avoid_misleading(self):
        """如何避免被误导"""
        self.clear()
        
        title = Text("如何识破辛普森悖论？", font_size=TITLE_SIZE, color=PROB_PURPLE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 防范策略
        strategies = VGroup(
            Text("🔍 策略一：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("始终查看分组数据", font_size=NORMAL_SIZE),
            Text("🎯 策略二：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("理解因果关系，而非只看相关性", font_size=NORMAL_SIZE),
            Text("⚖️ 策略三：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("考虑权重和样本分布", font_size=NORMAL_SIZE),
            Text("📊 策略四：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("使用标准化和加权平均", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        strategies.move_to(ORIGIN + UP * 0.3)
        
        for i in range(0, 8, 2):
            self.play(
                Write(strategies[i]),
                Write(strategies[i+1]),
                run_time=0.8
            )
        
        # 核心原则
        principle = Text(
            "记住：整体 ≠ 部分之和",
            font_size=SUBTITLE_SIZE,
            color=PROB_GREEN,
            weight=BOLD
        )
        principle.to_edge(DOWN, buff=0.5)
        self.play(Write(principle))
        
        self.wait(3)
        self.play(FadeOut(title), FadeOut(strategies), FadeOut(principle))
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        # 核心总结
        summary = VGroup(
            Text("辛普森悖论告诉我们：", font_size=36, color=WHITE),
            Text("数据不会说谎", font_size=TITLE_SIZE, color=PROB_BLUE),
            Text("但会误导", font_size=TITLE_SIZE, color=PROB_RED, weight=BOLD),
            Text("关键在于如何解读", font_size=32, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.4)
        summary.move_to(ORIGIN)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.play(Write(summary[3]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 三个要点
        key_points = VGroup(
            Text("记住三点：", font_size=SUBTITLE_SIZE, color=PROB_YELLOW),
            Text("1. 总体趋势可能与分组相反", font_size=NORMAL_SIZE),
            Text("2. 权重和分布决定一切", font_size=NORMAL_SIZE),
            Text("3. 深入分析，不要被表象欺骗", font_size=NORMAL_SIZE, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.35)
        key_points.move_to(ORIGIN)
        
        for point in key_points:
            self.play(Write(point), run_time=0.8)
        
        self.wait(3)
        self.play(FadeOut(key_points))
        
        # 系列结尾
        self.show_series_ending(
            "批判性思维",
            "让数据为你服务，而非相反"
        )
    
    def show_series_ending(self, main_message: str, sub_message: str):
        """显示系列结尾动画"""
        # 主信息
        main_text = Text(
            main_message,
            font_size=50,
            color=PROB_PURPLE,
            weight=BOLD
        )
        main_text.move_to(ORIGIN + UP * 0.5)
        
        # 副信息
        sub_text = Text(
            sub_message,
            font_size=30,
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
        preview_title = Text("下期预告", font_size=38, color=PROB_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))
        
        # EP20 内容预告
        ep20_title = Text(
            "第20集：本福特定律",
            font_size=TITLE_SIZE,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep20_title.move_to(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("为什么1开头的数字最多？", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("自然界的数字密码", font_size=SUBTITLE_SIZE, color=WHITE),
            Text("识破财务造假的利器", font_size=32, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.35)
        preview_content.next_to(ep20_title, DOWN, buff=0.6)
        
        self.play(Write(ep20_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "你的银行账单符合本福特定律吗？",
            font_size=24,
            color=PROB_YELLOW
        )
        think_question.to_edge(DOWN, buff=0.5)
        
        self.play(Write(think_question))
        self.wait(3)
        
        # 期待语
        see_you = Text(
            "下期见！",
            font_size=38,
            color=WHITE
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title), FadeOut(ep20_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))