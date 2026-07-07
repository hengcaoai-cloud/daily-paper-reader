---
title: "Human2Robot: Learning Robot Actions from Paired Human-Robot Videos"
title_zh: Human2Robot：从成对人-机器人视频学习机器人动作
authors: "Sicheng Xie, Haidong Cao, Zejia Weng, Zhen Xing, Haoran Chen, Shiwei Shen, Jiaqi Leng, Zuxuan Wu, Yu-Gang Jiang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38086/42048"
tags: ["query:data"]
score: 10.0
evidence: 精确对齐的成对人-机器人视频数据集，从人类演示学习机器人动作
tldr: Human2Robot 提出了一个包含 2600 个精确同步的人-机器人视频片段的数据集，并将细粒度人机对齐建模为条件视频生成问题，从而从人类演示直接学习机器人动作。该方法突破了传统粗略对齐的局限，实现了帧级动力学学习。实验表明在复杂操作和新任务上泛化能力显著提升，为人类技能向机器人的高效迁移提供了新范式。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 746, \"height\": 1079, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 872, \"height\": 260, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1796, \"height\": 1033, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1830, \"height\": 609, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38086/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1830, \"height\": 327, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38086/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1105, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38086/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 704, \"height\": 328, \"label\": \"Table\"}]"
motivation: 现有方法依赖粗糙对齐的视频对，无法捕获帧级操作动力学，泛化性差。
method: 构建精确同步的人-机器人视频数据集，将细粒度对齐视为条件视频生成任务。
result: 在新颖任务上展现出强泛化能力，优于基于粗略对齐的方法。
conclusion: Human2Robot 通过精确对齐的视频生成实现了人类技能到机器人的有效迁移。
---

## Abstract
Distilling knowledge from human demonstrations is a promising way for robots to learn and act. Existing methods, which often rely on coarsely-aligned video pairs, are typically constrained to learning global or task-level features. As a result, they tend to neglect the fine-grained frame-level dynamics required for complex manipulation and generalization to novel tasks. We posit that this limitation stems from a vicious circle of inadequate datasets and the methods they inspire. To break this cycle, we propose a paradigm shift that treats fine-grained human-robot alignment as a conditional video generation problem. To this end, we first introduce H&R, a novel third-person dataset containing 2,600 episodes of precisely synchronized human and robot motions, collected using a VR teleoperation system. We then present Human2Robot, a framework designed to leverage this data. Human2Robot employs a Video Prediction Model to learn a rich and implicit representation of robot dynamics by generating robot videos from human input, which in turn guides a decoupled action decoder. Our real-world experiments demonstrate that this approach not only achieves high performance on seen tasks but also exhibits significant one-shot generalization to novel positions, objects, instances, and even new task categories.

---

## 论文详细总结（自动生成）

# 论文总结

## 1. 核心问题与整体含义（研究动机与背景）
- 传统方法使用粗略对齐的人-机器人视频对进行学习，只能提取全局或任务级特征，忽略了细粒度帧级动力学，导致复杂操作和新任务泛化能力差。
- 该局限源于数据集不足与方法受限的恶性循环。
- 本文提出将细粒度人-机器人对齐重构为条件视频生成问题，旨在打破此循环，实现从人类演示到机器人动作的精细映射。

## 2. 方法论：核心思想与关键技术细节
- **数据集**：构建了H&R数据集，利用VR遥操作系统采集2600条精确同步的人手与机器人臂视频。
- **框架Human2Robot**：
  - **第一阶段（VPM）**：视频预测模型，基于人类视频生成机器人视频，包含：
    - 行为提取器（Behavior Extractor）：从人类视频提取运动与位置线索。
    - 空间UNet（S-UNet）：初始化自Stable Diffusion，提取机器人臂特征。
    - 时空UNet（ST-UNet）：结合空间层与时间层，建模时序动力学，生成预测帧。
    - VAE编码器/解码器：将图像压缩到潜空间去噪解码。
    - 训练分两小步：首先生成单帧，再训练时间层生成视频，优化目标为噪声预测损失（均方误差）。
  - **第二阶段（动作解码器）**：
    - 将预训练的VPM作为视觉编码器，提取第一次去噪后的特征（upsampling层输出）。
    - 使用Video Former将特征聚合为固定长度表示。
    - 通过扩散策略（Diffusion Policy）以交叉注意力方式注入聚合特征，重建动作序列，优化目标为动作噪声预测损失。
- **KNN推理**：对已知任务，通过DINOv2/CLIP提取当前场景特征，检索最相似的人类演示视频作为条件输入，无需显式提供人类视频。

## 3. 实验设计：数据集、场景与对比方法
- **任务场景**：
  - 训练：基础拾取-放置、推拉等简单任务。
  - 测试：涵盖外观、位置、实例、背景、任务组合、全新任务（如写字）等泛化设定。
- **对比基准**：
  - Diffusion Policy (DP)：语言条件的动作扩散策略。
  - XSkill：基于自监督学习的人-视频条件策略。
  - Video Prediction Policy (VPP)：语言条件的视频预测预训练策略。
  - Action Decoder w. Human：将人类视频直接输入动作解码器。
  - Human2Robot w/o. Pretrain：去掉视频生成预训练。
  - Human2Robot w. KNN：结合KNN的已知任务执行。

## 4. 资源与算力
- VPM训练：4块NVIDIA A100 GPU，耗时3天。
- 第二阶段训练：8块NVIDIA A100 GPU，约6小时。
- 特定任务（写字）训练：8块A100 GPU，约6小时。

## 5. 实验数量与充分性
- 共涉及：
  - 基础任务多组成功率比较（推拉、拾放、旋转等）。
  - 6种泛化维度（外观、位置、实例、背景、组合任务、全新任务）的测试。
  - 消融实验：视频预训练贡献、直接人类视频条件、KNN方法。
- 对比当前主流方法，测试环境覆盖真实世界，评估指标为成功率（每组20次试验），实验设计较全面、公平。

## 6. 主要结论与发现
- Human2Robot在已知任务上成功率最高（95%），显著优于XSkill（53%）和VPP（80%）。
- 在六种泛化任务上均表现优异（70-100%），而其他基线在实例、背景、组合和全新任务上完全失败（0%）。
- 视频生成预训练至关重要，缺少时成功率骤降至10-20%。
- KNN方法在无人类演示时仍保持较高成功率（82%）。

## 7. 优点
- 首次提出精确同步的人-机器人视频数据集，推动细粒度对齐学习。
- 将细粒度对齐建模为条件视频生成，捕捉帧级动力学，泛化性大幅提升。
- 两阶段设计解耦动态表示与动作执行，并可复用于已知任务的KNN驱动。
- 在多种未见任务乃至写字等全新技能上展现 one-shot 泛化能力。

## 8. 不足与局限
- 数据集仅包含简单拾取-放置任务，未涵盖更复杂的灵巧操作（如旋拧）。
- 依赖VR遥操作系统，存在“具身差异”问题，限制了可采集的任务类型。
- 对全新任务的泛化仍需提供人类视频作为条件，尚不能完全自主生成新技能。
- 实验平台为固定桌面环境，更复杂的动态场景或人机交互未涉及。

（完）
