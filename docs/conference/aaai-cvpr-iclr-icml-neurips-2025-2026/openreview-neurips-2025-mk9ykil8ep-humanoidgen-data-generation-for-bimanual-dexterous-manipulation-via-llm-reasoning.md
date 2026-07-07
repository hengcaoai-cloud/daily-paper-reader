---
title: "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning"
title_zh: HumanoidGen：通过LLM推理为双手灵巧操作生成数据
authors: "Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, Chenjia Bai"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Mk9ykil8eP"
tags: ["query:data"]
score: 9.0
evidence: 为双手灵巧操作自动生成任务和演示数据
tldr: 现有机器人数据集主要面向单臂平台，缺乏人形机器人双臂灵巧操作的高质量演示。HumanoidGen提出利用原子灵巧操作和LLM推理自动生成任务及约束，为仿真环境构建大规模、可扩展的双手操作数据集。该方法解决了人形机器人数据匮乏问题，为基于数据的灵巧操作学习提供了数据引擎。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 人形机器人双臂灵巧操作缺乏大规模高质量仿真数据。
method: 利用原子操作与LLM推理自动生成关系约束和任务，收集演示数据。
result: 构建了可扩展的人形机器人双手操作数据集。
conclusion: HumanoidGen为灵巧操作学习提供了数据生成引擎，促进数据驱动方法。
---

## Abstract
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

---

## 论文详细总结（自动生成）

# HumanoidGen 论文总结

## 1. 核心问题与研究背景
- 现有机器人操作数据集主要面向单臂机械臂平台，缺乏针对**人形机器人**（配备双臂与灵巧手）的仿真任务与高质量演示数据。
- 人形机器人的**双臂灵巧操作**本质上更复杂，需要协调手臂运动与手指操作，导致自动化数据采集困难。
- 动机：构建一个能**自动生成任务与收集演示数据**的框架，为人形机器人灵巧操作学习提供可扩展的数据引擎。

## 2. 方法论
- **核心思路**：利用“原子灵巧操作（atomic dexterous operations）”结合大语言模型（LLM）推理，自动生成任务中的关系约束与动作链。
- **关键技术细节**：
  - **空间标注**：对场景物体和灵巧手，基于原子操作预先进行空间标注，提供操作的基本几何与功能信息。
  - **LLM规划器**：根据物体的功能可供性（affordances）与场景内容，利用LLM生成一系列**可执行的空间约束链**，用以指导手臂的运动轨迹。
  - **增强规划能力**：针对长时域任务或标注不完全的情况，引入一种**蒙特卡洛树搜索（MCTS）的变体**来提升LLM的推理质量。
- **算法流程梗概**（文字描述）：
  1. 输入场景物体与灵巧手的空间标注。
  2. LLM规划器生成原子操作间的空间约束关系序列。
  3. 通过MCTS优化长序列规划中的不确定性，生成协调双臂与手指运动的完整任务描述。
  4. 在仿真环境中执行任务，收集演示数据。

## 3. 实验设计
- **生成数据集与评测基准**：创建了带有扩增场景的**新基准测试集**（augmented scenarios），用于评估生成数据的质量。
- **对比与验证方法**：
  - 在生成的双手灵巧操作数据集上，训练**2D扩散策略**与**3D扩散策略**，验证数据对策略性能的支撑作用。
  - 观察策略性能随数据规模扩展的能力。
- 未提及是否与其他具体基线数据集或方法直接对比。

## 4. 资源与算力
- **论文摘要未明确说明**使用的GPU型号、数量、训练时长或具体算力配置。需查阅正文获取进一步信息。

## 5. 实验充分性
- 从摘要看，实验部分主要完成：
  - 一个基准测试集的构建与评估。
  - 两种扩散策略（2D和3D）的数据规模扩展实验。
- **实验数量明显偏少**（仅报告策略性能随数据量 scaling 的结果），摘要中未包含消融实验、不同场景或任务类别的对比、与现有数据集的横向对比等。
- 因此，当前信息不足以判断实验是否完全充分、是否覆盖全面，可能存在**评价维度单一**的风险。

## 6. 主要结论与发现
- 利用原子操作与LLM推理自动生成的双手灵巧操作数据，能够有效驱动2D与3D扩散策略的性能提升，且性能可随数据集规模扩展。
- HumanoidGen为人形机器人灵巧操作学习提供了可扩展的数据生成解决方案。

## 7. 优点与亮点
- **创新性自动化数据生成框架**：将LLM推理与原子操作结合，是解决人形机器人数据匮乏问题的新思路。
- **可扩展性强**：通过LLM规划与MCTS优化，可适应不同场景和任务，具备放大到大规模数据生成的能力。
- **支持复杂任务**：专门针对人形机器人双人臂与灵巧手协调操作这一高难度问题。
- 初步实验证明了生成数据的有效性和扩展效益。

## 8. 不足与局限
- **实验覆盖有限**：摘要仅展示了数据生成后的策略性能 scaling 结果，缺乏多维度评估，如成功率、泛化能力、对比sota仿真数据集、不同任务复杂度的表现等。
- **可能偏差风险**：生成数据的质量高度依赖LLM与物体标注的准确性，若标注不足或LLM推理出现错误，可能导致不合理的操作或不可执行的任务。
- **应用限制**：目前仅在仿真环境中验证，迁移到真实人形机器人的物理可行性尚未提及。
- **算力信息缺失**：未能评估其对计算资源的需求与可复现性。

（完）
