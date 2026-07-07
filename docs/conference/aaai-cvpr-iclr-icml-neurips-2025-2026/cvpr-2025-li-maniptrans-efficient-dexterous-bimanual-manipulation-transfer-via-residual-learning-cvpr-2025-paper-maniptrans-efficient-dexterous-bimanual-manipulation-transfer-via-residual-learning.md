---
title: "ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning"
title_zh: ManipTrans：通过残差学习实现高效灵巧双手操作迁移
authors: "Li, Kailin, Li, Puhao, Liu, Tengyu, Li, Yuyang, Huang, Siyuan"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Li_ManipTrans_Efficient_Dexterous_Bimanual_Manipulation_Transfer_via_Residual_Learning_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 9.0
evidence: 将人类双手技能迁移到灵巧机械手
tldr: 针对人类双手技能向灵巧机器人手迁移的挑战，本文提出ManipTrans，一种两阶段方法：先预训练通用轨迹模仿器学习人手运动，再通过交互约束下的残差模块微调，实现高效且精确的双臂灵巧操作。实验表明，该方法在复杂双手任务上显著优于现有技术，为从人类演示中获取大规模机器人操作数据提供了可行途径。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1803, \"height\": 609, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1689, \"height\": 599, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1694, \"height\": 461, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 319, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 858, \"height\": 362, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 868, \"height\": 361, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 864, \"height\": 294, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 847, \"height\": 207, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-li-maniptrans-efficient-dexterous-bimanual-manipulation-transfer-via-residual-learning-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 847, \"height\": 113, \"label\": \"Table\"}]"
motivation: 数据驱动的具身AI需要大规模类人操作序列，但传统方法难以高效获取。
method: 两阶段方法：预训练轨迹模仿器捕捉人手运动，再通过残差学习适应机器人手形态与交互约束。
result: 在多种复杂双手任务上实现高效准确的技能迁移。
conclusion: ManipTrans为人类灵巧操作技能向机器人迁移提供了有效解决方案。
---

## Abstract
Human hands play a central role in interacting, motivating increasing research in dexterous robotic manipulation. Data-driven embodied AI algorithms demand precise, large-scale, human-like manipulation sequences, which are challenging to obtain with conventional reinforcement learning or real-world teleoperation. To address this, we introduce ManipTrans, a novel two-stage method for efficiently transferring human bimanual skills to dexterous robotic hands in simulation. ManipTrans first pre-trains a generalist trajectory imitator to mimic hand motion, then fine-tunes a specific residual module under interaction constraints, enabling efficient learning and accurate execution of complex bimanual tasks. Experiments show that ManipTrans surpasses state-of-the-art methods in success rate, fidelity, and efficiency. Leveraging ManipTrans, we transfer multiple hand-object datasets to robotic hands, creating DexManipNet, a large-scale dataset featuring previously unexplored tasks like pen capping and bottle unscrewing. DexManipNet comprises 3.3K episodes of robotic manipulation and is easily extensible, facilitating further policy training for dexterous hands and enabling real-world deployments.

---

## 论文详细总结（自动生成）

好的，以下是根据您提供的论文内容生成的结构化中文总结。

### 1. 论文的核心问题与整体含义
*   **研究动机**：具身人工智能对大规模、高精度、类人操作序列需求迫切。强化学习或遥操作等传统方法存在任务特化、成本高昂、数据规模受限等瓶颈。
*   **核心问题**：如何将人类单手/双手的灵巧操作技能（来自动捕数据）高效、高保真地迁移到形态各异的多指灵巧机械手上，并确保其在物理仿真中能完成复杂交互任务。
*   **整体含义**：提出一种名为 ManipTrans 的简单高效两阶段框架，通过将人手运动模仿与物体交互约束解耦，显著提升了技能迁移的成功率、精度和计算效率，并基于此构建了一个大规模灵巧手操作数据集 DexManipNet。

### 2. 论文提出的方法论
*   **核心思想**：将技能迁移分解为“人手轨迹模仿”和“任务交互微调”两个阶段。第一阶段学习模仿人手运动，解决形态差异；第二阶段通过残差学习在交互约束下精细调整动作，保证任务执行。
*   **关键技术细节**：
    *   **阶段一：手部轨迹模仿**。预训练一个通用策略，输入为人类手部参考轨迹（20个关键点）和机器人本体状态，输出为目标关节位置和腕部位姿力。奖励函数由手腕跟踪、手指模仿和动作平滑性组成。采用课程学习逐步收紧关键点偏差阈值。
    *   **阶段二：残差交互学习**。固定第一阶段策略，引入一个残差模块。状态空间扩展了物体姿态、BPS形状表征、手指-物体距离、接触力等信息。残差动作与粗动作逐元素相加形成最终指令。奖励函数增加了物体跟随和接触力奖励。训练中采用动态松弛机制（初期重力置零、高摩擦、宽松偏差阈值，后期逐步恢复正常）以避免局部最优。
*   **算法流程**：先在大规模手部数据上训练通用模仿器；然后在具体操控任务上，以模仿器为基础，微调零初始化高斯残差模块。

### 3. 实验设计
*   **数据集/场景**：
    *   **主要评估**：使用 OakInk-V2 官方验证集（约80个序列），包含近50%的双手任务。
    *   **定性展示**：还包括 GRAB、FAVOR、ARCTIC 等数据集。
    *   **建库**：在 FAVOR 和 OakInk-V2 上大规模迁移生成 DexManipNet 数据集（61个任务，3300个片段，134万帧）。
*   **Benchmark**：对迁移精度（物体旋转/平移误差、平均关节/指尖位置误差）和成功率进行定量评估。
*   **对比方法**：
    *   **RL组合式**：Retarget-Only（无学习）、RL-Only（从零训练PPO）、Retarget+Residual（基于硬对齐的残差学习）。
    *   **优化式**：QuasiSim（进行定性比较，因其代码和非公开验证集限制）。

### 4. 资源与算力
*   **硬件配置**：所有实验在一台个人电脑上完成，搭载一块 NVIDIA RTX 4090 GPU 和 Intel i9-13900KF CPU。
*   **训练设置**：使用 Isaac Gym 仿真器，并行运行 4096 个环境，时间步长 1/60 秒。训练算法为 PPO，批大小 1024，折扣因子 0.99。
*   **训练时耗**：文中举例一个未见过的单手操作序列（60帧），ManipTrans 仅需约 15 分钟训练即可达到鲁棒效果，而对比方法 QuasiSim 需约 40 小时。

### 5. 实验数量与充分性
*   **主要定量实验**：在 OakInk-V2 数据集上与3种基线方法进行了详细的指标对比（见 Table 1）。
*   **消融实验**：针对触觉信息（作为观测、奖励、终止条件）和训练策略（重力松弛、摩擦、阈值松弛）分别进行了消融，并给出了成功率训练曲线（Figure 7），论证了各模块的有效性。
*   **泛化性实验**：测试了在 Shadow Hand、MANO Hand、Inspire Hand、Allegro Hand 等4种不同自由度、形态的灵巧手上的表现。
*   **真实世界验证**：在真实双臂灵巧手上复现了轨迹，展示了 sim-to-real 的可行性。
*   **数据集基准测试**：在生成的 DexManipNet 数据集上，评估了 IBC、BET、扩散策略等4种模仿学习方法的性能。
*   **客观性与公平性**：对比方法包含了领域内代表性的基线（如从零RL、硬重定向+残差），且实验设置基于统一的公开数据集和仿真器，公平性较好。但 QuasiSim 因资源限制只进行了定性对比。

### 6. 论文的主要结论与发现
*   ManipTrans 在成功率、运动精度和计算效率上均超越了现有最优方法。
*   解耦人手运动模仿和物体交互的设计，有效降低了高维动作空间复杂度，缓解了形态差异和误差累积问题。
*   残差学习结合基于物理信息的状态扩展和动态松弛训练策略，使得模型能捕捉精细的接触和双手协调动作。
*   该方法具有跨多类灵巧手硬件的能力，并可直接构建大规模操作数据集（DexManipNet），为下游策略训练提供有力的数据支持。

### 7. 优点
*   **简洁高效的框架**：两阶段解耦思路清晰，避免任务特化奖励工程，计算资源需求低，训练速度快。
*   **高精度与高保真**：在双手复杂任务上显著提升了操控精度和物理合理性，能完成拧笔帽、开瓶盖等前辈方法难以处理的细粒度任务。
*   **强泛化性与可扩展性**：方法适用于多种灵巧手，模型可迁移，且基于该方法构建的数据集 DexManipNet 易于扩展，对社区具有潜在价值。
*   **实践闭环**：展示了从仿真生成数据到现实机器人复现的完整链路。

### 8. 不足与局限
*   **数据依赖**：迁移效果受限于动捕数据的质量，对噪声过大的交互姿态和不够精确的物体模型（尤其是铰接物体）处理能力有限。
*   **sim-to-real 差距**：现实部署时，由于执行器速度和自由度差异，需要进行额外的指尖对齐优化和关节角度拟合，并非端到端直接迁移。
*   **策略学习基准低**：尽管 DexManipNet 规模庞大，但在此上直接进行行为克隆等策略学习，成功率依然很低（最高仅18.44%），说明灵巧手操作策略学习本身仍有很大挑战。
*   **实验对比局限**：与重要的优化式基线 QuasiSim 仅做了定性对比，无法完全量化性能优势。

（完）
