from manim import *
import numpy as np

class NautilusSpiralEP3(Scene):
    """鹦鹉螺中的等角螺线 - 黄金分割系列 EP03"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：鹦鹉螺的美
        self.show_nautilus_beauty()
        
        # 第二部分：等角螺线介绍
        self.introduce_logarithmic_spiral()
        
        # 第三部分：数学原理
        self.show_mathematical_principle()
        
        # 第四部分：黄金螺线
        self.show_golden_spiral()
        
        # 第五部分：自然界中的螺线
        self.show_spirals_in_nature()
        
        # 结尾
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第三集：鹦鹉螺中的等角螺线", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_nautilus_beauty(self):
        """展示鹦鹉螺的美 - 0:10-0:40"""
        # 标题
        title = Text("鹦鹉螺的完美螺旋", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建鹦鹉螺轮廓
        nautilus = self.create_nautilus_shell()
        self.play(Create(nautilus), run_time=3)
        
        # 添加说明文字
        description = VGroup(
            Text("5亿年的进化杰作", font_size=28, color=WHITE),
            Text("自然界最优美的曲线", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.3).to_edge(DOWN)
        
        self.play(Write(description[0]))
        self.wait(1)
        self.play(Write(description[1]))
        self.wait(2)
        
        # 高亮螺旋线
        spiral_highlight = self.create_logarithmic_spiral(
            a=0.3, b=0.15, 
            t_max=4*PI,
            color=YELLOW,
            stroke_width=4
        )
        self.play(Create(spiral_highlight), run_time=2)
        self.wait(2)
        
        self.play(
            FadeOut(title),
            FadeOut(nautilus),
            FadeOut(spiral_highlight),
            FadeOut(description)
        )
    
    def create_nautilus_shell(self):
        """创建鹦鹉螺外壳"""
        # 创建螺旋腔室
        chambers = VGroup()
        
        # 参数
        a = 0.3
        b = 0.15
        phi = (1 + np.sqrt(5)) / 2
        
        # 创建多个腔室
        for i in range(8):
            # 计算腔室的角度范围
            theta_start = i * PI / 2
            theta_end = (i + 1) * PI / 2
            
            # 创建腔室轮廓
            chamber = self.create_chamber(
                a, b, theta_start, theta_end,
                color=BLUE_E if i % 2 == 0 else BLUE_D,
                fill_opacity=0.3
            )
            chambers.add(chamber)
        
        return chambers
    
    def create_chamber(self, a, b, theta_start, theta_end, color=BLUE, fill_opacity=0.3):
        """创建单个腔室"""
        # 创建腔室的点
        n_points = 50
        theta_values = np.linspace(theta_start, theta_end, n_points)
        
        # 外螺线点
        outer_points = []
        for theta in theta_values:
            r = a * np.exp(b * theta)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            outer_points.append([x, y, 0])
        
        # 内螺线点（缩小版）
        inner_points = []
        scale_factor = np.exp(-b * PI / 2)  # 缩小因子
        for theta in reversed(theta_values):
            r = a * np.exp(b * theta) * scale_factor
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            inner_points.append([x, y, 0])
        
        # 组合成闭合路径
        all_points = outer_points + inner_points
        
        # 创建多边形
        chamber = Polygon(
            *all_points,
            color=color,
            fill_opacity=fill_opacity,
            stroke_width=2
        )
        
        return chamber
    
    def introduce_logarithmic_spiral(self):
        """介绍等角螺线 - 0:40-1:20"""
        title = Text("等角螺线（对数螺线）", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 数学定义
        formula = MathTex(
            r"r = ae^{b\theta}",
            font_size=48,
            color=WHITE
        ).shift(UP*2)
        
        # 参数说明
        params = VGroup(
            Text("r: 到中心的距离", font_size=24),
            Text("θ: 旋转角度", font_size=24),
            Text("a: 初始半径", font_size=24),
            Text("b: 增长率", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        params.next_to(formula, DOWN, buff=0.8)
        
        self.play(Write(formula))
        self.wait(1)
        
        for param in params:
            self.play(Write(param), run_time=0.6)
        
        self.wait(2)
        
        # 展示不同参数的螺线
        self.play(FadeOut(params))
        
        # 创建多条螺线展示参数影响
        spirals = VGroup()
        b_values = [0.1, 0.15, 0.2, 0.25]
        colors = [BLUE, GREEN, ORANGE, RED]
        
        for b_val, color in zip(b_values, colors):
            spiral = self.create_logarithmic_spiral(
                a=0.2, b=b_val,
                t_max=3*PI,
                color=color,
                stroke_width=2
            )
            spirals.add(spiral)
            
            # 添加标签
            label = MathTex(f"b = {b_val}", font_size=20, color=color)
            label.next_to(spiral.get_end(), RIGHT, buff=0.1)
            spirals.add(label)
        
        spirals.shift(DOWN)
        
        self.play(
            *[Create(spiral) for spiral in spirals],
            run_time=3
        )
        
        explanation = Text(
            "b值越大，螺旋增长越快",
            font_size=24,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(3)
        
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(spirals),
            FadeOut(explanation)
        )
    
    def create_logarithmic_spiral(self, a=0.3, b=0.15, t_min=0, t_max=4*PI, 
                                 color=BLUE, stroke_width=3):
        """创建对数螺线"""
        spiral = ParametricFunction(
            lambda t: np.array([
                a * np.exp(b * t) * np.cos(t),
                a * np.exp(b * t) * np.sin(t),
                0
            ]),
            t_range=[t_min, t_max],
            color=color,
            stroke_width=stroke_width
        )
        return spiral
    
    def show_mathematical_principle(self):
        """展示数学原理 - 1:20-2:20"""
        title = Text("等角螺线的独特性质", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建螺线
        spiral = self.create_logarithmic_spiral(
            a=0.5, b=0.1,
            t_max=3*PI,
            color=BLUE
        )
        spiral.shift(LEFT*3)
        self.play(Create(spiral))
        
        # 展示等角性质
        center = spiral.get_start()
        
        # 创建多条径向线
        angles = [PI/4, PI/2, 3*PI/4, PI, 5*PI/4]
        radial_lines = VGroup()
        intersection_points = []
        
        for angle in angles:
            # 计算与螺线的交点
            t = angle  # 对于等角螺线，t就是角度
            r = 0.5 * np.exp(0.1 * t)
            point = center + r * np.array([np.cos(t), np.sin(t), 0])
            intersection_points.append(point)
            
            # 创建径向线
            line = Line(center, point, color=YELLOW, stroke_width=2)
            radial_lines.add(line)
        
        self.play(*[Create(line) for line in radial_lines])
        
        # 显示切线
        tangent_lines = VGroup()
        angles_text = VGroup()
        
        for i, (point, angle) in enumerate(zip(intersection_points, angles)):
            # 计算切线方向
            # 对于r = ae^(bθ)，切线与径向的夹角是恒定的
            tangent_angle = angle + np.arctan(1/0.1)  # arctan(1/b)
            
            # 创建切线
            tangent_end = point + 0.8 * np.array([
                np.cos(tangent_angle),
                np.sin(tangent_angle),
                0
            ])
            tangent_start = point - 0.3 * np.array([
                np.cos(tangent_angle),
                np.sin(tangent_angle),
                0
            ])
            
            tangent = Line(
                tangent_start,
                tangent_end,
                color=GREEN,
                stroke_width=2
            )
            tangent_lines.add(tangent)
            
            # 标记角度
            arc = Arc(
                radius=0.3,
                start_angle=angle,
                angle=np.arctan(1/0.1),
                arc_center=point,
                color=RED
            )
            tangent_lines.add(arc)
        
        self.play(*[Create(obj) for obj in tangent_lines])
        
        # 说明文字
        property_text = VGroup(
            Text("等角螺线的特性：", font_size=28, color=WHITE),
            Text("切线与径向线的夹角", font_size=24, color=WHITE),
            Text("处处相等！", font_size=32, color=YELLOW)
        ).arrange(DOWN, buff=0.3)
        property_text.shift(RIGHT*2.5)
        
        angle_formula = MathTex(
            r"\alpha = \arctan\left(\frac{1}{b}\right)",
            font_size=32,
            color=GREEN
        )
        angle_formula.next_to(property_text, DOWN, buff=0.5)
        
        self.play(Write(property_text))
        self.wait(1)
        self.play(Write(angle_formula))
        self.wait(3)
        
        self.play(
            FadeOut(title),
            FadeOut(spiral),
            FadeOut(radial_lines),
            FadeOut(tangent_lines),
            FadeOut(property_text),
            FadeOut(angle_formula)
        )
    
    def show_golden_spiral(self):
        """展示黄金螺线 - 2:20-3:00"""
        title = Text("黄金螺线", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 黄金比例
        phi = (1 + np.sqrt(5)) / 2
        
        # 创建斐波那契矩形
        fib_rects = self.create_fibonacci_rectangles()
        self.play(Create(fib_rects), run_time=2)
        
        # 创建黄金螺线
        # 对于黄金螺线，b = ln(φ) / (π/2)
        b_golden = np.log(phi) / (PI/2)
        
        golden_spiral = self.create_logarithmic_spiral(
            a=0.5,
            b=b_golden,
            t_max=2*PI,
            color=GOLD,
            stroke_width=4
        )
        golden_spiral.shift(LEFT*0.5 + DOWN*0.3)  # 调整位置以匹配矩形
        
        self.play(Create(golden_spiral), run_time=2)
        
        # 说明文字
        explanation = VGroup(
            Text("黄金螺线的增长率：", font_size=28, color=WHITE),
            MathTex(r"b = \frac{\ln(\varphi)}{\pi/2} \approx 0.3063", font_size=32, color=GOLD)
        ).arrange(DOWN, buff=0.3)
        explanation.shift(DOWN*2.5)
        
        self.play(Write(explanation))
        
        # 展示每转90度扩大φ倍
        growth_text = Text(
            "每转90°，半径扩大1.618倍",
            font_size=24,
            color=YELLOW
        ).next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(growth_text))
        self.wait(3)
        
        self.play(
            FadeOut(title),
            FadeOut(fib_rects),
            FadeOut(golden_spiral),
            FadeOut(explanation),
            FadeOut(growth_text)
        )
    
    def create_fibonacci_rectangles(self):
        """创建斐波那契矩形序列"""
        rectangles = VGroup()
        
        # 斐波那契数列
        fib = [1, 1, 2, 3, 5, 8]
        colors = [BLUE_E, BLUE_D, BLUE_C, BLUE_B, GREEN_E, GREEN_D]
        
        # 创建矩形
        scale = 0.3
        x, y = 0, 0
        
        for i, (size, color) in enumerate(zip(fib, colors)):
            rect = Square(
                side_length=size * scale,
                color=color,
                fill_opacity=0.3,
                stroke_width=2
            )
            
            # 定位矩形
            if i == 0:
                rect.move_to([x, y, 0])
            elif i == 1:
                rect.move_to([x + size*scale/2, y, 0])
                x += size*scale
            elif i == 2:
                rect.move_to([x, y + size*scale/2, 0])
                y += size*scale
            elif i == 3:
                rect.move_to([x - size*scale/2, y, 0])
                x -= size*scale
            elif i == 4:
                rect.move_to([x, y - size*scale/2, 0])
                y -= size*scale
            elif i == 5:
                rect.move_to([x + size*scale/2, y, 0])
                x += size*scale
            
            rectangles.add(rect)
            
            # 添加数字标签
            label = Text(str(size), font_size=20, color=WHITE)
            label.move_to(rect.get_center())
            rectangles.add(label)
        
        rectangles.move_to(ORIGIN)
        return rectangles
    
    def show_spirals_in_nature(self):
        """展示自然界中的螺线 - 3:00-3:30"""
        title = Text("等角螺线无处不在", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建示例网格
        examples = VGroup()
        
        # 1. 星系螺旋
        galaxy = self.create_galaxy_spiral()
        galaxy_label = Text("星系旋臂", font_size=20, color=WHITE)
        galaxy_label.next_to(galaxy, DOWN, buff=0.3)
        galaxy_group = VGroup(galaxy, galaxy_label)
        galaxy_group.shift(LEFT*4 + UP)
        examples.add(galaxy_group)
        
        # 2. 台风
        typhoon = self.create_typhoon_spiral()
        typhoon_label = Text("台风", font_size=20, color=WHITE)
        typhoon_label.next_to(typhoon, DOWN, buff=0.3)
        typhoon_group = VGroup(typhoon, typhoon_label)
        typhoon_group.shift(UP)
        examples.add(typhoon_group)
        
        # 3. 蜘蛛网
        web = self.create_spider_web()
        web_label = Text("蜘蛛网", font_size=20, color=WHITE)
        web_label.next_to(web, DOWN, buff=0.3)
        web_group = VGroup(web, web_label)
        web_group.shift(RIGHT*4 + UP)
        examples.add(web_group)
        
        # 4. 植物生长
        plant = self.create_plant_spiral()
        plant_label = Text("植物茎蔓", font_size=20, color=WHITE)
        plant_label.next_to(plant, DOWN, buff=0.3)
        plant_group = VGroup(plant, plant_label)
        plant_group.shift(LEFT*4 + DOWN*2)
        examples.add(plant_group)
        
        # 5. DNA双螺旋（简化版）
        dna = self.create_dna_spiral()
        dna_label = Text("DNA", font_size=20, color=WHITE)
        dna_label.next_to(dna, DOWN, buff=0.3)
        dna_group = VGroup(dna, dna_label)
        dna_group.shift(DOWN*2)
        examples.add(dna_group)
        
        # 6. 羊角
        horn = self.create_horn_spiral()
        horn_label = Text("羊角", font_size=20, color=WHITE)
        horn_label.next_to(horn, DOWN, buff=0.3)
        horn_group = VGroup(horn, horn_label)
        horn_group.shift(RIGHT*4 + DOWN*2)
        examples.add(horn_group)
        
        self.play(
            *[Create(example) for example in examples],
            run_time=3
        )
        
        # 总结文字
        summary = Text(
            "从微观到宏观，等角螺线是大自然的通用语言",
            font_size=24,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(summary))
        self.wait(3)
        
        self.play(
            FadeOut(title),
            FadeOut(examples),
            FadeOut(summary)
        )
    
    def create_galaxy_spiral(self):
        """创建星系螺旋"""
        spirals = VGroup()
        for i in range(2):
            spiral = self.create_logarithmic_spiral(
                a=0.1, b=0.15,
                t_max=2*PI,
                color=PURPLE_B,
                stroke_width=3
            )
            spiral.rotate(i * PI)
            spirals.add(spiral)
        
        # 添加星点
        stars = VGroup()
        for _ in range(20):
            star = Dot(
                radius=0.02,
                color=YELLOW,
                fill_opacity=np.random.random()
            )
            angle = np.random.random() * 2 * PI
            radius = 0.1 + np.random.random() * 0.5
            star.move_to(radius * np.array([np.cos(angle), np.sin(angle), 0]))
            stars.add(star)
        
        return VGroup(spirals, stars).scale(0.8)
    
    def create_typhoon_spiral(self):
        """创建台风螺旋"""
        spiral = self.create_logarithmic_spiral(
            a=0.05, b=0.25,
            t_max=4*PI,
            color=BLUE_D,
            stroke_width=4
        )
        
        # 添加风眼
        eye = Circle(radius=0.05, color=RED, fill_opacity=0.8)
        
        return VGroup(spiral, eye).scale(0.8)
    
    def create_spider_web(self):
        """创建蜘蛛网"""
        web = VGroup()
        
        # 径向线
        for i in range(8):
            angle = i * TAU / 8
            line = Line(
                ORIGIN,
                0.6 * np.array([np.cos(angle), np.sin(angle), 0]),
                color=GRAY,
                stroke_width=1
            )
            web.add(line)
        
        # 螺旋线
        spiral = self.create_logarithmic_spiral(
            a=0.05, b=0.2,
            t_max=3*PI,
            color=WHITE,
            stroke_width=2
        )
        web.add(spiral)
        
        return web.scale(0.8)
    
    def create_plant_spiral(self):
        """创建植物螺旋"""
        spiral = self.create_logarithmic_spiral(
            a=0.1, b=0.12,
            t_max=3*PI,
            color=GREEN,
            stroke_width=3
        )
        
        # 添加叶子
        leaves = VGroup()
        for i in range(5):
            t = i * PI / 2
            r = 0.1 * np.exp(0.12 * t)
            pos = r * np.array([np.cos(t), np.sin(t), 0])
            
            leaf = Ellipse(
                width=0.1, height=0.05,
                color=GREEN_D,
                fill_opacity=0.6
            )
            leaf.move_to(pos)
            leaf.rotate(t)
            leaves.add(leaf)
        
        return VGroup(spiral, leaves).scale(0.8)
    
    def create_dna_spiral(self):
        """创建DNA双螺旋（简化版）"""
        helices = VGroup()
        
        for i in range(2):
            helix = ParametricFunction(
                lambda t: np.array([
                    0.2 * np.cos(t + i * PI),
                    0.2 * np.sin(t + i * PI),
                    0.1 * t
                ]),
                t_range=[0, 4*PI],
                color=BLUE if i == 0 else RED,
                stroke_width=3
            )
            helices.add(helix)
        
        # 旋转以获得更好的视角
        helices.rotate(PI/6, axis=RIGHT)
        helices.rotate(PI/4, axis=UP)
        
        return helices.scale(0.5)
    
    def create_horn_spiral(self):
        """创建羊角螺旋"""
        horn = ParametricFunction(
            lambda t: np.array([
                0.1 * np.exp(0.1 * t) * np.cos(t),
                0.1 * np.exp(0.1 * t) * np.sin(t),
                0.05 * t
            ]),
            t_range=[0, 3*PI],
            color=MAROON_B,
            stroke_width=4
        )
        
        # 旋转以获得3D效果
        horn.rotate(PI/4, axis=RIGHT)
        horn.rotate(PI/6, axis=UP)
        
        return horn.scale(0.8)
    
    def show_ending(self):
        """结尾 - 3:30-4:00"""
        # 总结
        summary_lines = [
            Text("鹦鹉螺的螺旋", font_size=36, color=WHITE),
            Text("展现了大自然的数学智慧", font_size=36, color=WHITE),
            Text("等角螺线——", font_size=36, color=WHITE),
            Text("生长与美的完美结合", font_size=42, color=GOLD)
        ]
        summary = VGroup(*summary_lines).arrange(DOWN, buff=0.5)
        
        for line in summary_lines:
            self.play(Write(line), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(summary))
        
        # 下期预告
        next_episode = VGroup(
            Text("下期预告", font_size=36, color=YELLOW),
            Text("黄金矩形与艺术构图", font_size=32, color=WHITE),
            Text("探索美的数学法则", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(next_episode[0]), run_time=1)
        self.play(FadeIn(next_episode[1], shift=UP), run_time=1)
        self.play(FadeIn(next_episode[2], shift=UP), run_time=1)
        
        # 订阅提醒
        subscribe = Text("喜欢请三连支持！", font_size=32, color=RED)
        subscribe.next_to(next_episode, DOWN, buff=1)
        
        self.play(Write(subscribe))
        self.wait(3) 