from manim import *
import numpy as np

class HumanProportionsEP5(Scene):
    """人体比例中的1.618 - 黄金分割系列 EP05"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：维特鲁威人的秘密
        self.show_vitruvian_man()
        
        # 第二部分：面部的黄金比例
        self.show_facial_proportions()
        
        # 第三部分：身体各部分的黄金比例
        self.show_body_proportions()
        
        # 第四部分：黄金比例与美学标准
        self.show_aesthetic_standards()
        
        # 第五部分：现代应用
        self.show_modern_applications()
        
        # 结尾
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第五集：人体比例中的1.618", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_vitruvian_man(self):
        """维特鲁威人的秘密 - 0:10-1:00"""
        title = Text("维特鲁威人的黄金密码", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建简化的维特鲁威人
        # 外圆和内方
        circle = Circle(radius=2.5, color=BLUE, stroke_width=2)
        square = Square(side_length=4, color=BLUE, stroke_width=2)
        
        # 人体轮廓（简化版）
        # 头部
        head = Circle(radius=0.3, color=WHITE, stroke_width=2)
        head.shift(UP * 1.7)
        
        # 躯干（简单矩形）
        torso = Rectangle(width=0.8, height=1.5, color=WHITE, stroke_width=2)
        torso.shift(UP * 0.5)
        
        # 手臂（展开）
        left_arm = Line(torso.get_left(), torso.get_left() + LEFT * 1.5 + UP * 0.3, 
                       color=WHITE, stroke_width=2)
        right_arm = Line(torso.get_right(), torso.get_right() + RIGHT * 1.5 + UP * 0.3, 
                        color=WHITE, stroke_width=2)
        
        # 腿部
        left_leg = Line(torso.get_bottom() + LEFT * 0.2, 
                       torso.get_bottom() + LEFT * 0.2 + DOWN * 1.7, 
                       color=WHITE, stroke_width=2)
        right_leg = Line(torso.get_bottom() + RIGHT * 0.2, 
                        torso.get_bottom() + RIGHT * 0.2 + DOWN * 1.7, 
                        color=WHITE, stroke_width=2)
        
        human = VGroup(head, torso, left_arm, right_arm, left_leg, right_leg)
        vitruvian = VGroup(circle, square, human)
        
        self.play(Create(square), Create(circle))
        self.play(Create(human))
        
        # 显示关键比例
        # 肚脐线（黄金分割点）
        navel_line = DashedLine(
            LEFT * 3, RIGHT * 3,
            color=GOLD, stroke_width=2
        )
        navel_line.shift(UP * 0.2)
        
        self.play(Create(navel_line))
        
        # 标注比例
        phi = (1 + np.sqrt(5)) / 2
        
        # 上半身和下半身的标注
        upper_brace = Brace(Line(navel_line.get_center(), head.get_top()), LEFT)
        lower_brace = Brace(Line(left_leg.get_bottom(), navel_line.get_center()), LEFT)
        
        upper_text = Text("1", font_size=24, color=YELLOW)
        lower_text = MathTex(r"\varphi", font_size=32, color=YELLOW)
        
        upper_text.next_to(upper_brace, LEFT)
        lower_text.next_to(lower_brace, LEFT)
        
        self.play(
            Create(upper_brace), Write(upper_text),
            Create(lower_brace), Write(lower_text)
        )
        
        # 说明文字
        explanation = Text(
            "肚脐是身高的黄金分割点",
            font_size=24, color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 展示其他比例
        # 手臂展开的宽度等于身高
        arm_span_line = DoubleArrow(
            left_arm.get_end(), right_arm.get_end(),
            color=GREEN, stroke_width=2
        )
        height_line = DoubleArrow(
            head.get_top(), left_leg.get_bottom(),
            color=GREEN, stroke_width=2
        )
        height_line.shift(RIGHT * 3)
        
        span_text = Text("臂展", font_size=20, color=GREEN)
        span_text.next_to(arm_span_line, UP*0.01)
        height_text = Text("身高", font_size=20, color=GREEN)
        height_text.next_to(height_line, RIGHT)
        
        self.play(
            Transform(explanation, Text("臂展 = 身高", font_size=24, color=YELLOW).to_edge(DOWN)),
            Create(arm_span_line), Write(span_text),
            Create(height_line), Write(height_text)
        )
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(vitruvian), FadeOut(navel_line),
            FadeOut(upper_brace), FadeOut(upper_text),
            FadeOut(lower_brace), FadeOut(lower_text),
            FadeOut(explanation), FadeOut(arm_span_line), FadeOut(span_text),
            FadeOut(height_line), FadeOut(height_text)
        )
    
    def show_facial_proportions(self):
        """面部的黄金比例 - 1:00-1:50"""
        title = Text("面部的黄金比例", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建面部轮廓
        face_outline = Ellipse(width=3, height=4, color=WHITE, stroke_width=2)
        
        # 面部特征（简化版）
        # 眼睛
        left_eye = Ellipse(width=0.5, height=0.3, color=WHITE, stroke_width=2)
        left_eye.shift(LEFT * 0.6 + UP * 0.8)
        right_eye = Ellipse(width=0.5, height=0.3, color=WHITE, stroke_width=2)
        right_eye.shift(RIGHT * 0.6 + UP * 0.8)
        
        # 鼻子（简单线条）
        nose = VGroup(
            Line(ORIGIN + UP * 0.4, ORIGIN + DOWN * 0.2, color=WHITE, stroke_width=2),
            Arc(radius=0.2, start_angle=PI, angle=PI, color=WHITE, stroke_width=2).shift(DOWN * 0.2)
        )
        
        # 嘴巴
        mouth = Arc(radius=0.4, start_angle=-2*PI/3, angle=PI/3, 
                   color=WHITE, stroke_width=2).shift(DOWN * 0.8)
        
        face = VGroup(face_outline, left_eye, right_eye, nose, mouth)
        
        self.play(Create(face))
        
        # 显示黄金比例线
        phi = (1 + np.sqrt(5)) / 2
        
        # 三条主要的黄金分割线
        hairline = DashedLine(LEFT * 2, RIGHT * 2, color=GOLD, stroke_width=2)
        hairline.shift(UP * 1.8)
        
        eyebrow_line = DashedLine(LEFT * 2, RIGHT * 2, color=GOLD, stroke_width=2)
        eyebrow_line.shift(UP * 1.1)
        
        nose_bottom_line = DashedLine(LEFT * 2, RIGHT * 2, color=GOLD, stroke_width=2)
        nose_bottom_line.shift(DOWN * 0.2)
        
        chin_line = DashedLine(LEFT * 2, RIGHT * 2, color=GOLD, stroke_width=2)
        chin_line.shift(DOWN * 2)
        
        golden_lines = VGroup(hairline, eyebrow_line, nose_bottom_line, chin_line)
        
        self.play(Create(golden_lines))
        
        # 标注各部分
        labels = VGroup(
            Text("发际线", font_size=16, color=YELLOW).next_to(hairline, RIGHT),
            Text("眉线", font_size=16, color=YELLOW).next_to(eyebrow_line, RIGHT),
            Text("鼻底", font_size=16, color=YELLOW).next_to(nose_bottom_line, RIGHT),
            Text("下巴", font_size=16, color=YELLOW).next_to(chin_line, RIGHT)
        )
        
        self.play(*[Write(label) for label in labels])
        
        # 显示比例关系
        # 使用括号标注
        upper_third = Brace(Line(hairline.get_center(), eyebrow_line.get_center()), LEFT)
        middle_third = Brace(Line(eyebrow_line.get_center(), nose_bottom_line.get_center()), LEFT)
        lower_third = Brace(Line(nose_bottom_line.get_center(), chin_line.get_center()), LEFT)
        
        ratio_text = Text("1 : φ : 1", font_size=24, color=GOLD)
        ratio_text.shift(LEFT * 3)
        
        self.play(
            Create(upper_third), Create(middle_third), Create(lower_third),
            Write(ratio_text)
        )
        
        # 眼睛间距的黄金比例
        eye_distance = DoubleArrow(
            left_eye.get_center(), right_eye.get_center(),
            color=GREEN, stroke_width=2
        ).shift(DOWN * 0.3)
        
        face_width = DoubleArrow(
            face_outline.get_left(), face_outline.get_right(),
            color=GREEN, stroke_width=2
        ).shift(DOWN * 3)
        
        eye_ratio = Text("眼距 : 面宽 = 1 : φ", font_size=20, color=GREEN)
        eye_ratio.to_edge(DOWN)
        
        self.play(
            Create(eye_distance), Create(face_width),
            Write(eye_ratio)
        )
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(face), FadeOut(golden_lines),
            FadeOut(labels), FadeOut(upper_third), FadeOut(middle_third),
            FadeOut(lower_third), FadeOut(ratio_text), FadeOut(eye_distance),
            FadeOut(face_width), FadeOut(eye_ratio)
        )
    
    def show_body_proportions(self):
        """身体各部分的黄金比例 - 1:50-2:40"""
        title = Text("身体各部分的黄金比例", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建简化的人体侧面图
        # 使用线条和基本形状
        body_height = 5
        
        # 主要节点
        head_top = UP * 2.5
        chin = UP * 2
        shoulder = UP * 1.5
        elbow = UP * 0.5
        navel = ORIGIN
        hip = DOWN * 0.5
        knee = DOWN * 1.5
        ankle = DOWN * 2.5
        
        # 绘制身体轮廓
        body_line = Line(head_top, ankle, color=WHITE, stroke_width=3)
        
        # 标记关键点
        key_points = VGroup(
            Dot(head_top, color=RED),
            Dot(chin, color=RED),
            Dot(shoulder, color=RED),
            Dot(elbow, color=RED),
            Dot(navel, color=GOLD, radius=0.1),  # 肚脐特别标记
            Dot(hip, color=RED),
            Dot(knee, color=RED),
            Dot(ankle, color=RED)
        )
        
        # 标签
        labels = VGroup(
            Text("头顶", font_size=16).next_to(head_top, RIGHT),
            Text("下巴", font_size=16).next_to(chin, RIGHT),
            Text("肩", font_size=16).next_to(shoulder, RIGHT),
            Text("肘", font_size=16).next_to(elbow, RIGHT),
            Text("肚脐", font_size=16, color=GOLD).next_to(navel, RIGHT),
            Text("髋", font_size=16).next_to(hip, RIGHT),
            Text("膝", font_size=16).next_to(knee, RIGHT),
            Text("踝", font_size=16).next_to(ankle, RIGHT)
        )
        
        body_diagram = VGroup(body_line, key_points, labels)
        body_diagram.shift(LEFT * 3)
        
        self.play(Create(body_line), Create(key_points))
        self.play(*[Write(label) for label in labels])
        
        # 显示黄金比例关系
        phi = (1 + np.sqrt(5)) / 2
        
        # 主要的黄金比例
        ratios = VGroup(
            Text("头顶到肚脐 : 肚脐到脚底 = 1 : φ", font_size=20, color=YELLOW),
            Text("肩到指尖 : 肘到指尖 = φ : 1", font_size=20, color=YELLOW),
            Text("髋到脚底 : 膝到脚底 = φ : 1", font_size=20, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 2)
        
        # 逐个展示比例
        # 1. 肚脐分割
        upper_body = Brace(Line(navel, head_top).shift(LEFT * 3), LEFT)
        lower_body = Brace(Line(ankle, navel).shift(LEFT * 3), LEFT)
        
        self.play(
            Create(upper_body), Create(lower_body),
            Write(ratios[0])
        )
        self.wait(1)
        
        # 2. 手臂比例（简化展示）
        self.play(
            FadeOut(upper_body), FadeOut(lower_body),
            Write(ratios[1])
        )
        self.wait(1)
        
        # 3. 腿部比例
        upper_leg = Brace(Line(hip, knee).shift(LEFT * 3), RIGHT)
        lower_leg = Brace(Line(knee, ankle).shift(LEFT * 3), RIGHT)
        
        self.play(
            Create(upper_leg), Create(lower_leg),
            Write(ratios[2])
        )
        self.wait(1)
        
        # 手部细节
        hand_title = Text("手部的黄金比例", font_size=24, color=GOLD)
        hand_title.to_edge(DOWN).shift(UP * 1.5)
        
        # 简化的手指图 - 放在右下角，避免与ratios重叠
        finger = VGroup(
            Rectangle(width=0.3, height=0.8, color=WHITE, stroke_width=2),  # 近节
            Rectangle(width=0.3, height=0.5, color=WHITE, stroke_width=2).shift(UP * 0.65),  # 中节
            Rectangle(width=0.3, height=0.3, color=WHITE, stroke_width=2).shift(UP * 1.05)   # 远节
        ).shift(RIGHT * 4 + DOWN * 2)
        
        finger_text = Text("指节长度递减符合黄金比", font_size=16, color=YELLOW)
        finger_text.next_to(finger, LEFT, buff=0.5)
        
        # 手部细节
        hand_title = Text("手部的黄金比例", font_size=24, color=GOLD)
        hand_title.to_edge(DOWN).shift(UP * 1.5)
        
        # 简化的手指图 - 放在右下角，避免与ratios重叠
        finger = VGroup(
            Rectangle(width=0.3, height=0.8, color=WHITE, stroke_width=2),  # 近节
            Rectangle(width=0.3, height=0.5, color=WHITE, stroke_width=2).shift(UP * 0.65),  # 中节
            Rectangle(width=0.3, height=0.3, color=WHITE, stroke_width=2).shift(UP * 1.05)   # 远节
        ).shift(RIGHT * 4 + DOWN * 2)
        
        finger_text = Text("指节长度递减符合黄金比", font_size=16, color=YELLOW)
        finger_text.next_to(finger, LEFT, buff=0.5)
        
        self.play(
            FadeOut(upper_leg), FadeOut(lower_leg),
            Write(hand_title),
            Create(finger),
            Write(finger_text)
        )
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(body_diagram), FadeOut(ratios),
            FadeOut(hand_title), FadeOut(finger), FadeOut(finger_text)
        )
    
    def show_aesthetic_standards(self):
        """黄金比例与美学标准 - 2:40-3:20"""
        title = Text("黄金比例定义美", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建对比展示
        # 左侧：符合黄金比例
        golden_face = self.create_golden_face().shift(LEFT * 3.5)
        golden_label = Text("黄金比例", font_size=20, color=GOLD)
        golden_label.next_to(golden_face, DOWN)
        
        # 右侧：偏离黄金比例
        non_golden_face = self.create_non_golden_face().shift(RIGHT * 3.5)
        non_golden_label = Text("偏离比例", font_size=20, color=GRAY)
        non_golden_label.next_to(non_golden_face, DOWN)
        
        self.play(
            Create(golden_face), Write(golden_label),
            Create(non_golden_face), Write(non_golden_label)
        )
        
        # 中间的说明
        explanation = VGroup(
            Text("为什么黄金比例看起来更美？", font_size=24, color=YELLOW),
            Text("• 符合大脑的视觉处理习惯", font_size=20, color=WHITE),
            Text("• 在自然界中普遍存在", font_size=20, color=WHITE),
            Text("• 产生和谐与平衡感", font_size=20, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).shift(DOWN * 1)
        
        self.play(Write(explanation[0]))
        for line in explanation[1:]:
            self.play(Write(line), run_time=0.8)
        
        self.wait(2)
        
        # 文化差异说明
        self.play(FadeOut(explanation))
        
        cultural_note = Text(
            "美的标准因文化而异，黄金比例只是其中一种",
            font_size=22, color=YELLOW
        ).shift(DOWN * 2)
        
        self.play(Write(cultural_note))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(golden_face), FadeOut(golden_label),
            FadeOut(non_golden_face), FadeOut(non_golden_label),
            FadeOut(cultural_note)
        )
    
    def create_golden_face(self):
        """创建符合黄金比例的面部"""
        face = Ellipse(width=1.5, height=2, color=WHITE, stroke_width=2)
        
        # 按黄金比例放置特征
        phi = (1 + np.sqrt(5)) / 2
        
        # 三等分线
        lines = VGroup(
            DashedLine(LEFT * 0.8, RIGHT * 0.8, color=GOLD, stroke_width=1).shift(UP * 0.67),
            DashedLine(LEFT * 0.8, RIGHT * 0.8, color=GOLD, stroke_width=1).shift(DOWN * 0.0),
            DashedLine(LEFT * 0.8, RIGHT * 0.8, color=GOLD, stroke_width=1).shift(DOWN * 0.67)
        )
        
        # 眼睛
        eyes = VGroup(
            Ellipse(width=0.25, height=0.15, color=WHITE, stroke_width=1).shift(LEFT * 0.3 + UP * 0.4),
            Ellipse(width=0.25, height=0.15, color=WHITE, stroke_width=1).shift(RIGHT * 0.3 + UP * 0.4)
        )
        
        # 鼻子
        nose = Line(UP * 0.2, DOWN * 0.1, color=WHITE, stroke_width=1)
        
        # 嘴巴
        mouth = Arc(radius=0.2, start_angle=-2*PI/3, angle=PI/3, 
                   color=WHITE, stroke_width=1).shift(DOWN * 0.4)
        
        return VGroup(face, lines, eyes, nose, mouth)
    
    def create_non_golden_face(self):
        """创建不符合黄金比例的面部"""
        face = Ellipse(width=1.5, height=2, color=GRAY, stroke_width=2)
        
        # 不规则的特征放置
        # 眼睛（太高）
        eyes = VGroup(
            Ellipse(width=0.25, height=0.15, color=GRAY, stroke_width=1).shift(LEFT * 0.3 + UP * 0.7),
            Ellipse(width=0.25, height=0.15, color=GRAY, stroke_width=1).shift(RIGHT * 0.3 + UP * 0.7)
        )
        
        # 鼻子（太长）
        nose = Line(UP * 0.4, DOWN * 0.2, color=GRAY, stroke_width=1)
        
        # 嘴巴（太低）
        mouth = Arc(radius=0.2, start_angle=-2*PI/3, angle=PI/3, 
                   color=GRAY, stroke_width=1).shift(DOWN * 0.7)
        
        return VGroup(face, eyes, nose, mouth)
    
    def show_modern_applications(self):
        """现代应用 - 3:20-3:50"""
        title = Text("黄金比例的现代应用", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 应用领域
        applications = VGroup(
            VGroup(
                Text("整形外科", font_size=24, color=BLUE),
                Text("• 面部轮廓设计", font_size=18, color=WHITE),
                Text("• 鼻型矫正参考", font_size=18, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT),
            
            VGroup(
                Text("时装设计", font_size=24, color=GREEN),
                Text("• 服装比例裁剪", font_size=18, color=WHITE),
                Text("• 模特身材标准", font_size=18, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT),
            
            VGroup(
                Text("健身美体", font_size=24, color=ORANGE),
                Text("• 理想身材目标", font_size=18, color=WHITE),
                Text("• 训练部位规划", font_size=18, color=WHITE)
            ).arrange(DOWN, aligned_edge=LEFT)
        ).arrange(RIGHT, buff=1.5).shift(DOWN * 0.5)
        
        for app in applications:
            self.play(Write(app[0]))
            for line in app[1:]:
                self.play(Write(line), run_time=0.5)
        
        self.wait(1)
        
        # 科技应用
        tech_title = Text("AI与黄金比例", font_size=28, color=YELLOW)
        tech_title.shift(DOWN * 2)
        
        tech_examples = Text(
            "人脸识别 • 美颜算法 • 虚拟形象设计",
            font_size=20, color=WHITE
        ).next_to(tech_title, DOWN)
        
        self.play(
            FadeOut(applications),
            Write(tech_title),
            Write(tech_examples)
        )
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(tech_title), FadeOut(tech_examples)
        )
    
    def show_ending(self):
        """结尾 - 3:50-4:20"""
        # 总结
        summary_lines = [
            Text("人体——自然的黄金比例杰作", font_size=36, color=WHITE),
            Text("从整体到局部的和谐统一", font_size=36, color=WHITE),
            Text("数学规律与生命之美的完美结合", font_size=36, color=WHITE),
            Text("美，源于比例", font_size=42, color=GOLD)
        ]
        summary = VGroup(*summary_lines).arrange(DOWN, buff=0.5)
        
        for line in summary_lines:
            self.play(Write(line), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(summary))
        
        # 下期预告
        next_episode = VGroup(
            Text("下期预告", font_size=36, color=YELLOW),
            Text("音乐和弦中的数学", font_size=32, color=WHITE),
            Text("聆听数字的旋律", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(next_episode[0]), run_time=1)
        self.play(FadeIn(next_episode[1], shift=UP), run_time=1)
        self.play(FadeIn(next_episode[2], shift=UP), run_time=1)
        
        # 订阅提醒
        subscribe = Text("喜欢请三连支持！", font_size=32, color=RED)
        subscribe.next_to(next_episode, DOWN, buff=1)
        
        self.play(Write(subscribe))
        self.wait(3)