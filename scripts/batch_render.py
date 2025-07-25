#!/usr/bin/env python
"""
批量渲染Manim动画脚本
支持多质量级别渲染和进度跟踪
"""

import os
import sys
import subprocess
import json
import time
from datetime import datetime
from pathlib import Path
import argparse

class BatchRenderer:
    def __init__(self, config_file="render_config.json"):
        self.config_file = config_file
        self.load_config()
        self.results = []
        
    def load_config(self):
        """加载渲染配置"""
        default_config = {
            "scenes": [
                {
                    "file": "scenes/geometry/sunflower_golden_spiral_ep1.py",
                    "class": "SunflowerGoldenSpiralChinese",
                    "name": "EP01_向日葵螺旋",
                    "quality": ["low", "high"]
                },
                {
                    "file": "scenes/geometry/fibonacci_rabbits_ep2.py",
                    "class": "FibonacciRabbitsEP2",
                    "name": "EP02_斐波那契兔子",
                    "quality": ["low", "high"]
                }
            ],
            "output_dir": "output/videos",
            "quality_settings": {
                "low": "-pql",
                "medium": "-pqm",
                "high": "-pqh",
                "4k": "-pqk"
            }
        }
        
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = default_config
            self.save_config()
    
    def save_config(self):
        """保存配置文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)
    
    def render_scene(self, scene_config, quality):
        """渲染单个场景"""
        file_path = scene_config["file"]
        class_name = scene_config["class"]
        scene_name = scene_config["name"]
        quality_flag = self.config["quality_settings"][quality]
        
        print(f"\n{'='*60}")
        print(f"开始渲染: {scene_name}")
        print(f"文件: {file_path}")
        print(f"类名: {class_name}")
        print(f"质量: {quality}")
        print(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print('='*60)
        
        # 构建命令
        cmd = [
            "manim",
            file_path,
            class_name,
            quality_flag,
            "--disable_caching"
        ]
        
        # 设置输出目录
        output_name = f"{scene_name}_{quality}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        start_time = time.time()
        
        try:
            # 执行渲染
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            duration = time.time() - start_time
            
            print(f"\n✅ 渲染成功！")
            print(f"耗时: {duration:.2f}秒")
            
            # 记录结果
            self.results.append({
                "scene": scene_name,
                "quality": quality,
                "status": "success",
                "duration": duration,
                "timestamp": datetime.now().isoformat()
            })
            
            return True
            
        except subprocess.CalledProcessError as e:
            duration = time.time() - start_time
            
            print(f"\n❌ 渲染失败！")
            print(f"错误信息: {e.stderr}")
            
            # 记录失败
            self.results.append({
                "scene": scene_name,
                "quality": quality,
                "status": "failed",
                "error": e.stderr,
                "duration": duration,
                "timestamp": datetime.now().isoformat()
            })
            
            return False
    
    def render_all(self, quality_filter=None):
        """批量渲染所有场景"""
        print(f"\n开始批量渲染")
        print(f"共有 {len(self.config['scenes'])} 个场景待渲染")
        
        total_start = time.time()
        success_count = 0
        fail_count = 0
        
        for scene in self.config['scenes']:
            qualities = scene.get('quality', ['high'])
            
            # 应用质量过滤
            if quality_filter:
                qualities = [q for q in qualities if q in quality_filter]
            
            for quality in qualities:
                success = self.render_scene(scene, quality)
                if success:
                    success_count += 1
                else:
                    fail_count += 1
        
        total_duration = time.time() - total_start
        
        # 生成报告
        self.generate_report(success_count, fail_count, total_duration)
    
    def generate_report(self, success_count, fail_count, total_duration):
        """生成渲染报告"""
        print(f"\n{'='*60}")
        print(f"批量渲染完成！")
        print(f"{'='*60}")
        print(f"总耗时: {total_duration:.2f}秒 ({total_duration/60:.2f}分钟)")
        print(f"成功: {success_count}")
        print(f"失败: {fail_count}")
        print(f"总计: {success_count + fail_count}")
        
        # 保存详细报告
        report_file = f"render_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        report_path = os.path.join("output", report_file)
        
        report = {
            "summary": {
                "total_scenes": success_count + fail_count,
                "success": success_count,
                "failed": fail_count,
                "total_duration": total_duration,
                "timestamp": datetime.now().isoformat()
            },
            "details": self.results
        }
        
        os.makedirs("output", exist_ok=True)
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        
        print(f"\n详细报告已保存至: {report_path}")
    
    def add_scene(self, file_path, class_name, name, quality=None):
        """添加新场景到配置"""
        if quality is None:
            quality = ["low", "high"]
        
        new_scene = {
            "file": file_path,
            "class": class_name,
            "name": name,
            "quality": quality
        }
        
        self.config["scenes"].append(new_scene)
        self.save_config()
        print(f"✅ 已添加场景: {name}")

def main():
    parser = argparse.ArgumentParser(description="批量渲染Manim动画")
    parser.add_argument(
        "--quality", "-q",
        nargs="+",
        choices=["low", "medium", "high", "4k"],
        help="指定渲染质量"
    )
    parser.add_argument(
        "--add-scene",
        action="store_true",
        help="添加新场景到配置"
    )
    parser.add_argument(
        "--file", "-f",
        help="场景文件路径"
    )
    parser.add_argument(
        "--class", "-c",
        dest="class_name",
        help="场景类名"
    )
    parser.add_argument(
        "--name", "-n",
        help="场景名称"
    )
    parser.add_argument(
        "--config",
        default="render_config.json",
        help="配置文件路径"
    )
    
    args = parser.parse_args()
    
    renderer = BatchRenderer(args.config)
    
    if args.add_scene:
        if not all([args.file, args.class_name, args.name]):
            print("❌ 添加场景需要提供 --file, --class 和 --name 参数")
            sys.exit(1)
        
        renderer.add_scene(
            args.file,
            args.class_name,
            args.name,
            args.quality
        )
    else:
        renderer.render_all(args.quality)

if __name__ == "__main__":
    main()
