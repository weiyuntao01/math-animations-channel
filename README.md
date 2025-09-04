# 数学动画频道 - Math Animations Channel

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Manim-0.18.0+-green.svg" alt="Manim">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Series1-✅%20Complete-brightgreen.svg" alt="Series1">
  <img src="https://img.shields.io/badge/Series2-🚀%20Planning-blue.svg" alt="Series2">
</p>

<p align="center">
  <strong>用视觉讲述数学的故事 | Telling Mathematical Stories Visually</strong>
</p>

使用 Python 和 Manim 创建专业的数学教育动画视频，让抽象的数学概念变得生动可视化。

## 📋 目录

- [项目概述](#-项目概述)
- [快速开始](#-快速开始)
- [项目结构](#-项目结构)
- [内容规划](#-内容规划)
- [技术文档](#-技术文档)
- [参与贡献](#-参与贡献)

## 🎯 项目概述

### 项目愿景

通过精美的动画和深入浅出的讲解，让更多人发现数学之美，理解数学背后的深刻思想。

### 核心特色

- 🎨 **专业视觉效果** - 使用 Manim 引擎，媲美 3Blue1Brown 的视觉质量
- 📚 **严谨数学内容** - 确保数学概念 100% 准确，适合不同层次观众
- 🎬 **流畅动画体验** - 60fps 高帧率，细腻的过渡效果
- 📱 **高质量输出** - 生成高质量视频文件，保存到指定目录

### 项目里程碑 🏆

- ✅ **系列一完成** - 黄金分割与自然数学（8 集，5000+行代码）
- 🚀 **系列二启动** - 概率论的反直觉世界（规划中）
- 📊 **累计成果** - 8 集完整动画，8 篇配音文稿，涵盖几何、数论、艺术等多个领域

### 目标观众

- 主要：成人数学爱好者、理工科学生
- 次要：对数学感兴趣的中学生、教育工作者

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

# 高质量渲染（系列一完整动画）
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

## 🎬 制作流程

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

#### 第三步：视频渲染（1 天）

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

2. **批量渲染**

```bash
# 使用批量渲染脚本
python scripts/batch_render.py
```

## 📁 项目结构

```
math-animations-channel/
├── 📂 scenes/                  # 动画场景代码（核心）
│   ├── geometry/               # ✅ 几何系列（系列一完成）
│   │   ├── sunflower_golden_spiral_ep1.py  # ✅ 向日葵螺旋（370行）
│   │   ├── fibonacci_rabbits_ep2.py        # ✅ 斐波那契兔子（495行）
│   │   ├── nautilus_spiral_ep3.py          # ✅ 鹦鹉螺螺线（687行）
│   │   ├── golden_rectangle_ep4.py         # ✅ 黄金矩形（989行）
│   │   ├── human_proportions_ep5.py        # ✅ 人体比例（576行）
│   │   ├── music_mathematics_ep6.py        # ✅ 音乐数学（583行）
│   │   ├── architecture_mathematics_ep7.py # ✅ 建筑美学（658行）
│   │   └── stock_fibonacci_ep8.py          # ✅ 股市斐波那契（594行）
│   ├── probability/            # 🚀 概率系列（系列二规划中）
│   │   └── [EP09-EP18待创作]
│   ├── calculus/               # 📋 微积分系列（系列三计划）
│   ├── number_theory/          # 📋 数论系列（系列四计划）
│   ├── templates/              # 可复用模板
│   │   └── base_scene.py       # 基础场景模板
│   └── examples/               # 示例代码
│       └── first_animation.py  # 第一个示例
├── 📂 scripts/                 # 工具脚本
│   └── batch_render.py         # 批量渲染工具
├── 📂 docs/                    # 项目文档
│   ├── narration/              # ✅ 配音文稿（系列一完成）
│   │   ├── sunflower_narration_ep1.md        # ✅ 向日葵配音稿
│   │   ├── fibonacci_narration_ep2.md        # ✅ 斐波那契配音稿
│   │   ├── nautilus_narration_ep3.md         # ✅ 鹦鹉螺配音稿
│   │   ├── golden_rectangle_narration_ep4.md # ✅ 黄金矩形配音稿
│   │   ├── human_proportions_narration_ep5.md # ✅ 人体比例配音稿
│   │   ├── music_mathematics_narration_ep6.md # ✅ 音乐数学配音稿
│   │   ├── architecture_mathematics_narration_ep7.md # ✅ 建筑配音稿
│   │   └── stock_fibonacci_narration_ep8.md  # ✅ 股市配音稿
│   ├── project_guide_for_claude.md  # Claude创作指导文档
│   └── project_summary.md      # 项目总结
├── 📂 media/                   # Manim输出目录（自动生成）
├── 📂 output/                  # 最终输出目录
│   └── videos/                 # 渲染的视频文件
├── 📄 requirements.txt         # Python依赖
├── 📄 Makefile                # 自动化脚本
├── 📄 LICENSE                 # MIT许可证
└── 📄 README.md               # 项目说明（本文件）
```

## 📚 内容规划

### 系列规划总览

| 系列名称           | 集数  | 状态      | 预计完成 | 进度          |
| ------------------ | ----- | --------- | -------- | ------------- |
| 黄金分割与自然数学 | 8 集  | ✅ 已完成 | 2024 Q4  | 8/8 (100%) 🎉 |
| 概率论的反直觉世界 | 10 集 | 🚀 规划中 | 2025 Q1  | 0/10 (0%)     |
| 视觉化证明经典     | 12 集 | 📋 计划中 | 2025 Q2  | 未开始        |
| 数学史人物传奇     | 10 集 | 📋 计划中 | 2025 Q3  | 未开始        |

### 详细内容规划

#### ✅ 系列一：黄金分割与自然数学（已完成）

| 集数 | 标题               | 核心内容                       | 状态    | 代码行数 |
| ---- | ------------------ | ------------------------------ | ------- | -------- |
| EP01 | 向日葵中的螺旋密码 | 斐波那契数列、黄金角、螺旋生成 | ✅ 完成 | 370 行   |
| EP02 | 斐波那契与兔子问题 | 数列起源、递归思想、自然增长   | ✅ 完成 | 495 行   |
| EP03 | 鹦鹉螺中的等角螺线 | 对数螺线、自相似性、生长模式   | ✅ 完成 | 687 行   |
| EP04 | 黄金矩形与艺术构图 | 黄金分割、美学原理、名画分析   | ✅ 完成 | 989 行   |
| EP05 | 人体比例中的 1.618 | 维特鲁威人、理想比例、美的数学 | ✅ 完成 | 576 行   |
| EP06 | 音乐和弦中的数学   | 频率比、和谐音程、数学与美     | ✅ 完成 | 583 行   |
| EP07 | 建筑设计的数学美学 | 帕特农神庙、现代建筑、结构之美 | ✅ 完成 | 658 行   |
| EP08 | 股市中的斐波那契   | 回调理论、支撑阻力、实战应用   | ✅ 完成 | 594 行   |

**系列一总结**：

- 🎊 8 集全部完成，累计代码 4952 行
- 📚 8 篇完整配音文稿
- 🎨 涵盖自然、艺术、建筑、金融等多个应用领域
- 🔢 深入展现黄金分割的数学之美

#### 🚀 系列二：概率论的反直觉世界（规划中）

| 集数 | 标题                  | 核心内容                         | 状态      | 预计行数 |
| ---- | --------------------- | -------------------------------- | --------- | -------- |
| EP09 | 蒙蒂霍尔悖论          | 条件概率、直觉欺骗、贝叶斯思维   | 📋 规划中 | 600-700  |
| EP10 | 生日悖论与鸽笼原理    | 组合数学、概率计算、抽屉原理     | 📋 规划中 | 500-600  |
| EP11 | 赌徒谬误与独立事件    | 概率独立性、随机性本质、认知陷阱 | 📋 规划中 | 550-650  |
| EP12 | 大数定律的奇迹        | 频率与概率、收敛性、统计意义     | 📋 规划中 | 600-700  |
| EP13 | 正态分布的魔力        | 钟形曲线、中心极限定理、标准化   | 📋 规划中 | 650-750  |
| EP14 | 贝叶斯定理与医学诊断  | 先验后验、假阳性、决策理论       | 📋 规划中 | 600-700  |
| EP15 | 随机游走与股价模型    | 布朗运动、金融数学、预测极限     | 📋 规划中 | 700-800  |
| EP16 | 马尔可夫链与 PageRank | 状态转移、谷歌算法、网络分析     | 📋 规划中 | 750-850  |
| EP17 | 概率树与决策分析      | 决策树、期望值、风险评估         | 📋 规划中 | 550-650  |
| EP18 | 概率论史话与现代应用  | 历史发展、AI 算法、量子概率      | 📋 规划中 | 600-700  |

**系列二特色**：

- 🎲 聚焦概率论中违反直觉的经典问题
- 🧠 揭示人类认知偏误与数学真理的冲突
- 💡 通过动画模拟展现大数定律的威力
- 🔬 连接理论与现实应用（医学、金融、AI 等）

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

##### 系列颜色规范

**系列一（几何）**：

```python
# 主题色
MATH_BLUE = "#3B82F6"      # 数学蓝
GOLDEN = "#FFD700"         # 黄金色
NATURE_GREEN = "#10B981"   # 自然绿
```

**系列二（概率）**：

```python
# 概率主题色
PROB_BLUE = "#3B82F6"      # 概率蓝
PROB_RED = "#EF4444"       # 事件红
PROB_GREEN = "#10B981"     # 成功绿
PROB_PURPLE = "#8B5CF6"    # 概率紫
```

##### 字体规范

- 中文：Microsoft YaHei（微软雅黑）
- 英文：Arial
- 代码：Consolas

##### 动画时长

- 转场：0.5-1 秒
- 重要概念展示：2-3 秒
- 复杂推导：根据内容调整

### 系列特色技术

#### 系列一技术亮点

1. **黄金比例计算**：

```python
phi = (1 + np.sqrt(5)) / 2  # ≈ 1.618
golden_angle = (3 - np.sqrt(5)) * 180  # ≈ 137.5°
```

2. **螺线绘制**：

```python
def create_golden_spiral(self, a, b, t_max):
    def spiral_func(t):
        r = a * np.exp(b * t)
        return r * np.array([np.cos(t), np.sin(t), 0])
    return ParametricFunction(spiral_func, t_range=[0, t_max])
```

#### 系列二技术准备

1. **随机事件模拟**：

```python
import random
def simulate_probability(n_trials, success_prob):
    successes = sum(1 for _ in range(n_trials)
                   if random.random() < success_prob)
    return successes / n_trials
```

2. **统计可视化**：

```python
def create_probability_chart(self, data):
    bars = BarChart(values=data, y_range=[0, 1])
    return bars
```

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

## 🏆 项目成就

### 已完成里程碑

- ✅ **系列一完成** (2024 Q4)

  - 8 集高质量数学动画
  - 4952 行 Manim 代码
  - 8 篇完整配音文稿
  - 涵盖黄金分割的多个应用领域

- ✅ **技术栈成熟**
  - 建立了完整的制作流程
  - 形成了可复用的代码模板
  - 确立了视觉风格标准

### 进行中目标

- 🚀 **系列二启动** (2025 Q1)
  - 概率论系列动画制作
  - 新的数学领域探索
  - 反直觉概念的可视化挑战

### 未来规划

- 📊 **系列三：视觉化证明经典** (2025 Q2)
- 👥 **系列四：数学史人物传奇** (2025 Q3)
- 🌍 **国际化推广** (2025 Q4)

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
  <strong>🌟 系列一完成，系列二启航！用数学点亮思维，用动画传递美好 🌟</strong><br>
  <em>Series One Complete, Series Two Launching! Illuminate minds with mathematics, spread beauty through animation</em>
</p>

<p align="center">
  <strong>📊 项目统计：8集动画 | 4952行代码 | 8篇文稿 | 无限可能</strong>
</p>

<p align="center">
  Made with ❤️ by <a href="https://github.com/weiyuntao01">weiyuntao01</a>
</p>
