"""
数字生命系列 - 10集独立视频实现
每集1分钟，可独立发布到抖音/视频号
"""

from manim import *
import numpy as np

# ==================== 第1集：水母的钟形收缩 ====================
class Episode01_JellyfishBell(Scene):
    """第1集：水母的钟形收缩 - 流体力学的数学之美"""
    
    def construct(self):
        self.camera.background_color = "#001133"
        
        # 0-5秒：标题引入
        title = Text("水母的钟形收缩", font="Microsoft YaHei", font_size=42)
        subtitle = Text("流体力学的数学之美", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(BLUE_B, TEAL_C)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=1)
        
        # 5-20秒：钟形函数可视化
        formula = MathTex(
            r"r(\theta,t) = r_0 \cdot (1 + A\sin(\omega t)) \cdot e^{-\frac{\theta^2}{2\sigma^2}}",
            font_size=32
        ).to_edge(UP)
        formula.set_color(TEAL_B)
        
        # 创建动态钟形
        t_tracker = ValueTracker(0)
        
        def create_bell():
            t = t_tracker.get_value()
            points = []
            for theta in np.linspace(0, 2*PI, 100):
                r = 2 * (1 + 0.4*np.sin(t)) * np.exp(-theta**2/4)
                x = r * np.cos(theta)
                y = r * np.sin(theta) - 1
                points.append([x, y, 0])
            
            bell = Polygon(*points, color=BLUE_E, fill_opacity=0.3, stroke_color=TEAL_A)
            return bell
        
        bell_shape = always_redraw(create_bell)
        
        self.play(Write(formula), Create(bell_shape), run_time=3)
        
        # 20-40秒：收缩动画展示
        # 添加参数说明
        param_box = VGroup(
            Text("r₀ = 基础半径", font_size=20),
            Text("A = 收缩幅度", font_size=20),
            Text("ω = 收缩频率", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)
        param_box.set_color(BLUE_B)
        
        self.play(FadeIn(param_box))
        self.play(t_tracker.animate.set_value(4*PI), run_time=10, rate_func=linear)
        
        # 40-55秒：涡环形成
        vortex_text = Text("涡环推进原理", font_size=28).to_edge(DOWN)
        vortex_text.set_color(TEAL_C)
        
        # 创建涡环粒子
        particles = VGroup()
        for i in range(200):
            angle = np.random.uniform(0, 2*PI)
            r = np.random.uniform(1.5, 2.5)
            particle = Dot(
                point=[r*np.cos(angle), r*np.sin(angle)-1, 0],
                radius=0.02,
                color=BLUE_A,
                fill_opacity=0.6
            )
            particles.add(particle)
        
        self.play(
            FadeIn(vortex_text),
            *[Create(p) for p in particles[:50]],
            run_time=3
        )
        
        # 55-60秒：结束总结
        end_text = Text("下集预告：细胞分裂的黄金比例", font_size=24)
        end_text.set_color_by_gradient(BLUE_B, TEAL_B)
        
        self.play(
            FadeOut(VGroup(formula, bell_shape, param_box, particles, vortex_text)),
            FadeIn(end_text),
            run_time=3
        )
        self.wait(2)


# ==================== 第2集：细胞分裂的黄金比例 ====================
class Episode02_CellDivision(Scene):
    """第2集：细胞分裂的黄金比例 - 生命的数学密码"""
    
    def construct(self):
        self.camera.background_color = "#0a0e27"
        
        # 0-5秒：开场
        title = Text("细胞分裂的黄金比例", font="Microsoft YaHei", font_size=42)
        subtitle = Text("斐波那契数列与生命", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(GREEN_A, YELLOW_A)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(title_group.animate.scale(0.5).to_corner(UL), run_time=2)
        
        # 5-25秒：斐波那契数列可视化
        fib_text = MathTex("F_n = F_{n-1} + F_{n-2}", font_size=36).to_edge(UP)
        fib_text.set_color(YELLOW_B)
        
        # 创建细胞分裂动画
        cell = Circle(radius=0.5, color=GREEN_B, fill_opacity=0.5)
        
        self.play(Write(fib_text), Create(cell), run_time=2)
        
        # 分裂序列
        cells = VGroup(cell)
        generations = [1, 1, 2, 3, 5, 8]
        
        for i, count in enumerate(generations[1:], 1):
            new_cells = VGroup()
            for j in range(count - len(cells)):
                new_cell = Circle(radius=0.3/np.sqrt(i), color=GREEN_B, fill_opacity=0.5)
                angle = j * 2*PI / count
                new_cell.move_to([2*np.cos(angle), 2*np.sin(angle), 0])
                new_cells.add(new_cell)
            
            self.play(
                *[Transform(cells[0].copy(), nc) for nc in new_cells],
                run_time=2
            )
            cells.add(*new_cells)
        
        # 25-45秒：黄金角度展示
        golden_angle = 137.5
        golden_text = Text(f"黄金角 = 137.5°", font_size=28).to_edge(DOWN)
        golden_text.set_color(YELLOW_C)
        
        self.play(FadeIn(golden_text))
        
        # 创建螺旋排列
        spiral_dots = VGroup()
        for i in range(50):
            angle = i * golden_angle * DEGREES
            r = 0.1 * np.sqrt(i)
            dot = Dot(
                point=[r*np.cos(angle), r*np.sin(angle), 0],
                radius=0.05,
                color=interpolate_color(GREEN_E, YELLOW_E, i/50)
            )
            spiral_dots.add(dot)
        
        self.play(
            FadeOut(cells),
            *[Create(dot) for dot in spiral_dots],
            run_time=5
        )
        
        # 45-55秒：DNA双螺旋连接
        dna_text = Text("DNA中的黄金比例", font_size=28)
        dna_text.set_color(GREEN_C)
        
        self.play(
            Transform(golden_text, dna_text),
            spiral_dots.animate.rotate(PI/2, axis=UP),
            run_time=3
        )
        
        # 55-60秒：预告
        next_text = Text("下集：鱼群的集体智慧", font_size=24)
        next_text.set_color_by_gradient(BLUE_B, GREEN_B)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第3集：鱼群的集体智慧 ====================
class Episode03_FishSchool(Scene):
    """第3集：鱼群的集体智慧 - Boids算法的魅力"""
    
    def construct(self):
        self.camera.background_color = "#002244"
        
        # 0-5秒：标题
        title = Text("鱼群的集体智慧", font="Microsoft YaHei", font_size=42)
        subtitle = Text("从个体到群体的涌现", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(BLUE_A, TEAL_A)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=2)
        
        # 5-20秒：三大规则展示
        rules = VGroup(
            Text("规则1：分离 - 避免碰撞", font_size=24, color=RED_B),
            Text("规则2：对齐 - 保持方向", font_size=24, color=GREEN_B),
            Text("规则3：凝聚 - 靠近中心", font_size=24, color=BLUE_B)
        ).arrange(DOWN, buff=0.5).to_edge(LEFT)
        
        self.play(Write(rules), run_time=3)
        
        # 创建鱼群模拟
        num_fish = 30
        fish_group = VGroup()
        
        for i in range(num_fish):
            fish = Triangle(color=BLUE_C, fill_opacity=0.7).scale(0.1)
            fish.move_to([
                np.random.uniform(-3, 3),
                np.random.uniform(-2, 2),
                0
            ])
            fish.velocity = np.array([
                np.random.uniform(-1, 1),
                np.random.uniform(-1, 1),
                0
            ])
            fish_group.add(fish)
        
        self.play(*[Create(fish) for fish in fish_group], run_time=2)
        
        # 20-45秒：Boids算法动画
        def update_fish(mob, dt):
            for i, fish in enumerate(mob):
                pos = fish.get_center()
                vel = fish.velocity
                
                # 分离力
                separation = np.zeros(3)
                # 对齐力
                alignment = np.zeros(3)
                # 凝聚力
                cohesion = np.zeros(3)
                
                neighbors = 0
                for j, other in enumerate(mob):
                    if i != j:
                        diff = pos - other.get_center()
                        dist = np.linalg.norm(diff)
                        
                        if dist < 1.0:  # 邻域半径
                            neighbors += 1
                            # 分离
                            if dist < 0.3:
                                separation += diff / (dist + 0.01)
                            # 对齐
                            alignment += other.velocity
                            # 凝聚
                            cohesion += other.get_center()
                
                if neighbors > 0:
                    alignment /= neighbors
                    cohesion = cohesion / neighbors - pos
                    
                    # 合并力
                    vel += 0.1 * separation + 0.05 * alignment + 0.02 * cohesion
                    
                    # 限制速度
                    speed = np.linalg.norm(vel)
                    if speed > 2:
                        vel = vel / speed * 2
                
                # 边界反弹
                if abs(pos[0]) > 4:
                    vel[0] *= -1
                if abs(pos[1]) > 3:
                    vel[1] *= -1
                
                fish.velocity = vel
                fish.shift(vel * dt * 0.1)
                # 旋转朝向速度方向
                if np.linalg.norm(vel[:2]) > 0.01:
                    angle = np.arctan2(vel[1], vel[0])
                    fish.rotate(angle - fish.get_angle(), about_point=pos)
        
        fish_group.add_updater(update_fish)
        self.wait(15)
        fish_group.remove_updater(update_fish)
        
        # 45-55秒：形成图案
        pattern_text = Text("涌现的集体智慧", font_size=32).to_edge(DOWN)
        pattern_text.set_color(TEAL_C)
        
        self.play(FadeIn(pattern_text), run_time=2)
        self.wait(3)
        
        # 55-60秒：预告
        next_text = Text("下集：量子波的干涉之舞", font_size=24)
        next_text.set_color_by_gradient(PURPLE_A, BLUE_A)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第4集：量子波的干涉 ====================
class Episode04_QuantumWaves(Scene):
    """第4集：量子波的干涉之舞 - 概率云的视觉化"""
    
    def construct(self):
        self.camera.background_color = "#000814"
        
        # 0-5秒：开场
        title = Text("量子波的干涉之舞", font="Microsoft YaHei", font_size=42)
        subtitle = Text("双缝实验的数学之美", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(PURPLE_A, PINK)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(title_group.animate.scale(0.5).to_corner(UL), run_time=2)
        
        # 5-25秒：双缝干涉模拟
        formula = MathTex(
            r"\psi = A_1 e^{i(k r_1 - \omega t)} + A_2 e^{i(k r_2 - \omega t)}",
            font_size=28
        ).to_edge(UP)
        formula.set_color(PURPLE_B)
        
        self.play(Write(formula), run_time=2)
        
        # 创建双缝
        slit1 = Line(UP*0.5, DOWN*0.5, color=WHITE).shift(LEFT*2 + UP)
        slit2 = Line(UP*0.5, DOWN*0.5, color=WHITE).shift(LEFT*2 + DOWN)
        slits = VGroup(slit1, slit2)
        
        self.play(Create(slits), run_time=1)
        
        # 创建干涉图案
        t_tracker = ValueTracker(0)
        
        def create_interference():
            t = t_tracker.get_value()
            dots = VGroup()
            
            for x in np.linspace(-3, 3, 50):
                for y in np.linspace(-2, 2, 30):
                    # 计算到两个缝的距离
                    r1 = np.sqrt((x + 2)**2 + (y - 1)**2)
                    r2 = np.sqrt((x + 2)**2 + (y + 1)**2)
                    
                    # 波函数叠加
                    k = 2  # 波数
                    psi1 = np.exp(1j * (k * r1 - t))
                    psi2 = np.exp(1j * (k * r2 - t))
                    
                    # 概率幅
                    prob = np.abs(psi1 + psi2)**2 / 4
                    
                    if prob > 0.5:
                        color = interpolate_color(PURPLE_E, PINK, prob)
                        dot = Dot(
                            point=[x, y, 0],
                            radius=0.02 * prob,
                            color=color,
                            fill_opacity=prob
                        )
                        dots.add(dot)
            
            return dots
        
        interference = always_redraw(create_interference)
        self.add(interference)
        
        self.play(t_tracker.animate.set_value(4*PI), run_time=10, rate_func=linear)
        
        # 25-45秒：概率分布展示
        prob_text = Text("概率密度分布", font_size=28).to_edge(DOWN)
        prob_text.set_color(PURPLE_C)
        
        self.play(FadeIn(prob_text), run_time=2)
        
        # 创建概率分布曲线
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1, 0.2],
            x_length=6,
            y_length=3,
            tips=False
        ).shift(DOWN*0.5)
        
        prob_curve = axes.plot(
            lambda x: (np.cos(2*x)**2 + 1) / 2,
            color=PINK
        )
        
        self.play(Create(axes), Create(prob_curve), run_time=5)
        
        # 45-55秒：量子态叠加
        superposition_text = Text("量子叠加原理", font_size=32)
        superposition_text.set_color(PURPLE_A)
        
        self.play(Transform(prob_text, superposition_text), run_time=3)
        self.wait(2)
        
        # 55-60秒：预告
        next_text = Text("下集：分形龙的飞行轨迹", font_size=24)
        next_text.set_color_by_gradient(ORANGE, RED)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第5集：分形龙的飞行 ====================
class Episode05_FractalDragon(Scene):
    """第5集：分形龙的飞行轨迹 - 混沌中的秩序"""
    
    def construct(self):
        self.camera.background_color = "#1a0033"
        
        # 0-5秒：标题
        title = Text("分形龙的飞行轨迹", font="Microsoft YaHei", font_size=42)
        subtitle = Text("混沌系统的优美曲线", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(ORANGE, RED)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=2)
        
        # 5-30秒：龙曲线生成
        dragon_text = Text("Dragon Curve 分形", font_size=28).to_edge(UP)
        dragon_text.set_color(ORANGE)
        
        self.play(Write(dragon_text), run_time=2)
        
        # 递归生成龙曲线
        def dragon_curve(order, length=4, angle=90):
            if order == 0:
                return Line(ORIGIN, RIGHT*length, color=RED_B)
            
            curve = VGroup()
            sub_curve1 = dragon_curve(order-1, length/np.sqrt(2), angle)
            sub_curve2 = dragon_curve(order-1, length/np.sqrt(2), -angle)
            
            sub_curve1.rotate(angle/2 * DEGREES, about_point=ORIGIN)
            sub_curve2.rotate(-angle/2 * DEGREES, about_point=sub_curve1.get_end())
            sub_curve2.shift(sub_curve1.get_end() - sub_curve2.get_start())
            
            curve.add(sub_curve1, sub_curve2)
            return curve
        
        # 逐级展示
        for order in range(1, 8):
            dragon = dragon_curve(order)
            dragon.center()
            dragon.set_color_by_gradient(ORANGE, RED)
            
            if order == 1:
                self.play(Create(dragon), run_time=2)
            else:
                self.play(Transform(self.mobjects[-1], dragon), run_time=2)
        
        # 30-45秒：添加飞行动画
        fly_text = Text("S形波动飞行", font_size=28).to_edge(DOWN)
        fly_text.set_color(RED_C)
        
        self.play(FadeIn(fly_text), run_time=2)
        
        # 创建飞行路径
        t_tracker = ValueTracker(0)
        
        def create_flight_path():
            t = t_tracker.get_value()
            path = ParametricFunction(
                lambda s: np.array([
                    s - 3,
                    np.sin(s + t) * np.exp(-s/10),
                    0
                ]),
                t_range=[0, 6],
                color=YELLOW
            )
            return path
        
        flight = always_redraw(create_flight_path)
        self.add(flight)
        
        self.play(t_tracker.animate.set_value(2*PI), run_time=5, rate_func=linear)
        
        # 45-55秒：分形维度说明
        dimension_text = MathTex(r"D = \frac{\log 2}{\log \sqrt{2}} = 2", font_size=32)
        dimension_text.set_color(ORANGE)
        dimension_text.to_corner(UR)
        
        self.play(Write(dimension_text), run_time=3)
        self.wait(2)
        
        # 55-60秒：预告
        next_text = Text("下集：心脏跳动的混沌节律", font_size=24)
        next_text.set_color_by_gradient(RED_A, PURPLE_A)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第6集：心脏的混沌节律 ====================
class Episode06_HeartChaos(Scene):
    """第6集：心脏跳动的混沌节律 - 生命的非线性动力学"""
    
    def construct(self):
        self.camera.background_color = "#330011"
        
        # 0-5秒：标题
        title = Text("心脏的混沌节律", font="Microsoft YaHei", font_size=42)
        subtitle = Text("生命的非线性动力学", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(RED_A, PINK)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(title_group.animate.scale(0.5).to_corner(UL), run_time=2)
        
        # 5-25秒：心跳模型
        formula = MathTex(r"\ddot{x} - \mu(1-x^2)\dot{x} + x = 0", font_size=32).to_edge(UP)
        formula.set_color(RED_B)
        formula_name = Text("Van der Pol 振荡器", font_size=20).next_to(formula, DOWN)
        formula_name.set_color(PINK)
        
        self.play(Write(formula), FadeIn(formula_name), run_time=3)
        
        # 创建心电图
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            tips=False
        ).shift(DOWN)
        
        # 心电图曲线
        t_tracker = ValueTracker(0)
        
        def heartbeat(t):
            # 简化的心电图波形
            qrs = 1.5 * np.exp(-((t % 1 - 0.5) * 20)**2)  # QRS波
            p_wave = 0.2 * np.exp(-((t % 1 - 0.2) * 10)**2)  # P波
            t_wave = 0.3 * np.exp(-((t % 1 - 0.7) * 8)**2)  # T波
            return qrs + p_wave + t_wave - 0.2
        
        ecg_curve = always_redraw(
            lambda: axes.plot(
                lambda x: heartbeat(x + t_tracker.get_value()),
                x_range=[0, 10],
                color=RED_C
            )
        )
        
        self.play(Create(axes), Create(ecg_curve), run_time=3)
        self.play(t_tracker.animate.set_value(5), run_time=10, rate_func=linear)
        
        # 25-45秒：相空间轨迹
        phase_text = Text("相空间轨迹", font_size=28).to_edge(DOWN)
        phase_text.set_color(RED_D)
        
        self.play(FadeIn(phase_text), run_time=2)
        
        # 创建极限环
        phase_axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            tips=False
        ).shift(RIGHT*2)
        
        limit_cycle = ParametricFunction(
            lambda t: np.array([
                2 * np.cos(t),
                2 * np.sin(t) * (1 + 0.2 * np.sin(3*t)),
                0
            ]),
            t_range=[0, 2*PI],
            color=PINK
        ).move_to(phase_axes.get_center())
        
        self.play(Create(phase_axes), Create(limit_cycle), run_time=5)
        
        # 45-55秒：混沌过渡
        chaos_text = Text("健康与异常的边界", font_size=32)
        chaos_text.set_color(RED_A)
        
        self.play(Transform(phase_text, chaos_text), run_time=3)
        self.wait(2)
        
        # 55-60秒：预告
        next_text = Text("下集：DNA的双螺旋密码", font_size=24)
        next_text.set_color_by_gradient(GREEN_A, BLUE_A)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第7集：DNA双螺旋 ====================
class Episode07_DNAHelix(Scene):
    """第7集：DNA的双螺旋密码 - 生命信息的数学结构"""
    
    def construct(self):
        self.camera.background_color = "#001122"
        
        # 0-5秒：标题
        title = Text("DNA的双螺旋密码", font="Microsoft YaHei", font_size=42)
        subtitle = Text("生命信息的数学结构", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(GREEN_A, BLUE_A)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=2)
        
        # 5-30秒：双螺旋结构
        helix_formula = MathTex(
            r"x = r\cos(\theta), \quad y = r\sin(\theta), \quad z = \frac{h\theta}{2\pi}",
            font_size=28
        ).to_edge(UP)
        helix_formula.set_color(GREEN_B)
        
        self.play(Write(helix_formula), run_time=2)
        
        # 创建双螺旋
        def create_helix(phase_shift=0):
            helix = ParametricFunction(
                lambda t: np.array([
                    1.5 * np.cos(t + phase_shift),
                    t / 2 - 3,
                    1.5 * np.sin(t + phase_shift)
                ]),
                t_range=[0, 4*PI],
                color=GREEN_C if phase_shift == 0 else BLUE_C
            )
            return helix
        
        helix1 = create_helix(0)
        helix2 = create_helix(PI)
        
        self.play(Create(helix1), Create(helix2), run_time=5)
        
        # 添加碱基对
        base_pairs = VGroup()
        for i in range(10):
            t = i * PI / 2.5
            point1 = np.array([1.5 * np.cos(t), t/2 - 3, 1.5 * np.sin(t)])
            point2 = np.array([1.5 * np.cos(t + PI), t/2 - 3, 1.5 * np.sin(t + PI)])
            
            line = Line(point1, point2, color=YELLOW_C, stroke_width=2)
            base_pairs.add(line)
        
        self.play(*[Create(line) for line in base_pairs], run_time=5)
        
        # 30-45秒：碱基配对规则
        base_text = VGroup(
            Text("A - T", color=RED_C),
            Text("G - C", color=BLUE_C)
        ).arrange(RIGHT, buff=1).to_edge(DOWN)
        
        self.play(Write(base_text), run_time=3)
        
        # 旋转展示
        dna_group = VGroup(helix1, helix2, base_pairs)
        self.play(Rotate(dna_group, angle=2*PI, axis=UP), run_time=8)
        
        # 45-55秒：信息编码
        info_text = Text("3.2亿个碱基对 = 生命密码", font_size=28)
        info_text.set_color(GREEN_C)
        
        self.play(FadeIn(info_text.to_edge(DOWN)), run_time=3)
        self.wait(2)
        
        # 55-60秒：预告
        next_text = Text("下集：神经网络的电光传导", font_size=24)
        next_text.set_color_by_gradient(PURPLE_A, YELLOW_A)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第8集：神经网络 ====================
class Episode08_NeuralNetwork(Scene):
    """第8集：神经网络的电光传导 - 思维的数学模型"""
    
    def construct(self):
        self.camera.background_color = "#0a0a1a"
        
        # 0-5秒：标题
        title = Text("神经网络的电光传导", font="Microsoft YaHei", font_size=42)
        subtitle = Text("思维的数学模型", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(PURPLE_A, YELLOW_A)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=2)
        
        # 5-25秒：神经元模型
        neuron_formula = MathTex(
            r"y = \sigma(\sum_{i} w_i x_i + b)",
            font_size=32
        ).to_edge(UP)
        neuron_formula.set_color(PURPLE_B)
        
        self.play(Write(neuron_formula), run_time=2)
        
        # 创建神经元
        neuron = Circle(radius=0.5, color=PURPLE_C, fill_opacity=0.5)
        
        # 输入树突
        inputs = VGroup()
        for i in range(5):
            angle = (i - 2) * PI / 6
            start = neuron.get_center() + LEFT * 2 + UP * np.sin(angle)
            end = neuron.get_left()
            
            dendrite = Line(start, end, color=BLUE_C)
            input_dot = Dot(start, color=BLUE_B)
            inputs.add(dendrite, input_dot)
        
        # 输出轴突
        axon = Line(neuron.get_right(), neuron.get_right() + RIGHT * 2, color=YELLOW_C)
        output_dot = Dot(axon.get_end(), color=YELLOW_B)
        
        self.play(
            Create(neuron),
            *[Create(obj) for obj in inputs],
            Create(axon),
            Create(output_dot),
            run_time=5
        )
        
        # 信号传播动画
        for _ in range(3):
            signals = VGroup()
            for i in range(5):
                signal = Dot(color=WHITE, radius=0.05)
                signal.move_to(inputs[i*2 + 1].get_center())
                signals.add(signal)
            
            self.play(
                *[signal.animate.move_to(neuron.get_center()) for signal in signals],
                run_time=1
            )
            
            # 激发
            self.play(
                neuron.animate.set_color(YELLOW_C),
                run_time=0.2
            )
            
            output_signal = Dot(color=YELLOW, radius=0.05)
            output_signal.move_to(neuron.get_center())
            
            self.play(
                output_signal.animate.move_to(output_dot.get_center()),
                neuron.animate.set_color(PURPLE_C),
                run_time=1
            )
            
            self.remove(output_signal, *signals)
        
        # 25-45秒：网络结构
        network_text = Text("深度网络结构", font_size=28).to_edge(DOWN)
        network_text.set_color(PURPLE_C)
        
        self.play(FadeIn(network_text), run_time=2)
        
        # 创建多层网络
        self.clear()
        self.add(neuron_formula, network_text)
        
        layers = []
        layer_sizes = [3, 5, 4, 2]
        
        for l, size in enumerate(layer_sizes):
            layer = VGroup()
            for i in range(size):
                y_pos = (i - size/2) * 0.8
                x_pos = (l - len(layer_sizes)/2) * 2
                
                n = Circle(radius=0.2, color=PURPLE_C, fill_opacity=0.5)
                n.move_to([x_pos, y_pos, 0])
                layer.add(n)
            layers.append(layer)
        
        # 连接
        connections = VGroup()
        for l in range(len(layers) - 1):
            for n1 in layers[l]:
                for n2 in layers[l + 1]:
                    line = Line(
                        n1.get_center(),
                        n2.get_center(),
                        color=BLUE_C,
                        stroke_opacity=0.3
                    )
                    connections.add(line)
        
        self.play(
            *[Create(layer) for layer in layers],
            Create(connections),
            run_time=5
        )
        
        # 前向传播动画
        for _ in range(2):
            for l in range(len(layers)):
                self.play(
                    *[Flash(n, color=YELLOW_C) for n in layers[l]],
                    run_time=0.5
                )
        
        # 45-55秒：学习过程
        learning_text = Text("反向传播学习", font_size=32)
        learning_text.set_color(YELLOW_C)
        
        self.play(Transform(network_text, learning_text), run_time=3)
        self.wait(2)
        
        # 55-60秒：预告
        next_text = Text("下集：植物生长的L-系统", font_size=24)
        next_text.set_color_by_gradient(GREEN_A, YELLOW_A)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第9集：植物L-系统 ====================
class Episode09_LSystem(Scene):
    """第9集：植物生长的L-系统 - 递归之美"""
    
    def construct(self):
        self.camera.background_color = "#0a2a0a"
        
        # 0-5秒：标题
        title = Text("植物生长的L-系统", font="Microsoft YaHei", font_size=42)
        subtitle = Text("递归规则创造生命", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(GREEN_A, YELLOW_A)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=2)
        
        # 5-25秒：L-系统规则
        rule_text = Text("规则: F → F[+F]F[-F]F", font_size=32).to_edge(UP)
        rule_text.set_color(GREEN_B)
        
        self.play(Write(rule_text), run_time=2)
        
        # L-系统实现
        def l_system_generate(axiom, rules, iterations):
            current = axiom
            for _ in range(iterations):
                next_str = ""
                for char in current:
                    next_str += rules.get(char, char)
                current = next_str
            return current
        
        def draw_l_system(instructions, angle=25, length=0.5):
            path = VGroup()
            stack = []
            current_pos = np.array([0, -3, 0])
            current_angle = 90 * DEGREES
            
            for cmd in instructions:
                if cmd == 'F':
                    new_pos = current_pos + length * np.array([
                        np.cos(current_angle),
                        np.sin(current_angle),
                        0
                    ])
                    line = Line(current_pos, new_pos, color=GREEN_C)
                    path.add(line)
                    current_pos = new_pos
                elif cmd == '+':
                    current_angle += angle * DEGREES
                elif cmd == '-':
                    current_angle -= angle * DEGREES
                elif cmd == '[':
                    stack.append((current_pos.copy(), current_angle))
                elif cmd == ']':
                    current_pos, current_angle = stack.pop()
            
            return path
        
        # 逐代生长
        rules = {'F': 'F[+F]F[-F]F'}
        
        for iteration in range(1, 5):
            instructions = l_system_generate('F', rules, iteration)
            tree = draw_l_system(instructions, angle=25, length=3/(2**iteration))
            tree.center()
            
            generation_text = Text(f"第{iteration}代", font_size=20).to_corner(UR)
            generation_text.set_color(YELLOW_C)
            
            if iteration == 1:
                self.play(Create(tree), FadeIn(generation_text), run_time=3)
            else:
                self.play(
                    Transform(self.mobjects[-2], tree),
                    Transform(self.mobjects[-1], generation_text),
                    run_time=3
                )
        
        # 25-45秒：添加叶子和花
        leaf_text = Text("添加细节：叶子与花朵", font_size=28).to_edge(DOWN)
        leaf_text.set_color(GREEN_C)
        
        self.play(FadeIn(leaf_text), run_time=2)
        
        # 在末端添加叶子
        leaves = VGroup()
        for line in self.mobjects[-2]:
            if isinstance(line, Line) and np.random.random() > 0.7:
                leaf = Dot(line.get_end(), color=GREEN_B, radius=0.05)
                leaves.add(leaf)
        
        flowers = VGroup()
        for line in self.mobjects[-2]:
            if isinstance(line, Line) and np.random.random() > 0.9:
                flower = Dot(line.get_end(), color=PINK, radius=0.08)
                flowers.add(flower)
        
        self.play(
            *[GrowFromCenter(leaf) for leaf in leaves],
            run_time=3
        )
        self.play(
            *[GrowFromCenter(flower) for flower in flowers],
            run_time=2
        )
        
        # 45-55秒：分形维度
        fractal_text = MathTex(r"D_{fractal} = 1.58", font_size=32)
        fractal_text.set_color(YELLOW_B)
        fractal_text.to_corner(UL)
        
        self.play(Write(fractal_text), run_time=3)
        self.wait(2)
        
        # 55-60秒：预告
        next_text = Text("终章：生命游戏的涌现", font_size=24)
        next_text.set_color_by_gradient(WHITE, GRAY)
        
        self.play(FadeOut(VGroup(*self.mobjects)), FadeIn(next_text), run_time=3)
        self.wait(2)


# ==================== 第10集：生命游戏 ====================
class Episode10_GameOfLife(Scene):
    """第10集：生命游戏的涌现 - 简单规则的复杂世界"""
    
    def construct(self):
        self.camera.background_color = "#111111"
        
        # 0-5秒：标题
        title = Text("生命游戏的涌现", font="Microsoft YaHei", font_size=42)
        subtitle = Text("Conway's Game of Life", font="Microsoft YaHei", font_size=24)
        subtitle.next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        title_group.set_color_by_gradient(WHITE, GRAY)
        
        self.play(Write(title_group), run_time=2)
        self.wait(1)
        self.play(FadeOut(title_group), run_time=2)
        
        # 5-20秒：规则说明
        rules = VGroup(
            Text("规则1: 活细胞周围有2-3个邻居时存活", font_size=20),
            Text("规则2: 死细胞周围有3个邻居时复活", font_size=20),
            Text("规则3: 其他情况细胞死亡", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)
        rules.set_color(GRAY_B)
        
        self.play(Write(rules), run_time=3)
        
        # 创建网格
        grid_size = 15
        cell_size = 0.3
        grid = VGroup()
        cells = {}
        
        for i in range(grid_size):
            for j in range(grid_size):
                rect = Square(side_length=cell_size)
                rect.move_to([
                    (i - grid_size/2) * cell_size,
                    (j - grid_size/2) * cell_size,
                    0
                ])
                rect.set_fill(BLACK, opacity=1)
                rect.set_stroke(GRAY_C, width=1)
                grid.add(rect)
                cells[(i, j)] = rect
        
        grid.shift(RIGHT * 2)
        self.play(Create(grid), run_time=2)
        
        # 初始化滑翔机模式
        glider = [(7, 7), (8, 7), (9, 7), (9, 8), (8, 9)]
        for pos in glider:
            cells[pos].set_fill(WHITE, opacity=1)
        
        self.play(*[cells[pos].animate.set_fill(WHITE, opacity=1) for pos in glider])
        
        # 20-45秒：演化过程
        def get_neighbors(i, j):
            neighbors = []
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < grid_size and 0 <= nj < grid_size:
                        neighbors.append((ni, nj))
            return neighbors
        
        def evolve():
            alive = set()
            for i in range(grid_size):
                for j in range(grid_size):
                    if cells[(i, j)].fill_color == WHITE:
                        alive.add((i, j))
            
            new_alive = set()
            for i in range(grid_size):
                for j in range(grid_size):
                    neighbors = get_neighbors(i, j)
                    alive_neighbors = sum(1 for n in neighbors if n in alive)
                    
                    if (i, j) in alive:
                        if alive_neighbors in [2, 3]:
                            new_alive.add((i, j))
                    else:
                        if alive_neighbors == 3:
                            new_alive.add((i, j))
            
            animations = []
            for i in range(grid_size):
                for j in range(grid_size):
                    if (i, j) in new_alive:
                        if cells[(i, j)].fill_color != WHITE:
                            animations.append(cells[(i, j)].animate.set_fill(WHITE, opacity=1))
                    else:
                        if cells[(i, j)].fill_color == WHITE:
                            animations.append(cells[(i, j)].animate.set_fill(BLACK, opacity=1))
            
            return animations
        
        # 运行多代
        for generation in range(15):
            gen_text = Text(f"第{generation + 1}代", font_size=20).to_corner(UR)
            gen_text.set_color(GRAY_B)
            
            if generation == 0:
                self.play(FadeIn(gen_text), run_time=0.5)
            else:
                self.play(Transform(self.mobjects[-1], gen_text), run_time=0.5)
            
            animations = evolve()
            if animations:
                self.play(*animations, run_time=0.5)
        
        # 45-55秒：涌现的复杂性
        emerge_text = Text("从简单规则到复杂行为", font_size=32).to_edge(DOWN)
        emerge_text.set_color(WHITE)
        
        self.play(FadeIn(emerge_text), run_time=3)
        self.wait(2)
        
        # 55-60秒：系列结语
        end_text = VGroup(
            Text("数字生命系列", font_size=36),
            Text("完", font_size=48)
        ).arrange(DOWN)
        end_text.set_color_by_gradient(BLUE_A, PURPLE_A, ORANGE)
        
        self.play(
            FadeOut(VGroup(*self.mobjects)),
            FadeIn(end_text),
            run_time=3
        )
        self.wait(2)