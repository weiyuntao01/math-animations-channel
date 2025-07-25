#!/usr/bin/env python
"""
视频缩略图生成工具
为抖音、视频号等平台生成吸引人的封面图
"""

import os
import sys
from pathlib import Path
import argparse
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 添加项目根目录到Python路径
sys.path.append(str(Path(__file__).parent.parent))

from manim import *

class ThumbnailGenerator:
    def __init__(self):
        self.templates = {
            "standard": {
                "size": (1920, 1080),
                "title_size": 120,
                "subtitle_size": 60
            },
            "vertical": {
                "size": (1080, 1920),
                "title_size": 100,
                "subtitle_size": 50
            },
            "square": {
                "size": (1080, 1080),
                "title_size": 100,
                "subtitle_size": 50
            }
        }
        
        # 项目标准色
        self.colors = {
            "gold": "#FFD700",
            "blue": "#3B82F6",
            "green": "#10B981",
            "purple": "#8B5CF6",
            "orange": "#F59E0B",
            "red": "#EF4444"
        }
    
    def create_thumbnail_scene(self, episode_num, title, subtitle, template="standard"):
        """创建缩略图场景"""
        config = self.templates[template]
        width, height = config["size"]
        
        class ThumbnailScene(Scene):
            def __init__(self):
                super().__init__()
                # 设置画布大小
                self.camera.frame_width = width / 100
                self.camera.frame_height = height / 100
                
            def construct(self):
                # 设置中文字体
                Text.set_default(font="Microsoft YaHei")
                
                # 背景渐变
                bg = Rectangle(
                    width=self.camera.frame_width,
                    height=self.camera.frame_height,
                    fill_opacity=1,
                    stroke_width=0
                )
                bg.set_color_by_gradient(BLUE_E, BLUE_A)
                self.add(bg)
                
                # 根据集数选择主题元素
                if episode_num == 1:
                    # 向日葵螺旋
                    self.add_sunflower_pattern()
                elif episode_num == 2:
                    # 斐波那契数列
                    self.add_fibonacci_pattern()
                elif episode_num == 3:
                    # 鹦鹉螺螺线
                    self.add_nautilus_pattern()
                elif episode_num == 4:
                    # 黄金矩形
                    self.add_golden_rectangle()
                
                # 添加标题
                title_text = Text(
                    title,
                    font_size=config["title_size"] * 0.8,
                    color=GOLD,
                    weight=BOLD
                )
                
                if template == "vertical":
                    title_text.shift(UP * 3)
                else:
                    title_text.shift(UP * 1.5)
                
                # 添加副标题
                subtitle_text = Text(
                    subtitle,
                    font_size=config["subtitle_size"] * 0.8,
                    color=WHITE
                )
                subtitle_text.next_to(title_text, DOWN, buff=0.5)
                
                # 添加集数标记
                episode_mark = Text(
                    f"EP{episode_num:02d}",
                    font_size=80,
                    color=YELLOW,
                    weight=BOLD
                )
                
                if template == "vertical":
                    episode_mark.to_corner(UL, buff=0.5)
                else:
                    episode_mark.to_corner(UR, buff=0.5)
                
                # 添加品牌标识
                brand = Text(
                    "数学之美",
                    font_size=40,
                    color=WHITE
                )
                brand.to_corner(DR, buff=0.5)
                
                self.add(title_text, subtitle_text, episode_mark, brand)
                
                # 添加装饰元素
                self.add_decorations(template)
            
            def add_sunflower_pattern(self):
                """添加向日葵图案"""
                golden_angle = 137.5 * DEGREES
                n_seeds = 200
                scale = 0.05
                
                seeds = VGroup()
                for i in range(1, n_seeds + 1):
                    angle = i * golden_angle
                    radius = scale * np.sqrt(i)
                    
                    x = radius * np.cos(angle)
                    y = radius * np.sin(angle)
                    
                    seed = Dot(
                        [x, y, 0],
                        radius=0.02,
                        color=YELLOW if i % 21 == 0 else GOLD_E,
                        fill_opacity=0.8
                    )
                    seeds.add(seed)
                
                seeds.shift(DOWN * 1.5)
                self.add(seeds)
            
            def add_fibonacci_pattern(self):
                """添加斐波那契数列图案"""
                fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21]
                
                # 创建斐波那契矩形
                rectangles = VGroup()
                colors = [BLUE_B, BLUE_C, BLUE_D, BLUE_E, GREEN_B, GREEN_C, GREEN_D, GREEN_E]
                
                x, y = 0, 0
                for i, (num, color) in enumerate(zip(fib_numbers[:6], colors)):
                    size = num * 0.3
                    rect = Square(
                        side_length=size,
                        color=color,
                        fill_opacity=0.6,
                        stroke_width=3
                    )
                    
                    if i == 0:
                        rect.move_to([x, y, 0])
                    elif i == 1:
                        rect.move_to([x + size/2, y, 0])
                        x += size
                    elif i % 2 == 0:
                        rect.move_to([x, y - size/2, 0])
                        y -= size
                    else:
                        rect.move_to([x - size/2, y, 0])
                        x -= size
                    
                    rectangles.add(rect)
                
                rectangles.move_to(ORIGIN).shift(DOWN * 1.5)
                self.add(rectangles)
            
            def add_nautilus_pattern(self):
                """添加鹦鹉螺螺线图案"""
                # 创建对数螺线
                t = np.linspace(0, 4 * PI, 1000)
                a = 0.1
                b = 0.2
                
                spiral = ParametricFunction(
                    lambda t: np.array([
                        a * np.exp(b * t) * np.cos(t),
                        a * np.exp(b * t) * np.sin(t),
                        0
                    ]),
                    t_range=[0, 4 * PI],
                    color=GOLD,
                    stroke_width=4
                )
                
                spiral.shift(DOWN * 1.5)
                self.add(spiral)
            
            def add_golden_rectangle(self):
                """添加黄金矩形图案"""
                # 创建黄金矩形序列
                phi = (1 + np.sqrt(5)) / 2
                
                rect1 = Rectangle(
                    width=2,
                    height=2/phi,
                    color=GOLD,
                    fill_opacity=0.3,
                    stroke_width=3
                )
                
                rect2 = Rectangle(
                    width=2/phi,
                    height=2/phi,
                    color=GOLD_E,
                    fill_opacity=0.3,
                    stroke_width=3
                )
                rect2.next_to(rect1, LEFT, buff=0)
                
                golden_rects = VGroup(rect1, rect2)
                golden_rects.move_to(ORIGIN).shift(DOWN * 1.5)
                self.add(golden_rects)
            
            def add_decorations(self, template):
                """添加装饰元素"""
                # 添加数学符号装饰
                symbols = ["∞", "π", "φ", "∑", "∫"]
                decorations = VGroup()
                
                for i, symbol in enumerate(symbols):
                    sym = Text(
                        symbol,
                        font_size=30,
                        color=WHITE,
                        fill_opacity=0.3
                    )
                    
                    if template == "vertical":
                        angle = i * TAU / len(symbols)
                        sym.move_to(4 * np.array([np.cos(angle), np.sin(angle), 0]))
                    else:
                        sym.move_to(
                            np.array([
                                -4 + i * 2,
                                -3,
                                0
                            ])
                        )
                    
                    decorations.add(sym)
                
                self.add(decorations)
        
        return ThumbnailScene()
    
    def generate_thumbnail(self, episode_num, title, subtitle, output_path, template="standard"):
        """生成缩略图"""
        print(f"生成缩略图: EP{episode_num:02d} - {title}")
        
        # 创建场景
        scene = self.create_thumbnail_scene(episode_num, title, subtitle, template)
        
        # 配置渲染参数
        config.frame_rate = 1
        config.pixel_width = self.templates[template]["size"][0]
        config.pixel_height = self.templates[template]["size"][1]
        
        # 渲染场景为图片
        scene.renderer.camera.capture()
        
        # 确保输出目录存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # 保存图片
        scene.renderer.camera.save_image(output_path)
        
        print(f"✅ 缩略图已保存至: {output_path}")

def generate_all_thumbnails():
    """生成所有集数的缩略图"""
    generator = ThumbnailGenerator()
    
    episodes = [
        {
            "num": 1,
            "title": "向日葵中的螺旋密码",
            "subtitle": "斐波那契数列与黄金角"
        },
        {
            "num": 2,
            "title": "斐波那契与兔子问题",
            "subtitle": "数列的起源故事"
        },
        {
            "num": 3,
            "title": "鹦鹉螺中的等角螺线",
            "subtitle": "自然界最优美的曲线"
        },
        {
            "num": 4,
            "title": "黄金矩形与艺术构图",
            "subtitle": "美的数学原理"
        },
        {
            "num": 5,
            "title": "人体比例中的1.618",
            "subtitle": "理想美的数学密码"
        },
        {
            "num": 6,
            "title": "音乐和弦中的数学",
            "subtitle": "和谐之声的频率比"
        },
        {
            "num": 7,
            "title": "建筑设计的数学美学",
            "subtitle": "从帕特农到现代建筑"
        },
        {
            "num": 8,
            "title": "股市中的斐波那契",
            "subtitle": "技术分析的数学基础"
        }
    ]
    
    # 为每个平台生成不同尺寸的缩略图
    templates = ["standard", "vertical", "square"]
    
    for episode in episodes:
        for template in templates:
            output_dir = f"output/thumbnails/{template}"
            output_path = f"{output_dir}/EP{episode['num']:02d}_{episode['title']}.png"
            
            try:
                generator.generate_thumbnail(
                    episode["num"],
                    episode["title"],
                    episode["subtitle"],
                    output_path,
                    template
                )
            except Exception as e:
                print(f"❌ 生成失败: {e}")

def main():
    parser = argparse.ArgumentParser(description="生成视频缩略图")
    parser.add_argument(
        "--episode", "-e",
        type=int,
        help="集数"
    )
    parser.add_argument(
        "--title", "-t",
        help="标题"
    )
    parser.add_argument(
        "--subtitle", "-s",
        help="副标题"
    )
    parser.add_argument(
        "--template",
        choices=["standard", "vertical", "square"],
        default="standard",
        help="模板类型"
    )
    parser.add_argument(
        "--output", "-o",
        help="输出路径"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="生成所有集数的缩略图"
    )
    
    args = parser.parse_args()
    
    if args.all:
        generate_all_thumbnails()
    else:
        if not all([args.episode, args.title]):
            print("❌ 请提供 --episode 和 --title 参数")
            sys.exit(1)
        
        generator = ThumbnailGenerator()
        output_path = args.output or f"output/thumbnails/EP{args.episode:02d}.png"
        
        generator.generate_thumbnail(
            args.episode,
            args.title,
            args.subtitle or "",
            output_path,
            args.template
        )

if __name__ == "__main__":
    main() 