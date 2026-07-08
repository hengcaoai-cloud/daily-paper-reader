---
title: "House Of Dextra : Cross-Embodied Co-Design for Dexterous Hands"
title_zh: House Of Dextra：灵巧手的跨体现协同设计
authors: "Kehlani Fay, Darin Anthony Djapri, Anya Zorin, James Clinton, Ali El Lahib, Hao Su, Michael T. Tolley, Sha Yi, Xiaolong Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=k8ovuXEQQu"
tags: ["query:robot"]
score: 10.0
evidence: 面向特定任务的灵巧手形态与控制协同设计框架
tldr: House Of Dextra针对灵巧手设计缺乏共识的问题，提出一种协同设计框架，通过形态条件交叉体现控制同时学习任务特定的手部形态和控制策略。该框架支持关节、手指和手掌生成等广阔的设计空间，并利用可访问组件进行真实世界制造，在多个灵巧任务中验证了方法的有效性，为灵巧操作的最佳设计提供了新的范式。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 灵巧操作受限于控制与设计，对手部最优形态缺乏共识。
method: 提出协同设计框架，学习任务特定的手部形态及其对应的灵巧控制策略。
result: 在包括手中旋转在内的多个灵巧任务上进行了仿真和真实世界验证。
conclusion: 该方法为灵巧手的设计与控制提供了联合优化途径，推动了最佳操作器的开发。
---

## Abstract
Dexterous manipulation is limited by both control and design, without consensus as to what makes manipulators best for performing dexterous tasks. This raises a fundamental challenge: how should we design and control robot manipulators that are optimized for dexterity? We present a co-design framework that learns task-specific hand morphology and complementary dexterous control policies. The framework supports 1) an expansive morphology search space including joint, finger, and palm generation, 2) scalable evaluation across the wide design space via morphology-conditioned cross-embodied control, and 3) real-world fabrication with accessible components. We evaluate the approach across multiple dexterous tasks, including in-hand rotation with simulation and real deployment. Our framework enables an end-to-end pipeline that can design, train, fabricate, and deploy a new robotic hand in under 24 hours. The full framework is open-sourced and available on our website.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向特定任务的灵巧手形态与控制协同设计框架。

### 2. 核心内容
House Of Dextra针对灵巧手设计缺乏共识的问题，提出一种协同设计框架，通过形态条件交叉体现控制同时学习任务特定的手部形态和控制策略。该框架支持关节、手指和手掌生成等广阔的设计空间，并利用可访问组件进行真实世界制造，在多个灵巧任务中验证了方法的有效性，为灵巧操作的最佳设计提供了新的范式。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=k8ovuXEQQu](https://openreview.net/forum?id=k8ovuXEQQu)
