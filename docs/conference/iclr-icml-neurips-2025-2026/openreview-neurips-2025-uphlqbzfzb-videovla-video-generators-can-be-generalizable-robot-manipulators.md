---
title: "VideoVLA: Video Generators Can Be Generalizable Robot Manipulators"
title_zh: "VideoVLA: 视频生成器可成为通用机器人操作器"
authors: "Yichao Shen, Fangyun Wei, Zhiying Du, Yaobo Liang, Yan Lu, Jiaolong Yang, Nanning Zheng, Baining Guo"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=UPHlqbZFZB"
tags: ["query:model"]
score: 10.0
evidence: 基于视频生成扩散变换器的VLA模型，同时预测动作序列和未来图像
tldr: VideoVLA 将大规模视频生成模型转化为机器人VLA操作器，通过联合建模视频、语言和动作模态，充分利用视频先验知识，在新任务和物体上实现了更好的泛化能力。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有VLA模型依赖预训练理解模型，但在新任务和物体上的泛化能力仍有限。
method: 以多模态扩散变换器为基础，联合建模视频、语言和动作，将视频生成能力迁移到机器人控制。
result: 在模仿学习基准上显著提升了泛化性能，能处理多样化的操作任务。
conclusion: 视频生成模型作为VLA的基础可以有效注入运动先验，是实现通用操作的有前景路径。
---

## Abstract
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes.  Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy—forecasting both actions and their visual consequences—explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于视频生成扩散变换器的VLA模型，同时预测动作序列和未来图像。

### 2. 核心内容
VideoVLA 将大规模视频生成模型转化为机器人VLA操作器，通过联合建模视频、语言和动作模态，充分利用视频先验知识，在新任务和物体上实现了更好的泛化能力。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=UPHlqbZFZB](https://openreview.net/forum?id=UPHlqbZFZB)
