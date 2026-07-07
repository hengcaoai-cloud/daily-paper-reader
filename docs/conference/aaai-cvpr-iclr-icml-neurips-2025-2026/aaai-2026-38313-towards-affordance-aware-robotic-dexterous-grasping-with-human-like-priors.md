---
title: Towards Affordance-Aware Robotic Dexterous Grasping with Human-like Priors
title_zh: 面向可供性感知的机器人灵巧抓取与类人先验
authors: "Haoyu Zhao, Linghao Zhuang, Xingyue Zhao, Cheng Zeng, Haoran Xu, Yuming Jiang, Jun Cen, Kexiang Wang, Jiayan Guo, Siteng Huang, Xin Li, Deli Zhao, Hua Zou"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38313/42275"
tags: ["query:data"]
score: 7.0
evidence: 在大规模人类手部运动数据上预训练以注入自然运动先验，再适配到机器人灵巧抓取
tldr: 提出AffordDex框架，第一阶段在人类手部运动数据上预训练轨迹模仿器以获得自然运动先验，第二阶段训练残差模块进行机器人灵巧抓取，同时考虑物体可供性。解决了传统抓取忽视人类姿态和可供性定位的问题。实验表明该方法能实现更符合人类先验和可供性的通用抓取策略。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38313/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 778, \"height\": 775, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38313/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1730, \"height\": 879, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38313/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 768, \"height\": 613, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38313/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1727, \"height\": 744, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38313/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 771, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38313/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 747, \"height\": 351, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38313/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 628, \"height\": 341, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38313/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 864, \"height\": 444, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38313/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 828, \"height\": 220, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38313/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1814, \"height\": 784, \"label\": \"Table\"}]"
motivation: 现有灵巧抓取方法侧重低级稳定性，忽略可供性定位和类人姿态。
method: 两阶段训练：在人类手部运动上预训练模仿器，再训练残差模块适配机器人抓取。
result: 实现了具备运动先验和可供性理解的通用抓取策略。
conclusion: 人类运动先验能有效提升机器人灵巧抓取的泛化能力。
---

## Abstract
A dexterous hand capable of generalizable grasping objects is fundamental for the development of general-purpose embodied AI. However, previous methods focus narrowly on low-level grasp stability metrics, neglecting affordance-aware positioning and human-like poses which are crucial for downstream manipulation.  To address these limitations, we propose AffordDex, a novel framework with two-stage training that learns a universal grasping policy with an inherent understanding of both motion priors and object affordances.  In the first stage, a trajectory imitator is pre-trained on a large corpus of human hand motions to instill a strong prior for natural movement. In the second stage, a residual module is trained to adapt these general human-like motions to specific object instances. This refinement is critically guided by two components: our Negative Affordance-aware Segmentation (NAA) module, which identifies functionally inappropriate contact regions, and a privileged teacher-student distillation process that ensures the final vision-based policy is highly successful. Extensive experiments demonstrate that AffordDex not only achieves universal dexterous grasping but also remains remarkably human-like in posture and functionally appropriate in contact location. As a result, AffordDex significantly outperforms state-of-the-art baselines across seen objects, unseen instances, and even entirely novel categories.

---

## 论文详细总结（自动生成）

好的，以下是根据提供的论文内容生成的结构化详细中文总结。

### 1. 论文的核心问题与整体含义

*   **核心问题**：现有的机器人灵巧抓取方法主要关注低层次的抓取稳定性指标（如能否成功抓取并抬起物体），而严重忽视了抓取姿态的**类人自然性**和**功能可供性**。这导致抓取动作虽能成功，但姿势别扭或接触了不恰当的区域（如抓住刀刃），不利于后续的、更复杂的操作任务。
*   **研究动机**：为了开发通用的具身人工智能，灵巧手需要不仅能稳定抓取，还要能像人一样自然地运动和避开功能性不适宜的区域。本文旨在解决现有方法在“抓取成功”与“抓取合理”之间的鸿沟。
*   **整体含义**：论文提出了一个名为**AffordDex**的框架，通过学习人类运动先验和物体负可供性，生成既成功、又类人且功能上正确的通用灵巧抓取策略。

### 2. 论文提出的方法论

AffordDex 的核心思想是通过一个两阶段训练范式，将运动自然性和功能正确性问题解耦并协同解决。

*   **第一阶段：人类手部轨迹模仿**
    *   **核心思想**：在一个大规模人类手部运动数据集上，通过强化学习预训练一个基础策略π_H，为机器人手注入强大的自然运动先验。
    *   **技术细节**：
        *   状态S_t^H由机器人状态、物体状态和物体点云组成。
        *   训练目标是让机器人手的指尖关键点跟踪人类手（MANO模型）的参考轨迹，并鼓励动作平滑。
        *   奖励函数由手指模仿奖励和平滑度奖励两部分组成。

*   **第二阶段：可供性感知的残差学习**
    *   **核心思想**：冻结预训练好的基础策略π_H，训练一个轻量级的残差模块，将通用的人类运动适配到特定物体上，同时遵守功能约束。
    *   **关键技术组件**：
        *   **负可供性感知分割模块**：这是该阶段的核心引导组件，旨在明确告知策略“哪里不能碰”。
            1.  **视觉语言模型引导**：利用GPT-4V等模型获取物体的负可供性文本描述（如“刀刃”）。
            2.  **从分割到分类**：为解决视觉语言模型空间定位能力差的问题，该模块先将SAM模型生成的精确候选掩码作为视觉提示，再让CLIP模型找出与负可供性文本描述相似度最高的掩码，从而实现精确分割。
            3.  **3D投影**：将选中的2D掩码投影到物体点云上，获得最终的负可供性区域点集N_t。
        *   **特权教师-学生蒸馏**：
            *   **教师策略**：先训练一个能够访问环境真实状态（如物体状态）的状态基教师策略π_T，它以基础策略的输出加上自身输出的残差作为最终动作，并受到负可供性奖励的约束。
            *   **学生策略**：使用DAgger算法，将仅依赖视觉输入（点云、负可供性点云）的学生策略π_S，蒸馏为性能逼近教师策略的视觉基策略。

### 3. 实验设计

*   **数据集与场景**：
    *   **UniDexGrasp 数据集**：包含133个类别的3165个物体实例。用于评估在可见物体、可见类别的未见物体、未见类别的物体上的泛化能力。场景是桌面上的单个物体，使用固定全景相机合成点云。
    *   **OakInk2 数据集**：用于预训练基础策略π_H，并评估向其他数据集的泛化能力。
*   **Benchmark 与评估指标**：
    *   **抓取成功率**：物体在200步内到达目标位置即视为成功。
    *   **类人度分数**：通过Gemini 2.5 Pro模型分析抓取执行视频，评估动作与人类的相似性。
    *   **可供性分数**：惩罚指尖接触负可供性区域，评估抓取位置的合理性。
*   **对比方法**：论文对比了多种最新方法，包括纯强化学习算法、模仿学习算法以及针对灵巧抓取的专用框架。
    *   **强化学习/模仿学习**：PPO, DAPG, ILAD, GSL。
    *   **灵巧抓取专用**：UniDexGrasp, UniDexGrasp++， DexGrasp Anything。

### 4. 资源与算力

*   **硬件配置**：论文明确提到实验在NVIDIA RTX 4090 GPU上进行，训练时并行模拟了4096个环境。
*   **训练时长**：未明确说明总训练时长。仅提及负可供性感知分割（NAA）模块的离线预计算过程，每个物体大约需要**160秒**。
*   **政策网络**：使用的策略和价值网络为多层感知机（MLP），在视觉基设置中额外使用了PointNet+Transformer网络。

### 5. 实验数量与充分性

*   **实验组数**：实验设计相对充分。
    *   **主要对比实验**：在UniDexGrasp数据集的三个泛化层级（可见物体、未见实例、未见类别）和OakInk2数据集上，于状态基和视觉基两种设置下，与5种以上的基线方法进行了全面对比。
    *   **消融实验**：针对框架的三个核心组件（人类手部轨迹模仿HTI、负可供性感知分割NAA、教师-学生蒸馏）进行了消融研究，验证每个模块的贡献。
    *   **扩展实验**：将提出的HTI和NAA模块应用于其他方法（UniDexGrasp++），证实了其通用性和即插即用的潜力。
    *   **定性分析**：通过可视化结果（图4-7），直观展示了抓取姿态、消融对比和NAA模块的分割效果。
*   **客观性与公平性**：实验在相同的模拟器（Isaac Gym）环境中进行，并遵循先前工作的评估协议，与最新的方法进行了公平比较，实验设计客观。

### 6. 论文的主要结论与发现

*   AffordDex框架在所有泛化测试中均取得了最高的抓取成功率，性能显著优于最先进的基线方法。
*   通过引入人类运动先验，生成的抓取姿态在**类人度分数**上获得了极大提升，姿态更加自然。
*   提出的负可供性感知分割模块能精确识别并引导策略避开不适宜接触的区域，使得**可供性分数**显著降低，抓取位置功能上更合理、更安全。
*   框架中的两个核心模块（HTI和NAA）具有良好的通用性，可以应用于其他强化学习抓取方法并带来性能提升。
*   教师-学生蒸馏机制对于将高性能的状态基策略成功迁移到视觉基策略至关重要。

### 7. 优点

*   **问题视角新颖**：首次将类人运动先验和物体负可供性明确结合，解决了灵巧抓取中“抓得好”和“抓得对”的协同问题。
*   **方法论创新**：
    *   提出的**负可供性感知分割**模块，巧妙地将VLM缺乏细粒度空间理解能力的问题，转化为成熟的“先分割，后分类”任务，简单有效。
    *   两阶段训练范式清晰地将模仿学习和任务强化学习的优势结合。
*   **实验全面扎实**：量化指标丰富（成功率、类人度、可供性），消融实验充分证明了各模块的有效性，跨数据集实验展现了强泛化性，可视化结果也提供了直观佐证。

### 8. 不足与局限

*   **应用限制**：NAA模块依赖于对3D网格进行程序化纹理渲染和在线VLM查询，虽然论文声称其是离线一次性过程（每物体约160秒），但对于实时处理全新的、非网格化物体或动态变化的物体仍存在挑战。
*   **实验覆盖**：实验仅在仿真环境（Isaac Gym）中验证，未在真实机器人上进行，缺乏Sim-to-Real迁移的评估。
*   **负可供性定义**：论文聚焦于“负可供性”（避免接触的区域），虽然简化了问题，但也一定程度上忽略了正向供性（如“可拧的瓶盖”、“可按的按钮”）的引导，这可能限制抓取为后续更精细的操作任务提供最优起始位姿的能力。
*   **数据集依赖**：基础策略的人类运动先验来源于特定数据集（OakInk2），其多样性和偏向性可能会影响最终策略的泛化表现。

（完）
