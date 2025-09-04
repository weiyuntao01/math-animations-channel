"""
Unified Mathematical Dragon Animation
统一连贯的数学龙动画
"""

from manim import *
import numpy as np
from typing import List, Tuple, Optional

# ============= 配色方案 =============
class DragonColors:
    """龙的配色系统"""
    GOLD = ManimColor("#FFD700")       # 龙金
    RED = ManimColor("#FF4444")        # 龙红  
    CYAN = ManimColor("#00FFE5")       # 青龙
    PURPLE = ManimColor("#9B59B6")     # 紫龙
    GREEN = ManimColor("#00FF88")      # 龙绿
    WHITE = ManimColor("#FFFFFF")      # 纯白
    BLACK = ManimColor("#0A0A0A")      # 墨黑
    ORANGE = ManimColor("#FF8800")     # 橙色

# ============= 统一的龙类 =============
class UnifiedDragon(VGroup):
    """统一的龙对象 - 确保所有部件连贯"""
    
    def __init__(self, time: float = 0, **kwargs):
        super().__init__(**kwargs)
        self.time = time
        self.num_segments = 100  # 龙身段数
        self.create_dragon()
    
    def get_dragon_spine(self, t: float) -> List[np.ndarray]:
        """获取龙的脊柱曲线 - 这是龙的核心路径"""
        spine_points = []
        
        for i in range(self.num_segments + 1):
            s = i / self.num_segments  # 0到1的参数
            
            # 基础S形曲线 - 使用参数方程
            # x轴：从左到右
            x = -5 + s * 10
            
            # y轴：蛇形波动，振幅从头到尾递减
            amplitude = 1.5 * (1 - s * 0.3)  # 头部振幅大，尾部小
            y = amplitude * np.sin(2 * np.pi * s * 2 - t * 2)
            y += amplitude * 0.3 * np.sin(2 * np.pi * s * 4 - t * 3)
            
            # z轴效果（虽然是2D，但用于创造深度感）
            z = 0.2 * np.sin(2 * np.pi * s * 3 - t * 1.5)
            
            spine_points.append(np.array([x, y + z * 0.3, 0]))
        
        return spine_points
    
    def create_dragon(self):
        """创建完整的龙"""
        self.remove(*self.submobjects)  # 清除之前的内容
        
        # 获取龙的脊柱路径
        spine_points = self.get_dragon_spine(self.time)
        
        # 1. 创建龙身主体（使用连续的路径，而不是分散的点）
        dragon_body = self.create_body_from_spine(spine_points)
        
        # 2. 创建龙头部件（固定在脊柱第一个点）
        head_pos = spine_points[0]
        head_direction = spine_points[1] - spine_points[0]
        head_angle = np.arctan2(head_direction[1], head_direction[0])
        
        dragon_head_parts = self.create_head_parts(head_pos, head_angle)
        
        # 3. 创建龙尾
        tail_pos = spine_points[-1]
        tail_direction = spine_points[-1] - spine_points[-2]
        dragon_tail = self.create_tail(tail_pos, tail_direction)
        
        # 4. 创建龙鳞（沿着脊柱分布）
        dragon_scales = self.create_scales_along_spine(spine_points)
        
        # 添加所有部件
        self.add(dragon_body)
        self.add(dragon_scales)
        self.add(dragon_head_parts)
        self.add(dragon_tail)
    
    def create_body_from_spine(self, spine_points: List[np.ndarray]) -> VGroup:
        """根据脊柱创建龙身 - 使用连续的粗线条"""
        body = VGroup()
        
        # 主体线条 - 使用VMobject创建连续曲线
        main_body = VMobject()
        main_body.set_points_smoothly(spine_points)
        
        # 设置渐变宽度 - 头部粗，尾部细
        for i, point in enumerate(spine_points[:-1]):
            segment_ratio = i / len(spine_points)
            width = 15 * (1 - segment_ratio * 0.7)  # 从15到4.5的宽度变化
            
            # 颜色渐变
            if segment_ratio < 0.2:
                color = interpolate_color(DragonColors.GOLD, DragonColors.RED, segment_ratio * 5)
            elif segment_ratio < 0.7:
                color = interpolate_color(DragonColors.RED, DragonColors.CYAN, (segment_ratio - 0.2) * 2)
            else:
                color = interpolate_color(DragonColors.CYAN, DragonColors.PURPLE, (segment_ratio - 0.7) * 3.33)
            
            # 创建该段
            if i == 0:
                main_body.set_stroke(color=color, width=width, opacity=0.9)
            
        body.add(main_body)
        
        # 添加身体轮廓线（创造立体感）
        for offset in [-0.15, 0.15]:
            outline = VMobject()
            outline_points = []
            for i, point in enumerate(spine_points):
                # 计算法线方向
                if i == 0:
                    tangent = spine_points[1] - spine_points[0]
                elif i == len(spine_points) - 1:
                    tangent = spine_points[-1] - spine_points[-2]
                else:
                    tangent = spine_points[i+1] - spine_points[i-1]
                
                # 法线是切线旋转90度
                normal = np.array([-tangent[1], tangent[0], 0])
                normal = normal / np.linalg.norm(normal)
                
                # 宽度随位置变化
                width_factor = 1 - i / len(spine_points) * 0.5
                outline_points.append(point + normal * offset * width_factor)
            
            outline.set_points_smoothly(outline_points)
            outline.set_stroke(
                color=DragonColors.GOLD,
                width=2,
                opacity=0.4
            )
            body.add(outline)
        
        return body
    
    def create_head_parts(self, head_pos: np.ndarray, head_angle: float) -> VGroup:
        """创建龙头部件 - 包括须、角、眼等"""
        head_parts = VGroup()
        
        # 龙须 - 从头部伸出
        for side in [-1, 1]:
            for i in range(2):
                whisker = VMobject()
                whisker_points = []
                
                for j in range(10):
                    s = j / 10
                    # 须的基础形状
                    x = s * 0.8 * side
                    y = -s * s * 0.3 - i * 0.1
                    
                    # 添加飘动效果
                    x += np.sin(s * 3 + self.time * 3) * 0.05 * side
                    y += np.cos(s * 2 + self.time * 2) * 0.03
                    
                    # 旋转到头部方向
                    rot_x = x * np.cos(head_angle) - y * np.sin(head_angle)
                    rot_y = x * np.sin(head_angle) + y * np.cos(head_angle)
                    
                    whisker_points.append(head_pos + np.array([rot_x, rot_y, 0]))
                
                whisker.set_points_smoothly(whisker_points)
                whisker.set_stroke(
                    color=DragonColors.WHITE,
                    width=3 - i,
                    opacity=0.7
                )
                head_parts.add(whisker)
        
        # 龙角
        for side in [-1, 1]:
            horn = VMobject()
            horn_points = []
            
            for i in range(8):
                s = i / 8
                # 螺旋上升的角
                x = side * 0.15 * (1 - s * 0.3)
                y = 0.2 + s * 0.4
                
                # 旋转到头部方向
                rot_x = x * np.cos(head_angle) - y * np.sin(head_angle)
                rot_y = x * np.sin(head_angle) + y * np.cos(head_angle)
                
                horn_points.append(head_pos + np.array([rot_x, rot_y, 0]))
            
            horn.set_points_smoothly(horn_points)
            horn.set_stroke(
                color=DragonColors.GOLD,
                width=4,
                opacity=0.9
            )
            head_parts.add(horn)
        
        # 龙眼
        for side in [-1, 1]:
            eye_offset = np.array([
                side * 0.1 * np.cos(head_angle + np.pi/2),
                side * 0.1 * np.sin(head_angle + np.pi/2),
                0
            ])
            
            eye = Circle(
                radius=0.06,
                color=DragonColors.ORANGE,
                fill_color=DragonColors.RED,
                fill_opacity=0.8
            )
            eye.move_to(head_pos + eye_offset)
            
            # 瞳孔
            pupil = Dot(
                point=head_pos + eye_offset,
                radius=0.03,
                color=DragonColors.BLACK,
                fill_opacity=1
            )
            
            head_parts.add(eye, pupil)
        
        return head_parts
    
    def create_tail(self, tail_pos: np.ndarray, tail_direction: np.ndarray) -> VGroup:
        """创建龙尾 - 渐细的尾巴"""
        tail_parts = VGroup()
        
        # 尾巴延伸
        tail_extension = VMobject()
        tail_points = []
        
        for i in range(15):
            s = i / 15
            # 尾巴逐渐变细并弯曲
            extension = tail_direction * s * 0.5
            curve = np.array([
                np.sin(s * np.pi) * 0.3,
                -s * 0.2,
                0
            ])
            tail_points.append(tail_pos + extension + curve)
        
        tail_extension.set_points_smoothly(tail_points)
        tail_extension.set_stroke(
            color=DragonColors.PURPLE,
            width=6,  # 固定宽度
            opacity=0.8
        )
        tail_parts.add(tail_extension)
        
        return tail_parts
    
    def create_scales_along_spine(self, spine_points: List[np.ndarray]) -> VGroup:
        """沿脊柱创建龙鳞"""
        scales = VGroup()
        
        # 每隔几个脊柱点放置鳞片
        scale_indices = range(5, len(spine_points) - 10, 3)
        
        for idx in scale_indices:
            point = spine_points[idx]
            
            # 计算该点的切线方向
            if idx < len(spine_points) - 1:
                tangent = spine_points[idx + 1] - spine_points[idx]
            else:
                tangent = spine_points[idx] - spine_points[idx - 1]
            
            # 法线方向
            normal = np.array([-tangent[1], tangent[0], 0])
            normal = normal / np.linalg.norm(normal)
            
            # 在身体两侧创建鳞片
            for side in [-1, 1]:
                scale_pos = point + normal * side * 0.15
                
                # 鳞片大小随位置变化
                scale_size = 0.05 * (1 - idx / len(spine_points) * 0.5)
                
                # 创建菱形鳞片
                scale = RegularPolygon(
                    n=4,
                    radius=scale_size,
                    color=DragonColors.GOLD,
                    fill_opacity=0.6
                )
                scale.move_to(scale_pos)
                
                # 旋转鳞片使其贴合身体
                angle = np.arctan2(tangent[1], tangent[0])
                scale.rotate(angle + np.pi/4)
                
                scales.add(scale)
        
        return scales
    
    def update_time(self, new_time: float):
        """更新时间并重建龙"""
        self.time = new_time
        self.create_dragon()
        return self

# ============= 主场景 =============
class UnifiedDragonScene(Scene):
    """统一龙动画场景"""
    
    def construct(self):
        # 设置背景
        self.camera.background_color = "#0A0A0A"
        
        # 标题
        title = Text(
            "数学之龙",
            font_size=48,
            font="Microsoft YaHei",
            color=DragonColors.GOLD
        )
        subtitle = MathTex(
            r"x(s,t) = s, \quad y(s,t) = A\sin(\omega s - vt)",
            font_size=24,
            color=DragonColors.CYAN
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), Write(subtitle))
        
        # 创建时间追踪器
        t_tracker = ValueTracker(0)
        
        # 创建龙并绑定到时间追踪器
        dragon = UnifiedDragon(time=0)
        dragon.add_updater(lambda d: d.update_time(t_tracker.get_value()))
        
        self.add(dragon)
        
        # 说明文字
        description = Text(
            "一条完整的龙，在数学中游动",
            font_size=22,
            font="Microsoft YaHei",
            color=DragonColors.WHITE
        )
        description.to_edge(DOWN, buff=0.5)
        self.play(Write(description))
        
        # 执行动画
        self.play(
            t_tracker.animate.set_value(4 * PI),
            run_time=20,
            rate_func=linear
        )
        
        self.wait(1)
        
        # 淡出
        dragon.clear_updaters()
        self.play(
            FadeOut(VGroup(title_group, description, dragon)),
            run_time=2
        )

# ============= 飞行的龙 =============
class FlyingDragonScene(Scene):
    """飞行的龙 - 更复杂的运动"""
    
    def construct(self):
        self.camera.background_color = "#050515"
        
        # 创建飞行路径
        self.create_flying_dragon()
    
    def create_flying_dragon(self):
        """创建在空中飞行的龙"""
        
        # 时间和高度追踪器
        t_tracker = ValueTracker(0)
        height_tracker = ValueTracker(0)
        
        class FlyingDragon(UnifiedDragon):
            """飞行的龙 - 重写脊柱函数"""
            
            def __init__(self, time: float = 0, height: float = 0, **kwargs):
                self.height = height
                super().__init__(time, **kwargs)
            
            def get_dragon_spine(self, t: float) -> List[np.ndarray]:
                """飞行路径的脊柱"""
                spine_points = []
                
                for i in range(self.num_segments + 1):
                    s = i / self.num_segments
                    
                    # 螺旋飞行路径
                    angle = s * 4 * np.pi - t
                    radius = 3 * (1 - s * 0.3)
                    
                    x = radius * np.cos(angle)
                    y = self.height + radius * np.sin(angle) * 0.5
                    
                    # 添加起伏
                    y += np.sin(s * 6 * np.pi - t * 2) * 0.3
                    
                    spine_points.append(np.array([x, y, 0]))
                
                return spine_points
            
            def update_flight(self, new_time: float, new_height: float):
                """更新飞行状态"""
                self.time = new_time
                self.height = new_height
                self.create_dragon()
                return self
        
        # 创建飞行的龙
        flying_dragon = FlyingDragon(time=0, height=0)
        flying_dragon.add_updater(
            lambda d: d.update_flight(
                t_tracker.get_value(),
                height_tracker.get_value()
            )
        )
        
        # 标题
        title = Text(
            "龙的飞行轨迹",
            font_size=36,
            font="Microsoft YaHei",
            color=DragonColors.CYAN
        )
        title.to_edge(UP)
        
        self.play(Write(title))
        self.add(flying_dragon)
        
        # 飞行动画
        self.play(
            t_tracker.animate.set_value(2 * PI),
            height_tracker.animate.set_value(1),
            run_time=5,
            rate_func=smooth
        )
        
        self.play(
            t_tracker.animate.set_value(4 * PI),
            height_tracker.animate.set_value(-1),
            run_time=5,
            rate_func=smooth
        )
        
        self.play(
            t_tracker.animate.set_value(6 * PI),
            height_tracker.animate.set_value(0),
            run_time=5,
            rate_func=smooth
        )
        
        self.wait(1)
        
        # 清理
        flying_dragon.clear_updaters()
        self.play(FadeOut(title), FadeOut(flying_dragon))

# ============= 龙的诞生动画 =============
class DragonBirthScene(Scene):
    """龙的诞生 - 从无到有的过程"""
    
    def construct(self):
        self.camera.background_color = "#000000"
        
        self.show_dragon_birth()
    
    def show_dragon_birth(self):
        """展示龙的诞生过程"""
        
        # 开始文字
        intro_text = Text(
            "从一条线开始...",
            font_size=32,
            font="Microsoft YaHei",
            color=DragonColors.WHITE
        )
        self.play(Write(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))
        
        # 第一步：简单的线
        simple_line = VMobject()
        simple_points = [np.array([x, 0, 0]) for x in np.linspace(-5, 5, 20)]
        simple_line.set_points_smoothly(simple_points)
        simple_line.set_stroke(color=DragonColors.WHITE, width=3)
        
        self.play(Create(simple_line))
        self.wait(0.5)
        
        # 第二步：添加波动
        wave_line = VMobject()
        wave_points = []
        for i in range(50):
            x = -5 + i * 10 / 50
            y = np.sin(i / 50 * 4 * np.pi) * 0.8
            wave_points.append(np.array([x, y, 0]))
        wave_line.set_points_smoothly(wave_points)
        wave_line.set_stroke(color=DragonColors.CYAN, width=5)
        
        self.play(Transform(simple_line, wave_line))
        self.wait(0.5)
        
        # 第三步：变成龙
        t_tracker = ValueTracker(0)
        
        # 创建完整的龙
        dragon = UnifiedDragon(time=0)
        dragon.add_updater(lambda d: d.update_time(t_tracker.get_value()))
        
        # 渐变出现
        dragon.set_opacity(0)
        self.add(dragon)
        self.play(
            FadeOut(simple_line),
            dragon.animate.set_opacity(1),
            run_time=2
        )
        
        # 文字
        final_text = Text(
            "龙，诞生了",
            font_size=40,
            font="Microsoft YaHei",
            color=DragonColors.GOLD
        )
        final_text.to_edge(DOWN, buff=1)
        self.play(Write(final_text))
        
        # 让龙游动
        self.play(
            t_tracker.animate.set_value(2 * PI),
            run_time=8,
            rate_func=smooth
        )
        
        self.wait(1)
        
        # 结束
        dragon.clear_updaters()
        self.play(
            FadeOut(dragon),
            FadeOut(final_text),
            run_time=2
        )

# ============= 多条龙的场景 =============
class MultiDragonScene(Scene):
    """多条龙共舞"""
    
    def construct(self):
        self.camera.background_color = "#0A0520"
        
        self.create_dragon_dance()
    
    def create_dragon_dance(self):
        """创建龙群舞蹈"""
        
        title = Text(
            "双龙戏珠",
            font_size=40,
            font="Microsoft YaHei",
            color=DragonColors.GOLD
        )
        title.to_edge(UP)
        self.play(Write(title))
        
        # 时间追踪器
        t_tracker = ValueTracker(0)
        
        # 第一条龙 - 金龙
        class GoldenDragon(UnifiedDragon):
            def get_dragon_spine(self, t: float) -> List[np.ndarray]:
                spine_points = []
                for i in range(self.num_segments + 1):
                    s = i / self.num_segments
                    x = -5 + s * 10
                    y = 1.5 * np.sin(2 * np.pi * s * 2 - t * 2) + 1
                    spine_points.append(np.array([x, y, 0]))
                return spine_points
        
        # 第二条龙 - 青龙
        class CyanDragon(UnifiedDragon):
            def get_dragon_spine(self, t: float) -> List[np.ndarray]:
                spine_points = []
                for i in range(self.num_segments + 1):
                    s = i / self.num_segments
                    x = -5 + s * 10
                    y = 1.5 * np.sin(2 * np.pi * s * 2 - t * 2 + np.pi) - 1
                    spine_points.append(np.array([x, y, 0]))
                return spine_points
            
            def create_body_from_spine(self, spine_points: List[np.ndarray]) -> VGroup:
                body = super().create_body_from_spine(spine_points)
                # 改变颜色为青色系
                for mob in body:
                    if isinstance(mob, VMobject):
                        mob.set_stroke(color=DragonColors.CYAN, opacity=0.9)
                return body
        
        # 创建两条龙
        golden_dragon = GoldenDragon(time=0)
        golden_dragon.add_updater(lambda d: d.update_time(t_tracker.get_value()))
        
        cyan_dragon = CyanDragon(time=0)
        cyan_dragon.add_updater(lambda d: d.update_time(t_tracker.get_value()))
        
        # 创建龙珠
        pearl = Circle(
            radius=0.2,
            color=DragonColors.WHITE,
            fill_color=DragonColors.WHITE,
            fill_opacity=0.9
        )
        pearl.add_updater(
            lambda p: p.move_to([
                3 * np.cos(t_tracker.get_value()),
                3 * np.sin(t_tracker.get_value()),
                0
            ])
        )
        
        # 珠光效果
        pearl_glow = Circle(
            radius=0.3,
            color=DragonColors.WHITE,
            stroke_width=2,
            fill_opacity=0
        )
        pearl_glow.add_updater(
            lambda g: g.move_to(pearl.get_center()).set_stroke(
                opacity=0.3 + 0.2 * np.sin(t_tracker.get_value() * 3)
            )
        )
        
        # 添加所有元素
        self.add(golden_dragon, cyan_dragon, pearl_glow, pearl)
        
        # 动画
        self.play(
            t_tracker.animate.set_value(4 * PI),
            run_time=15,
            rate_func=linear
        )
        
        self.wait(1)
        
        # 清理
        golden_dragon.clear_updaters()
        cyan_dragon.clear_updaters()
        pearl.clear_updaters()
        pearl_glow.clear_updaters()
        
        self.play(
            FadeOut(VGroup(title, golden_dragon, cyan_dragon, pearl, pearl_glow)),
            run_time=2
        )

# ============= 主执行入口 =============
if __name__ == "__main__":
    # 可用场景列表
    scenes = [
        UnifiedDragonScene,      # 基础统一龙
        FlyingDragonScene,       # 飞行的龙
        DragonBirthScene,        # 龙的诞生
        MultiDragonScene,        # 多龙共舞
    ]
    
    print("Available Dragon Scenes:")
    print("=" * 40)
    for i, scene in enumerate(scenes, 1):
        print(f"{i}. {scene.__name__}")
        print(f"   Command: manim -pql dragon.py {scene.__name__}")
    print("=" * 40)
    print("\nExample commands:")
    print("  Preview: manim -pql dragon.py UnifiedDragonScene")
    print("  High Quality: manim -pqh dragon.py UnifiedDragonScene")
    print("  Save as GIF: manim -pql --format=gif dragon.py UnifiedDragonScene")