#!/usr/bin/env python3
"""
简化的缩略图生成脚本
直接使用manim命令行生成PNG格式的缩略图
"""

import os
import subprocess
import argparse
from pathlib import Path

def get_theme_graphics(episode_num):
    """根据集数返回主题图形代码"""
    if episode_num == 1:
        return '''
        # 向日葵螺旋 - 简洁版本
        golden_angle = 137.5 * DEGREES
        center = ORIGIN
        points = []
        
        for i in range(250):
            angle = i * golden_angle
            radius = 0.35 * np.sqrt(i)
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            points.append([x, y, 0])
        
        # 统一金黄色的点
        dots = VGroup(*[Dot(point, radius=0.06, color=GOLD, fill_opacity=0.9) for point in points])
        dots.shift(DOWN * 0.3)
        self.add(dots)
'''
    elif episode_num == 2:
        return '''
        # 斐波那契数列兔子 - 简洁版本
        def create_rabbit(scale_factor=1):
            rabbit_body = Circle(radius=0.4*scale_factor, color=WHITE, fill_opacity=0.9, stroke_width=2, stroke_color=GOLD)
            rabbit_ears = VGroup(
                Ellipse(width=0.2*scale_factor, height=0.4*scale_factor, color=WHITE, fill_opacity=0.9, 
                       stroke_width=2, stroke_color=GOLD).shift(UP*0.3*scale_factor + LEFT*0.15*scale_factor),
                Ellipse(width=0.2*scale_factor, height=0.4*scale_factor, color=WHITE, fill_opacity=0.9,
                       stroke_width=2, stroke_color=GOLD).shift(UP*0.3*scale_factor + RIGHT*0.15*scale_factor)
            )
            eyes = VGroup(
                Dot(LEFT*0.1*scale_factor + UP*0.1*scale_factor, radius=0.04*scale_factor, color=BLACK),
                Dot(RIGHT*0.1*scale_factor + UP*0.1*scale_factor, radius=0.04*scale_factor, color=BLACK)
            )
            return VGroup(rabbit_body, rabbit_ears, eyes)
        
        # 多个兔子排列，统一白色
        rabbits = VGroup()
        scales = [1.0, 0.8, 1.2, 0.9, 1.1, 0.7, 1.0, 0.8]
        
        for i in range(8):
            scale = scales[i % len(scales)]
            r = create_rabbit(scale).shift(RIGHT * (i-3.5) * 1.3)
            rabbits.add(r)
        
        rabbits.shift(DOWN * 0.2)
        self.add(rabbits)
        
        # 斐波那契数列 - 简洁金色
        fib_nums = Text("1, 1, 2, 3, 5, 8, 13, 21...", font_size=30, color=GOLD, weight=BOLD)
        fib_nums.next_to(rabbits, UP, buff=0.6)
        self.add(fib_nums)
'''
    elif episode_num == 3:
        return '''
        # 鹦鹉螺螺线 - 简洁版本
        # 主螺线
        spiral = ParametricFunction(
            lambda t: np.array([
                1.0 * np.exp(0.12 * t) * np.cos(t),
                1.0 * np.exp(0.12 * t) * np.sin(t),
                0
            ]),
            t_range=np.array([0, 3.5*TAU]),
            color=GOLD,
            stroke_width=6
        )
        spiral.shift(DOWN * 0.2)
        self.add(spiral)
        
        # 外壳轮廓
        shell = Circle(radius=2.8, color=WHITE, stroke_width=4, fill_opacity=0)
        shell.shift(DOWN * 0.2)
        self.add(shell)
'''
    else:
        return '''
        # 默认黄金比例图形 - 简洁版本
        phi = (1 + np.sqrt(5)) / 2
        rect1 = Rectangle(width=3.5, height=3.5/phi, color=GOLD, fill_opacity=0.3, stroke_width=4, stroke_color=WHITE)
        rect2 = Rectangle(width=3.5/phi, height=3.5/phi, color=GOLD, fill_opacity=0.3, stroke_width=4, stroke_color=WHITE)
        rect2.next_to(rect1, LEFT, buff=0)
        golden_rects = VGroup(rect1, rect2).shift(DOWN * 0.3)
        self.add(golden_rects)
        
        # 添加黄金比例数字
        phi_text = Text(f"φ = {phi:.3f}", font_size=26, color=GOLD, weight=BOLD)
        phi_text.next_to(golden_rects, UP, buff=0.5)
        self.add(phi_text)
'''

def create_thumbnail_scene_file(episode_num, title, subtitle):
    """为指定集数创建缩略图场景文件"""
    
    content = f'''
from manim import *
import numpy as np

class ThumbnailEP{episode_num:02d}(Scene):
    """EP{episode_num:02d} 缩略图场景"""
    
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")
        
        # 纯黑色背景 - 简洁专业
        bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            color=BLACK,
            fill_opacity=1,
            stroke_width=0
        )
        self.add(bg)
        
        # 主题图形
{get_theme_graphics(episode_num)}
        
        # 标题文字 - 简洁但突出
        main_title = Text(
            "{title}",
            font_size=52,
            color=WHITE,
            weight=BOLD
        ).to_edge(UP, buff=0.8)
        
        self.add(main_title)
        
        # 副标题
        subtitle_text = Text(
            "{subtitle}",
            font_size=32,
            color=GOLD,
            weight=BOLD
        ).next_to(main_title, DOWN, buff=0.3)
        
        self.add(subtitle_text)
        
        # 集数标签 - 简洁设计
        episode_bg = RoundedRectangle(
            width=1.2, height=0.7,
            corner_radius=0.1,
            color=GOLD,
            fill_opacity=1,
            stroke_width=0
        ).to_corner(UL).shift(RIGHT*0.4 + DOWN*0.4)
        
        episode_label = Text(
            "EP{episode_num:02d}",
            font_size=32,
            color=BLACK,
            weight=BOLD
        ).move_to(episode_bg.get_center())
        
        self.add(episode_bg, episode_label)
        
        # 频道标识 - 简洁设计
        channel_brand = Text(
            "数学之美",
            font_size=24,
            color=WHITE
        ).to_corner(DR).shift(LEFT*0.3 + UP*0.3)
        
        self.add(channel_brand)
'''
    
    return content

def generate_thumbnail(episode_num, title, subtitle, output_dir="output/thumbnails"):
    """生成指定集数的缩略图"""
    
    # 创建临时场景文件
    scene_file = f"temp_thumbnail_ep{episode_num:02d}.py"
    scene_content = create_thumbnail_scene_file(episode_num, title, subtitle)
    
    with open(scene_file, 'w', encoding='utf-8') as f:
        f.write(scene_content)
    
    try:
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 使用manim命令生成PNG
        class_name = f"ThumbnailEP{episode_num:02d}"
        
        cmd = [
            "manim", scene_file, class_name,
            "-s",  # 生成静止图像
            "-qh"  # 高质量
        ]
        
        print(f"正在生成简洁专业缩略图: EP{episode_num:02d} - {title}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ 缩略图已生成")
        else:
            print(f"❌ 生成失败: {result.stderr}")
            
    finally:
        # 清理临时文件
        if os.path.exists(scene_file):
            os.remove(scene_file)

def main():
    parser = argparse.ArgumentParser(description='生成视频缩略图')
    parser.add_argument('--episode', type=int, help='指定集数')
    parser.add_argument('--all', action='store_true', help='生成所有集数的缩略图')
    
    args = parser.parse_args()
    
    episodes = [
        {"num": 1, "title": "向日葵中的螺旋密码", "subtitle": "斐波那契数列与黄金角"},
        {"num": 2, "title": "斐波那契与兔子问题", "subtitle": "数列的起源故事"},
        {"num": 3, "title": "鹦鹉螺中的等角螺线", "subtitle": "自然界最优美的曲线"},
    ]
    
    if args.all:
        for ep in episodes:
            generate_thumbnail(ep["num"], ep["title"], ep["subtitle"])
    elif args.episode:
        ep = next((e for e in episodes if e["num"] == args.episode), None)
        if ep:
            generate_thumbnail(ep["num"], ep["title"], ep["subtitle"])
        else:
            print(f"未找到EP{args.episode}的信息")
    else:
        print("请指定 --episode <数字> 或 --all")

if __name__ == "__main__":
    main() 