from manim import *
import numpy as np

# --- 颜色定义 ---
GT_PURPLE = "#8B5CF6"    # 主题色
GT_BLUE = "#3B82F6"      # Alice
GT_RED = "#EF4444"       # Bob
GT_GREEN = "#10B981"     # 帕累托最优
GT_YELLOW = "#F59E0B"    # 纳什均衡
GT_GRAY = "#6B7280"      # 中性灰
BG_COLOR = "#111111"     # 深色背景建议

class GameTheoryEP01(Scene):
    """博弈论 EP01：囚徒困境 (修复版)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 震撼开场
        self.intro_transition()
        
        # 2. 故事引入
        self.introduce_scenario()
        
        # 3. 核心：构建矩阵
        # 注意：这里返回 matrix_group 和 matrix_object(包含内部引用)
        matrix_group, matrix_refs = self.build_payoff_matrix()
        
        # 4. 逻辑推演 (含报错修复和布局优化)
        self.analyze_strategies(matrix_group, matrix_refs)
        
        # 5. 概念提炼
        self.define_nash_equilibrium(matrix_refs)
        
        # 6. 现实映射
        self.real_world_application()
        
        # 7. 结尾
        self.show_ending()

    def intro_transition(self):
        old_series = Text("概率论：人 vs 自然", font_size=32, color=GT_GRAY).to_edge(UP)
        new_series = Text("博弈论：人 vs 人", font_size=54, color=GT_PURPLE, weight=BOLD)
        subtitle = Text("EP01: 囚徒困境", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        slogan = Text("当你的命运取决于对手的选择...", font_size=22, color=GT_YELLOW).next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(slogan))
        self.wait(2)
        self.play(FadeOut(new_series), FadeOut(subtitle), FadeOut(slogan))

    def introduce_scenario(self):
        # 标题置顶
        title = Text("经典思想实验：囚徒困境", font_size=36, color=GT_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 左右布局，拉大间距防止中间文字重叠
        alice = self.create_player("Alice", GT_BLUE, LEFT * 5)
        bob = self.create_player("Bob", GT_RED, RIGHT * 5)
        
        self.play(FadeIn(alice), FadeIn(bob))
        
        # 规则文本放在中间，缩小字号
        rules_bg = Rectangle(width=8, height=4, fill_color=BLACK, fill_opacity=0.8, stroke_width=0)
        rules = VGroup(
            Text("警察的规则：", font_size=24, color=GT_YELLOW, weight=BOLD),
            Text("1. 都不招供：各判 1 年", font_size=22),
            Text("2. 都招供：各判 5 年", font_size=22),
            Text("3. 一人招，一人不招：", font_size=22),
            Text("   招供者释放(0年)，不招者判 10 年", font_size=22, color=GT_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        
        rules_group = VGroup(rules_bg, rules).move_to(ORIGIN)
        
        self.play(FadeIn(rules_group))
        self.wait(4)
        
        self.play(
            FadeOut(rules_group),
            FadeOut(title),
            # 玩家缩小并移动到角落，为矩阵让路
            alice.animate.scale(0.01).move_to(LEFT*10), # 移出屏幕暂存或消失
            bob.animate.scale(0.01).move_to(RIGHT*10)
        )

    def create_player(self, name, color, pos):
        icon = VGroup(
            Circle(radius=0.6, color=color, fill_opacity=0.5),
            Text(name[0], font_size=40, color=WHITE)
        )
        label = Text(name, font_size=24, color=color).next_to(icon, DOWN, buff=0.2)
        return VGroup(icon, label).move_to(pos)

    def build_payoff_matrix(self):
        # 缩小矩阵尺寸，防止占满屏幕
        side_len = 4.0 
        matrix_bg = Square(side_length=side_len, color=WHITE)
        
        # 分隔线
        h_line = Line(LEFT * side_len/2, RIGHT * side_len/2)
        v_line = Line(UP * side_len/2, DOWN * side_len/2)
        
        # 标签 - 增加 buff 防止贴得太紧
        strat_a_label = Text("Alice", font_size=24, color=GT_BLUE).next_to(matrix_bg, LEFT, buff=0.6).rotate(PI/2)
        strat_b_label = Text("Bob", font_size=24, color=GT_RED).next_to(matrix_bg, UP, buff=0.4)
        
        # 策略名称
        offset = side_len / 4
        a_coop = Text("合作", font_size=18, color=GT_BLUE).move_to(LEFT*(side_len/2 + 0.4) + UP*offset)
        a_defect = Text("背叛", font_size=18, color=GT_BLUE).move_to(LEFT*(side_len/2 + 0.4) + DOWN*offset)
        
        b_coop = Text("合作", font_size=18, color=GT_RED).move_to(UP*(side_len/2 + 0.4) + LEFT*offset)
        b_defect = Text("背叛", font_size=18, color=GT_RED).move_to(UP*(side_len/2 + 0.4) + RIGHT*offset)
        
        # 单元格内容
        cells_group = VGroup()
        matrix_refs = [] # 存储单元格引用，用于后续动画
        
        # (Alice payoff, Bob payoff, BG Color)
        # 0:左上, 1:右上, 2:左下, 3:右下
        data = [
            ("-1", "-1", GT_GREEN), 
            ("-10", "0", GT_GRAY),
            ("0", "-10", GT_GRAY), 
            ("-5", "-5", GT_YELLOW)
        ]
        
        # 计算四个中心点坐标
        centers = [
            [-offset, offset, 0], [offset, offset, 0],
            [-offset, -offset, 0], [offset, -offset, 0]
        ]
        
        for i, (pa, pb, col) in enumerate(data):
            # 背景块
            bg = Square(side_length=side_len/2 - 0.05, fill_color=col, fill_opacity=0.2, stroke_width=0)
            bg.move_to(centers[i])
            
            # 分数
            nums = VGroup(
                Text(pa, font_size=32, color=GT_BLUE),
                Text(",", font_size=32),
                Text(pb, font_size=32, color=GT_RED)
            ).arrange(RIGHT, buff=0.1).move_to(centers[i])
            
            # 将背景和数字打包
            cell = VGroup(bg, nums)
            cells_group.add(cell)
            matrix_refs.append(cell)

        full_matrix = VGroup(
            matrix_bg, h_line, v_line,
            strat_a_label, strat_b_label,
            a_coop, a_defect, b_coop, b_defect,
            cells_group
        )
        
        self.play(Create(matrix_bg), Create(h_line), Create(v_line))
        self.play(Write(strat_a_label), Write(strat_b_label))
        self.play(FadeIn(a_coop), FadeIn(a_defect), FadeIn(b_coop), FadeIn(b_defect))
        self.play(FadeIn(cells_group))
        
        return full_matrix, matrix_refs

    def analyze_strategies(self, matrix_group, cells):
        """逻辑推演：修复布局重叠问题"""
        
        # 1. 矩阵移至左侧，留出右侧空间
        self.play(matrix_group.animate.scale(0.85).to_edge(LEFT, buff=1.0))
        
        # 右侧区域参考点
        RIGHT_ZONE = RIGHT * 3.5
        
        # 标题
        think_title = Text("Alice的思考：", font_size=26, color=GT_BLUE, weight=BOLD)
        think_title.move_to(RIGHT_ZONE + UP * 2.5)
        self.play(Write(think_title))
        
        # --- 情况 1：Bob 合作 ---
        case1_label = Text("假设 Bob 合作...", font_size=22, color=GT_GRAY)
        case1_label.next_to(think_title, DOWN, buff=0.5)
        self.play(Write(case1_label))
        
        # 高亮左列
        hl_rect = SurroundingRectangle(VGroup(cells[0], cells[2]), color=GT_RED, buff=0.1)
        self.play(Create(hl_rect))
        
        # 比较文字
        comp1 = VGroup(
            Text("我合作: -1年", font_size=20, color=WHITE),
            Text("我背叛: 0年 (赢)", font_size=20, color=GT_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(case1_label, DOWN, buff=0.3)
        self.play(Write(comp1))
        
        # 箭头1 (修正 shift 报错)
        arrow1 = Arrow(
            start=cells[0].get_center(), 
            end=cells[2].get_center(), 
            color=GT_BLUE, 
            buff=0.4,
            max_tip_length_to_length_ratio=0.2
        ).set_z_index(10) # 确保箭头在最上层
        self.play(GrowArrow(arrow1))
        self.wait(1)
        
        # --- 清理 情况1 的文字，为 情况2 腾空间 ---
        self.play(
            FadeOut(case1_label), 
            FadeOut(comp1), 
            FadeOut(hl_rect)
        )
        
        # --- 情况 2：Bob 背叛 ---
        case2_label = Text("假设 Bob 背叛...", font_size=22, color=GT_GRAY)
        case2_label.next_to(think_title, DOWN, buff=0.5) # 位置同上
        self.play(Write(case2_label))
        
        # 高亮右列
        hl_rect2 = SurroundingRectangle(VGroup(cells[1], cells[3]), color=GT_RED, buff=0.1)
        self.play(Create(hl_rect2))
        
        comp2 = VGroup(
            Text("我合作: -10年", font_size=20, color=WHITE),
            Text("我背叛: -5年 (赢)", font_size=20, color=GT_YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(case2_label, DOWN, buff=0.3)
        self.play(Write(comp2))
        
        # 箭头2
        arrow2 = Arrow(
            start=cells[1].get_center(), 
            end=cells[3].get_center(), 
            color=GT_BLUE, 
            buff=0.4,
            max_tip_length_to_length_ratio=0.2
        ).set_z_index(10)
        self.play(GrowArrow(arrow2))
        self.wait(1)
        
        # --- 清理 情况2 ---
        self.play(
            FadeOut(case2_label), 
            FadeOut(comp2), 
            FadeOut(hl_rect2)
        )
        
        # --- 结论 ---
        concl = Text("无论 Bob 选什么\n我都必须背叛！", font_size=24, color=GT_BLUE, line_spacing=1.2)
        concl.next_to(think_title, DOWN, buff=0.5)
        self.play(Write(concl))
        
        bob_too = Text("Bob 也是这么想的...", font_size=20, color=GT_RED)
        bob_too.next_to(concl, DOWN, buff=0.5)
        self.play(Write(bob_too))
        
        # Bob的箭头 (横向)
        # Shift 移到括号外，修正报错
        arrow3 = Arrow(
            start=cells[0].get_center(), 
            end=cells[1].get_center(), 
            color=GT_RED, 
            buff=0.4
        ).shift(UP*0.3)
        
        arrow4 = Arrow(
            start=cells[2].get_center(), 
            end=cells[3].get_center(), 
            color=GT_RED, 
            buff=0.4
        ).shift(UP*0.3)
        
        self.play(GrowArrow(arrow3), GrowArrow(arrow4))
        self.wait(2)
        
        # 清理右侧所有文字
        self.play(FadeOut(think_title), FadeOut(concl), FadeOut(bob_too))

    def define_nash_equilibrium(self, cells):
            # --- 1. 纳什均衡 (右下角) ---
            # 先定义纳什均衡，确立右侧文字的基准位置
            nash_rect = SurroundingRectangle(cells[3], color=GT_YELLOW, stroke_width=5)
            nash_label = Text("纳什均衡", font_size=28, color=GT_YELLOW, weight=BOLD)
            
            # 将文字放在矩阵右侧，留出足够的缓冲距离
            nash_label.next_to(nash_rect, RIGHT, buff=1.0) 
            
            nash_desc = Text("无论谁单方面改变策略\n结果都会变差", font_size=20, color=GT_GRAY, line_spacing=1.2)
            nash_desc.next_to(nash_label, DOWN, aligned_edge=LEFT)
            
            self.play(Create(nash_rect))
            self.play(Write(nash_label), Write(nash_desc))
            self.wait(2)
            
            # --- 2. 帕累托最优 (左上角) ---
            pareto_rect = SurroundingRectangle(cells[0], color=GT_GREEN, stroke_width=5)
            pareto_label = Text("帕累托最优", font_size=28, color=GT_GREEN, weight=BOLD)
            
            # --- 布局修复核心 ---
            # 不再根据 cells[0] 定位，而是强制与下方的纳什均衡文字“左对齐”
            # 并在垂直方向上，与矩阵的第一行(cells[0])对齐
            pareto_label.move_to([nash_label.get_x(), cells[0].get_y(), 0])
            # 微调：确保左边缘严格对齐
            pareto_label.align_to(nash_label, LEFT)
            
            pareto_desc = Text("集体利益最大化\n但不够稳定", font_size=20, color=WHITE, line_spacing=1.2)
            pareto_desc.next_to(pareto_label, DOWN, aligned_edge=LEFT)
            
            self.play(Create(pareto_rect))
            self.play(Write(pareto_label), Write(pareto_desc))
            
            self.wait(3)
            self.clear() # 清空屏幕进入下一环节

    def real_world_application(self):
        title = Text("现实映射：核军备竞赛", font_size=32, color=GT_PURPLE).to_edge(UP)
        self.play(Write(title))
        
        # 布局：左A，右B，中间结果
        country_a = self.create_player("A国", GT_BLUE, LEFT * 4)
        country_b = self.create_player("B国", GT_RED, RIGHT * 4)
        
        self.play(FadeIn(country_a), FadeIn(country_b))
        
        # 推演文本
        logic = VGroup(
            Text("如果对方裁军 -> 我扩军就能称霸", font_size=20),
            Text("如果对方扩军 -> 我必须扩军自保", font_size=20)
        ).arrange(DOWN, buff=0.2)
        logic.to_edge(DOWN, buff=1.5)
        
        self.play(Write(logic))
        
        # 结果动画
        bomb = Text("💣", font_size=60).move_to(ORIGIN)
        result = Text("陷入无休止的军备竞赛", font_size=24, color=GT_YELLOW).next_to(bomb, DOWN)
        
        self.play(FadeIn(bomb, scale=0.5), Write(result))
        self.wait(2)
        
        self.play(FadeOut(title), FadeOut(country_a), FadeOut(country_b), FadeOut(logic), FadeOut(bomb), FadeOut(result))

    def show_ending(self):
        summary = VGroup(
            Text("1. 个人理性可能导致集体崩溃", font_size=26),
            Text("2. 纳什均衡是一个\"死结\"", font_size=26),
            Text("3. 唯有信任能打破囚笼", font_size=26, color=GT_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
        
        # 预告
        next_ep = Text("下期预告：智猪博弈", font_size=40, color=GT_YELLOW)
        desc = Text("弱者如何在强者的游戏中生存？", font_size=24, color=GT_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)