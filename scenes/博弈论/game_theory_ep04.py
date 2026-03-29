from manim import *
import numpy as np
import random

# --- 颜色定义 ---
GT_PURPLE = "#8B5CF6"    # 主题色
GT_BLUE = "#3B82F6"      # 竞标者A / 策略A
GT_RED = "#EF4444"       # 竞标者B / 策略B
GT_GREEN = "#10B981"     # 真实价值/收益
GT_YELLOW = "#F59E0B"    # 货币/出价
GT_ORANGE = "#F97316"    # 亏损/诅咒
GT_GRAY = "#6B7280"      # 中性
BG_COLOR = "#111111"     # 深色背景

class GameTheoryEP04(Scene):
    """博弈论 EP04：拍卖的数学 (布局终极修复版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场
        self.intro_transition()
        
        # 2. 场景：猜猜有多少钱？
        jar_group = self.setup_coin_jar()
        
        # 3. 拍卖形式对比 (英式 vs 荷式)
        self.compare_auction_types(jar_group)
        
        # 4. 核心悖论：赢家诅咒 (修复重叠)
        self.explain_winners_curse()
        
        # 5. 解决方案：维克里拍卖 (修复重叠)
        self.vickrey_solution()
        
        # 6. 结尾
        self.show_ending()

    def intro_transition(self):
        old_series = Text("EP03: 斗鸡博弈 (胆量博弈)", font_size=32, color=GT_GRAY).to_edge(UP)
        new_series = Text("EP04: 拍卖的数学", font_size=54, color=GT_YELLOW, weight=BOLD)
        subtitle = Text("如何赢得比赛，但这值得吗？", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        slogan = Text("The Winner's Curse (赢家诅咒)", font_size=36, color=GT_ORANGE).next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(slogan))
        self.wait(2)
        
        self.play(FadeOut(new_series), FadeOut(subtitle), FadeOut(slogan))

    def setup_coin_jar(self):
        """场景：硬币罐子（公共价值拍卖）"""
        
        LEFT_ZONE = LEFT * 3.5
        
        # 1. 绘制罐子
        jar_body = RoundedRectangle(width=2.5, height=3.5, corner_radius=0.2, color=WHITE, stroke_width=4)
        jar_lid = Rectangle(width=2.7, height=0.3, fill_color=GT_GRAY, fill_opacity=1).next_to(jar_body, UP, buff=0)
        
        # 2. 生成硬币
        coins = VGroup()
        for _ in range(30):
            coin = Circle(radius=0.15, fill_color=GT_YELLOW, fill_opacity=0.8, stroke_color=GOLD, stroke_width=2)
            x_pos = random.uniform(-1.0, 1.0)
            y_pos = random.uniform(-1.5, 1.5)
            coin.move_to(jar_body.get_center() + np.array([x_pos, y_pos, 0]))
            coins.add(coin)
            
        # 3. 标签 (直接加入 jar_group，确保一起消失)
        label = Text("这里有多少钱？", font_size=28, color=WHITE).next_to(jar_lid, UP, buff=0.5)
        true_value = Text("真实价值: $100", font_size=24, color=GT_GREEN).next_to(jar_body, DOWN, buff=0.5)
        
        jar_group = VGroup(jar_body, coins, jar_lid, label, true_value).move_to(LEFT_ZONE)
        
        # 动画
        self.play(Create(jar_body), Create(jar_lid), Write(label))
        self.play(FadeIn(coins, lag_ratio=0.1))
        self.play(Write(true_value))
        
        return jar_group

    def compare_auction_types(self, jar_group):
        """对比英式和荷式拍卖"""
        
        RIGHT_ZONE = RIGHT * 3.0
        
        # 标题
        title = Text("如何卖掉这个罐子？", font_size=32, color=GT_PURPLE).move_to(RIGHT_ZONE + UP * 2.5)
        self.play(Write(title))
        
        # --- 1. 英式拍卖 ---
        english_title = Text("1. 英式拍卖 (公开叫价)", font_size=24, color=GT_BLUE, weight=BOLD)
        english_title.next_to(title, DOWN, buff=0.6).align_to(title, LEFT)
        self.play(Write(english_title))
        
        price_tracker = ValueTracker(10)
        dollar_sign = Text("$", font_size=36, color=GT_BLUE)
        price_num = Integer(10, font_size=36, color=GT_BLUE).next_to(dollar_sign, RIGHT, buff=0.1)
        price_label = VGroup(dollar_sign, price_num).next_to(english_title, DOWN, buff=0.2)
        
        up_arrow = Arrow(
            start=price_label.get_right() + RIGHT*0.2 + DOWN*0.2,
            end=price_label.get_right() + RIGHT*0.2 + UP*0.2,
            color=GT_BLUE, buff=0
        ).shift(RIGHT * 0.1)
        
        self.play(FadeIn(price_label), GrowArrow(up_arrow))
        
        self.play(price_tracker.animate.set_value(110), run_time=1.5)
        price_num.add_updater(lambda m: m.set_value(price_tracker.get_value()))
        self.wait(0.5)
        price_num.clear_updaters()
        
        english_desc = Text("价格由低到高，直到剩一人", font_size=20, color=GT_GRAY).next_to(price_label, DOWN, buff=0.2).align_to(title, LEFT)
        self.play(Write(english_desc))
        
        self.wait(1)
        
        # --- 2. 荷式拍卖 ---
        dutch_title = Text("2. 荷式拍卖 (降价拍卖)", font_size=24, color=GT_RED, weight=BOLD)
        dutch_title.next_to(english_desc, DOWN, buff=0.8).align_to(title, LEFT)
        self.play(Write(dutch_title))
        
        price_tracker_d = ValueTracker(200)
        dollar_sign_d = Text("$", font_size=36, color=GT_RED)
        price_num_d = Integer(200, font_size=36, color=GT_RED).next_to(dollar_sign_d, RIGHT, buff=0.1)
        price_label_d = VGroup(dollar_sign_d, price_num_d).next_to(dutch_title, DOWN, buff=0.2)
        
        down_arrow = Arrow(
            start=price_label_d.get_right() + RIGHT*0.2 + UP*0.2,
            end=price_label_d.get_right() + RIGHT*0.2 + DOWN*0.2,
            color=GT_RED, buff=0
        ).shift(RIGHT * 0.1)
        
        self.play(FadeIn(price_label_d), GrowArrow(down_arrow))
        
        self.play(price_tracker_d.animate.set_value(110), run_time=1.5)
        price_num_d.add_updater(lambda m: m.set_value(price_tracker_d.get_value()))
        self.wait(0.5)
        price_num_d.clear_updaters()
        
        dutch_desc = Text("价格由高到低，直到有人接受", font_size=20, color=GT_GRAY).next_to(price_label_d, DOWN, buff=0.2).align_to(title, LEFT)
        self.play(Write(dutch_desc))
        
        thm = Text("收益等价定理：\n理论上，两者的最终成交价相同", font_size=22, color=GT_GREEN)
        thm.next_to(dutch_desc, DOWN, buff=0.6).align_to(title, LEFT)
        self.play(Write(thm))
        
        self.wait(3)
        # 清理所有 (包含 jar_group 中的标签)
        self.play(
            FadeOut(title), FadeOut(english_title), FadeOut(price_label), FadeOut(up_arrow), FadeOut(english_desc),
            FadeOut(dutch_title), FadeOut(price_label_d), FadeOut(down_arrow), FadeOut(dutch_desc), FadeOut(thm),
            FadeOut(jar_group) 
        )

    def explain_winners_curse(self):
        """核心：解释赢家诅咒 (布局重构)"""
        
        title = Text("核心悖论：赢家诅咒", font_size=36, color=GT_ORANGE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 绘制数轴 (大幅下移，留出上方空间)
        axis = NumberLine(
            x_range=[60, 140, 10],
            length=10,
            color=WHITE,
            include_numbers=True,
            font_size=20
        ).shift(DOWN * 1.5) # 下移至 -1.5
        
        axis_label = Text("竞标者的估值 ($)", font_size=24).next_to(axis, DOWN, buff=0.5)
        
        self.play(Create(axis), Write(axis_label))
        
        # 2. 真实价值线 (放在数轴上方)
        true_val_line = DashedLine(axis.n2p(100) + UP*2.5, axis.n2p(100), color=GT_GREEN)
        true_val_label = Text("真实价值\n$100", font_size=24, color=GT_GREEN).next_to(true_val_line, UP)
        
        self.play(Create(true_val_line), Write(true_val_label))
        
        # 3. 模拟竞标者
        bids = np.random.normal(100, 10, 15) 
        bids.sort()
        dots = VGroup()
        for bid in bids:
            dot = Dot(axis.n2p(bid), color=GT_BLUE, radius=0.08)
            dots.add(dot)
        self.play(FadeIn(dots, lag_ratio=0.1))
        
        # 平均值说明 (放在左上角，远离中心)
        text_avg = Text("平均估值 ≈ 真实价值", font_size=24, color=GT_BLUE).to_edge(LEFT, buff=1.0).shift(UP * 1.0)
        self.play(Write(text_avg))
        
        # 4. 赢家 (最右侧)
        winner_dot = dots[-1]
        winner_bid = bids[-1]
        
        self.play(
            winner_dot.animate.set_color(GT_RED).scale(2),
            dots[:-1].animate.set_opacity(0.3)
        )
        
        # 赢家标签 (在数轴下方，防止遮挡上方的大括号)
        winner_arrow = Arrow(start=winner_dot.get_center()+DOWN*0.8, end=winner_dot.get_center(), color=GT_RED)
        winner_label = Text("赢家\n(出价最高)", font_size=20, color=GT_RED).next_to(winner_arrow, DOWN)
        self.play(GrowArrow(winner_arrow), Write(winner_label))
        
        # 5. 亏损展示 (使用上方大括号)
        overpayment = winner_bid - 100
        curse_brace = BraceBetweenPoints(axis.n2p(100), axis.n2p(winner_bid), color=GT_ORANGE, direction=UP)
        # 将文字放在大括号上方
        curse_text = Text(f"溢价: ${overpayment:.1f}\n(亏损)", font_size=24, color=GT_ORANGE).next_to(curse_brace, UP)
        
        self.play(Create(curse_brace), Write(curse_text))
        
        # 6. 总结 (右上角，独立区域)
        summary = VGroup(
            Text("为了赢得拍卖，", font_size=24),
            Text("你必须是那个", font_size=24),
            Text("估值最离谱的人。", font_size=24, color=GT_ORANGE, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(RIGHT, buff=1.0).shift(UP * 1.0)
        
        self.play(Write(summary))
        self.wait(3)
        
        self.play(FadeOut(Group(*self.mobjects)))

    def vickrey_solution(self):
        """解决方案：二价拍卖 (三段式布局修复)"""
        title = Text("如何避免诅咒？二价拍卖", font_size=36, color=GT_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 规则说明 (放在最上方，字体缩小)
        rule_text = VGroup(
            Text("维克里拍卖规则：", font_size=24, color=GT_YELLOW),
            Text("1. 密封递价，最高者得", font_size=22),
            Text("2. 只需支付第二高的价格！", font_size=24, color=GT_RED, weight=BOLD)
        ).arrange(DOWN)
        
        rule_bg = SurroundingRectangle(rule_text, color=GT_GRAY, fill_opacity=0.1, buff=0.2)
        rule_group = VGroup(rule_bg, rule_text).move_to(UP * 2.0)
        
        self.play(FadeIn(rule_group))
        
        # 2. 真实估值 (中间)
        val_text = Text("假设你的真实估值: $100", font_size=26, color=GT_GREEN).move_to(UP * 0.5)
        self.play(Write(val_text))
        
        # 3. 策略对比 (左右分栏，位于下方)
        # 左侧：诚实出价
        col_left = VGroup(
            Text("策略A: 诚实出价 $100", font_size=22, color=GT_BLUE, weight=BOLD),
            Text("若第二高 $90  -> 赚$10", font_size=20),
            Text("若第二高 $110 -> 没买到", font_size=20, color=GT_GRAY),
            Text("(安全)", font_size=20, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        col_left.move_to(LEFT * 3.5 + DOWN * 1.5)
        
        # 右侧：虚高出价
        col_right = VGroup(
            Text("策略B: 虚高出价 $120", font_size=22, color=GT_RED, weight=BOLD),
            Text("若第二高 $90  -> 赚$10 (没变)", font_size=20),
            Text("若第二高 $110 -> 买到了!", font_size=20),
            Text("但支付$110 > 价值$100", font_size=20, color=GT_ORANGE),
            Text("结果：亏损 $10", font_size=20, color=GT_ORANGE, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        # 顶部对齐
        col_right.move_to(RIGHT * 3.5 + DOWN * 1.5)
        col_right.align_to(col_left, UP)
        
        # 分隔线
        divider = Line(UP*0.5, DOWN*3.0, color=GT_GRAY).move_to(DOWN * 1.25)
        
        self.play(Write(col_left))
        self.play(Create(divider))
        self.play(Write(col_right))
        
        # 4. 结论 (最底部)
        conclusion = Text("结论：诚实报价是优势策略！", font_size=28, color=GT_YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_ending(self):
        summary = VGroup(
            Text("1. 在公共价值拍卖中，赢家往往是\"高估者\"", font_size=26),
            Text("2. 为了不亏本，你应该调低你的出价", font_size=26),
            Text("3. 二价拍卖不仅公平，还能鼓励人们说真话", font_size=26, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
        
        # 预告
        next_ep = Text("下期预告：进化博弈论", font_size=40, color=GT_YELLOW)
        desc = Text("为什么自然界会有利他行为？\n鹰与鸽的生存游戏。", font_size=24, color=GT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)