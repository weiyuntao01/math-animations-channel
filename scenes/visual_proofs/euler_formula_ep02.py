"""
系列三：视觉化证明经典
EP02: 圆周率π的5种推导
从阿基米德到蒙特卡洛
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple

# 系列三配色方案
PROOF_BLUE = "#2563EB"      # 主色：证明蓝
PROOF_GREEN = "#059669"     # 辅助：推理绿  
PROOF_ORANGE = "#EA580C"    # 强调：关键橙
PROOF_PURPLE = "#7C3AED"    # 特殊：优雅紫
PROOF_GRAY = "#6B7280"      # 中性：背景灰
PROOF_YELLOW = "#FCD34D"    # 标记：重点黄
PROOF_RED = "#DC2626"       # 警告：矛盾红
PROOF_CYAN = "#06B6D4"      # 清新：对比青

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class PiCalculationEP02(Scene):
    """圆周率π的5种推导 - 视觉化证明经典 EP02"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 0. 系列开场
        self.show_series_intro()
        
        # 1. 引入：π的神秘
        self.introduce_pi()
        
        # 2-6. 五种推导方法
        self.method_1_archimedes()      # 阿基米德多边形逼近
        self.method_2_liu_hui()          # 刘徽割圆术
        self.method_3_leibniz()          # 莱布尼茨级数
        self.method_4_monte_carlo()      # 蒙特卡洛方法
        self.method_5_buffon_needle()    # 布丰投针法
        
        # 7. π的性质总结
        self.pi_properties()
        
        # 8. 结尾
        self.conclusion()
    
    def show_series_intro(self):
        """系列开场动画"""
        series_title = Text(
            "视觉化证明经典",
            font_size=50,
            color=PROOF_BLUE,
            weight=BOLD
        )
        
        subtitle = Text(
            "看见数学之美",
            font_size=30,
            color=WHITE
        )
        subtitle.next_to(series_title, DOWN, buff=0.5)
        
        episode_text = Text(
            "第2集：圆周率π的5种推导",
            font_size=34,
            color=PROOF_GREEN
        )
        episode_text.next_to(subtitle, DOWN, buff=0.8)
        
        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.play(FadeIn(episode_text, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(
            FadeOut(series_title),
            FadeOut(subtitle),
            FadeOut(episode_text)
        )
    
    def introduce_pi(self):
        """引入π的神秘"""
        self.clear()
        
        title = Text("最神秘的数学常数", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # π的定义
        definition = VGroup(
            Text("圆周率 π", font_size=SUBTITLE_SIZE, color=PROOF_ORANGE),
            MathTex(r"\pi = \frac{\text{圆周长}}{\text{直径}}", font_size=40),
            Text("= 3.14159265358979323846...", font_size=NORMAL_SIZE, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.5)
        
        for line in definition:
            self.play(Write(line), run_time=0.8)
        
        # 历史
        history = VGroup(
            Text("古巴比伦：π ≈ 3.125", font_size=SMALL_SIZE),
            Text("古埃及：π ≈ 3.1605", font_size=SMALL_SIZE),
            Text("阿基米德：3.1408 < π < 3.1429", font_size=SMALL_SIZE),
            Text("祖冲之：π ≈ 355/113", font_size=SMALL_SIZE, color=PROOF_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        history.shift(DOWN * 1.5)
        
        self.play(
            definition.animate.shift(UP * 0.5),
            LaggedStart(*[Write(h) for h in history], lag_ratio=0.2)
        )
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(definition), FadeOut(history))
    
    def method_1_archimedes(self):
        """方法1：阿基米德多边形逼近"""
        self.clear()
        
        method_num = Text("方法 #1", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        method_num.to_edge(UL)
        
        title = Text("阿基米德多边形逼近法", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(method_num), Write(title))
        
        # 创建圆
        circle = Circle(radius=2, color=WHITE, stroke_width=2)
        circle.shift(LEFT * 3)
        self.play(Create(circle))
        
        # 内接和外切多边形动画
        n_sides_tracker = ValueTracker(6)
        
        # 内接多边形
        inscribed_polygon = RegularPolygon(n=6, radius=2, color=PROOF_GREEN, stroke_width=2)
        inscribed_polygon.shift(LEFT * 3)
        
        # 外切多边形
        circumscribed_polygon = RegularPolygon(
            n=6, 
            radius=2 / np.cos(PI/6), 
            color=PROOF_ORANGE, 
            stroke_width=2
        )
        circumscribed_polygon.shift(LEFT * 3)
        
        self.play(Create(inscribed_polygon), Create(circumscribed_polygon))
        
        # 显示边数
        n_text = Text("n = 6", font_size=NORMAL_SIZE)
        n_text.shift(LEFT * 3 + DOWN * 3)
        n_text.add_updater(
            lambda m: m.become(
                Text(f"n = {int(n_sides_tracker.get_value())}", font_size=NORMAL_SIZE)
                .shift(LEFT * 3 + DOWN * 3)
            )
        )
        
        # π的估计值
        pi_estimate = VGroup(
            Text("π的下界：", font_size=NORMAL_SIZE, color=PROOF_GREEN),
            MathTex("3.000", font_size=NORMAL_SIZE),
            Text("π的上界：", font_size=NORMAL_SIZE, color=PROOF_ORANGE),
            MathTex("3.464", font_size=NORMAL_SIZE)
        ).arrange(DOWN, buff=0.3)
        pi_estimate.shift(RIGHT * 3)
        
        def update_pi_estimate(mob):
            n = int(n_sides_tracker.get_value())
            lower = n * np.sin(PI/n)
            upper = n * np.tan(PI/n)
            mob[1].become(MathTex(f"{lower:.4f}", font_size=NORMAL_SIZE).next_to(mob[0], DOWN, buff=0.3))
            mob[3].become(MathTex(f"{upper:.4f}", font_size=NORMAL_SIZE).next_to(mob[2], DOWN, buff=0.3))
        
        pi_estimate.add_updater(update_pi_estimate)
        
        self.play(Write(n_text), Write(pi_estimate))
        
        # 增加边数
        for n in [12, 24, 48, 96]:
            new_inscribed = RegularPolygon(n=n, radius=2, color=PROOF_GREEN, stroke_width=2)
            new_inscribed.shift(LEFT * 3)
            
            new_circumscribed = RegularPolygon(
                n=n, 
                radius=2 / np.cos(PI/n), 
                color=PROOF_ORANGE, 
                stroke_width=2
            )
            new_circumscribed.shift(LEFT * 3)
            
            self.play(
                Transform(inscribed_polygon, new_inscribed),
                Transform(circumscribed_polygon, new_circumscribed),
                n_sides_tracker.animate.set_value(n),
                run_time=1
            )
        
        # 结论
        conclusion = Text(
            "n→∞时，多边形周长→圆周长",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        conclusion.shift(DOWN * 4)
        self.play(Write(conclusion))
        
        self.wait(2)
        self.play(
            FadeOut(method_num), FadeOut(title), FadeOut(circle),
            FadeOut(inscribed_polygon), FadeOut(circumscribed_polygon),
            FadeOut(n_text), FadeOut(pi_estimate), FadeOut(conclusion)
        )
    
    def method_2_liu_hui(self):
        """方法2：刘徽割圆术"""
        self.clear()
        
        method_num = Text("方法 #2", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        method_num.to_edge(UL)
        
        title = Text("刘徽割圆术（公元263年）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(method_num), Write(title))
        
        # 创建单位圆
        circle = Circle(radius=2, color=WHITE, stroke_width=2)
        self.play(Create(circle))
        
        # 从正六边形开始
        polygon = RegularPolygon(n=6, radius=2, color=PROOF_GREEN, stroke_width=2)
        self.play(Create(polygon))
        
        # 割圆过程
        steps = VGroup(
            Text("1. 从正六边形开始", font_size=SMALL_SIZE),
            Text("2. 每次边数翻倍", font_size=SMALL_SIZE),
            Text("3. 计算多边形面积", font_size=SMALL_SIZE),
            Text("4. 面积逼近圆面积", font_size=SMALL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        steps.shift(RIGHT * 4 + UP * 1)
        
        for step in steps:
            self.play(Write(step), run_time=0.5)
        
        # 面积计算公式
        area_formula = MathTex(
            r"S_n = \frac{n \cdot r^2 \cdot \sin(\frac{2\pi}{n})}{2}",
            font_size=32
        )
        area_formula.shift(RIGHT * 4 + DOWN * 1)
        self.play(Write(area_formula))
        
        # 迭代过程
        iterations = [
            (6, "π ≈ 3.000"),
            (12, "π ≈ 3.106"),
            (24, "π ≈ 3.133"),
            (48, "π ≈ 3.139"),
            (96, "π ≈ 3.141"),
            (192, "π ≈ 3.1414"),
            (3072, "π ≈ 3.14159")
        ]
        
        result_text = Text("", font_size=NORMAL_SIZE, color=PROOF_ORANGE)
        result_text.shift(DOWN * 2.5)
        
        for n, estimate in iterations[:5]:
            new_polygon = RegularPolygon(n=n, radius=2, color=PROOF_GREEN, stroke_width=2)
            new_result = Text(f"n = {n}: {estimate}", font_size=NORMAL_SIZE, color=PROOF_ORANGE)
            new_result.shift(DOWN * 2.5)
            
            self.play(
                Transform(polygon, new_polygon),
                Transform(result_text, new_result),
                run_time=0.8
            )
        
        # 刘徽的成就
        achievement = Text(
            "刘徽用3072边形得到 π ≈ 3.14159",
            font_size=NORMAL_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        achievement.shift(DOWN * 3.5)
        self.play(Write(achievement))
        
        self.wait(2)
        self.play(
            FadeOut(method_num), FadeOut(title), FadeOut(circle),
            FadeOut(polygon), FadeOut(steps), FadeOut(area_formula),
            FadeOut(result_text), FadeOut(achievement)
        )
    
    def method_3_leibniz(self):
        """方法3：莱布尼茨级数"""
        self.clear()
        
        method_num = Text("方法 #3", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        method_num.to_edge(UL)
        
        title = Text("莱布尼茨级数（1674年）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(method_num), Write(title))
        
        # 级数公式
        series = MathTex(
            r"\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots",
            font_size=40
        )
        self.play(Write(series))
        
        # 几何解释：单位圆的1/4
        quarter_circle = Arc(
            radius=2,
            start_angle=0,
            angle=PI/2,
            color=PROOF_ORANGE,
            stroke_width=3
        )
        quarter_circle.shift(LEFT * 3.5 + DOWN * 1)
        
        # 坐标轴
        axes = Axes(
            x_range=[0, 1.2, 0.2],
            y_range=[0, 1.2, 0.2],
            x_length=2.4,
            y_length=2.4,
            axis_config={"include_numbers": True, "font_size": 16}
        )
        axes.shift(LEFT * 3.5 + DOWN * 1)
        
        self.play(
            series.animate.shift(UP * 1.5),
            Create(axes),
            Create(quarter_circle)
        )
        
        # 部分和的可视化
        partial_sums = VGroup()
        sum_value = 0
        terms = []
        
        for i in range(10):
            term = (-1)**i / (2*i + 1)
            sum_value += term
            terms.append(term)
            
            # 创建条形
            bar = Rectangle(
                width=0.15,
                height=abs(term) * 2,
                fill_color=PROOF_GREEN if term > 0 else PROOF_RED,
                fill_opacity=0.7,
                stroke_width=1
            )
            bar.shift(RIGHT * (i * 0.4 - 0.5) + DOWN * 1)
            if term < 0:
                bar.shift(DOWN * abs(term))
            
            partial_sums.add(bar)
        
        partial_sums.shift(RIGHT * 2)
        
        # 逐项添加
        pi_approximation = Text(f"π ≈ {4 * sum_value:.6f}", font_size=NORMAL_SIZE, color=PROOF_PURPLE)
        pi_approximation.shift(RIGHT * 2 + DOWN * 3)
        
        for i, bar in enumerate(partial_sums):
            current_sum = sum(terms[:i+1])
            new_approx = Text(f"π ≈ {4 * current_sum:.6f}", font_size=NORMAL_SIZE, color=PROOF_PURPLE)
            new_approx.shift(RIGHT * 2 + DOWN * 3)
            
            self.play(
                Create(bar),
                Transform(pi_approximation, new_approx) if i > 0 else Write(pi_approximation),
                run_time=0.3
            )
        
        # 收敛性说明
        convergence = Text(
            "收敛很慢，但形式优美",
            font_size=NORMAL_SIZE,
            color=PROOF_CYAN
        )
        convergence.shift(DOWN * 4)
        self.play(Write(convergence))
        
        self.wait(2)
        self.play(
            FadeOut(method_num), FadeOut(title), FadeOut(series),
            FadeOut(axes), FadeOut(quarter_circle), FadeOut(partial_sums),
            FadeOut(pi_approximation), FadeOut(convergence)
        )
    
    def method_4_monte_carlo(self):
        """方法4：蒙特卡洛方法"""
        self.clear()
        
        method_num = Text("方法 #4", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        method_num.to_edge(UL)
        
        title = Text("蒙特卡洛方法（随机模拟）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(method_num), Write(title))
        
        # 创建正方形和内切圆
        square = Square(side_length=4, stroke_color=WHITE, stroke_width=2)
        circle = Circle(radius=2, stroke_color=PROOF_ORANGE, stroke_width=2)
        
        square.shift(LEFT * 3)
        circle.shift(LEFT * 3)
        
        self.play(Create(square), Create(circle))
        
        # 说明文字
        explanation = VGroup(
            Text("在正方形内随机投点", font_size=NORMAL_SIZE),
            MathTex(r"\frac{\text{圆内点数}}{\text{总点数}} \approx \frac{\pi r^2}{4r^2} = \frac{\pi}{4}", font_size=28),
            MathTex(r"\pi \approx 4 \times \frac{\text{圆内点数}}{\text{总点数}}", font_size=32, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(RIGHT * 3 + UP * 1)
        
        for line in explanation:
            self.play(Write(line), run_time=0.6)
        
        # 模拟投点
        random.seed(42)
        points_inside = 0
        points_total = 0
        
        # 计数器
        counter = VGroup(
            Text("总点数：0", font_size=SMALL_SIZE),
            Text("圆内点数：0", font_size=SMALL_SIZE, color=PROOF_GREEN),
            Text("π ≈ 0.000", font_size=NORMAL_SIZE, color=PROOF_PURPLE)
        ).arrange(DOWN, buff=0.2)
        counter.shift(RIGHT * 3 + DOWN * 2)
        
        for text in counter:
            self.play(Write(text), run_time=0.3)
        
        # 投点动画
        for _ in range(100):
            x, y = random.uniform(-2, 2), random.uniform(-2, 2)
            point_pos = LEFT * 3 + RIGHT * x + UP * y
            
            if x**2 + y**2 <= 4:
                color = PROOF_GREEN
                points_inside += 1
            else:
                color = PROOF_RED
            
            points_total += 1
            
            dot = Dot(point_pos, radius=0.03, color=color)
            self.add(dot)
            
            # 更新计数器（每10个点更新一次）
            if points_total % 10 == 0:
                pi_estimate = 4 * points_inside / points_total
                new_counter = VGroup(
                    Text(f"总点数：{points_total}", font_size=SMALL_SIZE),
                    Text(f"圆内点数：{points_inside}", font_size=SMALL_SIZE, color=PROOF_GREEN),
                    Text(f"π ≈ {pi_estimate:.3f}", font_size=NORMAL_SIZE, color=PROOF_PURPLE)
                ).arrange(DOWN, buff=0.2)
                new_counter.shift(RIGHT * 3 + DOWN * 2)
                
                counter.become(new_counter)
        
        # 结果
        result = Text(
            "点数越多，估计越准确",
            font_size=NORMAL_SIZE,
            color=PROOF_CYAN,
            weight=BOLD
        )
        result.shift(DOWN * 3.5)
        self.play(Write(result))
        
        self.wait(2)
        # 清理（保留一些点作为效果）
        self.clear()
    
    def method_5_buffon_needle(self):
        """方法5：布丰投针法"""
        self.clear()
        
        method_num = Text("方法 #5", font_size=SUBTITLE_SIZE, color=PROOF_YELLOW)
        method_num.to_edge(UL)
        
        title = Text("布丰投针法（1777年）", font_size=TITLE_SIZE, color=PROOF_BLUE)
        title.to_edge(UP)
        
        self.play(Write(method_num), Write(title))
        
        # 创建平行线
        lines = VGroup()
        for i in range(5):
            line = Line(
                LEFT * 4 + UP * (i - 2) * 1.5,
                RIGHT * 4 + UP * (i - 2) * 1.5,
                stroke_color=WHITE,
                stroke_width=2
            )
            lines.add(line)
        
        lines.shift(LEFT * 1)
        self.play(Create(lines))
        
        # 说明
        explanation = VGroup(
            Text("平行线间距：d", font_size=NORMAL_SIZE),
            Text("针的长度：l (l < d)", font_size=NORMAL_SIZE),
            Text("随机投针", font_size=NORMAL_SIZE, color=PROOF_ORANGE),
            MathTex(r"P(\text{相交}) = \frac{2l}{\pi d}", font_size=32, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(RIGHT * 4 + UP * 1)
        
        for line in explanation:
            self.play(Write(line), run_time=0.5)
        
        # 模拟投针
        random.seed(42)
        needles = VGroup()
        intersections = 0
        total = 0
        
        # 针的长度（小于线间距）
        needle_length = 1.0
        line_spacing = 1.5
        
        for _ in range(30):
            # 随机位置和角度
            center_x = random.uniform(-3, 3)
            center_y = random.uniform(-3, 3)
            angle = random.uniform(0, PI)
            
            # 计算针的两端
            dx = needle_length * np.cos(angle) / 2
            dy = needle_length * np.sin(angle) / 2
            
            start = np.array([center_x - dx, center_y - dy, 0])
            end = np.array([center_x + dx, center_y + dy, 0])
            
            # 检查是否与线相交
            for i in range(5):
                line_y = (i - 2) * 1.5
                if min(start[1], end[1]) <= line_y <= max(start[1], end[1]):
                    color = PROOF_RED
                    intersections += 1
                    break
            else:
                color = PROOF_GREEN
            
            total += 1
            
            # 创建针
            needle = Line(
                start + LEFT * 1,
                end + LEFT * 1,
                stroke_color=color,
                stroke_width=2
            )
            needles.add(needle)
            
            self.play(Create(needle), run_time=0.1)
        
        # 计算π
        if intersections > 0:
            pi_estimate = (2 * needle_length * total) / (line_spacing * intersections)
        else:
            pi_estimate = 0
        
        # 结果显示
        result = VGroup(
            Text(f"总针数：{total}", font_size=SMALL_SIZE),
            Text(f"相交数：{intersections}", font_size=SMALL_SIZE, color=PROOF_RED),
            MathTex(f"\\pi \\approx \\frac{{2l \\cdot n}}{{d \\cdot m}} = {pi_estimate:.3f}", 
                   font_size=32, color=PROOF_PURPLE)
        ).arrange(DOWN, buff=0.3)
        result.shift(RIGHT * 4 + DOWN * 2)
        
        for line in result:
            self.play(Write(line), run_time=0.5)
        
        self.wait(2)
        self.play(
            FadeOut(method_num), FadeOut(title), FadeOut(lines),
            FadeOut(needles), FadeOut(explanation), FadeOut(result)
        )
    
    def pi_properties(self):
        """π的性质总结"""
        self.clear()
        
        title = Text("π的奇妙性质", font_size=TITLE_SIZE, color=PROOF_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        properties = VGroup(
            Text("• π是无理数（1761年证明）", font_size=NORMAL_SIZE),
            Text("• π是超越数（1882年证明）", font_size=NORMAL_SIZE),
            Text("• π出现在各种公式中", font_size=NORMAL_SIZE),
            MathTex(r"e^{i\pi} + 1 = 0", font_size=32, color=PROOF_GREEN),
            MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}", font_size=32, color=PROOF_ORANGE),
            MathTex(r"\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}", font_size=32, color=PROOF_CYAN)
        ).arrange(DOWN, buff=0.4)
        
        for prop in properties:
            self.play(Write(prop), run_time=0.6)
        
        self.wait(2)
        self.play(FadeOut(title), FadeOut(properties))
    
    def conclusion(self):
        """总结"""
        self.clear()
        
        title = Text("圆周率π：永恒的追求", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 五种方法回顾
        methods = VGroup(
            Text("1. 阿基米德：多边形逼近", font_size=SMALL_SIZE, color=PROOF_BLUE),
            Text("2. 刘徽：割圆术", font_size=SMALL_SIZE, color=PROOF_GREEN),
            Text("3. 莱布尼茨：无穷级数", font_size=SMALL_SIZE, color=PROOF_ORANGE),
            Text("4. 蒙特卡洛：随机模拟", font_size=SMALL_SIZE, color=PROOF_RED),
            Text("5. 布丰：概率方法", font_size=SMALL_SIZE, color=PROOF_CYAN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        for method in methods:
            self.play(Write(method), run_time=0.4)
        
        # 现代记录
        modern = VGroup(
            Text("现代计算：", font_size=NORMAL_SIZE, color=PROOF_YELLOW),
            Text("2021年：62.8万亿位", font_size=NORMAL_SIZE),
            Text("用时：108天", font_size=NORMAL_SIZE)
        ).arrange(DOWN, buff=0.3)
        modern.shift(DOWN * 2)
        
        self.play(Write(modern))
        
        # 哲学意义
        philosophy = Text(
            "简单定义，无穷深邃",
            font_size=SUBTITLE_SIZE,
            color=PROOF_PURPLE,
            weight=BOLD
        )
        philosophy.shift(DOWN * 3.5)
        self.play(Write(philosophy))
        
        self.wait(3)
        
        # 下集预告
        self.play(FadeOut(title), FadeOut(methods), FadeOut(modern), FadeOut(philosophy))
        
        next_episode = VGroup(
            Text("下集预告", font_size=38, color=PROOF_YELLOW),
            Text("第3集：黄金分割的几何构造", font_size=TITLE_SIZE, color=PROOF_PURPLE, weight=BOLD),
            Text("从正五边形到斐波那契", font_size=SUBTITLE_SIZE, color=WHITE),
            MathTex(r"\phi = \frac{1+\sqrt{5}}{2}", font_size=40, color=PROOF_GREEN)
        ).arrange(DOWN, buff=0.5)
        
        for line in next_episode:
            self.play(Write(line), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(next_episode))