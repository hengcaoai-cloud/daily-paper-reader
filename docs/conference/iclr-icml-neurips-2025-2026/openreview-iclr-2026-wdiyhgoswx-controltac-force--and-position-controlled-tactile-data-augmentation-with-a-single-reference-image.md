---
title: "ControlTac: Force- and Position-Controlled Tactile Data Augmentation with a Single Reference Image"
title_zh: ControlTac：基于单张参考图像的力与位置可控触觉数据增强
authors: "Dongyu Luo, Kelin Yu, Amir Hossein Shahidzadeh, Cornelia Fermuller, Yiannis Aloimonos, Ruohan Gao"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=wdiyHGoswX"
tags: ["query:robot"]
score: 8.0
evidence: 基于接触力和位置控制的可控触觉数据增强框架
tldr: 针对视觉触觉感知中大规模数据采集成本高的问题，ControlTac提出一种两阶段可控生成框架，以单张参考触觉图像为基础，引入接触力和位置物理先验生成逼真的触觉图像。该方法能有效增强触觉数据集，提升下游动态操作任务的性能。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 大规模触觉数据采集因传感器差异和交互多样性而成本高昂。
method: 利用条件生成模型，以接触力和位置为先验，从单张参考图像生成多样触觉图像。
result: 生成的触觉图像逼真且能提升真实操作任务中的策略性能。
conclusion: ControlTac为触觉感知提供了高效的数据增强方案，有助于触觉基操作的发展。
---

## Abstract
Vision-based tactile sensing is widely used in perception, reconstruction, and robotic manipulation, yet collecting large-scale tactile data remains costly due to diverse sensor-object interactions and inconsistencies across sensor instances. Existing approaches to scaling tactile data—simulation and free-form tactile generation—often yield unrealistically rendered signals with poor transfer to highly dynamic real-world tasks. We propose **ControlTac**, a two-stage controllable framework that generates realistic tactile images conditioned on a single reference tactile image, contact force, and contact position. By grounding generation in these important physical priors, **ControlTac** produces realistic samples that effectively capture task-relevant variations. Across three downstream tasks and three real-world experiments, the augmented datasets using our approach consistently improve performance and demonstrate practical utility in dynamic real-world settings. Project page: https://controltac.github.io/

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于接触力和位置控制的可控触觉数据增强框架。

### 2. 核心内容
针对视觉触觉感知中大规模数据采集成本高的问题，ControlTac提出一种两阶段可控生成框架，以单张参考触觉图像为基础，引入接触力和位置物理先验生成逼真的触觉图像。该方法能有效增强触觉数据集，提升下游动态操作任务的性能。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=wdiyHGoswX](https://openreview.net/forum?id=wdiyHGoswX)
