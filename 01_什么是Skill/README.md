# 01 Skill 介绍

本期视频对 **Skill** 的定位、能力和上手路径做概览，便于大家在编写或接入 Skill 前建立整体认识。

### 本系列仓库位置

以下仓库存储我在YouTube频道和B站频道关于零基础上手 Skill 实战相关分享所有源文件，均开源免费。  

- GitHub 地址: [https://github.com/NanGePlus/SkillTutorial](https://github.com/NanGePlus/SkillTutorial)
- Gitee 地址: [https://gitee.com/NanGePlus/SkillTutorial](https://gitee.com/NanGePlus/SkillTutorial)

### 我的个人信息

- YouTube 频道(@南哥AGI研习社)：[https://www.youtube.com/channel/UChKJGiX5ddrIpJG-rBNVZ5g](https://www.youtube.com/channel/UChKJGiX5ddrIpJG-rBNVZ5g)
- B站频道(@南哥AGI研习社)：[https://space.bilibili.com/509246474](https://space.bilibili.com/509246474)
- GitHub 地址：[https://github.com/NanGePlus](https://github.com/NanGePlus)
- Gitee 地址：[https://gitee.com/NanGePlus](https://gitee.com/NanGePlus)
- 大模型代理平台: [https://nangeai.top/](https://nangeai.top/)

### 其他开源分享推荐

- **零基础上手 LangChain V1.x 实战： 学最主流 Agent 开发框架**：  
B站视频链接：[https://www.bilibili.com/video/BV17c6mBbEHv/](https://www.bilibili.com/video/BV17c6mBbEHv/)  
YouTube 视频链接：[https://www.youtube.com/playlist?list=PL8zBXedQ0ufld2C7nB28fGw9U6nTbagp1](https://www.youtube.com/playlist?list=PL8zBXedQ0ufld2C7nB28fGw9U6nTbagp1)  
GitHub 地址：[https://github.com/NanGePlus/LangChain_V1_Test](https://github.com/NanGePlus/LangChain_V1_Test)  
Gitee 地址：[https://gitee.com/NanGePlus/LangChain_V1_Test](https://gitee.com/NanGePlus/LangChain_V1_Test)       
- **零基础上手 n8n v2.x 实战：打造 n8n 驱动的自动化生产线**：  
B站视频链接：[https://www.bilibili.com/video/BV1Aq1NBYELp/](https://www.bilibili.com/video/BV1Aq1NBYELp/)  
YouTube 视频链接：[https://www.youtube.com/playlist?list=PL8zBXedQ0uflhkZBwlQNAp7H57CJFgfgV](https://www.youtube.com/playlist?list=PL8zBXedQ0uflhkZBwlQNAp7H57CJFgfgV)  
GitHub 地址：[https://github.com/NanGePlus/N8NWorkflowsTest](https://github.com/NanGePlus/N8NWorkflowsTest)  
Gitee 地址：[https://gitee.com/NanGePlus/N8NWorkflowsTest](https://gitee.com/NanGePlus/N8NWorkflowsTest)        
- **零基础上手OpenClaw系列：从零打造智能体驱动的商业自动化闭环**  
B站视频链接：[https://www.bilibili.com/video/BV1svQGBBERQ/](https://www.bilibili.com/video/BV1svQGBBERQ/)  
YouTube视频链接：[https://www.youtube.com/playlist?list=PL8zBXedQ0ufmtUvaHsSxNqZMwgb3hxsJB](https://www.youtube.com/playlist?list=PL8zBXedQ0ufmtUvaHsSxNqZMwgb3hxsJB)  
GitHub地址：[https://github.com/NanGePlus/OpenClawTutorial](https://github.com/NanGePlus/OpenClawTutorial)  
Gitee地址：[https://gitee.com/NanGePlus/OpenClawTutorial](https://gitee.com/NanGePlus/OpenClawTutorial)                  
- **2026 AI 编程 Cursor：专为提升开发生产力而设计的一款 AI 提效工具**：  
B站视频链接：[https://www.bilibili.com/video/BV1HEABzvEdo/](https://www.bilibili.com/video/BV1HEABzvEdo/)  
YouTube 视频链接：[https://www.youtube.com/playlist?list=PL8zBXedQ0ufkcPJWHVKFTFzS8yNCkfM5b](https://www.youtube.com/playlist?list=PL8zBXedQ0ufkcPJWHVKFTFzS8yNCkfM5b)       
- **更多开源项目**  
GitHub 地址：[https://github.com/NanGePlus](https://github.com/NanGePlus)  
Gitee 地址：[https://gitee.com/NanGePlus](https://gitee.com/NanGePlus)

---

## 本节目标

- **定位与边界**：把 Skill 看成「可反复点名加载、可版本化共享」的岗位级 SOP，分清它与随手写的 Markdown、与**单次对话里的提示词**各自管什么、怎么配合。
- **形态与元数据**：记住 Skill 以**目录**为单位、`SKILL.md` 必填，YAML 里 `name` / `description` 与正文各自承担什么角色，以及可选的 `references/`、`scripts/` 大致放什么。
- **渐进式披露**：理解「启动阶段只看摘要 → 匹配到任务再读完整 `SKILL.md` → 执行步骤里再按需打开脚本或参考文件」三层逻辑。
- **何时写、如何交付**：能按「是否已有现成 Skill 可复用」「同一工作流是否已稳定重复」「是否超出纯文本、需要脚本自动化」做判断；并区分 **Skill 包** 与 **API 服务** 两类交付方式。
- **是否适合自己**：对照「适合谁」，判断自己是否愿意持续打磨 `description` 与目录结构，为后续动手维护个人或项目 Skill 做准备。

---

## Skill 是什么

### 偏通俗点理解

**不要把 Skill 讲成「又写了一个 Markdown 文档」，而要讲成：你在教智能体「遇到某类任务时，按哪套流程、用哪套标准、读哪些材料」——并且这套说明可以被反复点名加载、在团队里版本化共享。**

这里有一个观念值得扭转：**把 Skill 当成「可复用的岗位手册」去写，而不是当成聊天里多贴一段字。**

大家可以想一想：新人入职会发员工手册、检查清单、示例邮件；Skill 对智能体起到的就是类似作用——**在需要时注入**它默认没有的上下文（公司 PR 规范、数据库约定、发布流程），避免每次对话从零复述。

如果只是把长篇大论堆进一个文件却不写好 `description`，智能体很难在恰当的时机「选中」这份 Skill，结果就等于白写。反过来，`description` 写清楚「做什么 + 何时用」、正文简洁分步，Skill 才会稳定被用上。

Skill 特别适合「专项、可重复、有明确触发场景」的任务：例如按团队模板审查 PR、按固定结构写提交说明、处理 PDF/表格的既定流水线。也正因为如此，有个实用经验：**不要把所有知识塞进一个巨型 Skill**；主文件宜控制在约 500 行以内，细节用 `reference/` 或 `scripts/` 做渐进式披露（智能体按需再读）。

再讲上下文成本：对话历史、用户消息、其它 Skills 都在抢同一块上下文。**Skill 正文越精炼，越像给员工「只发当天要用的那一页 SOP」**，而不是把整本百科全书每次塞进窗口。

### 偏官方点理解

**Skill** 是以 **目录** 为单位存放的一组文件，其中 `SKILL.md` 为必填：带 YAML frontmatter（至少包含 `name` 与 `description`），正文用 Markdown 写清步骤、约定与可选资源路径。

你可以把它理解成：**系统或项目把若干 Skill 的摘要（**`name` 与 `description`**）暴露给智能体 → 智能体根据任务与** `description` **判断是否点名加载 → 需要时再读完整** `SKILL.md` **乃至参考文件/脚本**。

### 关于 Skill 与对话提示词的关系

**它们不是谁替代谁，而是分层配合。**

- **Skill**：偏「某类任务的工作流与领域知识包」，像专项 SOP；靠 `description` 被智能体检索与点名。
- **单次对话里的提示词**：偏「本轮临时要求」，像口头交代；一般不版本化、也不跨会话复用。

正确预期是：**Skill 在命中场景时把步骤与材料喂饱智能体**，你在聊天里只补本轮例外即可。

### Skill 文件结构

Skill 以**目录**形式存放，目录内包含 `SKILL.md`：

```
skill-name/
├── SKILL.md              # 必填 - 主要说明
└── references/           # 可选 - 辅助说明
    ├── reference.md
    └── examples.md
└── scripts/              # 可选 - 实用脚本
    ├── validate.py
    └── helper.sh
```

### Skill 的核心运行机制：“渐进式披露”

- **启动时（元数据层）**：Agent 启动时，只加载所有可用 Skill 的名称（name）和描述（description）。
- **匹配时（SOP文档层）**：当你提出需求，Agent 判断某个 Skill 可能有用时，才会加载对应 SKILL.md 文件的完整正文，获取详细的操作指南。
- **执行时（资源文件层）**：在按照指南执行过程中，如果遇到需要使用脚本或查阅参考文档的步骤，Agent 才会去加载 `reference/` 或 `scripts/` 目录中具体文件。

### 什么时候写 Skill

- **效率优先，复用工作流，不重复造轮子**：现成的 Skill 已经能解决 80% 的问题，先用不用自己写，只是输出格式不满意先调整，不着急新写。
- **固化流程，累积工作记忆**：同一任务反复出现，输入和输出已经稳定，该写了。
- **超越纯文本，需要自动化执行**：需要精确计算、API 接口服务调用、文件批处理，再考虑加 `scripts/` 。

### 如何交付 Skill

- **Skill包**：交付的是一个“即插即用”的智能体技能。核心的逻辑是：你把“大脑”（提示词和逻辑）写好，交给平台的“身体”（运行环境）去执行。
- **API 服务**：交付的是一个“随时可调用的能力”。核心逻辑是：你自己搭建了一个“中央厨房”（服务器），所以复杂的烹饪过程都在你的厨房里完成，然后通过一个“外卖窗口”（API）把菜递出去。

---

## 适合谁

- 希望 **把重复教智能体的话术** 固化成可维护、可分享资产的个人开发者或小团队。  
- 需要 **在项目仓库里** 与同伴共享同一套「审查清单 / 发布流程 / 领域术语表」，并让智能体在相关任务时自动或显式遵循。  
- 愿意花一点时间打磨 `description` 与目录结构，以换取后续对话中更稳定、更省 token 的行为。

---

## 小结

**Skill** 是一种可版本化与可共享的专项能力包，供智能体按需加载：用 `description` 解决「何时用」**，用 `**SKILL.md` 解决「怎么做」**，用 **附属文件与脚本** 解决「细节与可重复执行」。适合希望减少重复说教、统一团队与智能体行为边界的用户。