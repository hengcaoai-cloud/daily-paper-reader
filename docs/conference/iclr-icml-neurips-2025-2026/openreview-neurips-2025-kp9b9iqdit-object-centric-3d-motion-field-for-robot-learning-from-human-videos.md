---
title: Object-centric 3D Motion Field for Robot Learning from Human Videos
title_zh: 物体中心3D运动场：从人类视频进行机器人学习
authors: "Zhao-Heng Yin, Sherry Yang, Pieter Abbeel"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=kp9B9iQDIt"
tags: ["query:robot"]
score: 9.0
evidence: 以物体中心3D运动场作为从人类视频学习的动作表示
tldr: 针对从人类视频提取动作表示用于策略学习的难题，提出物体中心3D运动场表示，设计去噪估计器从视频中提取细粒度物体3D运动，并训练策略实现零样本控制，在模拟与真实机器人上验证了该表示在复杂操作任务中的优越性。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有动作表示如像素流、点云流存在建模复杂或信息丢失等问题。
method: 提出用物体中心3D运动场表示动作，并设计去噪估计器从视频中提取该表示。
result: 以此训练的策略在物体操作任务上实现零样本控制，优于其他表示。
conclusion: 物体中心3D运动场是一种信息丰富且适合从视频学习的动作表示。
---

## Abstract
Learning robot control policies from human videos is a promising direction for scaling up robot learning. However, how to extract action knowledge (or action representations) from videos for policy learning remains a key challenge. Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information. In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this representation from videos for zero-shot control. We introduce two novel components. First, a novel training pipeline for training a ``denoising'' 3D motion field estimator to extract fine object 3D motions from human videos with noisy depth robustly. Second, a dense object-centric 3D motion field prediction architecture that favors both cross-embodiment transfer and policy generalization to background. We evaluate the system in real world setups. Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior approaches fail ($\lesssim 10$\%), and can even acquire fine-grained manipulation skills like insertion.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
以物体中心3D运动场作为从人类视频学习的动作表示。

### 2. 核心内容
针对从人类视频提取动作表示用于策略学习的难题，提出物体中心3D运动场表示，设计去噪估计器从视频中提取细粒度物体3D运动，并训练策略实现零样本控制，在模拟与真实机器人上验证了该表示在复杂操作任务中的优越性。

### 3. 对应检索需求
how to use large scale first person human videos for robot dexterous manipulation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=kp9B9iQDIt](https://openreview.net/forum?id=kp9B9iQDIt)
