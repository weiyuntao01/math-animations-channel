

"""
INF_EP02: 芝诺悖论 (Zeno's Paradox)
阿喀琉斯为什么追不上乌龟？无穷级数与极限。
"""

from manim import *
import numpy as np

# --- 颜色定义 ---
INF_PURPLE = "#7C3AED"   # 神秘紫
INF_GOLD = "#FBBF24"     # 无穷金
INF_BLUE = "#3B82F6"     # 阿喀琉斯
INF_GREEN = "#10B981"    # 乌龟
INF_RED = "#EF4444"      # 悖论/错误
INF_GRAY = "#6B7280"     # 背景/中性
BG_COLOR = "#0F172A"     # 深蓝灰背景

class InfinityEP02(Scene):
    """无穷系列 EP02：芝诺悖论"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场
        self.intro_transition()
        
        # 2. 场景构建：赛跑开始
        # 返回 race_group 用于后续操作
        race_group, positions = self.setup_race()
        
        # 3. 悖论演示：无限分割的步骤
        self.animate_paradox_steps(race_group, positions)
        
        # 4. 数学解决：几何级数可视化
        self.geometric_series_resolution()
        
        # 5. 哲学升华与结尾
        self.show_ending()

    def intro_transition(self):
        old_series = Text("EP01: 希尔伯特旅馆 (无穷大)", font_size=32, color=INF_GRAY).to_edge(UP)
        new_series = Text("EP02: 芝诺悖论", font_size=54, color=INF_GOLD, weight=BOLD)
        subtitle = Text("无穷小：阿喀琉斯与乌龟", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        question = Text("逻辑上永远追不上，\n现实中却瞬间超越？", font_size=24, color=INF_PURPLE).next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(question))
        self.wait(2)
        
        self.play(FadeOut(new_series), FadeOut(subtitle), FadeOut(question))

    def setup_race(self):
            """构建赛跑场景 (修复版：调整位置防止超屏)"""
            
            # --- 布局调整 ---
            # 原来 length=9 太长了，导致起点超出屏幕左侧
            # 现在改为 length=6，并调整中心点，确保在屏幕左半部分居中
            TRACK_LEN = 6.0
            TRACK_CENTER = LEFT * 3.5 
            
            title = Text("思想实验：绝对公平的赛跑？", font_size=36, color=INF_GOLD).to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            # 跑道数轴
            track = NumberLine(
                x_range=[0, 100, 10],
                length=TRACK_LEN,
                color=WHITE,
                include_numbers=True,
                font_size=16
            ).move_to(TRACK_CENTER + DOWN * 0.5)
            
            track_label = Text("距离 (米)", font_size=20, color=INF_GRAY).next_to(track, DOWN)
            
            # 角色图标
            # 兔子 (R) - 起点 0
            rabbit = self.create_runner("R", INF_BLUE, scale=0.8)
            rabbit.move_to(track.n2p(0) + UP * 0.8)
            
            # 乌龟 (T) - 起点 50 (让路50米)
            tortoise = self.create_runner("T", INF_GREEN, scale=0.6)
            tortoise.move_to(track.n2p(50) + UP * 0.6)
            
            # 初始标签 (稍微缩小字号防止拥挤)
            label_r = Text("兔子\n10m/s", font_size=18, color=INF_BLUE).next_to(rabbit, UP, buff=0.1)
            label_t = Text("乌龟\n1m/s", font_size=18, color=INF_GREEN).next_to(tortoise, UP, buff=0.1)
            label_t.shift(UP * 0.2)
            
            self.play(Create(track), Write(track_label))
            self.play(FadeIn(rabbit), Write(label_r))
            self.play(FadeIn(tortoise), Write(label_t))
            
            # 打包返回
            race_group = VGroup(track, track_label, rabbit, tortoise, label_r, label_t)
            positions = {"R": 0, "T": 50} 
            
            return race_group, positions
    def create_runner(self, label, color, scale=1.0):
        """创建选手图标"""
        icon = VGroup(
            Circle(radius=0.4, color=color, fill_opacity=0.5),
            Text(label, font_size=32, color=WHITE)
        ).scale(scale)
        return icon

    def animate_paradox_steps(self, race_group, positions):
            """演示芝诺的逻辑步骤 (兔子版)"""
            
            track = race_group[0]
            # race_group[2] 现在是兔子
            rabbit = race_group[2] 
            tortoise = race_group[3]
            label_r = race_group[4]
            label_t = race_group[5]
            
            # 右侧逻辑说明区
            RIGHT_ZONE = RIGHT * 4.0
            
            logic_title = Text("芝诺的逻辑：", font_size=28, color=INF_PURPLE, weight=BOLD)
            logic_title.move_to(RIGHT_ZONE + UP * 2.0)
            self.play(Write(logic_title))
            
            # 步骤演示
            # 速度：兔子=10, 乌龟=1. 比例 10:1
            
            steps_data = [
                # (兔子的目标, 乌龟的移动距离)
                # 步骤1: 兔子跑到50, 乌龟跑了5 (到55)
                (50, 5, "步骤 1: 追到起点"),
                # 步骤2: 兔子跑到55, 乌龟跑了0.5 (到55.5)
                (55, 0.5, "步骤 2: 追到新位置"),
                # 步骤3: 兔子跑到55.5, 乌龟跑了0.05 (到55.55)
                (55.5, 0.05, "步骤 3: 还在追...")
            ]
            
            prev_text = logic_title
            
            for i, (r_target, t_move, text) in enumerate(steps_data):
                # 文字说明
                step_text = Text(text, font_size=22, color=WHITE)
                step_text.next_to(prev_text, DOWN, buff=0.4)
                step_text.align_to(logic_title, LEFT)
                
                # 详细距离 (修改文案为兔子)
                detail = Text(f"兔子跑了 {r_target - positions['R']:.1f}m\n乌龟跑了 {t_move:.2f}m", font_size=18, color=INF_GRAY)
                detail.next_to(step_text, DOWN, buff=0.1).align_to(step_text, LEFT)
                
                self.play(Write(step_text), Write(detail))
                
                # 动画：两人同时移动
                t_target = positions['T'] + t_move
                
                self.play(
                    rabbit.animate.move_to(track.n2p(r_target) + UP * 0.8),
                    label_r.animate.next_to(track.n2p(r_target) + UP * 0.8, UP),
                    tortoise.animate.move_to(track.n2p(t_target) + UP * 0.6),
                    label_t.animate.next_to(track.n2p(t_target) + UP * 0.6 + UP*0.2, UP),
                    run_time=1.5
                )
                
                # 更新位置记录
                positions['R'] = r_target
                positions['T'] = t_target
                prev_text = detail
                
                self.wait(0.5)
                
            # 结论
            paradox_text = Text("步骤有无穷多个...\n所以时间是无穷大？", font_size=24, color=INF_RED, weight=BOLD)
            paradox_text.next_to(prev_text, DOWN, buff=0.6).align_to(logic_title, LEFT)
            self.play(Write(paradox_text))
            
            self.wait(2)
            
            # 清理
            self.play(FadeOut(Group(*self.mobjects)))
    def geometric_series_resolution(self):
            """数学解决：几何级数求和"""
            
            title = Text("数学的破解：无穷级数", font_size=36, color=INF_GREEN).to_edge(UP)
            self.play(Write(title))
            
            # 1. 建立时间条 (Time Bar)
            # 用一个长方形代表总时间
            bar_width = 10
            total_bar = Rectangle(width=bar_width, height=1, color=WHITE).move_to(UP * 0.5)
            bar_label = Text("总时间", font_size=24).next_to(total_bar, UP)
            
            self.play(Create(total_bar), Write(bar_label))
            
            # 2. 填充时间切片
            # 假设第一步耗时 5秒 (跑50米/10速度)
            # 第二步耗时 0.5秒
            # 第三步耗时 0.05秒
            # 这是一个公比为 0.1 的等比数列
            
            # 为了视觉效果，我们演示一个公比为 0.5 的级数 (Zeno's Dichotomy)，更直观
            # 1/2 + 1/4 + 1/8 ... = 1
            
            segments = VGroup()
            current_x = total_bar.get_left()[0]
            widths = [bar_width/2, bar_width/4, bar_width/8, bar_width/16, bar_width/32]
            colors = [INF_BLUE, INF_PURPLE, INF_RED, INF_GOLD, INF_GREEN]
            labels = ["1/2", "1/4", "1/8", "1/16", "..."]
            
            desc_text = Text("把时间切成无穷份：", font_size=24, color=INF_GRAY).move_to(UP * 2)
            self.play(Write(desc_text))
            
            for i, w in enumerate(widths):
                # 创建色块
                rect = Rectangle(width=w, height=1, fill_color=colors[i], fill_opacity=0.8, stroke_width=1)
                rect.move_to(np.array([current_x + w/2, total_bar.get_center()[1], 0]))
                
                # 创建标签
                if i < 4:
                    lbl = Text(labels[i], font_size=20, color=WHITE).move_to(rect.get_center())
                    self.play(FadeIn(rect), Write(lbl), run_time=0.5)
                    segments.add(rect, lbl)
                else:
                    # 最后的省略号
                    lbl = Text(labels[i], font_size=20, color=WHITE).next_to(rect, RIGHT, buff=0.1)
                    self.play(FadeIn(rect), Write(lbl), run_time=0.5)
                    segments.add(rect, lbl)
                    
                current_x += w
                
            # 3. 公式推导
            # 放在下方
            formula_group = VGroup()
            
            eq1 = MathTex(r"S = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots", font_size=36)
            eq2 = MathTex(r"S = \sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n", font_size=36)
            eq3 = MathTex(r"= \frac{a}{1-r} = \frac{1/2}{1-1/2} = 1", font_size=40, color=INF_GREEN)
            
            formula_group.add(eq1, eq2, eq3)
            formula_group.arrange(DOWN, buff=0.4).move_to(DOWN * 2.0)
            
            self.play(Write(eq1))
            self.wait(0.5)
            self.play(TransformMatchingTex(eq1.copy(), eq2))
            self.wait(0.5)
            self.play(Write(eq3))
            
            # 4. 结论
            conclusion = Text("无穷多个时间片段的和，是有限的！", font_size=32, color=INF_GOLD, weight=BOLD)
            conclusion.next_to(formula_group, UP, buff=0.5) # 放在公式上方，强调
            self.play(Write(conclusion))
            
            self.wait(3)
            self.play(FadeOut(Group(*self.mobjects)))

    def show_ending(self):
        # 总结
        summary_title = Text("芝诺的错误：", font_size=36, color=INF_PURPLE)
        summary_title.to_edge(UP)
        
        summary_points = VGroup(
            Text("1. 他认为：过程无限 = 结果无限", font_size=26),
            Text("2. 实际上：时空是连续统一体", font_size=26),
            Text("3. 微积分让我们驯服了无穷", font_size=26, color=INF_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary_title), Write(summary_points))
        self.wait(2)
        
        self.play(FadeOut(summary_title), FadeOut(summary_points))
        
        # 预告
        next_ep = Text("下期预告：加百列的号角", font_size=40, color=INF_GOLD)
        desc = Text("一个体积有限，表面积却无限的物体\n你填得满它，却刷不完它？", font_size=24, color=INF_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)