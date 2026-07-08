---
title: "Dyana: Benchmarking Dynamic Hand Intelligence"
title_zh: "Dyana: 动态手部智能基准测试"
authors: "Bo-Cheng Hu, Zhonghan Zhao, Gaoang Wang"
date: 2025-09-16
pdf: "https://openreview.net/pdf?id=xafFC4h8OO"
tags: ["query:robot"]
score: 9.0
evidence: 提出动态手部抓取基准(Dyana-12M)和评估套件，支持VLA/扩散策略/VLM评估
tldr: 针对现有手部抓取基准仅关注静态物体的问题，提出Dyana-12M大规模动态抓取基准，含1200万帧人手动态抓取轨迹，并统一评估接口支持VLA、扩散策略和VLM，为灵巧操作策略提供标准化动态评估平台，推动真实场景下的抓取研究。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有手部抓取基准多聚焦静态物体，无法应对真实动态场景中的抓取挑战。
method: 提出Dyana-12M基准，用三种可解释轨迹组合表示目标运动，并构建统一评估套件DGS。
result: 建立起包含1200万帧动态抓取轨迹的大规模基准，支持主流模型统一评估。
conclusion: 为动态灵巧抓取策略提供了一个标准化、可解释的评估框架。
---

## Abstract
Most existing hand grasping benchmarks focus on static objects, which fails to capture the challenges of dynamic, real-world scenarios where targets move and precise timing becomes critical. We first propose the Dynamic Grasp Suite (DGS), a unified platform for dynamic grasp evaluation, and Dyana-12M, a large-scale benchmark with 12M frames of human-hand dynamic grasp trajectories. Dyana-12M represents target motion with three interpretable trajectories: straight-line, circular-arc, and simple-harmonic, which compose into arbitrarily complex trajectories. DGS standardizes interfaces and protocols, supporting the evaluation of three major model zoo: vision–language–action (VLA) agents, diffusion policies, and vision–language models (VLMs). 
Together, DGS and Dyana-12M establish a new paradigm for dynamic grasping, shifting evaluation from static scenes to motion-aware, temporally aligned assessment at scale.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
提出动态手部抓取基准(Dyana-12M)和评估套件，支持VLA/扩散策略/VLM评估。

### 2. 核心内容
针对现有手部抓取基准仅关注静态物体的问题，提出Dyana-12M大规模动态抓取基准，含1200万帧人手动态抓取轨迹，并统一评估接口支持VLA、扩散策略和VLM，为灵巧操作策略提供标准化动态评估平台，推动真实场景下的抓取研究。

### 3. 对应检索需求
benchmarks for evaluating dexterous manipulation policies。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=xafFC4h8OO](https://openreview.net/forum?id=xafFC4h8OO)
