---
title: "Vidarc: Low Latency Embodied Video Diffusion Model with Closed-loop Control"
title_zh: Vidarc：低延迟具身视频扩散模型与闭环控制
authors: "Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu"
date: 2025-09-08
pdf: "https://openreview.net/pdf?id=gsvjCTIYPb"
tags: ["query:model"]
score: 7.0
evidence: Vidarc：一种用于机器人操作的带有闭环控制的自回归具身视频扩散模型。
tldr: 针对机器人臂在数据稀缺环境中的操作挑战，现有视频方法虽能利用互联网视频预训练捕捉物理交互，但延迟高且缺乏具身闭环接地。本文提出 Vidarc，一种自回归具身视频扩散方法，通过动作相关掩码结合逆动力学模型进行接地，并融入实时反馈实现闭环控制。该方法在数据稀缺条件下实现了低延迟的机器人操作，为利用视频预训练进行高效闭环控制提供了新思路。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有视频预训练方法用于机器人操作时存在高延迟和缺乏具身闭环控制的问题。
method: 提出 Vidarc，自回归视频扩散模型，利用掩码逆动力学模型进行动作接地和实时闭环控制。
result: 在数据稀缺场景下，Vidarc 实现了低延迟且有效的机器人臂操作。
conclusion: 视频扩散模型结合逆动力学接地为资源有限条件下的机器人控制提供了高效方案。
---

## Abstract
Robotic arm manipulation in data-scarce settings is a highly challenging task due to the complex embodiment dynamics and diverse contexts. Recent video-based approaches have shown great promise in capturing and transferring the temporal and physical interactions by pre-training on Internet-scale video data. However, such methods are often not optimized for the embodiment-specific closed-loop control, typically suffering from high latency and insufficient grounding. In this paper, we present Vidarc (Video Diffusion for Action Reasoning and Closed-loop Control), a novel autoregressive embodied video diffusion approach augmented by a masked inverse dynamics model. By grounding video predictions with action-relevant masks and incorporating real-time feedback through cached autoregressive generation, Vidarc achieves fast, accurate closed-loop control. Pre-trained on one million cross-embodiment episodes, Vidarc surpasses state-of-the-art baselines, achieving at least a 15% higher success rate in real-world deployment and a 91% reduction in latency. We also highlight its robust generalization and error correction capabilities across previously unseen robotic platforms.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
Vidarc：一种用于机器人操作的带有闭环控制的自回归具身视频扩散模型。

### 2. 核心内容
针对机器人臂在数据稀缺环境中的操作挑战，现有视频方法虽能利用互联网视频预训练捕捉物理交互，但延迟高且缺乏具身闭环接地。本文提出 Vidarc，一种自回归具身视频扩散方法，通过动作相关掩码结合逆动力学模型进行接地，并融入实时反馈实现闭环控制。该方法在数据稀缺条件下实现了低延迟的机器人操作，为利用视频预训练进行高效闭环控制提供了新思路。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=gsvjCTIYPb](https://openreview.net/forum?id=gsvjCTIYPb)
