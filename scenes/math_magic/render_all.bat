@echo off
REM 批量渲染数学之美系列 - Windows批处理脚本
REM 使用方法：双击运行或在命令行执行

echo ========================================
echo 数学之美系列 - 批量渲染脚本
echo ========================================
echo.

REM 设置输出目录
set OUTPUT_DIR=rendered_videos
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

REM 为什么总是拖延？
echo [1/3] 正在渲染：拖延症的数学公式...
manim -qh --resolution 1080,1920 --frame_rate 60 scenes/math_magic/math_magic_ep01.py ProcrastinationFormula
echo ✅ 拖延症公式渲染完成！
echo.

REM 为什么总买贵的？
echo [2/3] 正在渲染：锚定效应的数学陷阱...
manim -qh --resolution 1080,1920 --frame_rate 60 scenes/math_magic/math_magic_ep02.py AnchoringEffect
echo ✅ 锚定效应渲染完成！
echo.

REM 为什么刷视频停不下来？
echo [3/3] 正在渲染：上瘾的数学密码...
manim -qh --resolution 1080,1920 --frame_rate 60 scenes/math_magic/math_magic_ep03.py AddictionMechanism
echo ✅ 上瘾机制渲染完成！
echo.

echo ========================================
echo 所有视频渲染完成！
echo 输出位置：media\videos\
echo ========================================
pause
