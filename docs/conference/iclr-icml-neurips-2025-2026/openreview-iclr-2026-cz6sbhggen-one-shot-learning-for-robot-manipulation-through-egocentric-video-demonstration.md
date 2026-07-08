---
title: One-shot Learning for Robot Manipulation through Egocentric Video Demonstration
title_zh: 基于自我中心视频示范的一次性机器人操作学习
authors: "Xiwen Dengxiong, Xueting Wang, Rui Li, Jiebo Luo, Dongfang Liu, Yunbo Zhang"
date: 2025-09-03
pdf: "https://openreview.net/pdf?id=cz6SbHgGEn"
tags: ["query:robot"]
score: 9.0
evidence: 从单个自我中心视频示范一次性学习机器人操作
tldr: 从自我中心视频中学习操作技能因视角动态变化和环境不确定性而充满挑战。本文提出一种由粗到精的定向操作学习框架，结合集成动作预测模块和强化学习精化模块，使机器人能从单个自我中心视频示范中获取操作技能。实验验证了该方法在多种任务上的有效性，为利用海量第一人称视频数据提供了可扩展途径。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有一次性学习不适用于自我中心视频输入，限制其可扩展性和实际部署。
method: 集成动作预测生成粗略动作，再用强化学习细化工件轨迹，实现由粗到精的定向学习。
result: 机器人能从单个自我中心视频中成功学习多种操作技能。
conclusion: 首次实现了从自我中心视频的一次性机器人操作学习，拓展了从人类视频学习的边界。
---

## Abstract
Learning robot manipulation from egocentric video demonstrations is a challenging and promising direction for embodied intelligence, as it involves dynamic perspectives and uncertain environments. While existing methods have shown success in one-shot or few-shot learning from static videos, they are not applicable to egocentric video inputs, which significantly limits their scalability and real-world deployment. In this paper, we propose a novel coarse-to-fine directional manipulation learning framework that enables robots to acquire manipulation skills from a single egocentric video demonstration. Our method integrates an ensemble action prediction module for coarse action generation and a reinforcement learning-based refinement module for fine-grained, adaptive control. The ensemble module improves robustness by combining multiple diffusion policies, while the reinforcement module ensures accurate execution by refining motions based on real-time feedback. We evaluate our framework on three complex, multi-step manipulation tasks and demonstrate its superior performance over three state-of-the-art baselines in terms of both success rate and task robustness under one-shot egocentric settings.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
从单个自我中心视频示范一次性学习机器人操作。

### 2. 核心内容
从自我中心视频中学习操作技能因视角动态变化和环境不确定性而充满挑战。本文提出一种由粗到精的定向操作学习框架，结合集成动作预测模块和强化学习精化模块，使机器人能从单个自我中心视频示范中获取操作技能。实验验证了该方法在多种任务上的有效性，为利用海量第一人称视频数据提供了可扩展途径。

### 3. 对应检索需求
how to use large scale first person human videos for robot dexterous manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=cz6SbHgGEn](https://openreview.net/forum?id=cz6SbHgGEn)
