---
title: "MimicTouch:Tactile Affordance for Robot Synesthesia for Dexterous Manipulation"
title_zh: MimicTouch：面向灵巧操作的机器人联觉触觉可供性
authors: Jiangyu Hu
date: 2025-09-02
pdf: "https://openreview.net/pdf?id=RlMCc0JTu4"
tags: ["query:robot"]
score: 10.0
evidence: 通过点云表示的统一视触觉可供性框架，用于灵巧操作
tldr: MimicTouch针对灵巧操作中视觉与触觉模态融合的挑战，提出了机器人联觉框架TARS，通过统一点云表示结合视觉和触觉信息，学习物体的视触觉可供性。该框架在非接触场景下也能有效预测可供性，超越了仅依赖视觉的方法，为多指手操作的感知与决策提供了更全面的模态融合方案。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 灵巧操作中融合视觉与触觉模态具有挑战性，现有方法在非接触场景下依赖视觉有限。
method: 提出TARS框架，基于统一点云表示的机器人联觉，利用视触觉可供性进行灵巧操作。
result: 在非接触场景中实现了有效的触觉可供性预测，增强了操作策略的感官信息。
conclusion: 该框架为多模态感知集成的灵巧操作提供了新方法，促进了机器人联觉的应用。
---

## Abstract
In the field of dexterous robotic manipulation, integrating visual and tactile modalities to inform manipulation policies presents significant challenges, especially
in noncontact scenarios where reliance on tactile perception can be inadequate.
Visual affordance techniques currently offer effective manipulation-centric semantic priors focused on objects. However, most existing research is limited to
using camera sensors and prior object information for affordance prediction. In
this study, we introduce a unified framework called Tactile Affordance in Robot
Synesthesia (TARS) for dexterous manipulation that employs robotic synesthesia
through a unified point cloud representation. This framework harnesses the visuotactile affordance of objects, effectively merging comprehensive visual perception
from external cameras with tactile feedback from local optical tactile sensors to
handle tasks involving both contact and non-contact states. We simulated tactile
perception in a virtual environment and trained task-oriented manipulation policies.
Subsequently, we tested our approach on four distinct manipulation tasks, conducting extensive experiments to evaluate how different modules within our method
optimize the performance of these manipulation policies.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
通过点云表示的统一视触觉可供性框架，用于灵巧操作。

### 2. 核心内容
MimicTouch针对灵巧操作中视觉与触觉模态融合的挑战，提出了机器人联觉框架TARS，通过统一点云表示结合视觉和触觉信息，学习物体的视触觉可供性。该框架在非接触场景下也能有效预测可供性，超越了仅依赖视觉的方法，为多指手操作的感知与决策提供了更全面的模态融合方案。

### 3. 对应检索需求
approaches for visual tactile cross modal representation learning in dexterous manipulation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=RlMCc0JTu4](https://openreview.net/forum?id=RlMCc0JTu4)
