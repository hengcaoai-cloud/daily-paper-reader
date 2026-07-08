---
title: "Vidar: Embodied Video Diffusion Model for Generalist Manipulation"
title_zh: "Vidar: 面向通用操作的具身视频扩散模型"
authors: "Yao Feng, Hengkai Tan, Xinyi Mao, Chendong Xiang, Guodong Liu, Shuhe Huang, Hang Su, Jun Zhu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=CFuNu8dK4s"
tags: ["query:model"]
score: 9.0
evidence: 具身视频扩散模型，利用多视角轨迹和跨形态控制，作为通用操作的基础模型
tldr: Vidar 针对通用操作跨机器人形态泛化难题，利用互联网规模预训练视频扩散模型并在75万条多视角真实机器人轨迹上继续预训练，提出统一观测空间和掩码逆动力学适配器。该方法无需大量同类演示即可实现多平台零样本操控，验证了视频扩散模型作为具身基础模型的有效性。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 通用操作向新机器人形态扩展时通常需要大量同质演示，端到端像素到动作流水线易受背景和视角变化影响。
method: Vidar 使用互联网预训练视频扩散模型作为通用先验，在75万条多视角机器人轨迹上继续预训练，并提出统一观测空间和掩码逆动力学模型作为适配器。
result: 在多机器人平台上实现了强泛化能力，能够在新形态上零样本执行操作任务。
conclusion: 视频扩散模型可以通过大规模具身预训练成为通用的操作先验，有效解决跨形态泛化问题。
---

## Abstract
Scaling general-purpose manipulation to new robot embodiments remains challenging: each platform typically needs large, homogeneous demonstrations, and end-to-end pixel-to-action pipelines may degenerate under background and viewpoint shifts. Based on previous advances in video-based robot control, we present Vidar, consisting of an embodied video diffusion model as the generalizable prior and a masked inverse dynamics model (MIDM) as the adapter. We leverage a video diffusion model pre-trained at Internet scale, and further continuously pre-train it for the embodied domain using 750K multi-view trajectories collected from three real-world robot platforms. For this embodied pre-training, we introduce a unified observation space that jointly encodes robot, camera, task, and scene contexts. The MIDM module learns action-relevant pixel masks without dense labels, grounding the prior into the target embodiment’s action space while suppressing distractors. With only ∼20 minutes of human demonstrations on an unseen robot (∼1% of typical data), Vidar outperforms state-of-the-art baselines and generalizes to unseen tasks, backgrounds, and camera layouts. Our results suggest a scalable recipe for “one prior, many embodiments”: strong, inexpensive video priors together with minimal on-robot alignment.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
具身视频扩散模型，利用多视角轨迹和跨形态控制，作为通用操作的基础模型。

### 2. 核心内容
Vidar 针对通用操作跨机器人形态泛化难题，利用互联网规模预训练视频扩散模型并在75万条多视角真实机器人轨迹上继续预训练，提出统一观测空间和掩码逆动力学适配器。该方法无需大量同类演示即可实现多平台零样本操控，验证了视频扩散模型作为具身基础模型的有效性。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=CFuNu8dK4s](https://openreview.net/forum?id=CFuNu8dK4s)
