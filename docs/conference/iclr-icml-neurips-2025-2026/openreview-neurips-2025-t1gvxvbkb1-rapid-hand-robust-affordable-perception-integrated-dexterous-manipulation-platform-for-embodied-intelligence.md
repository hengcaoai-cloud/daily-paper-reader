---
title: "RAPID Hand: Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Embodied Intelligence"
title_zh: RAPID Hand：面向具身智能的鲁棒、低成本、感知集成灵巧操作平台
authors: "Zhaoliang Wan, Zetong Bi, Zida Zhou, Hao Ren, Yiming Zeng, Yihan Li, Lu Qi, Xu Yang, Ming-Hsuan Yang, Hui Cheng"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=T1gVXvbkB1"
tags: ["query:robot"]
score: 10.0
evidence: 集成触觉感知的20自由度灵巧手平台，用于灵巧操作数据收集
tldr: RAPID Hand针对低成本高灵巧度数据采集平台的缺失，提出了一款软硬件协同优化的灵巧手平台。该平台拥有紧凑的20自由度手部结构，集成了腕部视觉、指尖触觉传感和本体感知，并设计了高自由度遥操作界面，显著降低了多指手操作数据的收集门槛，为通用机器人自主性提供了重要的硬件基础。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 真实世界多指手机器人操作数据极度匮乏，缺乏低成本且高灵巧度的收集平台。
method: 设计软硬件协同优化的RAPID Hand平台，融合紧凑手型、感知和遥操作接口。
result: 实现了稳定的感知融合和低延迟数据流，遥操作界面支持高质量演示数据收集。
conclusion: 该平台为灵巧操作的大规模真实世界数据采集提供了可访问的解决方案。
---

## Abstract
This paper addresses the scarcity of low-cost but high-dexterity platforms for collecting real-world multi-fingered robot manipulation data towards generalist robot autonomy. 
To achieve it, we propose the RAPID Hand, a co-optimized hardware and software platform where the compact 20-DoF hand, robust whole-hand perception, and high-DoF teleoperation interface are jointly designed.
Specifically, RAPID Hand adopts a compact and practical hand ontology and a hardware-level perception framework that stably integrates wrist-mounted vision, fingertip tactile sensing, and proprioception with sub-7 ms latency and spatial alignment. 
Collecting high-quality demonstrations on high-DoF hands is challenging, as existing teleoperation methods struggle with precision and stability on complex multi-fingered systems.
We address this by co-optimizing hand design, perception integration, and teleoperation interface through a universal actuation scheme, custom perception electronics, and two retargeting constraints. We evaluate the platform’s hardware, perception, and teleoperation interface. Training a diffusion policy on collected data shows superior performance over prior works, validating the system’s capability for reliable, high-quality data collection.
The platform is constructed from low-cost and off-the-shelf components and will be made public to ensure reproducibility and ease of adoption.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
集成触觉感知的20自由度灵巧手平台，用于灵巧操作数据收集。

### 2. 核心内容
RAPID Hand针对低成本高灵巧度数据采集平台的缺失，提出了一款软硬件协同优化的灵巧手平台。该平台拥有紧凑的20自由度手部结构，集成了腕部视觉、指尖触觉传感和本体感知，并设计了高自由度遥操作界面，显著降低了多指手操作数据的收集门槛，为通用机器人自主性提供了重要的硬件基础。

### 3. 对应检索需求
robot dexterous manipulation with multi-fingered hands。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=T1gVXvbkB1](https://openreview.net/forum?id=T1gVXvbkB1)
