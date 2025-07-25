from manim import *
import numpy as np

class FibonacciRabbitsEP2(Scene):
    """斐波那契与兔子问题 - 黄金分割系列 EP02"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：历史背景
        self.show_historical_context()
        
        # 第二部分：兔子问题
        self.show_rabbit_problem()
        
        # 第三部分：数列生成
        self.generate_fibonacci_sequence()
        
        # 第四部分：自然界中的斐波那契
        self.show_fibonacci_in_nature()
        
        # 第五部分：黄金比例
        self.show_golden_ratio()
        
        # 结尾
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第二集：斐波那契与兔子问题", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_historical_context(self):
        """历史背景介绍 - 0:10-0:40"""
        # 斐波那契肖像（用简单图形代替）
        portrait_bg = Rectangle(width=3, height=4, color=GOLD_D, fill_opacity=0.3)
        portrait_text = Text("斐波那契\n(1170-1250)", font_size=24, color=WHITE)
        portrait = VGroup(portrait_bg, portrait_text)
        portrait.to_edge(LEFT)
        
        # 历史介绍
        intro_lines = [
            Text("列奥纳多·斐波那契", font_size=36, color=BLUE),
            Text("中世纪最伟大的数学家", font_size=28, color=WHITE),
            Text("将阿拉伯数字引入欧洲", font_size=28, color=WHITE)
        ]
        intro_text = VGroup(*intro_lines).arrange(DOWN, buff=0.4)
        intro_text.next_to(portrait, RIGHT, buff=1)
        
        self.play(FadeIn(portrait), run_time=1)
        for line in intro_lines:
            self.play(Write(line), run_time=1)
            self.wait(0.5)
        
        self.wait(2)
        
        # 《算盘书》介绍
        book_rect = Rectangle(width=2.5, height=3.5, color=MAROON, fill_opacity=0.5)
        book_title = Text("《算盘书》\n1202年", font_size=20, color=WHITE)
        book = VGroup(book_rect, book_title)
        book.move_to(portrait.get_center())
        
        self.play(
            Transform(portrait, book),
            FadeOut(intro_text),
            run_time=1.5
        )
        
        book_info = Text("在这本书中，他提出了一个有趣的问题...", 
                        font_size=28, color=YELLOW)
        book_info.next_to(book, RIGHT, buff=1)
        
        self.play(Write(book_info))
        self.wait(2)
        self.play(FadeOut(portrait), FadeOut(book_info))
    
    def show_rabbit_problem(self):
        """展示兔子问题 - 0:40-1:40"""
        # 问题描述
        problem_title = Text("兔子繁殖问题", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(problem_title))
        
        # 规则说明
        rules = VGroup(
            Text("1. 开始有一对新生的兔子", font_size=24),
            Text("2. 兔子出生后第二个月开始繁殖", font_size=24),
            Text("3. 每对成年兔子每月生一对小兔子", font_size=24),
            Text("4. 兔子永不死亡", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rules.shift(UP*0.5)
        
        for rule in rules:
            self.play(Write(rule), run_time=0.8)
        
        self.wait(2)
        self.play(FadeOut(rules))
        
        # 可视化兔子繁殖过程
        self.visualize_rabbit_growth()
        
        self.play(FadeOut(problem_title))
    
    def visualize_rabbit_growth(self):
        """可视化兔子繁殖 - 嵌入在show_rabbit_problem中"""
        # 创建兔子图标（简化版）- 修复：统一兔子形状
        def create_rabbit(size=0.3, color=WHITE, is_baby=False):
            # 统一使用相同的body大小和耳朵大小，只通过颜色区分成年/幼体
            body = Circle(radius=size, color=color, fill_opacity=0.8)
            ears = VGroup(
                Ellipse(width=size*0.4, height=size*0.6, color=color, fill_opacity=0.8)
                    .shift(UP*size*0.7 + LEFT*size*0.25),
                Ellipse(width=size*0.4, height=size*0.6, color=color, fill_opacity=0.8)
                    .shift(UP*size*0.7 + RIGHT*size*0.25)
            )
            return VGroup(body, ears)
        
        # 月份标签
        months = ["第0月", "第1月", "第2月", "第3月", "第4月", "第5月"]
        month_labels = VGroup()
        
        # 存储每个月的兔子和计数文本
        rabbit_groups = []
        count_texts = []
        
        # 第0月：1对小兔子
        month_0 = Text(months[0], font_size=20, color=BLUE).to_edge(LEFT).shift(UP*2.5)
        month_labels.add(month_0)
        
        rabbit_0 = create_rabbit(color=PINK, is_baby=True)
        rabbit_0.next_to(month_0, RIGHT, buff=1)
        rabbit_groups.append(VGroup(rabbit_0))
        
        count_0 = Text("1对", font_size=20, color=YELLOW)
        count_0.next_to(rabbit_0, RIGHT, buff=1)
        count_texts.append(count_0)
        
        self.play(Write(month_0), Create(rabbit_0), Write(count_0))
        self.wait(1)
        
        # 第1月：1对成年兔子
        month_1 = Text(months[1], font_size=20, color=BLUE).next_to(month_0, DOWN, buff=0.8)
        month_labels.add(month_1)
        
        rabbit_1 = create_rabbit(color=WHITE, is_baby=False)
        rabbit_1.next_to(month_1, RIGHT, buff=1)
        rabbit_groups.append(VGroup(rabbit_1))
        
        count_1 = Text("1对", font_size=20, color=YELLOW)
        count_1.next_to(rabbit_1, RIGHT, buff=1)
        count_texts.append(count_1)
        
        # 显示成长动画
        growth_arrow = Arrow(rabbit_0.get_bottom(), rabbit_1.get_top(), color=GREEN)
        self.play(Create(growth_arrow))
        # 修复：避免使用copy()，直接创建rabbit_1
        self.play(Write(month_1), Create(rabbit_1), Write(count_1))
        self.play(FadeOut(growth_arrow))
        self.wait(1)
        
        # 第2月：1对成年 + 1对小兔子 = 2对
        month_2 = Text(months[2], font_size=20, color=BLUE).next_to(month_1, DOWN, buff=0.8)
        month_labels.add(month_2)
        
        adult_2 = create_rabbit(color=WHITE, is_baby=False)
        baby_2 = create_rabbit(color=PINK, is_baby=True)
        adult_2.next_to(month_2, RIGHT, buff=1)
        baby_2.next_to(adult_2, RIGHT, buff=0.5)
        rabbit_groups.append(VGroup(adult_2, baby_2))
        
        count_2 = Text("2对", font_size=20, color=YELLOW)
        count_2.next_to(baby_2, RIGHT, buff=1)
        count_texts.append(count_2)
        
        # 繁殖动画
        birth_arrow = CurvedArrow(rabbit_1.get_right(), baby_2.get_left(), color=GREEN)
        self.play(Create(birth_arrow))
        self.play(
            Write(month_2),
            Create(adult_2),
            Create(baby_2),
            Write(count_2)
        )
        self.play(FadeOut(birth_arrow))
        self.wait(1)
        
        # 简化后续月份的展示
        remaining_data = [
            (months[3], 3, "3对"),  # 2成年 + 1小
            (months[4], 5, "5对"),  # 3成年 + 2小
            (months[5], 8, "8对")   # 5成年 + 3小
        ]
        
        prev_month = month_2
        for month_name, rabbit_count, count_text in remaining_data:
            month_label = Text(month_name, font_size=20, color=BLUE).next_to(prev_month, DOWN, buff=0.8)
            month_labels.add(month_label)
            
            # 简化显示：只显示数字
            count_display = Text(count_text, font_size=24, color=YELLOW)
            count_display.next_to(month_label, RIGHT, buff=2)
            count_texts.append(count_display)  # 修复：记录所有计数文本
            
            self.play(Write(month_label), Write(count_display), run_time=0.8)
            prev_month = month_label
        
        self.wait(2)
        
        # 高亮数字序列
        sequence_text = Text("1, 1, 2, 3, 5, 8...", font_size=36, color=GOLD)
        sequence_text.to_edge(RIGHT).shift(UP)
        
        self.play(Write(sequence_text))
        self.wait(2)
        
        # 修复：正确清理所有兔子和计数文本
        self.play(
            FadeOut(month_labels),
            FadeOut(rabbit_0), FadeOut(rabbit_1), FadeOut(adult_2), FadeOut(baby_2),
            *[FadeOut(count_text) for count_text in count_texts]
        )
        self.play(sequence_text.animate.move_to(ORIGIN).scale(1.5))
        self.wait(1)
        self.play(FadeOut(sequence_text))
    
    def generate_fibonacci_sequence(self):
        """生成斐波那契数列 - 1:40-2:20"""
        title = Text("斐波那契数列的规律", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 递推公式
        formula = MathTex(
            "F_n = F_{n-1} + F_{n-2}",
            font_size=48,
            color=WHITE
        )
        formula.shift(UP)
        
        initial_conditions = VGroup(
            MathTex("F_0 = 0", font_size=36),
            MathTex("F_1 = 1", font_size=36)
        ).arrange(RIGHT, buff=1)
        initial_conditions.next_to(formula, DOWN, buff=0.8)
        
        self.play(Write(formula))
        self.play(Write(initial_conditions))
        self.wait(2)
        
        # 动态生成数列
        self.play(
            FadeOut(formula),
            FadeOut(initial_conditions)
        )
        
        # 创建数列展示
        fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        
        # 第一行
        row1_nums = []
        for i in range(7):
            num = Text(str(fib_sequence[i]), font_size=36, color=WHITE)
            if i == 0:
                num.shift(LEFT*3.5 + UP*0.5)
            else:
                num.next_to(row1_nums[-1], RIGHT, buff=0.8)
            row1_nums.append(num)
        
        # 第二行
        row2_nums = []
        for i in range(7, 13):
            num = Text(str(fib_sequence[i]), font_size=36, color=WHITE)
            if i == 7:
                num.shift(LEFT*3.5 + DOWN*1.5)
            else:
                num.next_to(row2_nums[-1], RIGHT, buff=0.8)
            row2_nums.append(num)
        
        all_nums = row1_nums + row2_nums
        
        # 动画展示生成过程
        for i in range(len(all_nums)):
            if i < 2:
                self.play(Write(all_nums[i]), run_time=0.5)
            else:
                # 显示加法过程
                if i < 7:
                    nums_to_add = row1_nums
                else:
                    nums_to_add = all_nums
                
                idx1 = i - 2
                idx2 = i - 1
                
                # 创建加法指示
                arrow1 = Arrow(
                    nums_to_add[idx1].get_top() + UP*0.1,
                    nums_to_add[idx1].get_top() + UP*0.5,
                    color=GREEN,
                    buff=0
                )
                arrow2 = Arrow(
                    nums_to_add[idx2].get_top() + UP*0.1,
                    nums_to_add[idx2].get_top() + UP*0.5,
                    color=GREEN,
                    buff=0
                )
                
                self.play(
                    Create(arrow1),
                    Create(arrow2),
                    run_time=0.3
                )
                self.play(Write(all_nums[i]), run_time=0.5)
                self.play(
                    FadeOut(arrow1),
                    FadeOut(arrow2),
                    run_time=0.3
                )
        
        self.wait(2)
        
        # 渐变消失
        self.play(
            FadeOut(title),
            *[FadeOut(num) for num in all_nums]
        )
    
    def show_fibonacci_in_nature(self):
        """自然界中的斐波那契 - 2:20-3:00"""
        title = Text("大自然中的斐波那契", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建示例网格
        examples = VGroup()
        
        # 花瓣数示例
        flower_circle = Circle(radius=0.8, color=YELLOW, fill_opacity=0.3)
        petals = VGroup()
        petal_counts = [3, 5, 8, 13]
        
        for j, count in enumerate(petal_counts):
            flower = flower_circle.copy()
            flower.shift(LEFT*4 + RIGHT*j*2.5 + UP*1.5)
            
            # 添加花瓣
            for i in range(count):
                angle = i * TAU / count
                petal = Ellipse(
                    width=0.3, height=0.6,
                    color=PINK,
                    fill_opacity=0.8
                )
                petal.rotate(angle)
                petal.shift(flower.get_center() + 0.8 * np.array([np.cos(angle), np.sin(angle), 0]))
                petals.add(petal)
            
            label = Text(f"{count}瓣", font_size=20, color=WHITE)
            label.next_to(flower, DOWN, buff=0.3)
            
            examples.add(VGroup(flower, label))
        
        self.play(
            *[Create(example) for example in examples],
            *[Create(petal) for petal in petals],
            run_time=2
        )
        
        # 螺旋示例
        spiral_text = Text("松果、菠萝、向日葵的螺旋数", font_size=24, color=WHITE)
        spiral_text.shift(DOWN*0.5)
        
        spiral_numbers = Text("8, 13, 21, 34, 55, 89...", font_size=32, color=GOLD)
        spiral_numbers.next_to(spiral_text, DOWN, buff=0.5)
        
        self.play(Write(spiral_text))
        self.play(Write(spiral_numbers))
        
        self.wait(3)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(examples),
            FadeOut(petals),
            FadeOut(spiral_text),
            FadeOut(spiral_numbers)
        )
    
    def show_golden_ratio(self):
        """展示黄金比例 - 3:00-3:30"""
        title = Text("斐波那契与黄金比例", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 展示比值趋近黄金比例
        ratios_text = Text("相邻两项的比值：", font_size=28, color=WHITE)
        ratios_text.shift(UP*2 + LEFT*2)
        self.play(Write(ratios_text))
        
        # 计算并展示比值
        fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        ratios = []
        
        for i in range(1, 8):
            ratio = fib[i+1] / fib[i]
            ratio_text = MathTex(
                f"\\frac{{{fib[i+1]}}}{{{fib[i]}}} = {ratio:.4f}",
                font_size=24
            )
            if i == 1:
                ratio_text.next_to(ratios_text, DOWN, buff=0.5)
                ratio_text.align_to(ratios_text, LEFT)
            else:
                ratio_text.next_to(ratios[-1], DOWN, buff=0.3)
                ratio_text.align_to(ratios[-1], LEFT)
            ratios.append(ratio_text)
        
        for ratio in ratios[:5]:
            self.play(Write(ratio), run_time=0.6)
        
        # 黄金比例
        golden_ratio = MathTex(
            "\\phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.6180",
            font_size=36,
            color=GOLD
        )
        golden_ratio.to_edge(RIGHT).shift(UP)
        
        self.play(Write(golden_ratio))
        
        # 箭头指向
        arrow = Arrow(
            ratios[-1].get_right(),
            golden_ratio.get_left(),
            color=YELLOW
        )
        convergence_text = Text("趋近于", font_size=20, color=YELLOW)
        convergence_text.next_to(arrow, UP, buff=0.1)
        
        self.play(Create(arrow), Write(convergence_text))
        
        self.wait(3)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(ratios_text),
            *[FadeOut(ratio) for ratio in ratios],
            FadeOut(golden_ratio),
            FadeOut(arrow),
            FadeOut(convergence_text)
        )
    
    def show_ending(self):
        """结尾 - 3:30-4:00"""
        # 总结
        summary_lines = [
            Text("从一个简单的兔子问题", font_size=36, color=WHITE),
            Text("到贯穿整个自然界的数列", font_size=36, color=WHITE),
            Text("斐波那契数列展现了", font_size=36, color=WHITE),
            Text("数学与自然的完美和谐", font_size=42, color=GOLD)
        ]
        summary = VGroup(*summary_lines).arrange(DOWN, buff=0.5)
        
        for line in summary_lines:
            self.play(Write(line), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(summary))
        
        # 下期预告
        next_episode = VGroup(
            Text("下期预告", font_size=36, color=YELLOW),
            Text("鹦鹉螺中的等角螺线", font_size=32, color=WHITE),
            Text("探索自然界最优美的曲线", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(next_episode[0]), run_time=1)
        self.play(FadeIn(next_episode[1], shift=UP), run_time=1)
        self.play(FadeIn(next_episode[2], shift=UP), run_time=1)
        
        # 订阅提醒
        subscribe = Text("喜欢请三连支持！", font_size=32, color=RED)
        subscribe.next_to(next_episode, DOWN, buff=1)
        
        self.play(Write(subscribe))
        self.wait(3) 