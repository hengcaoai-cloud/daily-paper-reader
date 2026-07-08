---
title: Enhancing Tactile-based Reinforcement Learning for Robotic Control
title_zh: 增强基于触觉的强化学习以实现机器人控制
authors: "Elle Miller, Trevor McInroe, David Abel, Oisin Mac Aodha, Sethu Vijayakumar"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Toy96yYopR"
tags: ["query:robot"]
score: 9.0
evidence: 基于触觉的强化学习通过自监督学习利用稀疏二值接触实现超人灵巧性。
tldr: 针对触觉感知在强化学习中效果不一致的问题，本文开发自监督学习方法，在仅使用本体感知和稀疏二值接触的可扩展设置下有效利用触觉观测。实验证明，稀疏二值触觉信号对灵巧性至关重要，尤其适用于本体制导误差无法察觉的退耦机器人-物体运动，使智能体实现了超人灵巧水平。该工作凸显了简单触觉信号在接触丰富操作中的价值，并为触觉强化学习提供了高效训练策略。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 触觉感知在强化学习中的效果不一致，需要更有效的触觉观测利用方式。
method: 开发自监督学习方法，利用本体感知和稀疏二值接触信号训练强化学习智能体。
result: 稀疏触觉信号对退耦物体运动等灵巧操作至关重要，智能体达到超人灵巧性。
conclusion: 自监督学习能充分发挥触觉在灵巧操作中的作用，弥补纯视觉或本体的不足。
---

## Abstract
Achieving safe, reliable real-world robotic manipulation requires agents to evolve beyond vision and incorporate tactile sensing to overcome sensory deficits and reliance on idealised state information. Despite its potential, the efficacy of tactile sensing in reinforcement learning (RL) remains inconsistent. We address this by developing self-supervised learning (SSL) methodologies to more effectively harness tactile observations, focusing on a scalable setup of proprioception and sparse binary contacts. We empirically demonstrate that sparse binary tactile signals are critical for dexterity, particularly for interactions that proprioceptive control errors do not register, such as decoupled robot-object motions. Our agents achieve superhuman dexterity in complex contact tasks (ball bouncing and Baoding ball rotation). Furthermore, we find that decoupling the SSL memory from the on-policy memory can improve performance. We release the Robot Tactile Olympiad ($\texttt{RoTO}$) benchmark to standardise and promote future research in tactile-based manipulation. Project page: https://elle-miller.github.io/tactile_rl.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于触觉的强化学习通过自监督学习利用稀疏二值接触实现超人灵巧性。

### 2. 核心内容
针对触觉感知在强化学习中效果不一致的问题，本文开发自监督学习方法，在仅使用本体感知和稀疏二值接触的可扩展设置下有效利用触觉观测。实验证明，稀疏二值触觉信号对灵巧性至关重要，尤其适用于本体制导误差无法察觉的退耦机器人-物体运动，使智能体实现了超人灵巧水平。该工作凸显了简单触觉信号在接触丰富操作中的价值，并为触觉强化学习提供了高效训练策略。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=Toy96yYopR](https://openreview.net/forum?id=Toy96yYopR)
