---
title: Visuo-Tactile World Models
title_zh: 视觉触觉世界模型
authors: "Carolina Higuera, Sergio Arnaud, Byron Boots, Mustafa Mukadam, Francois Robert Hogan, Franziska Meier"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=zKQSyT7a7n"
tags: ["query:robot"]
score: 10.0
evidence: 融合视觉与触觉的多任务世界模型用于接触丰富操作
tldr: 提出多任务视觉触觉世界模型，通过触觉推理捕捉接触物理，改善视觉遮挡下的物体交互理解，在想象和规划中提升物理保真度，并在真实机器人零样本操作中验证。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 纯视觉模型在遮挡或接触模糊状态下易出现物体消失等物理违反。
method: 训练多任务世界模型融合视觉和触觉，进行触觉推理。
result: "物体持久性提高33%，运动规律遵守提高29%，提升规划效果。"
conclusion: 视觉触觉融合显著改善接触丰富的操作任务中的物理理解与规划。
---

## Abstract
We introduce multi-task Visuo-Tactile World Models (VT-WM), which capture the physics of contact through touch reasoning. By complementing vision with tactile sensing, VT-WM better understands robot–object interactions in contact-rich tasks, avoiding common failure modes of vision-only models under occlusion or ambiguous contact states, such as objects disappearing, teleporting, or moving in ways that violate basic physics. Trained across a set of contact-rich manipulation tasks, VT-WM improves physical fidelity in imagination, achieving 33\% better performance at maintaining object permanence and 29\% better compliance with the laws of motion in autoregressive rollouts. Moreover, experiments show that grounding in contact dynamics also translates to planning. In zero-shot real-robot experiments, VT-WM achieves up to 35\% higher success rates, with the largest gains in multi-step, contact-rich tasks. Finally, VT-WM shows data efficiency when targeting a new task, outperforming a behavioral cloning policy  by over 3.5$\times$ in success rate with limited demonstrations.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
融合视觉与触觉的多任务世界模型用于接触丰富操作。

### 2. 核心内容
提出多任务视觉触觉世界模型，通过触觉推理捕捉接触物理，改善视觉遮挡下的物体交互理解，在想象和规划中提升物理保真度，并在真实机器人零样本操作中验证。

### 3. 对应检索需求
visual-tactile cross-modal representation learning for manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=zKQSyT7a7n](https://openreview.net/forum?id=zKQSyT7a7n)
