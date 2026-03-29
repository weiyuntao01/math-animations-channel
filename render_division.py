#!/usr/bin/env python3
"""
竖式除法推理视频渲染脚本
"""

import subprocess
import sys
import os

def render_video():
    """渲染竖式除法推理视频"""
    
    # 确保在正确的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("🎬 开始渲染竖式除法推理视频...")
    print("=" * 50)
    
    try:
        # 渲染命令
        cmd = [
            "manim",
            "-pqh",  # 高质量渲染
            "scenes/math_magic/division_reasoning.py",
            "DivisionReasoningLesson"
        ]
        
        print(f"执行命令: {' '.join(cmd)}")
        print("-" * 50)
        
        # 执行渲染
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("✅ 渲染成功完成！")
        print("📁 视频文件位置: media/videos/")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 渲染失败: {e}")
        print(f"错误输出: {e.stderr}")
        return False
    except FileNotFoundError:
        print("❌ 未找到manim命令，请确保已安装manim并激活虚拟环境")
        return False
    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = render_video()
    if success:
        print("\n🎉 视频渲染完成！")
    else:
        print("\n💥 视频渲染失败！")
        sys.exit(1)
