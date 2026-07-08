---
title: "D-REX: Differentiable Real-to-Sim-to-Real Engine for Learning Dexterous Grasping"
title_zh: "D-REX: 用于学习灵巧抓取的可微现实-仿真-现实引擎"
authors: "Haozhe Lou, Mingtong Zhang, Haoran Geng, Hanyang Zhou, Sicheng He, Zhiyuan Gao, Siheng Zhao, Jiageng Mao, Pieter Abbeel, Jitendra Malik, Daniel Seita, Yue Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=13jshGCK9i"
tags: ["query:robot"]
score: 8.0
evidence: 用于学习灵巧抓取的可微现实-仿真-现实引擎
tldr: 针对灵巧抓取中仿真到现实的差距，提出基于高斯泼溅的可微引擎，结合质量辨识和策略学习，构建高保真数字孪生体，实现灵巧抓取策略的自动学习。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 灵巧抓取中仿真与真实世界动力学差距大，物理参数辨识困难。
method: 利用高斯泼溅构建可微引擎，优化物体质量以构建数字孪生。
result: 同时实现物体质量辨识和灵巧抓取策略学习。
conclusion: 可微引擎有效弥合灵巧抓取的仿真-现实差距。
---

## Abstract
Simulation provides a cost-effective and flexible platform for data generation and policy learning to develop robotic systems. However, bridging the gap between simulation and real-world dynamics remains a significant challenge, especially in physical parameter identification. In this work, we introduce a real-to-sim-to-real engine that leverages the Gaussian Splat representations to build a differentiable engine, enabling object mass identification from real-world visual observations and robot control signals, while enabling grasping policy learning simultaneously. Through optimizing the mass of the manipulated object, our method automatically builds high-fidelity and physically plausible digital twins. Additionally, we propose a novel approach to train force-aware grasping policies from limited data by transferring feasible human demonstrations into simulated robot demonstrations. Through comprehensive experiments, we demonstrate that our engine achieves accurate and robust performance in mass identification across various object geometries and mass values. Those optimized mass values facilitate force-aware policy learning, achieving superior and high performance in object grasping, effectively reducing the sim-to-real gap.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
用于学习灵巧抓取的可微现实-仿真-现实引擎。

### 2. 核心内容
针对灵巧抓取中仿真到现实的差距，提出基于高斯泼溅的可微引擎，结合质量辨识和策略学习，构建高保真数字孪生体，实现灵巧抓取策略的自动学习。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=13jshGCK9i](https://openreview.net/forum?id=13jshGCK9i)
