# 04 如何交付 Skill

当你把 Skill 从「自用」推向「给别人用」（团队协作、平台上架、对客户交付），问题就从“写得好不好”升级为“**怎么交付、怎么运行、怎么持续维护**”。本节聚焦最主流的两种交付路线：**交付 Skill 包（文件包）** 与 **交付 API 服务**，并给出清晰的决策指南与交付前检查清单，帮助你选对路径、少走弯路。

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
- **零基础上手OpenClaw：从零打造智能体驱动的商业自动化闭环**  
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

- **明确两条交付路线**：理解「交付 Skill 包」与「交付 API 服务」的核心逻辑、各自的前提条件与成本结构。
- **能做出交付决策**：根据目标用户/平台能力、数据合规、定制深度、运维能力等维度，快速判断该走哪条路。
- **能把交付说清楚**：能把交付物、运行方式、依赖与权限边界，用一套“对外可沟通”的说明写明白。
- **交付前自检**：掌握一份最小可用的交付检查清单（自包含性、配置与密钥、沙盒权限、稳定性与可观测、升级与兼容策略）。

---

## 交付方式概览

当准备把 Skill 推向更多平台或客户，实际有两类主流的交付方式，每种方式适用的场景和要求都大不相同：

### 1. 交付“Skill 包”（文件包）

这种方式相当于把写好的 Skill 打包，交给第三方平台去统一运行，强调“即插即用”。它的核心逻辑是：**你把“大脑”（提示词和逻辑）写好，交给平台的“身体”（运行环境）去执行**。核心特点如下：

1. **目标平台必须原生支持 Skill 机制**
  - 例如 OpenClaw 是最典型的平台：你上传一个包含 `SKILL.md` 和相关脚本文件的压缩包，平台自动识别、安装、部署和调度你的逻辑。
2. **Skill 必须做到“自包含”**
  - 逻辑、依赖、配置等都要封装在一个包里，确保在平台沙盒环境下无需依赖外部资源就能独立运行。
  - `SKILL.md` 文件极为关键，它像“说明书”+“驱动”，规定如何使用技能与如何触发执行。
3. **平台提供安全、功能完整的沙盒环境**
  - 平台需支持安装 `requirements.txt` 里声明的依赖（或其他语言依赖），同时具备安全的网络访问/读写能力。
  - 若沙盒权限受限（如不允许落盘/联网），你的技能可能部分能力无法发挥。

### 2. 交付 “API 服务”

这种方式更像是“自营店”，所有核心逻辑和数据都抓在自己手里，然后平台/客户通过标准 API 来调用服务。它的核心逻辑是：**你自己搭建一个“中央厨房”（服务器），所有复杂的烹饪过程都在你的厨房里完成，然后通过一个“外卖窗口”（API）把菜递出去**。核心要素有：

1. **拥有一台自主管理的服务器**
  - 必须有一台 7×24 不间断在线的“厨房”，云主机/家用设备均可，但需保证公网可访问和整体稳定。
2. **Skill 打包成标准 Web 服务（推荐用 FastAPI、Flask/Express 等）**
  - Web 服务负责对外开放一个 HTTP 接口，接收平台或客户发来的参数。
  - 解析参数后，按需调用本地脚本，再把结果（结构化 JSON）通过 API 返回给调用方。
  - 示例流程：监听 API → 校验入参 → 执行业务逻辑/脚本 → 返回标准 JSON 响应。
3. **自定义智能体框架和大模型调度**
  - 所有业务流程由自己设计、集成。你的 Web 服务内部，需要集成一个轻量级的智能体框架，或者你自己写逻辑来调度大模型 API。
  - 对接各种自定义客户系统（ERP、数据库等），按需定制联动逻辑，实现更高的技术壁垒和深度定制。

---

## 决策指南

- **更适合“Skill 包”（平台即插即用）场景：**
  - 想快速打磨 MVP，减少初期算法/系统运维压力。
  - 用户典型场景就在 OpenClaw 之类的平台生态圈。
  - Skill 逻辑标准化，客户不需要对接特殊内外部系统。
- **更适合“API 服务”场景：**
  - 客户业务对数据合规/安全极其敏感（如数据不能出境）。
  - 需要集成客户私有/独特系统（ERP/财务/数据库等）。
  - 想做更有技术壁垒、针对大单客户的定制与深度服务。
  - 想用自己品牌直接往外推，并构建基于接口调用量的收费体系。

---

## 交付前检查清单（建议）

不论选择哪条路线，交付前至少把下面这些问题讲清楚（写进交付说明或对外文档里），否则后续一定会反复扯皮：

- **交付物是什么**
  - Skill 包：压缩包内包含哪些文件（`SKILL.md`、脚本、`references/`、依赖清单、示例配置等）。
  - API 服务：接口文档（OpenAPI/Swagger/Markdown）、部署方式（容器/二进制/源码）、运行参数与依赖（数据库/缓存/对象存储等）。
- **配置与密钥怎么处理**
  - 明确哪些配置项必须由用户提供（API Key、数据库 DSN 等），以及推荐的注入方式（环境变量、平台密钥管理、挂载配置文件）。避免把密钥写进仓库或压缩包。
- **权限边界与限制**
  - Skill 包要写清平台沙盒权限需求（是否需要联网、是否需要落盘、是否需要调用外部 API、是否需要访问第三方服务）。
  - API 服务要写清网络边界（公网/内网/VPN）、鉴权方式（API Key/JWT/签名）与限流策略。
- **稳定性与可观测**
  - 最少要有：日志、错误码与重试策略、超时设置、关键路径告警。
- **升级与兼容策略**
  - Skill 包：版本号、变更说明、是否支持回滚。
  - API 服务：接口版本（如 `/v1`）、兼容窗口、破坏性变更如何通知。

---

## 小结

交付的关键不是“把文件发出去”，而是把 **运行环境、权限边界、配置密钥、稳定性与升级策略** 讲清楚。  
快速落地优先选 **Skill 包**（平台托管运行）；深度定制与数据掌控优先选 **API 服务**（自建运行环境）。两条路没有对错，只有是否匹配你的目标与约束。