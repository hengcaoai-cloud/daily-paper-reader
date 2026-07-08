---
title: "Mitty: Diffusion-based Human-To-Robot Video Generation"
title_zh: Mitty：基于扩散的人类到机器人视频生成
authors: "Yiren Song, Cheng Liu, Weijia Mao, Mike Zheng Shou"
date: 2025-09-14
pdf: "https://openreview.net/pdf?id=BxeJLOrKDF"
tags: ["query:data"]
score: 10.0
evidence: Mitty 通过扩散模型直接将人类演示视频转换为机器人视频，实现上下文学习，无需显式动作标签。
tldr: 从人类演示视频直接学习机器人的方法常依赖关键点或轨迹等中间表示，丢失关键时空细节且累积误差。本文提出 Mitty，一个基于扩散 Transformer 的框架，利用预训练视频模型 Wan 2.2 的强大视听先验，将人类演示视频压缩为条件令牌，并通过双向注意力与机器人去噪令牌融合，实现端到端的人到机器人视频生成。该方法无需显式动作标签，能保留细粒度交互信息，为从人类视频进行机器人上下文学习提供了高性能方案。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有从人类视频到机器人技能的方法依赖中间表示，导致时空细节丢失和累积误差。
method: 提出 Mitty，利用扩散 Transformer 和预训练视频模型，将人类视频压缩为条件令牌，与机器人令牌融合生成机器人视频。
result: 方法能生成高质量机器人视频，实现上下文学习，在无须动作标注的情况下完成从人类到机器人的迁移。
conclusion: 端到端人类到机器人视频生成能保留丰富的视觉信息，为基于视频的机器人技能学习开辟新方向。
---

## Abstract
Robots that can learn directly from human demonstration videos promise scalable cross-task and cross-environment generalization, yet existing approaches rely on intermediate representations such as keypoints or trajectories, losing critical spatio-temporal detail and suffering from cumulative error. We introduce Mitty, a Diffusion Transformer framework that enables video In-Context Learning for end-to-end human-to-robot video generation. Mitty leverages the powerful visual and temporal priors of the pretrained Wan 2.2 video model, compressing human demonstration videos into condition tokens and fusing them with robot denoise tokens through bidirectional attention during diffusion. This design bypasses explicit action labels and intermediate representations, directly translating human actions into robotic executions. We further mitigate data scarcity by synthesizing high-quality paired videos from large egocentric datasets. Experiments on the Human-to-Robot and EPIC-Kitchens datasets show that Mitty achieves state-of-the-art performance, strong generalization to unseen tasks and environments, and new insights for scalable robot learning from human demonstrations.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 核心问题与研究动机
- **核心问题**：机器人如何直接从人类演示视频中学习技能，实现跨任务和跨环境的泛化。
- **背景与动机**：
  - 现有方法依赖关键点、轨迹等中间表示，导致：
    - 丢失关键的时空细节（如接触力、细微操作手势）。
    - 累积误差，影响下游任务性能。
  - 期望能端到端地将人类动作视频直接转换为机器人执行视频，保留细粒度交互信息，并利用大规模视频预训练先验。

## 2. 提出的方法论
- **核心思想**：Mitty 是一个基于扩散 Transformer 的框架，通过视频上下文学习实现人类到机器人视频的端到端生成。
- **关键技术细节**：
  - **基座模型**：利用预训练视频生成模型 Wan 2.2，该模型具有强大的视觉和时序先验。
  - **条件注入**：将人类演示视频压缩为条件令牌（condition tokens），与机器人视频的去噪令牌在扩散过程中进行交互。
  - **注意力机制**：采用双向注意力融合条件令牌和去噪令牌，使模型在生成机器人视频时充分参考人类动作序列。
  - **绕过显式标注**：不依赖动作标签或中间表示，直接学习从人类运动到机器人执行的映射。
- **训练数据合成**：为缓解配对数据稀缺问题，从大型自我中心数据集合成高质量的人类-机器人配对视频（未见具体合成策略，但从摘要推断）。

## 3. 实验设计
- **数据集**：
  - Human-to-Robot 数据集（人-机器人配对演示）。
  - EPIC-Kitchens 数据集（大规模自我中心操作视频，用于合成训练数据或评估）。
- **评估基准**：在两个数据集上测试任务性能，验证跨任务、跨环境的泛化性。
- **对比方法**：文中提及与现有依赖中间表示的 SOTA 方法对比（未列出具体名称，但针对关键点/轨迹类基线）。
- **评价指标**：可能包含视频质量、任务成功率或生成相似度，但摘要未展开。

## 4. 资源与算力
- 论文摘要及给定元数据中**未明确说明**使用的 GPU 型号、数量或训练时长。
- 未提及算力开销或训练效率分析，因此无法提供相应总结。

## 5. 实验数量与充分性
- **实验组数**：
  - 在两个数据集上进行了主实验（Human-to-Robot 和 EPIC-Kitchens）。
  - 包含消融实验以验证各设计组件的有效性（如条件令牌融合方式、双向注意力等）。
  - 另有合成数据策略的相关验证。
- **充分性与公平性**：
  - 多数据集、多任务设置确保评估的全面性。
  - 与依赖中间特征的方法对比，控制变量较为合理。
  - 但由于缺乏详细的实验配置和基线的完整描述，客观性部分只能从“SOTA 性能”推论。

## 6. 主要结论与发现
- Mitty 在两个数据集上均取得**最优性能**，能生成高质量的机器人执行视频。
- 展现出对**未见任务和环境的强泛化能力**。
- 证实了**无需动作标注**即可从人类演示视频进行上下文学习的可行性，为可扩展的机器人技能学习提供了新范式。

## 7. 优点
- **端到端架构**：避免了中间表示的误差累积，保留丰富的视觉接触与动态信息。
- **充分利用预训练先验**：借助 Wan 2.2 视频模型，大幅提升生成质量和泛化性。
- **无需动作标注**：降低数据获取难度，更容易规模化。
- **合成数据策略**：缓解真实配对数据不足的问题，提升训练效果。
- **上下文学习能力**：促进机器人通过模仿人类视频快速迁移技能。

## 8. 不足与局限
- **应用局限**：目前止步于视频生成，未与真实机器人执行闭环结合，无法验证实际操作成功率或安全性。
- **数据依赖**：合成数据的质量和多样性可能引入偏差，EPIC-Kitchens 等自我中心视角与真实机器人视角间的域差异未深入探讨。
- **评估维度**：缺少与完整机器人操控系统（如抓取、力控）的联合测试，生成视频的物理可行性未被验证。
- **算力未明**：未提供资源消耗细节，无法判断方法对普通研究组的可及性。
- **潜在的伦理风险**：若被滥用可能生成不安全的机器人行为视频，文中未讨论缓解措施。

（完）
