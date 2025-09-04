from manim import *
import numpy as np

class MusicMathematicsEP6(Scene):
    """音乐和弦中的数学 - 黄金分割系列 EP06"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：音程与频率比
        self.show_frequency_ratios()
        
        # 第二部分：毕达哥拉斯音律
        self.show_pythagorean_tuning()
        
        # 第三部分：黄金比例与音阶
        self.show_golden_ratio_in_scales()
        
        # 第四部分：斐波那契与音乐结构
        self.show_fibonacci_in_music()
        
        # 第五部分：和弦的数学之美
        self.show_chord_mathematics()
        
        # 结尾
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第六集：音乐和弦中的数学", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_frequency_ratios(self):
        """音程与频率比 - 0:10-0:50"""
        title = Text("音程的数学本质", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建音叉示意图（简化版）
        def create_tuning_fork(freq, label):
            """创建音叉示意图"""
            fork = VGroup(
                Line(ORIGIN, UP * 1.5, color=GRAY, stroke_width=3),
                Line(UP * 1.5 + LEFT * 0.3, UP * 2.5 + LEFT * 0.3, color=GRAY, stroke_width=3),
                Line(UP * 1.5 + RIGHT * 0.3, UP * 2.5 + RIGHT * 0.3, color=GRAY, stroke_width=3)
            )
            freq_text = Text(f"{freq}Hz", font_size=20, color=WHITE)
            freq_text.next_to(fork, DOWN)
            note_label = Text(label, font_size=24, color=YELLOW)
            note_label.next_to(freq_text, DOWN)
            return VGroup(fork, freq_text, note_label)
        
        # 展示基础音和八度音
        c4_fork = create_tuning_fork("440", "A4").shift(LEFT * 3)
        c5_fork = create_tuning_fork("880", "A5").shift(RIGHT * 3)
        
        self.play(Create(c4_fork[0]), Write(c4_fork[1]), Write(c4_fork[2]))
        self.play(Create(c5_fork[0]), Write(c5_fork[1]), Write(c5_fork[2]))
        
        # 显示频率比
        ratio_arrow = DoubleArrow(
            c4_fork.get_right() + RIGHT * 0.5,
            c5_fork.get_left() + LEFT * 0.5,
            color=GREEN
        )
        ratio_text = Text("2:1", font_size=36, color=GREEN)
        ratio_text.next_to(ratio_arrow, UP)
        octave_text = Text("纯八度", font_size=24, color=WHITE)
        octave_text.next_to(ratio_arrow, DOWN)
        
        self.play(Create(ratio_arrow), Write(ratio_text), Write(octave_text))
        
        # 说明
        explanation = Text(
            "频率翻倍 = 高八度",
            font_size=24, color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 清理并准备下一个展示
        self.play(
            FadeOut(c4_fork), FadeOut(c5_fork),
            FadeOut(ratio_arrow), FadeOut(ratio_text),
            FadeOut(octave_text), FadeOut(explanation)
        )
        
        # 展示简单整数比
        intervals = [
            ("1:1", "纯一度", "C"),
            ("2:1", "纯八度", "C'"),
            ("3:2", "纯五度", "G"),
            ("4:3", "纯四度", "F"),
            ("5:4", "大三度", "E")
        ]
        
        interval_display = VGroup()
        for i, (ratio, name, note) in enumerate(intervals):
            ratio_mob = Text(ratio, font_size=28, color=BLUE)
            name_mob = Text(name, font_size=24, color=WHITE)
            note_mob = Text(note, font_size=24, color=YELLOW)
            
            group = VGroup(ratio_mob, name_mob, note_mob).arrange(RIGHT, buff=0.5)
            group.shift(UP * (2 - i * 0.8))
            interval_display.add(group)
        
        interval_display.shift(LEFT * 0.5)
        
        self.play(*[Write(group) for group in interval_display])
        
        # 强调简单整数比
        emphasis = Text(
            "和谐的音程 = 简单的整数比",
            font_size=28, color=GOLD
        ).to_edge(DOWN)
        
        self.play(Write(emphasis))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(interval_display), FadeOut(emphasis)
        )
    
    def show_pythagorean_tuning(self):
        """毕达哥拉斯音律 - 0:50-1:30"""
        title = Text("毕达哥拉斯的发现", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建弦的示意图
        string_length = 6
        string_y = 0
        
        # 全弦 - 向下移动避免重叠
        full_string = Line(
            LEFT * string_length/2, RIGHT * string_length/2,
            color=WHITE, stroke_width=4
        ).shift(UP * 0.5)
        
        # 支撑点
        left_support = Line(
            full_string.get_left() + DOWN * 0.2,
            full_string.get_left() + UP * 0.2,
            color=GRAY, stroke_width=6
        )
        right_support = Line(
            full_string.get_right() + DOWN * 0.2,
            full_string.get_right() + UP * 0.2,
            color=GRAY, stroke_width=6
        )
        
        self.play(
            Create(full_string),
            Create(left_support),
            Create(right_support)
        )
        
        # 标记分割点
        divisions = [
            (1/2, "1:2", "八度"),
            (2/3, "2:3", "五度"),
            (3/4, "3:4", "四度")
        ]
        
        markers = VGroup()
        labels = VGroup()
        
        for frac, ratio, interval in divisions:
            # 分割点标记
            pos = full_string.get_left() + RIGHT * string_length * frac
            marker = Line(
                pos + DOWN * 0.3,
                pos + UP * 0.3,
                color=RED, stroke_width=3
            )
            markers.add(marker)
            
            # 标签
            label = VGroup(
                Text(ratio, font_size=20, color=YELLOW),
                Text(interval, font_size=16, color=WHITE)
            ).arrange(DOWN, buff=0.1)
            label.next_to(marker, DOWN, buff=0.5)
            labels.add(label)
        
        self.play(*[Create(marker) for marker in markers])
        self.play(*[Write(label) for label in labels])
        
        # 展示振动模式
        vibration_text = Text(
            "弦长比例决定音高",
            font_size=24, color=YELLOW
        ).shift(DOWN * 2.5)  # 进一步下移，确保不与标签重叠
        
        self.play(Write(vibration_text))
        
        # 创建五度相生圈
        self.wait(1)
        self.play(
            FadeOut(full_string), FadeOut(left_support), FadeOut(right_support),
            FadeOut(markers), FadeOut(labels), FadeOut(vibration_text)
        )
        
        # 五度圈
        circle_of_fifths_label = Text("五度相生", font_size=28, color=GOLD)
        circle_of_fifths_label.shift(UP * 1.5)
        self.play(Write(circle_of_fifths_label))
        
        # 简化的五度圈
        notes = ["C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "F"]
        circle_radius = 2
        
        note_dots = VGroup()
        note_labels = VGroup()
        
        for i, note in enumerate(notes):
            angle = -PI/2 + i * TAU / 12  # 从顶部开始
            pos = circle_radius * np.array([np.cos(angle), np.sin(angle), 0])
            
            dot = Dot(pos, color=BLUE, radius=0.08)
            label = Text(note, font_size=18, color=WHITE)
            label.move_to(pos * 1.3)
            
            note_dots.add(dot)
            note_labels.add(label)
        
        circle = Circle(radius=circle_radius, color=GRAY, stroke_width=1)
        
        self.play(Create(circle))
        self.play(
            *[Create(dot) for dot in note_dots],
            *[Write(label) for label in note_labels]
        )
        
        # 显示3:2的关系
        arrow1 = CurvedArrow(
            note_dots[0].get_center(),
            note_dots[1].get_center(),
            color=YELLOW,
            angle=TAU/24
        )
        ratio_label = Text("3:2", font_size=16, color=YELLOW)
        ratio_label.move_to(arrow1.get_center() * 0.7)
        
        self.play(Create(arrow1), Write(ratio_label))
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(circle_of_fifths_label),
            FadeOut(circle), FadeOut(note_dots), FadeOut(note_labels),
            FadeOut(arrow1), FadeOut(ratio_label)
        )
    
    def show_golden_ratio_in_scales(self):
        """黄金比例与音阶 - 1:30-2:20"""
        title = Text("音阶中的黄金比例", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 钢琴键盘示意图
        def create_piano_keys():
            """创建简化的钢琴键盘"""
            white_keys = VGroup()
            black_keys = VGroup()
            
            # 白键
            for i in range(8):
                key = Rectangle(
                    width=0.6, height=2.5,
                    color=WHITE, fill_color=WHITE, fill_opacity=1,
                    stroke_width=2
                )
                key.shift(RIGHT * i * 0.65 + LEFT * 2.5)
                white_keys.add(key)
            
            # 黑键位置 (C#, D#, F#, G#, A#)
            black_positions = [0.65, 1.3, 2.6, 3.25, 3.9]
            for pos in black_positions:
                key = Rectangle(
                    width=0.4, height=1.5,
                    color=BLACK, fill_color=BLACK, fill_opacity=1,
                    stroke_width=2
                )
                key.shift(RIGHT * pos + LEFT * 2.5 + UP * 0.5)
                black_keys.add(key)
            
            return VGroup(white_keys, black_keys)
        
        piano = create_piano_keys()
        piano.shift(UP * 0.5)
        
        self.play(Create(piano))
        
        # 标记音名
        note_names = ["C", "D", "E", "F", "G", "A", "B", "C'"]
        note_labels = VGroup()
        for i, name in enumerate(note_names):
            label = Text(name, font_size=16, color=BLUE)
            label.shift(RIGHT * i * 0.65 + LEFT * 2.5 + DOWN * 1.5)
            note_labels.add(label)
        
        self.play(*[Write(label) for label in note_labels])
        
        # 展示大六度音程
        phi = (1 + np.sqrt(5)) / 2
        
        # C到A的标记
        c_pos = piano[0][0].get_center()
        a_pos = piano[0][5].get_center()
        
        interval_arrow = CurvedArrow(
            c_pos + DOWN * 1.8,
            a_pos + DOWN * 1.8,
            color=GOLD,
            angle=-TAU/8
        )
        
        # 频率比接近黄金比例
        ratio_text = VGroup(
            Text("大六度", font_size=20, color=GOLD),
            MathTex(r"\frac{5}{3} \approx 1.667", font_size=24, color=YELLOW),
            MathTex(r"\varphi \approx 1.618", font_size=24, color=GOLD)
        ).arrange(DOWN, buff=0.2)
        ratio_text.shift(DOWN * 2.5)
        
        self.play(Create(interval_arrow))
        self.play(Write(ratio_text))
        
        # 黄金分割点
        explanation = Text(
            "大六度最接近黄金比例",
            font_size=24, color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(piano), FadeOut(note_labels),
            FadeOut(interval_arrow), FadeOut(ratio_text),
            FadeOut(explanation)
        )
    
    def show_fibonacci_in_music(self):
        """斐波那契与音乐结构 - 2:20-3:10"""
        title = Text("斐波那契数列与音乐结构", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 斐波那契数列
        fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21]
        fib_display = VGroup()
        
        for i, num in enumerate(fib_numbers):
            num_text = Text(str(num), font_size=32, color=BLUE)
            num_text.shift(LEFT * 3 + RIGHT * i * 0.8 + UP * 2)
            fib_display.add(num_text)
        
        self.play(*[Write(num) for num in fib_display])
        
        # 音乐小节结构示例
        measures_label = Text("音乐结构", font_size=24, color=YELLOW)
        measures_label.shift(LEFT * 2.5 + UP * 0.5)
        self.play(Write(measures_label))
        
        # 创建小节表示
        def create_measure_blocks(sections):
            """创建音乐小节块"""
            blocks = VGroup()
            colors = [BLUE, GREEN, ORANGE, RED]
            start_x = -3.5
            
            for i, (length, label) in enumerate(sections):
                block = Rectangle(
                    width=length * 0.3,
                    height=0.8,
                    color=colors[i % len(colors)],
                    fill_opacity=0.5,
                    stroke_width=2
                )
                block.shift(RIGHT * start_x + RIGHT * block.get_width()/2)
                
                text = Text(label, font_size=16, color=WHITE)
                text.move_to(block.get_center())
                
                blocks.add(VGroup(block, text))
                start_x += block.get_width() + 0.1
            
            return blocks
        
        # 展示8小节结构 (3+5)
        structure_8 = create_measure_blocks([
            (3, "A部分\n3小节"),
            (5, "B部分\n5小节")
        ])
        structure_8.shift(DOWN * 0.5)
        
        self.play(*[Create(block) for block in structure_8])
        
        # 展示13小节结构 (5+8)
        structure_13 = create_measure_blocks([
            (5, "前奏\n5小节"),
            (8, "主题\n8小节")
        ])
        structure_13.shift(DOWN * 2)
        
        self.play(*[Create(block) for block in structure_13])
        
        # 黄金分割点标记
        golden_point = Line(
            UP * 0.2 + RIGHT * 0.7,
            DOWN * 2.5 + RIGHT * 0.7,
            color=GOLD,
            stroke_width=3
        )
        golden_label = Text("黄金分割点", font_size=18, color=GOLD)
        golden_label.next_to(golden_point, UP)
        
        self.play(Create(golden_point), Write(golden_label))
        
        # 实例说明
        example = Text(
            "巴托克、德彪西常用斐波那契结构",
            font_size=22, color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(example))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(fib_display), FadeOut(measures_label),
            FadeOut(structure_8), FadeOut(structure_13),
            FadeOut(golden_point), FadeOut(golden_label),
            FadeOut(example)
        )
    
    def show_chord_mathematics(self):
        """和弦的数学之美 - 3:10-3:50"""
        title = Text("和弦的数学之美", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 大三和弦的频率比
        chord_label = Text("C大三和弦", font_size=28, color=YELLOW)
        chord_label.shift(UP * 1.5)  # 从 UP * 2 改为 UP * 1.5，避免与标题重叠
        self.play(Write(chord_label))
        
        # 创建频率可视化
        base_freq = 1
        frequencies = {
            "C": base_freq,
            "E": base_freq * 5/4,
            "G": base_freq * 3/2
        }
        
        # 波形示意图
        wave_group = VGroup()
        wave_labels = VGroup()
        
        y_positions = [0.7, 0, -0.7]  # 增加间距
        colors = [RED, GREEN, BLUE]
        
        for i, (note, freq) in enumerate(frequencies.items()):
            # 创建正弦波
            wave = FunctionGraph(
                lambda x: 0.3 * np.sin(2 * PI * freq * x),
                x_range=[-3, 3],
                color=colors[i]
            ).shift(UP * y_positions[i])
            
            # 标签
            label = VGroup(
                Text(note, font_size=20, color=colors[i]),
                Text(f"频率比: {freq:.3f}", font_size=16, color=WHITE)
            ).arrange(DOWN, buff=0.1)
            label.shift(LEFT * 4.5 + UP * y_positions[i])  # 稍微左移避免与波形重叠
            
            wave_group.add(wave)
            wave_labels.add(label)
        
        self.play(*[Create(wave) for wave in wave_group])
        self.play(*[Write(label) for label in wave_labels])
        
        # 合成波形
        composite_label = Text("合成波形", font_size=20, color=YELLOW)
        composite_label.shift(DOWN * 1.5)  # 稍微上移
        
        composite_wave = FunctionGraph(
            lambda x: 0.3 * (np.sin(2 * PI * x) + 
                           np.sin(2 * PI * 5/4 * x) + 
                           np.sin(2 * PI * 3/2 * x)),
            x_range=[-3, 3],
            color=YELLOW,
            stroke_width=3
        ).shift(DOWN * 2.2)  # 相应调整
        
        self.play(Write(composite_label), Create(composite_wave))
        
        # 频率比关系
        ratio_explanation = VGroup(
            Text("C : E : G = 4 : 5 : 6", font_size=24, color=GOLD),
            Text("简单整数比 = 和谐音响", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        ratio_explanation.shift(RIGHT * 4.5 + UP * 0.5)  # 调整到右上方，避免与波形重叠
        
        self.play(Write(ratio_explanation))
        
        self.wait(2)
        
        # 展示不和谐和弦
        self.play(
            FadeOut(wave_group), FadeOut(wave_labels),
            FadeOut(composite_wave), FadeOut(composite_label),
            FadeOut(ratio_explanation)
        )
        
        # 不和谐示例
        discord_label = Text("增四度（魔鬼音程）", font_size=24, color=RED)
        discord_label.shift(UP * 1.5)  # 保持与chord_label相同高度
        
        discord_ratio = VGroup(
            MathTex(r"\frac{\sqrt{2}}{1} \approx 1.414", font_size=28, color=RED),
            Text("无理数比 = 不和谐", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        discord_ratio.shift(DOWN * 0.5)  # 调整位置避免重叠
        
        self.play(
            Transform(chord_label, discord_label),
            Write(discord_ratio)
        )
        
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(title), FadeOut(chord_label), FadeOut(discord_ratio)
        )
    
    def show_ending(self):
        """结尾 - 3:50-4:20"""
        # 总结
        summary_lines = [
            Text("音乐——时间中的数学", font_size=36, color=WHITE),
            Text("从毕达哥拉斯到巴赫", font_size=36, color=WHITE),
            Text("简单比例创造和谐之声", font_size=36, color=WHITE),
            Text("数学，音乐的灵魂", font_size=42, color=GOLD)
        ]
        summary = VGroup(*summary_lines).arrange(DOWN, buff=0.5)
        
        for line in summary_lines:
            self.play(Write(line), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(summary))
        
        # 下期预告
        next_episode = VGroup(
            Text("下期预告", font_size=36, color=YELLOW),
            Text("建筑设计的数学美学", font_size=32, color=WHITE),
            Text("从金字塔到摩天大楼", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(next_episode[0]), run_time=1)
        self.play(FadeIn(next_episode[1], shift=UP), run_time=1)
        self.play(FadeIn(next_episode[2], shift=UP), run_time=1)
        
        # 订阅提醒
        subscribe = Text("喜欢请三连支持！", font_size=32, color=RED)
        subscribe.next_to(next_episode, DOWN, buff=1)
        
        self.play(Write(subscribe))
        self.wait(3)