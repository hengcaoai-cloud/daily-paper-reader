---
title: "Mask2IV: Interaction-Centric Video Generation via Mask Trajectories"
title_zh: Mask2IV：基于掩码轨迹的交互中心视频生成
authors: "Gen Li, Bo Zhao, Jianfei Yang, Laura Sevilla-Lara"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37533/41495"
tags: ["query:data"]
score: 7.0
evidence: 以交互为中心的视频生成框架，可生成多样化的人/机器人-物体交互视频用于机器人学习
tldr: Mask2IV 提出一种解耦的两阶段机器人交互视频生成框架，通过预测掩码轨迹并动画化来实现可控生成。该方法能够产生丰富多样的交互视频，为机器人学习和操作策略训练提供视觉先验。实验显示其在交互生成质量上优于现有方法，尤其是在复杂动态场景下，有望成为构建机器人演示数据的有效工具。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37533/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 877, \"height\": 594, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37533/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1746, \"height\": 548, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37533/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1717, \"height\": 774, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37533/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 880, \"height\": 579, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37533/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1844, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37533/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1638, \"height\": 1579, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37533/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1800, \"height\": 297, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37533/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 880, \"height\": 317, \"label\": \"Table\"}]"
motivation: 现有视频生成方法难以建模复杂交互，掩码标注获取困难。
method: 提出解耦流水线，先预测合理的物体运动掩码轨迹，再基于轨迹生成交互视频。
result: 在质量和多样性上优于基线，特别是复杂交互场景生成效果提升显著。
conclusion: Mask2IV为生成高质量交互演示视频提供了新思路，辅助机器人学习。
---

## Abstract
Generating interaction-centric videos, such as those depicting humans or robots interacting with objects, is crucial for embodied intelligence, as they provide rich and diverse visual priors for robot learning, manipulation policy training, and affordance reasoning. However, existing methods often struggle to model such complex and dynamic interactions. While recent studies show that masks can serve as effective control signals and enhance generation quality, obtaining dense and precise mask annotations remains a major challenge for real-world use. To overcome this limitation, we introduce Mask2IV, a novel framework specifically designed for interaction-centric video generation. It adopts a decoupled two-stage pipeline that first predicts plausible motion trajectories for both actor and object, then generates a video conditioned on these trajectories. This design eliminates the need for dense mask inputs from users while preserving the flexibility to manipulate the interaction process. Furthermore, Mask2IV supports versatile and intuitive control, allowing users to specify the target object of interaction and guide the motion trajectory through action descriptions or spatial position cues. To support systematic training and evaluation, we curate two benchmarks covering diverse action and object categories across both human-object interaction and robotic manipulation scenarios. Extensive experiments demonstrate that our method achieves superior visual realism and controllability compared to existing baselines.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究背景与动机**：生成人与物体（HOI）或机器人与物体交互的视频，对具身智能（如机器人模仿学习、操作策略训练、可供性推理）至关重要，可以为下游任务提供丰富的视觉先验。然而，现有视频生成模型在刻画复杂的动态交互时表现不足。
- **核心痛点**：近期研究试图用掩码（mask）作为控制信号来改善交互生成质量，但要求用户逐帧提供精确的掩码序列，既不现实也不易用；同时，仅靠手部（actor）掩码难以处理目标物体指定、精细接触区域建模以及摄像机运动等复杂情况。
- **整体含义**：论文提出任务——交互中心视频生成，并设计了一个无需用户提供密集掩码的两阶段框架 **Mask2IV**，以自动生成可控、逼真的人/机器人-物体交互视频。

### 2. 论文提出的方法论
- **核心思想**：将交互视频生成解耦为**交互轨迹生成**与**轨迹条件视频生成**两个阶段，降低直接建模复杂动态的难度，同时保留对交互过程的灵活操控。
- **关键技术细节**（以文字说明算法流程）：
  - **阶段一：交互轨迹生成**  
    1. 输入初始 RGB 图像 `I`、指定交互对象的掩码 `M`，以及条件信号（文本 `T` 或目标位置掩码 `P`）。  
    2. 用 VAE 编码器 `E` 将 `I` 和经过颜色编码的 `M` 转化为潜变量 `f_i`、`f_m`。若初始帧存在 actor，先用 GroundedSAM 为其分配不同颜色以区分角色。  
    3. 将 `f_i` 与 `f_m` 沿通道拼接，复制 N 次以对齐视频长度，再与噪声潜变量 `z` 拼接，送入冻结时间注意层的潜在视频扩散模型，最后通过 VAE 解码器生成 N 帧的交互掩码轨迹 `S`（含 actor 与物体）。  
    4. 提供两种条件生成变体：  
       - **TT-Gen（文本条件）**：用 CLIP 编码文本提示，通过交叉注意力注入模型。  
       - **PT-Gen（位置条件）**：将目标位置掩码 `P` 的潜变量填入最后一帧槽位，初始物体掩码填入第一帧，中间帧置零，迫使模型插值出从当前到目标位置的连续轨迹。
  - **阶段二：轨迹条件视频生成**  
    1. 使用阶段一生成（训练时用真值）的掩码轨迹 `S`，经 VAE 编码得到 `f_s`。  
    2. 将 `f_s`、噪声潜变量 `z`、以及被扩展为 N 帧的第一帧图像潜变量 `f_i` 拼接，输入另一个潜在视频扩散模型，生成最终视频 `V`。  
    3. 针对交互视频的特殊挑战，引入两个设计：  
       - **随机掩码扰动**：训练时有概率 `p=0.2` 对轨迹掩码进行随机膨胀或腐蚀（核大小随机选自 {3,5,7}），提升模型对掩码形状变化的鲁棒性。  
       - **接触加权损失**：基于手掩码 `m_h` 与物体掩码 `m_o`，通过膨胀操作定义接触区域 `m_c`。用权重矩阵 `w = (1-m_c) + λ·m_c`（λ=5）对扩散损失进行重加权，强化接触区域的生成精度。  
   最终训练目标为：  
   \[
   L = \mathbb{E}_{z, S, \epsilon, t}\left[\| w \odot (\epsilon - \epsilon_\theta(z, f_\psi(S), t))\|_2^2\right]
   \]

### 3. 实验设计
- **数据集与基准**：
  - **HOI4D**（人-物交互）：利用时间戳标注裁剪视频片段，用模板“a hand {动词} an {物体}”生成文本提示，并基于手-物位移计算运动分数，滤除后5%的低运动片段。用于文本条件轨迹生成（TT-Gen）。
  - **BridgeData V2**（机器人操作）：使用 GroundingDINO 进行目标检测，SAM2 进行视频分割，并通过多帧间物体的时序 mIoU 识别被操纵对象。用于位置条件轨迹生成（PT-Gen）。
  - 两个基准均包含逐帧分割标注，用于训练和评估。
- **评估指标**：
  - 生成质量：FVD（时空相似性），PSNR、SSIM、LPIPS（逐帧保真度）。
  - 文本-视频对齐：使用 EgoVLP（HOI4D）和 ViCLIP（BridgeData V2）计算 T2V-Sim 与 V2V-Sim。
- **对比方法**：
  - 无控制基线：预训练 DynamiCrafter、经数据集微调的 DynamiCrafter-ft。
  - 控制型基线：CosHand（原为图像生成，扩展至视频，用掩码潜变量拼接）、InterDyn（用相同的伪掩码轨迹替代真值）。
  - 所有控制型方法均使用 Mask2IV 第一阶段生成的相同伪掩码作为输入，保证比较公平。

### 4. 资源与算力
- **GPU 资源**：所有实验在 **2 块 80GB NVIDIA A100 GPU** 上完成。
- **训练详情**：图像尺寸统一为 320×512，每段视频 16 帧。使用 AdamW 优化器，学习率 1×10⁻⁵，批大小 8。推理时使用 DDIM 采样器（50 步）。**训练时长未在论文中明确提及**，无法给出具体时间。

### 5. 实验数量与充分性
- **定量实验**：
  - 在两个数据集上分别报告 6 项指标，与 4 个基线（含无控制和有控制方法）对比，构成 **2 × 6 × 4 组主要结果**（表1）。
  - 在 HOI4D 上以真值掩码轨迹开展 **消融研究**，对比 ControlNet 架构、加物体掩码、随机扰动、接触损失等组件，共 5 组实验（表2）。
- **定性实验**：
  - 与 CosHand、InterDyn 的可视化对比（图4）。
  - 展示 Mask2IV 对不同物体（图5）、不同文本提示和位置掩码（图6）的控制能力。
- **充分性与公平性评价**：
  - 实验覆盖两个不同领域（HOI、机器人），兼顾视觉质量与语义对齐，消融实验清晰验证了各模块贡献。
  - 控制型基线均采用与 Mask2IV 相同的伪掩码输入，保证了对比的客观性。数据集构建过程公开透明，剔除了低运动片段等干扰项。
  - 总体实验设计较为全面，能支撑论文主张。

### 6. 论文的主要结论与发现
- Mask2IV 在 HOI4D 和 BridgeData V2 两个基准上均取得了优于现有基线的视频生成质量（更低的 FVD/LPIPS，更高的 PSNR/SSIM 和语义相似度）。
- 两阶段解耦设计有效规避了直接生成复杂交互的困难，同时让用户可以通过指定物体掩码、文本动作描述或目标位置灵活控制生成结果。
- 联合建模 actor 与物体的掩码轨迹，比仅使用 actor 掩码（如 InterDyn）更能提升精细交互区域的生成效果，尤其在多物体和摄像机运动场景下优势明显。
- 引入的随机掩码扰动和接触加权损失对提升生成鲁棒性和交互区域精度有显著贡献。

### 7. 优点
- **实用性强**：无需用户提供密集掩码序列，自动生成交互轨迹，大幅降低了使用门槛。
- **控制灵活**：支持目标物体指定（通过掩码）、动作类型控制（文本）和物体最终位置控制（位置掩码）三种模态，满足不同下游需求。
- **设计合理**：两阶段解耦使模型分工明确，轨迹生成专注运动，视频生成专注外观，并且通过扰动与接触损失强化了交互建模的精细度。
- **基准贡献**：为 HOI 和机器人操作分别构建了带掩码标注的专用基准，可复现且有利于后续研究。
- **实验扎实**：对比基线丰富，消融实验细致，评估指标多维，展现了方法的优越性和各组件的有效性。

### 8. 不足与局限
- **分割依赖**：阶段二训练依赖真值掩码，而机器人基准的掩码由 GroundingDINO+SAM2 自动生成，伪真值可能引入噪声，影响模型学习的上限。
- **场景与视角限制**：基准数据主要来自 HOI4D（典型室内抓取）和 BridgeData V2（特定机器人环境），模型对户外、高动态、重度遮挡或全新视角的泛化能力未经验证。
- **2D 视频局限**：仅生成 2D 图像序列，未涉及 3D 结构或物理正确性，可能产生看似合理但物理上不正确的接触（如穿模），在机器人物理仿真中直接应用仍有距离。
- **计算与时间成本未知**：论文未报告训练时长，且推理需运行两阶段扩散模型，实时性可能较差，影响交互式应用。
- **可控粒度**：虽然支持多种条件，但文本控制仍属高层语义，难以精细约束抓取姿态、力度等低层级行为；位置条件也仅限于物体最终放置，未覆盖完整运动路径上的细粒度控制。
- **偏差风险**：HOI4D 中的文本模板较为单一，可能使模型过度拟合特定句式，在多变的自然语言指令下表现可能退化。

（完）
