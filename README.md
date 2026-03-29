# 数学动画频道 - Math Animations Channel

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Manim-0.18.0+-green.svg" alt="Manim">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/MathBeauty-On%20Air-orange.svg" alt="MathBeauty">
  <img src="https://img.shields.io/badge/GoldenRatio-Complete-brightgreen.svg" alt="GoldenRatio">
</p>

<p align="center">
  <strong>用视觉讲述数学的故事 | Telling Mathematical Stories Visually</strong>
</p>

数学动画频道致力于用 Manim 将抽象数学转化为可视化证据。从黄金分割的几何美，到概率论的反直觉，再到正在热播的《数学之美》系列，我们保持严谨、故事感与可复现性并重。

## 目录
- [项目概述](#项目概述)
- [系列概览](#系列概览)
- [数学之美·制作路线](#数学之美制作路线)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [制作流程](#制作流程)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

## 项目概述

### 愿景
通过精美的动画和深入浅出的叙事，让观众用肉眼看到数学逻辑、用行动验证数学决策。

### 当前主线
- **《数学之美》 Math Beauty（主攻线）**：基于真实痛点讲述数学如何解释行为、经济、健康与社会现象。每集 5-8 分钟，结构“痛点 → 模型 → 验证 → 行动”。
- 推广节奏：每两周上线 1 集正片 + 1 条互动短剪，重点平台为 哔哩哔哩 / 抖音 / 视频号。

### 核心受众
- 年龄 25-45 岁的理工背景观众、对理性决策有诉求的职场人、关注子女教育的家长。
- 内容要求：数学严谨、案例真实、提供可跟做的数据或模板。

## 系列概览

| 系列 | 状态 | 简介 |
| --- | --- | --- |
| 数学之美 Math Beauty | On Air | 以生活痛点为入口，讲解决策背后的数学模型与可视化验证。当前已发布 EP01-EP09，正在制作新一季“财富与认知”篇。 |
| 黄金分割与自然数学 | Completed | 系列一，共 8 集；围绕斐波那契、黄金比例与自然艺术，适合作为频道视觉名片。 |
| 概率论的反直觉世界 | Archive | 系列二，已完成 EP09-EP21，其中《马尔可夫链》表现最佳；沉淀为组件库与脚本素材。 |
| 数字仿生 Digital Biomimetics | Lab | 算法生成艺术实验系列，共 12 集；保留用于特效素材与跨界合作。 |
| 视觉证明 Visual Proofs | Paused | 几何与代数经典证明，已完成 5 集；未来与教材合作时再扩展。 |

## 数学之美·制作路线

- **内容框架**：
  1. 真实案例设问（30s）
  2. 建模拆解（模型假设、关键公式）
  3. 动态验证（蒙特卡洛、敏感性分析、图形对比）
  4. 行动清单 / 互动挑战
- **视觉规范**：背景深灰、强调色使用 `#8B5CF6`、`#10B981`、`#F59E0B`，字体统一 `Microsoft YaHei`。
- **资产沉淀**：
  - `scenes/math_magic/components/` 内放置 BudgetBalancer、DecisionTimeline、ProbabilityMeter 等可复用模块；
  - 配套数据或模板存放在 `media/toolkits/math_beauty/`；
  - 文字稿与分镜保存在 `docs/narration/math_beauty/`。
- **近期优先级**：
  1. 完成 EP10-EP12 脚本与演示数据；
  2. 复盘 EP16（马尔可夫链）互动设计，迁移到数学之美系列的评论挑战；
  3. 更新各平台封面、简介，确保品牌统一。

## 项目结构

```
math-animations-channel/
├── scenes/
│   ├── math_magic/            # 《数学之美》主线场景与组件
│   ├── geometry/              # 黄金分割与自然数学（Series1 完结）
│   ├── probability/           # 概率反直觉系列（素材库）
│   ├── digital_biomimetics/   # 数字仿生（实验性）
│   ├── visual_proofs/         # 视觉证明（暂缓）
│   └── templates/             # 通用基类与工具
├── docs/
│   ├── narration/             # 各系列配音稿与分镜
│   └── ...
├── media/                     # 渲染输出、素材与数据
├── scripts/                   # 渲染与批处理脚本
├── requirements.txt
└── README.md
```

## 快速开始

### 安装依赖
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
manim --version  # 应显示 Manim Community v0.18.0+
```

### 渲染示例
```bash
# 预览《数学之美》某一集
manim scenes/math_magic/math_magic_ep09.py MathMagicEP09 -pql

# 正式输出 1080p
manim scenes/math_magic/math_magic_ep09.py MathMagicEP09 -pqh
```

## 制作流程

1. **选题与脚本（0.5-1 天）**：整理真实案例 → 明确数学模型 → 编写 `docs/narration/math_beauty/epXX.md`。
2. **动画实现（1-2 天）**：复用组件库，补充特定镜头；生成低清预览校验逻辑。
3. **验证与打磨（0.5 天）**：检查公式、变量命名、字幕对齐；与数据模板交叉验证。
4. **渲染与分发（0.5 天）**：渲染 HQ 版本、剪出短剪、准备互动文案。
5. **复盘与迭代（持续）**：收集观众问题、更新 README 的“项目战报”，规划下一集。

## 参与贡献

欢迎通过 Issue 提建议、提交 Pull Request 或分享可视化想法：
- `feat`: 新动画或组件
- `fix`: Bug 修复
- `docs`: 文档改进
- `style`/`refactor`/`test`/`chore`: 其他类别

执行前请确保通过 `black` 和 `flake8` 进行基础检查。

## 许可证

本项目使用 [MIT License](LICENSE)。保留版权与许可证声明即可自由使用、修改与分发。

---

> 让每一帧都是证据，让每个公式都能落地。
