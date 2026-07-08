---
title: "Grasp2Grasp: Vision-Based Dexterous Grasp Translation via Schrödinger Bridges"
title_zh: "Grasp2Grasp: 基于薛定谔桥的视觉灵巧抓取翻译"
authors: "Tao Zhong, Jonah Buchanan, Christine Allen-Blanchette"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=inEpyClGV2"
tags: ["query:robot"]
score: 9.0
evidence: 基于视觉的多指手灵巧抓取迁移，使用薛定谔桥方法
tldr: 针对不同形态灵巧手间抓取迁移需配对数据的问题，提出Grasp2Grasp，将抓取翻译建模为潜空间间的随机传输，利用薛定谔桥和物理启发代价函数，从单张视觉观测中为目标手合成功能等效抓取，无需配对演示，实现了跨形态的灵巧抓取泛化。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 跨形态灵巧手抓取迁移通常需要配对演示或手工特定模拟。
method: 将抓取翻译建模为潜空间间的薛定谔桥，用得分匹配和流匹配学习映射。
result: 在多种灵巧手上从源手视觉观测成功合成目标手功能等效抓取。
conclusion: 薛定谔桥为灵巧抓取跨形态迁移提供了随机传输新框架。
---

## Abstract
We propose a new approach to vision-based dexterous grasp translation, which aims to transfer grasp intent across robotic hands with differing morphologies. Given a visual observation of a source hand grasping an object, our goal is to synthesize a functionally equivalent grasp for a target hand without requiring paired demonstrations or hand-specific simulations. We frame this problem as a stochastic transport between grasp distributions using the Schrödinger Bridge formalism. Our method learns to map between source and target latent grasp spaces via score and flow matching, conditioned on visual observations. To guide this translation, we introduce physics-informed cost functions that encode alignment in base pose, contact maps, wrench space, and manipulability. Experiments across diverse hand-object pairs demonstrate that our approach generates stable, physically grounded grasps with strong generalization. This work enables semantic grasp transfer for heterogeneous manipulators and bridges vision-based grasping with probabilistic generative modeling. Additional details at https://grasp2grasp.github.io/.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于视觉的多指手灵巧抓取迁移，使用薛定谔桥方法。

### 2. 核心内容
针对不同形态灵巧手间抓取迁移需配对数据的问题，提出Grasp2Grasp，将抓取翻译建模为潜空间间的随机传输，利用薛定谔桥和物理启发代价函数，从单张视觉观测中为目标手合成功能等效抓取，无需配对演示，实现了跨形态的灵巧抓取泛化。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=inEpyClGV2](https://openreview.net/forum?id=inEpyClGV2)
