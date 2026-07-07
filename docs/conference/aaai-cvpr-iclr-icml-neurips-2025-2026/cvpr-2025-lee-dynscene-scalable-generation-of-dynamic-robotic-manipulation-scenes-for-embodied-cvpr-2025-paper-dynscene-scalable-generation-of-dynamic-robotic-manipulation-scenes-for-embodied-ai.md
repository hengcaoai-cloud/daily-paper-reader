---
title: "DynScene: Scalable Generation of Dynamic Robotic Manipulation Scenes for Embodied AI"
title_zh: DynScene：面向具身AI的可扩展动态机器人操作场景生成
authors: "Lee, Sangmin, Park, Sungyong, Kim, Heewon"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.pdf"
tags: ["query:data"]
score: 8.0
evidence: 基于扩散的可扩展动态机器人操作场景生成框架
tldr: DynScene 是一个基于扩散的框架，从文本指令生成可扩展、多样化的机器人操作场景，满足具身AI对大规模高质量数据集的需求。该框架将生成分解为静态场景合成和动作轨迹生成两个阶段，增强了真实感和物理可行性。实验证明其场景多样性优于现有方法，能有效支持操作策略训练。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1778, \"height\": 644, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1793, \"height\": 845, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1812, \"height\": 589, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1806, \"height\": 859, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1786, \"height\": 805, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 869, \"height\": 392, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 799, \"height\": 471, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 855, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1804, \"height\": 386, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 876, \"height\": 224, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lee-dynscene-scalable-generation-of-dynamic-robotic-manipulation-scenes-for-embodied-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 872, \"height\": 162, \"label\": \"Table\"}]"
motivation: 现有机器人操作数据收集流程缓慢、昂贵且依赖人工。
method: 提出扩散框架，分解生成静态场景和动作轨迹，实现纹理指令驱动的多样化场景生成。
result: 生成场景在真实感、物理可行性和多样性上超越基线方法。
conclusion: DynScene为具身AI提供了高效可扩展的数据生成新范式。
---

## Abstract
Robotic manipulation in embodied AI critically depends on large-scale, high-quality datasets that reflect realistic object interactions and physical dynamics. However, existing data collection pipelines are often slow, expensive, and heavily reliant on manual efforts. We present DynScene, a diffusion-based framework for generating dynamic robotic manipulation scenes directly from textual instructions. Unlike prior methods that focus solely on static environments or isolated robot actions, DynScene decomposes the generation into two phases static scene synthesis and action trajectory generation allowing fine-grained control and diversity. Our model enhances realism and physical feasibility through scene refinement (layout sampling, quaternion quantization) and leverages residual action representation to enable action augmentation, generating multiple diverse trajectories from a single static configuration. Experiments show DynScene achieves 26.8x faster generation, 1.84x higher accuracy, and 28% greater action diversity than human-crafted data. Furthermore, agents trained with DynScene exhibit up to 19.4% higher success rates across complex manipulation tasks. Our approach paves the way for scalable, automated dataset generation in robot learning.

---

## 论文详细总结（自动生成）

## DynScene 论文总结

### 1. 论文的核心问题与整体含义
- **核心问题**：具身AI中的机器人操作严重依赖大规模、高质量的数据集，但传统数据采集（如人工遥控示教）速度慢、成本高且依赖大量人工。现有自动生成方法要么仅合成静态场景，要么仅生成孤立动作，缺乏对物理交互、环境约束和连续状态的整体考虑，导致场景与动作不匹配、任务不可行。
- **整体含义**：提出一个基于扩散模型的**动态场景生成框架DynScene**，首次将静态场景布局与机器人动作轨迹**联合生成**，从自然语言指令出发直接得到可执行、多样且物理合理的操作数据，大幅提升数据生成效率和代理训练效果。

### 2. 论文提出的方法论
#### 核心思想
  将动态场景生成解耦为两阶段：
  1. **静态场景合成**：生成物体位姿、机器人基座、末端执行器初始状态及房间布局等。
  2. **动作轨迹生成**：基于已生成的静态场景，生成一系列末端执行器的**残差位移**（位置、四元数变化和夹爪状态），实现动作与场景的物理一致。

#### 关键技术细节
- **数据表示**
  - 静态场景 `s` = [物体属性 `o`（位置、方向、类别、尺寸、形状码、初始/目标状态），机器人属性 `r`（基座位姿、末端初始位姿、夹爪状态），房间布局 `z`]。
  - 动作 `a` = K个步骤的残差序列：`a_k = [Δp_ee_k, Δq_ee_k, g_k]`，其中 `Δp_ee_k = p_ee_k - p_ee_{k-1}`，`Δq_ee_k = q_ee_k - q_ee_{k-1}`。
- **静态场景生成与精炼**
  - **条件扩散模型**：以文本指令为条件，通过U‑Net去噪生成不含房间布局的初始物体和机器人参数。
  - **布局采样**：从数据集中选择房间布局，使得生成的物体与机器人基座位置与已有布局中的位置最接近，避免机器人与墙壁、物体碰撞或不可达。
  - **四元数量化**：将扩散预测的物体方向以固定间隔δ量化，防止因微小方向误差导致重力作用下关节物体（如柜门）坍塌、初始状态改变。
- **动作生成与增强**
  - **条件扩散**：以静态场景数据为条件，用另一个扩散模型生成残差动作序列。
  - **残差学习**：动作表示为相对上一步的差值，使其独立于绝对起始位姿，可迁移到不同静态场景。
  - **动作增强**：对同一个静态场景可生成多条不同动作轨迹；还可利用不同目标状态的静态场景训练，使模型生成原本未出现的状态（如训练过10 cm、20 cm拾取，可生成30 cm动作），实现多样化数据增强。
- **物理验证**：所有生成的动态场景在Isaac Sim中执行，仅保留达到任务成功阈值的场景用于后续代理训练，过滤无效数据。

#### 训练目标（文字说明）
  采用常规扩散去噪得分匹配损失：
  - 静态场景：最小化 `‖ϵ - ϵ_θ(s_t, t; y)‖²`，其中 `s_t` 为加噪场景，`y` 为文本指令。
  - 动作生成：最小化 `‖ϵ - ϵ_φ(a_t, t; s)‖²`，`a_t` 为加噪动作，`s` 为完整静态场景。

### 3. 实验设计
- **数据集**：**ARNOLD** 基准，包含8个语言引导的连续状态操作任务（如“关上抽屉50%”、“倒掉一半水”），提供3571个训练样本和773个测试样本，涵盖未见过的物体、场景和状态以评估泛化。
- **对比方法**
  - 动作多样性：与ARNOLD人工采集数据比较（FD、DTW、SC指标）。
  - 生成效率与成功率：与ARNOLD人工耗时、DiffuScene静态场景生成（配合ARNOLD动作数据）对比。
  - 代理训练：训练**PerAct**和提出的**PerAct-PSA**（分阶段训练抓取与操作），对比仅使用ARNOLD数据与混合DynScene生成数据的成功率，还包括BC‑Lang‑CNN/ViT等基线。
- **评估指标**
  - 生成质量：成功通过物理验证的比例（SR）、生成耗时。
  - 动作多样性：Fréchet Distance (FD)、Dynamic Time Warping (DTW)、Spatial Coverage (SC)。
  - 任务成功率：代理在测试集上的平均成功率。

### 4. 资源与算力
- **训练硬件**
  - DynScene模型训练：单卡 **NVIDIA RTX 4090**。
  - 代理训练：单卡 **NVIDIA A6000**。
- **训练配置**
  - 静态/动作扩散模型：每任务训练 **100,000 epochs**，优化器 Adam，学习率 **2e‑4**。
  - 代理训练：**200,000 training steps**，batch size **4**，学习率 **1e‑4**，优化器 LAMB。
- **推理效率**：生成单个动态场景平均 **2.52秒**（相较于人工平均67.5秒）。
- 论文未提供总训练时间（如小时数），仅给出了epoch/step数。

### 5. 实验数量与充分性
- 论文进行了多组实验，涵盖：
  - 8个任务的无条件动态场景生成（各100个场景）评估（表2、表3）。
  - 与DiffuScene静态场景生成的对比（表4）。
  - 动作多样性分布的可视化分析（图4，及附录所有任务图）。
  - 8个任务的文本条件生成成功率及定性样例（表6、图5）。
  - 三组代理架构（BC‑Lang‑CNN/ViT, PerAct, PerAct‑PSA）在ARNOLD原始数据与混合DynScene数据下的成功率对比（表5）。
  - 泛化能力评估：对未见物体、场景、状态及中间状态的测试（表7）。
- **充分性与公平性**：实验设计较为全面，从生成本身的质量、多样性、效率，到下游任务训练的增益，均进行了验证。对比基线包括人类数据、静态生成方法及多种代理，公平可信。但缺乏对布局采样、四元数量化、残差学习等模块的独立消融实验，只是通过整体性能间接体现其贡献。

### 6. 论文的主要结论与发现
- DynScene生成动态场景的速度**比人工快26.8倍**（2.52秒 vs 67.5秒），成功率**高1.84倍**（69.5% vs 37.5%）。
- 动作多样性相比人工数据平均提升28%（FD、DTW、SC均更优），且能保持任务特定约束（如倒水的垂直精度）。
- 使用DynScene数据训练代理，**最高使PerAct成功率提升19.4%**，PerAct‑PSA提升10.03%，尤其在连续状态和精细控制任务上效果显著。
- 在未见物体和场景上泛化能力有所提升，但对极端未见状态泛化仍受限（视为分布外）。

### 7. 优点
- **首度联合生成静态场景与动作**，填补了动态场景生成空白，数据物理一致性高。
- **两阶段扩散结合残差动作表示**，实现了动作与场景的解耦复用，支持灵活的数据增强。
- **精心设计的物理精炼策略**：布局采样解决可达性问题，四元数量化防止物体初始状态漂移。
- **模拟器闭环验证**，确保仅用成功样本训练代理，避免噪声标签污染。
- 显著的数据效率提升和下游任务增益，展现了走向自动化、可扩展数据管线的潜力。

### 8. 不足与局限
- **数据集单一**：仅在ARNOLD基准上评估，未在其他仿真器或任务集（如RLBench, ManiSkill）上验证方法的泛化能力。
- **极端状态泛化不足**：对完全未见的、超出训练分布的状态（如从未见过的打开程度）性能不佳。
- **复杂场景探索有限**：任务环境较为结构化，未涉及更繁琐的长序列、多物体交互或动态障碍物。
- **消融实验缺失**：未对布局采样、四元数量化、残差表示等核心模块进行逐一拆除对比，无法量化各部分的独立贡献。
- **真实世界迁移未讨论**：仅使用仿真环境，尚未探讨生成的数据对真实机器人操作的 sim‑to‑real 迁移效果。

（完）
