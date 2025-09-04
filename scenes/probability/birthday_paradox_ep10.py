"""
EP10: 生日悖论
巧合的必然性 - 组合数学的威力
"""

from manim import *
import numpy as np
import random
from typing import List, Dict, Tuple
from math import factorial, comb

# 概率系列颜色主题
PROB_PURPLE = "#8B5CF6"    # 主色：概率紫
PROB_GREEN = "#10B981"     # 成功绿
PROB_RED = "#EF4444"       # 失败红
PROB_BLUE = "#3B82F6"      # 数据蓝
PROB_YELLOW = "#F59E0B"    # 警告黄
PROB_GRAY = "#6B7280"      # 中性灰


class BirthdayParadoxEP10(Scene):
    """生日悖论 - 概率论系列 EP10"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(10, "生日悖论")
        
        # 2. 问题引入
        self.introduce_problem()
        
        # 3. 直觉分析
        self.analyze_intuition()
        
        # 4. 数学推导
        self.mathematical_derivation()
        
        # 5. 可视化验证
        self.visualization_verification()
        
        # 6. 概率曲线
        self.probability_curve()
        
        # 7. 应用拓展
        self.applications()
        
        # 8. 结尾
        self.show_ending()
    
    def show_series_intro(self, episode_num: int, episode_title: str):
        """显示系列介绍动画"""
        # 系列标题
        series_title = Text(
            "概率论的反直觉世界",
            font_size=48,
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 集数标题
        episode_text = Text(
            f"第{episode_num}集：{episode_title}",
            font_size=32,
            color=WHITE
        )
        episode_text.next_to(series_title, DOWN, buff=0.8)
        
        # 动画效果
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(series_title), FadeOut(episode_text))
    
    def introduce_problem(self):
        """引入生日问题"""
        # 场景设置
        title = Text("一个聚会的问题", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建人群图标（左侧）
        people = self.create_people_group(23)
        people.shift(LEFT * 3.5)
        
        # 问题文字（右侧）
        question = VGroup(
            Text("23个人的聚会", font_size=28, color=WHITE),
            Text("至少有两人生日相同", font_size=28, color=WHITE),
            Text("的概率是多少？", font_size=28, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.5)
        question.shift(RIGHT * 3.5)
        
        self.play(Create(people))
        self.play(Write(question))
        self.wait(2)
        
        # 三个选项
        options = VGroup(
            Text("A. 约 6%", font_size=24, color=WHITE),
            Text("B. 约 23%", font_size=24, color=WHITE),
            Text("C. 约 50%", font_size=24, color=WHITE),
            Text("D. 约 70%", font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        options.next_to(question, DOWN, buff=0.8)
        
        self.play(Write(options))
        self.wait(3)
        
        # 揭示答案
        answer_box = SurroundingRectangle(options[2], color=PROB_GREEN, stroke_width=3)
        answer_text = Text("正确答案：50.73%", font_size=32, color=PROB_GREEN)
        answer_text.next_to(options, DOWN, buff=0.5)
        
        self.play(Create(answer_box))
        self.play(Write(answer_text))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(people), FadeOut(question),
            FadeOut(options), FadeOut(answer_box), FadeOut(answer_text)
        )
    
    def create_people_group(self, n_people):
        """创建人群图标"""
        people = VGroup()
        
        # 计算布局
        cols = int(np.sqrt(n_people) + 1)
        rows = (n_people + cols - 1) // cols
        
        for i in range(n_people):
            row = i // cols
            col = i % cols
            
            # 简单的人形图标
            person = VGroup(
                Circle(radius=0.15, fill_color=PROB_BLUE, fill_opacity=0.8),
                Line(ORIGIN, DOWN * 0.3, stroke_width=2, color=PROB_BLUE),
            )
            
            x = (col - cols/2) * 0.5
            y = (rows/2 - row) * 0.7
            person.move_to([x, y, 0])
            
            people.add(person)
        
        people.scale(0.8)
        return people
    
    def analyze_intuition(self):
        """分析直觉误区"""
        title = Text("为什么直觉会出错？", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 直觉推理（右侧）
        intuition = VGroup(
            Text("直觉推理：", font_size=26, color=WHITE),
            Text("• 一年有365天", font_size=22, color=WHITE),
            Text("• 23人相对于365天很少", font_size=22, color=WHITE),
            Text("• 概率应该很小", font_size=22, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        intuition.shift(RIGHT * 3.5)
        
        # 错误标志（左侧）
        error_symbol = VGroup(
            Circle(radius=1, stroke_color=RED, stroke_width=8),
            Line(
                UP * 0.7 + LEFT * 0.7,
                DOWN * 0.7 + RIGHT * 0.7,
                stroke_color=RED,
                stroke_width=8
            )
        )
        error_symbol.shift(LEFT * 3.5)
        
        self.play(Write(intuition))
        self.play(Create(error_symbol))
        
        # 关键洞察
        key_insight = Text(
            "关键：不是特定某人，而是任意两人！",
            font_size=28,
            color=PROB_GREEN
        )
        key_insight.to_edge(DOWN).shift(UP * 0.5)
        
        self.play(Write(key_insight))
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(intuition),
            FadeOut(error_symbol), FadeOut(key_insight)
        )
    
    def mathematical_derivation(self):
        """严格的数学推导"""
        title = Text("数学推导", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 第一步：展示互补概率原理
        step1_title = Text("步骤1：使用互补概率", font_size=24, color=PROB_YELLOW)
        step1_title.to_edge(LEFT).shift(UP * 2)
        
        formula1 = MathTex(r"P(\text{match})", "=", r"1 - P(\text{all different})")
        formula1_cn = Text("P(至少两人相同) = 1 - P(所有人不同)", font_size=16, color=GRAY)
        formula1_group = VGroup(formula1, formula1_cn).arrange(DOWN, buff=0.2)
        formula1_group.next_to(step1_title, DOWN, buff=0.5).align_to(step1_title, LEFT)
        
        self.play(Write(step1_title))
        self.play(Write(formula1))
        self.play(FadeIn(formula1_cn))
        self.wait(2)
        
        # 第二步：计算所有人不同的概率
        step2_title = Text("步骤2：计算P(所有人不同)", font_size=24, color=PROB_YELLOW)
        step2_title.next_to(formula1_group, DOWN, buff=0.8).align_to(step1_title, LEFT)
        
        # 分两列显示：左边公式，右边解释
        formula2 = MathTex(
            r"P(\text{all different})", r"=", 
            r"\frac{365}{365}", r"\times", 
            r"\frac{364}{365}", r"\times", 
            r"\cdots", r"\times",
            r"\frac{365-n+1}{365}"
        )
        formula2.next_to(step2_title, DOWN, buff=0.3).align_to(step2_title, LEFT)
        
        # 解释放在公式右边
        explanations = VGroup(
            Text("第1人：365/365", font_size=18),
            Text("第2人：364/365", font_size=18),
            Text("第3人：363/365", font_size=18),
            Text("...", font_size=18),
            Text(f"第n人：(365-n+1)/365", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanations.next_to(formula2, RIGHT, buff=1.5)
        
        # 用箭头连接
        arrows = VGroup()
        for i, exp in enumerate(explanations[:-2]):
            if i < 3:
                arrow = Arrow(
                    formula2[2 + i*2].get_right(),
                    exp.get_left(),
                    buff=0.1,
                    stroke_width=2,
                    color=GRAY
                )
                arrows.add(arrow)
        
        self.play(Write(step2_title))
        self.play(Write(formula2))
        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            *[Write(exp) for exp in explanations]
        )
        self.wait(2)
        
        # 第三步：化简公式
        step3_title = Text("步骤3：化简为阶乘形式", font_size=24, color=PROB_YELLOW)
        step3_title.to_edge(RIGHT).shift(UP * 2)
        
        formula3 = MathTex(r"=", r"\frac{365!}{365^n \cdot (365-n)!}")
        formula3.next_to(step3_title, DOWN, buff=0.5)
        
        self.play(Write(step3_title))
        self.play(Write(formula3))
        self.wait(2)
        
        # 清理前三步，准备显示计算结果
        self.play(
            FadeOut(step1_title), FadeOut(formula1_group),
            FadeOut(step2_title), FadeOut(formula2), FadeOut(explanations), FadeOut(arrows),
            FadeOut(step3_title), FadeOut(formula3)
        )
        
        # 第四步：具体计算n=23
        result_title = Text("当 n = 23 时的计算结果", font_size=28, color=PROB_BLUE)
        result_title.shift(UP * 1.5)
        
        # 分两列展示结果
        left_results = VGroup(
            Text("计算过程：", font_size=22, color=WHITE),
            MathTex(r"P(\text{all different}) = \frac{365!}{365^{23} \cdot 342!}"),
            MathTex(r"= 0.493")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        left_results.shift(LEFT * 3.5)
        
        right_results = VGroup(
            Text("最终答案：", font_size=22, color=WHITE),
            MathTex(r"P(\text{match}) = 1 - 0.493"),
            MathTex(r"= 0.507 = ", r"50.7\%")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        right_results.shift(RIGHT * 3.5)
        
        # 中间的箭头
        result_arrow = Arrow(
            left_results.get_right(),
            right_results.get_left(),
            buff=0.5,
            color=PROB_GREEN,
            stroke_width=4
        )
        
        self.play(Write(result_title))
        self.play(Write(left_results))
        self.play(GrowArrow(result_arrow))
        self.play(Write(right_results))
        
        # 高亮最终结果
        highlight_box = SurroundingRectangle(
            right_results[2][1],
            color=PROB_GREEN,
            stroke_width=3
        )
        self.play(Create(highlight_box))
        self.play(right_results[2][1].animate.scale(1.2).set_color(PROB_GREEN))
        
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(result_title),
            FadeOut(left_results), FadeOut(right_results),
            FadeOut(result_arrow), FadeOut(highlight_box)
        )
    
    def visualization_verification(self):
        """可视化验证"""
        title = Text("直观理解：配对数量爆炸", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 第一部分：展示10人的配对
        section1_title = Text("以10人为例", font_size=24, color=PROB_YELLOW)
        section1_title.to_edge(LEFT).shift(UP * 2.5)
        self.play(Write(section1_title))
        
        # 创建人群 - 缩小规模，放在左上
        n_people = 10
        people = VGroup()
        positions = []
        
        # 更小的圆形排列
        radius = 1.5  # 缩小半径
        for i in range(n_people):
            angle = i * TAU / n_people
            pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
            positions.append(pos)
            
            person = Dot(pos, radius=0.1, color=PROB_BLUE)
            label = Text(str(i+1), font_size=14, color=WHITE)
            label.move_to(pos)
            
            people.add(VGroup(person, label))
        
        people.shift(LEFT * 4 + UP * 0.5)
        self.play(Create(people))
        
        # 配对数量公式 - 放在右上
        formula_title = Text("配对数量计算", font_size=24, color=PROB_YELLOW)
        formula_title.to_edge(RIGHT).shift(UP * 2.5).shift(LEFT * 0.5)
        
        pair_formula = VGroup(
            MathTex(r"C(n, 2) = \frac{n(n-1)}{2}"),
            Text("从n人中选2人的组合数", font_size=16, color=GRAY)
        ).arrange(DOWN, buff=0.2)
        pair_formula.next_to(formula_title, DOWN, buff=0.3)
        
        self.play(Write(formula_title))
        self.play(Write(pair_formula))
        
        # 具体计算 - 分两个例子展示
        calc_10 = VGroup(
            Text("n = 10:", font_size=20, color=PROB_BLUE),
            MathTex(r"C(10, 2) = \frac{10 \times 9}{2} = 45")
        ).arrange(RIGHT, buff=0.3)
        calc_10.next_to(pair_formula, DOWN, buff=0.5)
        
        calc_23 = VGroup(
            Text("n = 23:", font_size=20, color=PROB_GREEN),
            MathTex(r"C(23, 2) = \frac{23 \times 22}{2} = 253")
        ).arrange(RIGHT, buff=0.3)
        calc_23.next_to(calc_10, DOWN, buff=0.3)
        
        self.play(Write(calc_10))
        self.play(Write(calc_23))
        
        # 动画显示部分连线 - 只显示几条示例
        lines = VGroup()
        line_examples = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5)]  # 只显示5条线
        
        for i, j in line_examples:
            line = Line(
                positions[i] + LEFT * 4 + UP * 0.5,
                positions[j] + LEFT * 4 + UP * 0.5,
                stroke_color=PROB_YELLOW,
                stroke_width=2,
                stroke_opacity=0.7
            )
            lines.add(line)
        
        self.play(*[Create(line) for line in lines], run_time=1)
        
        # 添加省略号表示还有更多连线
        more_text = Text("... 共45条连线", font_size=18, color=PROB_YELLOW)
        more_text.next_to(people, DOWN, buff=0.5)
        self.play(Write(more_text))
        
        # 第二部分：对比展示
        self.wait(2)
        
        # 清理上半部分，准备对比
        compare_title = Text("关键对比", font_size=28, color=PROB_GREEN)
        compare_title.shift(UP * 1.5)
        
        # 创建对比表格
        compare_data = VGroup(
            # 标题行
            VGroup(
                Text("人数", font_size=22, color=WHITE),
                Text("配对数", font_size=22, color=WHITE),
                Text("vs 365天", font_size=22, color=WHITE)
            ).arrange(RIGHT, buff=2),
            
            # 数据行
            VGroup(
                Text("10", font_size=20),
                Text("45", font_size=20, color=PROB_YELLOW),
                Text("12.3%", font_size=20, color=PROB_RED)
            ).arrange(RIGHT, buff=2),
            
            VGroup(
                Text("23", font_size=20),
                Text("253", font_size=20, color=PROB_YELLOW),
                Text("69.3%", font_size=20, color=PROB_GREEN)
            ).arrange(RIGHT, buff=2),
            
            VGroup(
                Text("50", font_size=20),
                Text("1225", font_size=20, color=PROB_YELLOW),
                Text("335.6%", font_size=20, color=PROB_GREEN)
            ).arrange(RIGHT, buff=2)
        ).arrange(DOWN, buff=0.5)
        compare_data.shift(DOWN * 0.5)
        
        # 添加边框
        for row in compare_data:
            for i, cell in enumerate(row):
                cell.move_to(compare_data[0][i].get_center() + 
                           (row.get_center()[1] - compare_data[0].get_center()[1]) * UP)
        
        # 清理并显示对比
        self.play(
            FadeOut(section1_title), FadeOut(people), FadeOut(lines), FadeOut(more_text),
            FadeOut(formula_title), FadeOut(pair_formula), FadeOut(calc_10), FadeOut(calc_23),
            Write(compare_title)
        )
        self.play(Write(compare_data))
        
        # 强调关键数字
        emphasis_box = SurroundingRectangle(
            compare_data[2][1],  # 253这个数字
            color=PROB_GREEN,
            stroke_width=3
        )
        emphasis_text = Text(
            "253次机会 >> 23人",
            font_size=26,
            color=PROB_GREEN
        )
        emphasis_text.to_edge(DOWN).shift(UP * 0.5)
        
        self.play(Create(emphasis_box))
        self.play(Write(emphasis_text))
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(compare_title), FadeOut(compare_data),
            FadeOut(emphasis_box), FadeOut(emphasis_text)
        )
    
    def probability_curve(self):
        """概率曲线展示"""
        title = Text("概率随人数变化", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建坐标轴
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 1, 0.1],
            x_length=8,
            y_length=5,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": range(0, 101, 10),
                "label_direction": DOWN,
            },
            y_axis_config={
                "numbers_to_include": [0, 0.5, 1],
                "decimal_number_config": {"num_decimal_places": 1},
            }
        )
        axes.shift(DOWN * 0.5)
        
        # 轴标签
        x_label = Text("人数", font_size=20)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("概率", font_size=20)
        y_label.rotate(PI/2)
        y_label.next_to(axes.y_axis, LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 绘制概率曲线
        def birthday_prob(n):
            """计算n个人中至少两人生日相同的概率"""
            if n > 365:
                return 1.0
            prob_all_different = 1.0
            for i in range(n):
                prob_all_different *= (365 - i) / 365
            return 1 - prob_all_different
        
        # 创建曲线
        x_vals = range(0, 101)
        y_vals = [birthday_prob(n) for n in x_vals]
        
        curve_points = [axes.coords_to_point(x, y) for x, y in zip(x_vals, y_vals)]
        curve = VMobject()
        curve.set_points_smoothly(curve_points)
        curve.set_stroke(color=PROB_PURPLE, width=3)
        
        self.play(Create(curve))
        
        # 标记关键点
        key_points = [
            (23, birthday_prob(23), "23人: 50.7%"),
            (50, birthday_prob(50), "50人: 97.0%"),
            (70, birthday_prob(70), "70人: 99.9%")
        ]
        
        for n, prob, label_text in key_points:
            point = axes.coords_to_point(n, prob)
            dot = Dot(point, radius=0.08, color=PROB_YELLOW)
            label = Text(label_text, font_size=16, color=PROB_YELLOW)
            label.next_to(dot, UR, buff=0.1)
            
            self.play(Create(dot), Write(label))
        
        # 添加50%参考线
        half_line = DashedLine(
            axes.coords_to_point(0, 0.5),
            axes.coords_to_point(100, 0.5),
            color=GRAY,
            stroke_width=2
        )
        self.play(Create(half_line))
        
        # 洞察文字
        insight = Text(
            "仅需23人就能达到50%！",
            font_size=28,
            color=PROB_GREEN
        )
        insight.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(insight))
        
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(curve), FadeOut(half_line), FadeOut(insight),
            *[FadeOut(mob) for mob in self.mobjects if isinstance(mob, (Dot, Text)) and mob not in [title, x_label, y_label, insight]]
        )
    
    def applications(self):
        """实际应用"""
        title = Text("生日悖论的应用", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 应用场景
        applications = VGroup(
            VGroup(
                Text("密码学：生日攻击", font_size=28, color=PROB_BLUE),
                Text("哈希碰撞的概率分析", font_size=20, color=WHITE),
                Text("n位哈希：约需2^(n/2)次尝试", font_size=18, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            
            VGroup(
                Text("DNA指纹识别", font_size=28, color=PROB_GREEN),
                Text("评估匹配的可靠性", font_size=20, color=WHITE),
                Text("需要足够多的位点避免巧合", font_size=18, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2),
            
            VGroup(
                Text("数据去重", font_size=28, color=PROB_YELLOW),
                Text("预估重复记录的概率", font_size=20, color=WHITE),
                Text("优化存储和索引策略", font_size=18, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        ).arrange(DOWN, buff=0.8)
        applications.shift(DOWN * 0.5)
        
        for i, app in enumerate(applications):
            self.play(Write(app[0]))
            self.play(FadeIn(app[1], shift=UP))
            self.play(FadeIn(app[2], shift=UP))
            self.wait(1)
        
        self.wait(2)
        
        self.play(FadeOut(title), FadeOut(applications))
    
    def show_ending(self):
        """结尾"""
        # 核心总结
        summary = VGroup(
            Text("生日悖论告诉我们：", font_size=36, color=WHITE),
            Text("巧合比想象中更常见", font_size=42, color=PROB_PURPLE, weight=BOLD),
            Text("组合爆炸的威力", font_size=32, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 系列结尾
        self.show_series_ending(
            "小概率事件",
            "在足够多的机会下必然发生"
        )
    
    def show_series_ending(self, main_message: str, sub_message: str):
        """显示系列结尾动画"""
        # 主信息
        main_text = Text(
            main_message,
            font_size=48,
            color=PROB_PURPLE,
            weight=BOLD
        )
        
        # 副信息
        sub_text = Text(
            sub_message,
            font_size=28,
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
        preview_title = Text("下期预告", font_size=36, color=PROB_YELLOW)
        preview_title.to_edge(UP)
        self.play(Write(preview_title))
        
        # EP11 内容预告
        ep11_title = Text(
            "第11集：赌徒谬误",
            font_size=42,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep11_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("连续10次正面之后", font_size=28, color=WHITE),
            Text("下一次是反面的概率", font_size=28, color=WHITE),
            Text("真的会更大吗？", font_size=32, color=PROB_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep11_title, DOWN, buff=0.8)
        
        self.play(Write(ep11_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "硬币有记忆吗？",
            font_size=24,
            color=PROB_YELLOW
        )
        think_question.next_to(preview_content, DOWN, buff=0.3)
        
        self.play(Write(think_question))
        self.wait(3)
        
        # 期待语
        see_you = Text(
            "下期见！",
            font_size=36,
            color=WHITE
        )
        see_you.move_to(ORIGIN)
        
        self.play(
            FadeOut(preview_title), FadeOut(ep11_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))