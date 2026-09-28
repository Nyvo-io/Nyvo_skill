# 本地 Skill 总索引与出处

更新日期：2026-09-12。日常只需从这份总表查用途、文件位置、出处和维护建议。

**维护主文件：`/Users/nyvo/.codex/skills/PROVENANCE.md`。其他导出文件是本次快照，不是另一份维护主表。**

## 统计口径

- 个人 skill：**20 个不同名称、21 份目录**。`11-711-anlp-tutor` 有两份内容相同的目录，按一个能力计数。
- 个人出处：10 个有直接来源记录，10 个尚未核实 skill 自身来源；文献或产品文档链接不等同于安装出处。
- 系统 skill：磁盘有 6 个，本次会话提供其中 5 个；`review-agent` 未列入本次可用目录。
- 插件 skill：本次会话提供 12 个；插件缓存实际有 45 份 SKILL.md，其中 33 份未以对应路径列入本次可用目录。
- 安装后可见的不同能力共 **37 个**；磁盘扫描到 72 份 SKILL.md，包含重复目录、缓存版本和未提供给本次会话的条目。新装 skill 若没有立即显示，可重启 Codex。

范围：两个用户级目录、系统目录、插件缓存。不包含其他项目的专用 skill、工作区导出副本、下载的技能包或全盘历史缓存。当前可用性以这次会话提供的技能目录为准；磁盘存在不代表插件已连接或可调用。

## 统一结构与维护规则

```text
/Users/nyvo/.codex/skills/PROVENANCE.md   ← 唯一人工查阅总表
/Users/nyvo/.codex/skills/<skill>/       ← 现有个人技能
/Users/nyvo/.agents/skills/<skill>/      ← 另一个现有发现目录
/Users/nyvo/.codex/skills/.system/       ← 系统管理
/Users/nyvo/.codex/plugins/cache/        ← 插件管理
```

本次集中的是分类、用途、路径、出处和维护说明；技能本体保持独立，未搬动、合并或删除。系统与插件文件保留其原管理方式。单个 skill 的简短来源元数据仍随包保留，便于被复制或分享时溯源；完整个人清单只在本表维护。

官方文档说明 skill 是独立目录，支持符号链接目录；同名技能不会自动合并，可能同时出现在选择器中。因此不把多个 SKILL.md 拼成一个文件，也不为分类随意增加目录层级。当前文档推荐用户目录 `~/.agents/skills`；本机现有两个路径均已出现在本次技能目录中，本次保留该可观察状态。[OpenAI 官方文档](https://learn.chatgpt.com/docs/build-skills)

维护约定：新增、更新或移除 skill 时同时刷新本表对应行；已知第三方记录仓库、提交和维护者；本地改编记录直接文件、版本和哈希；未知来源写 unknown，核实前不猜作者。优先保留文件内已有的来源证据，若和总表冲突，核实后统一。

| 来源标记 | 含义 |
|---|---|
| third-party | 有明确外部仓库出处 |
| local-derived / local-custom | 有明确本地改编或创作依据；paper-reading 当前采用 local-derived |
| unknown | 尚未核实 skill 自身的来源 |
| openai-system | 本地系统目录提供 |
| plugin-managed | 由已识别的插件及版本目录提供；不据此推断原创作者 |

## 个人 Skill 完整清单

### 学习与论文（6）

| Skill | 用途 | 出处状态 | 文件入口 |
|---|---|---|---|
| `learn-anything` | 通用自适应教学、主动回忆与迁移练习 | 已记录：Astro-Han/skills，详见来源台账 | [Codex目录](/Users/nyvo/.codex/skills/learn-anything/SKILL.md) |
| `paper-reading` | 论文原文与证据核对、笔记和进度；交互精读/掌握检查配合 learn-anything，采用 Objective 收口与自由作答边界 | 已记录：本地协议 v2；2026-09-24 补充组合规则及答案折叠，详见包内出处 | [Codex目录](/Users/nyvo/.codex/skills/paper-reading/SKILL.md) |
| `course-study-tutor` | 通用课程材料学习、讲义笔记与作业准备 | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/course-study-tutor/SKILL.md) |
| `textbook-study-companion` | 教材长期学习的状态、断点与进度管理 | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/textbook-study-companion/SKILL.md) |
| `cs234-rl-tutor` | 本地 Stanford CS234 强化学习课程辅导 | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/cs234-rl-tutor/SKILL.md) |
| `11-711-anlp-tutor` | 本地 CMU 11-711 Advanced NLP 课程辅导 | unknown；未核实直接来源 | [Agents目录](/Users/nyvo/.agents/skills/11-711-anlp-tutor/SKILL.md) / [Codex目录](/Users/nyvo/.codex/skills/11-711-anlp-tutor/SKILL.md) |

### 编程、架构与协作流程（7）

| Skill | 用途 | 出处状态 | 文件入口 |
|---|---|---|---|
| `debug` | 诊断并修复错误、崩溃和性能回退 | 已记录：Astro-Han/skills；Nyvo-io fork 中有相同历史版本 | [Codex目录](/Users/nyvo/.codex/skills/debug/SKILL.md) |
| `tdd` | 行为变更的测试驱动开发 | 已记录：Astro-Han/skills；Nyvo-io fork 中有相同历史版本 | [Codex目录](/Users/nyvo/.codex/skills/tdd/SKILL.md) |
| `review-feedback` | 判断并落实已有代码审查反馈 | 已记录：Astro-Han/skills；版本晚于当前 Nyvo-io fork | [Codex目录](/Users/nyvo/.codex/skills/review-feedback/SKILL.md) |
| `shape` | 通过访谈收敛需求与关键设计选择 | 已记录：Astro-Han/skills，详见来源台账 | [Codex目录](/Users/nyvo/.codex/skills/shape/SKILL.md) |
| `wrap-up` | 处理会话遗留事项并交代最终状态 | 已记录：Astro-Han/skills；Nyvo-io fork 中有相同历史版本 | [Codex目录](/Users/nyvo/.codex/skills/wrap-up/SKILL.md) |
| `goal-writer` | 将模糊意图整理成精简、可验证的目标契约 | 已记录：Astro-Han/skills，经 Nyvo-io/skills 安装 | [Codex目录](/Users/nyvo/.codex/skills/goal-writer/SKILL.md) |
| `keel` | 设计和审查架构边界、所有权、恢复、迁移与长期治理 | 已记录：lencx/skills；Nyvo-io/Incex_skills 是 fork | [Codex目录](/Users/nyvo/.codex/skills/keel/SKILL.md) |

### Obsidian 与知识管理（4）

| Skill | 用途 | 出处状态 | 文件入口 |
|---|---|---|---|
| `obsidian-markdown` | Obsidian Markdown、双链、属性和嵌入 | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/obsidian-markdown/SKILL.md) |
| `obsidian-cli` | 通过 CLI 操作 vault、笔记和 Obsidian 插件 | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/obsidian-cli/SKILL.md) |
| `obsidian-bases` | 创建与编辑 Obsidian .base 数据视图 | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/obsidian-bases/SKILL.md) |
| `json-canvas` | 创建与编辑 .canvas 画布、节点和连线 | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/json-canvas/SKILL.md) |

### 研究与网页提取（2）

| Skill | 用途 | 出处状态 | 文件入口 |
|---|---|---|---|
| `parallel-research` | 多角度并行研究与证据交叉核对 | 已记录：Astro-Han/skills，详见来源台账 | [Codex目录](/Users/nyvo/.codex/skills/parallel-research/SKILL.md) |
| `defuddle` | 将网页提取为较干净的 Markdown | unknown；未核实直接来源 | [Codex目录](/Users/nyvo/.codex/skills/defuddle/SKILL.md) |

### 中文创作（1）

| Skill | 用途 | 出处状态 | 文件入口 |
|---|---|---|---|
| `modern-chinese-fantasy-prose` | 原创现代中国青春幻想题材的正文与场景创作 | unknown；未核实直接来源 | [Agents目录](/Users/nyvo/.agents/skills/modern-chinese-fantasy-prose/SKILL.md) |

## 已知出处台账

以下汇总所有已知个人 skill 的直接出处。本次克隆了 `Nyvo-io/skills`、其上游 `Astro-Han/skills`、`lencx/skills` 和 `Nyvo-io/Incex_skills`，并按具体历史版本核对；此前已有的验证说明仍保留。

| Skill | 来源 | 版本标识 | 原有验证记录 |
|---|---|---|---|
| `learn-anything` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/2c5d9a03ad0cfb5198e64cf720d438d917d091d2/skills/learn-anything) | `2c5d9a03ad0cfb5198e64cf720d438d917d091d2` | 旧登记表记载本地 Git blob 与该提交匹配 |
| `shape` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/ec7ae1d9798d87ff8c1da0124b6c659d2d2a4d18/skills/shape) | `ec7ae1d9798d87ff8c1da0124b6c659d2d2a4d18` | 旧登记表记载本地 Git blob 与该提交匹配 |
| `parallel-research` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/27cb141321fbe0669df92c4ec306e0df26a041f7/skills/parallel-research) | `27cb141321fbe0669df92c4ec306e0df26a041f7` | 旧登记表记载 2026-09-03 从该提交安装 |
| `paper-reading` | [本地 learning_protocol_v2.md](/Users/nyvo/paper/notes/learning_protocol_v2.md) | 协议 2.0；skill 1.0.0；初次改编源哈希 `sha256:534db3325ee46325e23c4099907ab2b1b570708a0b453f6e82f0ac5f59b2b615` | 哈希记录初次改编输入，不表示当前修订内容；2026-09-24 更新组合规则与折叠呈现 |
| `debug` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/2c0621deb03d9726a65fd7e350b7505b1e99a7cb/skills/debug) | `2c0621deb03d9726a65fd7e350b7505b1e99a7cb` | 本地 SKILL.md 与该提交逐字一致；该提交也在 Nyvo-io fork 中 |
| `tdd` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/2a5f587dd9495654aa2d42bf90eccb56de80cb00/skills/tdd) | `2a5f587dd9495654aa2d42bf90eccb56de80cb00` | 本地 SKILL.md 与该提交逐字一致；该提交也在 Nyvo-io fork 中 |
| `wrap-up` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/11d504bc2f93fd3eaeb156057f6381f8996d9e5b/skills/wrap-up) | `11d504bc2f93fd3eaeb156057f6381f8996d9e5b` | 本地 SKILL.md 与该提交逐字一致；该提交也在 Nyvo-io fork 中 |
| `review-feedback` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/b63681157a1a39f3172162d17a53bf7bfb7c525d/skills/review-feedback) | `b63681157a1a39f3172162d17a53bf7bfb7c525d` | 本地 SKILL.md 与该提交逐字一致；提交晚于当前 Nyvo-io fork HEAD |
| `goal-writer` | [Astro-Han/skills](https://github.com/Astro-Han/skills/tree/2fb6edeac2e401229a8f7b3e7188313b8d9dff6e/skills/goal-writer) | `2fb6edeac2e401229a8f7b3e7188313b8d9dff6e` | 从 [Nyvo-io/skills fork](https://github.com/Nyvo-io/skills/tree/2fb6edeac2e401229a8f7b3e7188313b8d9dff6e/skills/goal-writer) 安装；安装前检查全部文件及本地 lint 脚本 |
| `keel` | [lencx/skills](https://github.com/lencx/skills/tree/b848e124111be50a795cc961558247e7751825e2/skills/keel) | 仓库 `b848e124111be50a795cc961558247e7751825e2`；内容末次变更 `4d16c12db575242823030e7388090ec49eab9b7b` | 安装前读取全部文件；无执行脚本；[Nyvo-io/Incex_skills](https://github.com/Nyvo-io/Incex_skills) 是其 fork |

### 本次给定仓库的判断

- `Nyvo-io/awesome-agent-skills` 是 `VoltAgent/awesome-agent-skills` 的目录型 fork。它收录外部 skill 链接，不是这些 skill 的统一作者或安装源；清单自身也声明内容未经安全审计，因此没有从该列表批量安装。
- `Nyvo-io/skills` 是 `Astro-Han/skills` 的 fork。现有 `debug`、`tdd`、`wrap-up` 能在该 fork 历史中精确匹配；`learn-anything`、`shape`、`parallel-research` 属于同一上游系列；`review-feedback` 的本地版本来自 fork 当前 HEAD 之后的上游提交。
- `lencx/skills` 当前提供 `coding-protocol` 和 `keel`。本次安装 `keel`；`coding-protocol` 与现有 `debug`、`tdd`、代码执行规则重叠较多，没有安装。
- `Nyvo-io` 的其他公开仓库多数是课程、代码或资料仓库，不是可直接安装的 Agent Skill 包；本次没有把普通仓库误装成 skill。

### paper-reading 的完整来源关系

- 直接来源：nyvo 的 Paper Learning Protocol v2（2.0），由用户要求 Codex 整理成 skill，创建于 2026-09-12。维护者 nyvo。
- 上游原协议：`/Users/nyvo/paper/notes/learning_protocol.md`；SHA-256 `b2eb3a0df1b29f2f0bd83fbfa2642736cc909824221eec93b6047af6e9441b83`。更早的完整创作历史未核实。
- 评估说明：`/Users/nyvo/paper/notes/learning_protocol_review.md`；SHA-256 `275c2c25c083996413f04871d4a0e3020d9b9aa1e2fc469394bbdd038b8895c9`。
- 原协议继承 `learn-anything` 的自适应教学、主动回忆、逐步撤提示思想；该 skill 的仓库与提交见上表。
- 打包方式参考系统 `skill-creator`；笔记格式继承协议的 Obsidian 约定。运行规则已自包含，不依赖绝对来源路径持续可用。
- 随包保存的出处说明：[paper-reading/provenance.md](/Users/nyvo/.codex/skills/paper-reading/references/provenance.md)。完整出处要点已集中在本表；包内记录便于独立分享时携带。

论文协议评估引用的资料：

| 资料 | 支持的原则及限度 |
|---|---|
| [Keshav，How to Read a Paper，2016](https://read.seas.harvard.edu/cs161/2022/pdf/keshav16how.pdf) | 分层阅读；研究者实践建议 |
| [Karpicke 与 Blunt，Science，2011](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf) | 特定科学文本实验中的检索练习；不代表对本 skill 的验证 |
| [Cepeda 等，2006](https://pubmed.ncbi.nlm.nih.gov/16719566/) | 间隔与保持时间的关系；不证明固定复习日程普遍最优 |
| [Anthropic，Building effective agents，2024](https://www.anthropic.com/engineering/building-effective-agents) | 简单可组合流程与工具反馈；工程经验 |
| [Anthropic，Effective harnesses for long-running agents，2025](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | 进度持久化与跨会话恢复；原场景为软件开发 |

以上来源在前面的论文协议评估中读取，此处汇总原有记录；本次没有重新研究其内容。外部资料作者不是这个本地 skill 的作者。

### 有参考资料，但尚无 skill 自身出处

`modern-chinese-fantasy-prose` 有创作研究资料；Obsidian/JSON Canvas 技能有格式或产品文档；课程技能会引用课件与课程根目录。这些能说明内容依据，但不能据此确认 skill 的安装仓库或最初作者，故上述个人表仍标 unknown。

## 系统 Skill

| Skill | 当前会话 | 文件入口 |
|---|---|---|
| `imagegen` | 可用 | [SKILL.md](/Users/nyvo/.codex/skills/.system/imagegen/SKILL.md) |
| `openai-docs` | 可用 | [SKILL.md](/Users/nyvo/.codex/skills/.system/openai-docs/SKILL.md) |
| `plugin-creator` | 可用 | [SKILL.md](/Users/nyvo/.codex/skills/.system/plugin-creator/SKILL.md) |
| `review-agent` | 未列入当前可用目录，仅确认本地文件存在 | [SKILL.md](/Users/nyvo/.codex/skills/.system/review-agent/SKILL.md) |
| `skill-creator` | 可用 | [SKILL.md](/Users/nyvo/.codex/skills/.system/skill-creator/SKILL.md) |
| `skill-installer` | 可用 | [SKILL.md](/Users/nyvo/.codex/skills/.system/skill-installer/SKILL.md) |

## 当前可用的插件 Skill

以下名称沿用本次会话的插件命名空间；来源以插件家族、版本和实际路径记录。工具或服务是否已连接需另行确认。

| Skill | 提供来源与版本 | 文件入口 |
|---|---|---|
| `visualize:visualize` | `openai-bundled/visualize@1.0.32` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-bundled/visualize/1.0.32/skills/visualize/SKILL.md) |
| `deep-research-work:deep-research` | `openai-curated-remote/deep-research-work@0.1.15` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/deep-research-work/0.1.15/skills/deep-research/SKILL.md) |
| `plugin-management:plugin-management` | `openai-curated-remote/plugin-management@0.1.0` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/plugin-management/0.1.0/skills/plugin-management/SKILL.md) |
| `sites:sites-building` | `openai-curated-remote/sites@0.1.59` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/sites/0.1.59/skills/sites-building/SKILL.md) |
| `sites:sites-hosting` | `openai-curated-remote/sites@0.1.59` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/sites/0.1.59/skills/sites-hosting/SKILL.md) |
| `sites:sites-preview-troubleshooting` | `openai-curated-remote/sites@0.1.59` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/sites/0.1.59/skills/sites-preview-troubleshooting/SKILL.md) |
| `documents:documents` | `openai-primary-runtime/documents@26.905.11957` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-primary-runtime/documents/26.905.11957/skills/documents/SKILL.md) |
| `pdf:pdf` | `openai-primary-runtime/pdf@26.905.11957` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-primary-runtime/pdf/26.905.11957/skills/pdf/SKILL.md) |
| `presentations:Presentations` | `openai-primary-runtime/presentations@26.905.11957` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations/SKILL.md) |
| `spreadsheets:excel-live-control` | `openai-primary-runtime/spreadsheets@26.905.11957` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.905.11957/skills/excel-live-control/SKILL.md) |
| `spreadsheets:Spreadsheets` | `openai-primary-runtime/spreadsheets@26.905.11957` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-primary-runtime/spreadsheets/26.905.11957/skills/spreadsheets/SKILL.md) |
| `template-creator:template-creator` | `openai-primary-runtime/template-creator@26.905.11957` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-primary-runtime/template-creator/26.905.11957/skills/template-creator/SKILL.md) |

## 仅在磁盘确认的其他缓存条目

这些对应路径未出现在本次会话的技能目录中。可能是模板缓存、旧版本或未启用的插件，不把“缓存存在”算作已安装并可用，也未清理它们。

| 缓存 Skill | 来源与版本 | 文件入口 |
|---|---|---|
| `sites-building` | `openai-bundled/sites@0.1.70` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-bundled/sites/0.1.70/skills/sites-building/SKILL.md) |
| `sites-hosting` | `openai-bundled/sites@0.1.70` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-bundled/sites/0.1.70/skills/sites-hosting/SKILL.md) |
| `google-calendar` | `openai-curated/google-calendar@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/google-calendar/11c74d6b/skills/google-calendar/SKILL.md) |
| `google-calendar-daily-brief` | `openai-curated/google-calendar@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/google-calendar/11c74d6b/skills/google-calendar-daily-brief/SKILL.md) |
| `google-calendar-free-up-time` | `openai-curated/google-calendar@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/google-calendar/11c74d6b/skills/google-calendar-free-up-time/SKILL.md) |
| `google-calendar-group-scheduler` | `openai-curated/google-calendar@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/google-calendar/11c74d6b/skills/google-calendar-group-scheduler/SKILL.md) |
| `google-calendar-meeting-prep` | `openai-curated/google-calendar@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/google-calendar/11c74d6b/skills/google-calendar-meeting-prep/SKILL.md) |
| `slack` | `openai-curated/slack@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/slack/11c74d6b/skills/slack/SKILL.md) |
| `slack-channel-summarization` | `openai-curated/slack@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/slack/11c74d6b/skills/slack-channel-summarization/SKILL.md) |
| `slack-daily-digest` | `openai-curated/slack@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/slack/11c74d6b/skills/slack-daily-digest/SKILL.md) |
| `slack-notification-triage` | `openai-curated/slack@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/slack/11c74d6b/skills/slack-notification-triage/SKILL.md) |
| `slack-outgoing-message` | `openai-curated/slack@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/slack/11c74d6b/skills/slack-outgoing-message/SKILL.md) |
| `slack-reply-drafting` | `openai-curated/slack@11c74d6b` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated/slack/11c74d6b/skills/slack-reply-drafting/SKILL.md) |
| `artifact-template-analytics-dashboard` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-analytics-dashboard/SKILL.md) |
| `artifact-template-business-review` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-business-review/SKILL.md) |
| `artifact-template-design-report` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-design-report/SKILL.md) |
| `artifact-template-experiment-analysis` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-experiment-analysis/SKILL.md) |
| `artifact-template-financial-budget` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-financial-budget/SKILL.md) |
| `artifact-template-investment-committee-memo` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-investment-committee-memo/SKILL.md) |
| `artifact-template-legal-memorandum` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-legal-memorandum/SKILL.md) |
| `artifact-template-market-trends-report` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-market-trends-report/SKILL.md) |
| `artifact-template-minimal-letterhead` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-minimal-letterhead/SKILL.md) |
| `artifact-template-operating-calendar` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-operating-calendar/SKILL.md) |
| `artifact-template-operating-review` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-operating-review/SKILL.md) |
| `artifact-template-project-kickoff` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-project-kickoff/SKILL.md) |
| `artifact-template-project-tracker` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-project-tracker/SKILL.md) |
| `artifact-template-sales-pipeline` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-sales-pipeline/SKILL.md) |
| `artifact-template-simple-dark-mode` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-dark-mode/SKILL.md) |
| `artifact-template-simple-light-mode` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-simple-light-mode/SKILL.md) |
| `artifact-template-strategy-memorandum` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-strategy-memorandum/SKILL.md) |
| `artifact-template-system-design` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-system-design/SKILL.md) |
| `artifact-template-team-alignment` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-team-alignment/SKILL.md) |
| `artifact-template-three-statement-forecast` | `openai-curated-remote/openai-templates@0.1.1` | [SKILL.md](/Users/nyvo/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-three-statement-forecast/SKILL.md) |

## 整理意见与当前处理

1. **先统一入口。** 已将清单、分类、来源和状态集中到本文件。以后从本表查找，不需要分别翻两个目录猜来源。
2. **处理 ANLP 重复应单独做一次迁移。** 两个 `11-711-anlp-tutor` 目录经递归比较内容完全相同。本次保留原样并标记重复；以后优先保留一个主目录，明确旧引用与备份后再迁移。仅加两个软链接并不保证选择器去重。
3. **学习技能分工合理，不建议粗暴合并。** `learn-anything` 负责教学互动；`course-study-tutor` 负责通用课程；`textbook-study-companion` 负责教材长期进度；课程专用 tutor 管具体课程；`paper-reading` 管论文论证与证据。需要留意触发边界和重复指令，而不是只减少文件数量。
4. **出处未知保持未知。** 仍有 10 个个人 skill 需要通过安装历史、Git 记录或原始来源确认；不要仅凭名字相似补上一个网上仓库。
5. **保持系统和插件由原机制管理。** 不把缓存版本或所有 artifact-template 条目复制到个人目录，以免增加重复项和维护负担。
6. **新增技能统一登记。** 直接来源、来源版本、维护者、当前位置和用途至少要在本表可查；技能自身保留简短元数据与必要随包出处，避免独立拷贝后失去溯源。

本次为 7 个 Astro-Han 系列 skill 补充或扩展了来源元数据，安装了 `goal-writer` 与 `keel`，为两个新 skill 增加简介、调用元数据与 MIT 许可证副本，并更新总表。没有修改这些来源 skill 的运行正文，也没有修改论文文件或其他未知来源 skill。当前清单是 2026-09-12 的快照，不声称实时自动更新。
