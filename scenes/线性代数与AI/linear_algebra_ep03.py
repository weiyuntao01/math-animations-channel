from manim import *
import numpy as np

# --- 配色方案 (更具深度的配色) ---
LA_TEAL = "#2DD4BF"      # 主成分 / 本质
LA_PINK = "#F472B6"      # 噪音 / 干扰
LA_YELLOW = "#FACC15"    # 智慧 / 洞察
LA_PURPLE = "#A855F7"    # 高维空间
LA_GRAY = "#475569"      # 背景数据
BG_COLOR = "#0F172A"     # 深邃背景

class LinearAlgebraEP03(ThreeDScene):
    """线性代数 EP03：降维打击 (PCA) - 哲学版"""
    
    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 哲学开场：柏拉图的洞穴
        self.intro_philosophy()
        
        # 2. 3D 困境：混乱的高维世界
        # 返回 points_3d 用于后续
        points_3d, axes = self.show_high_dim_chaos()
        
        # 3. 寻找主成分：最佳视角的旋转
        self.find_principal_component(points_3d, axes)
        
        # 4. 数学原理：投影与损失
        self.explain_projection_loss()
        
        # 5. 升华结尾：少即是多
        self.show_deep_ending()

    def intro_philosophy(self):
        """开场：从哲学引入"""
        # 也不用 to_edge(UP)，用相对位置
        quote = Text("“我们可以为了解构而简化，\n但不能为了简化而撒谎。”", font_size=32, color=LA_YELLOW, slant=ITALIC)
        quote.move_to(UP * 0.5)
        
        author = Text("—— 索尔·贝娄", font_size=24, color=LA_GRAY).next_to(quote, DOWN, buff=0.5)
        
        self.play(Write(quote), FadeIn(author))
        self.wait(3)
        self.play(FadeOut(quote), FadeOut(author))
        
        # 引入主题
        title = Text("EP03: 降维打击 (PCA)", font_size=48, color=LA_TEAL, weight=BOLD)
        subtitle = Text("在复杂世界中抓住主线", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    def show_high_dim_chaos(self):
        """展示3D数据的混乱 (模拟人生的繁杂)"""
        
        # 切换到 3D 视角
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        axes = ThreeDAxes(
            x_range=[-4, 4], y_range=[-4, 4], z_range=[-4, 4],
            x_length=6, y_length=6, z_length=6
        )
        
        # 生成一个呈现椭球状分布的随机点云 (主要沿 x=y 方向分布)
        # 寓意：虽然看起来乱，但其实有一条隐含的主线
        points = VGroup()
        data_coords = []
        
        np.random.seed(42)
        for _ in range(50):
            # 主轴方向 (1, 1, 0.5)
            t = np.random.normal(0, 1.5)
            x = t + np.random.normal(0, 0.5)
            y = t + np.random.normal(0, 0.5)
            z = 0.5 * t + np.random.normal(0, 0.5)
            
            p = Dot3D(point=[x, y, z], radius=0.08, color=LA_GRAY)
            points.add(p)
            data_coords.append([x, y, z])
            
        # 标签 (固定在屏幕上，不随相机旋转)
        label = Text("我们的生活：\n充满了各种繁杂的数据", font_size=24, color=WHITE)
        self.add_fixed_in_frame_mobjects(label)
        label.to_corner(UL)
        
        self.play(Create(axes), FadeIn(points))
        self.play(Write(label))
        
        # 旋转相机展示混乱
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        self.play(FadeOut(label))
        
        return points, axes

    def find_principal_component(self, points, axes):
        """寻找主成分"""
        
        # 旁白文字
        text1 = Text("不仅要看清它，还要简化它", font_size=24, color=LA_YELLOW)
        self.add_fixed_in_frame_mobjects(text1)
        text1.to_corner(UL)
        self.play(Write(text1))
        
        # 画出第一主成分 (PC1) 的轴线
        # 这就是那根“定海神针”
        pc1_vector = np.array([1, 1, 0.5])
        pc1_vector = pc1_vector / np.linalg.norm(pc1_vector) * 5 # 归一化并拉长
        
        line = Line3D(start=-pc1_vector, end=pc1_vector, color=LA_TEAL, thickness=0.02)
        
        self.play(Create(line))
        
        text2 = Text("找到变异最大的方向 (PC1)", font_size=24, color=LA_TEAL)
        self.add_fixed_in_frame_mobjects(text2)
        text2.next_to(text1, DOWN, aligned_edge=LEFT)
        self.play(Write(text2))
        
        # 旋转相机到垂直于该线的角度，展示投影效果
        # 这一步是为了让观众看到，如果我们沿着这个方向看，数据分布最广
        self.move_camera(phi=60*DEGREES, theta=45*DEGREES, run_time=2)
        self.wait(1)
        
        # 投影动画：所有点移动到线上
        projected_points = VGroup()
        projection_lines = VGroup()
        
        # 这是一个单位向量
        u = np.array([1, 1, 0.5])
        u = u / np.linalg.norm(u)
        
        for p in points:
            coords = p.get_center()
            # 投影公式: p_proj = (p . u) * u
            proj_coords = np.dot(coords, u) * u
            
            proj_dot = Dot3D(point=proj_coords, radius=0.08, color=LA_TEAL)
            proj_line = Line(start=coords, end=proj_coords, color=LA_PINK, stroke_opacity=0.5)
            
            projected_points.add(proj_dot)
            projection_lines.add(proj_line)
            
        self.play(Create(projection_lines), run_time=1.5)
        self.play(Transform(points, projected_points), run_time=1.5)
        
        text3 = Text("忽略噪音，保留本质", font_size=24, color=LA_PINK)
        self.add_fixed_in_frame_mobjects(text3)
        text3.next_to(text2, DOWN, aligned_edge=LEFT)
        self.play(Write(text3))
        
        self.wait(2)
        
        # 清理 3D 场景，切回 2D 解释原理
        self.play(
            FadeOut(points), FadeOut(axes), FadeOut(line), 
            FadeOut(projection_lines),
            FadeOut(text1), FadeOut(text2), FadeOut(text3)
        )
        self.set_camera_orientation(phi=0, theta=-90*DEGREES) # 恢复 2D 视角

    def explain_projection_loss(self):
        """数学解释：二维平面的投影与损失"""
        
        # 布局
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 1. 左侧：2D 示意图
        axes_2d = Axes(x_range=[-4,4], y_range=[-3,3], x_length=6, y_length=5).move_to(LEFT_ZONE)
        
        # 模拟数据点 (2D)
        dots_2d = VGroup()
        # y = 0.5x + noise
        for _ in range(10):
            x = np.random.uniform(-3, 3)
            y = 0.5 * x + np.random.normal(0, 0.5)
            dots_2d.add(Dot(axes_2d.c2p(x,y), color=LA_GRAY))
            
        self.play(Create(axes_2d), FadeIn(dots_2d))
        
        # 2. 右侧：核心逻辑
        title = Text("如何选择最好的视角？", font_size=32, color=LA_PURPLE).move_to(RIGHT_ZONE + UP*2)
        self.play(Write(title))
        
        # 两个标准
        concept_1 = VGroup(
            Text("标准一：方差最大化", font_size=24, color=LA_TEAL, weight=BOLD),
            Text("保留最多的信息量", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        concept_2 = VGroup(
            Text("标准二：误差最小化", font_size=24, color=LA_PINK, weight=BOLD),
            Text("丢失最少的细节", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        concepts = VGroup(concept_1, concept_2).arrange(DOWN, buff=0.8).next_to(title, DOWN, buff=0.5)
        self.play(Write(concepts))
        
        # 3. 左侧动画配合：旋转直线寻找最佳投影
        # 初始线 (垂直于主轴，效果很差)
        line = Line(axes_2d.c2p(-3, 6), axes_2d.c2p(3, -6), color=LA_PINK) # 斜率 -2
        self.play(Create(line))
        
        label_bad = Text("糟糕的投影", font_size=20, color=LA_PINK).next_to(line, UP)
        self.play(Write(label_bad))
        self.wait(0.5)
        
        # 旋转到最佳位置 (斜率 0.5)
        best_line = Line(axes_2d.c2p(-4, -2), axes_2d.c2p(4, 2), color=LA_TEAL)
        label_good = Text("最佳投影 (PC1)", font_size=20, color=LA_TEAL).next_to(best_line, UP)
        
        self.play(
            Transform(line, best_line),
            Transform(label_bad, label_good),
            run_time=2
        )
        
        # 强调数学本质
        math_text = Text("这其实是同一个硬币的两面", font_size=24, color=LA_YELLOW)
        math_text.move_to(RIGHT_ZONE + DOWN * 1.5)
        self.play(Write(math_text))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_deep_ending(self):
        """升华结尾"""
        
        # 1. 标题
        title = Text("PCA 的人生哲学", font_size=40, color=LA_PURPLE).to_edge(UP, buff=1.5)
        
        # 2. 哲学金句 (逐行显示)
        lines = VGroup(
            Text("生活是高维的，精力是有限的", font_size=28),
            Text("我们无法抓住所有细节", font_size=28),
            Text("学会降维，就是学会舍弃", font_size=32, color=LA_PINK, weight=BOLD),
            Text("找到你生命中的\"主成分\"", font_size=32, color=LA_TEAL, weight=BOLD)
        ).arrange(DOWN, buff=0.6)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.5)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 3. 预告
        next_ep = Text("下期预告：奇异值分解 (SVD)", font_size=40, color=LA_YELLOW).move_to(UP * 0.5)
        desc = Text("万物皆可拆解。\n图片的压缩与信息的原子化。", font_size=24, color=LA_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))
