# 出处与改编说明

## 直接出处

本 skill 是用户 nyvo 于 2026-09-12 明确要求，将本地第二版论文学习协议整理为 `paper-reading` 后，由 Codex 编写的本地改编。不是从某个公开仓库直接安装，也不把下列参考文献作者列为此 skill 的作者。

| 项目 | 来源 |
|---|---|
| 直接改编文本 | `/Users/nyvo/paper/notes/learning_protocol_v2.md`，Paper Learning Protocol v2，版本 2.0 |
| 直接来源 SHA-256 | `534db3325ee46325e23c4099907ab2b1b570708a0b453f6e82f0ac5f59b2b615` |
| 上游协议 | `/Users/nyvo/paper/notes/learning_protocol.md`，用户既有本地协议；其更早完整创作历史未核实 |
| 上游 SHA-256 | `b2eb3a0df1b29f2f0bd83fbfa2642736cc909824221eec93b6047af6e9441b83` |
| 评估及改写依据 | `/Users/nyvo/paper/notes/learning_protocol_review.md`，2026-09-12 |
| 评估文件 SHA-256 | `275c2c25c083996413f04871d4a0e3020d9b9aa1e2fc469394bbdd038b8895c9` |
| 本 skill 版本 | 1.0.0；本地维护者 nyvo；用户级安装 |

这些路径和哈希用于追溯初次改编的输入，不代表后续本地修订的文件哈希。来源文件以后改变不会自动更新已安装 skill，也不会自动迁移历史论文进度。当前组合规则见 SKILL.md 的 Adaptive Teaching。

## 继承的思想与相关本地来源

原协议明确说明以 `learn-anything` 的自适应教学、主动回忆和逐步撤提示为基础。本地 `/Users/nyvo/.codex/skills/learn-anything/SKILL.md` 的出处元数据记录：

- 上游维护者：Astro-Han。
- 上游地址：[Astro-Han/skills — learn-anything](https://github.com/Astro-Han/skills/tree/main/skills/learn-anything)。
- 本地记录的来源提交：`2c5d9a03ad0cfb5198e64cf720d438d917d091d2`。

初次改编仅继承教学原则。2026-09-24 按用户确认的分工，交互精读与掌握检查改为读取并配合 `learn-anything`，提问形式、Objective 收口和跨会话回忆以 paper-reading 的组合边界为准；不可用时有最小教学回退。未修改 learn-anything 的独立运行规则。提交信息来自本地元数据，未重新核验远程仓库。

skill 的组织方式参考本地 `/Users/nyvo/.codex/skills/.system/skill-creator/SKILL.md`：明确触发范围，主文件保留核心规则，模板与条件性细节按需加载。公式、笔记与附件约定继承 v2 使用的 Obsidian Markdown 风格；这些格式约定不构成外部工具依赖。

## 第二版评估采用的公开资料

以下出处在前一轮协议评估中检索、阅读并记录。本次打包保留引用，不声称又进行了一次独立研究：

1. **S. Keshav，How to Read a Paper，2016 修订版。** 分层阅读、先建立全局理解再深入。属于实践建议，不能直接证明 agent 教学效果。[论文原文的高校镜像](https://read.seas.harvard.edu/cs161/2022/pdf/keshav16how.pdf)
2. **Jeffrey D. Karpicke、Janell R. Blunt，Science，2011。** *Retrieval Practice Produces More Learning than Elaborative Studying with Concept Mapping*。为检索练习提供特定科学文本实验依据，不保证任意论文教学的效果。[作者实验室保存的原文](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf)
3. **Nicholas J. Cepeda 等，Psychological Bulletin，2006。** *Distributed practice in verbal recall tasks: A review and quantitative synthesis*。支持根据保持目标考虑间隔复习，不推出固定日程普遍最优。[摘要与 DOI](https://pubmed.ncbi.nlm.nih.gov/16719566/)
4. **Anthropic，Building effective agents，2024-12-19。** 简洁可组合的流程、工具反馈与按效果调整复杂度。[作者工程文章](https://www.anthropic.com/engineering/building-effective-agents)
5. **Anthropic，Effective harnesses for long-running agents，2025-11-26。** 进度持久化、增量工作和避免过早完成判断。原案例为软件开发，在此借用恢复原则。[作者工程文章](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

上述资料分别支持部分原则，不构成对本 skill 的整体有效性验证；本地工作流应根据来源错误、遗漏、恢复成本、独立迁移与延迟回忆表现持续调整。

## 从协议到 Skill 的改编

- 将第二版的常用约束、任务模式、教学循环、一次保存检查和完成条件提炼到 `SKILL.md`。
- 将进度模板、格式及恢复细节放入 `state-and-notes.md`；证据类型、图表公式和核对细则放入 `source-and-evidence.md`。
- 显式调用 skill 即可选择这套流程；自动匹配不覆盖已有论文选定的协议。去掉对原绝对路径的运行依赖。
- 局部提问与只审查笔记不强制建立整套课程；保留中文与双语术语、单份动态笔记、来源追溯和内容/掌握分离。

保持出处元数据诚实：本地来源用文件路径与哈希，不伪造 GitHub 地址、提交、许可证或作者身份。将来从其他来源修改时补充相应出处，不把历史参考资料误称为新增代码的直接来源。
