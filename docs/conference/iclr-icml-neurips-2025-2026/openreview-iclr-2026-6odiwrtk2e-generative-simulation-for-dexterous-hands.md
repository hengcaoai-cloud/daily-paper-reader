---
title: Generative Simulation for Dexterous Hands
title_zh: GenDexHand：面向灵巧手的生成式仿真
authors: "Feng Chen, Zhuxiu Xu, Tianzhe Chu, Xunzhe Zhou, Li Sun, Zewen Wu, Shenghua Gao, Zhongyu Li, Yanchao Yang, Yi Ma"
date: 2025-09-01
pdf: "https://openreview.net/pdf?id=6oDiWrtk2e"
tags: ["query:robot"]
score: 10.0
evidence: 自主生成多样化的灵巧手任务和环境
tldr: GenDexHand针对灵巧手操作数据稀缺的问题，提出一种生成式仿真管线，通过视觉语言模型引导的闭环优化自动生成多样化、可训练的灵巧操作任务。该方法能调整物体摆放和尺寸，确保任务可行性，从而大规模合成多指手操作数据，突破了现有方法仅适用于夹爪的局限，显著增强了具身智能的数据基础。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 灵巧手操作因自由度更高而难度更大，现有方法难以大规模生成可行且可训练的任务。
method: 提出基于VLM的闭环优化生成管线，自动生成多样化的灵巧手操作任务和环境。
result: 能够大规模产生灵巧手操作数据，缓解了多指手策略学习的数据瓶颈。
conclusion: 为灵巧操作的仿真数据生成提供了自动化解决方案，促进了灵巧手策略的学习和泛化。
---

## Abstract
Data scarcity remains a fundamental bottleneck for embodied intelligence. 
Existing approaches use large language models (LLMs) to automate gripper‑based simulation generation, but they transfer poorly to dexterous manipulation, which demands more specialized environment design. Meanwhile, dexterous manipulation tasks are inherently more difficult due to their higher degrees of freedom. Massively generating feasible and trainable dexterous hand tasks remains an open challenge. To this end, we present **GenDexHand**, a *generative simulation pipeline* that autonomously produces diverse robotic tasks and environments for dexterous manipulation. **GenDexHand** introduces a closed‑loop refinement process that adjusts object placements and scales based on vision‑language model (VLM) feedback, substantially improving the average quality of generated environments. Each task is further decomposed into sub‑tasks to enable sequential reinforcement learning, reducing training time and increasing success rates.
Our work provides a viable path toward scalable training of diverse dexterous hand behaviors in embodied intelligence by offering a simulation-based solution to synthetic data generation. Our anonymous website: https://sites.google.com/view/gendexhand.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
自主生成多样化的灵巧手任务和环境。

### 2. 核心内容
GenDexHand针对灵巧手操作数据稀缺的问题，提出一种生成式仿真管线，通过视觉语言模型引导的闭环优化自动生成多样化、可训练的灵巧操作任务。该方法能调整物体摆放和尺寸，确保任务可行性，从而大规模合成多指手操作数据，突破了现有方法仅适用于夹爪的局限，显著增强了具身智能的数据基础。

### 3. 对应检索需求
datasets for robot dexterous manipulation and grasping。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=6oDiWrtk2e](https://openreview.net/forum?id=6oDiWrtk2e)
