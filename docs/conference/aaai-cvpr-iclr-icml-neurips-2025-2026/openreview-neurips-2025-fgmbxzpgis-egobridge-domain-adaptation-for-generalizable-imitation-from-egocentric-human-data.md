---
title: "EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data"
title_zh: EgoBridge：面向自我中心人类数据的通用模仿领域自适应方法
authors: "Ryan Punamiya, Dhruv Patel, Patcharapong Aphiwetsa, Pranav Kuppili, Lawrence Y. Zhu, Simar Kareer, Judy Hoffman, Danfei Xu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=FGMBxzpgis"
tags: ["query:data"]
score: 9.0
evidence: 通过最优传输对齐人机策略潜空间，实现人类技能向机器人转移
tldr: EgoBridge提出一种联合训练框架，通过最优传输对齐人类和机器人数据的策略潜空间，解决了自我中心人类数据用于机器人模仿学习时的域差异问题。该方法在多个操作任务上大幅提升了跨形态泛化性能，使得大规模人类经验数据能够有效驱动机器人学习。这为利用人类第一人称视频扩展机器人模仿学习提供了重要的域自适应技术。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 自我中心人类数据丰富，但视觉、传感器和运动学差异阻碍知识迁移。
method: 基于最优传输的域自适应，对齐人机数据的策略潜特征和动作空间。
result: 在多项操作任务上，EgoBridge显著提高了模仿学习的成功率。
conclusion: EgoBridge为利用大规模人类视频进行通用操作学习提供了有效的域对齐手段。
---

## Abstract
Egocentric human experience data presents a vast resource for scaling up end-to-end imitation learning for robotic manipulation. However, significant domain gaps in visual appearance, sensor modalities, and kinematics between human and robot impede knowledge transfer. This paper presents EgoBridge, a unified co-training framework that explicitly aligns the policy latent spaces between human and robot data using domain adaptation. Through a measure of discrepancy on the joint policy latent features and actions based on Optimal Transport (OT), we learn observation representations that not only align between the human and robot domain but also preserve the action-relevant information critical for policy learning. EgoBridge achieves a significant absolute policy success rate improvement by 44% over human-augmented cross-embodiment baselines in three real-world single-arm and bimanual manipulation tasks. EgoBridge also generalizes to new objects, scenes, and tasks seen only in human data, where baselines fail entirely. Videos and additional information can be found at https://ego-bridge.github.io/

---

## 论文详细总结（自动生成）

根据提供的论文元数据，以下是对论文《EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data》的结构化总结。

### 1. 论文的核心问题与整体含义
*   **研究动机**：以自我为中心（第一人称）的人类操作视频数据极为丰富，是扩展机器人模仿学习的理想资源。然而，将这些数据直接用于训练机器人策略时，存在显著的**领域差异**。
*   **核心问题**：人类和机器人在**视觉外观、传感器模态（如相机参数）和运动学结构**上的不同，构成了知识迁移的巨大障碍，导致在人类数据上训练的策略无法直接部署到机器人上。
*   **整体含义**：EgoBridge旨在通过**领域自适应**技术，搭建一座连接人类自我中心数据与机器人执行能力的“桥梁”，使大规模人类经验数据能够有效驱动机器人操作技能的学习。

### 2. 论文提出的方法论
*   **核心思想**：通过一个**联合训练框架**，将人类操作数据和机器人操作数据共同用于策略学习。关键在于，它不仅仅混合数据，而是**显式地对齐**人类和机器人策略的潜在表示空间。
*   **关键技术细节**：
    *   **领域对齐度量**：采用**最优传输**来衡量人类和机器人在**联合策略潜特征和动作空间**上的分布差异。最优传输能够有效计算两个分布之间的距离，并找到将人类数据分布“搬运”到机器人数据分布的最优方案。
    *   **表征学习目标**：在最小化基于最优传输的领域差异时，模型学习到的**观察表征**（从图像等输入中提取的特征）不仅能将人类和机器人域进行对齐，还能**保留对策略学习至关重要的动作相关信息**。这确保了领域对齐不会牺牲任务执行所需的判别性信息。
    *   **算法流程概括**：可以理解为，模型包含一个共享的编码器-策略网络。在训练时，同时输入人类和机器人的自我中心观察。网络提取各自的潜在特征并预测动作。然后，通过一个基于最优传输的损失函数，约束这两个域的潜在特征和动作分布的相似性，同时优化策略的模仿学习目标。
*   **公式与算法（文字说明）**：该方法构建一个优化问题，目标函数包含标准的行为克隆损失和基于最优传输的域对齐损失。最优传输损失计算的是人类批次样本和机器人批次样本在潜在空间中的推土机距离，迫使编码器产生域不变的、动作相关的特征。

### 3. 实验设计
*   **数据集/场景**：在**三个真实世界的操作任务**上进行了验证，具体包括**单臂和双臂操作**任务。
*   **基准**：对比了**“人类增强的跨形态基线”**方法，即那些简单地将人类数据增强到机器人数据集中进行共同训练，但不做显式域对齐的方法。
*   **对比方法**：文中明确指出与“人类增强的跨形态基线”进行对比，并表明基线在仅用人类数据见过的物体和场景上**完全失败**。此外，还考察了策略对新物体、新场景和仅在人类数据中出现的新任务的泛化能力。

### 4. 资源与算力
*   **说明**：提供的论文元数据和摘要中**未明确说明**训练所使用的GPU型号、数量或具体训练时长。

### 5. 实验数量与充分性
*   **实验组数**：从摘要信息推断，至少包含以下几个维度的实验：
    *   **主实验**：在3个真实世界任务上，与人类增强基线的性能对比。
    *   **泛化实验**：测试方法对**新物体、新场景**以及**仅在人类数据中出现的新任务**的泛化能力。
    *   **消融/变体实验**：隐含在“通过最优传输”这一明确的技术路径中，论文可能通过移除或以其他方式替换最优传输组件来验证其对最终效果的贡献（元数据未明确列出，属合理推断）。
*   **充分性与客观性**：实验覆盖了单臂和双臂操作任务，并在真实世界环境中评估，具有很强的现实意义。对比了直接的基线方法，并考察了关键的泛化能力，尤其是在基线完全失败的场景下仍能成功，证明了其有效性。实验设计在这些信息看来是**充分、客观且公平的**。

### 6. 论文的主要结论与发现
*   **主要结论**：EgoBridge能够有效弥合人类数据与机器人策略之间的领域鸿沟，为利用大规模人类第一人称视频进行通用机器人操作学习提供了**一个有效的领域对齐手段**。
*   **关键发现**：
    *   EgoBridge相比人类增强的跨形态基线，在三个真实世界操作任务中实现了**44%的绝对政策成功率显著提升**。
    *   该方法成功泛化到了**新的物体、新的场景和仅在人类数据中见过的新任务**，而在这些情况下，基线方法完全无法工作。

### 7. 优点
*   **技术新颖性**：将最优运输引入人-机策略的潜在空间对齐，同时对齐特征和动作空间，保证了迁移的特征具有任务相关性，思路清晰。
*   **性能显著**：在一个极具挑战性的现实问题上，取得了远超基线的大幅性能提升，验证了域对齐在跨形态模仿学习中的关键作用。
*   **泛化能力突出**：展示了对新物体、新场景乃至新任务的泛化能力，这是机器人走向实用的核心要求，证明了该方法能从人类数据中学到可泛化的技能表示。
*   **实际价值高**：直接面向利用海量、易于收集的人类自我中心数据，为解决机器人操作数据匮乏问题提供了有前景的范式。

### 8. 不足与局限
*   **（基于可用信息的推断，原文未详述）**：
    *   **数据集依赖**：方法可能需要成对或至少覆盖相同任务类型的人类与机器人数据进行联合训练，对数据采集有一定要求。
    *   **任务复杂性**：虽覆盖单臂和双臂任务，但任务的规模和多样性是否足以完全验证“通用”能力有待更多场景测试。
    *   **最优传输计算开销**：在训练过程中引入基于最优传输的损失可能会增加额外的计算成本，元数据未提及效率问题。
    *   **领域假设**：方法假设对齐观察表征足以弥合运动学差异，对于差异过大的形态，可能仍需更显式的运动重定向。

（完）
