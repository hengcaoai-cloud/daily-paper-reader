---
title: Video Generators are Robot Policies
title_zh: 视频生成器即机器人策略
authors: "Junbang Liang, Pavel Tokmakov, Ruoshi Liu, Sruthi Sudhakar, Paarth Shah, Rares Andrei Ambrus, Carl Vondrick"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=cWczH8ontO"
tags: ["query:robot"]
score: 9.0
evidence: 利用视频生成从有限的人类演示数据中学习灵巧操作策略
tldr: 针对灵巧操作中视觉运动策略泛化性差和依赖大量人类演示数据的问题，提出视频策略框架，通过端到端训练视频和动作生成，从极少量演示中提取策略，提升鲁棒性和样本效率，并在新物体、背景上展现强泛化能力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 灵巧操作策略面临分布偏移泛化难、依赖大量人类演示数据的局限。
method: 提出模块化视频策略框架，联合训练视频与动作生成。
result: 从极少量演示中学习策略，显著提高鲁棒性和样本效率。
conclusion: 视频生成作为代理可高效学习灵巧操作策略，减少对演示数据的依赖。
---

## Abstract
Despite tremendous progress in dexterous manipulation, current visuomotor policies remain fundamentally limited by two challenges: they struggle to generalize under perceptual or behavioral distribution shifts, and their performance is constrained by the size of human demonstration data. In this paper, we use video generation as a proxy for robot policy learning to address both limitations simultaneously.
We propose Video Policy, a modular framework that combines video and action generation that can be trained end-to-end. Our results demonstrate that learning to generate videos of robot behavior allows for the extraction of policies with minimal demonstration data, significantly improving robustness and sample efficiency. Our method shows strong generalization to unseen objects, backgrounds, and tasks, both in simulation and the real world. We further highlight that task success is closely tied to the generated video, with action-free video data providing critical benefits for generalizing to novel tasks. By leveraging large-scale video generative models, we achieve superior performance compared to recent VLAs and video-action models, paving the way for more scalable and data-efficient robot policy learning.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
利用视频生成从有限的人类演示数据中学习灵巧操作策略。

### 2. 核心内容
针对灵巧操作中视觉运动策略泛化性差和依赖大量人类演示数据的问题，提出视频策略框架，通过端到端训练视频和动作生成，从极少量演示中提取策略，提升鲁棒性和样本效率，并在新物体、背景上展现强泛化能力。

### 3. 对应检索需求
robot learning from human demonstrations for dexterous tasks。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=cWczH8ontO](https://openreview.net/forum?id=cWczH8ontO)
