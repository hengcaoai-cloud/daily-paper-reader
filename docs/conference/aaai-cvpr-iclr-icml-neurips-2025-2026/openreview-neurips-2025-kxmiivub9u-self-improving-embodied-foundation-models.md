---
title: Self-Improving Embodied Foundation Models
title_zh: 自改进的具身基础模型
authors: "Seyed Kamyar Seyed Ghasemipour, Ayzaan Wahid, Jonathan Tompson, Pannag R Sanketi, Igor Mordatch"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=KXMIIVUB9U"
tags: ["query:data"]
score: 6.0
evidence: 利用网络规模预训练的基础模型进行机器人学习，并通过两阶段后训练与强化学习实现自主改进
tldr: 提出一种两阶段后训练方法：先通过行为克隆和步骤目标预测进行微调，再利用步骤目标预测生成奖励函数，使机器人能在最小人工监督下自主练习改进。在多种真实机器人操作任务中，该方法使机器人能够自主练习并显著提高任务成功率。该后训练框架为具身基础模型提供了一种有效的自我改进机制，减少了人工干预需求。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 基础模型在机器人底层控制中仍主要依赖行为克隆，缺乏自主改进能力。
method: 通过步骤目标预测目标同时实现行为克隆和监督微调，并从中提取奖励函数和成功检测器，以支持强化学习阶段的自我改进。
result: 在多种真实机器人操作任务中，该方法使机器人能够自主练习并显著提高任务成功率。
conclusion: 该后训练框架为具身基础模型提供了一种有效的自我改进机制，减少了人工干预需求。
---

## Abstract
Foundation models trained on web-scale data have revolutionized robotics, but their application to low-level control remains largely limited to behavioral cloning. Drawing inspiration from the success of the reinforcement learning stage in fine-tuning large language models, we propose a two-stage post-training approach for robotics. The first stage, Supervised Fine-Tuning (SFT), fine-tunes pretrained foundation models using both: a) behavioral cloning, and b) steps-to-go prediction objectives. In the second stage, Self-Improvement, steps-to-go prediction enables the extraction of a well-shaped reward function and a robust success detector, enabling a fleet of robots to autonomously practice downstream tasks with minimal human supervision. Through extensive experiments on real-world and simulated robot embodiments, our novel post-training recipe unveils significant results on Embodied Foundation Models. First, we demonstrate that the combination of SFT and Self-Improvement is significantly more sample-efficient than scaling imitation data collection for supervised learning, and that it leads to policies with significantly higher success rates. Further ablations highlight that the combination of web-scale pretraining and Self-Improvement is the key to this sample-efficiency. Next, we demonstrate that our proposed combination uniquely unlocks a capability that current methods cannot achieve: autonomously practicing and acquiring novel skills that generalize far beyond the behaviors observed in the imitation learning datasets used during training. These findings highlight the transformative potential of combining pretrained foundation models with online Self-Improvement to enable autonomous skill acquisition in robotics.

---

## 论文详细总结（自动生成）

鉴于提供的论文原文为OpenReview的验证页面，未能获取完整内容，但根据论文元数据中的摘要、方法、结论等信息，可以生成如下结构化总结。

### 1. 论文的核心问题与整体含义
- **研究动机**：具身基础模型（如机器人控制模型）虽受益于网络规模预训练，但在底层操作任务中仍主要依赖行为克隆，缺乏自主改进和持续学习的能力，类似大语言模型后训练中“强化学习微调”阶段的缺失。
- **核心问题**：如何让预训练的基础模型在少量人类监督下，通过在线练习实现策略的自主改进和新技能泛化。

### 2. 论文提出的方法论
- **整体思路**：提出一种两阶段后训练方案，将大语言模型中的监督微调（SFT）与强化学习自改进（Self‑Improvement）范式迁移至具身智能领域。
- **阶段一：监督微调（SFT）**
  - 同时使用两个目标对预训练基础模型进行微调：
    - **行为克隆**：模仿专家示范。
    - **步骤目标预测（steps‑to‑go prediction）**：预测当前状态距离任务完成的剩余步骤数。
- **阶段二：自改进（Self‑Improvement）**
  - 利用阶段一学习的“步骤目标预测”模块，提取出：
    - **形状良好的奖励函数**：基于预测的剩余步数设计稠密奖励。
    - **鲁棒的成功检测器**：判断任务是否完成。
  - 在极少人类监督下，让机器人集群利用该奖励函数在线自主练习下游任务，通过强化学习实现策略提升。

### 3. 实验设计
- **测试场景**：多种真实机器人操作任务，以及仿真机器人形态。
- **基准对比**：
  - 缩放模仿学习数据量进行监督学习的方法。
  - 当前只能依赖行为克隆的方法（即无自改进阶段）。
- **对比方式**：比较不同方法在样本效率、任务成功率以及泛化能力上的差异。

### 4. 资源与算力
- 所提供的材料中**未明确说明**所使用的GPU型号、数量、训练时长等算力细节。

### 5. 实验数量与充分性
- 元数据中提到“广泛的真实与仿真实验”“消融研究进一步突出……”，表明实验包含：
  - 真实和仿真多形态环境下的任务评估；
  - 数据缩放对比实验；
  - 不同组件（如网络预训练、自改进）的消融实验。
- 这些实验设计从维度上看较为充分，可支撑文中关键结论；但由于无法获取具体任务数量、成功率数值等细节，无法进一步评估其客观公平性。

### 6. 论文的主要结论与发现
- **样本效率大幅提升**：SFT+自改进的组合在样本效率上远超单纯缩放模仿数据量的监督学习。
- **成功率显著更高**：自改进后的策略在任务成功率上表现更优。
- **关键驱动力**：网络规模预训练与自改进阶段的结合是实现高样本效率的核心要素。
- **独特能力解锁**：该方法使机器人能够自主练习并习得超越训练示范数据分布的新技能，这是现有方法难以做到的。
- **整体意义**：预训练基础模型与在线自改进的结合为机器人自主技能获取开辟了新路径。

### 7. 优点
- **范式创新**：首次在具身基础模型中系统引入“步骤目标预测”作为连接监督微调和强化学习自改进的桥梁，设计巧妙。
- **低监督要求**：自改进阶段仅需极少量人工监督，显著降低真实机器人学习门槛。
- **实证扎实**：在真实和仿真机器人上均进行了验证，并通过消融确认了各设计选择的有效性。
- **泛化能力突破**：实现了超越训练示范的技能获取，证明了基础模型的在线适应潜力。

### 8. 不足与局限
- **算力信息缺失**：未提供训练成本数据，实际部署的可行性难以评估。
- **任务粒度未知**：缺乏具体任务类别、数量、成功率统计，无法判断方法对复杂长序任务的适应性。
- **实验细节不足**：仅有元数据，无法评估实验统计显著性、偏差控制（如成功检测器误判的影响）。
- **潜在限制**：步骤目标预测的准确性可能限制奖励函数质量；在高度随机或部分可观测环境中，预测的可靠性待验证。

（完）
