# 零基础上手 Skill：从 0 到交付的全链路闭环实战

## 本系列视频定位

本系列按 **认知 → 编写 → 实战 → 交付闭环** 串起一条可走完的路径：

**认知** 建立 Skill 的定位与运行机制（`01_什么是Skill`）；

**编写** 系统讲清需求澄清、`description`、`SKILL.md` 结构、渐进式披露与避坑（`02_如何高质量写出Skill`）；

**实战** 用飞书 + Skill 搭建智能记账助手，覆盖图片/文本识别、校验与写入（`03_一个实战Skill用例`）；

**交付** 理清 Skill 包 vs API 两条主流路线与交付前检查清单（`04_如何去交付Skill`），并在 `04_如何去交付Skill/交付Skill包指南.md` 中以 OpenClaw 为例把「安装/注册 Skill 包」跑通闭环。

仓库中的 **05_Skills合集** 汇总可直接拷贝或打包交付的 Skill 工程，便于对照文档快速验证与二次分发。后续会持续补更多可复用的交付案例与模板。

### 仓库目录速览


| 目录                | 说明                                              |
| ----------------- | ----------------------------------------------- |
| `01_什么是Skill`     | Skill 概念、组成与运行逻辑                                |
| `02_如何高质量写出Skill` | 高质量编写方法论与自检                                     |
| `03_一个实战Skill用例`  | 飞书记账助手：从配置到跑通全流程                                |
| `04_如何去交付Skill`   | 交付决策、检查清单；子文件 `交付Skill包指南.md` 为 OpenClaw 安装注册实操 |
| `05_Skill合集`      | 成品 Skill 包                                      |


### 本系列仓库位置

以下仓库存储我在 YouTube 和 B 站频道关于「零基础上手 Skill 实战」相关分享的全部源文件，均开源免费。

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
- **零基础上手 OpenClaw 实战：从零打造智能体驱动的商业自动化闭环**  
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

## 本系列视频链接地址速查

**【整体介绍】零基础上手 Skill：从 0 到交付的全链路闭环实战。本系列按 认知 → 编写 → 实战 → 交付闭环 串起一条可走完的路径。源文件均开源免费。**      
YouTube频道对应视频: https://youtu.be/2FUWZ4jCc2U  
B站频道对应视频: https://www.bilibili.com/video/BV1TNGZ6uEGQ/  

---

## 适合的小伙伴

- 希望 **把重复教智能体的话术** 固化成可维护、可分享资产的个人开发者或小团队。  
- 需要 **在项目仓库里** 与同伴共享同一套「审查清单 / 发布流程 / 领域术语表」，并让智能体在相关任务时自动或显式遵循。  
- 愿意花一点时间打磨 `description` 与目录结构，以换取后续对话中更稳定、更省 token 的行为。

---

## 学完后你能做什么


| 能力域                     | 对应章节              | 能力描述                                                                                                                                                                                                                             |
| ----------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **整体认知**                | `01_什么是Skill`     | （1）建立对 Skill 的整体理解：它不是普通文档，而是可被智能体反复加载、可版本化复用的 SOP。（2）理解 Skill 的基本组成与运行逻辑：目录 + `SKILL.md`、`name/description` 的分工、以及“渐进式披露”的加载方式。（3）分清 Skill 与单次对话提示词的边界与协作方式，知道什么时候该写 Skill、什么时候只需临时指令。（4）为后续写 Skill、做实战、谈交付打好方法论基础。             |
| **高质量写作**               | `02_如何高质量写出Skill` | （1）会在动笔前做需求澄清：目的、触发场景、输出格式、领域知识、既有模式与约束。（2）能写出“找得到”的 `description`：第三人称、含触发词、WHAT + WHEN。（3）能把 `SKILL.md` 写得“读得懂、可执行”：简洁优先、篇幅控制、分层引用、按任务脆弱度设定自由度。（4）能套用模板/示例/工作流/分支/反馈闭环等写作模式，必要时配合脚本，并避开常见反面模式。（5）能按「澄清→设计→实现→验证」流程打磨，并用总结清单自检。 |
| **实战开发**                | `03_一个实战Skill用例`  | （1）能把一个真实业务场景落成可运行的 Skill（飞书多维表格记账助手）。（2）掌握图片/文本两条输入链路的结构化抽取方式，并用校验门禁保证“可写入才写入”。（3）会组织 Skill 目录：主文件 + `references/`（提示词/字段映射）+ `scripts/`（写入、上传票根等），把复杂度拆开、便于维护。（4）具备把“示例跑通”迁移到其它同类场景的能力（换 prompt/字段映射/脚本即可复用）。                  |
| **交付决策**                | `04_如何去交付Skill`   | （1）理解两条主流交付路线：交付 **Skill 包（文件包）** vs 交付 **API 服务**，知道各自的前提条件、成本结构与适用场景。（2）能根据平台能力、数据合规、定制深度、运维能力快速做选择。（3）能把交付物、运行方式、依赖、权限边界、配置与密钥、安全与稳定性、升级兼容策略写成对外可沟通的交付说明。（4）具备一套交付前检查清单，减少“交付后返工”。                                            |
| **交付实操（以 OpenClaw 为例）** | `04_如何去交付Skill`   | （1）能把 Skill 以“Skill 包”的方式交付给支持平台，并完成安装/注册/启用。（2）知道平台侧常见的权限与沙盒限制点，能根据约束调整依赖与实现。（3）能用最小闭环验证交付是否成功：安装识别→触发运行→输出可用→异常可定位。（4）为后续把 Skill 推向更多平台或客户，建立一条可复用的交付路径。                                                                       |
| **成品 Skill 与扩展案例**      | `05_Skill合集`      | 直接获取仓库内维护的 Skill 工程                                                                                                                                                                                                              |


---

## 学习建议

1. **顺序尽量不打乱**：建议按 `01 → 02 → 03 → 04` 学。`04` 的交付决策建立在你已经跑通一个真实 Skill（`03`）的基础上；需要上 OpenClaw 时，再跟做 `04_如何去交付Skill/交付Skill包指南.md`。需要直接拿可运行包时，对照 `05_Skills合集` 各子目录说明操作。
2. **先跑通再优化**：先把示例按文档跑通，再回头优化 `description`、工作流与脚本；别一上来就追求“写得很完美”。
3. **密钥与合规**：飞书写入、上传票根、对外 API 与浏览器自动化很多是不可撤销/可审计的；重要操作先做预览与最小权限授权。不要把 API Key、token 写进 `SKILL.md`、`references/` 或仓库里（含 `.env`）。
4. **把排错沉淀成资产**：每次踩坑都记录「现象 → 日志关键词/错误码 → 根因 → 修复步骤」，并回写到 `references/` 或脚本的使用说明里；下次交付或迁移环境会省很多时间。

