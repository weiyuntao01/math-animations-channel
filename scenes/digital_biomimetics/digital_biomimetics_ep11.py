"""
数字仿生系列 第11集：共生的博弈论
Digital Biomimetics EP11: Game Theory of Symbiosis

视频号优化版：超大字体、生活化场景、金句传播
"""

from manim import *
import numpy as np
from typing import List, Tuple

# 系列通用色彩
BIO_CYAN = ManimColor("#00FFE5")
BIO_PURPLE = ManimColor("#8B5CF6")
BIO_GREEN = ManimColor("#00FF88")
BIO_BLUE = ManimColor("#007EFF")
BIO_YELLOW = ManimColor("#FFE500")
BIO_RED = ManimColor("#FF0066")
BIO_WHITE = ManimColor("#FFFFFF")
BIO_GRAY = ManimColor("#303030")

# EP11 主题色
COOP_GREEN = ManimColor("#10B981")     # 合作绿
DEFECT_RED = ManimColor("#EF4444")     # 背叛红
WIN_WIN_GOLD = ManimColor("#F59E0B")   # 双赢金
GAME_BLUE = ManimColor("#3B82F6")      # 博弈蓝

# 视频号超大字体
MEGA_TITLE_SIZE = 64      # 超超大标题
TITLE_SIZE = 52           # 超大标题
SUBTITLE_SIZE = 40        # 大标题
NORMAL_SIZE = 32          # 正常文字
SMALL_SIZE = 28           # 最小文字


class DigitalBiomimeticsEP11(Scene):
    """数字仿生系列 第11集 - 共生的博弈论"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        # 1. 开场钩子（10秒）
        self.show_series_intro()
        
        # 2. 囚徒困境场景（30秒）
        self.restaurant_dilemma()
        
        # 3. 重复博弈策略（25秒）
        self.repeated_game()
        
        # 4. 现实应用（15秒）
        self.real_applications()
        
        # 5. 哲学升华（10秒）
        self.show_ending()

    def show_series_intro(self):
        """系列开场 + 问题钩子 - 15秒"""
        # 标准系列开场（5秒）
        series_title = Text("数字仿生", font_size=60, color=BIO_CYAN, weight=BOLD)
        episode_text = Text("第11集：共生的博弈论", font_size=36, color=COOP_GREEN)
        episode_text.next_to(series_title, DOWN, buff=0.5)
        
        self.play(Write(series_title), run_time=1)
        self.play(FadeIn(episode_text), run_time=0.8)
        self.wait(1)
        self.play(FadeOut(series_title), FadeOut(episode_text), run_time=0.5)
        # 直接的问题钩子
        question = Text(
            "为什么有些人",
            font_size=TITLE_SIZE,
            color=BIO_YELLOW
        )
        question2 = Text(
            "总能双赢？",
            font_size=TITLE_SIZE,
            color=BIO_YELLOW
        )
        question2.next_to(question, DOWN, buff=0.3)
        
        self.play(Write(question), run_time=1)
        self.play(Write(question2), run_time=1)
        self.wait(2)
        
        # 简单的对比
        vs_group = VGroup()
        
        # 左边：对抗
        fight_icon = Text("⚔️", font_size=80)
        fight_label = Text("对抗思维", font_size=NORMAL_SIZE, color=DEFECT_RED)
        fight_result = Text("两败俱伤", font_size=SMALL_SIZE, color=DEFECT_RED)
        fight_side = VGroup(fight_icon, fight_label, fight_result)
        fight_side.arrange(DOWN, buff=0.3)
        fight_side.shift(LEFT * 3)
        
        # 右边：合作
        coop_icon = Text("🤝", font_size=80)
        coop_label = Text("合作思维", font_size=NORMAL_SIZE, color=COOP_GREEN)
        coop_result = Text("共同受益", font_size=SMALL_SIZE, color=COOP_GREEN)
        coop_side = VGroup(coop_icon, coop_label, coop_result)
        coop_side.arrange(DOWN, buff=0.3)
        coop_side.shift(RIGHT * 3)
        
        vs_text = Text("VS", font_size=50, color=BIO_WHITE, weight=BOLD)
        
        self.play(
            FadeOut(question), FadeOut(question2),
            run_time=1
        )
        
        self.play(
            FadeIn(fight_side, shift=UP*0.3),
            Write(vs_text),
            FadeIn(coop_side, shift=UP*0.3),
            run_time=2
        )
        
        # 引出主题
        hook = Text(
            "秘密藏在数学里",
            font_size=SUBTITLE_SIZE,
            color=WIN_WIN_GOLD,
            weight=BOLD
        )
        hook.shift(DOWN * 2.5)
        self.play(Write(hook), run_time=1)
        
        self.wait(1)
        self.play(
            FadeOut(fight_side), FadeOut(vs_text), FadeOut(coop_side),
            FadeOut(hook), run_time=1
        )

    def restaurant_dilemma(self):
        """餐厅降价困境 - 30秒"""
        # 标题
        title = Text("两家餐厅的选择", font_size=TITLE_SIZE, color=GAME_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        
        # 创建两家餐厅
        restaurant_a = self.create_restaurant("餐厅A", LEFT * 3.5, BIO_BLUE)
        restaurant_b = self.create_restaurant("餐厅B", RIGHT * 3.5, BIO_PURPLE)
        
        self.play(
            FadeIn(restaurant_a, shift=UP*0.5),
            FadeIn(restaurant_b, shift=UP*0.5),
            run_time=1.5
        )
        
        # 选择问题
        choice_question = Text(
            "要不要降价抢客户？",
            font_size=SUBTITLE_SIZE,
            color=BIO_YELLOW,
            weight=BOLD
        )
        choice_question.move_to([0, 0.5, 0])
        self.play(Write(choice_question), run_time=1)
        
        # 简化的收益矩阵（用表情和文字，不用数字）
        matrix_title = Text("四种结果", font_size=NORMAL_SIZE, color=BIO_WHITE)
        matrix_title.move_to([0, -0.8, 0])
        self.play(Write(matrix_title), run_time=0.5)
        
        # 2x2矩阵，用简单的表情和文字
        outcomes = VGroup()
        
        # 都不降价 - 双赢
        outcome1 = VGroup(
            Text("😊😊", font_size=40),
            Text("都赚钱", font_size=SMALL_SIZE, color=COOP_GREEN)
        ).arrange(DOWN, buff=0.2)
        outcome1.move_to([-1.5, -1.8, 0])
        
        # A降B不降 - A赢B输
        outcome2 = VGroup(
            Text("😎😢", font_size=40),
            Text("A大赚", font_size=SMALL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.2)
        outcome2.move_to([1.5, -1.8, 0])
        
        # A不降B降 - A输B赢
        outcome3 = VGroup(
            Text("😢😎", font_size=40),
            Text("B大赚", font_size=SMALL_SIZE, color=BIO_YELLOW)
        ).arrange(DOWN, buff=0.2)
        outcome3.move_to([-1.5, -2.8, 0])
        
        # 都降价 - 双输
        outcome4 = VGroup(
            Text("😭😭", font_size=40),
            Text("都不赚", font_size=SMALL_SIZE, color=DEFECT_RED)
        ).arrange(DOWN, buff=0.2)
        outcome4.move_to([1.5, -2.8, 0])
        
        outcomes.add(outcome1, outcome2, outcome3, outcome4)
        
        # 逐个展示结果
        for i, outcome in enumerate(outcomes):
            self.play(FadeIn(outcome, scale=0.8), run_time=0.5)
        
        self.wait(2)
        
        # 关键洞察
        insight = Text(
            "理性选择：都降价",
            font_size=SUBTITLE_SIZE,
            color=DEFECT_RED,
            weight=BOLD
        )
        insight.shift(DOWN * 3.5)
        self.play(Write(insight), run_time=1)
        
        paradox = Text(
            "结果：大家都不赚钱",
            font_size=NORMAL_SIZE,
            color=BIO_YELLOW
        )
        paradox.next_to(insight, DOWN, buff=0.3)
        self.play(Write(paradox), run_time=1)
        
        self.wait(3)
        self.play(
            FadeOut(title), FadeOut(restaurant_a), FadeOut(restaurant_b),
            FadeOut(choice_question), FadeOut(matrix_title), FadeOut(outcomes),
            FadeOut(insight), FadeOut(paradox),
            run_time=2
        )

    def create_restaurant(self, name, position, color):
        """创建餐厅图标"""
        restaurant = VGroup()
        
        # 建筑图标（简化）
        building = Rectangle(width=1.5, height=1.2, fill_color=color, fill_opacity=0.3, stroke_color=color, stroke_width=3)
        roof = Polygon(
            [-0.75, 0.6, 0], [0, 1, 0], [0.75, 0.6, 0],
            fill_color=color, fill_opacity=0.5
        )
        
        # 餐厅名字
        label = Text(name, font_size=NORMAL_SIZE, color=color, weight=BOLD)
        label.next_to(building, DOWN, buff=0.3)
        
        restaurant.add(building, roof, label)
        restaurant.move_to(position)
        return restaurant

    def repeated_game(self):
        """重复博弈策略 - 25秒"""
        title = Text("如果明天还要见面？", font_size=TITLE_SIZE, color=WIN_WIN_GOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        
        # 创建两个角色
        player_a = self.create_simple_player("小明", LEFT * 3, BIO_BLUE)
        player_b = self.create_simple_player("小红", RIGHT * 3, BIO_PURPLE)
        
        self.play(
            FadeIn(player_a, shift=UP*0.3),
            FadeIn(player_b, shift=UP*0.3),
            run_time=1
        )
        
        # 策略说明
        strategy_title = Text("以德报德策略", font_size=SUBTITLE_SIZE, color=COOP_GREEN, weight=BOLD)
        strategy_title.move_to([0, 1, 0])
        self.play(Write(strategy_title), run_time=1)
        
        rule = Text(
            "你对我好，我就对你好",
            font_size=NORMAL_SIZE,
            color=BIO_YELLOW
        )
        rule.next_to(strategy_title, DOWN, buff=0.3)
        self.play(Write(rule), run_time=1)
        
        # 演示几轮互动
        rounds_title = Text("连续5天的选择", font_size=NORMAL_SIZE, color=BIO_WHITE)
        rounds_title.move_to([0, -0.5, 0])
        self.play(Write(rounds_title), run_time=0.5)
        
        # 创建5轮的结果展示
        rounds_display = VGroup()
        for i in range(5):
            day_label = Text(f"第{i+1}天", font_size=SMALL_SIZE, color=BIO_GRAY)
            
            # 都选择合作（绿色笑脸）
            cooperation = Text("😊", font_size=30, color=COOP_GREEN)
            vs_text = Text("vs", font_size=20, color=BIO_WHITE)
            cooperation2 = Text("😊", font_size=30, color=COOP_GREEN)
            
            day_result = VGroup(cooperation, vs_text, cooperation2).arrange(RIGHT, buff=0.2)
            
            round_group = VGroup(day_label, day_result).arrange(DOWN, buff=0.2)
            round_group.scale(0.8)
            
            # 水平排列5天
            round_group.move_to([i*2.5 - 5, -1.5, 0])
            rounds_display.add(round_group)
        
        # 逐天显示
        for round_group in rounds_display:
            self.play(FadeIn(round_group, scale=0.9), run_time=0.4)
        
        # 结果
        win_win = Text(
            "结果：天天双赢！",
            font_size=SUBTITLE_SIZE,
            color=WIN_WIN_GOLD,
            weight=BOLD
        )
        win_win.shift(DOWN * 2.8)
        self.play(Write(win_win), run_time=1)
        
        self.wait(3)
        self.play(
            FadeOut(title), FadeOut(player_a), FadeOut(player_b),
            FadeOut(strategy_title), FadeOut(rule), FadeOut(rounds_title),
            FadeOut(rounds_display), FadeOut(win_win),
            run_time=1
        )

    def create_simple_player(self, name, position, color):
        """创建简单的玩家角色"""
        player = VGroup()
        
        # 简单的头像（圆圈）
        avatar = Circle(radius=0.4, fill_color=color, fill_opacity=0.7, stroke_color=color, stroke_width=2)
        
        # 名字
        label = Text(name, font_size=NORMAL_SIZE, color=color, weight=BOLD)
        label.next_to(avatar, DOWN, buff=0.3)
        
        player.add(avatar, label)
        player.move_to(position)
        return player

    def real_applications(self):
        """现实应用 - 15秒"""
        title = Text("生活中的博弈", font_size=TITLE_SIZE, color=GAME_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 三个应用场景，水平排列
        applications = VGroup()
        
        # 1. 商业合作
        business = VGroup(
            Text("🏢", font_size=60),
            Text("商业合作", font_size=NORMAL_SIZE, color=COOP_GREEN, weight=BOLD),
            Text("长期共赢", font_size=SMALL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, buff=0.3)
        business.shift(LEFT * 4)
        
        # 2. 生态共生
        ecology = VGroup(
            Text("🌱", font_size=60),
            Text("生态共生", font_size=NORMAL_SIZE, color=COOP_GREEN, weight=BOLD),
            Text("互利互惠", font_size=SMALL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, buff=0.3)
        
        # 3. 人际关系
        relationship = VGroup(
            Text("❤️", font_size=60),
            Text("人际关系", font_size=NORMAL_SIZE, color=COOP_GREEN, weight=BOLD),
            Text("信任建立", font_size=SMALL_SIZE, color=BIO_WHITE)
        ).arrange(DOWN, buff=0.3)
        relationship.shift(RIGHT * 4)
        
        applications.add(business, ecology, relationship)
        
        for app in applications:
            self.play(FadeIn(app, shift=UP*0.5), run_time=0.8)
        
        # 核心规律
        rule_text = Text(
            "规律：重复博弈改变游戏",
            font_size=SUBTITLE_SIZE,
            color=WIN_WIN_GOLD,
            weight=BOLD
        )
        rule_text.shift(DOWN * 2.5)
        self.play(Write(rule_text), run_time=1)
        
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(applications), FadeOut(rule_text),
            run_time=1
        )

    def show_ending(self):
        """哲学升华结尾 - 10秒"""
        # 系列标识
        series_logo = Text("数字仿生", font_size=40, color=BIO_CYAN)
        episode_title = Text("第11集：共生的博弈论", font_size=28, color=BIO_WHITE)
        episode_title.next_to(series_logo, DOWN, buff=0.3)
        
        header = VGroup(series_logo, episode_title)
        header.to_edge(UP, buff=0.5)
        self.play(FadeIn(header), run_time=1)
        
        # 核心金句
        wisdom = VGroup()
        
        line1 = Text(
            "真正的智慧",
            font_size=TITLE_SIZE,
            color=BIO_WHITE
        )
        
        line2 = Text(
            "不是战胜对手",
            font_size=TITLE_SIZE,
            color=BIO_YELLOW
        )
        
        line3 = Text(
            "而是创造共赢",
            font_size=MEGA_TITLE_SIZE,
            color=WIN_WIN_GOLD,
            weight=BOLD
        )
        
        wisdom.add(line1, line2, line3)
        wisdom.arrange(DOWN, buff=0.4)
        wisdom.move_to([0, 0.5, 0])
        
        self.play(Write(line1), run_time=1)
        self.play(Write(line2), run_time=1)
        self.play(Write(line3), line3.animate.scale(1.1), run_time=2)
        
        # 数学本质
        math_essence = Text(
            "这就是博弈论的智慧",
            font_size=NORMAL_SIZE,
            color=BIO_CYAN
        )
        math_essence.shift(DOWN * 2.5)
        self.play(Write(math_essence), run_time=1)
        
        self.wait(3)
        
        # 淡出准备下期预告
        self.play(
            FadeOut(header), FadeOut(wisdom), FadeOut(math_essence),
            run_time=1
        )
        
        # 下期预告
        self.show_next_episode_preview()

    def show_next_episode_preview(self):
        """下期预告"""
        preview_title = Text("下期预告", font_size=SUBTITLE_SIZE, color=BIO_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title), run_time=0.5)

        # 左列：最终章标题 + 副标题（更聚拢，避免压底部）
        finale_title = Text(
            "第12集：生命的数学定理",
            font_size=TITLE_SIZE,
            color=BIO_PURPLE,
            weight=BOLD
        )
        subtitle = Text(
            "系列终章",
            font_size=SUBTITLE_SIZE,
            color=WIN_WIN_GOLD
        )
        left_col = VGroup(finale_title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # 右列：预告要点 + 期待语（上下分组，整体右列排列）
        preview_content = VGroup(
            Text("所有生命形态的", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("终极方程", font_size=SUBTITLE_SIZE, color=BIO_CYAN, weight=BOLD),
            Text("数学与生命的", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("最美对话", font_size=SUBTITLE_SIZE, color=BIO_GREEN, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        anticipation = Text(
            "敬请期待终极篇章",
            font_size=NORMAL_SIZE,
            color=BIO_YELLOW
        )
        right_col = VGroup(preview_content, anticipation).arrange(DOWN, aligned_edge=LEFT, buff=0.6)

        # 两列结构：顶边对齐，列间距增大防重叠
        columns = VGroup(left_col, right_col).arrange(RIGHT, aligned_edge=UP, buff=2.8)
        columns.next_to(preview_title, DOWN, buff=0.8)

        # 分步呈现，避免同屏过多对象
        self.play(Write(finale_title), run_time=0.8)
        self.play(Write(subtitle), run_time=0.6)

        for line in preview_content:
            self.play(Write(line), run_time=0.5)
        self.play(Write(anticipation), run_time=0.6)

        self.wait(2)
        self.play(
            FadeOut(preview_title), FadeOut(columns),
            run_time=1
        )