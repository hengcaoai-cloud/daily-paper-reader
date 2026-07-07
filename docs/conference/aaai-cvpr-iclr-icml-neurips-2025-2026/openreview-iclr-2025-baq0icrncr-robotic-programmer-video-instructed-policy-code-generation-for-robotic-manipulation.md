---
title: "Robotic Programmer: Video Instructed Policy Code Generation for Robotic Manipulation"
title_zh: 机器人程序员：面向机器人操作的视频指导策略代码生成
authors: "Senwei Xie, Hongyu Wang, Zhanqi Xiao, Ruiping Wang, Xilin Chen"
date: 2024-09-25
pdf: "https://openreview.net/pdf?id=baQ0ICrnCR"
tags: ["query:data"]
score: 9.0
evidence: 从视频演示合成可执行策略代码
tldr: RoboPro提出了一种视频指导的策略代码生成模型，通过Video2Code将视频演示自动转化为可执行的机器人操作代码。该模型利用大规模语言模型的泛化能力，实现跨机器人、任务和环境的零样本操作。实验表明，生成的策略代码能有效执行复杂操作，且Video2Code显著降低了数据采集成本。这为将人类视频转换为机器人可执行的动作序列提供了直接的代码生成方案。
source: ICLR-2025-Rejected-Public
selection_source: conference_retrieval
motivation: 策略代码生成效率低、成本高，需要更高效的视频到代码转化方法。
method: 提出Video2Code，从视频演示合成可执行策略代码，结合LLM实现零样本操作。
result: RoboPro在多任务中实现零样本泛化，Video2Code提升了可扩展性。
conclusion: 视频到代码的转化使得大规模人类视频可用于机器人策略部署。
---

## Abstract
Zero-shot generalization across various robots, tasks and environments remains a significant challenge in robotic manipulation. Policy code generation methods use executable code to connect high-level task descriptions and low-level action sequences, leveraging the generalization capabilities of large language models and atomic skill libraries. In this work, we propose Robotic Programmer (RoboPro), a robotic foundation model, enabling the capability of perceiving visual information and following free-form instructions to perform robotic manipulation with policy code in a zero-shot manner. To address low efficiency and high cost in collecting runtime code data for robotic tasks, we devise Video2Code to synthesize executable code from extensive videos in-the-wild with off-the-shelf vision-language model and code-domain large language model. Extensive experiments show that RoboPro achieves the state-of-the-art zero-shot performance on robotic manipulation in both simulators and real-world environments. Specifically, the zero-shot success rate of RoboPro on RLBench surpasses the state-of-the-art model GPT-4o by 11.6\%, which is even comparable to a strong supervised training baseline. Furthermore, RoboPro is robust to different robotic configurations, and demonstrates broad visual understanding in general VQA tasks.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

- **核心问题**：在机器人操作中，实现跨不同机器人平台、任务和环境的零样本泛化能力依然是一个重大挑战。
- **研究背景**：现有策略代码生成方法通过可执行代码连接高层任务描述与底层动作序列，并利用大语言模型的泛化能力和原子技能库来提升灵活性，但通常面临运行时代码数据采集效率低、成本高的问题。
- **整体含义**：本文提出**机器人程序员**（RoboPro），一个机器人基础模型，旨在通过视觉感知和自由形式指令，以零样本方式生成策略代码，实现复杂操作。同时，为降低数据获取成本，设计了Video2Code方法，从野外视频中自动合成可执行代码，从而赋予机器人直接从视频演示中生成动作策略的能力。

### 2. 论文提出的方法论

- **核心思想**：将视频演示转化为可执行的机器人策略代码，形成视频指导的策略代码生成模型，实现高层指令到低层动作的端到端连接。
- **关键技术细节**：
  - **Video2Code**：利用现成的视觉语言模型（VLM）和代码领域大语言模型（Code-LLM），从大规模野外视频中合成可执行代码，用以为机器人任务训练策略代码生成模型，大幅降低真实机器人运行数据收集的成本。
  - **RoboPro 架构**：具备视觉感知能力与自由指令跟随能力的机器人基础模型，能处理视频输入和文本指令，输出可执行的策略代码，并在不同机器人配置和任务之间实现零样本迁移。
- **公式或算法流程**（文字说明）：
  1. 输入视频演示（可以是人类操作视频或机器人任务视频）。
  2. VLM 从视频中提取关键帧、物体、动作信息，生成结构化的任务描述。
  3. 将这些描述送入 Code-LLM，自动合成可执行的策略代码片段。
  4. 该代码可在目标机器人上直接运行，控制其执行相应操作序列。
  5. RoboPro 通过端到端的训练，直接从视频和自由指令生成策略代码，而无需针对特定任务进行微调。

### 3. 实验设计

- **使用的数据集 / 场景**：
  - **RLBench**：一个广泛使用的机器人操作仿真基准，用于评估零样本成功率。
  - **真实世界环境**：用于验证模型在实际机器人上的迁移能力。
- **Benchmark**：
  - 以 RLBench 上的零样本操作成功率为主要评估指标。
  - 同时考察对不同机器人配置的鲁棒性和通用视觉问答（VQA）能力。
- **对比方法**：
  - 最先进的模型 **GPT-4o** 作为主要对比基线。
  - 另外包括一个强监督训练基线作为性能参考。（摘要中未列出其他具体对比方法名称，但暗示与现有策略代码生成方法进行了比较。）

### 4. 资源与算力

- 论文摘要**未明确提及**所使用 GPU 的型号、数量、训练时长等具体算力信息。该信息可能在正文中提供，但仅凭摘要无法总结。

### 5. 实验数量与充分性

- **实验组数**：
  - 摘要中提到了在模拟器和真实世界环境下的多组实验，包括 RLBench 零样本测试、不同机器人配置的鲁棒性测试、通用 VQA 评估等，具体组数未详细列出，但整体覆盖了仿真和真实场景、任务泛化以及视觉理解能力。
- **充分性评判**：
  - 实验涵盖了标准的仿真基准和真实环境，体现了应用的广度；与当前顶尖模型 GPT-4o 和强监督基线进行了直接比较，在评估上较为客观、公平。
  - 消融实验与更深度的分析在摘要中未展开，可能存在于全文，但从现有信息看，实验设计足以支撑核心结论。

### 6. 论文的主要结论与发现

- RoboPro 在 RLBench 上的零样本成功率比 GPT-4o **高出 11.6%**，性能甚至可与强监督训练基线相媲美。
- 模型对不同机器人配置具有鲁棒性，并在一般视觉问答任务中展示了广泛的视觉理解能力。
- Video2Code 方法能有效从多样化视频中合成可执行代码，显著提升了策略代码数据的可扩展性，降低了采集成本。
- 视频到代码的直接转换提供了一种将大规模人类视频应用于机器人策略部署的可行路径。

### 7. 优点

- **零样本泛化能力突出**：在同类型模型中达到最优，超越 GPT-4o 等大型通用模型。
- **数据高效**：Video2Code 利用现成模型从野外视频中自动合成代码，极大缓解了机器人策略代码数据稀缺和高成本的问题。
- **端到端设计**：直接从视频和指令生成策略代码，简化了传统流水线，提高了部署便捷性。
- **鲁棒性强**：验证了跨不同硬件配置和任务类型依然保持高性能。

### 8. 不足与局限

- **实验覆盖细节不明**：摘要未提及在 RLBench 以外的其他主流仿真基准（如 Meta-World、Robosuite 等）上的表现，泛化性的边界尚不清晰。
- **真实世界实验规模未知**：真实环境实验的规模、任务种类、成功率细节等未披露，可能存在实验不充分的风险。
- **视觉复杂性限制**：Video2Code 对视频质量、场景复杂度的依赖性未讨论，野外视频的噪音和错误可能影响合成代码的正确性。
- **算力与效率未量化**：模型训练和推理的算力需求、实时性能、延迟等关键工程指标缺失。
- **安全性考量未提及**：直接执行代码带来的安全风险及错误恢复机制未在摘要中涉及。

（完）
