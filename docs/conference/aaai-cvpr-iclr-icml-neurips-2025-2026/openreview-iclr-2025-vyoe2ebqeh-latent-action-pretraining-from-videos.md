---
title: Latent Action Pretraining from Videos
title_zh: 从视频中进行潜在动作预训练
authors: "Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Se June Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, Lars Liden, Kimin Lee, Jianfeng Gao, Luke Zettlemoyer, Dieter Fox, Minjoon Seo"
date: 2025-01-22
pdf: "https://openreview.net/pdf?id=VYOe2eBQeh"
tags: ["query:data"]
score: 9.0
evidence: 从互联网规模视频中学习，无需机器人动作标签，预训练视觉-语言-动作模型
tldr: 提出LAPA，首个无需真实动作标签的视觉-语言-动作模型无监督预训练方法。该方法从互联网规模视频中学习离散潜在动作，预训练模型预测这些潜在动作，再在小规模机器人数据上微调，从而大幅扩展机器人学习的可用数据源。在多种机器人操作任务上，LAPA预训练的VLA模型在小数据微调后达到与有监督预训练相当的性能。该方法为大规模利用无标签视频数据进行机器人学习开辟了新途径，降低了对人工标注的依赖。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 现有VLA模型预训练依赖遥操作采集的动作标签，限制了数据规模和来源。
method: 利用VQ-VAE目标训练动作量化模型学习帧间离散潜在动作，然后预训练潜在VLA模型预测这些动作并融合任务描述。
result: 在多种机器人操作任务上，LAPA预训练的VLA模型在小数据微调后达到与有监督预训练相当的性能。
conclusion: 该方法为大规模利用无标签视频数据进行机器人学习开辟了新途径，降低了对人工标注的依赖。
---

## Abstract
We introduce Latent Action Pretraining for general Action models (LAPA), the first unsupervised method for pretraining Vision-Language-Action (VLA) models without ground-truth robot action labels. Existing Vision-Language-Action models require action labels typically collected by human teleoperators during pretraining, which significantly limits possible data sources and scale. In this work, we propose a method to learn from internet-scale videos that do not have robot action labels. We first train an action quantization model leveraging VQ-VAE-based objective to learn discrete latent actions between image frames, then pretrain a latent VLA model to predict these latent actions from observations and task descriptions, and finally finetune the VLA on small-scale robot manipulation data to map from latent to robot actions. Experimental results demonstrate that our method significantly outperforms existing techniques that train robot manipulation policies from large-scale videos. Furthermore, it outperforms the state-of-the-art VLA model trained with robotic action labels on real-world manipulation tasks that require language conditioning, generalization to unseen objects, and semantic generalization to unseen instructions. Training only on human manipulation videos also shows positive transfer, opening up the potential for leveraging web-scale data for robotics foundation models.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：当前主流的视觉-语言-动作（VLA）模型预训练严重依赖人工遥操作采集的真实动作标签，这极大限制了可用的数据规模和来源。如何利用海量的无动作标签的互联网视频数据来预训练机器人操作模型，是一个尚未解决的关键问题。
- **整体含义**：论文提出了一种无监督预训练方法 LAPA，使得 VLA 模型能够从没有动作标签的大规模视频中学习，然后在少量带标签的机器人数据上微调，即可实现或超越需要大量动作标签的有监督预训练模型的性能。这为机器人基础模型利用互联网规模的视频数据打开了大门，有望大幅降低对人工标注的依赖。

### 2. 论文提出的方法论
- **核心思想**：将帧间变化量化为离散的“潜在动作”，在不访问真实动作标签的情况下，通过预测这些潜在动作来预训练模型，再将其迁移到真实的机器人动作输出上。
- **关键技术细节与流程**：
  - **动作量化模型训练（第一阶段）**：基于 VQ‑VAE 目标，在视频相邻图像帧之间学习离散的潜在动作表示。该模型将连续的帧间变化映射到一个有限的码本（codebook）中，每一帧对应一个潜在动作索引。
  - **潜在 VLA 模型预训练（第二阶段）**：预训练一个视觉‑语言‑动作模型，输入为观测（图像）和任务描述（语言指令），输出为预测的潜在动作码。此阶段使用大规模无动作标签的视频数据，模型学习如何根据当前状态和语言指令推断下一步该执行哪个离散潜在动作。
  - **下游微调（第三阶段）**：在小规模带真实机器人动作标签的操作数据上，对预训练好的 VLA 模型进行微调。此时模型学习将预测出的潜在动作映射回真实的机器人动作空间，从而完成从“潜在动作”到“物理动作”的适应。
- **算法流程简述**：视频 → 帧间量化 → 离散潜在动作序列 → 预训练（预测潜在动作 + 融合语言）→ 少量机器人数据微调（潜在动作 → 真实动作）。整个过程无需在预训练阶段接触任何实际机器人的动作标注。

### 3. 实验设计
- **使用数据集/场景**：
  - 预训练数据：互联网规模视频（具体数据集名称未在摘要中给出，但提及可以只使用人类操作视频，也显示正向迁移效果）。
  - 微调与评估：小规模机器人操作数据，涵盖需要语言条件化、对未见物体的泛化、对未见指令的语义泛化等 realistic manipulation 场景。
- **Benchmark与对比方法**：
  - 与现有利用大规模视频训练机器人操作策略的技术对比（LAPA 显著优于这些方法）。
  - 与使用真实机器人动作标签预训练的当前最先进的 VLA 模型对比（在 real‑world manipulation 任务上 LAPA 表现更优，尤其是在语言条件化和泛化能力方面）。
- **实验充分性**：摘要强调在多个维度（语言条件化、物体泛化、指令泛化）上进行了评估，并展示了人类视频的正向迁移效果，表明实验设计较为全面。

### 4. 资源与算力
- **提供信息**：摘要和元数据中**未明确提及** GPU 型号、数量、训练时长等算力细节。由于无法获取论文全文，无法补充该部分信息。

### 5. 实验数量与充分性
- **实验组数推测**：基于摘要，至少包含以下几组实验：
  - 与多种 baseline 方法的对比（大规模视频训练技术，有监督 VLA 模型）。
  - 多类机器人操作任务（语言条件化、物体泛化、指令泛化）。
  - 消融/变体实验：包括仅使用人类操作视频进行预训练的迁移实验。
- **充分性评估**：从覆盖的任务类型和对比维度来看，实验设计较为充分、客观。该方法在真实世界机器人操作任务上进行了验证，并明确展示了相对于有监督预训练的竞争力，以及人类视频数据的正向作用。但由于缺乏正文细节，无法对消融实验的彻底性做更精确的判断。

### 6. 论文的主要结论与发现
- LAPA 是无监督 VLA 预训练的第一个有效方法，成功将预训练数据源从带标签机器人数据扩展到无标签视频。
- 该预训练策略在多种机器人操作任务上显著超越了其他利用大规模视频训练的方法。
- 即使与用真实动作标签预训练的最优 VLA 模型相比，LAPA 在真实世界任务中表现更优，尤其在需要语言理解、未见物体泛化和语义泛化的情况下。
- 仅使用人类操作视频进行预训练就能带来正向迁移，证明网络视频在机器人学习中的巨大潜力。

### 7. 优点
- **数据效率与可扩展性**：突破了对昂贵动作标注的依赖，使机器人学习可以利用近乎无限的网络视频资源。
- **方法新颖**：通过离散潜在动作桥接视频预训练与机器人微调，为无监督 VLA 提供了清晰的范式。
- **性能优异**：在同等甚至更优的性能下，实现了从无监督视频到物理动作的有效迁移，且有较强的泛化能力。
- **实际应用价值高**：大幅减少人工遥操作标注需求，降低了机器人技能学习的门槛和成本。

### 8. 不足与局限
- **算力与训练细节不明**：从摘要无法获知训练所需的计算资源和时间，方法在大规模扩展时的效率仍有待后续论文正文揭示。
- **潜在动作的表征能力**：离散化的潜在动作是否能完美保留所有必要的操控信息，在更精细或连续的操控任务中可能面临挑战。
- **预训练数据质量依赖**：虽然可以利用互联网视频，但视频的质量、多样性及与机器人形态的领域差异（如人类手 vs. 机械夹爪）可能对迁移效果产生负面影响，摘要虽然展示了人类视频的正向迁移，但可能仍存在分布偏移问题。
- **微调数据需求**：方法仍然需要少量机器人操作数据进行微调，零样本迁移的能力尚未验证。
- **评估范围**：目前展示的任务集中在语言引导的物体操作，对更复杂的长时间任务、移动操作或动态环境的适用性有待进一步验证。

（完）
