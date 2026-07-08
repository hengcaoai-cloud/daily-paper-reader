---
title: "MIMIC: Mask-Injected Manipulation Video Generation with Interaction Control"
title_zh: MIMIC：带交互控制的掩码注入操作视频生成
authors: "Tianxiao Chen, Jintao Rong, Huajin Chen, Jingya Wang, Tao Zhou, Jiming Chen, Qi Ye"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=COrUdVuInH"
tags: ["query:data"]
score: 6.0
evidence: 两阶段图像到视频扩散框架，用于生成操作视频以扩展交互数据
tldr: 针对具身智能中大规模交互数据匮乏的瓶颈，MIMIC提出一种两阶段图像到视频扩散框架，通过交互运动感知模块融合视觉特征，以参考视频驱动操作视频生成。该方法能够捕获精细的接触丰富动态，为扩展机器人训练数据提供了可控的视频生成手段。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 具身智能缺乏大规模交互数据，操作视频生成可提供替代，但生成质量不足。
method: 设计两阶段扩散模型，利用参考视频和交互运动感知模块生成高质量操作视频。
result: 生成的视频能够捕获细微接触动态，优于现有视频生成方法。
conclusion: MIMIC为操作类视频生成提供了有效框架，可作为机器人数据增强的工具。
---

## Abstract
Embodied intelligence faces a fundamental bottleneck from limited large-scale interaction data. Video generation offers a scalable alternative, but manipulation videos remain particularly challenging, as they require capturing subtle, contact-rich dynamics. Despite recent advances, video diffusion models still struggle to balance semantic understanding with fine-grained visual details, restricting their effectiveness in manipulation scenarios. Our key insight is that reference videos provide rich semantic and motion cues that can effectively drive manipulation video generation. Building on this, we propose MIMIC, a two-stage image-to-video diffusion framework. (1) We first introduce an Interaction-Motion-Aware (IMA) module to fuse visual features from the reference video, producing coherent semantic masks that correspond to the target image. (2) then utilize these masks as semantic control signals to guide the video generation process. Moreover, considering the ambiguity of the motion attribution,  we introduce a Pair Prompt Control mechanism to disentangle object and camera motion by adding the reference video as an additional input. Extensive experiments demonstrate that MIMIC significantly outperforms existing methods, effectively preserves manipulation intent and motion details, even when handling diverse and deformable objects. Our findings underscore the effectiveness of reference-driven semantics for controllable and realistic manipulation video generation.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
两阶段图像到视频扩散框架，用于生成操作视频以扩展交互数据。

### 2. 核心内容
针对具身智能中大规模交互数据匮乏的瓶颈，MIMIC提出一种两阶段图像到视频扩散框架，通过交互运动感知模块融合视觉特征，以参考视频驱动操作视频生成。该方法能够捕获精细的接触丰富动态，为扩展机器人训练数据提供了可控的视频生成手段。

### 3. 对应检索需求
Papers central to scale data for robot learning, especially work that connects or combines: r; robot manipulation data engine; scalable manipulation dataset; web-scale robot learning data; robot learning from human videos; transferring human skills to robots; methods for converting human video demonstrations into robot executable action data; reconstructing hand object interactions from human videos for robot manipulation learning; aligning human body motion with different robot morphologies for robot learning from human demonstrations; scaling laws for robot learning from large scale internet video data.

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=COrUdVuInH](https://openreview.net/forum?id=COrUdVuInH)
