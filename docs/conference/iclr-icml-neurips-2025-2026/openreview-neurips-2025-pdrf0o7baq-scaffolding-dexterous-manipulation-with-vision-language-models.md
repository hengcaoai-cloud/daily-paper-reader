---
title: Scaffolding Dexterous Manipulation with Vision-Language Models
title_zh: 利用视觉语言模型为灵巧操作提供脚手架
authors: "Vincent de Bakker, Joey Hejna, Tyler Ga Wei Lum, Onur Celik, Aleksandar Taranovic, Denis Blessing, Gerhard Neumann, Jeannette Bohg, Dorsa Sadigh"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=PdRf0O7baQ"
tags: ["query:robot"]
score: 10.0
evidence: 使用视觉语言模型生成灵巧操作策略学习的参考轨迹
tldr: 灵巧手训练困难，强化学习依赖精心设计的奖励函数，难以扩展。本文提出利用视觉语言模型作为灵活性脚手脚架：通过 VLM 生成参考轨迹，为 RL 策略提供稠密的任务无关奖励和手部位姿目标。实验表明该方法在多种灵巧操作任务上无需手工奖励即可达到高性能，显著减轻了工程负担。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 灵巧操作强化学习需要密集奖励，但手工设计奖励函数繁琐且难以泛化。
method: 采用视觉语言模型生成子目标物体位姿和手部参考轨迹，作为 RL 的稠密引导。
result: 在多种灵巧任务上无需任务特定奖励即达到与手工奖励相当的性能。
conclusion: 展示了通过基础模型增强灵巧操作学习的可行性，为通用灵巧技能训练提供了新范式。
---

## Abstract
Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control. While reinforcement learning (RL) can alleviate the data bottleneck by generating experience in simulation, it typically relies on carefully designed, task-specific reward functions, which hinder scalability and generalization. Thus, contemporary works in dexterous manipulation have often bootstrapped from reference trajectories. These trajectories specify target hand poses that guide the exploration of RL policies and object poses that enable dense, task-agnostic rewards.
However, sourcing suitable trajectories---particularly for dexterous hands---remains a significant challenge. Yet, the precise details in explicit reference trajectories are often unnecessary, as RL ultimately refines the motion. Our key insight is that modern vision-language models (VLMs) already encode the commonsense spatial and semantic knowledge needed to specify tasks and guide exploration effectively. Given a task description (e.g., “open the cabinet”) and a visual scene, our method uses an off-the-shelf VLM to first identify task-relevant keypoints (e.g., handles, buttons) and then synthesize 3D trajectories for hand motion and object motion. Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or ``scaffolds'' with high fidelity. Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies. Moreover, we showcase that our method transfers to real-world robotic hands without any human demonstrations or handcrafted rewards.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
使用视觉语言模型生成灵巧操作策略学习的参考轨迹。

### 2. 核心内容
灵巧手训练困难，强化学习依赖精心设计的奖励函数，难以扩展。本文提出利用视觉语言模型作为灵活性脚手脚架：通过 VLM 生成参考轨迹，为 RL 策略提供稠密的任务无关奖励和手部位姿目标。实验表明该方法在多种灵巧操作任务上无需手工奖励即可达到高性能，显著减轻了工程负担。

### 3. 对应检索需求
embodied foundation models for multi fingered dexterous manipulation tasks。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=PdRf0O7baQ](https://openreview.net/forum?id=PdRf0O7baQ)
