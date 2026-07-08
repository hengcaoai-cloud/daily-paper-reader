---
title: "AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception"
title_zh: AnyTouch 2：面向动态触觉感知的通用光学触觉表示学习
authors: "Ruoxuan Feng, Yuxuan Zhou, Siyu Mei, Dongzhan Zhou, Pengwei Wang, Shaowei Cui, Bin Fang, Guocai Yao, Di Hu"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=ndilONnABZ"
tags: ["query:robot"]
score: 8.0
evidence: 面向操作中动态触觉感知的大规模触觉数据集与表示学习
tldr: 现有触觉数据集与模型多关注物体级属性，忽视时间动态信息。AnyTouch 2 提出了 ToucHD，一个包含丰富动态信息的大规模触觉数据集，并设计了动态触觉表示学习框架。实验表明该方法能有效捕捉细微表面形变与力动态，为接触丰富的机器人操作提供了关键的动态触觉感知基础。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 真实世界接触式操作需要感知时间触觉反馈，但现有触觉数据缺乏动态信息。
method: 提出大规模触觉数据集 ToucHD 和层次化动态触觉表示学习框架。
result: 方法能有效捕捉动态触觉模式，在物体属性与力动态推理上表现优越。
conclusion: 为接触丰富操作奠定了动态触觉感知基础，弥补了现有数据的动态信息缺失。
---

## Abstract
Real-world contact-rich manipulation demands robots to perceive temporal tactile feedback, capture subtle surface deformations, and reason about object properties and force dynamics.
Although optical tactile sensors are uniquely capable of providing such rich information, existing tactile datasets and models remain limited. These resources primarily focus on object-level attributes (e.g., material) while largely overlooking fine-grained temporal dynamics.
We consider that advancing dynamic tactile perception requires a systematic hierarchy of dynamic perception capabilities to guide both data collection and model design.
To address the lack of tactile data with rich dynamic information, we present ToucHD, a large-scale tactile dataset spanning tactile atomic actions, real-world manipulations, and touch-force paired data.
Beyond scale, ToucHD establishes a comprehensive dynamic data ecosystem that explicitly supports hierarchical perception capabilities from the data perspective.
Building on it, we propose AnyTouch 2, a general tactile representation learning framework for diverse optical tactile sensors that unifies object-level understanding with fine-grained, force-aware dynamic perception. The framework captures both pixel-level and action-specific deformations across frames, while explicitly modeling physical force dynamics, thereby learning multi-level dynamic perception capabilities from the model perspective.
We evaluate our model on benchmarks that covers static object properties and dynamic physical attributes, as well as real-world manipulation tasks spanning multiple tiers of dynamic perception capabilities—from basic object-level understanding to force-aware dexterous manipulation. Experimental results demonstrate consistent and strong performance across sensors and tasks, highlighting the framework’s effectiveness as a general dynamic tactile perception model. The code, dataset and model are available at gewu-lab.github.io/AnyTouch2/.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向操作中动态触觉感知的大规模触觉数据集与表示学习。

### 2. 核心内容
现有触觉数据集与模型多关注物体级属性，忽视时间动态信息。AnyTouch 2 提出了 ToucHD，一个包含丰富动态信息的大规模触觉数据集，并设计了动态触觉表示学习框架。实验表明该方法能有效捕捉细微表面形变与力动态，为接触丰富的机器人操作提供了关键的动态触觉感知基础。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=ndilONnABZ](https://openreview.net/forum?id=ndilONnABZ)
