---
title: "DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation"
title_zh: DexMachina：面向双臂灵巧操作的功能性动作重定向
authors: "Zhao Mandi, Yifan Hou, Dieter Fox, Yashraj Narang, Ajay Mandlekar, Shuran Song"
date: 2025-09-15
pdf: "https://openreview.net/pdf?id=3c6bnSJwDg"
tags: ["query:robot"]
score: 10.0
evidence: 通过课程式重定向从人类手物示范学习灵巧操作策略
tldr: 从人类示范学习灵巧操作面临动作空间大、时空不连续、具身差异等挑战。DexMachina 提出一种基于课程的算法，利用虚拟物体控制器逐渐减弱强度，使策略在运动与接触引导下逐步接管控制。实验结果在多种任务和灵巧手上显著优于基线方法，并开源了仿真基准。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 人类示范到灵巧手的策略迁移受限于大动作空间和具身差异。
method: 使用强度递减的虚拟物体控制器，以课程方式引导策略逐步学习跟踪物体状态。
result: 在长序双臂灵巧操作任务上表现显著提升，并开源多样化仿真基准。
conclusion: 为从人类示范学习灵巧操作提供了一种有效的重定向方法，推动了人机技能迁移。
---

## Abstract
We study the problem of functional retargeting: learning dexterous manipulation policies to track object states from human hand-object demonstrations. We focus on long-horizon, bimanual tasks with articulated objects, which are challenging due to large action space, spatiotemporal discontinuities, and the embodiment gap between human and robot hands. We propose DexMachina, a novel curriculum-based algorithm: the key idea is to use virtual object controllers with decaying strength: an object is first driven automatically towards its target states, such that the policy can gradually learn to take over under motion and contact guidance. We release a simulation benchmark with a diverse set of tasks and dexterous hands, and show that DexMachina significantly outperforms baseline methods. Our algorithm and benchmark enable a functional comparison for hardware designs, and we present key findings informed by quantitative and qualitative results. With the recent surge in dexterous hand development, we hope this work will provide a useful platform for identifying desirable hardware capabilities and lower the barrier for contributing to future research. Videos and more at \url{project-dexmachina.github.io}

---

## 论文详细总结（自动生成）

### 1. 检索相关性
通过课程式重定向从人类手物示范学习灵巧操作策略。

### 2. 核心内容
从人类示范学习灵巧操作面临动作空间大、时空不连续、具身差异等挑战。DexMachina 提出一种基于课程的算法，利用虚拟物体控制器逐渐减弱强度，使策略在运动与接触引导下逐步接管控制。实验结果在多种任务和灵巧手上显著优于基线方法，并开源了仿真基准。

### 3. 对应检索需求
robot learning from human demonstrations for dexterous tasks。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=3c6bnSJwDg](https://openreview.net/forum?id=3c6bnSJwDg)
