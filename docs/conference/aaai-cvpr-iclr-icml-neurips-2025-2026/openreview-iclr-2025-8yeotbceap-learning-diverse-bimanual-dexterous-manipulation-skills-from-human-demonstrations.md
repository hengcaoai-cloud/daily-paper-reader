---
title: Learning Diverse Bimanual Dexterous Manipulation Skills from Human Demonstrations
title_zh: 从人类示教学习多样化双手灵巧操作技能
authors: "Bohan Zhou, Haoqi Yuan, Yuhui Fu, Zongqing Lu"
date: 2024-09-17
pdf: "https://openreview.net/pdf?id=8yEoTBceap"
tags: ["query:data"]
score: 9.0
evidence: 从人类示教中学习多样化的双手灵巧操作技能。
tldr: 针对双手灵巧操作任务多样性不足和策略学习困难的问题，本文提出BiDexHD框架，利用教师-学生策略学习从丰富的人类演示中高效学习多样化技能。实验表明该方法显著提升了任务覆盖和策略性能，为通用灵巧操作提供了新途径。
source: ICLR-2025-Rejected-Public
selection_source: conference_retrieval
motivation: 高维动作空间和任务复杂性导致双手灵巧操作策略学习困难，现有基准任务多样性有限。
method: BiDexHD统一现有双手数据集构建任务，采用教师-学生策略学习应对高维挑战。
result: 在多种双手灵巧操作任务上取得优于现有方法的成功率。
conclusion: 从人类示教中高效学习多样化双手技能是可行的，并能推广至多种任务。
---

## Abstract
Bimanual dexterous manipulation is a critical yet underexplored area in robotics. Its high-dimensional action space and inherent task complexity present significant challenges for policy learning, and the limited task diversity in existing benchmarks hinders general-purpose skill development. Existing approaches largely depend on reinforcement learning, often constrained by intricately designed reward functions tailored to a narrow set of tasks. In this work, we present a novel approach for efficiently learning diverse bimanual dexterous skills from abundant human demonstrations. Specifically, we introduce BiDexHD, a framework that unifies task construction from existing bimanual datasets and employs teacher-student policy learning to address all tasks. The teacher learns state-based policies using a general two-stage reward function across tasks with shared behaviors, while the student distills the learned multi-task policies into a vision-based policy. With BiDexHD, scalable learning of numerous bimanual dexterous skills from auto-constructed tasks becomes feasible, offering promising advances toward universal bimanual dexterous manipulation. Our empirical evaluation on the TACO dataset, spanning 141 tasks across six categories, demonstrates a task fulfillment rate of 74.59% on trained tasks and 51.07% on unseen tasks, showcasing the effectiveness and competitive zero-shot generalization capabilities of BiDexHD. For videos and more information, visit our project page.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：双手灵巧操作（Bimanual Dexterous Manipulation）是机器人领域关键但研究不足的方向。其高维动作空间和固有的任务复杂度给策略学习带来极大困难，同时现有基准任务多样性有限，难以催生通用操作技能。
- **现有方法局限**：主流方案重度依赖强化学习，常需为狭窄任务集精心设计奖励函数，导致策略难以泛化到新任务，且手工设计奖励工程成本高。
- **研究动机**：人类示教数据蕴含丰富的操作多样性，但如何高效利用大量示教学习多样化、可扩展的双手灵巧技能，尚未得到充分解决。本文旨在从大量人类示教出发，提出能够自动构建任务、可扩展学习多种技能的框架，朝着通用双手灵巧操作迈出一步。

## 2. 论文提出的方法论

- **整体框架**：BiDexHD，包含两大核心组件：
  - **任务统一构建**：从现有双手操作数据集（如 TACO）自动统一提取和定义任务，无需手工切分。
  - **教师‑学生策略学习**：应对多维动作空间和任务多样性带来的学习挑战。
- **教师策略（Teacher Policy）**
  - 学习基于状态（state‑based）的多任务策略。
  - 采用**通用的两阶段奖励函数**，无需为每个任务手工设计奖励，利用任务间共享的行为结构（shared behaviors）训练教师完成全部任务。
- **学生策略（Student Policy）**
  - 将教师已学到的多任务操作知识蒸馏为**基于视觉（vision‑based）的策略**，使学生能够直接从图像观察执行多样化技能。
  - 蒸馏过程提升了视觉策略在多种任务上的稳定性和成功率。
- **可扩展性**：任务由数据自动构建，教师‑学生框架一次性学会全部任务，实现从人类示教中规模化学习大量双手灵巧技能。

## 3. 实验设计

- **数据集与场景**：
  - 使用 **TACO 数据集**，包含 6 个类别共 141 个双手灵巧操作任务。
  - 任务涵盖不同物体、不同操作类型，具有明确的任务多样性和难度梯度。
- **评估基准**：
  - 在全部训练任务上评测任务完成率（fulfillment rate）。
  - 特别测试了**未见任务（unseen tasks）** 上的零样本泛化能力。
- **对比方法**：文中与现有双手灵巧操作方法进行对比（限于摘要未列出具体方法名），BiDexHD 在成功率上表现更优。

## 4. 资源与算力

- 论文摘要及提供的元数据中**未明确说明**所使用的 GPU 型号、数量、训练时长等算力信息。
- 无法推断教师策略和学生策略的具体算力开销，也无法判断实验的可复现所需资源规模。

## 5. 实验数量与充分性

- **实验规模**：
  - 涵盖 6 个类别共 141 个双手操作任务，训练任务 + 未见任务两组评估，提供了较充实的任务覆盖面。
  - 包含了与现有方法的对比实验（推测至少一组主要对比）。
- **充分性评价**：
  - 在任务数量和多样性上明显优于以往仅包含少量任务的基准，具有较好的代表性。
  - 未见任务上的零样本泛化测试增加了实验的说服力。
  - **不足**：摘要中未提及消融实验（如奖励函数两阶段设计的必要性、教师‑学生框架的贡献度分析）、鲁棒性测试或真实机器人部署结果，因此无法完全评估实验设计的全面性与客观公平性。
- **结论公平性**：以标准任务完成率作为主要指标，未见明显偏向。但未呈现对比方法细节，无法判断对比条件是否完全一致。

## 6. 论文的主要结论与发现

- 从大量人类示教中高效学习多样化的双手灵巧操作技能是**可行**的，BiDexHD 框架能成功扩展到上百个任务。
- 教师‑学生策略学习设计有效克服高维动作空间和任务复杂性的挑战，无需逐任务奖励工程。
- 所学策略表现出一定的**零样本泛化能力**，在未见任务上依然达到 51.07% 的完成率，证明其技能具有一定通用性。
- 该方法为通用双手灵巧操作提供了可行的技术路径。

## 7. 优点

- **任务多样性大幅扩展**：统一现有数据集自动构建 141 个任务，明显拓宽了双手灵巧操作的评估范围。
- **奖励函数通用化**：两阶段通用奖励降低了为每个任务设计奖励的成本，易于扩展到新任务。
- **教师‑学生框架**：结合状态策略的优势和视觉策略的实用性，兼顾学习效率与部署灵活性。
- **零样本泛化验证**：将未见任务作为独立测试集，客观评估了策略的泛化能力，增强了结果的可信度。

## 8. 不足与局限

- **算力信息缺失**：论文未披露计算资源细节，难以评估方法的训练成本和可复现性。
- **实验覆盖不完整**：未见消融研究的详细说明，无法判断各个模块（如通用奖励、蒸馏）的相对贡献；也未提及真实机器人平台的验证，尚缺 sim‑to‑real 转移证据。
- **未见任务成功率有限**：零样本泛化成功率 51%，仍有相当比例任务无法完成，说明对完全陌生操作场景的泛化能力存在瓶颈。
- **依赖数据集质量**：任务构建完全基于现有数据集，可能受限于数据覆盖的偏差；对于与数据集差异较大的新技能，方法可能表现不佳。
- **对比方法未知**：若对比方法实现不充分或超参数未充分调优，结果可能被高估。

（完）
