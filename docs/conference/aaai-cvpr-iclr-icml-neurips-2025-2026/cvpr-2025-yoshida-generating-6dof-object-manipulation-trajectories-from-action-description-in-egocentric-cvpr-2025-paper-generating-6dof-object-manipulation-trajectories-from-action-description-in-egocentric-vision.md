---
title: Generating 6DoF Object Manipulation Trajectories from Action Description in Egocentric Vision
title_zh: 从第一人称视觉的动作描述生成6DoF物体操作轨迹
authors: "Yoshida, Tomoya, Kurita, Shuhei, Nishimura, Taichi, Mori, Shinsuke"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Yoshida_Generating_6DoF_Object_Manipulation_Trajectories_from_Action_Description_in_Egocentric_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 9.0
evidence: 从大规模第一/第三人称视频数据集中提取6DoF操作轨迹，并根据文本动作描述生成机器人可执行轨迹
tldr: 该工作提出从Exo-Ego4D大规模视频中提取多样化操作轨迹，并训练模型根据动作描述生成6DoF物体操作轨迹，从而将人类视频演示转化为机器人可执行动作数据。首先解决获取大规模操作演示数据的挑战，然后利用提取的轨迹和文本描述训练生成模型。实验验证了该方法在生成准确轨迹上的有效性，为机器人从人类视频中学习提供了可扩展的数据转换途径。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1781, \"height\": 552, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1798, \"height\": 562, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 860, \"height\": 642, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1790, \"height\": 256, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1793, \"height\": 255, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1803, \"height\": 351, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 820, \"height\": 343, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 845, \"height\": 648, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 793, \"height\": 228, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 419, \"height\": 739, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 842, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1564, \"height\": 640, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 846, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 736, \"height\": 250, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yoshida-generating-6dof-object-manipulation-trajectories-from-action-description-in-egocentric-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 828, \"height\": 254, \"label\": \"Table\"}]"
motivation: 训练交互式机器人需要大量多样化的操作演示，但实际采集几乎不可行。
method: 利用Exo-Ego4D的大规模视频数据集提取操作轨迹，结合动作描述训练基于视觉和点云的轨迹生成模型。
result: 展示了从文本描述生成六自由度物体操作轨迹的有效性。
conclusion: 该框架为从大规模人类视频中获取机器人操作数据提供了可行方案。
---

## Abstract
Learning to use tools or objects in common scenes, particularly handling them in various ways as instructed, is a key challenge for developing interactive robots. Training models to generate such manipulation trajectories requires a large and diverse collection of detailed manipulation demonstrations for various objects, which is nearly unfeasible to gather at scale. In this paper, we propose a framework that leverages large-scale ego- and exo-centric video datasets --- constructed globally with substantial effort --- of Exo-Ego4D to extract diverse manipulation trajectories at scale. From these extracted trajectories with the associated textual action description, we develop trajectory generation models based on visual and point cloud-based language models. In the recently proposed egocentric vision-based in-a-quality trajectory dataset of HOT3D, we confirmed that our models successfully generate valid object trajectories, establishing a training dataset and baseline models for the novel task of generating 6DoF manipulation trajectories from action descriptions in egocentric vision.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：交互式机器人需要在各类日常场景中按指令操控多种工具或物体。训练这样的操控轨迹生成模型需要大规模、多样化的精细操控演示数据，但真实录制高精度的人类演示极其昂贵且难以规模化。
- **整体思路**：本文提出一种可扩展的框架，从已有的第一人称与第三人称视频数据集（Exo-Ego4D）中自动提取 6DoF 物体操作轨迹，并结合对应的文本动作描述，训练视觉和点云语言模型，实现从动作描述生成物体的 6DoF 操作轨迹。目标是将其作为从人类视频演示向机器人可执行动作转化的基础方案。

## 2. 论文提出的方法论

### 2.1 从视频中提取 6DoF 操作轨迹的数据构建框架

针对第一人称视频，在不需要预先标定相机外参的前提下，通过以下四步自动构建训练数据：

1. **时序动作定位**  
   - 基于 GPT-4o，输入视频帧索引和动作描述，确定动作的起始帧与结束帧，并提取被操作物体的名称，过滤掉非刚体物体。
2. **位置序列提取**  
   - 利用开放词汇分割模型（Grounded SAM）在第一帧获取物体分割掩码；  
   - 使用单目深度估计模型（Depth Anything）为每一帧估计深度图；  
   - 结合 SpaTracker（稠密 3D 点跟踪器）在 3D 空间中跟踪分割区域，得到物体的 3D 位置序列。
3. **轨迹投影**  
   - 将每帧 RGB-D 图转换为点云，通过 FPFH 特征匹配和 RANSAC 初始对齐，再用有色点云迭代最近点算法（ICP）配准相邻帧的相机外参；  
   - 将所有跟踪结果的坐标投影到起始帧的相机坐标系下，消除相机自身运动的影响。
4. **旋转序列提取**  
   - 对物体在初始时刻与各后续时刻的点云进行奇异值分解（SVD），得到旋转矩阵并转换为旋转向量，最终拼接位置与旋转序列，形成 6DoF 轨迹。

此框架被应用于 Exo-Ego4D，构建了包含 28,497 条轨迹及对应动作描述的 **EgoTraj** 数据集（是目前最大的此类数据集）。

### 2.2 文本引导的 6DoF 操作轨迹生成模型

- **任务定义**：给定动作描述和初始状态（视觉输入、物体初始位姿），生成物体连续时刻的 6DoF 位姿序列。
- **轨迹离散化**：将每个维度的连续值量化为 256 个 bin，一条轨迹被表示为 N×6 个离散 token（位置和旋转各三维）。
- **模型架构**：基于视觉语言模型（VLM）和点云语言模型，将任务视为 token 预测问题。  
  - 主干的 VLM 包括 BLIP-2、VILA，点云模型包括 PointLLM、MiniGPT-3D；  
  - 对 2D 模型扩展深度编码器，将深度特征与图像特征拼接输入 LLM；  
  - 语言解码器在预测时引入新的轨迹 token 词汇，使用交叉熵损失训练。
- **生成策略**：采用自回归方式逐步预测轨迹 token，可产生不同长度的轨迹；利用核采样进行多条轨迹的随机性生成。

## 3. 实验设计

### 3.1 数据集与基准

- **训练/验证集**：从 Exo-Ego4D 自动构建的 EgoTraj，包含 27,788 训练样本、709 验证样本（平均轨迹长度约 15 帧，由原始 33 帧截断或填充）。
- **测试集**：HOT3D 数据集中的 986 条轨迹（由精确红外相机捕捉的 6DoF Ground Truth，通过动作描述和深度估计对齐到任务设定）。
- **评测指标**：
  - 3D/2D 位置的平均位移误差（ADE）与最终位移误差（FDE）；  
  - 旋转的测地距离（GD）。

### 3.2 对比方法

- **Seq2Seq**：经典 Transformer + MLP 递归预测下一时刻位姿。
- **USST**：先进 3D 手部轨迹预测模型，可选预训练和微调，仅预测位置，不使用动作描述。
- **多种 VLM 和点云模型**：BLIP-2 (2.7B/6.7B)、VILA (3B/8B)、PointLLM (7B)、MiniGPT-3D (2.7B)，部分加入深度输入。
- 除单独测试外，还进行了数据规模缩减实验（1.0, 0.5, 0.1, 0.05, 0.01 比例）、概率采样数量影响、动作描述生成等实验。

## 4. 资源与算力

- 论文没有明确提及 **GPU 型号、数量、训练时长等硬件或计算资源信息**。所有资源描述均为缺失状态。

## 5. 实验数量与充分性

- **多模型多模态对比**：涵盖 2D 图像、图像+深度、点云三种输入模态，至少对比了 6 种不同模型/变体，结果汇总于主要表格中。
- **粒度实验**：包括 3DoF 与 6DoF 轨迹对比；位置与旋转指标分别报告。
- **数据规模研究**：通过逐步缩小子集验证模型性能随数据量增加而提升。
- **随机性实验**：PointLLM 采用不同样本数 (1, 3, 10) 的核采样，观察指标改善。
- **消融或附加任务**：利用轨迹增强的图像与 3D 描述生成，证明动词相似度提升约 10%。
- **定性结果**：展示了不同动词下轨迹变化的合理性。
- **评价：** 实验覆盖较全面，从模型选择、输入模态、数据规模到生成策略，均进行了对比或分析，对提出的任务与数据集做了多维度验证，设计客观、公平。

## 6. 论文的主要结论与发现

- 基于 VLMs 和点云语言模型的方法可以从动作描述生成有效的 6DoF 物体操作轨迹，性能显著优于传统 Seq2Seq 基线。
- 点云输入和深度信息的引入对提升位置精度至关重要；模型规模并非唯一决定因素，不同 LLM 的特性同样重要。
- 即使使用自动提取的、质量不及精密采集的数据集，模型也能学习到有意义的操作轨迹，且增大数据量能持续提升性能。
- 通过核采样可生成符合相同描述的不同轨迹，反映动作描述执行方式的多样性。
- 轨迹信息能显著提升视觉描述中动词相似度，说明提取的轨迹捕捉到了真实的运动模式。
- 总体而言，本文提出的框架为大规模获取机器人操作轨迹、并从文本描述生成操作动作提供了可行且可扩展的路径。

## 7. 优点

- **首创性**：首次从普通第一人称视频（无需相机外参）中大规模提取 6DoF 操作轨迹，并基于此建立文本到 6DoF 轨迹生成的基准。
- **数据可扩展性**：自动提取流程充分利用现有大型视频数据集（Ego-Exo4D），避免了昂贵的数据采集，生成的数据集在动作动词和物体类别上远超此前依赖实验室标注的数据集。
- **方法灵活性**：模型兼容多种 VLMs 和点云模型，且生成的轨迹长度可变，支持多重采样，具有一定的不确定性表达。
- **实验全面性**：从模态对比、数据规模、生成多样性，到轨迹对 caption 的辅助作用，多角度验证了方法的有效性和潜力。

## 8. 不足与局限

- **仅适用于刚体**：框架以 6DoF 边界框表示物体姿态，无法处理衣物等可变形物体的操作。
- **提取误差累积**：管道中的物体分割错误（相似物体干扰）和点云配准失败（相机运动突变）会降低部分轨迹质量。
- **旋转生成精度偏低**：与位置指标相比，旋转的测地距离改善较小，说明准确生成旋转运动仍是难点。
- **实验覆盖局限**：测试集 HOT3D 规模有限，模型泛化到更多样化的“野外”操作场景尚待验证；缺乏与预训练数据集的深度交叉比较。
- **算力信息缺失**：未提供模型训练所需的计算资源，不利于复现和估算成本。

（完）
