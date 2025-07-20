import os
import subprocess
import sys
from pathlib import Path

def render_scene(filepath, scene_name, quality='ql'):
    """Render a single scene"""
    cmd = f"manim {filepath} {scene_name} -{quality}"
    print(f"Rendering: {scene_name}")
    subprocess.run(cmd.split())

if __name__ == '__main__':
    # Example usage
    render_scene('scenes/examples/first_animation.py', 'FirstAnimation')
