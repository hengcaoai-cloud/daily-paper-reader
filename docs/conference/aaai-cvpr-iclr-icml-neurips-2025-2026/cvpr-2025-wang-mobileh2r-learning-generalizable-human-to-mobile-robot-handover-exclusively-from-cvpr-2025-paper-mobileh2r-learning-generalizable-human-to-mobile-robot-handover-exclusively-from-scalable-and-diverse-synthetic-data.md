---
title: "MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data"
title_zh: MobileH2R：完全基于可扩展多样化合成数据学习泛化的人-移动机器人交接
authors: "Wang, Zifan, Chen, Ziqing, Chen, Junyu, Wang, Jilong, Yang, Yuxin, Liu, Yunze, Liu, Xueyi, Wang, He, Yi, Li"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_MobileH2R_Learning_Generalizable_Human_to_Mobile_Robot_Handover_Exclusively_from_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 7.0
evidence: 可扩展的合成全身人体运动数据生成管线，用于机器人交接学习
tldr: MobileH2R 提出一种可扩展的合成数据生成管线，无需真实世界演示即可训练泛化的人-移动机器人交接策略，为构建可扩展操作数据集提供了途径。该方法通过生成多样化的全身人体运动数据，使机器人能够在仿真中学习稳健的交接技能。实验结果验证了合成数据训练的策略在真实世界中具有良好的泛化能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1724, \"height\": 426, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1726, \"height\": 972, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 742, \"height\": 561, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1255, \"height\": 220, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1258, \"height\": 223, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1258, \"height\": 208, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1257, \"height\": 207, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1766, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 882, \"height\": 267, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 894, \"height\": 270, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 838, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-mobileh2r-learning-generalizable-human-to-mobile-robot-handover-exclusively-from-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 872, \"height\": 145, \"label\": \"Table\"}]"
motivation: 传统人机交接数据收集成本高，缺乏可扩展的生成方法。
method: 提出可扩展合成数据生成管线，自动创建安全且适合模仿的演示，并结合4D模仿学习。
result: 在真实移动机器人上验证了多距离、多对象的泛化交接能力。
conclusion: 合成数据可有效替代真实演示，实现泛化的移动机器人交接训练。
---

## Abstract
This paper introduces MobileH2R, a framework for learning generalizable vision-based human-to-mobile-robot (H2MR) handover skills. Unlike traditional fixed-base handovers, this task requires a mobile robot to reliably receive objects in a large workspace enabled by its mobility. Our key insight is that generalizable handover skills can be developed in simulators using high-quality synthetic data, without the need for real-world demonstrations. To achieve this, we propose a scalable pipeline for generating diverse synthetic full-body human motion data, an automated method for creating safe and imitation-friendly demonstrations, and an efficient 4D imitation learning method for distilling large-scale demonstrations into closed-loop policies with base-arm coordination. Experimental evaluations in both simulators and the real world show significant improvements (at least +15% success rate) over baseline methods in all cases. Experiments also validate that large-scale and diverse synthetic data greatly enhances robot learning, highlighting our scalable framework.

---

## 论文详细总结（自动生成）

好的，以下是基于您提供的论文内容生成的结构化中文总结。

### 1. 论文的核心问题与整体含义

-   **核心问题**：如何使移动机器人具备泛化能力，能够在无固定底座的大范围空间内，安全可靠地从人类手中接过物体（即人-移动机器人交接，H2MR）。传统方法通常处理固定底座的机械臂交接，或依赖真实世界演示，存在可扩展性差、安全风险高和成本高昂等问题。
-   **整体含义/研究动机**：论文的核心洞察是，完全可以在模拟器中，通过高质量、大规模且多样化的合成数据来培养机器人的通用交接技能，从而避免对昂贵且有风险的真实世界数据收集的依赖。这为解决人机交互任务中的数据瓶颈问题提供了可扩展的解决方案。

### 2. 论文提出的方法论

论文提出了名为 **MobileH2R** 的框架，包含三个核心组件，形成一套完整的合成数据驱动学习范式：

-   **核心思想**：利用模拟器生成大规模、多样化、任务相关的合成数据（包括人类运动、物体和机器人演示），并通过模仿学习训练一个能协调移动底盘与机械臂的视觉运动策略。

-   **关键技术细节**：
    -   **MobileH2R-Sim (场景与运动合成)**:
        -   **两阶段全身运动合成**:
            1.  **预交接阶段**：利用在大规模数据集（如AMASS）上预训练的可控生成模型（Guided Motion Diffusion, GMD），结合大语言模型（LLM）根据物体语义生成的提示词，生成丰富多样的任务无关全身动作（如行走、坐下、跳舞）。
            2.  **交接阶段**：采用任务相关的局部合成方法，随机采样交接位置，并通过运动学优化器求解手臂姿态，最后插值生成平滑的手臂递物动作。
        -   **交互式设计**：虚拟人会对机器人距离做出反应（靠近时从预交接动作切换至交接动作），模拟真实世界交互。
    -   **安全且易于模仿的演示生成**:
        -   **安全保证**：使用基于优化的运动规划器（CHOMP）。引入**未来避障损失**，利用上帝视角信息预防未来时刻的碰撞；施加**终点姿态约束**，确保机器人在人类正面可见范围停止，避免不安全行为。
        -   **模仿友好性**：为增强视觉信号到机器人动作的可学习性，设计了**视觉神经损失**。其核心是训练一个姿态预测网络P（从视觉输入预测物体姿态）和一个视觉-状态恢复估计器E（根据状态估计P的预测误差）。E使得梯度可从视觉损失回传至状态，从而在轨迹优化时引导状态朝向使其视觉渲染图更利于对象姿态估计的方向，从而建立了清晰的“视觉→状态→动作”学习路径。
    -   **4D模仿学习策略**:
        -   **输入处理**：融合头部和腕部相机分割出的人体、手部、物体点云，并将其转换到机器人末端执行器坐标系。
        -   **4D信息**：通过ICP（迭代最近点）算法计算连续点云间的流信息，作为时间维度特征进行增强。
        -   **特征提取与动作输出**：使用改进的PointNet++，分别对人体（大采样半径）和手-物体（小采样半径）点云进行层次化特征提取，后拼接为全局特征。该特征被输入一个MLP（多层感知机），同时解码出**协调的9D动作**（机械臂的6D运动SE(3)和底盘的3D运动SE(2)），并由模仿学习损失L_base和L_arm，以及辅助的抓取姿态预测损失L_pred联合监督。

### 3. 实验设计

-   **数据集/场景**:
    -   **合成数据集**：
        -   `m0`（简单场景）：人类以直接方式走向机器人递交物体。
        -   `n0`（复杂场景）：人类执行复杂的全身动作（如跑动、下楼梯）进行交接。
        每个场景包含10万训练场景和1千测试场景，使用了来自ShapeNet的8836个多样化物体。
    -   **真实运动捕捉数据集**：基于DexYCB的`s0`数据集，包含1000个真实的人-物体交接片段，用于评估在真实人类运动上的泛化能力。

-   **Benchmark与对比方法**:
    -   **Grasp Selection + Trajectory Planning**：非端到端方法，先预测抓取姿态，再在线规划运动。
    -   **GenH2R**：用于固定底座交接的端到端SOTA方法，本研究对其进行扩展以适应移动机器人（通过逆运动学求解底盘动作）。对比了原始模型和在本研究数据集上重训练的版本（GenH2R(reprod.)）。
    -   **消融研究变体**：移除4D流信息、移除人体信息、解除臂-底盘协同动作解码（使用独立网络）。

### 4. 资源与算力

文中未明确提及训练该框架所使用的具体算力（GPU型号、数量及总训练时长）。只是在评估指标处提及了策略的推理时间（约0.003秒），并说明测试时的计算时间标准化在单张空闲的RTX 3090和32核CPU上进行。

### 5. 实验数量与充分性

-   **实验数量**: 论文进行了多组实验，覆盖了方法对比、数据规模与资产缩放、演示策略和策略设计消融，以及真实世界验证，实验较为丰富。
    -   **主要对比实验**: 3个测试集（m0, n0, s0）x 4种方法。
    -   **数据缩放实验**: 3个测试集 x 4种数据配置（不同演示数量和资产多样性）。
    -   **演示策略实验**: 3个测试集 x 5种演示生成策略。
    -   **策略消融实验**: 3个测试集 x 3种策略变体。
    -   **真实世界用户研究**: 2种场景难度 x 2种方法。
-   **充分性与公平性**: 实验设计是充分且公平的。它在一个统一框架下对比了不同范式（规划 vs 学习），通过重训练和统一测试基准确保了对比的公平性。消融研究系统性地验证了每个核心组件（4D信息、人体输入、协同动作）的贡献，结论具有说服力。

### 6. 论文的主要结论与发现

-   **端到端学习优于传统规划**：相比“抓取选择+轨迹规划”的基线方法，我们的端到端框架在所有场景下成功率平均提高了26.3%。
-   **合成数据的规模与多样性至关重要**：将演示数量从1k增加到100k或使用更复杂多样的人类运动数据（n0），能显著提升策略的泛化能力和成功率。
-   **安全且模仿友好的演示是关键**：引入未来避障和视觉神经损失等设计的演示，能显著降低碰撞率并提升策略模仿效果，手动设计的启发式损失（如强制相机朝向）反而不如基于学习的视觉损失有效。
-   **泛化到现实世界是可行的**：完全在合成数据上训练的策略，不依赖任何真实世界数据，成功实现了零样本Sim-to-Real迁移，在真实移动机器人上安全地完成了人与移动机器人交接任务。

### 7. 优点

-   **可扩展的纯合成数据范式**：提出了一套完整的、自动化的数据生成框架，能生成超过10万个交互场景，彻底摆脱对昂贵真实世界演示的依赖，是该领域的一大进步。
-   **创新性的演示优化**：“视觉神经损失”概念颇具新意，能自动化地优化轨迹使其更利于视觉策略学习，优于传统的手工启发式设计。
-   **全面的移动操控建模**：将人体全身信息纳入策略输入，并实现臂-底盘协同动作的端到端学习，更贴近真实的移动机器人应用要求。
-   **严谨且充分的实验验证**：在多种难度的模拟场景和真实世界进行了系统性评估，并通过详尽的消融实验验证了各模块的有效性。

### 8. 不足与局限

-   **物体交互的简化**：研究聚焦于“接”的动作，将交接过程简化为机器人靠近并抓取静态手持物。文中未涉及人类放手时机、力控或动态调整抓取等更复杂的物理交互细节。
-   **对感知系统的依赖**：Sim-to-Real实验中使用了高性能的分割模型（SAM2）来获取干净的点云输入，现实世界中的感知噪声和不完善分割对策略性能的影响未作深入探讨。
-   **实验场景的局限**：真实世界测试的物体和场景多样性相对模拟实验有限，且用户研究的人数未在文中明确，对不同人类行为习惯的覆盖可能不够全面。
-   **人类行为的交互性有限**：模拟器中的人类行为虽是交互式的（响应距离），但仍是基于预设逻辑（如靠近后触发交接动作），与真实、动态的人类意图理解和双向协同（如人类根据机器人行为调整自身动作）尚有差距。

（完）
