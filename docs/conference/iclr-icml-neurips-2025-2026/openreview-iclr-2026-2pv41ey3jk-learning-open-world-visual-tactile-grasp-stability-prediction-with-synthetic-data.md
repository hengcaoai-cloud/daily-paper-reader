---
title: Learning Open-World Visual-Tactile Grasp Stability Prediction with Synthetic Data
title_zh: 用合成数据学习开放世界视觉-触觉抓取稳定性预测
authors: "Beining Han, Gan Luyang, Derek Geng, Abhishek Joshi, Jia Deng"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=2Pv41Ey3jK"
tags: ["query:robot"]
score: 8.0
evidence: 使用合成数据学习视觉-触觉抓取稳定性预测，实现开放世界泛化。
tldr: 该工作针对开放世界中视觉-触觉抓取稳定性预测问题，利用基于有限元仿真和光线追踪渲染生成高逼真合成数据，训练预测器以在新物体和新环境中实现零样本泛化。实验表明，相比刚体仿真，该仿真管线具有更高物理保真度，且基于合成数据训练的预测器在未知场景中表现优越，为视觉-触觉抓取预测提供了可扩展的解决方案。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有视觉-触觉抓取预测器依赖有限真实数据，且评估局限于简单环境，缺乏零样本泛化能力。
method: 采用基于有限元和光线追踪的仿真生成视觉-触觉合成数据，训练抓取稳定性预测器。
result: 合成数据训练的预测器能够在新物体和新环境中实现零样本泛化，且仿真保真度高于刚体方法。
conclusion: 该工作证明了高保真合成数据在视觉-触觉抓取预测中的有效性，为开放世界应用提供了可行路径。
---

## Abstract
Grasp stability prediction with visual-tactile data is an important problem in robotics. Most prior work learns these predictors with limited real-world data. Moreover, their evaluation has also been restricted to a simple and unitary laboratory environment. Our work studies open-world visual-tactile grasp stability prediction, i.e. the predictor should zero-shot generalize to novel objects in novel environment. Towards this problem, we propose to learn with synthetic visual-tactile data, generated with FEM-based simulation and ray-tracing rendering. In our experiment, we show that our simulation pipeline has much higher physical fidelity, compared to the rigid-body simulation. Furthermore, the predictor trained on our synthetic dataset has higher accuracy on open-world grasp stability prediction tasks than models trained on real-world dataset or on synthetic dataset from rigid-body simulation.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
使用合成数据学习视觉-触觉抓取稳定性预测，实现开放世界泛化。

### 2. 核心内容
该工作针对开放世界中视觉-触觉抓取稳定性预测问题，利用基于有限元仿真和光线追踪渲染生成高逼真合成数据，训练预测器以在新物体和新环境中实现零样本泛化。实验表明，相比刚体仿真，该仿真管线具有更高物理保真度，且基于合成数据训练的预测器在未知场景中表现优越，为视觉-触觉抓取预测提供了可扩展的解决方案。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=2Pv41Ey3jK](https://openreview.net/forum?id=2Pv41Ey3jK)
