"""
INF_EP01: 希尔伯特旅馆 (Hilbert's Hotel)
当无穷大的旅馆客满时，还能住进新客人吗？
"""

from manim import *
import numpy as np

# --- 颜色定义 (新系列主题色：深邃的太空紫/金) ---
INF_PURPLE = "#7C3AED"   # 神秘紫
INF_GOLD = "#FBBF24"     # 无穷金
INF_BLUE = "#3B82F6"     # 客人A
INF_RED = "#EF4444"      # 客人B/新客人
INF_GREEN = "#10B981"    # 解决方案
INF_GRAY = "#6B7280"     # 房间/背景
BG_COLOR = "#0F172A"     # 深蓝灰背景 (更有深渊感)

class InfinityEP01(Scene):
    """无穷系列 EP01：希尔伯特旅馆"""
    
    def construct(self):
        # 0. 全局设置
        Text.set_default(font="Microsoft YaHei")
        self.camera.background_color = BG_COLOR
        
        # 1. 开场：新系列Logo
        self.intro_new_series()
        
        # 2. 场景构建：无限旅馆
        # 返回 hotel_group, rooms (list of objects)
        hotel_group, rooms = self.setup_hotel()
        
        # 3. 悖论一：来了一位新客人 (n -> n+1)
        self.scenario_one_guest(rooms)
        
        # 4. 悖论二：来了无穷多客人 (n -> 2n)
        self.scenario_infinite_bus(rooms)
        
        # 5. 数学本质：基数
        self.explain_cardinality()
        
        # 6. 结尾
        self.show_ending()

    def intro_new_series(self):
        # 系列标题动画
        series_title = Text("无穷与悖论", font_size=60, color=INF_PURPLE, weight=BOLD)
        subtitle = Text("EP01: 希尔伯特旅馆", font_size=32, color=INF_GOLD).next_to(series_title, DOWN, buff=0.5)
        
        self.play(DrawBorderThenFill(series_title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)
        
        # 核心问题
        question = Text("假如一家旅馆有无穷多个房间，且都住满了...", font_size=24, color=WHITE).next_to(subtitle, DOWN, buff=1.0)
        self.play(Write(question))
        self.wait(2)
        
        self.play(FadeOut(series_title), FadeOut(subtitle), FadeOut(question))

    def setup_hotel(self):
        """构建无限旅馆的视觉模型"""
        
        title = Text("希尔伯特旅馆", font_size=36, color=INF_GOLD).to_edge(UP, buff=0.5)
        self.play(Write(title))
        
        # 定义房间参数
        room_width = 1.2
        room_height = 1.8
        start_x = -5.0
        
        rooms = []
        guests = []
        labels = []
        
        # 创建显示在屏幕上的前6个房间 + 省略号
        display_count = 6
        
        hotel_group = VGroup()
        
        for i in range(display_count):
            # 房间框
            room = Rectangle(width=room_width, height=room_height, color=WHITE, stroke_width=2)
            pos = np.array([start_x + i * (room_width + 0.2), 0, 0])
            room.move_to(pos)
            
            # 门牌号
            label = Integer(i + 1, font_size=24, color=INF_GOLD).next_to(room, UP, buff=0.1)
            
            # 客人 (老住户)
            guest = self.create_guest(INF_BLUE).move_to(pos + DOWN * 0.2)
            
            rooms.append(room)
            labels.append(label)
            guests.append(guest)
            
            hotel_group.add(room, label, guest)
            
            # 逐个出现
            self.play(Create(room), Write(label), FadeIn(guest), run_time=0.2)
            
        # 省略号
        dots = Text("...", font_size=48, color=WHITE).next_to(rooms[-1], RIGHT, buff=0.5)
        hotel_group.add(dots)
        self.play(Write(dots))
        
        # 状态描述
        status = Text("状态：客满 (Full)", font_size=28, color=INF_RED).next_to(hotel_group, DOWN, buff=1.0)
        self.play(Write(status))
        self.wait(1)
        
        self.status_text = status # 保存引用方便修改
        
        # 将所有动态对象打包返回，方便后续操作
        # rooms_data 包含：[room_bg, number, guest_obj] 的列表
        rooms_data = []
        for i in range(display_count):
            rooms_data.append({
                "room": rooms[i],
                "label": labels[i],
                "guest": guests[i],
                "index": i + 1 # 房间号
            })
            
        return hotel_group, rooms_data

    def create_guest(self, color):
        """创建一个简单的客人图标"""
        head = Circle(radius=0.15, color=color, fill_opacity=1)
        body = Line(DOWN*0.15, DOWN*0.6, color=color, stroke_width=4).next_to(head, DOWN, buff=0)
        arms = Line(LEFT*0.3, RIGHT*0.3, color=color, stroke_width=4).move_to(body.get_center() + UP*0.1)
        legs = VGroup(
            Line(body.get_end(), body.get_end() + DOWN*0.3 + LEFT*0.2, color=color, stroke_width=4),
            Line(body.get_end(), body.get_end() + DOWN*0.3 + RIGHT*0.2, color=color, stroke_width=4)
        )
        return VGroup(head, body, arms, legs)

    def scenario_one_guest(self, rooms_data):
        """场景一：来了一位新客人"""
        
        # 1. 新客人出现
        new_guest = self.create_guest(INF_RED).move_to(LEFT * 6 + DOWN * 2)
        new_guest_label = Text("新客人", font_size=20, color=INF_RED).next_to(new_guest, DOWN)
        
        self.play(FadeIn(new_guest), Write(new_guest_label))
        
        problem_text = Text("没房间了怎么办？", font_size=24, color=INF_GOLD).next_to(self.status_text, DOWN)
        self.play(Write(problem_text))
        self.wait(1)
        
        # 2. 解决方案：全体右移
        solution_text = Text("广播：所有客人请移动到 N+1 号房", font_size=28, color=INF_GREEN)
        solution_text.move_to(UP * 2.5) # 放在顶部
        
        self.play(Write(solution_text))
        
        # 动画：所有现有客人向右移动一个身位
        # 计算移动距离：一个房间宽度 + 间距
        move_vec = RIGHT * (1.2 + 0.2) 
        
        anims = []
        for item in rooms_data:
            guest = item["guest"]
            # 移动动画
            anims.append(guest.animate.shift(move_vec))
            
        self.play(*anims, run_time=1.5)
        
        # 3. 1号房空出来了
        # 将原1号房的客人引用更新（其实视觉上已经移走了，这里只是为了逻辑闭环）
        # 视觉上：原1号房现在空了
        
        empty_highlight = SurroundingRectangle(rooms_data[0]["room"], color=INF_GREEN, stroke_width=4)
        empty_text = Text("1号房空缺", font_size=20, color=INF_GREEN).next_to(empty_highlight, DOWN)
        
        self.play(Create(empty_highlight), FadeOut(self.status_text)) # 移除"客满"
        self.play(Write(empty_text))
        
        # 4. 新客人入住
        target_pos = rooms_data[0]["room"].get_center() + DOWN * 0.2
        self.play(
            new_guest.animate.move_to(target_pos),
            FadeOut(new_guest_label),
            FadeOut(problem_text)
        )
        
        # 5. 结论
        math_text = MathTex(r"\infty + 1 = \infty", color=INF_PURPLE, font_size=48)
        math_text.move_to(DOWN * 2.5)
        self.play(Write(math_text))
        
        self.wait(2)
        
        # 清理本场景增加的元素，恢复初始状态（为了演示下一个场景）
        # 把新客人移走，把老客人移回去
        self.play(
            FadeOut(math_text), FadeOut(solution_text), FadeOut(empty_highlight), FadeOut(empty_text),
            FadeOut(new_guest)
        )
        
        # 复原老客人位置
        reset_anims = []
        for item in rooms_data:
            reset_anims.append(item["guest"].animate.shift(-move_vec))
        self.play(*reset_anims, run_time=1.0)
        self.wait(1)

    def scenario_infinite_bus(self, rooms_data):
            """场景二：来了无穷多客人（无限巴士） - 修复重叠版"""
            
            # 1. 无限巴士出现
            bus = Rectangle(width=6, height=1.5, color=INF_RED, fill_opacity=0.2).move_to(DOWN * 2.5)
            bus_text = Text("无限巴士 (Infinite Bus)", font_size=24, color=INF_RED).move_to(bus.get_center())
            
            # 巴士里的客人 (示意)
            bus_guests = VGroup()
            for i in range(5):
                g = self.create_guest(INF_RED).scale(0.6).move_to(bus.get_left() + RIGHT * (0.8 + i*0.8))
                bus_guests.add(g)
            bus_dots = Text("...", font_size=36, color=INF_RED).next_to(bus_guests, RIGHT)
            
            bus_group = VGroup(bus, bus_text, bus_guests, bus_dots)
            
            self.play(FadeIn(bus_group, shift=UP))
            
            challenge = Text("无穷多新客人怎么办？", font_size=24, color=INF_GOLD).next_to(bus_group, UP)
            self.play(Write(challenge))
            self.wait(1)
            
            # 2. 解决方案：N -> 2N
            solution_text = Text("广播：请移动到 2N 号房 (房间号 x 2)", font_size=28, color=INF_GREEN)
            solution_text.move_to(UP * 2.5)
            
            self.play(Write(solution_text))
            
            # 3. 动画：客人移动 (现有客人右移)
            unit_vec = RIGHT * (1.2 + 0.2) # 一格的距离
            anims = []
            
            for i, item in enumerate(rooms_data):
                current_room_num = i + 1
                target_room_num = current_room_num * 2
                move_steps = target_room_num - current_room_num
                
                # 如果目标位置还在屏幕内，就移动；否则淡出
                if target_room_num <= 6:
                    anims.append(item["guest"].animate.shift(unit_vec * move_steps))
                else:
                    anims.append(FadeOut(item["guest"], shift=RIGHT))
            
            self.play(*anims, run_time=2.0)
            
            # 4. 奇数房间空出来了
            # 高亮 1, 3, 5 号房 (对应索引 0, 2, 4)
            highlights = VGroup()
            for i in [0, 2, 4]: 
                rect = SurroundingRectangle(rooms_data[i]["room"], color=INF_GREEN, stroke_width=3)
                highlights.add(rect)
                
            empty_text = Text("奇数房间全部腾空！", font_size=24, color=INF_GREEN).next_to(highlights, DOWN, buff=0.5)
            
            self.play(Create(highlights), Write(empty_text))
            self.wait(1)
            
            # --- 关键修复开始 ---
            
            # 5. 巴士客人入住
            # 我们有5个巴士客人，但屏幕上只有3个空房 (1,3,5)
            # 前3个客人入住，剩下的客人随巴士一起消失
            
            new_guests_anim = []
            target_rooms = [0, 2, 4] # 房间索引
            
            # 剩下的多余客人，需要单独收集起来FadeOut
            remaining_guests = VGroup()
            
            for i, g in enumerate(bus_guests):
                if i < len(target_rooms):
                    # 前3个客人：移动到房间
                    room_idx = target_rooms[i]
                    target = rooms_data[room_idx]["room"].get_center() + DOWN * 0.2
                    # 恢复大小并移动
                    new_guests_anim.append(g.animate.scale(1/0.6).move_to(target))
                else:
                    # 剩下的客人：加入待清理组
                    remaining_guests.add(g)
            
            # 先清理掉高亮框和文字，让画面干净一点
            self.play(FadeOut(highlights), FadeOut(empty_text), run_time=0.5)
            
            # 执行入住动画，同时清理巴士、文字和多余的客人
            self.play(
                *new_guests_anim, 
                FadeOut(bus), 
                FadeOut(bus_text), 
                FadeOut(bus_dots), 
                FadeOut(challenge),
                FadeOut(remaining_guests), # <--- 彻底清除多余小人
                run_time=1.5
            )
            
            # 6. 结论 (现在背景干净了)
            math_text = MathTex(r"\infty + \infty = \infty", color=INF_PURPLE, font_size=48)
            math_text.move_to(DOWN * 2.5) # 这个位置之前被巴士占了
            self.play(Write(math_text))
            
            # --- 关键修复结束 ---
            
            self.wait(2)
            self.play(FadeOut(Group(*self.mobjects)))

    def explain_cardinality(self):
        """数学解释：基数"""
        title = Text("这不科学？不，这很数学！", font_size=36, color=INF_GOLD).to_edge(UP)
        self.play(Write(title))
        
        # 定义
        def_text = VGroup(
            Text("康托尔 (Georg Cantor) 定义：", font_size=24, color=INF_PURPLE),
            Text("如果两个集合之间存在一一对应关系，", font_size=24),
            Text("它们的大小（基数）就是相等的。", font_size=24, color=INF_GREEN)
        ).arrange(DOWN, buff=0.3)
        
        self.play(Write(def_text))
        self.wait(1)
        
        # 映射演示
        # N: 1, 2, 3, 4 ...
        # E: 2, 4, 6, 8 ...
        
        mapping = VGroup()
        
        rows = 5
        for i in range(1, rows + 1):
            n_tex = MathTex(str(i), color=INF_BLUE)
            arrow = Arrow(LEFT, RIGHT, buff=0.2, color=WHITE)
            e_tex = MathTex(str(i*2), color=INF_RED)
            
            row = VGroup(n_tex, arrow, e_tex).arrange(RIGHT, buff=0.5)
            mapping.add(row)
            
        mapping.arrange(DOWN, buff=0.3).move_to(DOWN * 1.5)
        
        label_n = Text("自然数 (N)", font_size=24, color=INF_BLUE).next_to(mapping, LEFT, buff=1.0)
        label_e = Text("偶数 (E)", font_size=24, color=INF_RED).next_to(mapping, RIGHT, buff=1.0)
        
        self.play(
            def_text.animate.shift(UP * 1.0),
            Write(mapping),
            Write(label_n),
            Write(label_e)
        )
        
        conclusion = Text("整体等于局部，这是无穷的特性！", font_size=32, color=INF_GOLD, weight=BOLD)
        conclusion.to_edge(DOWN, buff=0.5)
        self.play(Write(conclusion))
        
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))

    def show_ending(self):
        summary = VGroup(
            Text("1. 无穷不是一个\"很大的数字\"，而是一种状态", font_size=26),
            Text("2. 所有的可数无穷(Countable Infinity)都一样大", font_size=26),
            Text("3. 希尔伯特旅馆永不客满", font_size=26, color=INF_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        self.play(Write(summary))
        self.wait(2)
        self.play(FadeOut(summary))
        
        # 预告
        next_ep = Text("下期预告：芝诺悖论", font_size=40, color=INF_GOLD)
        desc = Text("阿喀琉斯为什么追不上乌龟？\n时间和空间是连续的吗？", font_size=24, color=INF_GRAY).next_to(next_ep, DOWN)
        
        self.play(Write(next_ep))
        self.play(Write(desc))
        self.wait(3)