---
title: "DexCanvas: Bridging Human Demonstrations and Robot Learning for Dexterous Manipulation"
title_zh: DexCanvas：连接人类示范与灵巧操作机器人学习
authors: "Xinyue Xu, Jieqiang Sun, Jing Dai, Siyuan Chen, Lanjie Ma, Ke Sun, Bin Zhao, Jianbo Yuan, Yiwen Lu"
date: 2025-09-20
pdf: "https://openreview.net/pdf?id=K2ceVeoqbL"
tags: ["query:robot"]
score: 10.0
evidence: 基于人类示范的大规模虚实混合灵巧操作数据集
tldr: 灵巧操作数据不足阻碍了机器人学习。DexCanvas 构建了一个包含 7000 小时灵巧手物交互的混合真实-合成数据集，涵盖 21 种操作类型，提供多视角 RGB-D、动作捕捉、接触点及力剖面。通过仿真中训练 MANO 手策略，该数据集首次大规模提供了物理一致的接触力标注。为灵巧操作研究提供了宝贵的数据基础。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 缺乏大规模、多模态且带物理一致性接触力的灵巧操作数据集。
method: 从 70 小时真实人类示范扩展生成 7000 小时合成数据，并通过强化学习在仿真中复现接触力。
result: 构建了首个包含接触力标注的大规模灵巧操作数据集，在 21 种操作类型上验证了有效性。
conclusion: 为灵巧操作领域提供了标准化、可扩展的数据生成与评估基准。
---

## Abstract
We present DexCanvas, a large-scale hybrid real-synthetic human manipulation dataset containing 7,000 hours of dexterous hand-object interactions seeded from 70 hours of real human demonstrations, organized across 21 fundamental manipulation types based on the Cutkosky taxonomy. Each entry combines synchronized multi-view RGB-D, high-precision mocap with MANO hand parameters, and per-frame contact points with physically consistent force profiles. Our real-to-sim pipeline uses reinforcement learning to train policies that control an actuated MANO hand in physics simulation, reproducing human demonstrations while discovering the underlying contact forces that generate the observed object motion. DexCanvas is the first manipulation dataset to combine large-scale real demonstrations, systematic skill coverage based on established taxonomies, and physics-validated contact annotations. The dataset can facilitate research in robotic manipulation learning, contact-rich control, and skill transfer across different hand morphologies.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于人类示范的大规模虚实混合灵巧操作数据集。

### 2. 核心内容
灵巧操作数据不足阻碍了机器人学习。DexCanvas 构建了一个包含 7000 小时灵巧手物交互的混合真实-合成数据集，涵盖 21 种操作类型，提供多视角 RGB-D、动作捕捉、接触点及力剖面。通过仿真中训练 MANO 手策略，该数据集首次大规模提供了物理一致的接触力标注。为灵巧操作研究提供了宝贵的数据基础。

### 3. 对应检索需求
datasets for robot dexterous manipulation and grasping。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=K2ceVeoqbL](https://openreview.net/forum?id=K2ceVeoqbL)
