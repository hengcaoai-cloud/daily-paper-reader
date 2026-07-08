---
title: "TaCo:  A Benchmark for Lossless and Lossy Codecs of Heterogeneous Tactile Data"
title_zh: TaCo：异构触觉数据的无损与有损编解码器基准
authors: "Zhengxue Cheng, Yan Zhao, Keyu Wang, Hengdi ZHANG, Li Song"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=1PYXFkS6Hy"
tags: ["query:robot"]
score: 4.0
evidence: 触觉数据压缩基准，对实时触觉操纵至关重要
tldr: TaCo是首个触觉数据压缩基准，针对实时机器人应用中触觉数据的带宽限制，系统评估了30种压缩方法在五个不同触觉数据集上的性能，覆盖无损和有损压缩方案。该基准填补了触觉感知高效压缩的空白，为基于触觉的灵巧操作提供了关键的数据处理基础。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 触觉感知对具身智能至关重要，但触觉数据的异构性和时空复杂性使得高效压缩成为实时机器人应用尚未探索的挑战。
method: 提出首个全面的触觉数据编解码器基准TaCo，在五个数据集上评估30种压缩方法。
result: 系统比较了无损和有损压缩方案在四个关键任务上的表现，揭示了不同方法在触觉数据上的有效性。
conclusion: 为触觉数据的高效编解码提供了标准化的评估框架，推动触觉感知在实时机器人中的应用。
---

## Abstract
Tactile sensing is crucial for embodied intelligence, providing fine-grained perception and control in complex environments. However, efficient tactile data compression, which is essential for real-time robotic applications under strict bandwidth constraints, remains underexplored. The inherent heterogeneity and spatiotemporal complexity of tactile data further complicate this challenge. To bridge this gap, we introduce TaCo, the first comprehensive benchmark for Tactile data Codecs. TaCo evaluates 30 compression methods, including off-the-shelf compression algorithms and neural codecs, across five diverse datasets from various sensor types. We systematically assess both lossless and lossy compression schemes on four key tasks: lossless storage, human visualization, material and object classification, and dexterous robotic grasping. Notably, we pioneer the development of data-driven codecs explicitly trained on tactile data, TaCo-LL (lossless) and TaCo-L (lossy). Results have validated the superior performance of our TaCo-LL and TaCo-L. This benchmark provides a foundational framework for understanding the critical trade-offs between compression efficiency and task performance, paving the way for future advances in tactile perception.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
触觉数据压缩基准，对实时触觉操纵至关重要。

### 2. 核心内容
TaCo是首个触觉数据压缩基准，针对实时机器人应用中触觉数据的带宽限制，系统评估了30种压缩方法在五个不同触觉数据集上的性能，覆盖无损和有损压缩方案。该基准填补了触觉感知高效压缩的空白，为基于触觉的灵巧操作提供了关键的数据处理基础。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=1PYXFkS6Hy](https://openreview.net/forum?id=1PYXFkS6Hy)
