后续系列规划 (EP13 - EP20) 与 ⚠️ 长期避坑指南
这是为了确保未来 AI 接手时能保持一致性的核心文档。
1. 剩余剧集规划 (Roadmap)
第四章：秘密与信任 (续)
EP13: 零知识证明 (Zero Knowledge Proof)
核心场景：阿里巴巴的洞穴。Peggy 拥有开门的咒语，Victor 在外面验证。
视觉重点：环形洞穴的拓扑结构，Peggy 从一边进去，从另一边出来。
哲理：信任不需要“坦白”，只需要“验证”。
第五章：智能与极限 (AI篇)
EP14: 交叉熵 (Cross Entropy)
核心场景：分类问题。两个概率分布的重合度。
视觉重点：用红蓝两色的流体代表概率分布，
H
(
P
,
Q
)
H(P,Q)
 越小，重合度越高。
哲理：学习就是不断降低对世界的“惊讶程度”。
EP15: KL散度 (KL Divergence)
核心场景：真实分布 
P
P
 vs 预测分布 
Q
Q
。
视觉重点：两个形状不同的波形，中间的差值面积就是 KL 散度。
哲理：痛苦源于“预期”与“现实”的错位。
EP16: 柯尔莫哥洛夫复杂性 (Kolmogorov Complexity)
核心场景：ababab... (简单) vs 84h21... (复杂)。
视觉重点：代码长度的对比。最短的描述程序的长度。
哲理：如果生活能被一句话概括，那你活得太简单了。
EP17: 图灵机与停机问题 (Halting Problem)
核心场景：无限长的纸带，读写头。逻辑悖论“我断言我是错的”。
视觉重点：机器试图预测自己是否会停机，陷入死循环（红灯闪烁）。
哲理：理性有边界，有些问题注定无解。
第六章：终章
EP18: 生命与信息
核心：DNA 双螺旋 = 四进制代码。
画面：ATCG 碱基对的数据流化。
EP19: 全息宇宙论
核心：黑洞视界表面积 = 信息量。
画面：3D 物体的信息投影到 2D 表面。
EP20: 万物皆比特 (It from Bit)
核心：系列大总结，宇宙的本质是信息处理。
画面：回顾所有 19 集的图标，汇聚成一个巨大的比特符号。
2. ⚠️ 长期避坑指南 (The Manim Bible)
请将此指南发送给任何接手此项目的 AI：
A. 布局铁律 (Layout)
严格分区：LEFT_ZONE = LEFT * 3.5 (或 4.0)，RIGHT_ZONE = RIGHT * 3.5 (或 4.0)。绝不越界。
流式排版：右侧文字必须使用 arrange(DOWN) 或 next_to。严禁使用绝对坐标手动堆叠文字（如 move_to(UP*2), move_to(UP*1)），必重叠！
分阶段清场：如果一页内容太多，必须先 FadeOut 上一部分，再 Write 下一部分。
屏幕底线：DOWN * 3.5 是底线，不要把文字放到 DOWN * 4.0（会被进度条遮挡）。
B. 语法修正 (Syntax)
Arrow：Arrow(start=..., end=...).shift(UP)。shift 必须后置。
Integer：严禁使用 unit 参数。请用 VGroup(Text("$"), Integer(100))。
Constants：Manim 无 CENTER 常量，用 ORIGIN。
Sector：使用 radius，而非 outer_radius。
Line：使用 stroke_width，而非 width。
Imports：必须包含 import random。
C. 视觉规范 (Visuals)
无灰原则：严禁使用灰色字体。背景线条可用灰色，但传递信息的文字必须是白色或高亮色。
字体：必须设置 Text.set_default(font="Microsoft YaHei")。
公式：如果不确定环境是否支持 LaTeX，优先使用 Text(font="Consolas") 模拟公式，或者使用 MathTex 但不包含中文。
D. 生产流程
生成代码。
检查 import 和颜色定义。
检查 Arrow 和 Integer 的写法。
检查文字布局是否使用了流式排列。
运行预览。