---
title: Object-centric 3D Motion Field for Robot Learning from Human Videos
title_zh: 以物体为中心的三维运动场用于从人类视频中学习机器人
authors: "Zhao-Heng Yin, Sherry Yang, Pieter Abbeel"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=kp9B9iQDIt"
tags: ["query:data"]
score: 10.0
evidence: 从人类视频中提取以物体为中心的三维运动场，用于机器人零样本控制
tldr: 针对从人类视频中提取动作知识用于策略学习的挑战，提出以物体为中心的3D运动场作为动作表示，并设计去噪估计器和零样本控制器，显著提升了机器人从视频中学习的能力。在多种操作任务中，使用该运动场实现了零样本控制，比现有方法更精确。物体中心3D运动场为从人类视频中学习机器人控制提供了一种高效、可扩展的动作表示方法。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有动作表示（如视频帧、像素流等）在建模复杂度或信息丢失方面存在局限。
method: 提出两个新组件：训练去噪3D运动场估计器提取精细物体3D运动，以及基于此运动场的零样本机器人控制框架。
result: 在多种操作任务中，使用该运动场实现了零样本控制，比现有方法更精确。
conclusion: 物体中心3D运动场为从人类视频中学习机器人控制提供了一种高效、可扩展的动作表示方法。
---

## Abstract
Learning robot control policies from human videos is a promising direction for scaling up robot learning. However, how to extract action knowledge (or action representations) from videos for policy learning remains a key challenge. Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information. In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this representation from videos for zero-shot control. We introduce two novel components. First, a novel training pipeline for training a ``denoising'' 3D motion field estimator to extract fine object 3D motions from human videos with noisy depth robustly. Second, a dense object-centric 3D motion field prediction architecture that favors both cross-embodiment transfer and policy generalization to background. We evaluate the system in real world setups. Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior approaches fail ($\lesssim 10$\%), and can even acquire fine-grained manipulation skills like insertion.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：从人类视频中学习机器人操控策略，是扩展机器人学习规模的一条有前景的路径。其核心瓶颈在于如何从视频中提取有效的动作知识（或动作表示），以用于策略学习。
- **现有表示的局限**：
  - **视频帧**：直接预测下一帧图像，建模复杂度极高，且难以直接转换为机器人可执行的动作。
  - **像素流（Pixel flow）**：仅包含2D运动，丢失了深度和三维结构信息。
  - **点云流（Pointcloud flow）**：虽然包含三维信息，但往往对背景噪声敏感，且难以精确捕捉物体本身的细粒度运动。
- **本文解决的问题**：提出一种新的动作表示——**以物体为中心的3D运动场（object-centric 3D motion field）**，并给出从含噪声的人类视频中鲁棒提取该表示、并将其用于机器人零样本控制的完整框架。

## 2. 论文提出的方法论

- **核心思想**：
  - 用**物体表面三维点的前景运动场**来描述动作：对视频中感兴趣的物体，预测其每个表面点在下一帧的三维位移。
  - 这种表示天然捕获了物体的刚体/非刚体运动、尺度和姿态变化，同时滤除背景无关信息，适合跨形态迁移（从人类手到机器手）。

- **关键技术细节**：
  1. **去噪3D运动场估计器训练管线**：
     - 针对人类视频中深度估计噪声大的问题，设计专门的训练策略：**先给估计器提供带噪声的深度输入，再训练其输出干净、细致的物体3D运动场**，实现“去噪”效果。
     - 该估计器能够鲁棒地从单目RGB‑D（或深度估计）视频中提取精细的物体运动。
  2. **密集物体中心3D运动场预测架构**：
     - 架构设计强调**跨形态泛化**：即使训练时仅见人手，推理时也能迁移到机器手。
     - 架构鼓励**对背景不变性**：仅关注前景物体，忽略背景变化，提升策略泛化能力。
  3. **零样本机器人控制框架**：
     - 给定一张当前场景的机器人视角图像和目标物体，利用训练好的运动场估计器预测目标物体的未来3D运动场。
     - 将该运动场作为期望的运动目标，映射到机器人末端执行器的运动指令，实现直接从人类视频演示到机器人执行的零样本泛化。

- **算法流程示意（文字）**：
  > 人类视频序列 → 提取目标物体mask + 初始深度 → 去噪3D运动场估计器预测每个表面点的位移 → 得到密集的object‑centric 3D motion field → 在机器人控制时，输入当前目标图 → 预测运动场 → 转换为机器人末端期望位移/姿态 → 执行。

## 3. 实验设计

- **实验环境**：真实世界机器人操作设置（real‑world setups），未明确说明机器人平台细节，但涉及多种操控任务。
- **任务场景**：覆盖多种操作任务（根据摘要至少包含“diverse tasks”），特别提及了**精细操作技能如插入（insertion）**。
- **对比基准**：
  - 与**最新的同类方法**对比（latest method，未具体指明，可能为基于点云流或视频预测的领先方法）。
  - 评估了**3D运动估计的精度**：本文方法将估计误差降低超过50%。
- **成功率比较**：
  - 本文方法在多样任务中平均成功率达到 **55%**。
  - 先前方法在相同任务上成功率极低（≲10%），近乎失败。
  - 表明基于物体中心3D运动场的表示和控制器显著超越了先前技术。

## 4. 资源与算力

- 论文摘要及提供的元数据中**未明确提及**任何计算资源信息，包括GPU型号、数量、训练时长、推理速度等。
- 因此无法给出具体的算力统计。

## 5. 实验数量与充分性

- **实验组数推断**：
  - 至少包含**多个真实世界操作任务**（diverse tasks），以及一个精细技能（插入）。
  - 明确进行了**定量精度对比**（3D motion estimation error over 50% reduction）和**成功率对比**（55% vs. ≲10%）。
  - 很可能包含**消融实验**（用于验证两个新组件各自的作用），但现有信息未明确描述。
- **实验充分性评价**：
  - 从摘要可见，实验覆盖了真实环境、多任务、与最新方法的对比，以及从粗糙到精细的技能，实验设计较为全面。
  - **客观性与公平性**：对比基准为最新方法，且指标包括标准化误差和成功率，具备可比性；但在未公开完整论文的情况下，无法判断训练数据、机器人配置、成功率统计细节是否完全对等。
  - 需注意，摘要无法展示所有消融或统计分析，因此现有信息下，实验数量看似合理但尚不完整。

## 6. 论文的主要结论与发现

- **表示有效性**：以物体为中心的3D运动场是一种高效、可扩展的动作表示，能直接从人类视频中提取可用的操控知识。
- **性能突破**：该方法在3D运动估计精度上大幅提升（误差减半），并首次在零样本真实机器人控制中取得可行成功（55%平均成功率），而先前方法无法胜任。
- **精细技能获取**：证明了该表示能捕捉足够细粒度的运动，使得机器人能执行如插入这类高精度操作任务。
- **整体结论**：所提出的框架为从人类视频学习机器人控制提供了新的动作表示和对应提取方案，显著推进了该方向的实际应用能力。

## 7. 优点

- **创新性表示**：提出object‑centric 3D motion field，将动作建模聚焦于前景物体的三维细密运动，克服了2D流信息缺失和点云流背景敏感的问题。
- **鲁棒训练策略**：专为含噪声人类视频设计的“去噪”训练管道，使模型对深度估计噪声具有强鲁棒性，更适用于现实世界应用。
- **跨形态零样本迁移**：预测架构本身促进从人类手到机器手的泛化，无需配对数据或域适应微调。
- **从粗糙到精细**：既能在多种典型任务上显著超越基线，又展示了插入等精细操作的潜力，覆盖面广。
- **实验真实且对比突出**：在真实机器人上验证，与最新方法直接对比，效果提升明显（误差降50%+，成功率从<10%到55%）。

## 8. 不足与局限

- **摘要信息有限**：评价基于摘要提供的有限内容，以下局限部分为合理推测，具体限制需阅读全文。
- **依赖深度估计**：方法输入需要深度信息（或从图像估计深度），在深度质量极差或纹理缺失场景下可能失效。
- **物体分割要求**：以物体为中心的前提需要前景物体分割/检测，额外模块的失败可能影响整体系统。
- **动作映射性**：从3D运动场映射到机器人控制命令，可能依赖特定的标定和运动学模型，泛化到不同形态的机器人可能存在额外挑战（虽文中声称跨形态迁移，但仅适应于末端位置控制，难以处理关节空间的奇异性等）。
- **实验覆盖可能的局限**：摘要未提及对动态背景、多物体交互、长期任务、或非刚性物体的全面测试，也可能未在完全无监督的场景下评估。
- **未明确算力与效率**：缺乏计算开销信息，实际部署的实时性未知。
- **成功率仍有提升空间**：55%平均成功率在真实操作中仍属中低水平，离实用化有一定距离，尤其在安全攸关场景。

（完）
