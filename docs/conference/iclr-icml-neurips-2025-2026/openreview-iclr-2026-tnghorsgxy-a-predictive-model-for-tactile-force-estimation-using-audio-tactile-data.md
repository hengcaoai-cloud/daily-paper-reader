---
title: A Predictive Model for Tactile Force Estimation using Audio-Tactile Data
title_zh: 基于音频-触觉数据的触觉力预测模型
authors: Jiangyu Hu
date: 2025-09-15
pdf: "https://openreview.net/pdf?id=TnGhoRSgXy"
tags: ["query:robot"]
score: 9.0
evidence: 使用音频-触觉数据和回声状态网络估计手中操作时的触觉力
tldr: 针对手中操作含可移动内容物体时视觉遮挡导致的动力学估计难题，提出利用回声状态网络从音频-触觉数据预测手部扭矩，以足够提前量实现自适应控制，在真实机器人手上验证了对液体等物体的稳定操纵。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 物体内部运动不能视觉观测时，实时估计物体动力学以适应手中操作具有挑战。
method: 构建回声状态网络学习框架，从音频-触觉数据提前预测机械手承受的扭矩。
result: 预测模型为实时自适应控制提供足够的提前量，实现稳定物体操纵。
conclusion: 音频-触觉融合的预测模型弥补了视觉信息缺失，提升了手中操作鲁棒性。
---

## Abstract
Robust in-hand manipulation of objects with movable content requires estimation
 and prediction of the contents’ motion with enough anticipation to allow time to
 compensate for resulting internal torques. The quick estimation of the objects’
 dynamics can be challenging when the objects’ motion properties (e.g., type,
 amount, dynamics) cannot be observed visually due to robot occlusions or opacity
 of the container. This can be further complicated by the computational requirements
 of onboard hardware available for real-time processing and control for robotics. In
 this work, we develop a simple learning framework that uses echo state networks
 to predict the torques experienced on the robotic hand with enough anticipation
 to allow for adaptive controls and sufficient efficiency for real-time prediction
 without GPU processing. We demonstrate the efficacy of this formulation for
 tactile force prediction on the Allegro robotic hand with a Tekscan tactile skin
 using both material-specific and material-agnostic learned models. We show that
 while both are effective, the material-specific models show an improvement in
 accuracy due to the difference in inertial properties between the different materials.
 Wealso develop a prediction model that uses audio feedback to augment the tactile
 predictions. We show that adding auditory feedback improves the prediction error,
 though it significantly increases the computation cost of the model. We validate
 this formulation for online prediction on the robotic hand moving materials in
 real-time and adapting grip for slip detection.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
使用音频-触觉数据和回声状态网络估计手中操作时的触觉力。

### 2. 核心内容
针对手中操作含可移动内容物体时视觉遮挡导致的动力学估计难题，提出利用回声状态网络从音频-触觉数据预测手部扭矩，以足够提前量实现自适应控制，在真实机器人手上验证了对液体等物体的稳定操纵。

### 3. 对应检索需求
tactile sensors and tactile-based manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=TnGhoRSgXy](https://openreview.net/forum?id=TnGhoRSgXy)
