---
title: Learning Diverse Bimanual Dexterous Manipulation Skills from Human Demonstrations
title_zh: 从人类演示中学习多样化的双手灵巧操作技能
authors: "Bohan Zhou, Haoqi Yuan, Yuhui Fu, Zongqing Lu"
date: 2026-03-17
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/40127/44088"
tags: ["query:data"]
score: 8.0
evidence: 从大量人类演示中学习双手灵巧技能
tldr: 针对双手灵巧操作技能学习面临的高维动作空间和任务多样性挑战，BiDexHD框架统一利用现有双手数据集进行任务构建，并采用教师-学生策略从大量人类演示中高效学习多样化技能。实验表明该方法能学习多种双手操作任务，为机器人从人类示教中学习操作技能提供了可扩展的解决方案。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40127/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1807, \"height\": 564, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40127/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1810, \"height\": 542, \"label\": \"Figure\"}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-40127/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 841, \"height\": 329, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40127/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 876, \"height\": 450, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40127/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1691, \"height\": 522, \"label\": \"Table\"}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-40127/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 828, \"height\": 371, \"label\": \"Table\"}]"
motivation: 解决双手灵巧操作技能学习中任务多样性不足和策略学习效率低的问题。
method: 提出BiDexHD框架，统一任务构建并采用教师-学生学习策略，利用人类演示训练双手操作技能。
result: 该方法能高效学习多种双手操作任务，超越传统强化学习方法。
conclusion: 为从人类示范中学习机器人双手技能提供了新框架，有助于开发通用操作能力。
---

## Abstract
Bimanual dexterous manipulation is a critical yet underexplored area in robotics. Its high-dimensional action space and inherent task complexity present significant challenges for policy learning, and the limited task diversity in existing benchmarks hinders general-purpose skill development. Existing approaches largely depend on reinforcement learning, often constrained by intricately designed reward functions tailored to a narrow set of tasks. In this work, we present a novel approach for efficiently learning diverse bimanual dexterous skills from abundant human demonstrations. Specifically, we introduce BiDexHD, a framework that unifies task construction from existing bimanual datasets and employs teacher-student policy learning to address all tasks. The teacher learns state-based policies using a general two-stage reward function across tasks with shared behaviors, while the student distills the learned multi-task policies into a vision-based policy. With BiDexHD, scalable learning of numerous bimanual dexterous skills from auto-constructed tasks becomes feasible, offering promising advances toward universal bimanual dexterous manipulation. Experiments on TACO tool-using dataset spanning 141 tasks across 6 categories demonstrate a task fulfillment rate of 74.59% on trained tasks and 51.07% on unseen tasks. We further transfer BiDexHD to 11 ARCTIC collaborative tasks and achieve an average of 80.49% task fulfillment rate on trained tasks and 65.99% on unseen task. All empirical results demonstrate the effectiveness and competitive zero-shot generalization capabilities of BiDexHD.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：双手灵巧操作（bimanual dexterous manipulation）虽然对机器人至关重要，但其动作空间维度极高、任务复杂度大，现有方法（尤其是强化学习）依赖为每个具体任务精心设计的奖励函数，导致策略缺乏可扩展性和通用性。同时，已有任务集的多样性有限，难以支撑通用技能的开发。
- **整体含义**：提出一种从人类演示中高效学习多样化双手灵巧技能的通用框架，通过自动将现有双手数据集构建为仿真任务，并利用一种通用的两阶段奖励函数驱动教师-学生策略学习，从而突破传统强化学习在双手灵巧任务中的可扩展性瓶颈。

### 2. 方法论
- **核心思想**：利用海量人类演示（如TACO、ARCTIC数据集），在仿真中自动构造任务，并通过教师-学生框架学习视觉策略，避免为每个任务手动设计奖励。
- **关键技术细节**：
  - **三阶段框架 BiDexHD**：
    1. **任务构造**：从人类双手操作数据集中提取手部-物体姿态序列，在Isaac Gym中初始化仿真任务，包括工具、物体的网格，以及双臂灵巧手。利用AnyTeleop优化手指关节，IK求解手臂关节，形成去中心化部分可观测马尔可夫决策过程（Dec‑POMDP）任务。
    2. **教师学习（状态策略）**：采用独立PPO（IPPO）训练多任务状态基策略。设计通用的两阶段奖励函数：
       - **阶段1：仿真对齐**。鼓励手部接近功能性抓取中心（由人类演示锚点计算得出），并将物体提升到参考位姿，奖励包含接近奖励、提升奖励和成功奖金。
       - **阶段2：轨迹跟踪**。使用指数奖励鼓励物体精确跟随人类演示轨迹。
    3. **学生蒸馏（视觉策略）**：通过DAgger将状态教师策略蒸馏为视觉策略。学生输入包含物体点云、机器人本体感知、未来K步物体位置，以实现零样本泛化。
- **公式或算法流程**（文字说明）：
  - 阶段1奖励：\(r_{\text{align}} = w_1 r_{\text{appro}} + w_2 r_{\text{lift}} + w_3 r_{\text{bonus}}\)，其中\(r_{\text{appro}}\)最小化手掌/指尖到抓取中心的距离，\(r_{\text{lift}}\)鼓励将物体提升到参考位姿，\(r_{\text{bonus}}\)在物体稳定处于参考位姿后激活。
  - 阶段2奖励：\(r_{\text{track}} = \exp(-w_t \|x_{\text{obj}}^{t_i} - \hat{x}_{\text{obj}}^i\|_2)\)。
  - 总体奖励\(r_{\text{total}} = r_{\text{align}} + w_4 r_{\text{track}}\)。

### 3. 实验设计
- **数据集/场景**：
  - **主实验**：TACO数据集，包含141个工具使用任务，6个类别（Dust, Empty, Pour in some, Put out, Skim off, Smear），自动构建为仿真任务。
  - **迁移实验**：ARCTIC数据集，11个双手协作任务（单物体），8个训练，3个测试。
- **Benchmark与对比方法**：
  - **教师学习对比**：独立PPO（BiDexHD‑IPPO） vs 集中式PPO（BiDexHD‑PPO），以及消融去掉阶段1、去掉功能性抓取中心、去掉成功奖金。
  - **学生学习对比**：BiDexHD‑IPPO+DAgger vs BiDexHD‑PPO+DAgger，以及行为克隆（BC）基线。
  - **其他**：评估未来步数\(K=\{0,1,2,5\}\)的影响。
- **评价指标**：
  - \(m_1\)：阶段1平均成功率（物体到达参考位姿并保持\(u\)步）。
  - \(m_2\)：阶段2轨迹跟踪率（物体同时满足位置和姿态误差≤ \(\epsilon_{\text{track}}\)的比例，其中\(\epsilon_{\text{succ}} = \epsilon_{\text{track}} = 0.1\)）。
  - 测试集分为组合任务（物体和工具均在训练集中出现过）和新任务（含新物体）。

### 4. 资源与算力
- 论文中**未明确提及**使用的GPU型号、数量或训练时长。仅提到在Isaac Gym中进行并行仿真，但未给出具体的算力配置细节。

### 5. 实验数量与充分性
- **实验量**：
  - 主数据集141个任务，分为16个语义子任务，训练80%，测试20%（组合和新物体）。
  - 多个教师学习方法对比（IPPO vs PPO，三个消融）。
  - 学生蒸馏方法对比（IPPO+DAgger vs PPO+DAgger vs BC），并测试不同\(K\)值。
  - 跨数据集迁移实验（ARCTIC 11个任务）。
- **充分性与公平性**：实验设计较为系统，涵盖了主要模块的消融（奖励组成、抓取中心选择、未来步数），并在两个不同性质的数据集上验证了可扩展性。对比基线包括现有的模仿学习（BC）和集中式RL，具有公平性。但缺少与专门为TACO或ARCTIC设计的其他方法的直接比较（如文中提到与PGDM的对比仅在附录中）。

### 6. 主要结论与发现
- BiDexHD框架能够从自动构建的任务中高效学习多样化双手灵巧技能，在TACO训练任务上达到74.59%的跟踪率，未见任务上达到51.07%。
- 通用两阶段奖励函数有效避免了任务特定奖励设计，阶段1的对齐奖励对策略学习至关重要。
- 视觉策略蒸馏结合未来K步位置能够实现零样本泛化，即使\(K=0\)性能下降也有限，说明教师策略已具备鲁棒技能。
- 行为克隆（BC）在双手灵巧任务中完全失败，因为仿真动力学与收集数据时的静态回放差异巨大，证实了本文RL+蒸馏方法的必要性。
- 框架可迁移至ARCTIC协作任务，展现了良好的跨任务泛化能力。

### 7. 优点
- **可扩展的通用框架**：不依赖人工定义任务，能从任意双手操作数据集中自动构造并学习，为通用双手灵巧操作提供了可行路径。
- **通用奖励设计**：两阶段奖励函数适用于所有基于物体的任务，摒弃了每任务繁琐的奖励工程。
- **教师-学生蒸馏策略**：结合状态基教师的高效训练和视觉学生的泛化能力，便于落地。
- **零样本泛化能力**：视觉策略在未见物体/组合上的表现明显优于纯状态策略，验证了框架的泛化潜力。
- **实验扎实**：在两个数据集、141+11个任务上进行了系统消融和对比，分析全面。

### 8. 不足与局限
- **算力与训练细节缺失**：未报告GPU资源、训练时间等关键计算成本，难以评估实际开销。
- **未见更先进RL基线**：仅与BC和集中式PPO对比，未与近期同领域的专门方法（如基于关键点、LLM等）进行定量比较，实验覆盖范围可进一步拓宽。
- **阈值敏感性讨论不足**：评价指标\(m_1, m_2\)依赖\(\epsilon_{\text{succ}}\)和\(\epsilon_{\text{track}}\)，文中虽提及敏感性分析见附录，但正文未充分解释其鲁棒性。
- **仿真到现实迁移未涉及**：整个框架均在仿真中验证，未讨论 sim2real 挑战及部署可行性。
- **任务复杂度限制**：当前任务主要为工具使用和单物体协作，对于更具动态性的场景（如双手交接、变形物体操作）尚未覆盖。
- **未来步数依赖**：视觉策略利用未来K步位置信息，实际部署时需提供物体未来轨迹规划，文中未深入讨论如何获取该信息，增加了应用复杂度。

（完）
