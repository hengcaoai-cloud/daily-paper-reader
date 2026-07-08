---
title: "UniHM: Unified Dexterous Hand Manipulation with Vision Language Model"
title_zh: "UniHM: 用视觉语言模型实现统一的灵巧手操作"
authors: "Zhenhao Zhang, Jiaxin Liu, Ye Shi, Jingya Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=cVX3VqO8BO"
tags: ["query:robot"]
score: 9.0
evidence: 基于视觉语言动作模型的统一灵巧手操作，使用人类-物体交互数据训练
tldr: 提出UniHM，首个由自由形式语言指令引导的统一灵巧手操作框架，设计统一手部灵巧分词器，在人类-物体交互数据上训练视觉语言动作模型，无需大量遥操作数据，实现跨手部泛化。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有灵巧操作规划缺乏开放词汇指导，依赖对象中心提示。
method: 设计统一手部灵巧分词器，在人类交互数据上训练视觉语言动作模型。
result: 实现语言引导的灵巧操作，并能泛化到新灵巧手形态。
conclusion: 灵巧操作可通过视觉语言模型和人类演示数据高效学习。
---

## Abstract
Planning physically feasible dexterous hand manipulation is a central challenge in robotic manipulation and Embodied AI. Prior work typically relies on object-centric cues or precise hand-object interaction sequences, foregoing the rich, compositional guidance of open-vocabulary instruction. We introduce UniHM, the first framework for unified dexterous hand manipulation guided by free-form language commands. 
We propose a Unified Hand-Dexterous Tokenizer that maps heterogeneous dexterous-hand morphologies into a single shared codebook, improving cross-dexterous hand generalization and scalability to new morphologies. Our vision language action model is trained solely on human-object interaction data, eliminating the need for massive real-world teleoperation datasets, and demonstrates strong generalizability in producing human-like manipulation sequences from open-ended language instructions. To ensure physical realism, we introduce a physics-guided dynamic refinement module that performs segment-wise joint optimization under generative and temporal priors, yielding smooth and physically feasible manipulation sequences. Across multiple datasets and real-world evaluations, UniHM attains state-of-the-art results on both seen and unseen objects and trajectories, demonstrating strong generalization and high physical feasibility.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于视觉语言动作模型的统一灵巧手操作，使用人类-物体交互数据训练。

### 2. 核心内容
提出UniHM，首个由自由形式语言指令引导的统一灵巧手操作框架，设计统一手部灵巧分词器，在人类-物体交互数据上训练视觉语言动作模型，无需大量遥操作数据，实现跨手部泛化。

### 3. 对应检索需求
embodied foundation models for multi fingered dexterous manipulation tasks。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=cVX3VqO8BO](https://openreview.net/forum?id=cVX3VqO8BO)
