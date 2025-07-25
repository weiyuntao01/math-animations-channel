#!/usr/bin/env python
"""
短视频制作工具
将长视频剪辑成适合抖音、视频号的短视频格式
"""

import os
import sys
import json
import subprocess
from pathlib import Path
import argparse
from datetime import datetime

class ShortVideoCreator:
    def __init__(self):
        self.platforms = {
            "douyin": {
                "name": "抖音",
                "resolution": "1080x1920",
                "fps": 30,
                "duration": 60,  # 最长60秒
                "aspect_ratio": "9:16"
            },
            "video_account": {
                "name": "视频号",
                "resolution": "1080x1920", 
                "fps": 30,
                "duration": 60,
                "aspect_ratio": "9:16"
            },
            "xiaohongshu": {
                "name": "小红书",
                "resolution": "1080x1920",
                "fps": 30,
                "duration": 60,
                "aspect_ratio": "9:16"
            },
            "bilibili_short": {
                "name": "B站竖版",
                "resolution": "1080x1920",
                "fps": 30,
                "duration": 180,  # 最长3分钟
                "aspect_ratio": "9:16"
            }
        }
        
        self.clips_config = {
            "EP01": [
                {
                    "name": "开场悬念",
                    "start": "00:00:10",
                    "duration": 15,
                    "title": "向日葵种子为什么是螺旋排列？",
                    "description": "大自然隐藏的数学密码"
                },
                {
                    "name": "黄金角揭秘",
                    "start": "00:01:20", 
                    "duration": 30,
                    "title": "137.5°的神奇角度",
                    "description": "黄金角与斐波那契数列"
                },
                {
                    "name": "螺旋生成",
                    "start": "00:02:00",
                    "duration": 45,
                    "title": "看向日葵如何生长",
                    "description": "数学动画演示螺旋形成过程"
                }
            ],
            "EP02": [
                {
                    "name": "兔子问题",
                    "start": "00:00:40",
                    "duration": 30,
                    "title": "一对兔子引发的数学革命",
                    "description": "斐波那契数列的起源"
                },
                {
                    "name": "数列规律",
                    "start": "00:01:40",
                    "duration": 20,
                    "title": "每个数都是前两个数的和",
                    "description": "最简单却最神奇的规律"
                },
                {
                    "name": "自然界应用",
                    "start": "00:02:20",
                    "duration": 40,
                    "title": "花瓣为什么是3、5、8瓣？",
                    "description": "斐波那契数列在自然界"
                }
            ]
        }
    
    def create_short_video(self, input_video, episode, clip_index, platform, output_dir="output/shorts"):
        """创建短视频"""
        if episode not in self.clips_config:
            print(f"❌ 未找到 {episode} 的剪辑配置")
            return False
        
        clips = self.clips_config[episode]
        if clip_index >= len(clips):
            print(f"❌ {episode} 只有 {len(clips)} 个剪辑片段")
            return False
        
        clip = clips[clip_index]
        platform_config = self.platforms[platform]
        
        print(f"\n{'='*60}")
        print(f"制作短视频: {clip['name']}")
        print(f"平台: {platform_config['name']}")
        print(f"片段: {clip['start']} - {clip['duration']}秒")
        print(f"标题: {clip['title']}")
        print('='*60)
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 生成输出文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{episode}_{clip['name']}_{platform}_{timestamp}.mp4"
        output_path = os.path.join(output_dir, output_filename)
        
        # 构建FFmpeg命令
        cmd = self._build_ffmpeg_command(
            input_video,
            clip['start'],
            clip['duration'],
            platform_config,
            clip['title'],
            output_path
        )
        
        try:
            print("\n执行命令:")
            print(" ".join(cmd))
            
            # 执行转换
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            print(f"\n✅ 短视频制作成功！")
            print(f"输出文件: {output_path}")
            
            # 生成配套文案
            self._generate_copy(episode, clip, platform, output_dir)
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"\n❌ 制作失败！")
            print(f"错误信息: {e.stderr}")
            return False
    
    def _build_ffmpeg_command(self, input_video, start_time, duration, platform_config, title, output_path):
        """构建FFmpeg命令"""
        # 基础命令
        cmd = [
            "ffmpeg",
            "-i", input_video,
            "-ss", start_time,
            "-t", str(duration),
        ]
        
        # 视频滤镜
        filters = []
        
        # 1. 裁剪为竖版（中心裁剪）
        if platform_config["aspect_ratio"] == "9:16":
            filters.append("crop=ih*9/16:ih")
        
        # 2. 缩放到目标分辨率
        width, height = platform_config["resolution"].split("x")
        filters.append(f"scale={width}:{height}")
        
        # 3. 添加标题文字（如果需要）
        # 注意：Windows下中文字体路径需要特殊处理
        title_filter = (
            f"drawtext=text='{title}':"
            f"fontfile='C\\\\:/Windows/Fonts/msyh.ttc':"
            f"fontsize=48:"
            f"fontcolor=white:"
            f"box=1:"
            f"boxcolor=black@0.5:"
            f"boxborderw=10:"
            f"x=(w-text_w)/2:"
            f"y=100"
        )
        filters.append(title_filter)
        
        # 4. 添加品牌水印
        watermark_filter = (
            f"drawtext=text='数学之美':"
            f"fontfile='C\\\\:/Windows/Fonts/msyh.ttc':"
            f"fontsize=24:"
            f"fontcolor=white@0.8:"
            f"x=w-tw-20:"
            f"y=h-th-20"
        )
        filters.append(watermark_filter)
        
        # 组合所有滤镜
        filter_string = ",".join(filters)
        cmd.extend(["-vf", filter_string])
        
        # 视频编码设置
        cmd.extend([
            "-c:v", "libx264",
            "-preset", "slow",
            "-crf", "23",
            "-r", str(platform_config["fps"])
        ])
        
        # 音频设置
        cmd.extend([
            "-c:a", "aac",
            "-b:a", "128k"
        ])
        
        # 输出文件
        cmd.extend(["-y", output_path])
        
        return cmd
    
    def _generate_copy(self, episode, clip, platform, output_dir):
        """生成配套文案"""
        platform_name = self.platforms[platform]["name"]
        
        copy_templates = {
            "douyin": f"""【{clip['title']}】

{clip['description']}

你知道吗？{self._get_hook(episode, clip['name'])}

完整视频讲解更精彩，关注我看更多数学之美！

#数学 #科普 #涨知识 #数学之美 #斐波那契 #黄金分割 #自然规律
""",
            "video_account": f"""《{clip['title']}》

{clip['description']}

{self._get_detailed_description(episode, clip['name'])}

关注"数学之美"，每周更新数学科普视频。

#数学科普 #知识分享 #自然之美
""",
            "xiaohongshu": f"""✨{clip['title']}✨

今天给大家分享一个超神奇的数学知识！

{self._get_notes_style_content(episode, clip['name'])}

💡 知识点总结：
{self._get_key_points(episode, clip['name'])}

觉得有用的话记得点赞收藏哦～
有问题可以在评论区讨论！

#数学笔记 #学习打卡 #知识分享 #数学之美
""",
            "bilibili_short": f"""【{clip['title']}】{clip['description']}

{self._get_detailed_description(episode, clip['name'])}

本期重点：
{self._get_key_points(episode, clip['name'])}

完整版视频已更新，欢迎三连支持！

#科普 #数学 #知识分享
"""
        }
        
        # 保存文案
        copy_filename = f"{episode}_{clip['name']}_{platform}_文案.txt"
        copy_path = os.path.join(output_dir, copy_filename)
        
        with open(copy_path, 'w', encoding='utf-8') as f:
            f.write(copy_templates.get(platform, copy_templates["douyin"]))
        
        print(f"📝 配套文案已保存: {copy_path}")
    
    def _get_hook(self, episode, clip_name):
        """获取吸引人的钩子文案"""
        hooks = {
            "EP01": {
                "开场悬念": "向日葵的种子排列竟然遵循着宇宙级的数学规律",
                "黄金角揭秘": "137.5度这个角度，决定了整个自然界的生长模式",
                "螺旋生成": "21条和34条螺旋，永远是相邻的斐波那契数"
            },
            "EP02": {
                "兔子问题": "一个简单的兔子繁殖问题，却揭示了自然界最基本的规律",
                "数列规律": "这个数列预测了花瓣数、树枝分叉，甚至股市走势",
                "自然界应用": "为什么自然界偏爱3、5、8、13这些数字"
            }
        }
        return hooks.get(episode, {}).get(clip_name, "数学无处不在")
    
    def _get_detailed_description(self, episode, clip_name):
        """获取详细描述"""
        descriptions = {
            "EP01": {
                "开场悬念": "向日葵种子的排列看似杂乱，实则蕴含着精妙的数学规律。每一粒种子的位置都由黄金角决定。",
                "黄金角揭秘": "137.5°，这个看似普通的角度，却是自然界最优雅的分割方式。它让每粒种子都能获得最大的生长空间。",
                "螺旋生成": "当我们用黄金角排列种子时，神奇的事情发生了——螺旋线自然出现，而且螺旋的数量总是斐波那契数。"
            },
            "EP02": {
                "兔子问题": "斐波那契在800年前提出：一对兔子每月生一对小兔子，小兔子长大后也开始繁殖，会有多少对兔子？",
                "数列规律": "1、1、2、3、5、8、13...每个数都是前两个数的和，这个简单的规律创造了一个影响深远的数列。",
                "自然界应用": "从花瓣数到松果螺旋，从鹦鹉螺到银河系，斐波那契数列无处不在，仿佛是大自然的设计密码。"
            }
        }
        return descriptions.get(episode, {}).get(clip_name, "探索数学之美")
    
    def _get_notes_style_content(self, episode, clip_name):
        """获取笔记风格的内容"""
        return f"""
📌 今日学习要点：
{self._get_detailed_description(episode, clip_name)}

📊 实际应用：
• 建筑设计中的黄金比例
• 摄影构图的三分法则
• 股市技术分析的斐波那契回调

🔍 延伸思考：
为什么大自然会"选择"这些数学规律？是巧合还是必然？
"""
    
    def _get_key_points(self, episode, clip_name):
        """获取关键知识点"""
        key_points = {
            "EP01": {
                "开场悬念": "• 向日葵种子呈螺旋排列\n• 螺旋数量是斐波那契数\n• 自然界的优化策略",
                "黄金角揭秘": "• 黄金角 = 137.5°\n• 360° × (2-φ) = 137.5°\n• 最优空间利用",
                "螺旋生成": "• 21条顺时针螺旋\n• 34条逆时针螺旋\n• 相邻斐波那契数"
            },
            "EP02": {
                "兔子问题": "• 递推关系：F(n) = F(n-1) + F(n-2)\n• 初始条件：F(0)=0, F(1)=1\n• 指数级增长",
                "数列规律": "• 每项等于前两项之和\n• 相邻项比值趋近黄金比例\n• 自然界的基本模式",
                "自然界应用": "• 花瓣数：3、5、8、13瓣\n• 叶序排列：2/5、3/8、5/13\n• 贝壳螺旋：对数螺线"
            }
        }
        return key_points.get(episode, {}).get(clip_name, "• 数学与自然的和谐统一")
    
    def batch_create(self, input_video, episode, platform="douyin"):
        """批量创建某一集的所有短视频片段"""
        if episode not in self.clips_config:
            print(f"❌ 未找到 {episode} 的配置")
            return
        
        clips = self.clips_config[episode]
        success_count = 0
        
        print(f"\n开始批量制作 {episode} 的短视频")
        print(f"共有 {len(clips)} 个片段")
        
        for i, clip in enumerate(clips):
            print(f"\n制作第 {i+1}/{len(clips)} 个片段")
            if self.create_short_video(input_video, episode, i, platform):
                success_count += 1
        
        print(f"\n批量制作完成！成功: {success_count}/{len(clips)}")

def main():
    parser = argparse.ArgumentParser(description="短视频制作工具")
    parser.add_argument(
        "input",
        help="输入视频文件路径"
    )
    parser.add_argument(
        "--episode", "-e",
        required=True,
        help="集数编号（如：EP01）"
    )
    parser.add_argument(
        "--clip", "-c",
        type=int,
        help="片段索引（从0开始）"
    )
    parser.add_argument(
        "--platform", "-p",
        choices=["douyin", "video_account", "xiaohongshu", "bilibili_short"],
        default="douyin",
        help="目标平台"
    )
    parser.add_argument(
        "--output", "-o",
        default="output/shorts",
        help="输出目录"
    )
    parser.add_argument(
        "--batch", "-b",
        action="store_true",
        help="批量制作所有片段"
    )
    
    args = parser.parse_args()
    
    creator = ShortVideoCreator()
    
    if args.batch:
        creator.batch_create(args.input, args.episode, args.platform)
    else:
        if args.clip is None:
            print("❌ 请指定片段索引 --clip 或使用 --batch 批量制作")
            sys.exit(1)
        
        creator.create_short_video(
            args.input,
            args.episode,
            args.clip,
            args.platform,
            args.output
        )

if __name__ == "__main__":
    main() 