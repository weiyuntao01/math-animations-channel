"""
数字仿生系列 第8集：DNA的信息宇宙
Digital Biomimetics EP08: Information Universe of DNA

从双螺旋几何到遗传密码 - 4个字母编写生命故事
"""

from manim import *
import numpy as np
import random
from typing import List, Tuple

# 系列通用色彩
BIO_CYAN = ManimColor("#00FFE5")
BIO_PURPLE = ManimColor("#8B5CF6")
BIO_GREEN = ManimColor("#00FF88")
BIO_BLUE = ManimColor("#007EFF")
BIO_YELLOW = ManimColor("#FFE500")
BIO_RED = ManimColor("#FF0066")
BIO_WHITE = ManimColor("#FFFFFF")
BIO_GRAY = ManimColor("#303030")

# EP08 主题色
DNA_BLUE = ManimColor("#4A90E2")
BASE_PURPLE = ManimColor("#7D3C98")
GENE_GOLD = ManimColor("#F1C40F")

# 字体大小
TITLE_SIZE = 44
SUBTITLE_SIZE = 30
NORMAL_SIZE = 24
SMALL_SIZE = 20


class DigitalBiomimeticsEP08(Scene):
    """数字仿生系列 第8集"""

    def construct(self):
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = "#090909"

        self.show_series_intro()
        self.answer_preview_question()
        self.dna_mathematics()
        self.double_helix_scene()
        self.genetic_code_scene()
        self.show_ending()

    def show_series_intro(self):
        """系列开场动画 - DNA螺旋背景 + 标题"""
        bg = self.create_dna_background()
        bg.set_opacity(0.2)
        self.play(Create(bg), run_time=2)

        series_title = Text("数字仿生", font_size=60, color=BIO_CYAN, weight=BOLD).move_to([0, 1, 0])
        subtitle = Text("DIGITAL BIOMIMETICS", font_size=24, color=BIO_WHITE, font="Arial").next_to(series_title, DOWN, buff=0.3)
        episode_text = Text("第8集：DNA的信息宇宙", font_size=34, color=DNA_BLUE).move_to([0, -1.5, 0])

        self.play(Write(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=1)
        self.play(Write(episode_text), run_time=1.5)
        self.play(series_title.animate.scale(1.1).set_color(BASE_PURPLE), rate_func=there_and_back, run_time=1)
        self.wait(3)
        self.play(FadeOut(series_title), FadeOut(subtitle), FadeOut(episode_text), FadeOut(bg))

    def create_dna_background(self) -> VGroup:
        """创建抽象DNA双螺旋背景"""
        group = VGroup()
        for i in range(20):
            t = np.linspace(0, 4*np.pi, 100)
            x = 0.5 * np.cos(t + i*0.3)
            y = t / 2 - 3
            z = np.zeros_like(x)
            
            # 第一条螺旋
            pts1 = np.column_stack([x, y, z])
            curve1 = VMobject().set_points_smoothly(pts1).set_stroke(DNA_BLUE, width=1.5, opacity=0.3)
            
            # 第二条螺旋（相位偏移）
            x2 = x + 0.3 * np.sin(t + i*0.3)
            pts2 = np.column_stack([x2, y, z])
            curve2 = VMobject().set_points_smoothly(pts2).set_stroke(BASE_PURPLE, width=1.5, opacity=0.3)
            
            group.add(curve1, curve2)
        return group

    def answer_preview_question(self):
        """回应EP07预告：4个字母如何编写生命的全部故事？"""
        title = Text("生命的编程语言", font_size=TITLE_SIZE, color=DNA_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 创建4个碱基字母
        bases = VGroup(
            Text("A", font_size=80, color=BIO_RED, weight=BOLD),
            Text("T", font_size=80, color=BIO_BLUE, weight=BOLD),
            Text("G", font_size=80, color=BIO_GREEN, weight=BOLD),
            Text("C", font_size=80, color=BIO_YELLOW, weight=BOLD)
        ).arrange(RIGHT, buff=1)
        bases.move_to([0, 0.5, 0])
        
        self.play(Write(bases))
        
        # 解释
        explanation = VGroup(
            Text("仅用4个字母：A、T、G、C", font_size=NORMAL_SIZE, color=BIO_WHITE),
            Text("就能编写出地球上所有生命", font_size=NORMAL_SIZE, color=BIO_CYAN),
            Text("这就是DNA的信息奇迹", font_size=NORMAL_SIZE, color=GENE_GOLD, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        explanation.move_to([0, -1.5, 0])
        
        for line in explanation:
            self.play(Write(line), run_time=0.8)
        
        self.wait(3)
        self.play(
            FadeOut(title),
            FadeOut(bases), 
            FadeOut(explanation)
        )

    def dna_mathematics(self):
        """展示DNA与遗传信息的数学本质"""
        title = Text("DNA的数学密码", font_size=TITLE_SIZE, color=DNA_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        left = VGroup(
            Text("双螺旋几何", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"x = r \cos(\theta)", font_size=28, color=BIO_CYAN),
            MathTex(r"y = r \sin(\theta)", font_size=28, color=BIO_CYAN),
            MathTex(r"z = p \cdot \theta / (2\pi)", font_size=28, color=BIO_CYAN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        right = VGroup(
            Text("遗传信息论", font_size=SMALL_SIZE, color=BIO_WHITE),
            MathTex(r"H = -\sum p_i \log_2 p_i", font_size=28, color=BIO_GREEN),
            Text("碱基对信息熵", font_size=SMALL_SIZE, color=BIO_YELLOW),
            MathTex(r"\Delta G = \Delta H - T\Delta S", font_size=28, color=BIO_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        cols = VGroup(left, right).arrange(RIGHT, buff=2.5)
        cols.next_to(title, DOWN, buff=0.6)

        for grp in [left, right]:
            for item in grp:
                self.play(Write(item), run_time=0.5)

        insight = Text("螺旋几何 + 信息编码 = 生命的蓝图", font_size=SUBTITLE_SIZE, color=GENE_GOLD)
        insight.to_edge(DOWN, buff=0.8)
        self.play(Write(insight))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(cols), FadeOut(insight))

    def double_helix_scene(self):
        """可视化：DNA双螺旋（动态旋转 + 碱基对标识）"""
        self.clear()
        title = Text("生命形态 I：双螺旋的旋转之舞", font_size=SUBTITLE_SIZE, color=DNA_BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        t_tracker = ValueTracker(0.0)

        def create_double_helix():
            t = t_tracker.get_value()
            helix = VGroup()
            
            # 减少点数以提高性能
            num_points = 60
            for i in range(num_points):
                theta = i * 0.3 + t * 0.8
                # 调整高度范围，避免与标题重叠
                height = (i / num_points) * 3.5 - 1.2  # 从-1.2到2.3，标题在3.5左右
                
                # 双链坐标
                x1 = 1.5 * np.cos(theta)
                y1 = height
                x2 = 1.5 * np.cos(theta + np.pi)
                y2 = height
                
                # 投影到2D - 增加水平间距
                pos1 = [x1 * 0.4, y1, 0]
                pos2 = [x2 * 0.4, y2, 0]
                
                # 糖磷酸骨架
                backbone1 = Dot(pos1, radius=0.04, color=DNA_BLUE, fill_opacity=0.8)
                backbone2 = Dot(pos2, radius=0.04, color=BASE_PURPLE, fill_opacity=0.8)
                helix.add(backbone1, backbone2)
                
                # 碱基对连接（每5个点一次）
                if i % 5 == 0:
                    # 碱基对横杠
                    base_pair = Line(pos1, pos2, color=GENE_GOLD, stroke_width=2)
                    helix.add(base_pair)
                    
                    # 碱基标识（A-T或G-C）
                    base_types = ['A', 'T', 'G', 'C']
                    base_choice = base_types[i % 4]
                    
                    if base_choice in ['A', 'T']:
                        base_color = BIO_RED if base_choice == 'A' else BIO_BLUE
                        complement_color = BIO_BLUE if base_choice == 'A' else BIO_RED
                    else:
                        base_color = BIO_GREEN if base_choice == 'G' else BIO_YELLOW  
                        complement_color = BIO_YELLOW if base_choice == 'G' else BIO_GREEN
                    
                    # 只在某些位置显示字母，避免过密
                    if i % 15 == 0:
                        base_text = Text(base_choice, font_size=12, color=base_color)
                        base_text.move_to(pos1)
                        helix.add(base_text)
            
            return helix

        helix = always_redraw(create_double_helix)

        info = Text("每一圈螺旋包含10个碱基对", font_size=SMALL_SIZE, color=BIO_WHITE)
        info.to_edge(DOWN, buff=0.5)

        self.add(helix)
        self.play(Write(info))
        self.play(t_tracker.animate.set_value(6*np.pi), run_time=12, rate_func=linear)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(info), FadeOut(helix))

    def genetic_code_scene(self):
        """可视化：遗传密码翻译（DNA → RNA → 蛋白质）"""
        self.clear()
        title = Text("生命形态 II：中心法则的信息流", font_size=SUBTITLE_SIZE, color=GENE_GOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        # 创建三层结构，垂直排列
        # DNA层
        dna_label = Text("DNA", font_size=NORMAL_SIZE, color=DNA_BLUE, weight=BOLD)
        dna_label.move_to([-5.5, 2, 0])
        
        # 使用更简洁的序列展示
        dna_sequence = "ATGCGATAC"  # 3个完整的密码子
        dna_group = VGroup()
        
        for i, base in enumerate(dna_sequence):
            x_pos = -2.5 + i * 0.6
            color_map = {'A': BIO_RED, 'T': BIO_BLUE, 'G': BIO_GREEN, 'C': BIO_YELLOW}
            
            # 创建圆形碱基，更美观
            base_circle = Circle(radius=0.25, color=color_map[base], fill_opacity=0.9, stroke_width=2)
            base_circle.move_to([x_pos, 2, 0])
            base_text = Text(base, font_size=20, color=BIO_WHITE, weight=BOLD)
            base_text.move_to([x_pos, 2, 0])
            
            dna_group.add(base_circle, base_text)
        
        self.play(Write(dna_label), Create(dna_group), run_time=2)
        
        # 添加密码子分组框
        codon_boxes = VGroup()
        for i in range(0, len(dna_sequence), 3):
            if i + 2 < len(dna_sequence):
                box = Rectangle(
                    width=1.6, height=0.7,
                    color=BIO_WHITE, stroke_width=1.5, fill_opacity=0
                )
                box.move_to([-2.5 + (i + 1) * 0.6, 2, 0])
                codon_boxes.add(box)
        
        self.play(Create(codon_boxes), run_time=1)
        self.wait(0.5)
        
        # 第二步：转录动画（DNA → RNA）
        # 创建转录箭头
        transcription_arrow = CurvedArrow(
            start_point=[0, 1.6, 0],
            end_point=[0, 0.4, 0],
            angle=-TAU/8,
            color=BIO_WHITE,
            stroke_width=3
        )
        transcription_text = Text("转录", font_size=SMALL_SIZE, color=BIO_WHITE)
        transcription_text.next_to(transcription_arrow, RIGHT, buff=0.3)
        
        self.play(Create(transcription_arrow), Write(transcription_text))
        
        # RNA层
        rna_label = Text("RNA", font_size=NORMAL_SIZE, color=BIO_CYAN, weight=BOLD)
        rna_label.move_to([-5.5, 0, 0])
        
        rna_group = VGroup()
        
        # 先创建所有RNA碱基（不显示）
        for i, base in enumerate(dna_sequence):
            x_pos = -2.5 + i * 0.6
            # T → U 转换
            rna_base = 'U' if base == 'T' else base
            color_map = {'A': BIO_RED, 'U': BIO_PURPLE, 'G': BIO_GREEN, 'C': BIO_YELLOW}
            
            # 创建RNA碱基在目标位置
            rna_circle = Circle(radius=0.25, color=color_map[rna_base], fill_opacity=0.7, stroke_width=2)
            rna_circle.move_to([x_pos, 0, 0])
            rna_text = Text(rna_base, font_size=20, color=BIO_WHITE, weight=BOLD)
            rna_text.move_to([x_pos, 0, 0])
            
            rna_group.add(rna_circle, rna_text)
        
        # 使用FadeIn动画显示RNA，避免与DNA重叠
        self.play(
            *[FadeIn(mob, shift=DOWN*0.5) for mob in rna_group],
            run_time=2
        )
        
        self.play(Write(rna_label))
        self.wait(1)
        
        # 第三步：翻译动画（RNA → 蛋白质）
        # 创建翻译箭头
        translation_arrow = CurvedArrow(
            start_point=[0, -0.4, 0],
            end_point=[0, -1.6, 0],
            angle=-TAU/8,
            color=BIO_WHITE,
            stroke_width=3
        )
        translation_text = Text("翻译", font_size=SMALL_SIZE, color=BIO_WHITE)
        translation_text.next_to(translation_arrow, RIGHT, buff=0.3)
        
        self.play(Create(translation_arrow), Write(translation_text))
        
        # 蛋白质层
        protein_label = Text("蛋白质", font_size=NORMAL_SIZE, color=BIO_PURPLE, weight=BOLD)
        protein_label.move_to([-5.5, -2, 0])
        
        # 密码子到氨基酸的翻译
        rna_sequence = dna_sequence.replace('T', 'U')  # AUGCGAUAC
        
        # 准确的密码子表
        codon_table = {
            'AUG': ('Met', '起始'),  # 甲硫氨酸
            'CGA': ('Arg', '精氨酸'),
            'UAC': ('Tyr', '酪氨酸')
        }
        
        # 动画：三个碱基组合成一个氨基酸
        protein_group = VGroup()
        
        for codon_idx in range(0, len(rna_sequence), 3):
            if codon_idx + 2 < len(rna_sequence):
                # 高亮当前处理的三个RNA碱基
                highlight_boxes = VGroup()
                for j in range(3):
                    box = Rectangle(
                        width=0.55, height=0.55,
                        color=GENE_GOLD, stroke_width=3, fill_opacity=0.2
                    )
                    box.move_to([-2.5 + (codon_idx + j) * 0.6, 0, 0])
                    highlight_boxes.add(box)
                
                self.play(Create(highlight_boxes), run_time=0.5)
                
                # 获取密码子和对应氨基酸
                codon = rna_sequence[codon_idx:codon_idx+3]
                amino_acid, chinese_name = codon_table.get(codon, ('Xxx', '未知'))
                
                # 创建氨基酸球体（更美观）
                aa_pos = [-1.5 + (codon_idx // 3) * 1.5, -2, 0]
                aa_sphere = Circle(radius=0.4, color=BIO_PURPLE, fill_opacity=0.9, stroke_width=3)
                aa_sphere.move_to(aa_pos)
                aa_text = Text(amino_acid, font_size=18, color=BIO_WHITE, weight=BOLD)
                aa_text.move_to(aa_pos)
                
                # 中文名称
                aa_chinese = Text(chinese_name, font_size=12, color=BIO_CYAN)
                aa_chinese.move_to([aa_pos[0], aa_pos[1] - 0.6, 0])
                
                protein_group.add(aa_sphere, aa_text, aa_chinese)
                
                # 从RNA位置飞到蛋白质位置的动画
                temp_sphere = aa_sphere.copy()
                temp_sphere.scale(0.5).move_to([-2.5 + codon_idx * 0.6 + 0.6, 0, 0])  # 从密码子中心开始
                
                self.play(
                    FadeOut(highlight_boxes),
                    FadeIn(temp_sphere),
                    run_time=0.4
                )
                self.play(
                    temp_sphere.animate.scale(2).move_to(aa_pos),
                    run_time=0.8
                )
                self.remove(temp_sphere)
                self.add(aa_sphere)
                self.play(
                    Write(aa_text),
                    Write(aa_chinese),
                    run_time=0.5
                )
        
        self.play(Write(protein_label))
        
        # 连接氨基酸的肽键
        peptide_bonds = VGroup()
        for i in range(2):
            bond = Line(
                [-1.5 + i * 1.5 + 0.4, -2, 0],
                [-1.5 + (i + 1) * 1.5 - 0.4, -2, 0],
                color=BIO_WHITE, stroke_width=2
            )
            peptide_bonds.add(bond)
        
        self.play(Create(peptide_bonds), run_time=1)
        
        # 最终总结动画
        self.wait(1)
        
        # 创建信息流动效果
        flow_particles = VGroup()
        for i in range(15):
            particle = Dot(radius=0.02, color=GENE_GOLD, fill_opacity=0.8)
            start_y = 2 - i * 0.3
            particle.move_to([-4 + np.random.uniform(-0.5, 0.5), start_y, 0])
            flow_particles.add(particle)
        
        self.play(
            *[particle.animate.shift(RIGHT * 8) for particle in flow_particles],
            run_time=3,
            rate_func=linear
        )
        
        self.wait(1)
        
        # 淡出所有元素，准备展示总结文字
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        
        # 新页面：只显示三行总结文字
        info = VGroup(
            Text("中心法则：生命信息的单向流动", font_size=NORMAL_SIZE, color=GENE_GOLD, weight=BOLD),
            Text("DNA → RNA → 蛋白质", font_size=SMALL_SIZE, color=BIO_WHITE),
            Text("4个字母 → 20种氨基酸 → 无限可能", font_size=SMALL_SIZE, color=BIO_CYAN)
        ).arrange(DOWN, buff=0.4)
        info.move_to(ORIGIN)
        
        for line in info:
            self.play(Write(line), run_time=0.8)
        
        self.wait(3)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )


    def show_ending(self):
        """结尾与下期预告"""
        self.clear()
        recap_title = Text("本集回顾", font_size=SUBTITLE_SIZE, color=DNA_BLUE)
        recap_title.to_edge(UP, buff=0.5)
        self.play(Write(recap_title))

        recap = VGroup(
            Text("✓ 双螺旋的几何美学", font_size=NORMAL_SIZE),
            Text("✓ 遗传代码的信息论", font_size=NORMAL_SIZE),
            Text("✓ 演化动力学的可视化", font_size=NORMAL_SIZE, color=GENE_GOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to([0, 0.5, 0])

        for line in recap:
            self.play(Write(line), run_time=0.6)

        self.wait(3)
        self.play(FadeOut(recap_title), FadeOut(recap))

        philosophy = VGroup(
            Text("DNA：生命的编码与演化", font_size=38, color=BIO_PURPLE),
            Text("信息流，塑造万物", font_size=38, color=BIO_CYAN),
            Text("数学，解锁遗传之谜", font_size=SUBTITLE_SIZE, color=GENE_GOLD)
        ).arrange(DOWN, buff=0.6)

        for line in philosophy:
            self.play(Write(line), run_time=1)

        self.wait(3)
        self.play(FadeOut(philosophy))

        self.show_next_episode_preview()

    def show_next_episode_preview(self):
        """下期预告：免疫系统的战争艺术（EP09）"""
        preview_title = Text("下期预告", font_size=38, color=BIO_YELLOW)
        preview_title.to_edge(UP, buff=0.5)
        self.play(Write(preview_title))

        ep9_title = Text("第9集：免疫系统的战争艺术", font_size=TITLE_SIZE, color=BIO_RED, weight=BOLD).move_to([0, 1.5, 0])
        bullets = VGroup(
            Text("细胞战争的数学模型", font_size=SUBTITLE_SIZE, color=BIO_CYAN),
            Text("免疫记忆与适应", font_size=SUBTITLE_SIZE, color=BIO_GREEN),
            Text("防御网络的动态平衡", font_size=SUBTITLE_SIZE, color=BIO_RED)
        ).arrange(DOWN, buff=0.5).move_to([0, -0.5, 0])
        self.play(Write(ep9_title))
        for line in bullets:
            self.play(Write(line), run_time=0.8)

        q = Text("思考：免疫系统如何'学习'并记住敌人？", font_size=20, color=BIO_YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(q))
        self.wait(3)
        
        see_you = Text(
            "下期再见！",
            font_size=38,
            color=BIO_WHITE
        )
        see_you.move_to(ORIGIN)

        self.play(
            FadeOut(preview_title),
            FadeOut(ep9_title), 
            FadeOut(bullets),
            FadeOut(q),
            Write(see_you)
        )

        # 最后的DNA螺旋动画
        final_dna = self.create_dna_background()
        final_dna.scale(0.5).set_opacity(0.3)
        self.play(Create(final_dna), run_time=2)

        self.wait(2)
        self.play(FadeOut(see_you), FadeOut(final_dna))
