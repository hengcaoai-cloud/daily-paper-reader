---
title: Data Scaling Laws in Imitation Learning for Robotic Manipulation
title_zh: 机器人操作中模仿学习的数据缩放规律
authors: "Fanqi Lin, Yingdong Hu, Pingyue Sheng, Chuan Wen, Jiacheng You, Yang Gao"
date: 2025-01-22
pdf: "https://openreview.net/pdf?id=pISLZG7ktL"
tags: ["query:data"]
score: 7.0
evidence: 机器人操作模仿学习中数据缩放规律的实证研究
tldr: 该工作系统研究了机器人操作模仿学习中的数据缩放规律，发现策略的零样本泛化性能随训练环境数量、物体种类和演示数量的增加而提升，并量化了缩放关系。通过在大量环境和物体上收集数据，实验揭示了数据多样性的最关键维度。该研究为可复现的机器人学习缩放规律提供了实证基础，指导未来如何有效扩大数据集以实现泛化。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 借鉴NLP和CV的成功，探究机器人操作是否同样存在数据缩放规律。
method: 收集大规模数据，系统改变环境、物体和演示数量，评估策略泛化性能。
result: 揭示了零样本泛化随这些变量增长的幂律关系，并确定了关键缩放维度。
conclusion: 为机器人模仿学习的数据收集和缩放提供了可操作的指导。
---

## Abstract
Data scaling has revolutionized fields like natural language processing and computer vision, providing models with remarkable generalization capabilities. In this paper, we investigate whether similar data scaling laws exist in robotics, particularly in robotic manipulation, and whether appropriate data scaling can yield single-task robot policies that can be deployed zero-shot for any object within the same category in any environment. To this end, we conduct a comprehensive empirical study on data scaling in imitation learning. By collecting data across numerous environments and objects, we study how a policy’s generalization performance changes with the number of training environments, objects, and demonstrations. Throughout our research, we collect over 40,000 demonstrations and execute more than 15,000 real-world robot rollouts under a rigorous evaluation protocol. Our findings reveal several intriguing results: the generalization performance of the policy follows a roughly power-law relationship with the number of environments and objects. The diversity of environments and objects is far more important than the absolute number of demonstrations; once the number of demonstrations per environment or object reaches a certain threshold, additional demonstrations have minimal effect. Based on these insights, we propose an efficient data collection strategy. With four data collectors working for one afternoon, we collect sufficient data to enable the policies for two tasks to achieve approximately 90\% success rates in novel environments with unseen objects.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

*   **研究动机**：在大语言模型（NLP）和计算机视觉（CV）领域，数据规模扩大（data scaling）已被证明是模型获得强大泛化能力的关键驱动力。然而，在机器人操作领域，是否存在类似的数据缩放规律尚不明确。
*   **核心问题**：本工作旨在系统性地探究机器人操作模仿学习中的数据缩放规律，回答三个关键维度（训练环境数量、物体种类数量、演示数量）如何影响策略的零样本（zero-shot）泛化性能。
*   **整体目标**：验证是否通过恰当的数据缩放，能够使单任务机器人策略在新环境、同类任意物体上实现零样本部署，并为未来机器人学习的数据收集提供可操作的指导原则。

### 2. 论文提出的方法论：核心思想与关键技术细节

*   **核心思想**：通过大规模、系统性地变化训练数据中的环境数量、物体数量和演示数量，测量策略最终在未见环境和未见物体上的零样本成功率，从而拟合出数据规模与泛化性能之间的定量关系。
*   **数据收集与评估方案**：
    *   收集了超过 **40,000** 个演示（demonstrations）。
    *   在真实世界的机器人上执行了超过 **15,000** 次 rollout，进行严格评估。
*   **关键调控变量**：
    *   **环境维度**：改变训练时所涉及的不同场景/背景的数量。
    *   **物体维度**：改变训练时所使用物体实例的数量（物体属于同一类别，但外观、几何等不同）。
    *   **演示维度**：改变每个特定环境或物体上收集的演示数量。
*   **研究方法**：通过控制变量法，分别研究上述每一维度单独增加时，策略泛化性能的变化曲线，并尝试拟合其数学关系（如幂律，power-law）。

### 3. 实验设计：场景、基准与对比方法

*   **任务与场景**：
    *   聚焦于**机器人操作**（robotic manipulation）任务，具体任务在摘要中提及“两个任务”可实现约90%成功率，但未详述任务类型（如抓取、放置等）。
    *   实验环境为**真实世界**（real-world），而非仿真，涉及大量不同环境和物体。
*   **评估基准（Benchmark）**：
    *   主要基准为策略在**新环境+未见物体**组合下的零样本泛化成功率。
*   **对比方法**：
    *   论文本身不侧重算法横向对比，而是**以自身策略为对象，研究其性能随数据量（环境数、物体数、演示数）改变的规律**。即不同实验组对应不同数据规模下的同一类策略性能对比。
*   **实验规模**：通过大量实物环境、物体实例和超过4万次演示构建了大规模数据集，以保证规律的可靠性。

### 4. 资源与算力

*   文中**未明确提供**训练过程所消耗的具体算力信息（如 GPU 型号、数量、训练时长等）。主要资源投入体现在**大规模真实环境搭建、数千次机器人数据采集与评估**的人力与物理成本上（如提到四个数据采集员工作一个下午即可为两个任务收集足够数据达到约90%成功率）。

### 5. 实验数量与充分性

*   **实验组数**：基于系统性的多维度缩放设计，可以推断实验组数量较多。至少需要覆盖：
    *   不同环境数量下的性能测试（数点到数十点）。
    *   不同物体数量下的性能测试（类似尺度）。
    *   不同每个环境/物体的演示数量下的性能测试。
*   **充分性**：实验设计非常充分，通过**超过 40,000 个演示**和 **15,000 次真实机器人 rollout** 的大规模数据支撑，且探索了三个独立维度，足够支撑其核心结论。
*   **客观性与公平性**：采用统一的评估协议，在新环境与未见物体上进行零样本测试，且是基于真实物理环境的严格评测，避免了仿真与现实的差距，评估体系客观公正。

### 6. 论文的主要结论与发现

*   **缩放关系成立**：策略的泛化性能与环境数量、物体数量大致遵循**幂律（power-law）关系**，即随着数据在这些维度上增长，性能可预测地提升。
*   **多样性压倒绝对数量**：环境和物体的多样性远比单纯的演示绝对数量更重要。每一个环境或物体上的演示数量存在一个**红利递减的阈值**，超过该阈值后，额外演示的带来的增益微乎其微。
*   **可操作的高效数据策略**：基于上述发现，可以制定高效的数据收集策略。例如，只需**四个数据采集员投入一个下午**，即可为两个任务收集到足够多样化的数据，使策略在全新环境和物体上达到大约 **90% 的成功率**。
*   **维度重要性排序**：实验揭示了环境与物体多样性是实现零样本泛化最关键的数据缩放维度。

### 7. 优点：方法与实验设计亮点

*   **系统性**：首次在机器人操作模仿学习中，系统、量化地拆解并研究了数据三大维度（环境、物体、演示）的缩放效应，而非笼统地增加数据量。
*   **实证严谨**：实验完全在**真实世界**进行，数据规模极大（>40k demo, >15k rollout），结论扎实可信。
*   **揭示了实用规律**：明确指出了“多样性优于单一场景大量重复数据”这一反直觉但重要的结论，并给出了效率阈值，对数据收集策略具有直接指导意义。
*   **可复现性倡导**：通过规律的量化，为机器人学习领域提供了类似 NLP、CV 中的可复现缩放律，推动领域从经验摸索向工程科学转变。

### 8. 不足与局限

*   **任务泛化性有限**：结论基于“两个操作任务”和“同类物体”的零样本泛化，是否能够推广到完全不同的任务族（如接触力密集型任务、长序列任务）尚待验证。
*   **最高性能仍受限**：缩放规律只在研究的数据范围内成立，是否继续扩展数据规模会使性能持续提升或趋于饱和未知。
*   **算力信息缺失**：没有提及策略架构（如扩散策略、ACT等）及其训练所占用的计算资源，无法评估算力 scaling 的成本。
*   **环境与物体多样性定义**：文中未详细定义环境与物体的复杂度、差异度指标，实际应用中如何量化“多样性”可能会影响规律的直接迁移。
*   **潜在偏差**：物体和环境的选取可能有特定偏向，非完全随机采样，可能影响规律的普适性。

（完）
