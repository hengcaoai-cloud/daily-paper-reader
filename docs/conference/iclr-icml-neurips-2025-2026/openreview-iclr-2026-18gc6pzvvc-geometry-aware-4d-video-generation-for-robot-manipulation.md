---
title: Geometry-aware 4D Video Generation for Robot Manipulation
title_zh: 几何感知的4D视频生成用于机器人操作
authors: "Zeyi Liu, Shuang Li, Eric Cousineau, Siyuan Feng, Benjamin Burchfiel, Shuran Song"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=18gC6pZVVc"
tags: ["query:model"]
score: 4.0
evidence: 生成几何一致的4D视频用于机器人操作，为具身模型提供3D空间理解
tldr: 该工作针对视频生成模型缺乏多视角三维一致性的问题，提出通过跨视角点图对齐监督来学习共享3D场景表示，从单张RGB-D图像生成时空一致的未来视频序列。该方法增强了机器人操作规划中的空间理解能力，可为具身模型提供几何感知的视频预训练数据。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有视频生成模型难以同时保持时序连贯性和跨视角几何一致性，限制了在机器人操作中的应用。
method: 通过跨视角点图对齐训练4D视频生成模型，学习共享3D场景表示。
result: 能够从单张RGB-D图像生成多视角一致的未来视频，在合成和真实数据上验证了时空对齐效果。
conclusion: 几何感知的4D视频生成有望为机器人操作提供更可靠的空间推理先验。
---

## Abstract
Understanding and predicting dynamics of the physical world can enhance a robot's ability to plan and interact effectively in complex environments. While recent video generation models have shown strong potential in modeling dynamic scenes, generating videos that are both temporally coherent and geometrically consistent across camera views remains a significant challenge. To address this, we propose a 4D video generation model that enforces multi-view 3D consistency of generated videos by supervising the model with cross-view pointmap alignment during training. Through this geometric supervision, the model learns a shared 3D scene representation, enabling it to generate spatio-temporally aligned future video sequences from novel viewpoints given a single RGB-D image per view, and without relying on camera poses as input. Compared to existing baselines, our method produces more visually stable and spatially aligned predictions across multiple simulated and real-world robotic datasets. We further show that the predicted 4D videos can be used to recover robot end-effector trajectories using an off-the-shelf 6DoF pose tracker, yielding robot manipulation policies that generalize well to novel camera viewpoints.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
生成几何一致的4D视频用于机器人操作，为具身模型提供3D空间理解。

### 2. 核心内容
该工作针对视频生成模型缺乏多视角三维一致性的问题，提出通过跨视角点图对齐监督来学习共享3D场景表示，从单张RGB-D图像生成时空一致的未来视频序列。该方法增强了机器人操作规划中的空间理解能力，可为具身模型提供几何感知的视频预训练数据。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=18gC6pZVVc](https://openreview.net/forum?id=18gC6pZVVc)
