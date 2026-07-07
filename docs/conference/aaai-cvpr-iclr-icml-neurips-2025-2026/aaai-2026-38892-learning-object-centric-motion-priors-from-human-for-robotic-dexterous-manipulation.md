---
title: Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation
title_zh: 从人类学习以物体为中心的运动先验用于机器人灵巧操作
authors: "Zhengdong Hong, Guofeng Zhang"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38892/42854"
tags: ["query:data"]
score: 9.0
evidence: 利用人-物交互数据集预测未来手-物状态，为灵巧操作强化学习提供奖励。
tldr: 为克服多指灵巧手操作的复杂动态问题，本文从大规模人-物交互数据中学习以物体为中心的运动先验，预测未来手-物状态作为通用奖励，减少对任务特定奖励工程的依赖。在仿真和真实世界的三种操作任务上全面超越现有方法，展现了利用人类交互数据提升泛化性的潜力。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38892/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1845, \"height\": 750, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38892/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1850, \"height\": 608, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38892/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1840, \"height\": 1050, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38892/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 859, \"height\": 547, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38892/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 828, \"height\": 630, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38892/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 485, \"height\": 334, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38892/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 865, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38892/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 868, \"height\": 224, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38892/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 850, \"height\": 303, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38892/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 852, \"height\": 302, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38892/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1609, \"height\": 301, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38892/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1613, \"height\": 300, \"label\": \"Table\"}]"
motivation: 多指灵巧手操作高维且动态复杂，现有方法依赖繁重的任务特定奖励设计。
method: 从HOI数据集全面预测未来手-物状态，将物体未来状态作为强化学习通用奖励。
result: 在仿真和真实世界三项操作任务中全面超过SOTA方法。
conclusion: 利用人类交互先验可以显著增强跨任务的灵巧操作泛化能力。
---

## Abstract
Manipulating diverse objects with multi-fingered dexterous hands is challenging due to the high dimensionality and complex dynamics. Human-Object Interaction (HOI) datasets provide rich knowledge about task information and embodied interactions. Instead of solely imitating the human demonstrations, our method learns to holistically predict future hand-object states by leveraging these datasets. The predicted future states of the object can serve as a general-purpose reward term for reinforcement learning, reducing reliance on task-specific reward engineering and enhancing generalization across tasks. We conduct extensive experiments on three manipulation tasks in simulation and the real world. Our approach outperforms existing SOTA methods in both success rate and generalizability on novel objects. Furthermore, we validate the cross-embodiment compatibility of our methods by successfully deploying the skills on different robot hands.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究动机**：多指灵巧手（如五指的机器人手）操作物体时，具有极高的自由度与复杂的接触动力学，传统方法（如基于模型的轨迹优化、强化学习）严重依赖任务特定的奖励工程设计，难以在不同任务间泛化。
- **核心思想**：人类在操作物体时会潜意识预测物体的未来状态，该隐式能力可被建模为“以物体为中心的运动先验”。作者提出从大规模人-物交互（Human-Object Interaction，HOI）数据集中学习这种先验，将其转化为强化学习的通用奖励信号，从而避免为每个新任务重新设计奖励，提升多任务泛化能力。

### 2. 方法论
论文提出两步走的层次化框架：

#### 2.1 学习人类手-物运动先验（HOI 运动预测器）
- **数据集**：使用包含三维手部姿态（MANO 参数）和物体6自由度位姿的 Dex-YCB、ARCTIC 数据集。
- **模型结构**：
  - 先用最远点采样（FPS）从物体网格提取100个三维点，经 PointNet 编码得到物体形状特征。
  - 采用6层 GPT-2 风格的 Transformer，以自回归方式预测未来手-物状态对。输入长度为n的历史手-物状态序列（n=10），并拼接物体形状特征，输出下一步的手-物状态。
  - 训练损失为手部位姿和物体位姿的加权L2损失（物体项权重 $\beta=2$ 高于手项 $\alpha=1$）。
- **机器人重定向**：预测的人类手部姿态通过优化方法（类似 AnyTeleop）转化为机器人手的关节构型，优化目标为指尖位置匹配，并加入平滑项与关节限位。

#### 2.2 轨迹引导的强化学习
- **MDP 建模**：状态包含机器人关节位置与物体6D位姿；动作是末端执行器增量位姿和手指关节增量。
- **奖励函数设计**：
  - **机器人跟随奖励** $R_f$：鼓励机器人手靠近参考轨迹的关节位置和末端执行器的位置/朝向。
  - **物体跟随奖励** $R_o$：核心创新，鼓励实际物体位姿逼近预测的未来物体位姿（使用平移差和四元数差的指数衰减形式），替代了传统提升（lifting）等任务特定奖励。
  - **接触奖励** $R_{contact}$：奖励拇指与至少另一手指接触物体，提高抓取探索。
  - **成功奖励** $R_{success}$：任务完成时的大额奖励；对有障碍物的任务，增加接触障碍物的高惩罚项。
- **训练与 sim-to-real**：使用 PPO 训练状态策略，包含物体初始位姿随机化；通过系统辨识（PID参数、力限等）和域随机化（摩擦、物体尺度、重量）实现零样本仿真到真实世界的迁移。

### 3. 实验设计
#### 3.1 任务场景
- **YCB 物体抓取**：抓取并提升物体超过10cm，测试了 DexYCB 数据集内的物体、非 DexYCB 物体以及新物体位姿。
- **铰接物体操作**：将铰接部分（如笔记本电脑屏幕）打开超过30度，测试了 ARCTIC 数据集物体和日常物体。
- **带障碍物的抓取**：在抓取路径上引入未知位姿的障碍物，要求手和臂全程避免碰撞。
- **跨具身测试**：更换不同型号的机器人手（PSYONIC Ability、XHand1、Inspire），验证方法对运动学差异的适应性。

#### 3.2 数据集与基准对比
- **自身预测器训练**：基于 Dex-YCB 和 ARCTIC 数据集。
- **对比方法**：ViviDex、AdaDexGrasp、ManipTrans、HOP（含 RL 微调）、以及去除了物体跟随和手指跟随奖励的 PPO 变体（PPO w/o following）等当前领先方法。
- **评估指标**：任务成功率，在仿真中每方法测试100次（多个随机场景），真实机器人实验每方法重复20次。

### 4. 资源与算力
- **仿真训练**：PPO 训练使用单张 NVIDIA RTX 4090 (24GB) 搭配 i7-14700K CPU，运行1024个并行环境，每秒约10000步，训练100万步至收敛。
- **运动预测器训练**：文中未详细说明所用算力（如 GPU 型号和训练时长），但为实现方案提供了可参考的硬件基线。

### 5. 实验数量与充分性
- **实验数目**：在仿真和真实机器人上分别进行了3类任务、多种物体类别（已见/未见、不同位姿）的实验，并包含消融研究（移除 $R_o$ 或 $R_{contact}$）以及跨具身测试（3种不同机器人手）。
- **充分性与客观性**：
  - 多个对比方法覆盖了近期顶会/顶刊的工作，对比维度全面。
  - 仿真和真机结果表格化呈现，种子数和重复次数明确定义，体现了统计可靠性。
  - 消融实验清晰展示了物体跟随奖励对样本效率和成功率的关键作用，增强了结论的可信度。
  - 对未见物体和未见初始位姿的泛化测试，反映了方法的实际适应能力。

### 6. 主要结论与发现
- 所提方法在**所有测试任务中均取得最高的平均成功率**，尤其在未见物体和变化位姿下优势明显，大幅超越了现有 SOTA。
- **物体跟随奖励**是保证学习效率和最终性能的关键，移除后成功率和训练稳定性显著下降。
- 学习的运动先验具有**跨具身通用性**，可轻松部署到不同结构的机器人手上。
- 整体框架成功实现了零样本 sim-to-real 迁移，证明基于人类数据的先验能有效指导灵巧操作。

### 7. 优点
- **奖励泛化**：用预测物体状态替代任务特定奖励，大幅降低新任务上的奖励工程负担，这是方法论的核心亮点。
- **层次化结构**：第一阶段的运动预测器独立于具体机器人，第二阶段利用通用奖励学习，架构清晰，复用性强。
- **跨具身验证**：在三种不同形态的灵巧手上成功复现，表明先验对运动学差异具有良好适应性。
- **真实世界验证**：在真实机器人上完成了抓取、铰接操作和避障任务，并给出了 honest 的成功率数值，实用性强。
- **对比实验扎实**：包含多个近期 SOTA 方法、消融和泛化测试，研究结论具有较高的说服力。

### 8. 不足与局限
- **任务类型相对有限**：目前仅验证了抓取、简单铰接压开和静态避障，尚未探索更复杂的连续操作或动态交互任务。
- **物体状态预测依赖物体跟踪**：预测器推理需要准确的物体姿态估计（基于模型跟踪），对缺乏精准三维模型的任意物体可能难以直接应用。
- **先验数据覆盖面**：使用的 HOI 数据集主要是固定桌面场景，其蕴含的交互多样性有限，可能影响在完全开放环境中的行为生成。
- **障碍物规避设计**：目前障碍物任务是靠强化学习惩罚项被动学习，轨迹本身不包含主动避障语义，仍需工程干预。
- **训练的物理随机化范围**：仅提及摩擦、尺度、重量和观测噪声，未涉及更复杂的物理参数（如物体形变、表面纹理差异），可能限制真实世界鲁棒性。
- **计算成本未完全透明**：仅给出 PPO 训练的具体配置，HOI 预测器的训练时间未披露，完整复现成本不易评估。

（完）
