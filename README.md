# Math Animations Channel

Professional math education animations using Python and Manim.

## Project Goals

Create high-quality, visual math concept animations for adult math enthusiasts and students.

## Content Series

### Planned Series

1. **Golden Ratio and Natural Mathematics** (8 episodes)
2. **Counter-intuitive World of Probability** (10 episodes)
3. **Visual Proof Classics** (12 episodes)
4. **Mathematical History Legends** (10 episodes)

## Tech Stack

- **Animation Engine**: Manim Community v0.18.0+
- **Programming Language**: Python 3.8+
- **Video Processing**: FFmpeg
- **Version Control**: Git/GitHub

## Quick Start

### Environment Setup

```bash
# Clone project
git clone https://github.com/YOUR_USERNAME/math-animations-channel.git
cd math-animations-channel

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

# update_readme_complete.py

readme_content = '''# 数学动画频道 - Math Animations Channel

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Manim-0.18.0+-green.svg" alt="Manim">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/github/stars/weiyuntao01/math-animations-channel?style=social" alt="Stars">
</p>

<p align="center">
  <strong>用视觉讲述数学的故事 | Telling Mathematical Stories Visually</strong>
</p>

使用 Python 和 Manim 创建专业的数学教育动画视频，让抽象的数学概念变得生动可视化。

## 📋 目录

- [项目概述](#-项目概述)
- [快速开始](#-快速开始)
- [视频展示](#-视频展示)
- [制作教程](#-制作教程)
- [自媒体运营指南](#-自媒体运营指南)
- [项目结构](#-项目结构)
- [内容规划](#-内容规划)
- [技术文档](#-技术文档)
- [参与贡献](#-参与贡献)
- [支持项目](#-支持项目)

## 🎯 项目概述

### 项目愿景

通过精美的动画和深入浅出的讲解，让更多人发现数学之美，理解数学背后的深刻思想。

### 核心特色

- 🎨 **专业视觉效果** - 使用 Manim 引擎，媲美 3Blue1Brown 的视觉质量
- 📚 **严谨数学内容** - 确保数学概念 100%准确，适合不同层次观众
- 🎬 **流畅动画体验** - 60fps 高帧率，细腻的过渡效果
- 🗣️ **中文配音解说** - 专业配音，让国内观众无障碍学习
- 📱 **多平台发布** - 抖音、视频号、B 站、小红书等多平台同步更新

### 目标观众

- 主要：成人数学爱好者、理工科学生
- 次要：对数学感兴趣的中学生、教育工作者
- 扩展：短视频平台的知识类内容爱好者

## 🚀 快速开始

### 环境要求

- Python 3.8 或更高版本
- FFmpeg（用于视频处理）
- LaTeX（可选，用于复杂数学公式）
- Git

### Windows 安装步骤

1. **克隆项目**

```bash
git clone https://github.com/weiyuntao01/math-animations-channel.git
cd math-animations-channel
```

2. **创建虚拟环境**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **安装依赖**

```bash
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

4. **验证安装**

```bash
manim --version
# 应该显示: Manim Community v0.18.0 或更高
```

5. **运行测试动画**

```bash
# 低质量快速预览
manim scenes/examples/first_animation.py FirstAnimation -pql

# 高质量渲染
manim scenes/geometry/sunflower_golden_spiral_ep1.py SunflowerGoldenSpiralChinese -pqh
```

### Mac/Linux 安装步骤

```bash
# 使用 Homebrew (Mac) 或 apt (Linux) 安装系统依赖
# Mac
brew install python ffmpeg

# Ubuntu/Debian
sudo apt update
sudo apt install python3-pip ffmpeg

# 后续步骤同Windows，只是激活虚拟环境命令不同
source venv/bin/activate
```

## 🎬 视频展示

### 已完成作品

#### 1. 向日葵中的螺旋密码（黄金分割系列 EP01）

- **时长**：3 分 30 秒
- **内容**：揭示向日葵种子排列中的斐波那契数列和黄金角
- **亮点**：
  - 动态生成 800 个种子的向日葵
  - 可视化展示 137.5° 黄金角
  - 高亮 21 和 34 条螺旋线（斐波那契数）
- **文件**：`scenes/geometry/sunflower_golden_spiral_ep1.py`

### 制作中作品

#### 2. 斐波那契与兔子问题（黄金分割系列 EP02）

- **预计完成**：2024 年 8 月
- **内容**：斐波那契数列的起源故事
- **进度**：脚本编写中

## 🎥 制作教程

### 完整制作流程

#### 第一步：创意与脚本（1-2 天）

1. **选题研究**

   - 浏览数学资料，寻找有趣主题
   - 参考资源：
     - MacTutor 数学史档案
     - Wolfram MathWorld
     - 数学科普书籍

2. **编写脚本**
   - 创建文档：`docs/narration/episode_XX.md`
   - 包含内容：
     - 时间轴规划
     - 配音文稿
     - 视觉呈现说明

#### 第二步：动画编程（2-3 天）

1. **创建场景文件**

```python
# scenes/category/your_animation.py
from manim import *
import numpy as np

class YourAnimation(Scene):
    def construct(self):
        # 设置中文字体
        Text.set_default(font="Microsoft YaHei")

        # 动画逻辑
        self.show_opening()
        self.demonstrate_concept()
        self.show_examples()
        self.conclude()
```

2. **开发技巧**
   - 使用模块化设计，每个概念一个方法
   - 控制好动画节奏，重要概念停留 2-3 秒
   - 颜色使用项目标准色板

#### 第三步：渲染与优化（1 天）

1. **分阶段渲染**

```bash
# 开发阶段：低质量快速预览
manim scene.py SceneName -pql

# 检查阶段：中等质量
manim scene.py SceneName -pqm

# 发布阶段：高质量1080p
manim scene.py SceneName -pqh

# 特殊需求：4K超高清
manim scene.py SceneName -pqk
```

2. **性能优化**
   - 限制同屏对象数量（<1000 个）
   - 使用 VGroup 批量管理
   - 合理使用 LaggedStart

#### 第四步：配音制作（1 天）

1. **录音要求**

   - 设备：专业麦克风或高质量耳麦
   - 环境：安静的室内环境
   - 格式：48kHz, 16bit, 单声道

2. **录音技巧**

   - 语速：每分钟 180-200 字
   - 语调：平稳自然，重点处略微提高
   - 停顿：数字和公式处适当停顿

3. **后期处理**
   - 降噪处理
   - 音量标准化（-23 LUFS）
   - 导出高质量 WAV 格式

#### 第五步：视频合成（0.5 天）

1. **使用专业软件**

   - Adobe Premiere Pro
   - DaVinci Resolve（免费）
   - 剪映专业版（适合快速制作）

2. **合成步骤**
   - 导入动画和音频
   - 精确对齐时间轴
   - 添加背景音乐（音量-30dB）
   - 添加片头片尾

#### 第六步：短视频制作（0.5 天）

1. **竖版视频制作（抖音/视频号）**

   - 分辨率：1080x1920（9:16）
   - 时长：15-60 秒
   - 要点：
     - 开头 3 秒抓住注意力
     - 核心内容精简呈现
     - 结尾引导互动

2. **横版精华剪辑（B 站/西瓜）**
   - 分辨率：1920x1080（16:9）
   - 时长：1-3 分钟
   - 保留完整知识点

## 📱 自媒体运营指南

### 平台策略

#### 抖音运营

- **发布时间**：晚上 7-9 点，周末下午 2-4 点
- **标题格式**：疑问句+知识点，如"为什么向日葵的种子是螺旋排列的？"
- **标签建议**：#数学 #科普 #知识分享 #涨知识 #数学之美
- **互动技巧**：
  - 评论区提问引导讨论
  - 制作系列内容，引导关注
  - 适时直播讲解

#### 视频号运营

- **目标用户**：25-45 岁知识型用户
- **内容调性**：专业但不失趣味
- **引流方式**：
  - 公众号联动
  - 朋友圈分享
  - 社群传播

#### B 站运营

- **完整版发布**：保持 3-5 分钟完整内容
- **分区选择**：科技-科普-理科
- **封面设计**：清晰展示核心概念
- **弹幕互动**：预设互动点

#### 小红书运营

- **图文结合**：动画截图+知识卡片
- **笔记风格**：学习笔记分享
- **话题标签**：#数学笔记 #学习打卡

### 内容优化

#### 短视频剪辑要点

1. **黄金 3 秒**：开头必须吸引眼球
2. **节奏控制**：每 10 秒一个知识点
3. **视觉冲击**：动画效果要突出
4. **情绪引导**：从好奇到恍然大悟

#### 标题公式

- 疑问式：为什么 XX 中隐藏着数学规律？
- 数字式：3 分钟看懂 XX 背后的数学原理
- 对比式：你以为的 XX vs 数学家眼中的 XX
- 悬念式：这个数学规律，改变了整个世界

#### 封面设计

- 主体突出：核心视觉元素占 60%
- 文字醒目：标题字体大且对比强
- 色彩鲜明：使用项目标准色
- 品牌统一：保持系列视觉一致性

### 引流转化

#### 私域流量构建

1. **微信群运营**

   - 建立数学爱好者交流群
   - 定期分享额外内容
   - 组织线上讨论会

2. **公众号内容**

   - 视频文字版详解
   - 延伸阅读材料
   - 习题与解答

3. **知识付费**
   - 系统课程开发
   - 一对一辅导
   - 会员专属内容

#### 商业变现

- 知识付费课程
- 企业培训合作
- 图书出版机会
- 品牌赞助合作

## 📁 项目结构

```
math-animations-channel/
├── 📂 .github/                 # GitHub配置
│   ├── workflows/              # 自动化工作流
│   └── ISSUE_TEMPLATE/         # Issue模板
├── 📂 scenes/                  # 动画场景代码（核心）
│   ├── geometry/               # 几何系列
│   │   ├── sunflower_golden_spiral_ep1.py  # ✅ 向日葵螺旋
│   │   ├── fibonacci_rabbits_ep2.py        # 🚧 斐波那契兔子
│   │   ├── nautilus_spiral_ep3.py          # 📋 鹦鹉螺螺线
│   │   ├── golden_rectangle_ep4.py         # 📋 黄金矩形
│   │   ├── human_proportion_ep5.py         # 📋 人体比例
│   │   ├── music_harmony_ep6.py            # 📋 音乐和弦
│   │   ├── architecture_beauty_ep7.py      # 📋 建筑美学
│   │   └── fibonacci_trading_ep8.py        # 📋 股市分析
│   ├── probability/            # 概率系列
│   ├── calculus/               # 微积分系列
│   ├── number_theory/          # 数论系列
│   ├── templates/              # 可复用模板
│   │   └── base_scene.py              # 基础场景模板
│   └── examples/               # 示例代码
├── 📂 assets/                  # 媒体资源
│   ├── audio/                  # 音频文件
│   ├── images/                 # 图片资源
│   └── fonts/                  # 字体文件
├── 📂 scripts/                 # 工具脚本
│   ├── batch_render.py         # 批量渲染工具
│   ├── create_thumbnail.py     # 缩略图生成
│   ├── short_video_creator.py  # 短视频制作工具
│   └── publish_helper.py       # 多平台发布助手
├── 📂 docs/                    # 项目文档
│   ├── narration/              # 配音文稿
│   │   ├── sunflower_narration.md     # ✅ 向日葵配音稿
│   │   ├── fibonacci_narration.md     # 📋 斐波那契配音稿
│   │   └── ...                        # 其他配音稿
│   ├── tutorials/              # 教程文档
│   └── planning/               # 规划文档
├── 📂 output/                  # 输出目录
│   ├── videos/                 # 渲染的视频
│   ├── shorts/                 # 短视频版本
│   └── thumbnails/             # 视频缩略图
├── 📂 tests/                   # 测试代码
├── 📄 requirements.txt         # Python依赖
├── 📄 Makefile                # 自动化脚本
├── 📄 LICENSE                 # MIT许可证
└── 📄 README.md               # 项目说明（本文件）
```

## 📚 内容规划

### 系列规划总览

| 系列名称           | 集数  | 状态      | 预计完成 |
| ------------------ | ----- | --------- | -------- |
| 黄金分割与自然数学 | 8 集  | 🚧 制作中 | 2024 Q4  |
| 概率论的反直觉世界 | 10 集 | 📋 规划中 | 2025 Q1  |
| 视觉化证明经典     | 12 集 | 📋 规划中 | 2025 Q2  |
| 数学史人物传奇     | 10 集 | 📋 规划中 | 2025 Q3  |

### 详细内容规划

#### 系列一：黄金分割与自然数学（8 集）

| 集数 | 标题                     | 核心内容                       | 状态      | 文件位置                                         |
| ---- | ------------------------ | ------------------------------ | --------- | ------------------------------------------------ |
| EP01 | 向日葵中的螺旋密码       | 斐波那契数列、黄金角、螺旋生成 | ✅ 完成   | `scenes/geometry/sunflower_golden_spiral_ep1.py` |
| EP02 | 斐波那契与兔子问题       | 数列起源、递归思想、自然增长   | 🚧 制作中 | `scenes/geometry/fibonacci_rabbits_ep2.py`       |
| EP03 | 鹦鹉螺中的等角螺线       | 对数螺线、自相似性、生长模式   | 📋 规划中 | -                                                |
| EP04 | 黄金矩形与艺术构图       | 黄金分割、美学原理、名画分析   | 📋 规划中 | -                                                |
| EP05 | 人体比例中的 1.618       | 维特鲁威人、理想比例、美的数学 | 📋 规划中 | -                                                |
| EP06 | 音乐和弦中的数学         | 频率比、和谐音程、数学与美     | 📋 规划中 | -                                                |
| EP07 | 建筑设计的数学美学       | 帕特农神庙、现代建筑、结构之美 | 📋 规划中 | -                                                |
| EP08 | 股市技术分析中的斐波那契 | 回调理论、支撑阻力、实战应用   | 📋 规划中 | -                                                |

#### 系列二：概率论的反直觉世界（10 集）

| 集数 | 标题               | 核心概念     | 状态    |
| ---- | ------------------ | ------------ | ------- |
| EP01 | 生日悖论           | 概率累积效应 | 🚧 脚本 |
| EP02 | 蒙提霍尔的三扇门   | 条件概率     | 📋 规划 |
| EP03 | 赌徒谬误           | 独立事件     | 📋 规划 |
| EP04 | 辛普森悖论         | 统计陷阱     | 📋 规划 |
| EP05 | 贝叶斯的智慧       | 先验概率     | 📋 规划 |
| EP06 | 随机漫步与醉汉回家 | 布朗运动     | 📋 规划 |
| EP07 | 大数定律           | 概率收敛     | 📋 规划 |
| EP08 | 中心极限定理       | 正态分布     | 📋 规划 |
| EP09 | 本福特定律         | 数字分布     | 📋 规划 |
| EP10 | 概率与直觉的战争   | 综合应用     | 📋 规划 |

## 🛠️ 技术文档

### Manim 核心概念

#### 1. 场景结构

```python
class StandardScene(Scene):
    """标准场景模板"""

    def construct(self):
        # 场景构建方法，按顺序执行
        self.show_title()         # 显示标题
        self.introduce_concept()  # 介绍概念
        self.demonstrate()        # 演示过程
        self.summarize()         # 总结要点

    def show_title(self):
        title = Text("标题", font_size=56)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
```

#### 2. 常用对象

| 类型 | 类名    | 用途     | 示例                           |
| ---- | ------- | -------- | ------------------------------ |
| 文字 | Text    | 显示文字 | `Text("你好", font_size=48)`   |
| 数学 | MathTex | 数学公式 | `MathTex(r"\frac{a}{b}")`      |
| 几何 | Circle  | 圆形     | `Circle(radius=2, color=BLUE)` |
| 几何 | Square  | 正方形   | `Square(side_length=2)`        |
| 几何 | Line    | 直线     | `Line(start=LEFT, end=RIGHT)`  |
| 坐标 | Axes    | 坐标系   | `Axes(x_range=[-5,5])`         |
| 组合 | VGroup  | 对象组   | `VGroup(obj1, obj2, obj3)`     |

#### 3. 动画类型

```python
# 创建动画
self.play(Create(circle))        # 绘制创建
self.play(Write(text))          # 书写文字
self.play(FadeIn(obj))          # 淡入
self.play(FadeOut(obj))         # 淡出

# 变换动画
self.play(Transform(obj1, obj2)) # 变形
self.play(obj.animate.scale(2))  # 缩放
self.play(obj.animate.shift(UP)) # 移动
self.play(Rotate(obj, PI/2))     # 旋转

# 复合动画
self.play(
    Create(circle),
    Write(text),
    run_time=2  # 同时执行，总时长2秒
)
```

#### 4. 项目标准

##### 颜色规范

```python
# 主题色
MATH_BLUE = "#3B82F6"      # 数学蓝
GOLDEN = "#FFD700"         # 黄金色
NATURE_GREEN = "#10B981"   # 自然绿
PROB_PURPLE = "#8B5CF6"    # 概率紫

# 功能色
HIGHLIGHT = "#F59E0B"      # 高亮橙
ERROR_RED = "#EF4444"      # 错误红
SUCCESS_GREEN = "#10B981"  # 成功绿
```

##### 字体规范

- 中文：Microsoft YaHei（微软雅黑）
- 英文：Arial
- 代码：Consolas

##### 动画时长

- 转场：0.5-1 秒
- 重要概念展示：2-3 秒
- 复杂推导：根据内容调整
- 片头片尾：各 2 秒

### 常见问题解决

#### Q1: 中文显示乱码？

```python
# 在construct方法开始处添加
Text.set_default(font="Microsoft YaHei")
```

#### Q2: 渲染速度太慢？

```bash
# 使用低质量预览
manim scene.py SceneName -pql

# 限制帧率
manim scene.py SceneName -pql --fps 30
```

#### Q3: 内存不足？

- 减少同屏对象数量
- 使用`remove`及时清理不需要的对象
- 分段渲染长视频

#### Q4: 短视频竖版适配？

```python
# 在场景初始化时设置
self.camera.frame_width = 9
self.camera.frame_height = 16
```

## 🤝 参与贡献

### 贡献方式

1. **🐛 报告问题**

   - 使用 GitHub Issues
   - 说明问题复现步骤
   - 附上错误截图或日志

2. **💡 功能建议**

   - 在 Issues 中打上 `enhancement` 标签
   - 详细描述需求和使用场景

3. **📝 内容贡献**
   - Fork 项目到自己的仓库
   - 创建功能分支：`git checkout -b feature/new-animation`
   - 提交代码：`git commit -m "feat: 添加xxx动画"`
   - 推送分支：`git push origin feature/new-animation`
   - 提交 Pull Request

### 代码规范

1. **Python 代码风格**

```bash
# 使用 Black 格式化
black scenes/

# 使用 Flake8 检查
flake8 scenes/ --max-line-length=88
```

2. **提交信息规范**

   - `feat`: 新功能
   - `fix`: 修复 bug
   - `docs`: 文档更新
   - `style`: 代码格式调整
   - `refactor`: 代码重构
   - `test`: 测试相关
   - `chore`: 构建过程或辅助工具的变动

3. **分支管理**
   - `main` - 主分支，稳定版本
   - `develop` - 开发分支
   - `feature/*` - 功能分支
   - `bugfix/*` - 修复分支

## 📊 项目统计

| 指标         | 数值                                                                                            | 更新时间 |
| ------------ | ----------------------------------------------------------------------------------------------- | -------- |
| 总视频数     | 1                                                                                               | 2024.07  |
| 代码行数     | 2,500+                                                                                          | 2024.07  |
| GitHub Stars | ![Stars](https://img.shields.io/github/stars/weiyuntao01/math-animations-channel?style=social)  | 实时     |
| 贡献者       | ![Contributors](https://img.shields.io/github/contributors/weiyuntao01/math-animations-channel) | 实时     |

## 💖 支持项目

如果您觉得这个项目有帮助，可以通过以下方式支持：

1. **⭐ Star** - 给项目点个星
2. **🔄 Share** - 分享给更多人
3. **📺 Subscribe** - 订阅视频频道
4. **💬 Feedback** - 提供宝贵意见

## 📮 联系方式

- **GitHub**: [@weiyuntao01](https://github.com/weiyuntao01)
- **Email**: weiyuntao01@gmail.com
- **抖音**: [数学之美频道]
- **视频号**: [数学动画讲堂]
- **B 站**: [数学可视化]
- **小红书**: [数学笔记分享]

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。详见 LICENSE 文件。

这意味着您可以：

- ✅ 商业使用
- ✅ 修改
- ✅ 分发
- ✅ 私人使用

只需要：

- 📋 保留版权声明
- 📋 保留许可证声明

---

<p align="center">
  <strong>🌟 用数学点亮思维，用动画传递美好 🌟</strong><br>
  <em>Illuminate minds with mathematics, spread beauty through animation</em>
</p>

<p align="center">
  Made with ❤️ by <a href="https://github.com/weiyuntao01">weiyuntao01</a>
</p> '''
保存文件
with open('README.md', 'w', encoding='utf-8') as f: f.write(readme_content)
print("✅ README.md 已更新完成！") print("\n下一步操作：") print("1. git add README.md") print("2. git commit -m 'docs: 完善项目README文档'") print("3. git push origin main")

运行脚本：

```cmd
python update_readme_complete.py
然后提交到GitHub：
cmd
git add README.md
git commit -m "docs: 完善项目README文档"
git push origin main
这个README包含了：
完整的项目介绍
详细的制作流程
技术文档
内容规划
贡献指南
项目统计
所有内容都整合在一个文件里，方便管理和查看！
```
