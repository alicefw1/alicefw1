<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1200&color=22D3EE&center=true&vCenter=true&width=760&lines=Hi%2C+I%27m+Feng+Wanyi+%F0%9F%91%8B;Computer+Vision+%26+Deep+Learning;Algorithm+Engineer+%7C+Researcher" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://www.xsyu.edu.cn/"><img src="https://img.shields.io/badge/-Xi%27an_Shiyou_University-0F2A43?style=flat-square&labelColor=0B1220&logo=google-scholar&logoColor=22D3EE" alt="Xi'an Shiyou University" /></a>
  <a href="https://www.seu.edu.cn/"><img src="https://img.shields.io/badge/-Southeast_University_(M.Sc._Recommended)-0F2A43?style=flat-square&labelColor=0B1220&logo=bookstack&logoColor=22D3EE" alt="Southeast University (M.Sc. Recommended)" /></a>
  <img src="https://img.shields.io/badge/-Computer_Vision_%7C_Deep_Learning-0F2A43?style=flat-square&labelColor=0B1220&logo=pytorch&logoColor=22D3EE" alt="Computer Vision | Deep Learning" />
  <img src="https://img.shields.io/badge/-Xi%27an%2C_China-0F2A43?style=flat-square&labelColor=0B1220&logo=googlemaps&logoColor=22D3EE" alt="Xi'an, China" />
  <a href="https://github.com/alicefw1"><img src="https://img.shields.io/badge/-alicefw1-0F2A43?style=flat-square&labelColor=0B1220&logo=github&logoColor=22D3EE" alt="GitHub" /></a>
</p>

<p align="center">
  <img src="assets/rule.png" width="100%" alt="" />
</p>

## 关于我 · About Me

西安石油大学计算机学院本科生在读，**保研至东南大学（985）苏州联合研究生院计算机技术硕士**；专业排名 **1/65（Top 1.5%）**，**GPA 4.55/5.0**，国家奖学金获得者。专注于**计算机视觉与深度学习**算法研究，以**第一作者**完成 2 篇科研论文，并有医学影像（脊椎手术螺钉定位）、机器人感知（灵巧手手势识别）等核心项目经历；热衷把顶会论文（如 CVPR 2026 D4RT）做成可交互的精读系统，相信「能复现、能讲清、能落地」才是真正的掌握。

> CS undergrad at Xi'an Shiyou University (ranked **1/65, Top 1.5%**, GPA **4.55/5.0**, National Scholarship), **recommended for admission to Southeast University (985) — M.Sc. in Computer Technology**. Focused on **computer vision and deep learning**; first author of 2 research papers, with hands-on project experience in medical imaging (spine screw localization) and robotic perception (dexterous-hand gesture recognition). I enjoy turning top-tier papers (e.g., CVPR 2026 D4RT) into interactive, reproducible learning systems.

- **研究方向 · Research** — 计算机视觉 · 医学影像 · 深度学习 · 工业视觉检测 · 机器人感知
- **现在 · Now** — 深耕 CV 算法，推进科研论文投稿与方法落地
- **方法 · Approach** — 把模型做准，把实验做实，把论文讲清

<p align="center">
  <img src="assets/rule.png" width="100%" alt="" />
</p>

## 研究成果 · Research

> 第一作者论文 + 核心项目经历 · First-author papers & key project experience

### 01 · 脊椎手术螺钉定位｜手术机器人智能仿真与规划软件系统
*核心成员 · 合作方：邦杰星 ｜ 2026.09 – 至今*
- 参与基于 **CT 影像**的椎体分割、影像配准与螺钉定位全流程；项目数据约 600 例，筛选 **251 例**用于模型开发与评估
- 围绕螺钉出入点及角度预测，比较模板库匹配、**landmark 预测**与 **nnU-Net** 等方案，同步开展 landmark 与密集预测实验
- 结合人工审核与专家复核进行结果质检，分析定位误差并反馈至训练与方案迭代；当前定位误差约 **4–5 mm**，持续优化中
- `医学影像` `CT 分割` `nnU-Net` `landmark 预测` `手术机器人`

### 02 · WDRS：面向石油工业轴承故障诊断的先进深度学习架构
*第一作者 · 发表于 EI 国际会议 ｜ 2025.03 – 2026.05*
- 提出 **WDRS**（小波变换 + 储备池计算 + SVM）故障诊断模型，设计跨工况实验与消融实验，验证各模块在变负载下的互补性与稳健性
- 相比 WT+MLP 基线，将故障检测准确率从 **<90% 提升至 97.35%**，推理耗时更短，适配工业在线监测与预测性维护
- 论证模型在旋转机械、工业物联网等领域的推广应用前景
- `深度学习` `信号处理` `小波变换` `SVM` `工业检测`

### 03 · 西电灵巧手手势识别与 ROS2 仿真联调
*参与人 ｜ 2025.09 – 2025.10*
- 基于灵巧手示波器时序数据，打通 **CSV 信号 → 预处理 → 特征提取 → 分类 → ROS2 仿真控制**全链路，聚焦分类算法对比与替换
- 比较 **10 类**代表性模型并采用连续块 5 折验证；选定收缩 LDA，**Accuracy 98.82%、Macro-F1 98.84%**（XGBoost 基线 92.06%）
- 将识别标签及置信度接入 **ROS2 bridge**，支持仿真节点订阅控制，RViz 展示分类概率；整理算法比较、验证口径与适用边界
- `时序分类` `LDA` `XGBoost` `ROS2` `RViz`

### 04 · 基于语言风格指纹的 AI 生成文本溯源
*第一作者*
- 构建覆盖 **ChatGPT / Claude / Gemini / ERNIE / Grok** 的五模型文本数据集
- 提出 **125 维语言风格指纹**特征体系（词法 / 句法 / 标点），结合 TabPFN 实现最高 **91%** 的模型级溯源准确率
- 从「区分 AI / 人类文本」升级为「判断由哪个 AI 模型生成」，服务于学术打假、内容治理与生成式 AI 合规监管
- `自然语言处理` `特征工程` `TabPFN` `AI 治理`

<p align="center">
  <img src="assets/rule.png" width="100%" alt="" />
</p>

## 技术栈 · Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,cpp,java,pytorch,sklearn,opencv,numpy,git,linux,vscode&theme=dark&perline=10" alt="Python, C++, Java, PyTorch, scikit-learn, OpenCV, NumPy, Git, Linux, VS Code" />
</p>

- **算法 · Algorithms** — 计算机视觉 · 医学影像分割 · 机器学习 · 时序信号分类 · 特征工程
- **语言 · Languages** — **Python**（主力）· C / C++ · Java
- **框架工具 · Tools** — PyTorch · nnU-Net · scikit-learn · XGBoost · OpenCV · NumPy / Pandas · ROS2 · RViz
- **科研能力 · Research** — 英文论文撰写 · 文献检索 · 交叉验证 / 消融实验 · Accuracy / Macro-F1 / Dice 指标分析 · 小波变换与时序特征提取

<p align="center">
  <img src="assets/rule.png" width="100%" alt="" />
</p>

## 精选项目 · Featured Projects

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/alicefw1/d4rt-paper-lab">01 · D4RT 论文实验室</a></h3>
<p>把 <strong>CVPR 2026 最佳论文 D4RT</strong> 做成可交互教学仪器：五维查询矩阵 <code>(u, v, t_src, t_tgt, t_cam) → P ∈ R³</code>，Python / JS 双实现一致性校验，纯静态、零依赖、离线可用。</p>
<p><sub>Interactive lab for CVPR 2026 best paper D4RT — a 5D query matrix with dual Python/JS consistency checks, zero-dependency and offline-ready.</sub></p>
<p><code>Computer Vision</code> <code>Python</code> <code>JavaScript</code> <code>Canvas</code></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/alicefw1/cumcm-2025-smoke-interference-sim">02 · 烟幕干扰仿真</a></h3>
<p>2025 全国大学生数学建模竞赛 A 题：离线 Plotly 三维场景、三视图与 184 条视线遮挡判定，获<strong>省级一等奖</strong>。</p>
<p><sub>Interactive 3D/2D simulation for CUMCM 2025 Problem A, with offline Plotly and 184 sightline samples for occlusion tests.</sub></p>
<p><code>Python</code> <code>Plotly</code> <code>3D Visualization</code></p>
<p><a href="https://alicefw1.github.io/cumcm-2025-smoke-interference-sim/"><strong>在线体验 →</strong></a></p>
</td>
</tr>
</table>

<p align="center">
  <sub>更多项目见 <a href="https://github.com/alicefw1?tab=repositories">全部公开仓库 →</a></sub>
</p>

<p align="center">
  <img src="assets/rule.png" width="100%" alt="" />
</p>

## 荣誉奖项 · Honors

- 🏆 **国家奖学金** · 中国石油奖学金 · 品学兼优一等奖学金 · 学科竞赛奖学金
- 🥇 2025 全国大学生数学建模竞赛 **省级一等奖**
- 🥈 2024 全国大学生英语竞赛（NECCS）**国家级二等奖** · CET-6 **559**
- 🥈 CATTI 杯全国翻译大赛（英语笔译）**省级二等奖**
- 🥈 2025 全国大学生软件创新大赛 · 软件系统安全赛 西北赛区二等奖
- 🥈 2025 计算机设计大赛西北赛区 · 数据可视化 / 物联网 / Web 开发 三项二等奖
- 📚 专业核心课程多门满分：算法分析与设计（100）· 概率论与数理统计（100）· 线性代数（100）· 数字逻辑（99）· 数据通信原理（99）

<p align="center">
  <img src="assets/rule.png" width="100%" alt="" />
</p>

## GitHub 数据 · GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=alicefw1&show_icons=true&hide_border=true&hide_rank=true&bg_color=0D1117&title_color=22D3EE&icon_color=22D3EE&text_color=C9D1D9&locale=cn" alt="GitHub stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=alicefw1&layout=compact&hide_border=true&bg_color=0D1117&title_color=22D3EE&text_color=C9D1D9&langs_count=8&locale=cn" alt="Top languages" />
</p>

<p align="center">
  <img width="70%" src="https://streak-stats.demolab.com?user=alicefw1&theme=github-dark-blue&hide_border=true&background=0D1117&ring=22D3EE&fire=22D3EE&currStreakLabel=22D3EE&sideLabels=8B949E&dates=8B949E" alt="GitHub streak" />
</p>

## 贡献 · Contribution

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/alicefw1/alicefw1/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/alicefw1/alicefw1/output/github-contribution-grid-snake.svg" />
    <img alt="GitHub contribution grid snake animation" src="https://raw.githubusercontent.com/alicefw1/alicefw1/output/github-contribution-grid-snake.svg" width="100%" />
  </picture>
</p>

<p align="center">
  <img src="assets/rule.png" width="100%" alt="" />
</p>

## 联系 · Contact

- **GitHub** — [@alicefw1](https://github.com/alicefw1)
- **Email** — [wanyi_f@163.com](mailto:wanyi_f@163.com)

<p align="center">
  <sub>如果你对计算机视觉、深度学习或 AI 算法研究感兴趣，欢迎交流与合作 🤝</sub>
  <sub>Feel free to reach out for collaborations on computer vision or deep learning.</sub>
</p>

<p align="center">
  <sub>“See clearly. Learn deeply. Ship responsibly.”</sub>
  <sub>Designed &amp; built with care</sub>
</p>
