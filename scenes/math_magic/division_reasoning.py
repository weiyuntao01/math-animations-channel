"""
竖式除法填空题的数学思维讲解
Mathematical Thinking in Division Fill-in Problems
"""

from manim import *
import numpy as np

# 颜色主题
THEME_PURPLE = "#8B5CF6"    # 主色：紫色
THEME_GREEN = "#10B981"     # 成功绿
THEME_RED = "#EF4444"       # 错误红
THEME_BLUE = "#3B82F6"      # 数据蓝
THEME_YELLOW = "#F59E0B"    # 提示黄
THEME_GRAY = "#6B7280"      # 中性灰
THEME_DARK = "#111827"      # 深色面板

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


# ========== 公用排版组件（只优化文字排版，不动图片与思维总结） ==========
def make_panel(title_text: str, body_vgroup: Mobject, width=6.2, pad=0.4):
    """
    右侧信息面板：标题条 + 分割线 + 正文区（传入VGroup）
    """
    header = Text(title_text, font_size=SUBTITLE_SIZE, color=THEME_YELLOW, weight=BOLD)
    divider = Line(LEFT * (width * 0.45), RIGHT * (width * 0.45), color=THEME_GRAY, stroke_width=2)

    body_vgroup.arrange(DOWN, aligned_edge=LEFT, buff=0.24)
    body_vgroup.next_to(divider, DOWN, buff=0.36).align_to(divider, LEFT)

    # 面板背景
    body_bbox = SurroundingRectangle(
        VGroup(header, divider, body_vgroup),
        color=THEME_GRAY,
        corner_radius=0.2,
        buff=pad
    )
    body_bbox.set_fill(color=THEME_DARK, opacity=0.25)
    panel = VGroup(body_bbox, header, divider, body_vgroup)
    return panel


def bullet(text: str, size=NORMAL_SIZE, color=WHITE, bold=False):
    """
    统一的项目符号行（•），更紧凑的行距与对齐。
    """
    t = Text(f"• {text}", font_size=size, color=color, weight=BOLD if bold else NORMAL)
    return t


def subbullet(text: str, size=SMALL_SIZE, color="#E5E7EB"):
    """
    二级缩进子弹。
    """
    t = Text(f"  ↳ {text}", font_size=size, color=color)
    t.shift(RIGHT * 0.06)
    return t


def equation(tex: str, size=28, color=WHITE):
    """
    等式/表达式统一样式。
    """
    m = MathTex(tex, font_size=size)
    m.set_color(color)
    m.align_on_border(LEFT)
    return m


def boxed_step(title_text: str, lines: list, extra: list | None = None, width=6.2):
    """
    推理步骤盒：蓝色标题 + 内容要点（bullet）+ 公式/强调等（extra）
    """
    step_title = Text(title_text, font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD)
    content = VGroup(*[bullet(*x) if isinstance(x, tuple) else bullet(x) for x in lines])
    if extra:
        content.add(*extra)
    # 竖向排布并加细分割线
    content.arrange(DOWN, aligned_edge=LEFT, buff=0.18).next_to(step_title, DOWN, buff=0.22)

    divider = Line(LEFT * (width * 0.46), RIGHT * (width * 0.46), color=THEME_GRAY, stroke_width=1.5)
    divider.next_to(step_title, DOWN, buff=0.14).align_to(step_title, LEFT)

    group = VGroup(step_title, divider, content)
    box = SurroundingRectangle(group, color=THEME_GRAY, corner_radius=0.18, buff=0.26)
    box.set_fill(color=THEME_DARK, opacity=0.25)
    return VGroup(box, group)


class DivisionReasoningLesson(Scene):
    """竖式除法填空题的数学思维讲解"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 1. 开场
        self.show_intro()
        
        # 2. 第二题展示（左图右文）
        self.show_problem_2_with_image()
        
        # 3. 数学思维总结（保持不动）
        self.mathematical_thinking_summary()
        
        # 4. 结尾
        self.show_ending()
    
    def show_intro(self):
        """开场介绍"""
        title = Text(
            "竖式除法填空题",
            font_size=50,
            color=THEME_PURPLE,
            weight=BOLD
        )
        
        subtitle = Text(
            "逆向思维与推理的艺术",
            font_size=34,
            color=WHITE
        )
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    # ===================（仅优化此块的文字排版）===================
    def show_problem_2_with_image(self):
        """题目展示：左图右文，展示完整推理过程"""
        self.clear()
        
        # 标题
        title = Text("竖式除法填空题", font_size=TITLE_SIZE, color=THEME_PURPLE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：题目图片（不改动）
        try:
            problem_image = ImageMobject("images/第二题原题目（未做任何标记）.png")
            problem_image.scale_to_fit_height(4)
            problem_image.shift(LEFT * 3.5)
            self.play(FadeIn(problem_image))
        except Exception:
            image_placeholder = Rectangle(
                width=6, height=4,
                stroke_color=THEME_GREEN,
            stroke_width=3,
                fill_color=THEME_GREEN,
                fill_opacity=0.1
            )
            image_text = Text("题目图片", font_size=NORMAL_SIZE, color=THEME_GREEN)
            image_group = VGroup(image_placeholder, image_text)
            image_group.shift(LEFT * 3.5)
            self.play(Create(image_placeholder), Write(image_text))

        # 右侧：钩子描述（重新排版，防止重叠）
        hook_lines = [
            Text("小学四年级竖式除法填空题", font_size=SUBTITLE_SIZE, color=THEME_YELLOW, weight=BOLD),
            Text("面对这样的题目，应该如何思考？", font_size=NORMAL_SIZE, color=WHITE),
            Text("观察结构 → 分析条件 → 逆向推理", font_size=NORMAL_SIZE, color=THEME_BLUE),
            Text("准备好了吗？我们一起看推理过程！", font_size=NORMAL_SIZE, color=THEME_GREEN, weight=BOLD),
        ]
        hook_content = VGroup(*hook_lines)
        hook_content.arrange(DOWN, aligned_edge=LEFT, buff=0.6)

        anchor_target = problem_image if 'problem_image' in locals() else image_group
        hook_content.next_to(anchor_target, RIGHT, buff=1.4, aligned_edge=UP)
        hook_content.shift(UP * 0.2)

        self.play(LaggedStart(*[Write(line) for line in hook_lines], lag_ratio=0.25, run_time=2.5))
        self.wait(3.5)

        # 清除当前页面，展示推理过程
        self.play(
            FadeOut(title),
            FadeOut(problem_image if 'problem_image' in locals() else image_group),
            FadeOut(hook_content),
        )

        # 展示推理过程页面（右侧文本重新排版）
        self.show_detailed_reasoning_process()

    # ===================（仅优化此块的文字排版）===================
    def show_detailed_reasoning_process(self):
        """展示详细的推理过程（右侧步骤采用“盒状步骤”+ 公式行）"""
        # 标题
        title = Text("推理步骤", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 左侧：推理过程图片（不改动）
        try:
            reasoning_image = ImageMobject("images/题目二推理过程所用图片.png")
            reasoning_image.scale_to_fit_height(4)
            reasoning_image.shift(LEFT * 3.5)
            self.play(FadeIn(reasoning_image))
        except Exception:
            image_placeholder = Rectangle(
                width=5, height=4,
                stroke_color=THEME_GREEN,
            stroke_width=3,
                fill_color=THEME_GREEN,
                fill_opacity=0.1
            )
            image_text = Text("推理过程图片", font_size=NORMAL_SIZE, color=THEME_GREEN)
            image_group = VGroup(image_placeholder, image_text)
            image_group.shift(LEFT * 3.5)
            self.play(Create(image_group))

        # 定义显示区域（固定位置）
        display_area = Rectangle(
            width=6, height=4,
            stroke_color=THEME_GRAY,
            stroke_width=1,
            fill_color=THEME_GRAY,
            fill_opacity=0.05
        )
        display_area.shift(RIGHT * 3.5 + UP * 0.5)
        self.play(Create(display_area))

        # 左侧：垂直标题“推理过程”（保持与显示区域的间距）
        reasoning_title = VGroup(
            *[
                Text(char, font_size=SUBTITLE_SIZE, color=THEME_YELLOW, weight=BOLD)
                for char in "推理过程"
            ]
        )
        reasoning_title.arrange(DOWN, buff=0.5, aligned_edge=ORIGIN)
        reasoning_title.next_to(display_area, LEFT, buff=1.2)
        self.play(Write(reasoning_title))

        # 定义每个步骤的内容
        steps_data = [
            {
                "title": "1) 第一次试商必为 1",
                "content": [
                    "两位除数 ÷ 三位被除数'1□2'，先看'1□'",
                    "商只能取 1，否则太大",
                    "因此第一次的减数就是除数本身，形如 1e",
                ],
                "equations": []
            },
            {
                "title": "2) 由'第一次差'为 3 得到约束",
                "content": [
                    "设被除数中间位为 a，除数个位为 e",
                    "根据竖式：十位相消后得到差 3",
                ],
                "equations": [
                    "1a - 1e = a - e = 3",
                    "⇒ a = e + 3"
                ]
            },
            {
                "title": "3) 组第二次被减数",
                "content": [
                    "把差'3'与个位'2'落下，拼成新数",
                    "得到：32",
                ],
                "equations": [
                    "10 × 3 + 2 = 32"
                ]
            },
            {
                "title": "4) 由'32'试商确定除数",
                "content": [
                    "令第二次的商为 r，除数为 1e",
                    "使乘积刚好不超过 32 且尽量接近",
                ],
                "equations": [
                    "(10 + e) × r = 32",
                    "r = 2 可行 ⇒ 10 + e = 16 ⇒ e = 6"
                ]
            },
            {
                "title": "5) 回代并给出唯一解",
                "content": [
                    "由 e = 6 得 a = 9",
                    "结论：192 ÷ 16 = 12（余 0）",
                ],
                "equations": [
                    "a = e + 3 = 9",
                    "被除数 = 1a2 = 192",
                    "除数 = 16，商 = 12，余数 = 0"
                ]
            }
        ]

        # 逐步显示每个步骤（在同一个位置）
        current_step = None
        for i, step_data in enumerate(steps_data):
            # 创建当前步骤
            step_group = VGroup()
            
            # 标题
            title_text = Text(step_data["title"], font_size=NORMAL_SIZE, color=THEME_BLUE, weight=BOLD)
            step_group.add(title_text)
            
            # 内容
            for content_line in step_data["content"]:
                content_text = Text(content_line, font_size=SMALL_SIZE, color=WHITE)
                step_group.add(content_text)
            
            # 公式
            for equation_line in step_data["equations"]:
                equation_text = Text(equation_line, font_size=SMALL_SIZE, color=THEME_GREEN, weight=BOLD)
                step_group.add(equation_text)
            
            # 设置位置（都在同一个位置）
            step_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            step_group.move_to(display_area.get_center())
            
            # 显示当前步骤
            if current_step is not None:
                # 淡出上一步
                self.play(FadeOut(current_step), run_time=0.8)
                self.wait(0.5)
            
            # 显示当前步骤
            self.play(Write(step_group), run_time=2)
            current_step = step_group
            
            # 等待更长时间让观众理解
            self.wait(6)
        
        # 最后一步额外等待
        self.wait(3)

        # 淡出所有内容
        all_elements = VGroup(title, reasoning_title, display_area, current_step)
        if 'reasoning_image' in locals():
            self.play(FadeOut(all_elements), FadeOut(reasoning_image))
        else:
            self.play(FadeOut(all_elements), FadeOut(image_group))

    # ===================（以下保持不动）===================
    def mathematical_thinking_summary(self):
        """数学思维总结"""
        self.clear()
        
        # 总标题
        main_title = Text(
            "数学思维精髓",
            font_size=50,
            color=THEME_PURPLE,
            weight=BOLD
        )
        main_title.to_edge(UP)
        self.play(Write(main_title))
        self.wait(1)
        
        # 依次展示六种思维
        self.show_thinking_1()  # 逆向思维
        self.show_thinking_2()  # 等式思想
        self.show_thinking_3()  # 位值思维
        self.show_thinking_4()  # 推理验证
        self.show_thinking_5()  # 规律迁移
        self.show_thinking_6()  # 严谨耐心
        
        # 总结
        self.final_summary()
    
    def show_thinking_1(self):
        """展示逆向思维"""
        self.clear()
        
        title = Text("1. 逆向思维", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 图示：正向vs逆向
        forward_arrow = Arrow(LEFT * 3, RIGHT * 3, color=THEME_GRAY)
        forward_text = Text("正向：条件 → 结果", font_size=NORMAL_SIZE)
        forward_text.next_to(forward_arrow, UP, buff=0.3)
        
        reverse_arrow = Arrow(RIGHT * 3, LEFT * 3, color=THEME_GREEN, stroke_width=6)
        reverse_text = Text("逆向：结果 → 条件", font_size=NORMAL_SIZE, color=THEME_GREEN)
        reverse_text.next_to(reverse_arrow, DOWN, buff=0.3)
        
        arrows = VGroup(forward_arrow, forward_text, reverse_arrow, reverse_text)
        arrows.shift(UP * 0.5)
        
        self.play(Create(forward_arrow), Write(forward_text))
        self.play(Create(reverse_arrow), Write(reverse_text))
        
        # 具体例子
        example = VGroup(
            Text("例：第二次减到32，取商2最稳妥", font_size=NORMAL_SIZE),
            Text("→ 由32÷2=16、16×12=192，反推出结论", font_size=NORMAL_SIZE, color=THEME_YELLOW)
        ).arrange(DOWN, buff=0.3)
        example.shift(DOWN * 2)
        
        self.play(Write(example))
        
        # 核心理念
        core = Text(
            "不是单纯'算'，而是'反推'",
            font_size=SUBTITLE_SIZE,
            color=THEME_GREEN,
            weight=BOLD
        )
        core.shift(DOWN * 3.5)
        self.play(Write(core))
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, arrows, example, core)))
    
    def show_thinking_2(self):
        """展示等式思想"""
        self.clear()
        
        title = Text("2. 等式思想", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 核心公式
        formula = MathTex(
            r"\text{Dividend} = \text{Divisor} \times \text{Quotient} + \text{Remainder}",
            font_size=40
        )
        formula.shift(UP * 0.5)
        self.play(Write(formula))
        
        # 强调整体性
        emphasis = Text(
            "把竖式看作完整的等式关系",
            font_size=NORMAL_SIZE,
            color=THEME_YELLOW
        )
        emphasis.shift(DOWN * 0.5)
        self.play(Write(emphasis))
        
        # 图形化展示
        equation_parts = VGroup(
            Rectangle(width=2, height=1, fill_color=THEME_BLUE, fill_opacity=0.3),
            Text("=", font_size=40),
            Rectangle(width=1.5, height=1, fill_color=THEME_GREEN, fill_opacity=0.3),
            Text("×", font_size=30),
            Rectangle(width=1.5, height=1, fill_color=THEME_YELLOW, fill_opacity=0.3),
            Text("+", font_size=30),
            Rectangle(width=1, height=1, fill_color=THEME_RED, fill_opacity=0.3)
        ).arrange(RIGHT, buff=0.2)
        equation_parts.shift(DOWN * 2)
        
        labels = VGroup(
            Text("被除数", font_size=SMALL_SIZE),
            Text("除数", font_size=SMALL_SIZE),
            Text("商", font_size=SMALL_SIZE),
            Text("余数", font_size=SMALL_SIZE)
        )
        labels[0].next_to(equation_parts[0], DOWN, buff=0.2)
        labels[1].next_to(equation_parts[2], DOWN, buff=0.2)
        labels[2].next_to(equation_parts[4], DOWN, buff=0.2)
        labels[3].next_to(equation_parts[6], DOWN, buff=0.2)
        
        self.play(Create(equation_parts))
        self.play(Write(labels))
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, formula, emphasis, equation_parts, labels)))
    
    def show_thinking_3(self):
        """展示位值思维"""
        self.clear()
        
        title = Text("3. 位值与数位思维", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 数位对齐示意
        alignment_demo = VGroup()
        
        # 创建数位格子
        hundreds = VGroup(
            Text("百位", font_size=SMALL_SIZE, color=THEME_YELLOW),
            Square(side_length=0.8, stroke_color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        tens = VGroup(
            Text("十位", font_size=SMALL_SIZE, color=THEME_YELLOW),
            Square(side_length=0.8, stroke_color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        ones = VGroup(
            Text("个位", font_size=SMALL_SIZE, color=THEME_YELLOW),
            Square(side_length=0.8, stroke_color=WHITE)
        ).arrange(DOWN, buff=0.2)
        
        place_values = VGroup(hundreds, tens, ones).arrange(RIGHT, buff=0.3)
        place_values.shift(UP * 0.5)
        
        self.play(Create(place_values))
        
        # 强调对齐的重要性
        emphasis_text = VGroup(
            Text("十位对十位", font_size=NORMAL_SIZE),
            Text("个位对个位", font_size=NORMAL_SIZE),
            Text("运算必须按位进行", font_size=NORMAL_SIZE, color=THEME_GREEN)
        ).arrange(DOWN, buff=0.3)
        emphasis_text.shift(DOWN * 1.5)
        
        for text in emphasis_text:
            self.play(Write(text), run_time=0.6)
        
        # 错误示例
        wrong_example = Text(
            "❌ 数位不对齐 = 计算错误",
            font_size=NORMAL_SIZE,
            color=THEME_RED
        )
        wrong_example.shift(DOWN * 3)
        self.play(Write(wrong_example))
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, place_values, emphasis_text, wrong_example)))
    
    def show_thinking_4(self):
        """展示推理验证思维"""
        self.clear()
        
        title = Text("4. 推理与验证思维", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 思维链条
        chain = VGroup()
        
        # 假设
        hypothesis = VGroup(
            Circle(radius=0.5, fill_color=THEME_BLUE, fill_opacity=0.7),
            Text("假设", font_size=SMALL_SIZE, color=WHITE)
        )
        hypothesis.shift(LEFT * 4)
        
        # 推理
        reasoning = VGroup(
            Circle(radius=0.5, fill_color=THEME_YELLOW, fill_opacity=0.7),
            Text("推理", font_size=SMALL_SIZE, color=WHITE)
        )
        
        # 验证
        verification = VGroup(
            Circle(radius=0.5, fill_color=THEME_GREEN, fill_opacity=0.7),
            Text("验证", font_size=SMALL_SIZE, color=WHITE)
        )
        verification.shift(RIGHT * 4)
        
        # 箭头
        arrow1 = Arrow(hypothesis.get_right(), reasoning.get_left(), buff=0.2)
        arrow2 = Arrow(reasoning.get_right(), verification.get_left(), buff=0.2)
        
        chain.add(hypothesis, arrow1, reasoning, arrow2, verification)
        chain.shift(UP * 0.5)
        
        self.play(Create(hypothesis))
        self.play(Create(arrow1))
        self.play(Create(reasoning))
        self.play(Create(arrow2))
        self.play(Create(verification))
        
        # 具体例子
        example = VGroup(
            Text("例：设除数为1e（十位为1、个位为e）", font_size=SMALL_SIZE),
            Text("→ 十位相差3，因此 a = e + 3", font_size=SMALL_SIZE),
            Text("→ 以32试商取 r=2，可解得 e=6 ✓", font_size=SMALL_SIZE, color=THEME_GREEN)
        ).arrange(DOWN, buff=0.3)
        example.shift(DOWN * 1.5)
        
        for line in example:
            self.play(Write(line), run_time=0.6)
        
        # 核心理念
        core = Text(
            "完整的思维链：假设→推理→验证",
            font_size=NORMAL_SIZE,
            color=THEME_GREEN,
            weight=BOLD
        )
        core.shift(DOWN * 3)
        self.play(Write(core))
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, chain, example, core)))
    
    def show_thinking_5(self):
        """展示规律迁移"""
        self.clear()
        
        title = Text("5. 运算规律迁移", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 知识迁移示意图
        multiplication = VGroup(
            Rectangle(width=3, height=1.5, fill_color=THEME_BLUE, fill_opacity=0.3),
            Text("乘法规律", font_size=NORMAL_SIZE)
        )
        multiplication.shift(LEFT * 3 + UP * 0.5)
        
        division = VGroup(
            Rectangle(width=3, height=1.5, fill_color=THEME_GREEN, fill_opacity=0.3),
            Text("除法问题", font_size=NORMAL_SIZE)
        )
        division.shift(RIGHT * 3 + UP * 0.5)
        
        # 迁移箭头
        transfer_arrow = CurvedArrow(
            multiplication.get_right(),
            division.get_left(),
            color=THEME_YELLOW,
            stroke_width=4
        )
        transfer_text = Text("知识迁移", font_size=SMALL_SIZE, color=THEME_YELLOW)
        transfer_text.move_to(transfer_arrow.get_center() + UP * 0.5)
        
        self.play(Create(multiplication))
        self.play(Create(division))
        self.play(Create(transfer_arrow), Write(transfer_text))
        
        # 具体例子
        example = VGroup(
            Text("例：用乘法估算试商", font_size=NORMAL_SIZE),
            Text("(10+e)×2≈32 ⇒ e=6（个位取6）", font_size=SMALL_SIZE),
            Text("⇒ 除数=16，商=12（余数0）", font_size=NORMAL_SIZE, color=THEME_GREEN)
        ).arrange(DOWN, buff=0.3)
        example.shift(DOWN * 2)
        
        for line in example:
            self.play(Write(line), run_time=0.6)
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, multiplication, division, transfer_arrow, transfer_text, example)))
    
    def show_thinking_6(self):
        """展示严谨性与耐心"""
        self.clear()
        
        title = Text("6. 严谨性与耐心", font_size=TITLE_SIZE, color=THEME_PURPLE, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # 创建检查清单
        checklist = VGroup(
            Text("✓ 数位对齐", font_size=NORMAL_SIZE),
            Text("✓ 逐步演算", font_size=NORMAL_SIZE),
            Text("✓ 验证答案", font_size=NORMAL_SIZE),
            Text("✓ 检查余数", font_size=NORMAL_SIZE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        checklist.shift(LEFT * 2)
        
        for item in checklist:
            self.play(Write(item), run_time=0.5)
        
        # 强调条理性
        emphasis = VGroup(
            Text("按顺序推理", font_size=NORMAL_SIZE, color=THEME_YELLOW),
            Text("不跳步骤", font_size=NORMAL_SIZE, color=THEME_YELLOW),
            Text("培养条理性", font_size=NORMAL_SIZE, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        emphasis.shift(RIGHT * 2)
        
        for text in emphasis:
            self.play(Write(text), run_time=0.6)
        
        # 核心理念
        core = Text(
            "数学需要严谨，更需要耐心",
            font_size=SUBTITLE_SIZE,
            color=THEME_GREEN,
            weight=BOLD
        )
        core.shift(DOWN * 2.5)
        self.play(Write(core))
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, checklist, emphasis, core)))
    
    def final_summary(self):
        """最终总结"""
        self.clear()
        
        title = Text(
            "竖式除法的深层价值",
            font_size=TITLE_SIZE,
            color=THEME_PURPLE,
            weight=BOLD
        )
        title.to_edge(UP)
        self.play(Write(title))
        
        # 六大思维能力
        abilities = VGroup(
            Text("1. 逆向思维", font_size=NORMAL_SIZE),
            Text("2. 等式思想", font_size=NORMAL_SIZE),
            Text("3. 数位思维", font_size=NORMAL_SIZE),
            Text("4. 推理验证", font_size=NORMAL_SIZE),
            Text("5. 规律迁移", font_size=NORMAL_SIZE),
            Text("6. 条理严谨", font_size=NORMAL_SIZE)
        ).arrange_in_grid(2, 3, buff=(1, 0.5))
        abilities.shift(UP * 0.5)
        
        # 用方框包围
        boxes = VGroup()
        for ability in abilities:
            box = SurroundingRectangle(
                ability,
                color=THEME_GREEN,
                corner_radius=0.1,
                buff=0.2
            )
            boxes.add(box)
        
        self.play(
            AnimationGroup(
                *[Write(ability) for ability in abilities],
                lag_ratio=0.2
            )
        )
        self.play(
            AnimationGroup(
                *[Create(box) for box in boxes],
                lag_ratio=0.1
            )
        )
        
        # 核心总结
        conclusion = VGroup(
            Text("不仅是算一道题", font_size=NORMAL_SIZE),
            Text("而是培养解决复杂问题的能力", font_size=SUBTITLE_SIZE, color=THEME_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        conclusion.shift(DOWN * 2.5)
        
        self.play(Write(conclusion[0]))
        self.play(Write(conclusion[1]), conclusion[1].animate.scale(1.1))
        
        self.wait(3)
        self.play(FadeOut(VGroup(title, abilities, boxes, conclusion)))
    
    def show_ending(self):
        """结尾"""
        self.clear()
        
        # 主要信息
        main_message = Text(
            "数学思维，从练习中培养",
            font_size=45,
            color=THEME_PURPLE,
            weight=BOLD
        )
        
        # 副信息
        sub_message = Text(
            "每一道题都是思维的体操",
            font_size=30,
            color=WHITE
        )
        sub_message.next_to(main_message, DOWN, buff=0.8)
        
        self.play(Write(main_message), run_time=2)
        self.play(Write(sub_message), run_time=1.5)
        self.wait(3)
        
        # 淡出
        self.play(FadeOut(main_message), FadeOut(sub_message))
        
        # 感谢观看
        thanks = Text(
            "感谢观看",
            font_size=40,
            color=WHITE
        )
        self.play(Write(thanks))
        self.wait(2)
        self.play(FadeOut(thanks))


# 用于测试的场景
class TestDivisionReasoning(Scene):
    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        
        # 测试第二题（只运行包含排版优化的部分）
        lesson = DivisionReasoningLesson()
        lesson.show_problem_2_with_image()
