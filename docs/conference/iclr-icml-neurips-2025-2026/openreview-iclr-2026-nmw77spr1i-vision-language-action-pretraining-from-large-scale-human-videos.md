---
title: Vision-Language-Action Pretraining from Large-Scale Human Videos
title_zh: 从大规模人类视频中预训练视觉-语言-动作模型
authors: "Hao Luo, Yicheng Feng, Wanpeng Zhang, Sipeng Zheng, Ye Wang, Haoqi Yuan, jiazheng liu, Chaoyi Xu, Haiweng Xu, Qin Jin, Zongqing Lu"
date: 2025-09-04
pdf: "https://openreview.net/pdf?id=nmW77spR1I"
tags: ["query:data"]
score: 10.0
evidence: 利用大规模人类视频进行 VLA 预训练，通过物理指令微调实现灵巧操作。
tldr: 现有 VLA 模型在需要高灵巧性的复杂操作任务上表现不佳，主要受限于模拟数据与真实数据的差距或有限的遥操作演示。本文提出以人手为操作模板，从大规模人类视频中预训练 VLA 模型，并通过物理指令微调（结合透视空间对齐和物理环境后训练）实现跨实体的灵巧操作。此外，引入部件级动作分词来增强动作表示。该方法在灵巧操作任务上展示了从人类视频迁移到机器人的潜力，为利用网络规模的人类操作数据训练通用机器人策略开辟了新途径。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有 VLA 模型依赖合成数据或有限遥操作演示，难以泛化到高灵巧性操作任务。
method: 以人手为操作模板，从大规模人类视频中预训练 VLA 模型，并通过物理指令微调、透视空间对齐和后训练适应实现跨实体迁移，引入部件级动作分词。
result: 方法在灵巧操作任务上取得有效表现，证明从人类视频到机器人操作的迁移可行性。
conclusion: 该工作为利用网络人类操作视频训练通用灵巧操作策略提供了新范式。
---

## Abstract
Existing Vision-Language-Action models (VLA) struggle with complex manipulation tasks requiring high dexterity and generalization, primarily due to their reliance on synthetic data with significant sim-to-real gaps or limited teleoperated demonstrations.
To address this bottleneck, we propose leveraging human hands as a ``manipulator template'', capitalizing on the rich dexterity and scalability present in web data of human manipulation.
Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, perspective spatial alignment for reasoning in a unified physical
space, and post-training adaptation in physical environment.
Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. 
To support our paradigm, we develop a comprehensive data curation pipeline that integrates heterogeneous sources --- including motion capture, VR, and RGB-only videos --- into a large-scale dataset with millions of motion-based instructional instances.
We empirically show the excellence of our model in hand motion generation and instruction following, and it also scales well with model and data sizes.
Importantly, we observe the expected gains in robotic dexterous manipulation as physical instruction tuning is applied.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：当前的视觉-语言-动作（VLA）模型在处理需要较高灵巧性和泛化能力的复杂操控任务时表现不佳，主要原因是它们依赖存在显著“模拟-真实”差距的合成数据，或依赖数量有限的遥操作演示。
- **整体含义**：该工作提出将“人手”作为操控模板，利用大规模互联网人类视频中丰富的灵巧操作数据来预训练 VLA 模型，从而使机器人能够习得更通用、更精细的操控策略。这为利用现成的网络人类操作视频训练通用机器人灵巧操作策略开辟了一条新的范式。

## 2. 论文提出的方法论

- **核心思想**：以人手为操作范本，从大规模人类视频中学习精细运动先验，再通过对齐与适应将其迁移到机器人实体上。
- **关键技术细节与流程**：
    - **物理指令微调（Physical Instruction Tuning）**：一种新的训练范式，包含三个阶段：
        1.  **大规模 VLA 预训练**：在包含动作捕捉、VR 和纯 RGB 视频等多元数据源构建的大规模基于运动的教学实例数据集上进行预训练。
        2.  **透视空间对齐**：设计统一物理空间的推理机制，使模型能够理解并关联人手与机器人末端执行器的空间关系。
        3.  **物理环境后训练适应**：在物理仿真或真实环境中对预训练模型进行微调，完成跨实体迁移。
    - **部件级运动分词（Part-level Motion Tokenization）**：提出一种能够实现毫米级重建精度的运动表示方法，对手部精确轨迹进行离散化，供模型学习精细动作。
- **数据构建**：开发了一套综合数据管护流水线，整合动作捕捉、VR、RGB 视频等异构数据源，生成百万级基于运动的教学实例数据集。

## 3. 实验设计

- **数据集/场景**：
    - 使用自建的百万级人类操作数据集，包含动作捕捉、VR 及 RGB 视频数据。
    - 在机器人灵巧操作任务上验证，具体操作场景未在摘要中详述。
- **Benchmark与对比方法**：摘要未明确提及所参与的公开 benchmark 或详细对比的基线方法。根据元数据，该论文被 ICLR 2026 拒稿，因此未呈现发表级别的严格实验对比。
- **评估维度**：
    - 手部运动生成的精度。
    - 指令跟随能力。
    - 模型和数据的缩放特性。
    - 机器人灵巧操作任务上的增益。

## 4. 资源与算力

- 论文摘要及元数据中**未明确说明**所使用的 GPU 型号、数量及训练时长。由于原 PDF 内容未能成功抓取，详细计算资源信息缺失。

## 5. 实验数量与充分性

- **实验规模**：摘要中提到了手部运动生成评估、指令跟随评估、缩放性实验以及机器人操作任务实验，推测至少包含 4 类主要实验组。
- **充分性与客观性**：
    - 文中声称模型展现了卓越的手部运动生成与指令跟随能力，并具有缩放性。
    - 然而，由于未提供具体 benchmark 名称、对比基线方法及其数值结果，无法判断实验对比的公平性和充分性。被 ICLR 拒稿可能暗示实验验证或对比在某些方面未完全满足顶会审稿人的要求。
    - 消融实验未在摘要中明示，但“部件级运动分词”等模块的提出暗示可能包含相关消融分析。

## 6. 论文的主要结论与发现

- 从大规模人类视频中预训练 VLA 模型，结合物理指令微调，能够有效生成精准手部运动并遵循指令。
- 模型性能展现出良好的数据与模型规模可扩展性。
- 应用物理指令微调后，机器人灵巧操作任务获得了预期的性能增益，验证了从人类视频到机器人操控迁移的可行性。

## 7. 优点

- **视角新颖**：将人手作为直接的操控模板，充分利用丰富的网络人类操作数据，绕过了遥操作数据稀缺的瓶颈。
- **方法论系统**：提出的物理指令微调框架完整覆盖了预训练、空间对齐、实体适配三个阶段，逻辑清晰。
- **高精度动作表示**：部件级运动分词达到毫米级精度，有助于保留人类灵巧操作的细腻特性。
- **数据管护完备**：开发了融合动捕、VR、RGB 多源数据的大规模流水线，数据质量与多样性有保障。

## 8. 不足与局限

- **实验细节不透明**：缺乏具体对比方法、基准测试以及数值结果，难以客观评估方法的绝对优势。被拒稿状态表明其实验验证或论述可能不够坚实。
- **跨实体对齐的挑战**：以人手为模板，在实际部署时需解决人手自由度与机器人手爪/灵巧手之间的结构差异，摘要未深入说明该对齐的泛化性及局限性。
- **物理环境后训练的依赖性**：仍需仿真或真实物理环境微调，未能完全摆脱对物理交互数据的依赖。
- **应用限制**：所有结论均停留在“潜力”与“预期增益”层面，未提供真实世界高灵巧任务（如穿针引线）的成功率或鲁棒性指标，实用性待验证。

（完）
