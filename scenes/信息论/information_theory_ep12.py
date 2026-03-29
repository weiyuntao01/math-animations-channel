from manim import *
import numpy as np

# --- 信息论系列配色 ---
IT_GREEN = "#00FF41"     # 信号 / 成功 / Alice混合色 (绿)
IT_RED = "#FF2A68"       # 噪音 / 错误 / Bob私有色 (红)
IT_BLUE = "#00BFFF"      # 结构 / Alice私有色 (蓝)
IT_YELLOW = "#FFD700"    # 公共底色 (黄)
IT_ORANGE = "#F97316"    # Bob混合色 (橙)
IT_BROWN = "#8B4513"     # 最终共享密钥 (褐)
IT_PURPLE = "#8B5CF6"    # 哲学 / Eve (窃听者)
IT_GRAY = "#333333"      # 背景细节
BG_COLOR = "#000000"     # 纯黑背景

class InformationTheoryEP12(Scene):
    """信息论 EP12: 公钥密码 (Diffie-Hellman Color Exchange)"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：不信任的世界
        self.intro_trust_problem()
        
        # 2. 核心演示：颜色混合游戏 (DH算法)
        self.color_exchange_demo()
        
        # 3. 数学本质：模运算与离散对数
        self.math_behind_magic()
        
        # 4. 哲学升华
        self.show_philosophy()

    def intro_trust_problem(self):
        """开场：如何在监视下交换秘密？"""
        
        # 标题上移
        title = Text("EP12: 公钥密码", font_size=54, color=IT_GREEN, weight=BOLD).to_edge(UP, buff=1.0)
        subtitle = Text("Diffie-Hellman Key Exchange", font_size=28, color=IT_GRAY).next_to(title, DOWN, buff=0.3)
        
        self.play(DrawBorderThenFill(title), FadeIn(subtitle, shift=UP))
        
        # 场景布局
        LEFT_POS = LEFT * 4.5
        RIGHT_POS = RIGHT * 4.5
        
        alice = self.create_avatar("Alice", IT_BLUE).move_to(LEFT_POS)
        bob = self.create_avatar("Bob", IT_RED).move_to(RIGHT_POS)
        
        # 中间的公开信道
        channel = Line(LEFT * 3.5, RIGHT * 3.5, color=IT_GRAY)
        
        # 窃听者 Eve
        eve = self.create_avatar("Eve", IT_PURPLE).move_to(UP * 0.5)
        eve_label = Text("(窃听者)", font_size=20, color=IT_PURPLE).next_to(eve, UP)
        
        self.play(FadeIn(alice), FadeIn(bob), Create(channel))
        self.play(FadeIn(eve), Write(eve_label))
        
        # 演示困境：传输钥匙
        key = Text("🔑", font_size=48).move_to(alice)
        self.play(FadeIn(key))
        
        # 钥匙移动
        self.play(key.animate.move_to(ORIGIN), run_time=1.5)
        
        # Eve 拦截
        self.play(eve.animate.scale(1.2), color=IT_RED)
        alert = Text("拦截成功！", font_size=24, color=IT_RED).next_to(eve, DOWN)
        self.play(Write(alert))
        self.wait(1)
        
        # 撤回
        self.play(
            FadeOut(key), FadeOut(alert), 
            eve.animate.scale(1/1.2).set_color(IT_PURPLE)
        )
        
        # 核心问题
        question = Text("如何在不直接传递钥匙的情况下，\n让双方拥有同一把钥匙？", font_size=32, color=IT_YELLOW).move_to(DOWN * 2.5)
        self.play(Write(question))
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))

    def create_avatar(self, name, color):
        """创建简单的人物图标"""
        body = Circle(radius=0.6, color=color, fill_opacity=0.3)
        label = Text(name, font_size=24, color=color).next_to(body, DOWN)
        return VGroup(body, label)

    def color_exchange_demo(self):
        """核心：颜色混合隐喻"""
        
        title = Text("颜色的魔法", font_size=36, color=IT_YELLOW).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # 布局
        LEFT_ZONE = LEFT * 4.5
        RIGHT_ZONE = RIGHT * 4.5
        CENTER_ZONE = ORIGIN
        
        # 人物标签 (固定不动)
        alice_label = Text("Alice", font_size=24, color=IT_BLUE).move_to(LEFT_ZONE + UP * 2.5)
        bob_label = Text("Bob", font_size=24, color=IT_RED).move_to(RIGHT_ZONE + UP * 2.5)
        eve_label = Text("Eve (可以看到交换过程)", font_size=20, color=IT_PURPLE).move_to(UP * 2.5)
        
        self.play(Write(alice_label), Write(bob_label), Write(eve_label))
        
        # --- 步骤 1: 公共颜色 ---
        step_text = Text("1. 公共颜色 (公开)", font_size=24).to_edge(DOWN, buff=1.5)
        self.play(Write(step_text))
        
        # 生成公共色桶
        bucket_pub = self.create_bucket(IT_YELLOW, "公共")
        self.play(FadeIn(bucket_pub))
        
        # 分发给 Alice 和 Bob
        bucket_a_pub = bucket_pub.copy()
        bucket_b_pub = bucket_pub.copy()
        
        self.play(
            bucket_a_pub.animate.move_to(LEFT_ZONE),
            bucket_b_pub.animate.move_to(RIGHT_ZONE),
            run_time=1.5
        )
        self.play(FadeOut(bucket_pub))
        
        # --- 步骤 2: 加入私有颜色 ---
        self.play(Transform(step_text, Text("2. 混合私有颜色 (保密)", font_size=24, color=IT_BLUE).to_edge(DOWN, buff=1.5)))
        
        # 私钥
        priv_a = self.create_bucket(IT_BLUE, "私密").next_to(bucket_a_pub, UP)
        priv_b = self.create_bucket(IT_RED, "私密").next_to(bucket_b_pub, UP)
        
        self.play(FadeIn(priv_a), FadeIn(priv_b))
        self.wait(0.5)
        
        # 混合动画：两个桶合并成一个新的混合桶
        mix_a = self.create_bucket(IT_GREEN, "混合A").move_to(bucket_a_pub) # 黄+蓝=绿
        mix_b = self.create_bucket(IT_ORANGE, "混合B").move_to(bucket_b_pub) # 黄+红=橙
        
        self.play(
            ReplacementTransform(VGroup(bucket_a_pub, priv_a), mix_a),
            ReplacementTransform(VGroup(bucket_b_pub, priv_b), mix_b)
        )
        
        # --- 步骤 3: 交换混合色 ---
        self.play(Transform(step_text, Text("3. 交换混合色 (公开)", font_size=24, color=IT_YELLOW).to_edge(DOWN, buff=1.5)))
        
        # 路径经过中间 Eve
        self.play(
            mix_a.animate.move_to(CENTER_ZONE + LEFT * 1.5),
            mix_b.animate.move_to(CENTER_ZONE + RIGHT * 1.5),
        )
        
        # Eve 困惑
        eve_thought = Text("只有混合色...\n无法分离出私钥", font_size=20, color=IT_PURPLE).next_to(eve_label, DOWN)
        self.play(FadeIn(eve_thought))
        self.wait(1)
        self.play(FadeOut(eve_thought))
        
        # 完成交换
        self.play(
            mix_a.animate.move_to(RIGHT_ZONE), # A的给B
            mix_b.animate.move_to(LEFT_ZONE),  # B的给A
        )
        
        # --- 步骤 4: 再次混合私有色 ---
        self.play(Transform(step_text, Text("4. 再次加入自己的私有色", font_size=24, color=IT_BROWN).to_edge(DOWN, buff=1.5)))
        
        # 再次显示私有色 (注意：私钥从未离开过各自的手)
        priv_a_2 = self.create_bucket(IT_BLUE, "私密").next_to(mix_b, UP) 
        priv_b_2 = self.create_bucket(IT_RED, "私密").next_to(mix_a, UP)
        
        self.play(FadeIn(priv_a_2), FadeIn(priv_b_2))
        
        # 最终混合
        final_a = self.create_bucket(IT_BROWN, "密钥").move_to(mix_b)
        final_b = self.create_bucket(IT_BROWN, "密钥").move_to(mix_a)
        
        self.play(
            ReplacementTransform(VGroup(mix_b, priv_a_2), final_a),
            ReplacementTransform(VGroup(mix_a, priv_b_2), final_b)
        )
        
        # 成功提示
        success = Text("共享密钥建立成功！", font_size=32, color=IT_GREEN, weight=BOLD).next_to(step_text, UP, buff=0.5)
        self.play(Write(success))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def create_bucket(self, color, label_text):
        """创建颜料桶图标"""
        bucket = VGroup(
            # 桶身
            Rectangle(width=1.2, height=1.5, fill_color=color, fill_opacity=1, color=WHITE, stroke_width=2),
            # 标签
            Text(label_text, font_size=20, color=BLACK if color in [IT_YELLOW, IT_GREEN] else WHITE).move_to(ORIGIN)
        )
        bucket[1].move_to(bucket[0])
        return bucket

    def math_behind_magic(self):
        """数学原理：离散对数"""
        
        title = Text("数学本质：单向函数", font_size=36, color=IT_BLUE).to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # 布局
        LEFT_ZONE = LEFT * 3.5
        RIGHT_ZONE = RIGHT * 3.5
        
        # 左侧：易 (混合)
        # g^a mod p
        easy_group = VGroup(
            Text("正向计算 (混合)", font_size=24, color=IT_GREEN),
            Text("g ^ a mod p", font_size=36, font="Consolas"),
            Text("Easy", font_size=32, color=IT_GREEN, weight=BOLD)
        ).arrange(DOWN, buff=0.3).move_to(LEFT_ZONE)
        
        # 右侧：难 (分离)
        # log_g(Y)
        hard_group = VGroup(
            Text("逆向计算 (分离)", font_size=24, color=IT_RED),
            Text("log_g(Y) mod p", font_size=36, font="Consolas"),
            Text("Hard", font_size=32, color=IT_RED, weight=BOLD)
        ).arrange(DOWN, buff=0.3).move_to(RIGHT_ZONE)
        
        # 中间箭头
        arrow = Arrow(LEFT_ZONE, RIGHT_ZONE, color=IT_GRAY)
        
        self.play(Write(easy_group))
        self.wait(0.5)
        self.play(Create(arrow))
        self.play(Write(hard_group))
        
        # 解释
        expl = VGroup(
            Text("这就是“离散对数问题”", font_size=28, color=IT_YELLOW),
            Text("混合颜料很容易 (乘方)", font_size=24),
            Text("把混合色还原成原色极难 (对数)", font_size=24, color=IT_RED)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)
        
        self.play(Write(expl))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_philosophy(self):
        """哲学升华"""
        
        title = Text("信任的悖论", font_size=40, color=IT_PURPLE).to_edge(UP, buff=1.5)
        
        lines = VGroup(
            Text("我们生活在一个零信任的网络中", font_size=28, color=WHITE),
            Text("公钥密码学告诉我们：", font_size=28, color=WHITE),
            Text("即使在众目睽睽之下", font_size=32, color=IT_RED),
            Text("依然可以建立私密的连接", font_size=32, color=IT_GREEN),
            Text("有些秘密，是可以公开交换的", font_size=36, color=IT_YELLOW, weight=BOLD)
        ).arrange(DOWN, buff=0.6)
        
        lines.next_to(title, DOWN, buff=0.8)
        
        self.play(Write(title))
        
        for line in lines:
            self.play(FadeIn(line, shift=UP), run_time=1.2)
            self.wait(0.5)
            
        self.wait(2)
        self.play(FadeOut(title), FadeOut(lines))
        
        # 预告
        next_ep = Text("下期预告：零知识证明", font_size=40, color=IT_BLUE).move_to(UP * 0.5)
        desc = Text("阿里巴巴的洞穴故事。\n如何向你证明我知道秘密，却不告诉你秘密？", font_size=24, color=WHITE).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))