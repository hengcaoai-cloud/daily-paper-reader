---
title: "Touch in the Wild: Learning Fine-Grained Manipulation with a Portable Visuo-Tactile Gripper"
title_zh: 野接触：利用便携式视触觉夹爪学习精细操作
authors: "Xinyue Zhu, Binghao Huang, Yunzhu Li"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=WabVVQKTUF"
tags: ["query:robot"]
score: 10.0
evidence: 便携式视触觉夹爪及面向精细操作的跨模态表示学习
tldr: 手持夹爪常用于收集人类示范，但大多缺乏触觉感知。本文提出一种集成触觉传感器的便携轻量夹爪，可在野外同步采集视觉与触觉数据。并设计跨模态表示学习框架，融合视触觉信号且保留各自特性，产生可解释表示，聚焦接触区域。实验表明该方法显著提升了精细操作策略的性能。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有手持数据采集工具缺乏触觉感知，无法捕获精细操作中的关键接触信息。
method: 设计带触觉传感器的便携夹爪，并提出视触觉跨模态表示学习框架。
result: 学习到的表示一致聚焦于接触区域，在精细操作任务上取得显著提升。
conclusion: 为野外环境下的视触觉数据收集与表示学习提供了实用解决方案，促进了基于触觉的精细操作。
---

## Abstract
Handheld grippers are increasingly used to collect human demonstrations due to their ease of deployment and versatility. However, most existing designs lack tactile sensing, despite the critical role of tactile feedback in precise manipulation. We present a portable, lightweight gripper with integrated tactile sensors that enables synchronized collection of visual and tactile data in diverse, real-world, and in-the-wild settings. Building on this hardware, we propose a cross-modal representation learning framework that integrates visual and tactile signals while preserving their distinct characteristics. The learning procedure allows the emergence of interpretable representations that consistently focus on contacting regions relevant for physical interactions. When used for downstream manipulation tasks, these representations enable more efficient and effective policy learning, supporting precise robotic manipulation based on multimodal feedback. We validate our approach on fine-grained tasks such as test tube insertion and pipette-based fluid transfer, demonstrating improved accuracy and robustness under external disturbances. Our project page is available at \url{https://binghao-huang.github.io/touch_in_the_wild/}.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
便携式视触觉夹爪及面向精细操作的跨模态表示学习。

### 2. 核心内容
手持夹爪常用于收集人类示范，但大多缺乏触觉感知。本文提出一种集成触觉传感器的便携轻量夹爪，可在野外同步采集视觉与触觉数据。并设计跨模态表示学习框架，融合视触觉信号且保留各自特性，产生可解释表示，聚焦接触区域。实验表明该方法显著提升了精细操作策略的性能。

### 3. 对应检索需求
visual-tactile cross-modal representation learning for manipulation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=WabVVQKTUF](https://openreview.net/forum?id=WabVVQKTUF)
