---
title: Egocentric Cross-Embodiment Video Editing via Dual Contrastive Representation Learning
title_zh: 基于双对比表示学习的自我中心跨形态视频编辑
authors: "Zhiyuan Li, Wenyan Yang, Wenshuai Zhao, Yue Ma, Yuanpeng Tu, Pekka Marttinen, Joni Pajarinen"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=hGcb46DWQD"
tags: ["query:robot"]
score: 8.0
evidence: 从第一人称人类视频解耦任务与形态表示，实现跨形态迁移
tldr: 针对从人类视频学习时任务与形态信息纠缠导致适应性差的问题，提出双对比表示学习框架，通过最小化任务与形态潜空间互信息、最大化类内相似性，将第一人称演示视频分解为正交表示，进而生成机器人视图视频，为下游策略学习提供更易迁移的数据。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 人类视频与机器人间分布偏移大，现有方法常产生纠缠表示，适应性有限。
method: 采用双对比目标学习解耦的任务和形态表示，将人类视频编辑为机器人视图视频。
result: 解耦表示显著提高了从人类视频到机器人的迁移效率。
conclusion: 解耦任务与形态信息是提升跨形态视频迁移的有效途径。
---

## Abstract
Learning robotic manipulation from human videos is a promising solution to the data bottleneck in robotics, but the distribution shift between humans and robots remains a critical challenge. Existing approaches often produce entangled representations, where task-relevant information is coupled with human-specific kinematics, limiting their adaptability. We propose a generative framework for cross-embodiment video editing that directly addresses this by learning explicitly disentangled task and embodiment representations. Our method factorizes a demonstration video into two orthogonal latent spaces by enforcing a dual contrastive objective: it minimizes mutual information between the spaces to ensure independence while maximizing intra-space consistency to create stable representations. A parameter-efficient adapter injects these latent codes into a frozen video diffusion model, enabling the synthesis of a coherent robot execution video from a single human demonstration, without requiring paired cross-embodiment data. Experiments show our approach generates temporally consistent and morphologically accurate robot demonstrations, offering a scalable solution to leverage internet-scale human video for robot learning.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
从第一人称人类视频解耦任务与形态表示，实现跨形态迁移。

### 2. 核心内容
针对从人类视频学习时任务与形态信息纠缠导致适应性差的问题，提出双对比表示学习框架，通过最小化任务与形态潜空间互信息、最大化类内相似性，将第一人称演示视频分解为正交表示，进而生成机器人视图视频，为下游策略学习提供更易迁移的数据。

### 3. 对应检索需求
how to use large scale first person human videos for robot dexterous manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=hGcb46DWQD](https://openreview.net/forum?id=hGcb46DWQD)
