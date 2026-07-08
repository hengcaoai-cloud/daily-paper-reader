---
title: "$\\textit{HiMaCon:}$ Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data"
title_zh: HiMaCon：从未标注多模态数据中发现层次化操作概念
authors: "Ruizhe Liu, Pei Zhou, Qian Luo, Li Sun, Jun CEN, Yibing Song, Yanchao Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=2aIoEG2Hwz"
tags: ["query:analysis"]
score: 7.0
evidence: 从跨模态数据自监督学习层次化操作概念，得到更优表示
tldr: 为实现机器人操作的泛化，提出HiMaCon框架，无需人工标注，通过跨模态相关网络提取跨感官不变模式，并结合多时间尺度预测器组织层次化表示，学到的操作概念使策略能够聚焦于可迁移的关系模式，在多任务设置中表现出更好的泛化能力。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 有效泛化需要捕捉跨环境和任务的交互不变模式，但标注成本高。
method: 结合跨模态相关网络和多步预测器，自监督学习层次化操作概念表示。
result: 学到的表示使策略在多个操作任务上展现出更强的泛化性能。
conclusion: 层次化跨模态表示学习是提升操作策略泛化性的有效途径。
---

## Abstract
Effective generalization in robotic manipulation requires representations that capture invariant patterns of interaction across environments and tasks.
We present a self-supervised framework for learning hierarchical manipulation concepts that encode these invariant patterns through cross-modal sensory correlations and multi-level temporal abstractions without requiring human annotation.
Our approach combines a cross-modal correlation network that identifies persistent patterns across sensory modalities with a multi-horizon predictor that organizes representations hierarchically across temporal scales. Manipulation concepts learned through this dual structure enable policies to focus on transferable relational patterns while maintaining awareness of both immediate actions and longer-term goals.
Empirical evaluation across simulated benchmarks and real-world deployments demonstrates significant performance improvements with our concept-enhanced policies. 
Analysis reveals that the learned concepts resemble human-interpretable manipulation primitives despite receiving no semantic supervision. This work advances both the understanding of representation learning for manipulation and provides a practical approach to enhancing robotic performance in complex scenarios.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
从跨模态数据自监督学习层次化操作概念，得到更优表示。

### 2. 核心内容
为实现机器人操作的泛化，提出HiMaCon框架，无需人工标注，通过跨模态相关网络提取跨感官不变模式，并结合多时间尺度预测器组织层次化表示，学到的操作概念使策略能够聚焦于可迁移的关系模式，在多任务设置中表现出更好的泛化能力。

### 3. 对应检索需求
Papers central to representation learning and model interpretability, especially work that connects or combines: learning better representations for robot actions; latent representations of robot actions; hidden state representations and their mismatch with action control; representation misalignment between model internals and action outputs; interpretability methods for vision-language-action architectures; generating robot actions from learned representations; What representations are most effective for VLA and WAM models to generate robot actions?; How to learn better latent representations for robot manipulation policies?; Methods for diagnosing and attributing causes in VLA and WAM models; Challenges in aligning hidden state representations with action control in robot learning.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=2aIoEG2Hwz](https://openreview.net/forum?id=2aIoEG2Hwz)
