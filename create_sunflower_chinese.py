code = '''from manim import *
import numpy as np

class SunflowerGoldenSpiralChinese(Scene):
    """向日葵中的螺旋密码 - 中文版"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 开场
        self.show_opening()
        
        # 第一部分：神秘现象
        self.show_mystery()
        
        # 第二部分：斐波那契数列
        self.show_fibonacci()
        
        # 第三部分：黄金角度
        self.show_golden_angle()
        
        # 第四部分：向日葵生成
        self.create_sunflower()
        
        # 结尾
        self.show_ending()
    
    def show_opening(self):
        """开场动画 - 0:00-0:10"""
        # 讲解词：大家好，欢迎来到数学之美。今天，我们要揭开一个隐藏在向日葵中的数学秘密。
        
        title = Text("数学之美", font_size=56, color=GOLD)
        subtitle = Text("第一集：向日葵中的螺旋密码", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def show_mystery(self):
        """引入神秘现象 - 0:10-0:30"""
        # 讲解词：你有没有仔细观察过向日葵的花盘？那些种子并不是随机排列的，
        # 而是形成了精美的螺旋图案。这背后，隐藏着大自然最神奇的数学规律。
        
        question = Text("为什么向日葵的种子\n会形成螺旋？", font_size=42, color=WHITE)
        self.play(Write(question), run_time=2)
        self.wait(2)
        
        # 创建向日葵示意图
        flower_disk = Circle(radius=2.5, color=YELLOW_D, fill_opacity=0.3)
        flower_petals = VGroup()
        
        # 添加花瓣
        for i in range(16):
            angle = i * TAU / 16
            petal = Ellipse(width=0.8, height=2, color=YELLOW, fill_opacity=0.8)
            petal.rotate(angle)
            petal.shift(2.5 * np.array([np.cos(angle), np.sin(angle), 0]))
            flower_petals.add(petal)
        
        flower = VGroup(flower_disk, flower_petals)
        
        self.play(
            Transform(question, flower_disk),
            *[GrowFromCenter(petal) for petal in flower_petals],
            run_time=2
        )
        self.wait(2)
        
        # 高亮螺旋
        spiral_hint = Text("隐藏的螺旋", font_size=28, color=GREEN).to_edge(DOWN)
        self.play(Write(spiral_hint))
        self.wait(1)
        
        self.play(FadeOut(flower), FadeOut(question), FadeOut(spiral_hint))
    
    def show_fibonacci(self):
        """斐波那契数列 - 0:30-1:20"""
        # 讲解词：要理解这个秘密，我们需要先认识一个神奇的数列——斐波那契数列。
        # 这个数列的规律很简单：从1和1开始，每个数都是前两个数的和。
        # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
        # 这个看似简单的数列，却在自然界中无处不在。
        
        fib_title = Text("斐波那契数列", font_size=48, color=BLUE).to_edge(UP)
        self.play(Write(fib_title))
        
        # 数列展示
        fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        fib_text = VGroup()
        
        # 第一行数字
        for i, num in enumerate(fib_numbers[:6]):
            number = Text(str(num), font_size=40, color=WHITE)
            if i == 0:
                number.shift(LEFT * 3 + UP * 0.5)
            else:
                number.next_to(fib_text[-1], RIGHT, buff=0.8)
            fib_text.add(number)
        
        # 动画展示规律
        for i in range(len(fib_text)):
            if i < 2:
                self.play(Write(fib_text[i]), run_time=0.5)
            else:
                # 显示加法过程
                arrow1 = Arrow(
                    fib_text[i-2].get_bottom(),
                    fib_text[i-2].get_bottom() + DOWN * 0.5,
                    color=GREEN,
                    buff=0.1
                )
                arrow2 = Arrow(
                    fib_text[i-1].get_bottom(),
                    fib_text[i-1].get_bottom() + DOWN * 0.5,
                    color=GREEN,
                    buff=0.1
                )
                plus = Text("+", font_size=30, color=GREEN)
                plus.move_to((arrow1.get_end() + arrow2.get_end()) / 2)
                
                self.play(
                    Create(arrow1), Create(arrow2),
                    Write(plus),
                    run_time=0.3
                )
                self.play(Write(fib_text[i]), run_time=0.5)
                self.play(
                    FadeOut(arrow1), FadeOut(arrow2), FadeOut(plus),
                    run_time=0.3
                )
        
        self.wait(1)
        
        # 展示在自然界中的应用
        nature_examples = Text(
            "花瓣数、树枝分叉、贝壳螺旋...\n大自然钟爱这个数列！",
            font_size=28,
            color=GREEN
        ).next_to(fib_text, DOWN, buff=1.5)
        
        self.play(Write(nature_examples))
        self.wait(3)
        
        self.play(
            FadeOut(fib_title),
            FadeOut(fib_text),
            FadeOut(nature_examples)
        )
    
    def show_golden_angle(self):
        """黄金角度 - 1:20-2:00"""
        # 讲解词：现在，让我们来看看向日葵是如何运用这个数列的。
        # 关键在于一个特殊的角度——黄金角，约等于137.5度。
        # 这个角度来自黄金比例，是自然界中最优雅的分割方式。
        
        title = Text("黄金角", font_size=48, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 创建圆和角度展示
        circle = Circle(radius=2, color=WHITE, stroke_width=2)
        center = Dot(ORIGIN, color=WHITE)
        
        # 黄金角
        golden_angle = 137.5 * DEGREES
        
        # 创建角度弧
        arc = Arc(
            radius=0.8,
            start_angle=0,
            angle=golden_angle,
            color=GOLD,
            stroke_width=4
        )
        
        # 半径线
        line1 = Line(ORIGIN, RIGHT * 2, color=BLUE, stroke_width=3)
        line2 = Line(
            ORIGIN,
            2 * np.array([np.cos(golden_angle), np.sin(golden_angle), 0]),
            color=BLUE,
            stroke_width=3
        )
        
        # 角度标注
        angle_label = Text("137.5°", font_size=32, color=GOLD)
        angle_label.move_to(0.5 * np.array([np.cos(golden_angle/2), np.sin(golden_angle/2), 0]))
        
        # 黄金比例说明
        golden_ratio_text = Text(
            "黄金角 = 360° × (2 - φ)\nφ = 1.618... (黄金比例)",
            font_size=24,
            color=YELLOW
        ).to_corner(DR)
        
        # 动画展示
        self.play(Create(circle), Create(center))
        self.play(Create(line1))
        self.play(Create(line2), Create(arc), run_time=1.5)
        self.play(Write(angle_label))
        self.wait(1)
        self.play(Write(golden_ratio_text))
        self.wait(2)
        
        # 展示为什么这个角度特殊
        explanation = Text(
            "这个角度能让新生长的种子\n与已有种子的重叠最小",
            font_size=28,
            color=GREEN
        ).next_to(circle, DOWN, buff=0.8)
        
        self.play(Write(explanation))
        self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(circle), FadeOut(center),
            FadeOut(line1), FadeOut(line2), FadeOut(arc),
            FadeOut(angle_label), FadeOut(golden_ratio_text),
            FadeOut(explanation)
        )
    
    def create_sunflower(self):
        """创建向日葵 - 2:00-3:00"""
        # 讲解词：现在，让我们用黄金角来创建一朵向日葵。
        # 每个新种子都比前一个种子旋转137.5度，
        # 距离中心的距离与种子序号的平方根成正比。
        # 看看会发生什么神奇的事情...
        
        title = Text("向日葵的数学生成", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 参数设置
        golden_angle = 137.5 * DEGREES
        n_seeds = 800
        scale_factor = 0.06
        
        # 创建中心
        center = Dot(ORIGIN, radius=0.05, color=ORANGE)
        self.play(Create(center))
        
        # 种子容器
        seeds = VGroup()
        clockwise_spirals = []  # 顺时针螺旋
        counter_spirals = []    # 逆时针螺旋
        
        # 创建种子
        for i in range(1, n_seeds + 1):
            angle = i * golden_angle
            radius = scale_factor * np.sqrt(i)
            
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            
            # 根据斐波那契数标记特殊螺旋
            if i % 21 == 0:  # 21条顺时针螺旋
                color = RED
                seed = Dot([x, y, 0], radius=0.03, color=color)
                clockwise_spirals.append(seed)
            elif i % 34 == 0:  # 34条逆时针螺旋
                color = BLUE
                seed = Dot([x, y, 0], radius=0.03, color=color)
                counter_spirals.append(seed)
            else:
                color = YELLOW
                seed = Dot([x, y, 0], radius=0.015, color=color)
            
            seeds.add(seed)
        
        # 分阶段动画
        # 第一阶段：展示前100个种子
        info_text = Text("每个种子旋转137.5°", font_size=24, color=WHITE).to_corner(UR)
        self.play(Write(info_text))
        
        self.play(
            LaggedStart(*[Create(seed) for seed in seeds[:100]], lag_ratio=0.02),
            run_time=3
        )
        
        # 第二阶段：加速展示剩余种子
        self.play(FadeOut(info_text))
        info_text2 = Text("螺旋图案自然形成", font_size=24, color=WHITE).to_corner(UR)
        self.play(Write(info_text2))
        
        self.play(
            LaggedStart(*[Create(seed) for seed in seeds[100:]], lag_ratio=0.001),
            run_time=3
        )
        
        self.wait(1)
        
        # 高亮显示螺旋
        self.play(FadeOut(info_text2))
        
        # 显示斐波那契螺旋
        spiral_info = VGroup(
            Text("21条顺时针螺旋", font_size=24, color=RED),
            Text("34条逆时针螺旋", font_size=24, color=BLUE),
            Text("都是斐波那契数！", font_size=28, color=GREEN)
        ).arrange(DOWN, buff=0.3).to_corner(UR)
        
        # 高亮螺旋
        self.play(
            *[seed.animate.scale(2) for seed in clockwise_spirals],
            Write(spiral_info[0]),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            *[seed.animate.scale(0.5) for seed in clockwise_spirals],
            *[seed.animate.scale(2) for seed in counter_spirals],
            Write(spiral_info[1]),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            *[seed.animate.scale(0.5) for seed in counter_spirals],
            Write(spiral_info[2]),
            run_time=1
        )
        self.wait(2)
        
        # 淡出
        self.play(
            FadeOut(title), FadeOut(seeds), FadeOut(center),
            FadeOut(spiral_info)
        )
    
    def show_ending(self):
        """结尾 - 3:00-3:30"""
        # 讲解词：这就是向日葵的秘密——通过黄金角和斐波那契数列，
        # 大自然创造出了最优雅、最高效的种子排列方式。
        # 这不仅仅是巧合，而是数学在自然界中的完美体现。
        # 下一集，我们将探索更多隐藏在大自然中的数学奇迹。
        # 如果你喜欢这个视频，请点赞订阅，我们下期再见！
        
        # 总结信息
        summary = VGroup(
            Text("大自然的数学智慧", font_size=48, color=GOLD),
            Text("黄金角 × 斐波那契数列 = 完美螺旋", font_size=32, color=YELLOW),
            Text("从向日葵到银河系，数学无处不在", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.6)
        
        self.play(Write(summary[0]), run_time=2)
        self.play(FadeIn(summary[1], shift=UP), run_time=1.5)
        self.play(FadeIn(summary[2], shift=UP), run_time=1.5)
        self.wait(3)
        
        self.play(FadeOut(summary))
        
        # 订阅提醒
        subscribe_group = VGroup(
            Text("喜欢请三连支持！", font_size=36, color=RED),
            Text("下期预告：分形几何的奇妙世界", font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(subscribe_group[0]), run_time=1.5)
        self.play(FadeIn(subscribe_group[1], shift=UP), run_time=1)
        self.wait(3)
'''

# 保存动画文件
with open('scenes/geometry/sunflower_chinese.py', 'w', encoding='utf-8') as f:
    f.write(code)

# 创建配音文稿
narration = '''# 向日葵中的螺旋密码 - 配音文稿

## 时间轴与配音内容

### 0:00-0:10 开场
大家好，欢迎来到数学之美。今天，我们要揭开一个隐藏在向日葵中的数学秘密。

### 0:10-0:30 引入神秘现象
你有没有仔细观察过向日葵的花盘？那些种子并不是随机排列的，而是形成了精美的螺旋图案。这背后，隐藏着大自然最神奇的数学规律。

### 0:30-1:20 斐波那契数列
要理解这个秘密，我们需要先认识一个神奇的数列——斐波那契数列。这个数列的规律很简单：从1和1开始，每个数都是前两个数的和。

1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

这个看似简单的数列，却在自然界中无处不在。花瓣的数量、树枝的分叉、贝壳的螺旋，都遵循着这个规律。

### 1:20-2:00 黄金角度
现在，让我们来看看向日葵是如何运用这个数列的。关键在于一个特殊的角度——黄金角，约等于137.5度。

这个角度来自黄金比例，是自然界中最优雅的分割方式。为什么这个角度如此特殊？因为它能让新生长的种子与已有种子的重叠最小，实现空间的最优利用。

### 2:00-3:00 向日葵生成
现在，让我们用黄金角来创建一朵向日葵。每个新种子都比前一个种子旋转137.5度，距离中心的距离与种子序号的平方根成正比。

看看会发生什么神奇的事情...

螺旋出现了！如果仔细数一数，你会发现有21条顺时针螺旋，34条逆时针螺旋——都是斐波那契数！

### 3:00-3:30 结尾
这就是向日葵的秘密——通过黄金角和斐波那契数列，大自然创造出了最优雅、最高效的种子排列方式。

这不仅仅是巧合，而是数学在自然界中的完美体现。

下一集，我们将探索更多隐藏在大自然中的数学奇迹。如果你喜欢这个视频，请点赞订阅，我们下期再见！

---

## 配音技巧建议：
1. 语速适中，每分钟180-200字
2. 在数字和公式处稍作停顿
3. 情绪递进：好奇→惊叹→领悟→赞叹
4. 重点词汇加重语气：斐波那契、黄金角、137.5度
'''

# 保存配音文稿
with open('docs/sunflower_narration.md', 'w', encoding='utf-8') as f:
    f.write(narration)

print('文件创建成功！')
print('动画文件：scenes/geometry/sunflower_chinese.py')
print('配音文稿：docs/sunflower_narration.md')