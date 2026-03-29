"""
GT_EP05: 进化博弈论 (Evolutionary Game Theory)
鹰鸽博弈：为什么好斗者不能彻底消灭和平者？
"""

from manim import *
import numpy as np
import random

# --- 颜色定义 ---
GT_PURPLE = "#8B5CF6"    # 主题色
GT_RED = "#EF4444"       # 鹰 (Hawk) - 好斗
GT_BLUE = "#3B82F6"      # 鸽 (Dove) - 和平
GT_GREEN = "#10B981"     # 资源/食物
GT_YELLOW = "#F59E0B"    # 警告/均衡
GT_GRAY = "#6B7280"      # 中性
BG_COLOR = "#111111"     # 深色背景

class GameTheoryEP05(Scene):
    """博弈论 EP05：进化博弈论"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场
        self.intro_transition()
        
        # 2. 核心模型：鹰鸽博弈矩阵
        # 返回 matrix_group 用于后续清理
        matrix_group = self.setup_hawk_dove_matrix()
        
        # 3. 动态模拟：种群演化
        # 这一步会清理掉矩阵
        self.simulate_evolution(matrix_group)
        
        # 4. 现实意义：仪式化斗争
        self.real_world_implication()
        
        # 5. 系列大结局
        self.show_series_ending()

    def intro_transition(self):
        old_series = Text("EP04: 拍卖理论 (信息博弈)", font_size=32, color=GT_GRAY).to_edge(UP)
        new_series = Text("EP05: 进化博弈论", font_size=54, color=GT_GREEN, weight=BOLD)
        subtitle = Text("从个人理性 -> 群体生存", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        slogan = Text("Survival of the Fittest (适者生存)", font_size=36, color=GT_YELLOW).next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(slogan))
        self.wait(2)
        
        self.play(FadeOut(new_series), FadeOut(subtitle), FadeOut(slogan))

    def setup_hawk_dove_matrix(self):
        """构建鹰鸽博弈矩阵与规则"""
        
        # 1. 标题
        title = Text("鹰鸽博弈 (Hawk-Dove Game)", font_size=36, color=GT_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 2. 矩阵构建 (左侧)
        side_len = 3.5
        matrix_bg = Square(side_length=side_len, color=WHITE)
        h_line = Line(LEFT * side_len/2, RIGHT * side_len/2)
        v_line = Line(UP * side_len/2, DOWN * side_len/2)
        
        # 标签
        player1 = Text("玩家A", font_size=20, color=WHITE).next_to(matrix_bg, LEFT, buff=0.6).rotate(PI/2)
        player2 = Text("玩家B", font_size=20, color=WHITE).next_to(matrix_bg, UP, buff=0.4)
        
        # 策略名
        offset = side_len / 4
        h_label_a = Text("鹰 (打)", font_size=18, color=GT_RED).move_to(LEFT*(side_len/2 + 0.4) + UP*offset)
        d_label_a = Text("鸽 (跑)", font_size=18, color=GT_BLUE).move_to(LEFT*(side_len/2 + 0.4) + DOWN*offset)
        h_label_b = Text("鹰", font_size=18, color=GT_RED).move_to(UP*(side_len/2 + 0.4) + LEFT*offset)
        d_label_b = Text("鸽", font_size=18, color=GT_BLUE).move_to(UP*(side_len/2 + 0.4) + RIGHT*offset)
        
        centers = [
            [-offset, offset, 0], [offset, offset, 0],
            [-offset, -offset, 0], [offset, -offset, 0]
        ]
        
        cells_content = VGroup()
        cell_data = [
            ("-25", "-25", GT_RED),   # 鹰鹰
            ("50", "0", GT_YELLOW),   # 鹰鸽
            ("0", "50", GT_YELLOW),   # 鸽鹰
            ("25", "25", GT_BLUE)     # 鸽鸽
        ]
        
        for i, (p1, p2, col) in enumerate(cell_data):
            bg = Square(side_length=side_len/2 - 0.05, fill_color=col, fill_opacity=0.2, stroke_width=0)
            bg.move_to(centers[i])
            txt = VGroup(
                Text(p1, font_size=24, color=GT_RED), 
                Text(",", font_size=24), 
                Text(p2, font_size=24, color=GT_BLUE)
            ).arrange(RIGHT, buff=0.1).move_to(centers[i])
            cells_content.add(bg, txt)
            
        matrix_full = VGroup(
            matrix_bg, h_line, v_line, player1, player2,
            h_label_a, d_label_a, h_label_b, d_label_b,
            cells_content
        ).move_to(LEFT * 3.5)
        
        self.play(Create(matrix_bg), Create(h_line), Create(v_line))
        self.play(Write(player1), Write(player2))
        self.play(Write(h_label_a), Write(d_label_a), Write(h_label_b), Write(d_label_b))
        self.play(FadeIn(cells_content))
        
        # 3. 规则解释 (右侧流式布局)
        RIGHT_ZONE = RIGHT * 3.0
        
        rule_title = Text("生存规则：", font_size=26, color=GT_GREEN).move_to(RIGHT_ZONE + UP * 2.0)
        self.play(Write(rule_title))
        
        # 规则 1: V & C
        rule1 = VGroup(
            Text("资源价值 V = 50", font_size=22),
            Text("受伤代价 C = 100", font_size=22, color=GT_RED)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(rule_title, DOWN, buff=0.4)
        self.play(Write(rule1))
        
        # 规则 2: 遭遇战
        rule2 = VGroup(
            Text("🦅 vs 🦅: 严重受伤 (-25)", font_size=22, color=GT_RED),
            Text("🦅 vs 🕊️: 鹰独吞 (50)", font_size=22, color=GT_YELLOW),
            Text("🕊️ vs 🕊️: 和平分享 (25)", font_size=22, color=GT_BLUE)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(rule1, DOWN, buff=0.4)
        self.play(Write(rule2))
        
        # 规则 3: 进化逻辑 (修复位置)
        rule3_bg = Rectangle(width=5, height=1.2, fill_color=GT_GRAY, fill_opacity=0.2)
        rule3_text = Text("收益高 -> 繁殖更多后代\n收益低 -> 逐渐灭绝", font_size=20, color=GT_GREEN)
        rule3 = VGroup(rule3_bg, rule3_text).next_to(rule2, DOWN, buff=0.6)
        
        # --- 核心修复 ---
        # 原来是 align_to(rule_title, LEFT)，导致宽方块向右溢出
        # 现在强制设置 X 坐标为 3.5 (右侧区域的中心)，确保左右都不超界
        rule3.set_x(3.5)
        
        self.play(FadeIn(rule3))
        self.wait(3)
        
        # 返回整个大组，方便后续清除
        full_scene = VGroup(title, matrix_full, rule_title, rule1, rule2, rule3)
        return full_scene
    def simulate_evolution(self, previous_scene):
        """模拟种群演化过程"""
        
        # 清理上一幕
        self.play(FadeOut(previous_scene))
        
        # 1. 场景搭建
        # 左侧：培养皿 (Petri Dish)
        dish_radius = 2.2
        dish = Circle(radius=dish_radius, color=WHITE, stroke_width=4).move_to(LEFT * 3.5)
        dish_label = Text("生物群落", font_size=24).next_to(dish, UP)
        
        # 右侧：统计条 (Bar Chart)
        bar_axis = Line(LEFT*1.5, RIGHT*1.5).move_to(RIGHT * 3.5 + DOWN * 1.5)
        bar_hawk = Rectangle(width=0.8, height=0.1, fill_color=GT_RED, fill_opacity=1).move_to(bar_axis.get_center() + LEFT*0.6 + UP*0.05)
        bar_dove = Rectangle(width=0.8, height=0.1, fill_color=GT_BLUE, fill_opacity=1).move_to(bar_axis.get_center() + RIGHT*0.6 + UP*0.05)
        
        label_h = Text("鹰", font_size=20, color=GT_RED).next_to(bar_hawk, DOWN)
        label_d = Text("鸽", font_size=20, color=GT_BLUE).next_to(bar_dove, DOWN)
        
        right_group = VGroup(bar_axis, bar_hawk, bar_dove, label_h, label_d)
        
        # 阶段标题 (右上)
        phase_title = Text("阶段 1: 鸽子乐园", font_size=32, color=GT_BLUE).move_to(RIGHT * 3.5 + UP * 2.5)
        
        self.play(Create(dish), Write(dish_label), FadeIn(right_group), Write(phase_title))
        
        # 2. 初始状态：全是鸽子
        dots = VGroup()
        num_dots = 30
        for _ in range(num_dots):
            # 随机分布在圆内
            r = np.sqrt(random.random()) * (dish_radius - 0.2)
            theta = random.random() * 2 * PI
            dot = Dot(radius=0.08, color=GT_BLUE).move_to(dish.get_center() + np.array([r*np.cos(theta), r*np.sin(theta), 0]))
            dots.add(dot)
            
        self.play(FadeIn(dots))
        self.play(bar_dove.animate.stretch_to_fit_height(3.0, about_edge=DOWN))
        
        expl_1 = Text("和平分享，收益 25", font_size=20, color=GT_BLUE).next_to(phase_title, DOWN)
        self.play(Write(expl_1))
        self.wait(1)
        
        # 3. 突变：一只鹰出现
        self.play(FadeOut(phase_title), FadeOut(expl_1))
        phase_title_2 = Text("阶段 2: 鹰的入侵", font_size=32, color=GT_RED).move_to(RIGHT * 3.5 + UP * 2.5)
        self.play(Write(phase_title_2))
        
        # 变异一只
        mutant = dots[0]
        self.play(mutant.animate.set_color(GT_RED).scale(1.5))
        
        expl_2 = Text("鹰独吞资源(50)，疯狂繁殖", font_size=20, color=GT_RED).next_to(phase_title_2, DOWN)
        self.play(Write(expl_2))
        
        # 鹰数量激增
        new_hawks = VGroup()
        for i in range(1, 20): # 变大部分为鹰
            dots[i].generate_target()
            dots[i].target.set_color(GT_RED)
        
        self.play(
            [MoveToTarget(d) for d in dots[1:20]],
            bar_hawk.animate.stretch_to_fit_height(2.5, about_edge=DOWN),
            bar_dove.animate.stretch_to_fit_height(1.0, about_edge=DOWN),
            run_time=2
        )
        self.wait(1)
        
        # 4. 崩溃：鹰太多了
        self.play(FadeOut(phase_title_2), FadeOut(expl_2))
        phase_title_3 = Text("阶段 3: 内卷崩溃", font_size=32, color=ORANGE).move_to(RIGHT * 3.5 + UP * 2.5)
        self.play(Write(phase_title_3))
        
        expl_3 = Text("鹰遇见鹰 (-25)，大家都亏损", font_size=20, color=ORANGE).next_to(phase_title_3, DOWN)
        self.play(Write(expl_3))
        
        # 模拟打架震动
        self.play(dots.animate.shift(RIGHT*0.1), run_time=0.1)
        self.play(dots.animate.shift(LEFT*0.2), run_time=0.1)
        self.play(dots.animate.shift(RIGHT*0.1), run_time=0.1)
        
        # 鹰数量减少
        self.play(
            [d.animate.set_color(GT_BLUE) for d in dots[15:25]], # 部分变回鸽子（或是鸽子繁殖更快）
            bar_hawk.animate.stretch_to_fit_height(1.5, about_edge=DOWN),
            bar_dove.animate.stretch_to_fit_height(1.5, about_edge=DOWN),
            run_time=2
        )
        
        # 5. 最终：进化稳定策略 (ESS)
        self.play(FadeOut(phase_title_3), FadeOut(expl_3))
        phase_title_4 = Text("最终: 进化稳定 (ESS)", font_size=32, color=GT_GREEN).move_to(RIGHT * 3.5 + UP * 2.5)
        self.play(Write(phase_title_4))
        
        expl_4 = Text("鹰鸽比例达到动态平衡", font_size=20, color=GT_GREEN).next_to(phase_title_4, DOWN)
        
        # 均衡公式 (V/C)
        # 只有当 (鸽收益 = 鹰收益) 时才稳定
        # 鹰收益 = p(-25) + (1-p)(50)
        # 鸽收益 = p(0) + (1-p)(25)
        # 计算得 p = V/C = 50/100 = 0.5
        math_ess = MathTex(r"\text{Hawk} \% = \frac{V}{C} = \frac{50}{100} = 50\%", color=GT_YELLOW).scale(0.8)
        math_ess.next_to(expl_4, DOWN, buff=0.5)
        
        self.play(Write(expl_4), Write(math_ess))
        self.wait(3)
        
        # 清理所有
        self.play(
            FadeOut(dish), FadeOut(dish_label), FadeOut(dots),
            FadeOut(right_group), FadeOut(phase_title_4), FadeOut(expl_4), FadeOut(math_ess)
        )

    def real_world_implication(self):
        """现实意义"""
        title = Text("为什么我们不互相残杀？", font_size=36, color=GT_PURPLE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 左右对比
        # 左：雄鹿打架 (Ritualized)
        left_text = VGroup(
            Text("雄鹿争夺配偶", font_size=24, color=GT_BLUE),
            Text("1. 比嗓门 (吼叫)", font_size=20),
            Text("2. 比体型 (展示)", font_size=20),
            Text("3. 极少真打 (避免重伤)", font_size=20, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(LEFT * 3)
        
        # 右：人类社会
        right_text = VGroup(
            Text("人类社会规范", font_size=24, color=GT_RED),
            Text("1. 法律与道德", font_size=20),
            Text("2. 产权制度", font_size=20),
            Text("3. 将争斗转化为\"竞标\"", font_size=20, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(RIGHT * 3)
        
        self.play(FadeIn(left_text), FadeIn(right_text))
        
        # 核心结论
        center_text = Text("限制过度暴力，符合群体的最大利益", font_size=28, color=GT_YELLOW)
        center_text.move_to(DOWN * 2)
        self.play(Write(center_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_series_ending(self):
        """第一季完结撒花"""
        
        # 标题
        end_title = Text("博弈论系列 (第一季) 完", font_size=48, color=GT_PURPLE)
        end_title.move_to(UP * 0.5)
        
        # 回顾
        review = Text("囚徒困境 · 智猪博弈 · 斗鸡博弈 · 拍卖 · 进化", font_size=24, color=GRAY)
        review.next_to(end_title, DOWN, buff=0.5)
        
        self.play(Write(end_title), Write(review))
        
        # 下一季预告 (无穷与悖论)
        next_series = VGroup(
            Text("下一季预告：", font_size=28, color=GT_YELLOW),
            Text("无穷与悖论：数学的深渊", font_size=40, color=WHITE, weight=BOLD),
            Text("希尔伯特旅馆 · 芝诺悖论 · 罗素悖论", font_size=24, color=GT_BLUE)
        ).arrange(DOWN, buff=0.3)
        next_series.move_to(DOWN * 2.0)
        
        self.play(FadeIn(next_series, shift=UP))
        self.wait(3)
        
        # 最终淡出
        self.play(FadeOut(Group(*self.mobjects)))
