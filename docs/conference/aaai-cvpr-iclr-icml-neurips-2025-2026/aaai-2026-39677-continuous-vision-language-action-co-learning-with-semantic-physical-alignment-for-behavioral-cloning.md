---
title: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
title_zh: 连续视觉-语言-动作协同学习与语义-物理对齐用于行为克隆
authors: "Xiuxiu Qi, Yu Yang, Jiannong Cao, Luyao Bai, Chongshan Fan, Chengtai Cao, Hongpeng Wang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/39677/43638"
tags: ["query:data"]
score: 5.0
evidence: 通过语义-物理对齐解决从人类示教进行行为克隆时的复合误差。
tldr: 针对语言条件操作行为克隆中顺序动作决策的复合误差问题，本文提出CCoL框架，通过连续跨模态协同学习和语义-物理对齐来提升动作一致性。实验表明该方法有效缓解了执行中断，在多种操作任务上提升了成功率。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1724, \"height\": 739, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 860, \"height\": 461, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 864, \"height\": 383, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 592, \"height\": 312, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 591, \"height\": 173, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 844, \"height\": 365, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-39677/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 862, \"height\": 444, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 870, \"height\": 486, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 862, \"height\": 373, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 880, \"height\": 409, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-39677/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1779, \"height\": 499, \"label\": \"Table\"}]"
motivation: 行为克隆存在语义-物理失配导致动作不连续和错误累积的问题。
method: CCoL框架实现视觉、语言和动作的连续协同学习，并对齐语义与物理特性。
result: 在多项语言条件操作任务上显著降低错误，提升克隆性能。
conclusion: 连续协同学习与对齐机制能有效提升从人类示教中学习的鲁棒性。
---

## Abstract
Language-Conditioned Manipulation (LCM) facilitates human-robot interaction via Behavioral Cloning (BC), which learns control policies from human demonstrations and serves as a cornerstone of embodied AI. Overcoming compounding errors in sequential action decisions remains a central challenge to improving BC performance. Existing approaches mitigate compounding errors through data augmentation, expressive representation, or temporal abstraction. However, they suffer from physical discontinuities and semantic-physical misalignment, leading to inaccurate action cloning and intermittent execution. In this paper, we present Continuous vision-language-action Co-Learning with Semantic-Physical Alignment (CCoL), a novel BC framework that ensures temporally consistent execution and fine-grained semantic grounding. It generates robust and smooth action execution trajectories through continuous co-learning across vision, language, and proprioceptive inputs (i.e., robot internal states). Meanwhile, we anchor language semantics to visuomotor representations by a bidirectional cross-attention to learn contextual information for action generation, successfully overcoming the problem of semantic-physical misalignment. Extensive experiments show that CCoL achieves an average 8.0% relative improvement across three simulation suites, with up to 19.2% relative gain in human-demonstrated bimanual insertion tasks. Real-world tests on a 7-DoF robot further confirm CCoL’s generalization under unseen and noisy object states.

---

## 论文详细总结（自动生成）

好的，以下是基于您提供的论文内容生成的结构化中文总结。

### 1. 论文的核心问题与整体含义

-   **研究背景：**
    -   论文聚焦于**语言条件操作**，这是具身人工智能（Embodied AI）的关键领域，旨在让机器人根据人类自然语言指令执行复杂的物理操作。
    -   **行为克隆**是实现LCM的主流范式之一，它通过模仿人类专家示教数据来学习控制策略。

-   **核心问题：**
    -   行为克隆面临一个核心挑战——**复合误差**。即，单步动作预测的微小误差会在序列决策中不断累积，最终导致机器人状态偏离训练分布（协变量偏移），引发任务失败。
    -   现有缓解复合误差的方法（如数据增强、表达性表征、时序抽象）虽然有效，但引入了两个新问题：
        1.  **物理不连续性**：时序抽象等离散动作建模方法会破坏动作轨迹的平滑性，导致机器人运动抖动、不连贯。
        2.  **语义-物理失配**：高层的语言指令（如“把杯子放到架子上”）未能与底层的视觉运动表征在每个时间步精确对齐，导致机器人抓错目标或动作执行不准确。

-   **整体含义：**
    -   本文旨在提出一个全新的行为克隆框架，以解决上述**物理不连续**和**语义-物理失配**问题，从而实现更流畅、更精准的语言条件机器人操作。

### 2. 论文提出的方法论

-   **核心思想：**
    -   提出 **CCoL（连续视觉-语言-动作协同学习与语义-物理对齐）** 框架，包含两大核心机制：
        1.  **多模态连续协同学习（MCC）**：确保动作序列在时间上平滑一致。
        2.  **跨模态语义-物理对齐（CSA）**：实现细粒度的语言指令与视觉运动表征的逐步对齐。

-   **关键技术细节与算法流程：**
    1.  **上下文感知表征学习：**
        -   **视觉编码器**：使用ViT从RGB-D图像帧中提取空间特征。
        -   **文本编码器**：使用RoBERTa将语言指令编码为上下文嵌入。
        -   **本体感知编码器**：使用CVAE和Transformer/TCN处理机器人内部状态（如关节位置序列），得到本体感知嵌入。

    2.  **多模态连续协同学习 (MCC)：**
        -   从本体感知嵌入中初始化一个隐状态 `z0`。
        -   使用**神经常微分方程**来模拟隐状态在潜在空间中的连续演化过程，从而获得时间上一致的本体感知表征序列 `Zt`，替代了传统离散的逐步骤表征，解决了物理不连续问题。
        -   最后将视觉、语言和从NeuralODE得到的本体感知特征映射到一个共享嵌入空间。

    3.  **跨模态语义-物理对齐 (CSA)：**
        -   设计一个**双向交叉注意力机制**，将语言标记（如名词、动词）与共享空间中的联合视觉-本体感知表征进行逐时间步的精确对齐。
        -   通过注意力分数，模型可以动态地将“杯子”等名词锚定到图像中的相关区域，将“放”等动词与特定的运动轨迹模式关联起来。
        -   融合后的特征还加入了位置编码，以保证时间上的连贯性。

    4.  **上下文动作生成与优化：**
        -   将CSA融合后的特征通过一个目标条件解码器，预测未来 `k` 个时间步的动作序列。
        -   **混合损失函数**进行联合优化，包括：
            -   **行为克隆损失**：最小化预测动作与专家动作的差异。
            -   **不连续性惩罚**：通过约束隐状态变化率的平滑性，显式地强制动作轨迹的物理可行性。

### 3. 实验设计

-   **数据集/仿真环境：**
    1.  **Aloha MuJoCo**：进行双手协同操作任务（`Cube Transfer`， `Bimanual Insertion`），使用人类和脚本化示教数据。
    2.  **RLBench**：用于多场景评估，包含 `LampOn`， `GrillMeat`， `Phone`， `OpenBottle` 等任务。
    3.  **Franka Kitchen**：评估长时域任务性能，包括单任务和多个子任务组合的长序列任务。

-   **对比方法：**
    -   **时序建模基线**：BC-CNN， RT-1， BeT， VINN。
    -   **动作分块/航点抽象方法**：ACT， AWE。
    -   **扩散策略方法**：DP， DIC， HDP， 3DDiff。
    -   **表征增强策略**：R3M， Voltron， MPI。

-   **评估指标：**
    -   **成功率**：衡量任务是否在规定条件下（如特定位置、避碰）成功完成。

### 4. 资源与算力

-   **训练资源：** 论文在**真实世界实验**部分明确提到，模型在一块 **NVIDIA RTX 4090 GPU** 上训练，耗时 **5.3 小时**。
-   **推理速度：** 推理时，每生成一个动作序列耗时 **0.015s（±0.003s）**，对应约 **67Hz** 的策略频率，满足实时控制要求。对于仿真实验部分，未明确说明使用的GPU型号和数量。

### 5. 实验数量与充分性

-   **实验组数：实验设计较为充分和全面，涵盖了多个维度。**
    -   **主流基准测试**：在三个不同的、广泛使用的仿真基准（Aloha， RLBench， Franka Kitchen）上进行了评估。
    -   **多类别基线对比**：与至少14种代表不同技术路线（CNN, Transformer, 扩散模型等）的基线方法进行了比较。
    -   **消融研究**：系统地验证了核心组件MCC、CSA、不连续性惩罚项，以及注意力机制、编码器结构（TCN）的作用。
    -   **超参数分析**：研究了NeuralODE求解器步长对性能的影响。
    -   **定性分析**：通过注意力可视化展示了语义-物理对齐的效果，并对轨迹平滑度进行了定量分析（速度、加速度的标准差）。
    -   **真实世界验证**：在7-DoF机械臂上完成了3项操作的泛化测试，验证了仿真到现实的迁移能力。
-   **客观性与公平性：** 对比时，论文尽量保持与基线方法（如AWE, 3DDiff, MPI）相同的实验设置（如视觉主干网络、3D表征分辨率），保证了比较的公平性。

### 6. 论文的主要结论与发现

-   CCoL框架能有效缓解行为克隆中的复合误差问题。
-   提出的多模态连续协同学习显著提升了动作轨迹的平滑性，减少了高频抖动和加速度突变。
-   跨模态语义-物理对齐机制能成功地将语言语义动态地锚定到视觉和运动状态上，实现了细粒度的感知-动作一致性。
-   CCoL在多个仿真基准上取得了最优性能，尤其在需要时序连续性和语义理解的复杂任务（如双手协同、长时域操作）上优势明显，并在真实世界实验中展现了良好的泛化能力。

### 7. 优点

-   **问题建模新颖**：首次将物理连续性和语义-物理动态对齐这两个问题联合建模来解决行为克隆的复合误差。
-   **技术方法创新**：
    -   创新性地使用**NeuralODE**来建模本体感知状态在潜在空间的连续演化，保证了动作的物理平滑性。
    -   通过**双向交叉注意力**实现语言与视觉-运动特征的逐时间步精细对齐，优于传统的全局静态融合方法。
-   **实验论证扎实**：实验设计全面，包含多环境、多基线对比，并通过消融、可视化、量化分析和真实世界测试进行了充分论证，结论可信度高。
-   **兼顾实时性**：在保证高成功率的同时，实现了高效的推理速度，具备实际部署的潜力。

### 8. 不足与局限

-   **语言指令的泛化性**：论文主要关注任务描述性的指令，对于开放词汇、更抽象或需要复杂推理的语言指令的泛化能力还有待考证。
-   **任务场景有限**：虽然涵盖了多个仿真和真实任务，但整体仍属于结构化的桌面级操作任务，对于更复杂的环境交互（如移动操作、非刚性物体操作、动态避障）的适应性未作探讨。
-   **计算成本**：虽未在仿真实验中明确提及，但MCC中的NeuralODE求解器在长序列上可能会带来额外的计算开销和内存消耗，其在大规模、长时域任务中的训练效率可能面临挑战。
-   **依赖专家示教**：作为行为克隆方法，其性能上限仍受限于示教数据的质量和覆盖范围，对于未见过的新状态组合可能仍然会失败。

（完）
