
"""
INF_EP05: 罗素悖论 (Russell's Paradox)
理发师该不该给自己刮胡子？数学大厦的基石崩塌。
"""

from manim import *
import numpy as np

# --- 颜色定义 ---
INF_PURPLE = "#7C3AED"   # 神秘紫
INF_GOLD = "#FBBF24"     # 无穷金/逻辑
INF_BLUE = "#3B82F6"     # 集合A (给自己刮)
INF_RED = "#EF4444"      # 集合B (不给自己刮)
INF_GREEN = "#10B981"    # 规则
INF_GRAY = "#6B7280"     # 背景/中性
BG_COLOR = "#0F172A"     # 深蓝灰背景

class InfinityEP05(Scene):
    """无穷系列 EP05：罗素悖论"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：危机的到来
        self.intro_crisis()
        
        # 2. 直观案例：理发师悖论 (Barber Paradox)
        # 全屏清场式衔接
        self.barber_scenario()
        
        # 3. 数学形式：集合论的崩溃
        self.set_theory_logic()
        
        # 4. 解决方案与系列大结局
        self.show_series_finale()

    def intro_crisis(self):
        """开场：数学危机"""
        old_series = Text("EP04: 分形几何 (分数维度)", font_size=32, color=INF_GRAY).to_edge(UP)
        new_series = Text("EP05: 罗素悖论", font_size=54, color=INF_RED, weight=BOLD)
        subtitle = Text("The Third Crisis of Mathematics (第三次数学危机)", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        # 引用
        quote = Text("\"数学大厦的地基动摇了\"", font_size=32, color=INF_GOLD, slant=ITALIC).next_to(subtitle, DOWN, buff=1.0)
        self.play(Write(quote))
        self.wait(2)
        
        # 彻底清场，为下一幕留出干净画布
        self.play(FadeOut(Group(*self.mobjects)))

    def barber_scenario(self):
        """场景：理发师悖论"""
        
        # 布局定义
        LEFT_CENTER = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 1. 标题
        title = Text("理发师悖论 (1901)", font_size=36, color=INF_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 2. 视觉区域 (左侧)：两个集合
        # 集合A：给自己刮胡子的人
        circle_self = Circle(radius=1.5, color=INF_BLUE, fill_opacity=0.1).move_to(LEFT_CENTER + UP * 1.5)
        label_self = Text("给自己刮脸", font_size=20, color=INF_BLUE).next_to(circle_self, UP)
        
        # 集合B：不给自己刮胡子的人
        circle_nonself = Circle(radius=1.5, color=INF_RED, fill_opacity=0.1).move_to(LEFT_CENTER + DOWN * 1.5)
        label_nonself = Text("不给自己刮脸", font_size=20, color=INF_RED).next_to(circle_nonself, DOWN)
        
        self.play(Create(circle_self), Write(label_self))
        self.play(Create(circle_nonself), Write(label_nonself))
        
        # 3. 规则 (右侧上部)
        rule_title = Text("萨维尔村的规则：", font_size=26, color=INF_GOLD, weight=BOLD)
        rule_title.move_to(RIGHT_ZONE + UP * 2.0) # 绝对定位防重叠
        
        rule_body = Text(
            "理发师只给且必须给\n所有\"不给自己刮脸的人\"\n刮脸。",
            font_size=22, color=WHITE, line_spacing=1.5
        )
        rule_body.next_to(rule_title, DOWN, buff=0.4)
        
        self.play(Write(rule_title), Write(rule_body))
        
        # 4. 主角登场：理发师
        barber = self.create_barber_icon().move_to(LEFT_CENTER) # 初始在中间
        barber_label = Text("理发师", font_size=20, color=INF_GOLD).next_to(barber, RIGHT)
        
        self.play(FadeIn(barber), Write(barber_label))
        
        # 5. 逻辑推演 (右侧下部)
        question = Text("问题：理发师给自己刮脸吗？", font_size=24, color=INF_PURPLE).next_to(rule_body, DOWN, buff=0.8)
        self.play(Write(question))
        
        # --- 情况 A ---
        # 假设他给自己刮 -> 属于蓝色圈 -> 规则说他不给这类人刮 -> 矛盾
        case_a_text = Text("假设：他给自己刮", font_size=20, color=INF_BLUE)
        case_a_text.next_to(question, DOWN, buff=0.4).align_to(question, LEFT)
        
        self.play(Write(case_a_text))
        
        # 动画：理发师移入蓝圈
        self.play(barber.animate.move_to(circle_self.get_center()), run_time=1)
        
        # 错误提示
        error_a = Text("违反规则！", font_size=20, color=INF_RED).next_to(barber, RIGHT)
        self.play(Write(error_a))
        self.play(Indicate(rule_body)) # 闪烁规则
        
        result_a = Text("-> 他不能给自己刮", font_size=20, color=INF_RED).next_to(case_a_text, DOWN, buff=0.1).align_to(case_a_text, LEFT)
        self.play(Write(result_a))
        
        self.wait(1)
        self.play(FadeOut(error_a)) # 清理局部文字
        
        # --- 情况 B ---
        # 假设他不给自己刮 -> 属于红色圈 -> 规则说他必须给这类人刮 -> 矛盾
        case_b_text = Text("假设：他不给自己刮", font_size=20, color=INF_RED)
        # 布局：放在 result_a 下方
        case_b_text.next_to(result_a, DOWN, buff=0.4).align_to(question, LEFT)
        
        self.play(Write(case_b_text))
        
        # 动画：理发师移入红圈
        self.play(barber.animate.move_to(circle_nonself.get_center()), run_time=1)
        
        # 错误提示
        error_b = Text("必须给自己刮！", font_size=20, color=INF_BLUE).next_to(barber, RIGHT)
        self.play(Write(error_b))
        
        result_b = Text("-> 他必须给自己刮", font_size=20, color=INF_BLUE).next_to(case_b_text, DOWN, buff=0.1).align_to(case_b_text, LEFT)
        self.play(Write(result_b))
        
        self.wait(1)
        
        # 6. 死循环动画
        # 理发师在两个圈之间快速移动
        self.play(FadeOut(error_b))
        
        loop_path = [circle_self.get_center(), circle_nonself.get_center(), circle_self.get_center()]
        for _ in range(2):
            self.play(
                barber.animate.move_to(loop_path[1]),
                run_time=0.3
            )
            self.play(
                barber.animate.move_to(loop_path[0]),
                run_time=0.3
            )
            
        paradox_label = Text("逻辑死循环", font_size=32, color=INF_RED, weight=BOLD).move_to(LEFT_CENTER)
        self.play(Write(paradox_label))
        
        self.wait(3)
        # 全屏清场
        self.play(FadeOut(Group(*self.mobjects)))

    def create_barber_icon(self):
            """创建理发师图标 (修复参数报错)"""
            face = Circle(radius=0.3, color=INF_GOLD, fill_opacity=1)
            
            # 修复：将 outer_radius 改为 radius
            beard = Sector(
                radius=0.32, 
                angle=PI, 
                start_angle=PI, 
                color=BLACK, 
                fill_opacity=0.8,
                stroke_width=0
            ).shift(DOWN*0.05)
            
            # 剪刀 (简化)
            scissor = Cross(stroke_width=4, scale_factor=0.2).set_color(WHITE).move_to(RIGHT*0.4)
            
            return VGroup(face, beard, scissor)

    def set_theory_logic(self):
        """数学形式：罗素悖论"""
        
        title = Text("数学形式：罗素悖论", font_size=36, color=INF_PURPLE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 1. 定义集合 R
        # 屏幕中心偏上
        def_text = MathTex(
            r"R = \{ x \mid x \notin x \}",
            font_size=48
        ).shift(UP * 1.5)
        
        def_desc = Text("R 是所有\"不包含自身的集合\"的集合", font_size=24, color=INF_GRAY).next_to(def_text, DOWN, buff=0.3)
        
        self.play(Write(def_text), Write(def_desc))
        
        # 2. 核心问题
        question = Text("R 包含它自己吗？", font_size=28, color=INF_GOLD).shift(UP * 0.2)
        question_math = MathTex(r"R \in R \text{ ?}", font_size=36, color=INF_GOLD).next_to(question, DOWN, buff=0.2)
        
        self.play(Write(question), Write(question_math))
        
        # 3. 分栏推导 (左右布局)
        
        # 左侧：如果 R 包含 R
        left_group = VGroup()
        if_in = MathTex(r"\text{If } R \in R", color=INF_BLUE)
        arrow_1 = Arrow(UP, DOWN, color=WHITE, buff=0.1)
        then_out = MathTex(r"\text{Then } R \notin R", color=INF_RED)
        desc_1 = Text("(根据定义)", font_size=18, color=GRAY)
        
        left_group.add(if_in, arrow_1, then_out, desc_1)
        left_group.arrange(DOWN, buff=0.3)
        left_group.move_to(LEFT * 3.0 + DOWN * 2.0)
        
        # 右侧：如果 R 不包含 R
        right_group = VGroup()
        if_out = MathTex(r"\text{If } R \notin R", color=INF_RED)
        arrow_2 = Arrow(UP, DOWN, color=WHITE, buff=0.1)
        then_in = MathTex(r"\text{Then } R \in R", color=INF_BLUE)
        desc_2 = Text("(符合入群条件)", font_size=18, color=GRAY)
        
        right_group.add(if_out, arrow_2, then_in, desc_2)
        right_group.arrange(DOWN, buff=0.3)
        right_group.move_to(RIGHT * 3.0 + DOWN * 2.0)
        
        # 4. 展示矛盾
        self.play(FadeIn(left_group))
        self.wait(1)
        self.play(FadeIn(right_group))
        self.wait(1)
        
        # 矛盾符号
        contradiction = MathTex(r"R \in R \iff R \notin R", color=INF_RED, font_size=40)
        contradiction.move_to(DOWN * 2.0)
        
        # 爆炸效果
        self.play(
            FadeOut(left_group), 
            FadeOut(right_group),
            Transform(question_math, contradiction)
        )
        
        fail_text = Text("逻辑崩溃", font_size=36, color=INF_RED, weight=BOLD).next_to(contradiction, DOWN)
        self.play(Write(fail_text))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_series_finale(self):
            """系列大结局 (分幕式修复版)"""
            
            # 1. 标题 (置顶)
            title = Text("无穷与悖论 (系列完)", font_size=48, color=INF_GOLD)
            title.to_edge(UP, buff=1.5) # 留出顶部空间
            
            # 2. 总结内容
            summary = VGroup(
                Text("从希尔伯特旅馆到罗素悖论", font_size=28),
                Text("我们在无穷的边缘试探", font_size=28),
                Text("数学不仅是计算，更是逻辑的艺术", font_size=28, color=INF_PURPLE)
            ).arrange(DOWN, buff=0.5)
            summary.next_to(title, DOWN, buff=1.0)
            
            self.play(Write(title))
            self.play(Write(summary))
            self.wait(3) # 多停留一会儿供阅读
            
            # --- 3. 转场：清理总结，为预告腾出C位 ---
            self.play(FadeOut(summary))
            
            # 4. 下一季预告 (线性代数)
            next_series = VGroup(
                Text("下一季预告：", font_size=28, color=INF_BLUE),
                Text("可视化的线性代数", font_size=56, color=WHITE, weight=BOLD), # 加大字号
                Text("矩阵 · 空间变换 · 降维打击", font_size=28, color=INF_GRAY)
            ).arrange(DOWN, buff=0.4)
            
            # 放在屏幕正中央，视觉冲击力更强
            next_series.move_to(ORIGIN)
            
            self.play(FadeIn(next_series, shift=UP))
            self.wait(3)
            
            # 最终全屏淡出
            self.play(FadeOut(Group(*self.mobjects)))