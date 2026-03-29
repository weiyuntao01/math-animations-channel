
"""
INF_EP04: 分形几何 (Fractals)
英国的海岸线有多长？有限面积内的无限周长。
"""

from manim import *
import numpy as np

# --- 颜色定义 ---
INF_PURPLE = "#7C3AED"   # 神秘紫
INF_GOLD = "#FBBF24"     # 无穷金
INF_BLUE = "#3B82F6"     # 几何蓝
INF_RED = "#EF4444"      # 悖论红
INF_GREEN = "#10B981"    # 答案绿
INF_GRAY = "#6B7280"     # 背景灰
BG_COLOR = "#0F172A"     # 深蓝灰背景

class InfinityEP04(Scene):
    """无穷系列 EP04：分形几何"""
    
    def construct(self):
            # 0. 全局设置
            Text.set_default(font="Microsoft YaHei")
            self.camera.background_color = BG_COLOR
            
            # 1. 开场：海岸线悖论
            self.intro_coastline()
            
            # 2. 构造：科赫雪花
            # 修复：接收返回的 text_group 以便后续清理
            snowflake, text_group_to_clear = self.construct_koch_snowflake()
            
            # 3. 数学分析：周长与面积
            # 修复：传入 text_group_to_clear 进行清理
            self.analyze_math(snowflake, text_group_to_clear)
            
            # 4. 概念升华：分数维度
            self.explain_fractional_dimension()
            
            # 5. 结尾
            self.show_ending()

    def intro_coastline(self):
        """开场：海岸线悖论"""
        
        old_series = Text("EP03: 加百列的号角 (体积vs面积)", font_size=32, color=INF_GRAY).to_edge(UP)
        new_series = Text("EP04: 分形几何", font_size=54, color=INF_BLUE, weight=BOLD)
        subtitle = Text("Coastline Paradox (海岸线悖论)", font_size=28, color=WHITE).next_to(new_series, DOWN, buff=0.4)
        
        self.play(Write(old_series))
        self.wait(0.5)
        self.play(
            ReplacementTransform(old_series, new_series),
            FadeIn(subtitle, shift=UP)
        )
        
        # 模拟海岸线
        coastline_points = [
            [-3, 2, 0], [-2, 1.5, 0], [-1, 2.2, 0], [0, 1.8, 0], 
            [1, 2.5, 0], [2, 1.2, 0], [3, 2, 0]
        ]
        coastline = VMobject(color=INF_GOLD, stroke_width=4).set_points_smoothly(coastline_points)
        coastline.move_to(ORIGIN)
        
        question = Text("这条海岸线有多长？", font_size=32).next_to(coastline, UP, buff=1.0)
        self.play(Create(coastline), Write(question))
        
        # 尺子测量动画
        ruler_1 = Line(coastline.get_left(), coastline.get_right(), color=INF_RED, stroke_width=4)
        label_1 = Text("直尺测量：短", font_size=24, color=INF_RED).next_to(ruler_1, DOWN)
        
        self.play(Create(ruler_1), Write(label_1))
        self.wait(1)
        
        # 这是一个简化的示意，实际应用分形生成
        msg = Text("尺子越短，测得的长度越长！", font_size=28, color=INF_PURPLE, weight=BOLD).move_to(DOWN * 2)
        self.play(Write(msg))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def construct_koch_snowflake(self):
        """构造科赫雪花 (修复重叠版)"""
        
        # 布局
        LEFT_ZONE = LEFT * 3.0
        RIGHT_ZONE = RIGHT * 3.5
        
        title = Text("科赫雪花 (Koch Snowflake)", font_size=36, color=INF_BLUE).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 初始三角形 (稍微缩小半径，防止生长后遮挡)
        radius = 1.8
        v1 = [radius * np.cos(PI/6 + 2*PI/3 * 0), radius * np.sin(PI/6 + 2*PI/3 * 0), 0]
        v2 = [radius * np.cos(PI/6 + 2*PI/3 * 1), radius * np.sin(PI/6 + 2*PI/3 * 1), 0]
        v3 = [radius * np.cos(PI/6 + 2*PI/3 * 2), radius * np.sin(PI/6 + 2*PI/3 * 2), 0]
        
        points = [v1, v2, v3, v1] 
        
        snowflake = VMobject(color=INF_BLUE, stroke_width=2).set_points_as_corners(points)
        snowflake.move_to(LEFT_ZONE)
        
        # 标签区
        level_label = Text("Level 0", font_size=32, color=WHITE).move_to(RIGHT_ZONE + UP * 1.0)
        desc = Text("每条边变为 4 段", font_size=24, color=INF_GOLD).next_to(level_label, DOWN, buff=0.5)
        
        # 初始显示
        self.play(Create(snowflake), Write(level_label))
        # 这里不立即显示 desc，在循环里统一处理
        
        prev_desc = desc # 初始化引用
        
        # 迭代过程
        iterations = 4
        
        for i in range(iterations):
            # 1. 计算几何
            current_points = snowflake.get_points() # 获取不到顶点，需要重新计算
            # 这里的 points 变量一直保存着顶点数据
            points = self.get_koch_points(points)
            
            new_snowflake = VMobject(color=INF_BLUE, stroke_width=2).set_points_as_corners(points)
            new_snowflake.move_to(LEFT_ZONE)
            
            # 2. 准备文字
            new_label = Text(f"Level {i+1}", font_size=32, color=WHITE).move_to(level_label.get_center())
            
            if i == 0:
                new_desc_text = "每条边变为 4 段"
                col = INF_GOLD
            elif i == 1:
                new_desc_text = "长度增加 1/3"
                col = INF_GREEN
            elif i == 2:
                new_desc_text = "细节无限增加"
                col = INF_PURPLE
            else:
                new_desc_text = "形状趋于稳定"
                col = INF_GRAY
            
            new_desc = Text(new_desc_text, font_size=24, color=col).next_to(new_label, DOWN, buff=0.5)
            
            # 3. 执行动画
            if i == 0:
                # 第一步：显示第一个描述
                self.play(
                    Transform(snowflake, new_snowflake),
                    Transform(level_label, new_label),
                    FadeIn(new_desc, shift=UP)
                )
                prev_desc = new_desc
            else:
                # 后续步骤：变换描述
                self.play(
                    Transform(snowflake, new_snowflake),
                    Transform(level_label, new_label),
                    Transform(prev_desc, new_desc) 
                )
            
            self.wait(0.5)
            
        # 打包需要清理的文字对象
        # 注意：level_label 和 prev_desc 现在是屏幕上显示的最后状态
        text_group_to_clear = VGroup(title, level_label, prev_desc)
            
        return snowflake, text_group_to_clear

    def get_koch_points(self, points):
        """科赫曲线生成算法"""
        new_points = []
        for i in range(len(points) - 1):
            p1 = np.array(points[i])
            p2 = np.array(points[i+1])
            
            # 向量 p1 -> p2
            vector = p2 - p1
            
            # 三等分点
            one_third = p1 + vector / 3
            two_thirds = p1 + vector * 2 / 3
            
            # 突出的三角形顶点 (旋转60度)
            # 旋转矩阵
            rot_matrix = np.array([
                [np.cos(PI/3), -np.sin(PI/3), 0],
                [np.sin(PI/3), np.cos(PI/3), 0],
                [0, 0, 1]
            ])
            peak = one_third + np.dot(rot_matrix, vector / 3)
            
            new_points.extend([p1, one_third, peak, two_thirds])
        
        new_points.append(points[-1])
        return new_points

    def analyze_math(self, snowflake, text_group_to_clear):
        """数学分析：周长与面积 (修复重叠版)"""
        
        RIGHT_ZONE = RIGHT * 3.5
        
        # --- 核心修复步骤 ---
        # 1. 先清理上一阶段的残留文字
        # 2. 同时将雪花变色/变细，作为背景
        self.play(
            FadeOut(text_group_to_clear), 
            snowflake.animate.set_color(INF_GOLD).set_stroke(width=1),
            run_time=1.0
        )
        
        # 1. 周长分析
        p_title = Text("周长 (Perimeter)", font_size=28, color=INF_RED, weight=BOLD)
        p_title.move_to(RIGHT_ZONE + UP * 2.5) # 上移一点，留出空间
        
        p_math = MathTex(
            r"L_n = L_0 \times \left(\frac{4}{3}\right)^n",
            color=WHITE
        ).next_to(p_title, DOWN, buff=0.3)
        
        p_limit = MathTex(
            r"\lim_{n \to \infty} L_n = \infty",
            color=INF_RED, font_size=40
        ).next_to(p_math, DOWN, buff=0.3)
        
        self.play(Write(p_title))
        self.play(Write(p_math))
        self.play(Write(p_limit))
        self.wait(1)
        
        # 2. 面积分析
        a_title = Text("面积 (Area)", font_size=28, color=INF_GREEN, weight=BOLD)
        a_title.next_to(p_limit, DOWN, buff=1.0) # 增加间距
        
        a_math = Text("整个图形被限制在\n一个有限的圆内", font_size=20, color=WHITE).next_to(a_title, DOWN, buff=0.2)
        
        # 画外接圆
        circle = Circle(radius=2.3, color=INF_GREEN, stroke_width=1).move_to(snowflake.get_center())
        
        a_limit = MathTex(
            r"\lim_{n \to \infty} A_n = \text{Finite}",
            color=INF_GREEN, font_size=36
        ).next_to(a_math, DOWN, buff=0.3)
        
        self.play(Create(circle), Write(a_title), Write(a_math))
        self.play(Write(a_limit))
        
        # 3. 悖论结论
        paradox = Text("周长无限，面积有限！", font_size=32, color=INF_GOLD, weight=BOLD).to_edge(DOWN, buff=0.5)
        self.play(Write(paradox))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def explain_fractional_dimension(self):
        """分数维度的解释"""
        title = Text("它是几维物体？", font_size=42, color=INF_PURPLE).to_edge(UP, buff=1.0)
        self.play(Write(title))
        
        # 维度对比布局
        # 1D 线段
        line = Line(LEFT, RIGHT, color=INF_BLUE).shift(LEFT * 4)
        label_1d = Text("1维\n(长度)", font_size=24).next_to(line, DOWN)
        
        # 2D 正方形
        square = Square(side_length=1.5, color=INF_GREEN, fill_opacity=0.5).shift(RIGHT * 4)
        label_2d = Text("2维\n(面积)", font_size=24).next_to(square, DOWN)
        
        # 分形
        # 这里简单画一个 Level 2 的雪花代表分形
        # 重新生成一个小雪花
        points = [[0, 1, 0], [-0.866, -0.5, 0], [0.866, -0.5, 0], [0, 1, 0]]
        points = self.get_koch_points(points) # Level 1
        points = self.get_koch_points(points) # Level 2
        fractal = VMobject(color=INF_GOLD).set_points_as_corners(points).scale(0.8)
        fractal.move_to(ORIGIN)
        label_fd = Text("?", font_size=36, color=INF_GOLD).next_to(fractal, DOWN)
        
        self.play(Create(line), Write(label_1d))
        self.play(Create(square), Write(label_2d))
        self.play(Create(fractal), Write(label_fd))
        
        # 豪斯多夫维数 (Hausdorff Dimension)
        # log(N) / log(S) = log(4) / log(3) ≈ 1.2618
        
        dim_text = MathTex(
            r"D = \frac{\log(4)}{\log(3)} \approx 1.2618",
            color=INF_GOLD, font_size=40
        ).move_to(DOWN * 2.0)
        
        explanation = Text("它比线更复杂，但填不满面", font_size=24, color=INF_GRAY).next_to(dim_text, DOWN, buff=0.3)
        
        self.play(Transform(label_fd, Text("1.26维", font_size=24, color=INF_GOLD).next_to(fractal, DOWN)))
        self.play(Write(dim_text))
        self.play(Write(explanation))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_ending(self):
        # 总结
        summary = VGroup(
            Text("1. 分形具有自相似性 (Self-similarity)", font_size=26),
            Text("2. 现实中的海岸线具有分形特征", font_size=26),
            Text("3. 维度不一定是整数，可以是分数", font_size=26, color=INF_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
        
        # 预告
        next_ep = Text("下期预告：罗素悖论", font_size=40, color=INF_GOLD)
        desc = Text("理发师该不该给自己刮胡子？\n数学大厦的基石崩塌。", font_size=24, color=INF_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)