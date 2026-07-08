---
title: "DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation"
title_zh: "DynaRend: 通过遮掩未来渲染学习三维动力学用于机器人操作"
authors: "Jingyi Tian, Le Wang, Sanping Zhou, Sen Wang, lijiayi, Gang Hua"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=r4dzaP61QH"
tags: ["query:model"]
score: 7.0
evidence: 通过自监督学习三维动态特征以用于机器人操作
tldr: 针对现有操作表征学习未能联合学习几何、语义和动力学的问题，提出DynaRend框架，通过遮掩重建和未来预测学习三维意识的三维平面特征，增强操作策略的泛化能力。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 机器人操作策略泛化受限于缺乏多样真实数据，现有表征学习未能同时学习几何、语义和动力学。
method: 通过遮掩三维渲染和未来预测，学习三维意识的三维平面特征。
result: 学习到的特征有效捕获三维动态信息，提升操作表现。
conclusion: 联合学习三维几何和动态信息对操作泛化至关重要。
---

## Abstract
Learning generalizable robotic manipulation policies remains a key challenge due to the scarcity of diverse real-world training data. While recent approaches have attempted to mitigate this through self-supervised representation learning, most either rely on 2D vision pretraining paradigms such as masked image modeling, which primarily focus on static semantics or scene geometry, or utilize large-scale video prediction models that emphasize 2D dynamics, thus failing to jointly learn the geometry, semantics, and dynamics required for effective manipulation. In this paper, we present DynaRend, a representation learning framework that learns 3D-aware and dynamics-informed triplane features via masked reconstruction and future prediction using differentiable volumetric rendering. By pretraining on multi-view RGB-D video data, DynaRend jointly captures spatial geometry, future dynamics, and task semantics in a unified triplane representation. The learned representations can be effectively transferred to downstream robotic manipulation tasks via action value map prediction. We evaluate DynaRend on two challenging benchmarks, RLBench and Colosseum, as well as in real-world robotic experiments, demonstrating substantial improvements in policy success rate, generalization to environmental perturbations, and real-world applicability across diverse manipulation tasks.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
通过自监督学习三维动态特征以用于机器人操作。

### 2. 核心内容
针对现有操作表征学习未能联合学习几何、语义和动力学的问题，提出DynaRend框架，通过遮掩重建和未来预测学习三维意识的三维平面特征，增强操作策略的泛化能力。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=r4dzaP61QH](https://openreview.net/forum?id=r4dzaP61QH)
