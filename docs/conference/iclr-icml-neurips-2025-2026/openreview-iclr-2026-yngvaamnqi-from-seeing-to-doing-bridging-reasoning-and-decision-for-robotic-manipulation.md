---
title: "From Seeing to Doing: Bridging Reasoning and Decision for Robotic Manipulation"
title_zh: 从看到做：桥接推理与决策的机器人操作
authors: "Yifu Yuan, Haiqin Cui, Yibin Chen, Zibin Dong, Fei Ni, Longxin Kou, Jinyi Liu, Pengyi Li, YAN ZHENG, Jianye HAO"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=yngvAamNQi"
tags: ["query:model"]
score: 8.0
evidence: 生成空间关系推理中间表征的视觉语言模型，用于引导机器人操作
tldr: 为解决视觉-语言-行动模型在零样本泛化上的不足，FSD提出一种通过空间关系推理生成中间表征的方法，为操作任务提供精细指导。该方法结合层次化数据构建和自一致性机制对齐空间坐标，在未见场景和任务中展现出更强的泛化性，推动了VLA模型的推理能力。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有VLA模型因具身数据稀缺和异构，零样本泛化性能不足。
method: 设计VLM生成空间推理中间表征，搭配层次化数据与自一致性机制指导操作。
result: 在新任务和场景上取得了稳健的零样本操作性能。
conclusion: FSD通过空间推理增强VLA模型的决策能力，为通用操作模型提供了新思路。
---

## Abstract
Achieving generalization in robotic manipulation remains a critical challenge, particularly for unseen scenarios and novel tasks. Current Vision-Language-Action (VLA) models, while building on top of general Vision-Language Models (VLMs), still fall short of achieving robust zero-shot performance due to the scarcity and heterogeneity prevalent in embodied datasets. To address these limitations, we propose FSD (From Seeing to Doing), a novel vision-language model that generates intermediate representations through spatial relationship reasoning, providing fine-grained guidance for robotic manipulation. Our approach combines a hierarchical data construction pipeline for training with a self-consistency mechanism that aligns spatial coordinates with visual signals. Through extensive experiments, we comprehensively validated FSD’s capabilities in both “seeing” and “doing”, achieving outstanding performance across 8 benchmarks for general spatial reasoning and embodied reference abilities, as well as on our proposed more challenging benchmark VABench. We also verified zero-shot capabilities in robot manipulation, demonstrating significant performance improvements over baseline methods in both SimplerEnv and real robot settings. Experimental results show that FSD achieves 40.6% success rate in SimplerEnv and 72% success rate across 8 real-world tasks, outperforming the strongest baseline by 30%.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
生成空间关系推理中间表征的视觉语言模型，用于引导机器人操作。

### 2. 核心内容
为解决视觉-语言-行动模型在零样本泛化上的不足，FSD提出一种通过空间关系推理生成中间表征的方法，为操作任务提供精细指导。该方法结合层次化数据构建和自一致性机制对齐空间坐标，在未见场景和任务中展现出更强的泛化性，推动了VLA模型的推理能力。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=yngvAamNQi](https://openreview.net/forum?id=yngvAamNQi)
