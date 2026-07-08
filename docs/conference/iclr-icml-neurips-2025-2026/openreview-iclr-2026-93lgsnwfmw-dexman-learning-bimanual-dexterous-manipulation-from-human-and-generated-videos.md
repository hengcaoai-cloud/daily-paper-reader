---
title: "DexMan: Learning Bimanual Dexterous Manipulation from Human and Generated Videos"
title_zh: DexMan：从人类和生成视频学习双臂灵巧操作
authors: "Jhen Hsieh, Kuan-Hsun Tu, Kuo-Han Hung, Tsung-Wei Ke"
date: 2025-09-13
pdf: "https://openreview.net/pdf?id=93LGsNwfMW"
tags: ["query:robot"]
score: 10.0
evidence: DexMan 将人类视频转化为仿人机器人的双臂灵巧操作技能，无需标定或标注。
tldr: 现有从人类视频到机器人灵巧操作的方法常依赖相机标定、深度传感器等，在野外视频中不可行。本文提出 DexMan，直接从第三人称人类操作视频学习仿人机器人的双臂灵巧操作技能，无需额外传感器或标注。它利用新颖的接触奖励和估计出的手-物体姿态在仿真中训练策略，在 TACO 基准上实现物体姿态估计的最优性能，并成功迁移技能至仿真仿人机器人执行多种灵巧操作任务。该工作为从互联网人类视频快速获取机器人灵巧技能提供了自动化解决方案。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 在野外人类视频中提取灵巧操作技能存在相机标定、资产建模等限制。
method: DexMan 自动从第三人称视频估计手-物体姿态，利用接触奖励在仿真中训练仿人机器人双臂灵巧策略。
result: 在物体姿态估计上达到最优，并成功将技能迁移至仿人机器人，实现多种双臂操作任务。
conclusion: DexMan 消除了外部传感器需求，为从人类视频中自动化学习双臂灵巧技能提供了有效途径。
---

## Abstract
We present DexMan, an automated framework that converts human visual demonstrations into bimanual dexterous manipulation skills for humanoid robots in simulation. Operating directly on third-person videos of humans manipulating rigid objects, DexMan eliminates the need for camera calibration, depth sensors, scanned 3D object assets, or ground-truth hand and object motion annotations. Unlike prior approaches that consider only simplified floating hands, it directly controls a humanoid robot and leverages novel contact-based rewards to improve policy learning from noisy hand–object poses estimated from in-the-wild videos.

DexMan achieves state-of-the-art performance in object pose estimation on the TACO benchmark, with absolute gains of 0.08 and 0.12 in ADD-S and VSD. Meanwhile, its reinforcement learning policy surpasses previous methods by 19% in success rate on OakInk-v2. Furthermore, DexMan can generate skills from both real and synthetic videos, without the need for manual data collection and costly motion capture, and enabling the creation of large-scale, diverse datasets for training generalist dexterous manipulation. 

Video results are available at: https://dexman2026.github.io/

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：如何将互联网上随手可得的人类操作视频，直接、自动化地转化为仿人机器人的双臂灵巧操作技能，而无需依赖相机标定、深度传感器、三维资产扫描或精确的手–物体动作标注。
- **研究动机**：现有从人类视频迁移技能的方法普遍依赖严格的硬件设置（如多相机系统、深度相机）和繁重的人工标注，无法推广到场景多样的“野外”视频（in-the-wild videos）。DexMan 正是为解决这一局限性而提出。
- **整体含义**：DexMan 通过消除对特定传感器和人工介入的依赖，为从海量互联网人类视频中低成本、自动化获取机器人灵巧技能提供了一条可行的技术路径，使“看到即学到”的灵巧操作自动化成为可能。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

由于仅提供了摘要与元数据，无法呈现完整的公式与算法细节，以下是其核心方法脉络：

- **整体框架**：DexMan 是一个自动化框架，直接将第三人称人类操作视频转化为仿真环境中仿人机器人的双臂灵巧操作策略。
- **手–物体姿态估计**：系统首先从输入的 RGB 视频中自动估计手部与物体的三维姿态，无需任何相机标定或深度信息。这是该框架消除外部传感器依赖的关键一步。
- **仿真环境与机器人控制**：与以往只考虑简化“浮动灵巧手”的做法不同，DexMan 直接控制完整的仿人机器人模型，使策略学习更贴近真实部署场景。
- **接触奖励设计**：针对从野外视频估计得到的手–物体姿态通常含有噪声的问题，DexMan 引入新颖的基于接触的奖励函数。该奖励在强化学习训练中引导策略，能在姿态估计不完全准确的条件下依然学会稳定、准确的操作。
- **技能生成管道**：最终，将估计的轨迹与接触奖励相结合，在仿真中训练出仿人机器人双臂灵巧操作策略，并能将学习到的技能施用于各类刚性物体的交互任务。

### 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法

- **物体姿态估计基准测试**：
  - 使用 **TACO benchmark** 进行评测。
  - 评价指标：ADD-S 与 VSD。
  - 结果达到当前最优水平，相较于已有方法在 ADD-S 上获得 +0.08 的绝对提升，在 VSD 上获得 +0.12 的绝对提升。
- **操作策略基准测试**：
  - 使用 **OakInk-v2** 数据集上的灵巧操作任务。
  - 评价指标：成功率。
  - DexMan 的强化学习策略成功路由比先前方法高出 **19%**。
- **数据源与场景扩展**：
  - 展示了从**真实人类视频**和**合成（生成）视频**中习得技能的能力，显著拓宽了数据来源，并可借此构造大规模、多多样化数据集，用于训练通用灵巧操作策略。
- 报告中未列出具体对比方法的名称，仅以“previous methods”泛指。

### 4. 资源与算力：如果文中有提到，请总结

- 在所提供的摘要和元数据中，**未明确说明**任何关于 GPU 型号、GPU 数量、单次训练时长或总算力消耗的细节。因此，该部分的资源需求无法评估。

### 5. 实验数量与充分性：大概做了多少组实验，这些实验是否充分、是否客观、公平

- **实验组数**：从现有信息中无法准确推断总共运行了多少组实验。可见的评测维度包括：
  - 在 TACO 上的物体姿态估对比实验；
  - 在 OakInk-v2 上的成功率对比实验；
  - 从真实视频与合成视频两种数据源生成技能的测试。
- **充分性与客观性评估**：由于未呈现详细的实验设置（如训练集规模、随机种子数、误差棒、消融实验等），难以全面评价实验的充分性。但从两个不同性质基准（感知级别的姿态估计、策略级别的操作成功）上均取得显著提升，且与先前方法进行直接对比，客观性较强。若要确认实验是否完全公平，还需更多原文细节支撑。

### 6. 论文的主要结论与发现

- DexMan 成功构建了一条无需外部传感器和人工标注的自动化流水线，能够从第三人称人类视频中学习仿人机器人双臂灵巧操作技能。
- 在物体姿态估计方面，DexMan 在 TACO 基准上超越以往方法，证明了其感知模块的有效性。
- 在操作策略学习方面，借助新颖的接触奖励，DexMan 的强化学习策略在 OakInk-v2 上的成功率比前法高出 19%，显示出良好的噪声容忍和技能迁移能力。
- 方法同时适用于真实和合成视频，为低成本、规模化生成灵巧操作训练数据铺平了道路。

### 7. 优点：方法或实验设计上有哪些亮点

- **消除硬性依赖**：彻底移除相机标定、深度传感器、扫描资产和运动捕捉，极大地降低了系统部署门槛。
- **全机器人本体控制**：不再局限于浮动灵巧手，直接操控整个人形机器人，使研究更贴近真实应用。
- **接触奖励设计**：针对姿态估计噪声这一实务难题，通过奖励函数创新提升策略鲁棒性，增益显著。
- **数据源灵活**：可兼容真实和生成视频，有望利用大规模生成式模型产出几乎无限的训练样本，推动通才型灵巧操作策略的发展。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等

- **实验覆盖有限**：从摘要看，仅汇报了在 TACO 与 OakInk-v2 上的结果，且未提及消融实验、跨任务泛化性测试或在真实机器人上的验证，可能存在仿真到现实的差距。
- **信息不详尽**：未提供训练算力、训练数据量、对比方法具体名称等细节，难以复现或深入评估方法的效率与边界。
- **潜在偏差风险**：若姿态估计模块在某些视频域（如极端光照、遮挡）失效，可能对下游策略产生系统性影响；接触奖励的设计也可能对特定任务类型有偏好。
- **应用限制**：目前展示的操作对象限于刚体，且技能迁移仅在仿真环境中验证，向真实世界的泛化能力尚未可知。

（完）
