"""
EP11: 赌徒谬误
随机无记忆 - 独立事件的真相
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


class GamblersFallacyEP11(Scene):
    """赌徒谬误 - 概率论系列 EP11"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 设置随机种子
        random.seed(42)
        np.random.seed(42)
        
        # 1. 开场
        self.show_series_intro(11, "赌徒谬误")
        
        # 2. 问题引入 - 连续10次正面
        self.introduce_problem()
        
        # 3. 直觉陷阱
        self.analyze_intuition()
        
        # 4. 数学真相 - 独立事件
        self.mathematical_truth()
        
        # 5. 实验验证
        self.experimental_verification()
        
        # 6. 历史案例 - 蒙特卡洛赌场
        self.monte_carlo_story()
        
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
    
    def introduce_problem(self):
        """引入问题 - 连续10次正面"""
        title = Text("一个硬币实验", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建硬币（左侧）
        coin = self.create_coin()
        coin.shift(LEFT * 4)
        self.play(FadeIn(coin))
        
        # 显示连续10次正面（右侧）
        results_title = Text("投掷结果：", font_size=24, color=WHITE)
        results_title.shift(RIGHT * 2 + UP * 2)
        self.play(Write(results_title))
        
        # 创建10个正面结果
        heads_results = VGroup()
        for i in range(10):
            head = self.create_coin_result("H", PROB_YELLOW)
            head.scale(0.8)
            if i < 5:
                head.move_to(RIGHT * 2 + RIGHT * i * 0.8 + UP * 0.5)
            else:
                head.move_to(RIGHT * 2 + RIGHT * (i-5) * 0.8 + DOWN * 0.5)
            heads_results.add(head)
        
        # 逐个显示，营造紧张感
        for i, head in enumerate(heads_results):
            self.play(
                coin.animate.rotate(PI * 4),  # 硬币旋转
                FadeIn(head, scale=0.5),
                run_time=0.3 if i < 8 else 0.5
            )
            if i == 9:
                # 最后一个特别强调
                self.play(head.animate.scale(1.2).set_color(PROB_RED))
        
        # 震惊的问题
        question = Text(
            "下一次投掷，反面的概率是多少？",
            font_size=32,
            color=PROB_YELLOW
        )
        question.shift(DOWN * 2)
        self.play(Write(question))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(coin), FadeOut(results_title),
            FadeOut(heads_results), FadeOut(question)
        )
    
    def create_coin(self):
        """创建硬币"""
        coin = VGroup()
        
        # 硬币圆形
        circle = Circle(radius=1, fill_color=GOLD, fill_opacity=0.8, stroke_color=YELLOW)
        
        # 正面标记
        head_text = Text("正", font_size=48, color=BLACK)
        
        coin.add(circle, head_text)
        return coin
    
    def create_coin_result(self, side: str, color):
        """创建硬币结果标记"""
        result = VGroup()
        
        circle = Circle(radius=0.3, fill_color=color, fill_opacity=0.8)
        text = Text(side, font_size=24, color=WHITE)
        
        result.add(circle, text)
        return result
    
    def analyze_intuition(self):
        """分析直觉陷阱"""
        title = Text("大多数人的想法", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：错误直觉
        wrong_title = Text("错误直觉", font_size=28, color=PROB_RED)
        wrong_title.shift(LEFT * 3.5 + UP * 2)
        
        wrong_thoughts = VGroup(
            Text("• 正面出现太多了", font_size=22),
            Text("• 该轮到反面了", font_size=22),
            Text("• 宇宙需要平衡", font_size=22),
            Text("• 反面概率应该更大", font_size=22, color=PROB_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        wrong_thoughts.next_to(wrong_title, DOWN, buff=0.5)
        
        # 右侧：心理原因
        psych_title = Text("心理原因", font_size=28, color=PROB_BLUE)
        psych_title.shift(RIGHT * 3.5 + UP * 2)
        
        psych_reasons = VGroup(
            Text("• 模式识别本能", font_size=22),
            Text("• 寻求规律倾向", font_size=22),
            Text("• 因果关系错觉", font_size=22),
            Text("• 小数定律误解", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        psych_reasons.next_to(psych_title, DOWN, buff=0.5)
        
        # 显示内容
        self.play(Write(wrong_title), Write(psych_title))
        self.play(
            Write(wrong_thoughts),
            Write(psych_reasons),
            run_time=2
        )
        
        # 大大的错误符号
        big_cross = Cross(
            VGroup(wrong_thoughts),
            color=RED,
            stroke_width=8
        )
        self.play(Create(big_cross))
        
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(wrong_title), FadeOut(wrong_thoughts),
            FadeOut(psych_title), FadeOut(psych_reasons), FadeOut(big_cross)
        )
    
    def mathematical_truth(self):
        """数学真相 - 独立事件"""
        title = Text("独立事件的数学真相", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 第一部分：独立性定义
        self.show_independence_definition()
        
        # 第二部分：概率计算
        self.show_probability_calculation()
        
        self.play(FadeOut(title))
    
    def show_independence_definition(self):
        """展示独立性定义"""
        # 标题
        def_title = Text("什么是独立事件？", font_size=28, color=PROB_YELLOW)
        def_title.shift(UP * 2)
        self.play(Write(def_title))
        
        # 数学定义（左侧）
        math_def = VGroup(
            Text("数学定义：", font_size=24, color=WHITE),
            MathTex(r"P(A \cap B) = P(A) \times P(B)"),
            Text("事件A不影响事件B的概率", font_size=18, color=GRAY)
        ).arrange(DOWN, buff=0.3)
        math_def.shift(LEFT * 3.5)
        
        # 通俗解释（右侧）
        plain_def = VGroup(
            Text("通俗解释：", font_size=24, color=WHITE),
            Text("硬币没有记忆", font_size=22, color=PROB_GREEN),
            Text("每次投掷都是全新开始", font_size=20),
            Text("过去不影响未来", font_size=20)
        ).arrange(DOWN, buff=0.3)
        plain_def.shift(RIGHT * 3.5)
        
        self.play(Write(math_def), Write(plain_def))
        self.wait(2)
        
        # 强调
        emphasis = Text(
            "硬币不知道自己刚才是正面还是反面！",
            font_size=26,
            color=PROB_GREEN
        )
        emphasis.shift(DOWN * 2)
        self.play(Write(emphasis))
        self.wait(2)
        
        self.play(
            FadeOut(def_title), FadeOut(math_def),
            FadeOut(plain_def), FadeOut(emphasis)
        )
    
    def show_probability_calculation(self):
        """展示概率计算"""
        # 标题
        calc_title = Text("连续事件的概率", font_size=28, color=PROB_YELLOW)
        calc_title.shift(UP * 2)
        self.play(Write(calc_title))

        # 左侧：单次概率
        single_prob = VGroup(
            Text("单次投掷：", font_size=24),
            MathTex(r"P(\text{H}) = P(\text{T}) = 0.5"),
            Text("正面和反面概率各50%", font_size=18, color=GRAY)
        ).arrange(DOWN, buff=0.3)
        single_prob.shift(LEFT * 3.5 + UP * 0.5)
        
        self.play(Write(single_prob))
        self.wait(1)
        
        # 右侧：连续10次正面的概率
        consecutive_title = Text("连续10次正面的概率：", font_size=24)
        consecutive_title.shift(RIGHT * 3.5 + UP * 1.1)
        
        consecutive_calc = MathTex(
            r"P(\text{10H}) = 0.5^{10} = \frac{1}{1024} \approx 0.098\%"
        )
        consecutive_calc.next_to(consecutive_title, DOWN, buff=0.3)
        
        self.play(Write(consecutive_title))
        self.play(Write(consecutive_calc))
        
        # 底部中央：关键点
        key_point = VGroup(
            Text("但是！第11次投掷：", font_size=26, color=PROB_RED),
            MathTex(r"P(\text{H}) = 0.5, \quad P(\text{T}) = 0.5"),
            Text("概率完全没有改变！", font_size=24, color=PROB_GREEN)
        ).arrange(DOWN, buff=0.3)
        key_point.shift(DOWN * 1.5)
        
        self.play(Write(key_point))
        self.play(key_point[2].animate.scale(1.2))
        self.wait(3)
        
        self.play(
            FadeOut(calc_title), FadeOut(single_prob),
            FadeOut(consecutive_title), FadeOut(consecutive_calc),
            FadeOut(key_point)
        )
    
    def experimental_verification(self):
        """实验验证"""
        title = Text("实验验证", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建实验设置
        self.run_coin_flip_experiment()
        
        self.play(FadeOut(title))
    
    def run_coin_flip_experiment(self):
        """运行硬币投掷实验"""
        # 说明文字
        exp_text = Text(
            "收集所有\"连续10次正面后\"的第11次结果",
            font_size=24,
            color=WHITE
        )
        exp_text.shift(UP * 2.5)
        self.play(Write(exp_text))
        
        # 创建统计显示
        stats_bg = Rectangle(
            width=10, height=3,
            fill_color=PROB_GRAY,
            fill_opacity=0.3,
            stroke_color=WHITE
        )
        
        # 左右两个统计框
        heads_box = self.create_result_box("正面", PROB_YELLOW, LEFT * 2.5)
        tails_box = self.create_result_box("反面", PROB_BLUE, RIGHT * 2.5)
        
        self.play(Create(stats_bg), Create(heads_box), Create(tails_box))
        
        # 模拟数据
        n_sequences = 1000  # 找到1000个"连续10次正面"的序列
        heads_count = 0
        tails_count = 0
        
        # 快速模拟
        for i in range(n_sequences):
            # 第11次投掷的结果
            result = random.choice([True, False])  # True代表正面
            if result:
                heads_count += 1
            else:
                tails_count += 1
            
            # 每100次更新一次显示
            if (i + 1) % 100 == 0:
                self.update_result_box(heads_box, heads_count, i + 1)
                self.update_result_box(tails_box, tails_count, i + 1)
        
        # 最终结果
        final_text = Text(
            f"正面：{heads_count/n_sequences:.1%}  反面：{tails_count/n_sequences:.1%}",
            font_size=32,
            color=PROB_GREEN
        )
        final_text.shift(DOWN * 2)
        
        self.play(Write(final_text))
        self.wait(2)
        
        # 结论
        conclusion = Text(
            "结果接近50:50，历史不影响未来！",
            font_size=28,
            color=PROB_GREEN,
            weight=BOLD
        )
        conclusion.shift(DOWN * 3)
        self.play(Write(conclusion))
        self.wait(3)
        
        self.play(
            FadeOut(exp_text), FadeOut(stats_bg),
            FadeOut(heads_box), FadeOut(tails_box),
            FadeOut(final_text), FadeOut(conclusion)
        )
    
    def create_result_box(self, label: str, color, position):
        """创建结果统计框"""
        box = VGroup()
        
        # 背景
        bg = Rectangle(
            width=3, height=2,
            fill_color=color,
            fill_opacity=0.2,
            stroke_color=color
        )
        
        # 标签
        label_text = Text(label, font_size=24, color=color)
        label_text.shift(UP * 0.5)
        
        # 计数
        count_text = Text("0", font_size=36, color=WHITE)
        
        # 百分比
        percent_text = Text("0.0%", font_size=20, color=color)
        percent_text.shift(DOWN * 0.5)
        
        box.add(bg, label_text, count_text, percent_text)
        box.shift(position)
        
        # 保存引用
        box.count_text = count_text
        box.percent_text = percent_text
        
        return box
    
    def update_result_box(self, box, count: int, total: int):
        """更新结果框"""
        new_count = Text(str(count), font_size=36, color=WHITE)
        new_count.move_to(box.count_text.get_center())
        
        percent = count / total * 100
        new_percent = Text(f"{percent:.1f}%", font_size=20, color=box[0].get_stroke_color())
        new_percent.move_to(box.percent_text.get_center())
        
        self.play(
            Transform(box.count_text, new_count),
            Transform(box.percent_text, new_percent),
            run_time=0.1
        )
    
    def monte_carlo_story(self):
        """蒙特卡洛赌场的故事"""
        title = Text("历史上的真实案例", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 故事背景
        story_title = Text("1913年，蒙特卡洛赌场", font_size=28, color=PROB_YELLOW)
        story_title.shift(UP * 2)
        self.play(Write(story_title))
        
        # 创建轮盘赌（左侧）
        roulette = self.create_roulette()
        roulette.shift(LEFT * 4)
        self.play(Create(roulette))
        
        # 连续26次黑色（右侧）
        black_sequence = VGroup()
        for i in range(26):
            black = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1)
            if i < 13:
                black.move_to(RIGHT * 2 + RIGHT * i * 0.35 + UP * 1)
            else:
                black.move_to(RIGHT * 2 + RIGHT * (i-13) * 0.35 + DOWN * 0.5)
            black_sequence.add(black)
        
        # 逐个显示，营造紧张感
        for i, black in enumerate(black_sequence):
            self.play(
                Rotate(roulette, angle=PI/4),
                FadeIn(black, scale=0.5),
                run_time=0.1 if i < 20 else 0.3
            )
        
        # 震惊的数字
        shock_text = Text(
            "连续26次黑色！",
            font_size=32,
            color=PROB_RED
        )
        shock_text.shift(DOWN * 2)
        self.play(Write(shock_text))
        
        # 赌徒的反应
        gambler_reaction = Text(
            "赌徒们疯狂下注红色，认为\"该轮到红色了\"",
            font_size=24,
            color=PROB_YELLOW
        )
        gambler_reaction.shift(DOWN * 2.8)
        self.play(Write(gambler_reaction))
        
        # 结果
        result = Text(
            "结果：赌场赚了数百万法郎！",
            font_size=28,
            color=PROB_GREEN
        )
        result.shift(DOWN * 3.6)
        self.play(Write(result))
        
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(story_title),
            FadeOut(roulette), FadeOut(black_sequence),
            FadeOut(shock_text), FadeOut(gambler_reaction),
            FadeOut(result)
        )
    
    def create_roulette(self):
        """创建轮盘赌"""
        roulette = VGroup()
        
        # 外圈
        outer_circle = Circle(radius=1.5, stroke_color=GOLD, stroke_width=4)
        
        # 内圈
        inner_circle = Circle(radius=1.2, fill_color=DARK_BROWN, fill_opacity=0.8)
        
        # 红黑格子（简化版）
        sectors = VGroup()
        n_sectors = 8
        for i in range(n_sectors):
            start_angle = i * TAU / n_sectors
            color = RED if i % 2 == 0 else BLACK
            
            # 使用AnnularSector代替Sector
            sector = AnnularSector(
                inner_radius=0.8,
                outer_radius=1.2,
                angle=TAU/n_sectors,
                start_angle=start_angle,
                fill_color=color,
                fill_opacity=0.8,
                stroke_width=0
            )
            sectors.add(sector)
        
        # 中心点
        center = Dot(radius=0.1, color=GOLD)
        
        roulette.add(outer_circle, inner_circle, sectors, center)
        return roulette
    
    def real_world_applications(self):
        """现实应用"""
        title = Text("赌徒谬误在生活中", font_size=42, color=PROB_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 应用场景 - 左右分布
        left_apps = VGroup(
            # 股市投资
            VGroup(
                Text("股市投资", font_size=28, color=PROB_BLUE),
                Text("\"跌了这么多天，该涨了\"", font_size=22, color=WHITE),
                Text("错误！每天都是独立的", font_size=20, color=PROB_RED)
            ).arrange(DOWN, buff=0.2),
            
            # 彩票
            VGroup(
                Text("彩票选号", font_size=28, color=PROB_GREEN),
                Text("\"这个号很久没出了\"", font_size=22, color=WHITE),
                Text("错误！每期概率相同", font_size=20, color=PROB_RED)
            ).arrange(DOWN, buff=0.2)
        ).arrange(DOWN, buff=1.0)
        left_apps.shift(LEFT * 3)
        
        right_apps = VGroup(
            # 生育
            VGroup(
                Text("生育性别", font_size=28, color=PROB_YELLOW),
                Text("\"前三个都是女儿，第四个该是儿子了\"", font_size=22, color=WHITE),
                Text("错误！每次都是50%", font_size=20, color=PROB_RED)
            ).arrange(DOWN, buff=0.2)
        )
        right_apps.shift(RIGHT * 3)
        
        applications = VGroup(left_apps, right_apps)
        
        # 先显示左侧应用
        for app in left_apps:
            self.play(Write(app[0]))
            self.play(FadeIn(app[1], shift=UP))
            self.play(FadeIn(app[2], shift=UP))
            self.wait(1)
        
        # 再显示右侧应用
        for app in right_apps:
            self.play(Write(app[0]))
            self.play(FadeIn(app[1], shift=UP))
            self.play(FadeIn(app[2], shift=UP))
            self.wait(1)
        
        # 正确思维
        correct_thinking = Text(
            "记住：随机事件没有记忆！",
            font_size=32,
            color=PROB_GREEN,
            weight=BOLD
        )
        correct_thinking.shift(DOWN * 2.5)
        self.play(Write(correct_thinking))
        self.wait(3)
        
        self.play(
            FadeOut(title), FadeOut(applications),
            FadeOut(correct_thinking)
        )
    
    def show_ending(self):
        """结尾"""
        # 核心总结
        summary = VGroup(
            Text("赌徒谬误的本质：", font_size=36, color=WHITE),
            Text("把独立事件当成相关事件", font_size=42, color=PROB_PURPLE, weight=BOLD),
            Text("过去不能预测未来", font_size=32, color=PROB_YELLOW)
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]))
        self.play(Write(summary[1]))
        self.play(Write(summary[2]))
        self.wait(2)
        
        self.play(FadeOut(summary))
        
        # 系列结尾
        self.show_series_ending(
            "概率没有记忆",
            "但人类有"
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
        
        # EP12 内容预告
        ep12_title = Text(
            "第12集：大数定律",
            font_size=42,
            color=PROB_PURPLE,
            weight=BOLD
        )
        ep12_title.shift(UP * 0.5)
        
        # 预告内容
        preview_content = VGroup(
            Text("为什么赌场永远是赢家？", font_size=28, color=WHITE),
            Text("样本越大，越接近真相", font_size=28, color=WHITE),
            Text("混沌中的必然秩序", font_size=32, color=PROB_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.4)
        preview_content.next_to(ep12_title, DOWN, buff=0.8)
        
        self.play(Write(ep12_title))
        self.play(Write(preview_content[0]))
        self.play(Write(preview_content[1]))
        self.play(Write(preview_content[2]), preview_content[2].animate.scale(1.1))
        
        # 思考问题
        think_question = Text(
            "抛多少次硬币才能相信概率？",
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
            FadeOut(preview_title), FadeOut(ep12_title),
            FadeOut(preview_content), FadeOut(think_question),
            Write(see_you)
        )
        self.wait(2)
        self.play(FadeOut(see_you))