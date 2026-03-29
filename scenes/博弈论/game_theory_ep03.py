
"""
GT_EP03: 斗鸡博弈 (Game of Chicken)
狭路相逢勇者胜？还是最疯的人赢？
"""

from manim import *
import numpy as np

# --- 颜色定义 ---
GT_PURPLE = "#8B5CF6"    # 主题色
GT_BLUE = "#3B82F6"      # 玩家A (Blue)
GT_RED = "#EF4444"       # 玩家B (Red)
GT_GREEN = "#10B981"     # 收益/胜利
GT_YELLOW = "#F59E0B"    # 警告/均衡
GT_ORANGE = "#F97316"    # 爆炸/碰撞
GT_GRAY = "#6B7280"      # 背景/中性
BG_COLOR = "#111111"     # 深色背景

class GameTheoryEP03(Scene):
    """博弈论 EP03：斗鸡博弈"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场
        self.intro_transition()
        
        # 2. 场景模拟：两车对撞
        self.setup_car_crash()
        
        # 3. 核心：构建高风险矩阵
        matrix_group, matrix_refs = self.build_payoff_matrix()
        
        # 4. 逻辑推演：寻找均衡点
        self.analyze_strategies(matrix_group, matrix_refs)
        
        # 5. 进阶策略：破局之道
        self.brinkmanship_strategy()
        
        # 6. 现实映射：古巴导弹危机
        self.real_world_application()
        
        # 7. 结尾
        self.show_ending()

    def intro_transition(self):
        old_series = Text("EP02: 智猪博弈 (强弱博弈)", font_size=32, color=GT_GRAY).to_edge(UP)
        new_series = Text("EP03: 斗鸡博弈", font_size=54, color=GT_ORANGE, weight=BOLD)
        subtitle = Text("Game of Chicken: 谁先怂谁输", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        slogan = Text("不想同归于尽？那你得学会发疯", font_size=24, color=GT_YELLOW).next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(slogan))
        self.wait(2)
        self.play(FadeOut(new_series), FadeOut(subtitle), FadeOut(slogan))

    def setup_car_crash(self):
        """场景：两车相向而行"""
        title = Text("经典场景：单行道上的决斗", font_size=32, color=GT_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 道路
        road = VGroup(
            Line(LEFT*6, RIGHT*6, color=WHITE),
            Line(LEFT*6, RIGHT*6, color=WHITE).shift(DOWN*1.5),
            DashedLine(LEFT*6, RIGHT*6, color=GRAY).shift(DOWN*0.75)
        ).shift(UP*0.5)
        
        # 左右两车
        car_a = self.create_car(GT_BLUE).move_to(LEFT*5 + UP*0.1)
        car_b = self.create_car(GT_RED).move_to(RIGHT*5 + UP*0.1)
        # B车翻转朝左
        car_b.flip(axis=UP)
        
        self.play(Create(road), FadeIn(car_a), FadeIn(car_b))
        
        # 动画：冲向中间
        self.play(
            car_a.animate.move_to(LEFT*1 + UP*0.1),
            car_b.animate.move_to(RIGHT*1 + UP*0.1),
            run_time=1.5,
            rate_func=linear
        )
        
        # 暂停，显示选项
        options = VGroup(
            Text("选项 A: 转向 (认怂)", font_size=24, color=GT_GREEN),
            Text("选项 B: 直冲 (硬刚)", font_size=24, color=GT_RED)
        ).arrange(RIGHT, buff=2).next_to(road, DOWN, buff=0.5)
        
        self.play(Write(options))
        
        # 模拟碰撞后果
        boom = Text("💥", font_size=80).move_to(UP*0.1)
        danger_text = Text("最坏结果：同归于尽 (-100)", font_size=28, color=GT_ORANGE).next_to(options, DOWN, buff=0.5)
        
        self.play(FadeIn(boom, scale=0.5), Write(danger_text))
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(road), FadeOut(car_a), FadeOut(car_b),
            FadeOut(options), FadeOut(boom), FadeOut(danger_text)
        )

    def create_car(self, color):
        """简单的汽车图形"""
        body = RoundedRectangle(width=1.2, height=0.6, corner_radius=0.2, fill_color=color, fill_opacity=1)
        top = RoundedRectangle(width=0.7, height=0.4, corner_radius=0.1, fill_color=WHITE, fill_opacity=0.5).shift(UP*0.3)
        wheel1 = Circle(radius=0.15, color=BLACK, fill_opacity=1).shift(LEFT*0.3 + DOWN*0.3)
        wheel2 = Circle(radius=0.15, color=BLACK, fill_opacity=1).shift(RIGHT*0.3 + DOWN*0.3)
        return VGroup(wheel1, wheel2, body, top)

    def build_payoff_matrix(self):
        # 1. 基础矩阵
        side_len = 4.0 
        matrix_bg = Square(side_length=side_len, color=WHITE)
        
        # 分隔线
        h_line = Line(LEFT * side_len/2, RIGHT * side_len/2)
        v_line = Line(UP * side_len/2, DOWN * side_len/2)
        
        # 标签
        strat_a_label = Text("蓝色车", font_size=24, color=GT_BLUE).next_to(matrix_bg, LEFT, buff=0.6).rotate(PI/2)
        strat_b_label = Text("红色车", font_size=24, color=GT_RED).next_to(matrix_bg, UP, buff=0.4)
        
        # 策略名称
        offset = side_len / 4
        a_swerve = Text("转向", font_size=18, color=GT_GREEN).move_to(LEFT*(side_len/2 + 0.4) + UP*offset)
        a_rush = Text("直冲", font_size=18, color=GT_ORANGE).move_to(LEFT*(side_len/2 + 0.4) + DOWN*offset)
        
        b_swerve = Text("转向", font_size=18, color=GT_GREEN).move_to(UP*(side_len/2 + 0.4) + LEFT*offset)
        b_rush = Text("直冲", font_size=18, color=GT_ORANGE).move_to(UP*(side_len/2 + 0.4) + RIGHT*offset)
        
        # 收益数据 (Blue, Red)
        # 左上(都转向): 0, 0 (平局，安全)
        # 右上(蓝转向,红直冲): -1(胆小鬼), +1(英雄)
        # 左下(蓝直冲,红转向): +1(英雄), -1(胆小鬼)
        # 右下(都直冲): -100, -100 (死亡)
        
        cells_group = VGroup()
        matrix_refs = []
        
        data = [
            ("0", "0", GT_GRAY),        # 左上
            ("-1", "+1", GT_GRAY),      # 右上 (均衡点1)
            ("+1", "-1", GT_GRAY),      # 左下 (均衡点2)
            ("-100", "-100", GT_ORANGE) # 右下 (灾难)
        ]
        
        centers = [
            [-offset, offset, 0], [offset, offset, 0],
            [-offset, -offset, 0], [offset, -offset, 0]
        ]
        
        for i, (pa, pb, col) in enumerate(data):
            bg = Square(side_length=side_len/2 - 0.05, fill_color=col, fill_opacity=0.2, stroke_width=0)
            bg.move_to(centers[i])
            nums = VGroup(
                Text(pa, font_size=28, color=GT_BLUE),
                Text(",", font_size=28),
                Text(pb, font_size=28, color=GT_RED)
            ).arrange(RIGHT, buff=0.1).move_to(centers[i])
            
            cell = VGroup(bg, nums)
            cells_group.add(cell)
            matrix_refs.append(cell)

        full_matrix = VGroup(
            matrix_bg, h_line, v_line,
            strat_a_label, strat_b_label,
            a_swerve, a_rush, b_swerve, b_rush,
            cells_group
        )
        
        self.play(Create(matrix_bg), Create(h_line), Create(v_line))
        self.play(Write(strat_a_label), Write(strat_b_label))
        self.play(FadeIn(a_swerve), FadeIn(a_rush), FadeIn(b_swerve), FadeIn(b_rush))
        self.play(FadeIn(cells_group))
        
        return full_matrix, matrix_refs

    def analyze_strategies(self, matrix_group, cells):
        """分析策略：没有绝对的优势"""
        
        # 1. 矩阵左移
        self.play(matrix_group.animate.scale(0.85).to_edge(LEFT, buff=1.0))
        
        # 2. 右侧区域基准
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("蓝车的策略分析：", font_size=26, color=GT_BLUE, weight=BOLD)
        title.move_to(RIGHT_ZONE + UP * 2.5)
        self.play(Write(title))
        
        # --- 情况 1：如果红车【直冲】 ---
        case1 = Text("假设 红车 直冲(疯了)...", font_size=22, color=GT_RED)
        case1.next_to(title, DOWN, buff=0.5)
        self.play(Write(case1))
        
        # 高亮右列 (红车直冲)
        hl_col = SurroundingRectangle(VGroup(cells[1], cells[3]), color=GT_RED, buff=0.1)
        self.play(Create(hl_col))
        
        comp1 = VGroup(
            Text("我直冲: -100 (死)", font_size=20, color=GT_ORANGE),
            Text("我转向: -1 (丢脸但活着)", font_size=20, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(case1, DOWN, buff=0.3)
        self.play(Write(comp1))
        
        # 箭头1 (纵向向上) - 修正 shift
        arrow1 = Arrow(
            start=cells[3].get_center(),
            end=cells[1].get_center(),
            color=GT_BLUE,
            buff=0.4
        ).shift(LEFT*0.2)
        self.play(GrowArrow(arrow1))
        self.wait(1)
        
        # 清理1
        self.play(FadeOut(case1), FadeOut(comp1), FadeOut(hl_col))
        
        # --- 情况 2：如果红车【转向】 ---
        case2 = Text("假设 红车 转向(怂了)...", font_size=22, color=GT_RED)
        case2.next_to(title, DOWN, buff=0.5)
        self.play(Write(case2))
        
        # 高亮左列 (红车转向)
        hl_col2 = SurroundingRectangle(VGroup(cells[0], cells[2]), color=GT_RED, buff=0.1)
        self.play(Create(hl_col2))
        
        comp2 = VGroup(
            Text("我转向: 0 (平局)", font_size=20),
            Text("我直冲: +1 (赢!)", font_size=20, color=GT_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(case2, DOWN, buff=0.3)
        self.play(Write(comp2))
        
        # 箭头2 (纵向向下)
        arrow2 = Arrow(
            start=cells[0].get_center(),
            end=cells[2].get_center(),
            color=GT_BLUE,
            buff=0.4
        ).shift(LEFT*0.2)
        self.play(GrowArrow(arrow2))
        self.wait(1)
        
        # 清理2
        self.play(FadeOut(case2), FadeOut(comp2), FadeOut(hl_col2))
        
        # --- 结论 ---
        concl = Text("没有优势策略！", font_size=24, color=GT_YELLOW, weight=BOLD)
        concl.next_to(title, DOWN, buff=0.5)
        self.play(Write(concl))
        
        desc = Text("我的选择取决于\n对手的选择", font_size=22, color=WHITE, line_spacing=1.2)
        desc.next_to(concl, DOWN, buff=0.3)
        self.play(Write(desc))
        self.wait(1)
        
        # 红车的箭头 (对称的)
        # 红车如果蓝车转向 -> 红车直冲 (左上->右上)
        arrow3 = Arrow(
            start=cells[0].get_center(),
            end=cells[1].get_center(),
            color=GT_RED,
            buff=0.4
        ).shift(UP*0.2)
        
        # 红车如果蓝车直冲 -> 红车转向 (右下->左下)
        arrow4 = Arrow(
            start=cells[3].get_center(),
            end=cells[2].get_center(),
            color=GT_RED,
            buff=0.4
        ).shift(UP*0.2)
        
        self.play(GrowArrow(arrow3), GrowArrow(arrow4))
        
        # 标记两个纳什均衡
        nash1 = SurroundingRectangle(cells[1], color=GT_YELLOW, stroke_width=4) # 右上
        nash2 = SurroundingRectangle(cells[2], color=GT_YELLOW, stroke_width=4) # 左下
        
        self.play(Create(nash1), Create(nash2))
        
        nash_label = Text("两个纳什均衡点", font_size=22, color=GT_YELLOW)
        nash_label.next_to(desc, DOWN, buff=0.5)
        self.play(Write(nash_label))
        
        self.wait(2)
        
        # 清理右侧，准备下一节
        self.play(
            FadeOut(title), FadeOut(concl), FadeOut(desc), FadeOut(nash_label),
            FadeOut(nash1), FadeOut(nash2), FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4)
        )

    def brinkmanship_strategy(self):
            """进阶策略：边缘政策"""
            
            # 定义右侧基准
            RIGHT_ZONE = RIGHT * 3.5
            
            # 1. 标题
            title = Text("如何必胜？", font_size=28, color=GT_PURPLE, weight=BOLD)
            title.move_to(RIGHT_ZONE + UP * 2.5)
            self.play(Write(title))
            
            # 2. 策略描述 (上部文字区)
            strategy_text = VGroup(
                Text("如果我想赢(直冲)，", font_size=22),
                Text("我就必须让对手相信：", font_size=22),
                Text("我不怕死 / 我疯了", font_size=22, color=GT_ORANGE, weight=BOLD),
                Text("从而迫使对手转向。", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            strategy_text.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(strategy_text))
            self.wait(1)
            
            # 3. 方向盘动画 (下部图形区)
            wheel = Circle(radius=0.8, color=WHITE, stroke_width=8)
            spokes = VGroup(
                Line(UP*0.8, DOWN*0.8, color=WHITE, stroke_width=8),
                Line(LEFT*0.8, RIGHT*0.8, color=WHITE, stroke_width=8)
            )
            steering_wheel = VGroup(wheel, spokes).move_to(RIGHT_ZONE + DOWN * 1.0)
            
            self.play(Create(steering_wheel))
            
            # 4. 扔掉方向盘 (文字位置修复)
            # 原来是 next_to(..., UP)，导致撞上 strategy_text
            # 现在改为 next_to(..., DOWN)，放在最底部，彻底解决重叠
            throw_text = Text("最佳策略：\n当着对手的面，扔掉方向盘！", font_size=20, color=GT_YELLOW)
            throw_text.next_to(steering_wheel, DOWN, buff=0.4)
            
            self.play(Write(throw_text))
            
            # 飞出动画
            self.play(
                steering_wheel.animate.rotate(PI*2).shift(RIGHT*4 + UP*2).scale(0.1).set_opacity(0),
                run_time=1.5
            )
            
            # 5. 总结解释
            # 放在 strategy_text 下方较远的位置，避开之前的区域
            logic = Text("限制自己的选择 = 增加可信度", font_size=20, color=GT_GREEN)
            # 使用 absolute positioning 确保位置准确
            logic.move_to(RIGHT_ZONE + DOWN * 0.2)
            
            self.play(Write(logic))
            
            self.wait(3)
            self.clear()
    def real_world_application(self):
        title = Text("现实映射：古巴导弹危机 (1962)", font_size=32, color=GT_PURPLE).to_edge(UP)
        self.play(Write(title))
        
        # 地图/国家示意
        us = VGroup(Text("美国", font_size=32, color=GT_BLUE), Text("肯尼迪", font_size=20)).arrange(DOWN)
        ussr = VGroup(Text("苏联", font_size=32, color=GT_RED), Text("赫鲁晓夫", font_size=20)).arrange(DOWN)
        
        us.move_to(LEFT * 4)
        ussr.move_to(RIGHT * 4)
        
        self.play(FadeIn(us), FadeIn(ussr))
        
        # 导弹图标
        missile = Text("🚀", font_size=60).move_to(ORIGIN)
        self.play(FadeIn(missile))
        
        # 僵局描述
        standoff = VGroup(
            Text("谁先撤退谁就是\"胆小鬼\"", font_size=24, color=GT_YELLOW),
            Text("谁都不撤就是全面核战", font_size=24, color=GT_ORANGE)
        ).arrange(DOWN, buff=0.2).next_to(missile, DOWN, buff=0.5)
        
        self.play(Write(standoff))
        self.wait(2)
        
        # 解决
        resolution = Text("最终：苏联撤回导弹，美国承诺不入侵古巴", font_size=24, color=GT_GREEN)
        resolution.to_edge(DOWN, buff=1.0)
        self.play(Write(resolution))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_ending(self):
        summary = VGroup(
            Text("1. 斗鸡博弈有两个纳什均衡，没有绝对优劣", font_size=26),
            Text("2. 胜利的关键在于展示\"绝不退让\"的决心", font_size=26),
            Text("3. 限制自己的选择权，反而能获得主动权", font_size=26, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
        
        # 预告
        next_ep = Text("下期预告：拍卖的数学", font_size=40, color=GT_YELLOW)
        desc = Text("为什么赢了拍卖的人往往是亏本的？\n赢家诅咒是什么？", font_size=24, color=GT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)