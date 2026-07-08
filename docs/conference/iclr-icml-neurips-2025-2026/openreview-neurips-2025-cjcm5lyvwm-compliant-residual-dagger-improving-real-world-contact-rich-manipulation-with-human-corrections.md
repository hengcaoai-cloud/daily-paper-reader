---
title: "Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections"
title_zh: 柔顺残差DAgger：利用人为修正提升真实世界接触丰富操作
authors: "Xiaomeng Xu, Yifan Hou, Zeyi Liu, Shuran Song"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=cjcm5LYVWm"
tags: ["query:robot"]
score: 7.0
evidence: 通过柔顺干预收集人类修正数据，学习残差策略用于接触丰富操作
tldr: 针对真实世界接触丰富操作中数据收集与策略更新难题，CR-DAgger提出柔顺干预接口，允许人类在不中断策略执行的情况下提供微小动作修正，并学习包含力反馈的残差策略。实验表明该方法显著提升了精细操作任务的性能，为人类参与式学习提供了高效机制。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 真实接触丰富操作中，如何高效收集人类修正数据并更新策略是关键挑战。
method: 设计柔顺干预接口收集人类增量修正，学习融合力控制的残差策略。
result: 在精细接触操作任务中显著提升了成功率和策略性能。
conclusion: CR-DAgger为人类指导接触丰富操作提供了一种可行且高效的框架。
---

## Abstract
We address key challenges in Dataset Aggregation (DAgger) for real-world contact-
rich manipulation: how to collect informative human correction data and how to
effectively update policies with this new data. We introduce Compliant Residual
DAgger (CR-DAgger), which contains two novel components: 1) a Compliant
Intervention Interface that leverages compliance control, allowing humans to pro-
vide gentle, accurate delta action corrections without interrupting the ongoing
robot policy execution; and 2) a Compliant Residual Policy formulation that learns
from human corrections while incorporating force feedback and force control.
Our system significantly enhances performance on precise contact-rich manipu-
lation tasks using minimal correction data, improving base policy success rates
by over 60% on two challenging tasks (book flipping and belt assembly) while
outperforming both retraining-from-scratch and finetuning approaches. Through
extensive real-world experiments, we provide practical guidance for implementing
effective DAgger in real-world robot learning tasks.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
通过柔顺干预收集人类修正数据，学习残差策略用于接触丰富操作。

### 2. 核心内容
针对真实世界接触丰富操作中数据收集与策略更新难题，CR-DAgger提出柔顺干预接口，允许人类在不中断策略执行的情况下提供微小动作修正，并学习包含力反馈的残差策略。实验表明该方法显著提升了精细操作任务的性能，为人类参与式学习提供了高效机制。

### 3. 对应检索需求
robot learning from human demonstrations for dexterous tasks。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=cjcm5LYVWm](https://openreview.net/forum?id=cjcm5LYVWm)
