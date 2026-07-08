---
title: "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation"
title_zh: ForceVLA：通过力感知混合专家增强视觉-语言-动作模型以实现接触丰富操作
authors: "Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang, Yan Song, Panpan Cai, Wenqiang Zhang, Cewu Lu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=2845H8Ua5D"
tags: ["query:model"]
score: 9.0
evidence: 使用力感知混合专家模块增强 VLA 模型，实现接触丰富的操作。
tldr: 现有 VLA 模型在需要精细力控的接触丰富任务（如视觉遮挡或动态不确定）中表现不佳。本文提出 ForceVLA，将外部力传感视为第一类模态，通过力感知混合专家融合模块（FVLMoE）动态集成预训练的视觉-语言嵌入与实时六轴力反馈，在动作解码时实现上下文感知的多模态路由。该方法使 VLA 模型能更好地处理接触丰富操作，提升了力觉依赖任务的性能，推动通用操作模型走向力觉融合。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有 VLA 模型在需要精细力控的接触丰富任务中表现不佳，尤其在视觉遮挡或动态不确定下。
method: 提出 ForceVLA 框架，引入力感知混合专家模块，动态融合视觉-语言嵌入与实时力反馈进行动作解码。
result: 实验证明 ForceVLA 在多种接触丰富任务上优于基线 VLA 模型，展示了力感知对精细控制的重要性。
conclusion: 将力传感作为 VLA 模型的第一类模态，显著提升了机器人在接触丰富任务中的操作能力。
---

## Abstract
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose \textbf{ForceVLA}, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces \textbf{FVLMoE}, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2\% over strong $\pi_0$-based baselines, achieving up to 80\% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025/.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
使用力感知混合专家模块增强 VLA 模型，实现接触丰富的操作。

### 2. 核心内容
现有 VLA 模型在需要精细力控的接触丰富任务（如视觉遮挡或动态不确定）中表现不佳。本文提出 ForceVLA，将外部力传感视为第一类模态，通过力感知混合专家融合模块（FVLMoE）动态集成预训练的视觉-语言嵌入与实时六轴力反馈，在动作解码时实现上下文感知的多模态路由。该方法使 VLA 模型能更好地处理接触丰富操作，提升了力觉依赖任务的性能，推动通用操作模型走向力觉融合。

### 3. 对应检索需求
Papers central to embodied foundation model, especially work that connects or combines: embodied foundation models for physical robots; vision-language-action models for robot control; World Action Model for embodied agents; training with heterogeneous human and robot data; Representation learning for robot perception and control; few-shot generalization for robots; Memory mechanisms, long horizon planning, and cross embodiment transfer for generalist robot model; Embodied foundation model with 3D spatial understanding and reasoning capabilities; Training embodied foundation models with large scale heterogeneous robot data; Zero shot and few shot generalization in vision language action models and world action models for robotics.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=2845H8Ua5D](https://openreview.net/forum?id=2845H8Ua5D)
