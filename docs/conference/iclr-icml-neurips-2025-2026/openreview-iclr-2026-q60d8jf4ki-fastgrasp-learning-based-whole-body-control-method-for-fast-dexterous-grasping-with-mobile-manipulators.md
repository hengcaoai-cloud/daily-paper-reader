---
title: "FastGrasp: Learning-based Whole-body Control method for Fast Dexterous Grasping with Mobile Manipulators"
title_zh: "FastGrasp: 基于学习的移动机器人全身控制快速灵巧抓取方法"
authors: "Heng Tao, Yiming Zhong, Zemin Yang, Hengan Zhou, Yuexin Ma"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=Q60D8jF4KI"
tags: ["query:robot"]
score: 9.0
evidence: 融合抓取引导、全身控制和触觉反馈实现快速灵巧抓取
tldr: 针对移动机器人高速抓取中冲击稳定、实时协调和泛化难题，提出结合抓取引导、全身控制和触觉反馈的FastGrasp框架，通过两阶段强化学习实现快速灵巧抓取。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 高速运动下移动抓取面临冲击稳定、全身协调和泛化挑战。
method: 两阶段强化学习：首先生成抓取候选，然后执行带触觉反馈的全身协调运动。
result: 在移动平台上实现快速、泛化的灵巧抓取。
conclusion: 触觉反馈和全身控制对高速灵巧抓取至关重要。
---

## Abstract
Fast grasping is critical for mobile robots in logistics, manufacturing, and service applications. Existing methods face fundamental challenges in impact stabilization under high-speed motion, real-time whole-body coordination, and generalization across diverse objects and scenarios, limited by fixed bases, simple grippers, or slow tactile response capabilities. We propose **FastGrasp**, a learning-based framework that integrates grasp guidance, whole-body control, and tactile feedback for mobile fast grasping. Our two-stage reinforcement learning strategy first generates diverse grasp candidates via conditional variational autoencoder conditioned on object point clouds, then executes coordinated movements of mobile base, arm, and hand guided by optimal grasp selection. Tactile sensing enables real-time grasp adjustments to handle impact effects and object variations. Extensive experiments demonstrate superior grasping performance in both simulation and real-world scenarios, achieving robust manipulation across diverse object geometries through effective sim-to-real transfer.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
融合抓取引导、全身控制和触觉反馈实现快速灵巧抓取。

### 2. 核心内容
针对移动机器人高速抓取中冲击稳定、实时协调和泛化难题，提出结合抓取引导、全身控制和触觉反馈的FastGrasp框架，通过两阶段强化学习实现快速灵巧抓取。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=Q60D8jF4KI](https://openreview.net/forum?id=Q60D8jF4KI)
