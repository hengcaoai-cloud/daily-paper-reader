---
title: Grounding Bodily Awareness in Visual Representations for Efficient Policy Learning
title_zh: 在视觉表征中扎根身体意识以实现高效策略学习
authors: "Junlin Wang, Zhiyun Lin"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ZaB2fV3TYo"
tags: ["query:analysis"]
score: 7.0
evidence: 通过令牌间对比学习以智体为中心的视觉表征，提高策略学习效率
tldr: 针对机器人操作中视觉表征忽略身体动态的问题，提出ICon方法，通过对比学习分离智体与环境令牌，获得嵌入身体先验的视觉表征，显著提升下游策略学习效率。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有视觉表征未充分考虑机器人身体动态，影响策略学习效率。
method: 在ViT的令牌级特征上应用对比学习，分离智体与环境令牌。
result: 在多种操作任务上，策略样本效率大幅提升。
conclusion: 身体中心视觉表征有效引导策略学习，提升数据效率。
---

## Abstract
Learning effective visual representations for robotic manipulation remains a fundamental challenge due to the complex body dynamics involved in action execution. In this paper, we study how visual representations that carry body-relevant cues can enable efficient policy learning for downstream robotic manipulation tasks. We present $\textbf{I}$nter-token $\textbf{Con}$trast ($\textbf{ICon}$), a contrastive learning method applied to the token-level representations of Vision Transformers (ViTs). ICon enforces a separation in the feature space between agent-specific and environment-specific tokens, resulting in agent-centric visual representations that embed body-specific inductive biases. This framework can be seamlessly integrated into end-to-end policy learning by incorporating the contrastive loss as an auxiliary objective. Our experiments show that ICon not only improves policy performance across various manipulation tasks but also facilitates policy transfer across different robots. The project website: https://anonymous.4open.science/w/ICon/

---

## 论文详细总结（自动生成）

### 1. 检索相关性
通过令牌间对比学习以智体为中心的视觉表征，提高策略学习效率。

### 2. 核心内容
针对机器人操作中视觉表征忽略身体动态的问题，提出ICon方法，通过对比学习分离智体与环境令牌，获得嵌入身体先验的视觉表征，显著提升下游策略学习效率。

### 3. 对应检索需求
Papers central to representation learning and model interpretability, especially work that connects or combines: learning better representations for robot actions; latent representations of robot actions; hidden state representations and their mismatch with action control; representation misalignment between model internals and action outputs; interpretability methods for vision-language-action architectures; generating robot actions from learned representations; What representations are most effective for VLA and WAM models to generate robot actions?; How to learn better latent representations for robot manipulation policies?; Methods for diagnosing and attributing causes in VLA and WAM models; Challenges in aligning hidden state representations with action control in robot learning.

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=ZaB2fV3TYo](https://openreview.net/forum?id=ZaB2fV3TYo)
