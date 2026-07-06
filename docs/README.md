<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-27 ~ 2026-07-06
- 运行时间：2026-07-06 01:31:37 UTC
- 运行状态：成功
- 本次总论文数：22
- 精读区：11
- 速读区：11

### 今日简报（AI）
本期精选22篇前沿论文，带你深入人形机器人从人类视频零样本学习的奇点时刻，以及如何通过约束感知规划实现跨本体迁移。

最值得关注的突破在于，人形机器人正获得“看视频学会技能”的能力，同时我们发现了避免强化学习奖励稀疏的关键——阶段过渡密集奖励。

想要跟上这波浪潮，不妨从理解“任意关键点引导全身控制”和“从像素到时间关联的预训练表征”这两把新钥匙开始。
- 详情：[/20260627-20260706/README](/20260627-20260706/README)

### 精读区论文标签
1. [Human2Any: Human-to-Robot Transfer via Constraint-Aware Compositional Planning](/20260627-20260706/2606.28813v1-human2any-human-to-robot-transfer-via-constraint-aware-compositional-planning)  
   标签：评分：10.0/10、query:data
   evidence：从人类视频中学习可重用的对象交互先验并与机器人可行性规划组合
2. [Human-as-Humanoid: Enabling Zero-Shot Humanoid Learning from Ego-Exo Human Videos with Human-Aligned Embodiments](/20260627-20260706/2606.32009v1-human-as-humanoid-enabling-zero-shot-humanoid-learning-from-ego-exo-human-videos-with-human-aligned-embodiments)  
   标签：评分：10.0/10、query:data
   evidence：将人类视频转化为人形机器人可执行动作用于VLA训练
3. [HandsOnWorld: Unconstrained Egocentric Video Generation with Camera-Disentangled Hand Control](/20260627-20260706/2607.02075v1-handsonworld-unconstrained-egocentric-video-generation-with-camera-disentangled-hand-control)  
   标签：评分：10.0/10、query:data
   evidence：通过单目重建直接在自然场景自我中心视频上标注3D手部，实现从人类视频重建手-物交互
4. [CORE: Common Outcome Regularities from Action-Free Visual Demonstrations for Robot Manipulation](/20260627-20260706/2606.29517v1-core-common-outcome-regularities-from-action-free-visual-demonstrations-for-robot-manipulation)  
   标签：评分：9.0/10、query:data
   evidence：从人类视频等无动作视觉演示中提取共同结果规律，无需显式动作即可训练机器人策略
5. [WARP: Whole-Body Retargeting for Learning from Offline Human Demonstrations](/20260627-20260706/2606.29940v1-warp-whole-body-retargeting-for-learning-from-offline-human-demonstrations)  
   标签：评分：9.0/10、query:data
   evidence：显式建模具身差异以从人体姿态提取精确全身动作用于机器人学习
6. [X-Morph: Human Motion Priors for Scalable Robot Learning Across Morphologies](/20260627-20260706/2606.30290v1-x-morph-human-motion-priors-for-scalable-robot-learning-across-morphologies)  
   标签：评分：9.0/10、query:data
   evidence：将人类运动转化为跨形态的机器人策略
7. [The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction](/20260627-20260706/2606.30308v1-the-surprising-effectiveness-of-video-diffusion-models-for-hand-motion-reconstruction)  
   标签：评分：9.0/10、query:data
   evidence：利用预训练的视频扩散模型从第一人称视频中重建手物交互，用于机器人操作学习
8. [Behavior Prompting Policy: Demonstrations as Prompts for Manipulation](/20260627-20260706/2606.30457v1-behavior-prompting-policy-demonstrations-as-prompts-for-manipulation)  
   标签：评分：9.0/10、query:data
   evidence：行为提示策略在推理时将单个人类演示转化为机器人动作
9. [RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation](/20260627-20260706/2606.31836v1-robotacdex-a-dexterous-visual-tactile-action-dataset-for-humanoid-manipulation)  
   标签：评分：9.0/10、query:data
   evidence：人形机器人灵巧操作的大规模多模态数据集
10. [Local Motion Matters: A Deconstruct-Recompose Paradigm for Reinforcement Learning Pre-training from Videos](/20260627-20260706/2607.00808v1-local-motion-matters-a-deconstruct-recompose-paradigm-for-reinforcement-learning-pre-training-from-videos)  
   标签：评分：9.0/10、query:data
   evidence：从视频中学习可迁移的局部运动表示，克服形态依赖的全局运动，使预训练适用于不同机器人形态
11. [HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum](/20260627-20260706/2607.02332v1-heft-heavy-payload-full-size-humanoid-teleoperation-with-privileged-motion-guidance-and-windowed-payload-curriculum)  
   标签：评分：9.0/10、query:data
   evidence：将VR中的人体运动重定向到全尺寸人形机器人的遥操作框架

### 速读区论文标签
1. [AnyBody: Free-Form Whole-Body Humanoid Control from Arbitrary Keypoint Guidance](/20260627-20260706/2606.29209v1-anybody-free-form-whole-body-humanoid-control-from-arbitrary-keypoint-guidance)  
   标签：评分：8.0/10、query:data
   evidence：从任意关键点子集学习统一全身人形控制器，避免昂贵动作捕捉，实现人体运动重定向用于可扩展的数据收集
2. [Stage-Transition Dense Reward Modeling for Reinforcement Learning](/20260627-20260706/2606.31377v1-stage-transition-dense-reward-modeling-for-reinforcement-learning)  
   标签：评分：8.0/10、query:data
   evidence：将非结构化专家视频转化为强化学习的密集奖励
3. [From Pixels to Temporal Correlations: Learning Informative Representations for Reinforcement Learning Pre-training](/20260627-20260706/2607.00811v1-from-pixels-to-temporal-correlations-learning-informative-representations-for-reinforcement-learning-pre-training)  
   标签：评分：8.0/10、query:data
   evidence：利用大规模无动作互联网视频预训练表征，实现网络数据的可扩展利用
4. [Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation](/20260627-20260706/2607.01067v1-human-centric-transferable-tactile-pre-training-for-dexterous-robotic-manipulation)  
   标签：评分：8.0/10、query:data
   evidence：来自人类自我中心视频的大规模触觉-动作数据集用于机器人学习
5. [SAMoR: Motion Modelling for Articulated Objects of Any Skeleton and Topology](/20260627-20260706/2607.02148v1-samor-motion-modelling-for-articulated-objects-of-any-skeleton-and-topology)  
   标签：评分：8.0/10、query:data
   evidence：跨骨架拓扑的运动表示，适用于人体、动物和潜在的机器人骨架之间的运动共享
6. [DCGrasp: Distance-aware Controllable Grasp Generation](/20260627-20260706/2606.29924v1-dcgrasp-distance-aware-controllable-grasp-generation)  
   标签：评分：7.0/10、query:data
   evidence：生成可控的三维手物交互
7. [Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision](/20260627-20260706/2606.30552v1-training-vision-language-action-models-with-dense-embodied-chain-of-thought-supervision)  
   标签：评分：7.0/10、query:data
   evidence：利用密集具身思维链在VLA模型中对齐跨具身表示
8. [VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes](/20260627-20260706/2606.30645v1-vlk-learning-humanoid-loco-manipulation-from-synthetic-interactions-in-reconstructed-scenes)  
   标签：评分：7.0/10、query:data
   evidence：通过合成方式生成视觉-语言-运动学监督，从自我中心观测提供机器人兼容轨迹，充当操作数据引擎
9. [HABIT: Human-Aware Behavior and Interaction Training Dataset for Robot Manipulation](/20260627-20260706/2606.31682v1-habit-human-aware-behavior-and-interaction-training-dataset-for-robot-manipulation)  
   标签：评分：7.0/10、query:data
   evidence：大规模机器人演示数据集，在有人环境下包含超万段演示和60任务，支持可扩展操作学习
10. [FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model](/20260627-20260706/2607.01212v1-furniturevla-learning-long-horizon-bimanual-furniture-assembly-with-vision-language-action-model)  
   标签：评分：7.0/10、query:data
   evidence：开发了可扩展的仿真管线用于专家数据生成，充当机器人操作数据引擎
11. [Rank-Then-Act: Reward-Free Control from Frame-Order Progress](/20260627-20260706/2607.01897v1-rank-then-act-reward-free-control-from-frame-order-progress)  
   标签：评分：6.0/10、query:data
   evidence：通过从帧序中训练进度评分器从视频演示中学习控制策略，可应用于人类视频数据


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
