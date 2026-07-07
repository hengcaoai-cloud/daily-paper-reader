---
title: "H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation"
title_zh: "H-RDT: 人类操作增强的双臂机器人操作"
authors: "Hongzhe Bi, Lingxuan Wu, Tianwei Lin, Hengkai Tan, Zhizhong Su, Hang Su, Jun Zhu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38875/42837"
tags: ["query:data"]
score: 9.0
evidence: 利用大规模第一人称人类操作视频与3D手部姿态，通过扩散变压器增强双臂机器人操作
tldr: 提出H-RDT（人-机器人扩散变压器），利用大规模带有3D手部姿态标注的第一人称人类操作视频提供行为先验，增强双臂机器人操作能力。针对机器人演示数据稀缺的问题，该方法将人类操作数据转化为机器人可用的动作先验，实现从人类技能到机器人的迁移。实验表明该方法能有效提升双臂操作策略的性能，为跨形态机器人学习提供了新途径。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38875/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1832, \"height\": 1135, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38875/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1402, \"height\": 919, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38875/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 893, \"height\": 684, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38875/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 834, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38875/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 870, \"height\": 215, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38875/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1268, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38875/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 874, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38875/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 830, \"height\": 461, \"label\": \"Table\"}]"
motivation: 模仿学习面临大规模高质量机器人演示数据稀缺的挑战。
method: 利用大规模第一人称人类操作视频和3D手部姿态，训练扩散变压器将人类行为先验迁移到机器人。
result: 增强了双臂机器人操作策略的学习效果。
conclusion: 人类操作数据可有效弥补机器人数据不足，提升跨形态操作能力。
---

## Abstract
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present  H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. The modular design of action encoder and decoder components enables effective knowledge transfer from the unified human embodiment to diverse robot platforms through efficient fine-tuning. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including π0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义
- **核心问题**：机器人模仿学习长期受限于大规模、高质量演示数据的稀缺，而现有跨形态机器人数据集预训练又面临不同形态与动作空间难以统一建模的挑战。
- **研究动机**：大规模第一人称人类操作视频天然包含丰富的行为先验（物体可供性、操作策略、任务分解模式），若能高效迁移至机器人，有望从根本上缓解数据短缺问题，并减少跨形态冲突。
- **整体含义**：提出一种从人类数据到机器人策略的知识迁移框架，证明人类操作数据可以成为双臂机器人操作策略学习的强大基础，尤其适用于小样本和跨形态场景。

## 2. 方法论
- **核心思想**：采用两阶段训练→先在大规模人类操作数据上预训练，再在特定机器人数据上进行跨形态微调，通过模块化设计实现人类行为先验向多种机器人平台的迁移。
- **人类动作表示**：将人类双手动作编码为统一的48维向量（双手腕位姿18维 + 指尖位置30维），该表示可作为大多数末端执行器控制机器人动作空间的超集，从而弥合形态差异。
- **两阶段训练范式**  
  - 阶段1：在EgoDex全数据集上（338K+条轨迹、194种操作任务）使用48维手部姿态进行预训练。  
  - 阶段2：选择性权重迁移→保留视觉编码器、语言编码器、Transformer主干权重；重新初始化状态适配器、动作适配器、动作解码器，以适应目标机器人的具体动作空间。
- **扩散变压器架构**  
  - 总参数量约2B，采用基于LLaMA‑3风格的Transformer主干，融合RMSNorm、SwiGLU。  
  - 视觉编码器：DinoV2 + SigLIP；语言编码器：T5‑XXL；图片/语言特征通过交叉注意力注入。  
  - 流匹配（Flow Matching）替代传统扩散目标：构建直线流路径 \(a_\tau = \tau a^* + (1-\tau)z\)，网络学习向量场最小化损失 \(\mathcal{L}_{\mathrm{FM}} = \mathbb{E}\|v_\theta (a_\tau,\tau,c) - (z-a^*)\|^2\)，提升训练稳定性与推理效率。  
  - 推理时使用ODE求解器通过确定性步骤还原动作序列。

## 3. 实验设计
- **数据集与场景**  
  - 人类数据：EgoDex（829小时、338K段第一人称视频+3D手部姿态+语言描述）。  
  - 仿真基准：RoboTwin 2.0，包含Easy（干净桌面）和Hard（域随机化：光照、背景、物体杂乱、桌面高度）模式，涵盖13个单任务和45个多任务。  
  - 真实世界：三套平台—Aloha‑Agilex‑2.0（双Piper）执行毛巾折叠、杯子放杯垫；双ARX5执行113种取放任务（小样本：每任务1‑5次演示）；双UR5+UMI执行外卖袋放置（4个子任务）。
- **对比方法**  
  - RDT（机器人扩散变压器基线）、π0（SOTA视觉‑语言‑动作模型）、w/o human（相同架构但无人类预训练）。  
- **评估指标**：成功率（完整完成或分步骤评分）、跨形态表现、小样本效率、环境鲁棒性。

## 4. 资源与算力
- 论文**未明确说明**训练所使用的GPU型号、数量、批大小与具体耗时，仅指出模型参数规模为2B。在资源透明度上有欠缺。

## 5. 实验数量与充分性
- **实验组数概览**  
  - 仿真：单任务13项 ×2难度模式；多任务45项（报告代表性10项）；跨形态对比（Aloha‑Agilex‑1.0与Franka‑Panda）。  
  - 真实世界：Aloha‑Agilex‑2.0两个任务各25次试验；ARX5少样本113任务×1‑5演示；UR5+UMI四子任务各25次试验。  
  - 与从头训练、RDT、π0的全面对比，涵盖单/多任务、跨形态、少样本、域随机化等多个维度。  
- **充分性与公平性**：实验覆盖仿真到真实、多个机器人平台、不同数据规模，对比方法均是当前SOTA，评价指标客观，实验设计较为充分且公平。唯一可改进的是多任务报告仅选用10个代表任务，而非全部45项结果。

## 6. 主要结论与发现
- 大规模人类操作预训练能够为双臂机器人策略提供强有力的行为先验。  
- H‑RDT在所有实验设置下均显著优于从头训练及现有SOTA（RDT、π0），尤其在多任务（+20%绝对提升）和极低数据（1‑5次演示）场景下优势突出。  
- 模块化动作适配器设计使单一预训练模型可高效迁移到多种差异显著的机器人形态，验证了人类‑机器人知识迁移的有效性。

## 7. 优点
- **数据创新**：率先在大规模第一人称人类操作数据上进行机器人策略预训练，有效缓解机器人数据稀缺。  
- **结构设计**：统一的48维手部动作空间作为通用中间表示，配合模块化编/解码器实现灵活跨形态迁移。  
- **训练策略**：流匹配替代传统扩散损失，提升训练稳定性；两阶段训练避免联合优化中的形态冲突。  
- **实验充分**：涵盖多平台、多任务类型、少样本与域随机化，验证结论的可靠性与泛化性。

## 8. 不足与局限
- **算力与效率**：未披露训练资源消耗，2B参数模型的实际部署成本与延迟不明，可能制约真实场景应用。  
- **数据依赖**：预训练严重依赖带3D手部姿态标注的大规模人类视频，此类数据获取和标注成本较高。  
- **任务泛化边界**：真实世界实验主要为拾放、折叠等桌面操作，尚未验证在更复杂动态任务或非刚性精细操作上的效果。  
- **跨形态上限**：模块化微调虽有效，但可能并未消除所有形态差异；不同机器人平台仍需独立微调，极端形态或动作空间差异仍可能带来挑战。  
- **评估公平性**：多任务评估仅展示10项子集，未提供全部45项结果，可能存在选择性报告风险。

（完）
