"""
GT_EP02: 智猪博弈 (Boxed Pigs Game)
大公司创新，小公司抄袭？弱者如何搭便车？
"""

from manim import *
import numpy as np

# --- 颜色定义 (保持统一) ---
GT_PURPLE = "#8B5CF6"    # 主题色
GT_BLUE = "#3B82F6"      # 大猪 (强者)
GT_RED = "#EF4444"       # 小猪 (弱者)
GT_GREEN = "#10B981"     # 收益/正面
GT_YELLOW = "#F59E0B"    # 按钮/食物
GT_GRAY = "#6B7280"      # 背景/中性
BG_COLOR = "#111111"     # 深色背景

class GameTheoryEP02(Scene):
    """博弈论 EP02：智猪博弈"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：强弱不对称
        self.intro_transition()
        
        # 2. 场景模拟：猪圈的构造
        self.setup_pig_pen()
        
        # 3. 核心：构建非对称矩阵
        matrix_group, matrix_refs = self.build_payoff_matrix()
        
        # 4. 逻辑推演：小猪的占优策略 (先看小猪)
        self.analyze_small_pig(matrix_group, matrix_refs)
        
        # 5. 逻辑推演：大猪的无奈 (再看大猪)
        self.analyze_big_pig(matrix_refs)
        
        # 6. 现实映射：商业与股市
        self.real_world_application()
        
        # 7. 结尾
        self.show_ending()

    def intro_transition(self):
        old_series = Text("EP01: 囚徒困境 (对称博弈)", font_size=32, color=GT_GRAY).to_edge(UP)
        new_series = Text("EP02: 智猪博弈", font_size=54, color=GT_PURPLE, weight=BOLD)
        subtitle = Text("当强者遇上弱者，谁会赢？", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        # 核心概念展示
        tagline = Text("搭便车 (Free Rider)", font_size=36, color=GT_YELLOW).next_to(subtitle, DOWN, buff=1.0)
        self.play(Write(tagline))
        self.wait(2)
        
        self.play(FadeOut(new_series), FadeOut(subtitle), FadeOut(tagline))

    def setup_pig_pen(self):
        """可视化猪圈场景"""
        title = Text("思想实验：这个槽里有两头猪", font_size=32, color=GT_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 猪圈背景
        pen = Rectangle(width=10, height=2.5, color=WHITE, stroke_width=4)
        
        # 左边：按钮
        button = VGroup(
            Rectangle(width=0.5, height=1.5, fill_color=GT_RED, fill_opacity=0.8),
            Text("按\n钮", font_size=16, color=WHITE)
        ).arrange(ORIGIN)
        button.move_to(pen.get_left() + RIGHT * 0.5)
        
        # 右边：食槽
        trough = VGroup(
            Rectangle(width=1.5, height=1.0, color=GT_YELLOW, fill_opacity=0.3),
            Text("食槽", font_size=20, color=GT_YELLOW)
        ).arrange(ORIGIN)
        trough.move_to(pen.get_right() + LEFT * 1.0)
        
        # 大猪和小猪
        big_pig = self.create_pig("大猪", GT_BLUE, 0.7).move_to(pen.get_center() + LEFT * 2)
        small_pig = self.create_pig("小猪", GT_RED, 0.45).move_to(pen.get_center() + RIGHT * 2)
        
        scene_group = VGroup(pen, button, trough, big_pig, small_pig)
        self.play(Create(scene_group))
        
        # 规则说明 (放在下方，居中)
        rules = VGroup(
            Text("1. 按按钮需要消耗 2 单位体力", font_size=24, color=GT_GRAY),
            Text("2. 食槽会掉落 10 单位食物", font_size=24, color=GT_YELLOW),
            Text("3. 谁去按按钮，谁就晚吃到食物", font_size=24, color=WHITE)
        ).arrange(DOWN,  buff=0.2)
        rules.next_to(pen, DOWN, buff=0.5)
        
        self.play(Write(rules))
        self.wait(3)
        
        # 清理，保留大猪小猪图标用于后续矩阵
        self.play(
            FadeOut(title), FadeOut(pen), FadeOut(button), FadeOut(trough), FadeOut(rules),
            FadeOut(big_pig), FadeOut(small_pig)
        )

    def create_pig(self, name, color, scale_val):
        body = Circle(radius=scale_val, color=color, fill_opacity=0.5)
        snout = Ellipse(width=scale_val, height=scale_val*0.6, color=color, fill_opacity=0.8)
        label = Text(name, font_size=20*scale_val*2.5, color=WHITE)
        return VGroup(body, snout, label)

    def build_payoff_matrix(self):
        # 1. 基础矩阵结构 (尺寸缩小适应屏幕)
        side_len = 4.0 
        matrix_bg = Square(side_length=side_len, color=WHITE)
        
        # 分隔线
        h_line = Line(LEFT * side_len/2, RIGHT * side_len/2)
        v_line = Line(UP * side_len/2, DOWN * side_len/2)
        
        # 标签 (左侧大猪，上方小猪)
        strat_big_label = Text("大猪", font_size=24, color=GT_BLUE).next_to(matrix_bg, LEFT, buff=0.6).rotate(PI/2)
        strat_small_label = Text("小猪", font_size=24, color=GT_RED).next_to(matrix_bg, UP, buff=0.4)
        
        # 策略名称
        offset = side_len / 4
        big_press = Text("按", font_size=18, color=GT_BLUE).move_to(LEFT*(side_len/2 + 0.4) + UP*offset)
        big_wait = Text("等", font_size=18, color=GT_BLUE).move_to(LEFT*(side_len/2 + 0.4) + DOWN*offset)
        
        small_press = Text("按", font_size=18, color=GT_RED).move_to(UP*(side_len/2 + 0.4) + LEFT*offset)
        small_wait = Text("等", font_size=18, color=GT_RED).move_to(UP*(side_len/2 + 0.4) + RIGHT*offset)
        
        # 收益数据 (Big, Small)
        # 假设总食量10，成本2
        # 左上(都按): 大猪吃7-2=5, 小猪吃3-2=1
        # 右上(大按小等): 大猪吃6-2=4, 小猪吃4 (小猪先吃很多)
        # 左下(大等小按): 大猪吃9, 小猪吃1-2=-1 (小猪会饿死)
        # 右下(都等): 0, 0
        
        cells_group = VGroup()
        matrix_refs = []
        
        data = [
            ("5", "1", GT_GRAY),    # 左上
            ("4", "4", GT_GRAY),    # 右上 (纳什均衡)
            ("9", "-1", GT_GRAY),   # 左下
            ("0", "0", GT_GRAY)     # 右下
        ]
        
        centers = [
            [-offset, offset, 0], [offset, offset, 0],
            [-offset, -offset, 0], [offset, -offset, 0]
        ]
        
        for i, (pb, ps, col) in enumerate(data):
            bg = Square(side_length=side_len/2 - 0.05, fill_color=col, fill_opacity=0.2, stroke_width=0)
            bg.move_to(centers[i])
            nums = VGroup(
                Text(pb, font_size=32, color=GT_BLUE),
                Text(",", font_size=32),
                Text(ps, font_size=32, color=GT_RED)
            ).arrange(RIGHT, buff=0.1).move_to(centers[i])
            
            cell = VGroup(bg, nums)
            cells_group.add(cell)
            matrix_refs.append(cell)

        full_matrix = VGroup(
            matrix_bg, h_line, v_line,
            strat_big_label, strat_small_label,
            big_press, big_wait, small_press, small_wait,
            cells_group
        )
        
        self.play(Create(matrix_bg), Create(h_line), Create(v_line))
        self.play(Write(strat_big_label), Write(strat_small_label))
        self.play(FadeIn(big_press), FadeIn(big_wait), FadeIn(small_press), FadeIn(small_wait))
        self.play(FadeIn(cells_group))
        
        return full_matrix, matrix_refs

    def analyze_small_pig(self, matrix_group, cells):
        """分析小猪的策略：为什么小猪一定会等待？"""
        
        # 1. 矩阵左移
        self.play(matrix_group.animate.scale(0.85).to_edge(LEFT, buff=1.0))
        
        # 2. 右侧分析区域
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("小猪的思考：", font_size=26, color=GT_RED, weight=BOLD)
        title.move_to(RIGHT_ZONE + UP * 2.5)
        self.play(Write(title))
        
        # --- 情况 1：大猪去按按钮 ---
        case1 = Text("如果大猪去【按】...", font_size=22, color=GT_BLUE)
        case1.next_to(title, DOWN, buff=0.5)
        self.play(Write(case1))
        
        # 高亮第一行 (大猪按)
        hl_row1 = SurroundingRectangle(VGroup(cells[0], cells[1]), color=GT_BLUE, buff=0.1)
        self.play(Create(hl_row1))
        
        comp1 = VGroup(
            Text("我去按: 得 1", font_size=20),
            Text("我等待: 得 4 (赢!)", font_size=20, color=GT_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(case1, DOWN, buff=0.3)
        self.play(Write(comp1))
        
        # 小猪箭头1 (横向)
        arrow1 = Arrow(
            start=cells[0].get_center(),
            end=cells[1].get_center(),
            color=GT_RED,
            buff=0.4
        ).shift(DOWN*0.2) # 稍微向下偏移避开数字
        self.play(GrowArrow(arrow1))
        self.wait(1)
        
        # 清理1
        self.play(FadeOut(case1), FadeOut(comp1), FadeOut(hl_row1))
        
        # --- 情况 2：大猪等待 ---
        case2 = Text("如果大猪也【等】...", font_size=22, color=GT_BLUE)
        case2.next_to(title, DOWN, buff=0.5)
        self.play(Write(case2))
        
        # 高亮第二行 (大猪等)
        hl_row2 = SurroundingRectangle(VGroup(cells[2], cells[3]), color=GT_BLUE, buff=0.1)
        self.play(Create(hl_row2))
        
        comp2 = VGroup(
            Text("我去按: 得 -1 (亏本)", font_size=20),
            Text("我等待: 得 0 (没亏)", font_size=20, color=GT_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(case2, DOWN, buff=0.3)
        self.play(Write(comp2))
        
        # 小猪箭头2
        arrow2 = Arrow(
            start=cells[2].get_center(),
            end=cells[3].get_center(),
            color=GT_RED,
            buff=0.4
        ).shift(DOWN*0.2)
        self.play(GrowArrow(arrow2))
        self.wait(1)
        
        # 清理2
        self.play(FadeOut(case2), FadeOut(comp2), FadeOut(hl_row2))
        
        # --- 小猪结论 ---
        concl = Text("小猪发现：\n无论大猪做什么，我都该等待！", font_size=24, color=GT_RED, line_spacing=1.2)
        concl.next_to(title, DOWN, buff=0.5)
        self.play(Write(concl))
        
        dominant_label = Text("【搭便车】是优势策略", font_size=24, color=GT_YELLOW, weight=BOLD)
        dominant_label.next_to(concl, DOWN, buff=0.5)
        self.play(Write(dominant_label))
        
        self.wait(2)
        
        # 清理右侧，准备分析大猪
        self.play(
            FadeOut(title), FadeOut(concl), FadeOut(dominant_label)
        )
        self.small_pig_arrows = VGroup(arrow1, arrow2) # 保存以便最后一起消失

    def analyze_big_pig(self, cells):
            """分析大猪的策略：被迫勤劳"""
            
            # 1. 定义右侧对齐基准线
            RIGHT_ZONE = RIGHT * 3.5
            
            # 2. 标题 (位置不变)
            title = Text("大猪的思考：", font_size=26, color=GT_BLUE, weight=BOLD)
            title.move_to(RIGHT_ZONE + UP * 2.5)
            self.play(Write(title))
            
            # 3. 步骤1
            step1 = Text("我知道小猪肯定会【等】", font_size=22, color=GT_RED)
            step1.next_to(title, DOWN, buff=0.4)
            self.play(Write(step1))
            
            # 高亮右列 (小猪等)
            hl_col = SurroundingRectangle(VGroup(cells[1], cells[3]), color=GT_RED, buff=0.1)
            self.play(Create(hl_col))
            
            # 4. 比较逻辑
            comp = VGroup(
                Text("我等待: 得 0 (一起饿死)", font_size=20),
                Text("我去按: 得 4 (只能这样)", font_size=20, color=GT_YELLOW)
            ).arrange(DOWN, aligned_edge=LEFT).next_to(step1, DOWN, buff=0.3)
            self.play(Write(comp))
            
            # 大猪箭头 (纵向)
            arrow3 = Arrow(
                start=cells[3].get_center(),
                end=cells[1].get_center(),
                color=GT_BLUE,
                buff=0.4
            ).shift(LEFT*0.2) # 向左偏移避开数字
            self.play(GrowArrow(arrow3))
            
            # 均衡点高亮 (右上角)
            nash_rect = SurroundingRectangle(cells[1], color=GT_YELLOW, stroke_width=5)
            self.play(Create(nash_rect))
            
            # 5. 结论 (纳什均衡) - 修复布局重叠
            # 原来是 next_to(nash_rect)，现在改为 next_to(comp) 向下排列
            final_text = VGroup(
                Text("纳什均衡", font_size=28, color=GT_YELLOW, weight=BOLD),
                Text("大猪按按钮", font_size=22, color=GT_BLUE),
                Text("小猪搭便车", font_size=22, color=GT_RED)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            
            # 核心修改：放在比较文字下方，留出充足间距
            final_text.next_to(comp, DOWN, buff=0.8)
            # 强制左对齐，保持整洁
            final_text.align_to(title, LEFT)
            
            self.play(Write(final_text))
            
            self.wait(3)
            self.clear()

    def real_world_application(self):
        title = Text("现实映射：股市与商业", font_size=32, color=GT_PURPLE).to_edge(UP)
        self.play(Write(title))
        
        # 1. 商业研发
        corp_group = VGroup(
            Text("大公司 (大猪)", font_size=24, color=GT_BLUE),
            Text("投入巨资研发创新", font_size=20),
            Text("获得部分利润", font_size=20, color=GT_GRAY)
        ).arrange(DOWN).move_to(LEFT * 3)
        
        small_corp_group = VGroup(
            Text("小公司 (小猪)", font_size=24, color=GT_RED),
            Text("等待并模仿", font_size=20),
            Text("低成本获利", font_size=20, color=GT_GRAY)
        ).arrange(DOWN).move_to(RIGHT * 3)
        
        arrow = Arrow(LEFT, RIGHT, color=GT_YELLOW)
        label = Text("技术溢出", font_size=18).next_to(arrow, UP)
        
        self.play(FadeIn(corp_group), FadeIn(small_corp_group))
        self.play(GrowArrow(arrow), Write(label))
        self.wait(2)
        
        # 2. 股市散户
        self.play(FadeOut(corp_group), FadeOut(small_corp_group), FadeOut(arrow), FadeOut(label))
        
        stock_text = VGroup(
            Text("股市中的智猪博弈：", font_size=28, color=GT_YELLOW),
            Text("机构 (大猪)：花费高成本调研挖掘价值", font_size=24, color=GT_BLUE),
            Text("散户 (小猪)：跟随机构动向，搭便车", font_size=24, color=GT_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(stock_text))
        self.wait(3)
        
        self.play(FadeOut(title), FadeOut(stock_text))

    def show_ending(self):
        summary = VGroup(
            Text("1. 弱者最好的策略往往是\"等待\"", font_size=26),
            Text("2. 强者因为利益大，被迫承担责任", font_size=26),
            Text("3. 多劳者多得，但不一定是最优比", font_size=26, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
        
        # 预告
        next_ep = Text("下期预告：斗鸡博弈", font_size=40, color=GT_YELLOW)
        desc = Text("狭路相逢勇者胜？\n还是最疯的人赢？", font_size=24, color=GT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
