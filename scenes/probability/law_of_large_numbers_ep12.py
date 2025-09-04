"""
EP12: 大数定律
为什么赌场永远是赢家？
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


class LawOfLargeNumbersEP12(Scene):
    """大数定律 - 概率论系列 EP12"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(12, "大数定律")
        
        # 2. 问题引入 - 赌场的秘密
        self.introduce_casino_secret()
        
        # 3. 直觉 vs 真相
        self.analyze_intuition_vs_truth()
        
        # 4. 大数定律的数学证明
        self.mathematical_proof()
        
        # 5. 硬币投掷实验
        self.coin_flip_experiment()
        
        # 6. 赌场盈利模型
        self.casino_profit_model()
        
        # 7. 现实应用
        self.real_world_applications()
        
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
    
    def introduce_casino_secret(self):
        """引入问题 - 赌场的秘密"""
        title = Text("赌场的终极秘密", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建赌场场景（左侧）
        casino_scene = self.create_casino_scene()
        casino_scene.shift(LEFT * 3.5)
        self.play(FadeIn(casino_scene))
        
        # 金钱流动动画（右侧）
        money_flow = VGroup()
        for i in range(5):
            arrow = Arrow(
                LEFT * 1.5 + UP * (i - 2) * 0.5,
                RIGHT * 1.5 + UP * 0.2,
                color=PROB_GREEN,
                stroke_width=3
            )
            dollar = Text("$", color=PROB_GREEN, font_size=24)
            dollar.move_to(arrow.get_start())
            money_flow.add(arrow, dollar)
        
        # 显示金钱流向
        for i in range(0, len(money_flow), 2):
            self.play(
                Create(money_flow[i]),
                money_flow[i+1].animate.move_to(money_flow[i].get_end()),
                run_time=0.5
            )
        
        # 核心问题
        question = VGroup(
            Text("为什么赌场", font_size=36, color=WHITE),
            Text("永远是赢家？", font_size=36, color=PROB_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        question.shift(DOWN * 2)
        
        self.play(Write(question))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(casino_scene),
            FadeOut(money_flow), FadeOut(question)
        )
    
    def create_casino_scene(self):
        """创建赌场场景"""
        scene = VGroup()
        
        # 建筑轮廓
        building = Rectangle(
            width=4, height=3,
            fill_color=DARK_BROWN,
            fill_opacity=0.8,
            stroke_color=GOLD
        )
        
        # 霓虹灯招牌
        sign_bg = Rectangle(
            width=3, height=0.8,
            fill_color=PROB_RED,
            fill_opacity=0.9
        )
        sign_text = Text("CASINO", font_size=24, color=YELLOW, weight=BOLD)
        sign = VGroup(sign_bg, sign_text)
        sign.shift(UP * 1.5)
        
        # 装饰灯
        lights = VGroup()
        for i in range(5):
            light = Dot(
                radius=0.1,
                color=YELLOW,
                fill_opacity=0.8
            )
            light.shift(LEFT * 1.5 + RIGHT * i * 0.75 + DOWN * 1.2)
            lights.add(light)
        
        scene.add(building, sign, lights)
        return scene
    
    def analyze_intuition_vs_truth(self):
        """分析直觉与真相"""
        title = Text("直觉 VS 数学真相", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：错误直觉
        intuition_title = Text("普通人的想法", font_size=28, color=PROB_RED)
        intuition_title.shift(LEFT * 3.5 + UP * 2)
        
        intuition_points = VGroup(
            Text("• 运气有好有坏", font_size=22),
            Text("• 总会有人赢大钱", font_size=22),
            Text("• 我可能是幸运儿", font_size=22),
            Text("• 小赌怡情无妨", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        intuition_points.next_to(intuition_title, DOWN, buff=0.5)
        
        # 右侧：数学真相
        truth_title = Text("数学的真相", font_size=28, color=PROB_GREEN)
        truth_title.shift(RIGHT * 3.5 + UP * 2)
        
        truth_points = VGroup(
            Text("• 赌场有数学优势", font_size=22),
            Text("• 玩得越多输得越多", font_size=22),
            Text("• 大数定律保证盈利", font_size=22),
            Text("• 时间站在赌场一边", font_size=22, color=PROB_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        truth_points.next_to(truth_title, DOWN, buff=0.5)
        
        # 显示对比
        self.play(Write(intuition_title), Write(truth_title))
        self.play(Write(intuition_points), Write(truth_points))
        
        # 强调关键点
        key_point = Text(
            "赌场不靠运气，靠数学！",
            font_size=32,
            color=PROB_YELLOW,
            weight=BOLD
        )
        key_point.shift(DOWN * 2.5)
        self.play(Write(key_point))
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(intuition_title), FadeOut(intuition_points),
            FadeOut(truth_title), FadeOut(truth_points), FadeOut(key_point)
        )
    
    def mathematical_proof(self):
        """大数定律的数学证明"""
        title = Text("大数定律", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 第一部分：定义
        self.show_law_definition()
        
        # 第二部分：证明要点
        self.show_proof_key_points()
        
        self.play(FadeOut(title))
    
    def show_law_definition(self):
        """展示大数定律定义"""
        # 通俗解释（上方）
        plain_def = Text(
            "样本越大，平均值越接近期望值",
            font_size=28,
            color=PROB_YELLOW
        )
        plain_def.shift(UP * 2)
        self.play(Write(plain_def))
        
        # 数学定义（中间）
        math_title = Text("数学表述：", font_size=24, color=WHITE)
        math_title.shift(UP * 0.5)
        
        math_def = MathTex(
            r"\lim_{n \to \infty} P\left(\left|\frac{1}{n}\sum_{i=1}^{n}X_i - \mu\right| > \epsilon\right) = 0"
        )
        math_def.shift(DOWN * 0.5)
        
        self.play(Write(math_title))
        self.play(Write(math_def))
        
        # 解释符号（下方）
        explanation = VGroup(
            MathTex(r"X_i", color=PROB_BLUE).scale(0.8),
            Text("：第i次试验结果", font_size=20),
            MathTex(r"\mu", color=PROB_GREEN).scale(0.8),
            Text("：期望值", font_size=20),
            MathTex(r"n", color=PROB_YELLOW).scale(0.8),
            Text("：试验次数", font_size=20)
        ).arrange_in_grid(rows=3, cols=2, buff=0.3)
        explanation.shift(DOWN * 2)
        
        self.play(Write(explanation))
        self.wait(2)
        
        self.play(
            FadeOut(plain_def), FadeOut(math_title),
            FadeOut(math_def), FadeOut(explanation)
        )
    
    def show_proof_key_points(self):
        """展示证明要点"""
        # 标题
        proof_title = Text("证明的核心思想", font_size=28, color=PROB_YELLOW)
        proof_title.shift(UP * 2.5)
        self.play(Write(proof_title))
        
        # 左侧：方差分析
        var_title = Text("方差递减", font_size=24, color=PROB_BLUE)
        var_title.shift(LEFT * 3.5 + UP * 1)
        
        var_formula = MathTex(
            r"\text{Var}\left(\frac{1}{n}\sum X_i\right) = \frac{\sigma^2}{n}"
        ).scale(0.9)
        var_formula.next_to(var_title, DOWN, buff=0.5)
        
        var_explanation = Text(
            "n越大，方差越小",
            font_size=20,
            color=GRAY
        )
        var_explanation.next_to(var_formula, DOWN, buff=0.3)
        
        # 右侧：切比雪夫不等式
        cheby_title = Text("切比雪夫不等式", font_size=24, color=PROB_GREEN)
        cheby_title.shift(RIGHT * 3.5 + UP * 1)
        
        cheby_formula = MathTex(
            r"P(|X-\mu| \geq k\sigma) \leq \frac{1}{k^2}"
        ).scale(0.9)
        cheby_formula.next_to(cheby_title, DOWN, buff=0.5)
        
        cheby_explanation = Text(
            "偏离概率有上界",
            font_size=20,
            color=GRAY
        )
        cheby_explanation.next_to(cheby_formula, DOWN, buff=0.3)
        
        # 显示内容
        self.play(Write(var_title), Write(cheby_title))
        self.play(Write(var_formula), Write(cheby_formula))
        self.play(Write(var_explanation), Write(cheby_explanation))
        
        # 结论
        conclusion = Text(
            "当n→∞时，样本均值必然收敛到期望值！",
            font_size=26,
            color=PROB_GREEN,
            weight=BOLD
        )
        conclusion.shift(DOWN * 2)
        self.play(Write(conclusion))
        self.wait(2)
        
        self.play(
            FadeOut(proof_title), FadeOut(var_title), FadeOut(var_formula),
            FadeOut(var_explanation), FadeOut(cheby_title), FadeOut(cheby_formula),
            FadeOut(cheby_explanation), FadeOut(conclusion)
        )
    
    def coin_flip_experiment(self):
        """硬币投掷实验"""
        title = Text("硬币实验：见证收敛", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建坐标系
        axes = Axes(
            x_range=[0, 1000, 200],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=5,
            axis_config={
                "color": WHITE,
                "include_tip": True,
                "include_numbers": True,
                "decimal_number_config": {"num_decimal_places": 1}
            }
        ).shift(DOWN * 0.5)
        
        x_label = Text("投掷次数", font_size=20).next_to(axes.x_axis, DOWN)
        y_label = Text("正面比例", font_size=20).next_to(axes.y_axis, LEFT).rotate(PI/2)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # 期望值线
        expected_line = DashedLine(
            axes.c2p(0, 0.5),
            axes.c2p(1000, 0.5),
            color=PROB_GREEN,
            stroke_width=3
        )
        expected_label = Text("期望值 0.5", font_size=18, color=PROB_GREEN)
        expected_label.next_to(expected_line, RIGHT)
        
        self.play(Create(expected_line), Write(expected_label))
        
        # 运行多次实验
        curves = VGroup()
        n_experiments = 3
        colors = [PROB_BLUE, PROB_YELLOW, PROB_RED]
        
        for exp in range(n_experiments):
            # 模拟数据
            n_flips = 1000
            results = []
            heads_count = 0
            
            for i in range(1, n_flips + 1):
                if random.random() < 0.5:
                    heads_count += 1
                if i % 10 == 0:  # 每10次记录一次
                    results.append((i, heads_count / i))
            
            # 创建曲线
            points = [axes.c2p(x, y) for x, y in results]
            curve = VMobject(color=colors[exp], stroke_width=2)
            curve.set_points_smoothly(points)
            curves.add(curve)
            
            # 动画显示
            self.play(Create(curve), run_time=2)
        
        # 添加说明
        convergence_text = Text(
            "所有曲线都向0.5收敛！",
            font_size=28,
            color=PROB_GREEN,
            weight=BOLD
        )
        convergence_text.shift(DOWN * 1.5)
        self.play(Write(convergence_text))
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(expected_line), FadeOut(expected_label),
            FadeOut(curves), FadeOut(convergence_text)
        )
    
    def casino_profit_model(self):
        """赌场盈利模型"""
        title = Text("轮盘赌的数学优势", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：轮盘赌说明
        roulette_title = Text("美式轮盘", font_size=28, color=PROB_YELLOW)
        roulette_title.shift(LEFT * 4 + UP * 2)
        
        roulette_info = VGroup(
            Text("• 38个数字格", font_size=20),
            Text("• 18红 + 18黑", font_size=20),
            Text("• 2个绿色(0,00)", font_size=20, color=PROB_GREEN),
            Text("• 押红/黑赔率1:1", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        roulette_info.next_to(roulette_title, DOWN, buff=0.5)
        
        # 右侧：期望值计算
        ev_title = Text("期望值计算", font_size=28, color=PROB_BLUE)
        ev_title.shift(RIGHT * 3.5 + UP * 2)
        
        # 押$100在红色
        bet_text = Text("押$100在红色：", font_size=22)
        bet_text.next_to(ev_title, DOWN, buff=0.5)
        
        # 期望值公式
        ev_calc = VGroup(
            MathTex(r"E(X) = ", color=WHITE),
            MathTex(r"\frac{18}{38} \times 100", color=PROB_GREEN),
            MathTex(r" + ", color=WHITE),
            MathTex(r"\frac{20}{38} \times (-100)", color=PROB_RED)
        ).arrange(RIGHT, buff=0.1)
        ev_calc.next_to(bet_text, DOWN, buff=0.3)
        
        # 结果
        ev_result = MathTex(r"E(X) = -5.26", color=PROB_RED, font_size=32)
        ev_result.next_to(ev_calc, DOWN, buff=0.5)
        
        # 显示内容
        self.play(Write(roulette_title), Write(ev_title))
        self.play(Write(roulette_info))
        self.play(Write(bet_text))
        self.play(Write(ev_calc))
        self.play(Write(ev_result))
        self.play(ev_result.animate.scale(1.2))
        
        # 长期结果
        long_term = VGroup(
            Text("玩1000次，预期损失：", font_size=24),
            Text("$5,260", font_size=36, color=PROB_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        long_term.shift(DOWN * 2)
        
        self.play(Write(long_term))
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(roulette_title), FadeOut(roulette_info),
            FadeOut(ev_title), FadeOut(bet_text), FadeOut(ev_calc),
            FadeOut(ev_result), FadeOut(long_term)
        )
    
    def real_world_applications(self):
        """现实应用"""
        title = Text("大数定律的应用", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 四个应用场景
        applications = VGroup()
        
        # 1. 保险公司
        insurance = self.create_application_card(
            "保险公司",
            PROB_BLUE,
            [
                "个体风险不可预测",
                "群体规律可计算",
                "客户越多越稳定"
            ]
        )
        insurance.shift(LEFT * 5 + UP * 1)
        
        # 2. 民意调查
        polling = self.create_application_card(
            "民意调查",
            PROB_GREEN,
            [
                "样本代表总体",
                "1000人足够准确",
                "误差范围可控"
            ]
        )
        polling.shift(LEFT * 1.5 + UP * 1)
        
        # 3. 质量控制
        quality = self.create_application_card(
            "质量控制",
            PROB_YELLOW,
            [
                "抽检产品质量",
                "不良率可估计",
                "生产线可监控"
            ]
        )
        quality.shift(RIGHT * 1.5 + UP * 1)
        
        # 4. A/B测试
        ab_test = self.create_application_card(
            "A/B测试",
            PROB_RED,
            [
                "对比两种方案",
                "数据量要充足",
                "结果才可信"
            ]
        )
        ab_test.shift(RIGHT * 5 + UP * 1)
        
        applications.add(insurance, polling, quality, ab_test)
        
        # 逐个显示
        for app in applications:
            self.play(FadeIn(app, shift=UP), run_time=0.5)
        
        # 核心总结
        summary = Text(
            "样本足够大，真相必现！",
            font_size=32,
            color=PROB_GREEN,
            weight=BOLD
        )
        summary.shift(DOWN * 2.5)
        self.play(Write(summary))
        self.wait(3)
        
        self.play(FadeOut(title), FadeOut(applications), FadeOut(summary))
    
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
        title_text = Text(title, font_size=22, color=color, weight=BOLD)
        title_text.shift(UP * 0.8)
        
        # 要点
        points_text = VGroup()
        for i, point in enumerate(points):
            point_text = Text(f"• {point}", font_size=16, color=WHITE)
            point_text.shift(DOWN * i * 0.4)
        points_text.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        points_text.shift(DOWN * 0.2)
        
        card.add(bg, title_text, points_text)
        return card
    
    def show_ending(self):
        """结尾"""
        # 核心总结
        summary = VGroup(
            Text("大数定律告诉我们：", font_size=36, color=WHITE),
            Text("偶然中有必然", font_size=42, color=PROB_PURPLE, weight=BOLD),
            Text("时间会揭示真相", font_size=32, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 系列结尾
        self.show_series_ending(
            "赌场靠的不是运气",
            "而是数学的必然"
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
        
        # EP13 内容预告
        ep13_title = Text(
            "第13集：正态分布",
            font_size=42,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep13_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("为什么它无处不在？", font_size=28, color=WHITE),
            Text("从身高到考试成绩", font_size=28, color=WHITE),
            Text("自然界最美的曲线", font_size=32, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep13_title, DOWN, buff=0.8)
        
        self.play(Write(ep13_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "你的身高在人群中排第几？",
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
            FadeOut(preview_title), FadeOut(ep13_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))