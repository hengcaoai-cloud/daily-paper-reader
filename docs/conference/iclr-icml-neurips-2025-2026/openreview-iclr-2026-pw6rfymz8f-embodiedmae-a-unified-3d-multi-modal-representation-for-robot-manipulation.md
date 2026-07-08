---
title: "EmbodiedMAE: A Unified 3D Multi-Modal Representation for Robot Manipulation"
title_zh: EmbodiedMAE：面向机器人操作的统一三维多模态表征
authors: "Zibin Dong, Fei Ni, Yifu Yuan, Yinchuan Li, Jianye HAO"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=pW6rFymZ8F"
tags: ["query:model"]
score: 8.0
evidence: 统一的三维多模态掩码自编码器，跨模态学习表征用于机器人操作
tldr: 针对机器人操作中三维信息利用不足的问题，EmbodiedMAE提出一种多模态掩码自编码器，在增强的DROID-3D数据集上同时学习RGB、深度和点云的表征。该统一三维表征在多种操作任务上显著优于现有视觉模型，为实现具身基础模型的三维空间理解提供了有效路径。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 当前机器人操作模型缺乏有效的三维信息融合，域差距大。
method: 在DROID-3D上训练多模态掩码自编码器，跨RGB、深度、点云学习统一三维表征。
result: 在多项操作任务中，EmbodiedMAE表征性能超越最先进的视觉模型。
conclusion: EmbodiedMAE为机器人操作提供了强大的三维多模态感知表征，助力具身基础模型发展。
---

## Abstract
We present EmbodiedMAE, a unified 3D multi-modal representation for robot manipulation. Current approaches suffer from significant domain gaps between training datasets and robot manipulation tasks, while also lacking model architectures that can effectively incorporate 3D information. To overcome these limitations, we enhance the DROID dataset with high-quality depth maps and point clouds, constructing DROID-3D as a valuable supplement for 3D embodied vision research. Then we develop EmbodiedMAE, a multi-modal masked autoencoder that simultaneously learns representations across RGB, depth, and point cloud modalities through stochastic masking and cross-modal fusion. Trained on DROID-3D, EmbodiedMAE consistently outperforms state-of-the-art vision foundation models (VFMs) in both training efficiency and final performance across 70 simulation tasks and 20 real-world robot manipulation tasks on two robot platforms. The model exhibits strong scaling behavior with size and promotes effective policy learning from 3D inputs. Experimental results establish EmbodiedMAE as a reliable unified 3D multi-modal VFM for embodied AI systems, particularly in precise tabletop manipulation settings where spatial perception is critical.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
统一的三维多模态掩码自编码器，跨模态学习表征用于机器人操作。

### 2. 核心内容
针对机器人操作中三维信息利用不足的问题，EmbodiedMAE提出一种多模态掩码自编码器，在增强的DROID-3D数据集上同时学习RGB、深度和点云的表征。该统一三维表征在多种操作任务上显著优于现有视觉模型，为实现具身基础模型的三维空间理解提供了有效路径。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=pW6rFymZ8F](https://openreview.net/forum?id=pW6rFymZ8F)
