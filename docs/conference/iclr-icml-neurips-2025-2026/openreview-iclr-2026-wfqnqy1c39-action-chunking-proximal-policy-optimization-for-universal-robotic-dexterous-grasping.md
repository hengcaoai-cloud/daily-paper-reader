---
title: Action Chunking Proximal Policy Optimization for Universal Robotic Dexterous Grasping
title_zh: 动作分块近端策略优化用于通用机器人灵巧抓取
authors: "Sanghyun Hahn, Jonghyun Choi"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=WFQnqY1c39"
tags: ["query:robot"]
score: 9.0
evidence: 使用动作分块PPO实现通用多指灵巧抓取
tldr: 针对多指灵巧抓取中普通PPO探索不足的问题，提出动作分块PPO方法，通过时序连贯的动作提升探索效果，实现通用的灵巧抓取策略。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 普通PPO在多指手灵巧抓取中存在探索不足和策略改进缓慢的问题。
method: 提出将动作分块与PPO结合，生成时序连贯的动作以改善探索。
result: 在多种物体上实现了通用灵巧抓取，策略性能提升。
conclusion: 动作分块PPO有效提升灵巧抓取探索效率，实现通用抓取能力。
---

## Abstract
Universal dexterous grasping across diverse objects is a crucial step towards human-like manipulation. 
In order to handle the high degrees of freedom (DoF) of dexterous hands, state-of-the-art universal dexterous grasping methods adopt online reinforcement learning (RL) algorithms such as Proximal Policy Optimization (PPO) to learn action policies.
Although PPO is a common choice, its vanilla version often leads to insufficient exploration and slow policy improvement, requiring additional training augmentation to achieve high performance.
While action chunking is a promising strategy to improve exploration by temporally coherent actions, prior RL algorithms that integrate action chunking are unsuitable for dexterous hands due to their high-DoF Q-functions.
To address this, we reformulate the PPO objective over action chunks and use a standard state-value function as the critic, naming \emph{Action Chunking Proximal Policy Optimization} (ACPPO). 
ACPPO retains the simplicity of PPO while encouraging temporally coherent exploration and avoiding the curse of dimensionality.
Validating on the DexGraspNet dataset, we observe that ACPPO outperforms all prior PPO-based methods by a success rate of 95.4\% with $2.3\times$ faster training without any auxiliary learning mechanisms.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
使用动作分块PPO实现通用多指灵巧抓取。

### 2. 核心内容
针对多指灵巧抓取中普通PPO探索不足的问题，提出动作分块PPO方法，通过时序连贯的动作提升探索效果，实现通用的灵巧抓取策略。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=WFQnqY1c39](https://openreview.net/forum?id=WFQnqY1c39)
