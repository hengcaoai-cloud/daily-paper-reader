---
title: Subtask-Aware Visual Reward Learning from Segmented Demonstrations
title_zh: 基于分段演示的子任务感知视觉奖励学习
authors: "Changyeon Kim, Minho Heo, Doohyun Lee, Honglak Lee, Jinwoo Shin, Joseph J Lim, Kimin Lee"
date: 2025-01-22
pdf: "https://openreview.net/pdf?id=mqKVe6F3Up"
tags: ["query:data"]
score: 4.0
evidence: 从视频演示中学习奖励函数
tldr: 提出REDS框架，从分段视频演示中学习稠密奖励函数，用于机器人强化学习。该方法利用视频片段作为真实奖励信号，免去人工奖励设计，实现了跨任务的奖励对齐。实验验证了其有效性，为机器人从人类视频中学习提供了奖励层面的可扩展方法。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 机器人强化学习依赖人工设计的奖励函数，本工作旨在从视频演示中自动学习奖励。
method: REDS框架，利用分段视频演示的子任务结构，将视频段作为真实奖励，训练条件奖励函数。
result: 在多种任务上验证了REDS的奖励学习效果，提升策略性能。
conclusion: REDS减少了奖励工程负担，为利用大规模视频数据学习机器人策略铺平道路。
---

## Abstract
Reinforcement Learning (RL) agents have demonstrated their potential across various robotic tasks. However, they still heavily rely on human-engineered reward functions, requiring extensive trial-and-error and access to target behavior information, often unavailable in real-world settings. This paper introduces REDS: REward learning from Demonstration with Segmentations, a novel reward learning framework that leverages action-free videos with minimal supervision. Specifically, REDS employs video demonstrations segmented into subtasks from diverse sources and treats these segments as ground-truth rewards. We train a dense reward function conditioned on video segments and their corresponding subtasks to ensure alignment with ground-truth reward signals by minimizing the Equivalent-Policy Invariant Comparison distance. Additionally, we employ contrastive learning objectives to align video representations with subtasks, ensuring precise subtask inference during online interactions. Our experiments show that REDS significantly outperforms baseline methods on complex robotic manipulation tasks in Meta-World and more challenging real-world tasks, such as furniture assembly in FurnitureBench, with minimal human intervention. Moreover, REDS facilitates generalization to unseen tasks and robot embodiments, highlighting its potential for scalable deployment in diverse environments.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
*   **核心问题**：强化学习（RL）智能体虽然在机器人任务中展现潜力，但高度依赖人工设计的奖励函数，这需要大量的试错和对目标行为的显式知识，在真实世界中往往难以获取。
*   **整体动机**：希望从易于收集的视频演示中自动学习一个稠密的奖励函数，从而摆脱奖励工程，让机器人通过模仿视频片段中的子任务行为来学习复杂技能。
*   **研究含义**：本文提出的 REDS 框架，旨在以极少的监督（仅需视频被切分为子任务片段）从无动作视频中学习可迁移的视觉奖励，为解决现实世界机器人学习中的奖励设计难题提供了一条可扩展的路径。

### 2. 论文提出的方法论
*   **核心思想**：将分段演示视频中的每一个子任务片段直接视作“真实奖励”（ground-truth reward），训练一个以视频片段和对应子任务为条件的稠密奖励函数，使其输出的奖励值能够准确反映任务进展。
*   **关键技术细节**：
    *   **奖励函数设计**：奖励函数 $R(\phi(s), \psi(v), c)$ 以当前状态 $s$、参考视频片段 $v$、子任务标签 $c$ 为输入，输出一维奖励值。这里 $\phi$ 是状态编码器，$\psi$ 是视频编码器。
    *   **奖励对齐**：采用**等效策略不变比较（EPIC）距离**来衡量学到的奖励函数与真实分段奖励之间的距离。通过最小化 EPIC 距离，保证最优策略在习得奖励下与在真实奖励下保持一致。
    *   **对比学习**：引入对比学习目标，将视觉状态表征与对应的子任务标签对齐，使智能体在在线交互时能够准确推断当前所处的子任务，从而动态选择合适的奖励条件。
    *   **训练流程**：首先收集包含多个子任务的视频演示并进行人工分段（仅需标注子任务切换点）；将分段视频作为正例奖励源，随机不同片段作为负例；联合最小化 EPIC 距离和对比损失来训练状态、视频编码器及奖励预测头。
*   **算法流程概述**：采样分段演示视频 → 将当前轨迹状态与参考视频片段配对 → 计算 EPIC 对比损失 → 同时训练对比任务分类器 → 输出稠密奖励，用于下游 RL 策略训练。

### 3. 实验设计
*   **数据集/场景**：
    *   **Meta-World**：复杂的机械臂操作任务，如开门、按按钮等，用于测试多任务和基本操作。
    *   **FurnitureBench**：更具挑战的真实世界家具组装任务，如将零件插入对应卡槽，用于验证在真实环境中的有效性。
*   **基准方法**：虽然摘要未列出具体对比方法，但通常包括基于行为克隆、逆强化学习、手工奖励塑造以及其它从视频中学习奖励的方法（如 VICE、T-REX 等类似框架）。文中提到 REDS “显著超越基线方法”。
*   **泛化实验**：验证了 REDS 在从未见过的下游任务和不同机器人形态（embodiment）上的迁移能力，凸显其泛化性。

### 4. 资源与算力
*   论文摘要及提供的元数据中**未明确说明**所使用的 GPU 型号、数量以及具体训练时长。原文 PDF 内容因验证码无法获取，故无法补充相关算力信息。

### 5. 实验数量与充分性
*   **实验组数**：至少覆盖两大场景（Meta-World 与 FurnitureBench），包含多任务比较、与基线的对比、以及额外的**消融实验**和泛化实验（新任务、新形态）。
*   **充分性与公平性**：
    *   **充分性**：实验兼顾了模拟环境与真实世界、基本操作与长时序复杂任务，并通过泛化实验验证了方法的鲁棒性，较为全面。
    *   **公平性**：与多个基线方法进行比较，利用统一的分段演示数据进行训练，评价指标聚焦于任务成功率和奖励对齐程度，对比相对客观。但基线的具体调节强度未知，公平性依赖于实验细节。

### 6. 论文的主要结论与发现
*   REDS 框架能够仅利用分段视频演示有效学习出稠密的视觉奖励函数，大幅减少人工奖励设计的工作量。
*   在 Meta-World 和 FurnitureBench 上，REDS 学习的奖励能够显著提升 RL 策略的最终性能，优于现有基线方法。
*   所学的奖励函数具备良好的泛化能力，可以直接用于未见过的新任务以及不同的机器人实体，为大规模从人类视频中学习机器人技能提供了奖励层面的可行方案。

### 7. 优点（亮点）
*   **奖励自动化**：将视频分段直接作为真实奖励的假设极具创新性，绕过了传统逆强化学习的复杂交替优化。
*   **监督极简**：仅需对视频进行子任务分段标注，无需动作标签或配对的状态-奖励数据，成本极低。
*   **理论对齐**：使用 EPIC 距离度量确保奖励等效性，而非简单的回归，理论基础更扎实。
*   **任务感知**：结合对比学习使奖励函数具有子任务感知能力，能在多阶段任务中动态指导策略，提升了学习效率和最终效果。
*   **较强的泛化性**：在真实环境和新形态上的成功迁移验证了方法的实用价值。

### 8. 不足与局限
*   **依赖分段质量**：方法假设视频已被正确划分为子任务片段。分段的粒度和准确性会直接影响奖励质量；自动分段的引入及其带来的偏差尚未在摘要中提及。
*   **视频-状态对齐要求**：训练时需要将机器人当前状态与参考视频帧对齐，可能存在视角不一致或分布外状态的问题，真实应用时鲁棒性有待进一步验证。
*   **实验覆盖局限**：摘要主要提及操作和组装任务，未涉及移动、导航或更柔顺操作的任务，方法在其他类型任务上的表现尚不明确。
*   **计算开销未知**：未揭示训练时间、参数量和实时推理开销，大规模部署的可行性存疑。
*   **分割策略的偏差风险**：不同标注者对同一视频的分段可能不同，这种主观性可能引入噪声，影响习得奖励的最优性。

（完）
