---
title: "AuxVLA: Auxiliary Task Learning and Multi-Modal Enhancement for Vision-Language-Action Models in Mobile Manipulation"
title_zh: AuxVLA：移动操作中视觉-语言-动作模型的辅助任务学习与多模态增强
authors: "Ruisen Tu, Arth Shukla, Sohyun Yoo, Xuanlin Li, Junxi Li, Jianwen Xie, Hao Su, Zhuowen Tu"
date: 2025-09-15
pdf: "https://openreview.net/pdf?id=lcuA4RYit9"
tags: ["query:model"]
score: 6.0
evidence: AuxVLA 通过辅助任务和多模态输入增强 VLA 模型，用于移动操作。
tldr: 当前 VLA 模型在家庭场景中的复杂移动操作任务上表现不佳，尤其面对高维动作空间（手臂和移动底盘的 13 维）。本文提出 AuxVLA，通过辅助任务协同训练和增强输入模态（多视角视觉与深度信息）提升 VLA 模型控制移动操作机器人的能力。实验证明该方法能有效改善直接模仿学习的次优结果，为移动操作中的 VLA 应用提供了可行方案。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: VLA 模型在控制移动操作机器人的高维动作空间时，直接模仿学习效果不佳。
method: 提出 AuxVLA，结合辅助任务协同训练和多视角视觉、深度输入来增强 VLA 模型。
result: 方法在家庭场景移动操作任务上取得优于基线 VLA 模型的性能。
conclusion: 辅助任务与多模态增强能有效提升 VLA 在复杂移动操作中的表现。
---

## Abstract
Vision-Language-Action (VLA) models have shown promise for robotic control, but their application to complex household manipulation tasks remains challenging. In this work, we propose AuxVLA, a comprehensive approach that enables VLA models to control mobile manipulation robots in domestic environments through both auxiliary task co-training and enhanced input modalities. Our method addresses the challenges of controlling high-dimensional action spaces (13 dimensions for both arm and mobile base) where direct imitation learning typically yields suboptimal results. AuxVLA incorporates two complementary strategies: (1) leveraging multi-view visual inputs and depth information to provide richer spatial context, and (2) co-training with auxiliary decoders that predict interpretable intermediate representations including global robot position, joint configurations, grasp affordances, target object relative positions, and segmentation masks from shared visual-language features. Through evaluation on home rearrangement tasks, AuxVLA demonstrates favorable performance across picking, placing, opening and closing tasks. We hypothesize that auxiliary supervision on interpretable representations enhances spatial understanding and scene reasoning capabilities, while enriched sensory inputs provide necessary spatial context for precise manipulation. These findings suggest that combining auxiliary objectives with multi-modal sensing offers a promising direction for VLA models in mobile manipulation, contributing to the development of more capable domestic robots.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
AuxVLA 通过辅助任务和多模态输入增强 VLA 模型，用于移动操作。

### 2. 核心内容
当前 VLA 模型在家庭场景中的复杂移动操作任务上表现不佳，尤其面对高维动作空间（手臂和移动底盘的 13 维）。本文提出 AuxVLA，通过辅助任务协同训练和增强输入模态（多视角视觉与深度信息）提升 VLA 模型控制移动操作机器人的能力。实验证明该方法能有效改善直接模仿学习的次优结果，为移动操作中的 VLA 应用提供了可行方案。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=lcuA4RYit9](https://openreview.net/forum?id=lcuA4RYit9)
