# 02 如何高质量写出 Skill

本期内容聚焦 **如何把 Skill 写清楚、写好用**：从动笔前该收集哪些信息，到 `description` 与 `SKILL.md` 的结构、篇幅与渐进式披露，再到常见写作模式、脚本配合、反面模式与定稿自检。Skill 本质上是 Markdown 说明，用于教智能体按你的规范完成专项任务（例如按团队规范审查 PR、按固定格式写提交说明、查询库表约定等）。

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
- **零基础上手 OpenClaw：从零打造智能体驱动的商业自动化闭环**         
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

- **动笔前：对齐需求**：会用六类问题框定目的与范围、存放位置、触发场景、领域知识、输出格式与既有模式，避免一上来就堆正文。
- **结构与元数据**：能搭好 Skill 目录（`SKILL.md` 必填，可选 `references/`、`scripts/`），会为`SKILL.md` 写好 YAML frontmatter，并掌握 `name`、`description` 的格式与长度要求。
- **可发现性：`description`**：会按第三人称、具体触发词、WHAT + WHEN 撰写描述，并能对照文中的 YAML 示例举一反三。
- **正文与篇幅**：能落实「简洁优先、主文件约 500 行内、渐进式披露、引用不宜过深、按任务脆弱度设定自由度」等原则，把 token 用在刀刃上。
- **写法与脚本**：能按场景选用模板、示例、工作流、条件分支、反馈闭环等模式；知道何时引入脚本、如何在正文里写清路径、调用方式、依赖，以及「执行」与「仅阅读参考」的区别。
- **避坑与定稿**：能识别路径、选项堆砌、强时效表述、术语漂移、命名含糊等反面模式；能按澄清 → 设计 → 实现 → 验证四阶段推进，并对照总结清单自检；最后能读懂「完整示例」的结构，并判断自己是否属于「适合谁」所描述的那类作者。

---

## 开始之前：收集需求

创建 Skill 前，建议先对齐以下信息：

1. **目的与范围**：该 Skill 应帮助完成哪类具体任务或工作流？
2. **触发场景**：智能体应在何时应用该 Skill（自动或点名）？
3. **领域知识**：有哪些智能体默认不知道、必须补充的专门信息？
4. **输出格式偏好**：是否需要固定模板、格式或风格？
5. **既有模式**：是否有可参考的示例或约定？

---

## Skill 文件结构

### 目录布局

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

### SKILL.md 结构

每个 Skill 都需要带 YAML 头信息（frontmatter）与 Markdown 正文的 `SKILL.md`：

```markdown
---
name: your-skill-name
description: 简要说明该 Skill 做什么、何时使用
version: 1.0.0
---

# 你的 Skill 名称

## 说明
面向 Agent 的清晰分步指引。

## 示例
使用该 Skill 的具体示例。
```

通用 Skill 以 `name`、`description` 与 `version` 为准。

### 必填元数据字段


| 字段            | 要求                             | 作用                     |
| ------------- | ------------------------------ | ---------------------- |
| `name`        | 最多 64 个字符，仅小写字母、数字、连字符         | Skill 的唯一标识            |
| `description` | 最多 1024 个字符（若环境有更严限制以环境为准），非空  | 帮助 Agent 判断何时应用该 Skill |
| `version`     | 遵循 `主.次.补丁` 语义化版本号（如 1.0.0），必填 | 标明该 Skill 的当前版本        |


---

## 如何写好 description

在 `description` 中写清 WHAT + WHEN，含具体触发词，对 Skill **能否被找到**至关重要。它是 Agent 在加载全文前**唯一可见**的 Skill 摘要。

### description 最佳实践

1. **使用第三人称**（description 常注入系统或路由提示）：
  - ✅ 好：「处理 Excel 文件并生成报表」
  - ❌ 避免：「我可以帮你处理 Excel」
  - ❌ 避免：「你可以用这个来处理 Excel」
2. **具体，并包含触发词**：
  - ✅ 好：「从 PDF 提取文本与表格、填写表单、合并文档。在处理 PDF 或用户提到 PDF、表单、文档提取时使用。」
  - ❌ 含糊：「帮助处理文档」
3. **同时说明 WHAT 与 WHEN**：
  - WHAT：Skill 做什么（具体能力）
  - WHEN：Agent 应在何时使用（触发场景）

### description 示例

```yaml
# PDF 处理
description: 从 PDF 提取文本与表格、填写表单、合并文档。在处理 PDF 或用户提到 PDF、表单、文档提取时使用。

# Excel 分析
description: 分析 Excel 表格、创建数据透视表、生成图表。在分析 Excel、电子表格、表格数据或 .xlsx 文件时使用。

# Git 提交信息助手
description: 通过分析 git diff 生成描述清晰的提交说明。在用户需要撰写提交信息或查看已暂存改动时使用。

# 代码审查
description: 按团队规范审查代码质量、安全与最佳实践。在审查 PR、代码改动或用户请求代码审查时使用。
```

---

## 核心编写原则

### 1. 简洁优先

上下文窗口要与对话历史、其他 Skills 和当前请求共享，每个 token 都在竞争空间。

**默认假设**：Agent 已经足够聪明，只补充它**尚不具备**的上下文。

对每条信息自问：

- 「Agent 真的需要这段解释吗？」
- 「能否默认 Agent 已经知道？」
- 「这段话是否值得占用这些 token？」

**好（简洁）**：

```markdown
## 提取 PDF 文本

文本提取使用 pdfplumber：

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

**差（冗长）**：

```markdown
## 提取 PDF 文本

PDF（便携式文档格式）是一种常见格式，可包含文本、图像等内容。
要从 PDF 提取文本需要使用库。市面上有很多 PDF 库，我们推荐 pdfplumber，
因为它简单易用且能覆盖大多数场景……
```

### 2. 保持 SKILL.md 在 500 行以内

为获得更好效果，主文件 `SKILL.md` 应精炼；详细内容用渐进式披露放到其他文件。

### 3. 渐进式披露

把必备信息放在 `SKILL.md`；详细参考资料放在单独文件中，仅在需要时由 Agent 读取。

```markdown
# PDF 处理

## 快速开始
[核心步骤写在这里]

## 更多资料
- 完整 API 说明见 [reference.md](reference.md)
- 使用示例见 [examples.md](examples.md)
```

**引用保持一层**：从 `SKILL.md` 直接链到参考文件。嵌套过深可能导致只读到部分内容。

### 4. 设定合适的自由度

根据任务「脆弱程度」决定写得有多死：


| 自由度           | 适用情况         | 示例     |
| ------------- | ------------ | ------ |
| **高**（文字说明）   | 多种可行做法、依赖上下文 | 代码审查准则 |
| **中**（伪代码/模板） | 有首选模式但允许变通   | 报表生成   |
| **低**（具体脚本）   | 操作脆弱、一致性极重要  | 数据库迁移  |


---

## 常见模式

### 1. 模板模式

提供固定输出骨架（如报告章节、表格字段、回复结构等），让智能体按模板填空而不是自由发挥。  
**举例：**

```markdown
## 报告结构

使用以下模板：

# [分析标题]

## 执行摘要
[一段话概括主要结论]

## 主要发现
- 发现 1（附数据或依据）
- 发现 2（附数据或依据）

## 建议
1. 可执行的具体建议
2. 可执行的具体建议
```

### 2. 示例模式

若输出质量依赖「看过例子」，在正文中给出成对的「输入 / 期望输出」片段（如提交信息、邮件、JSON 片段等），示例越贴近真实越好。  
**举例：**

```markdown
## 提交信息格式

**示例 1：**
输入：新增基于 JWT 的用户认证
输出：
feat(auth): implement JWT-based authentication
Add login endpoint and token validation middleware

**示例 2：**
输入：修复日期显示错误
输出：
fix(reports): correct date formatting in timezone conversion
Use UTC timestamps consistently across report generation
```

### 3. 工作流模式

把复杂操作拆成带编号的步骤，并附可复制勾选的进度清单；需要跑脚本时在对应步骤写出命令与期望产物。  
**举例：**

```markdown
## 表单填写工作流

任务进度：

- 步骤 1：分析表单
- 步骤 2：建立字段映射
- 步骤 3：校验映射
- 步骤 4：填写表单
- 步骤 5：核对输出

**步骤 1：分析表单**
运行：`python scripts/analyze_form.py input.pdf`
...
```

### 4. 条件分支工作流

在决策点写清「若 A 则走分支 1，若 B 则走分支 2」，避免智能体在中间状态猜下一步。  
**举例：**

```markdown
## 文档修改工作流

1. 判断修改类型：

   **新建内容？** → 按下方「创建工作流」
   **编辑已有内容？** → 按下方「编辑工作流」

2. 创建工作流：
   - 使用 docx-js
   - 从零构建文档
   ...
```

### 5. 反馈闭环模式

对质量敏感的任务，在步骤中嵌入「完成 → 校验命令 → 失败则修复再校验 → 通过后继续」，把「必须通过校验」写死为门禁。  
**举例：**

```markdown
## 文档编辑流程

1. 完成编辑
2. **立即校验**：`python scripts/validate.py output/`
3. 若校验失败：
   - 阅读报错
   - 修复问题
   - 再次运行校验
4. **仅在校验通过后**继续后续步骤
```

---

## 实用脚本

预制脚本相对「现场生成的代码」的优势：

- 比生成代码更可靠
- 节省 token（不必把大段代码放进上下文）
- 节省时间（无需生成代码）
- 多次使用保持一致

```markdown
## 实用脚本

**analyze_form.py**：从 PDF 提取所有表单字段
```bash
python scripts/analyze_form.py input.pdf > fields.json
```

**validate.py**：检查错误

```bash
python scripts/validate.py fields.json
# 返回："OK" 或列出冲突
```

```

须写清 Agent 应**执行**脚本（最常见）还是仅**阅读**脚本作参考。

---

## 应避免的反面模式

### 1. Windows 风格路径

- ✅ 使用：`scripts/helper.py`
- ❌ 避免：`scripts\helper.py`

### 2. 选项过多

```markdown
# 差 - 令人困惑
「你可以用 pypdf、pdfplumber、PyMuPDF……」

# 好 - 给默认方案与例外
「文本提取默认用 pdfplumber。
扫描版 PDF 需要 OCR 时，改用 pdf2image + pytesseract。」
```

### 3. 强时间敏感信息

```markdown
# 差 - 容易过时
「若在 2025 年 8 月前操作，请用旧版 API。」

# 好 - 使用「旧模式」区块
## 当前做法
使用 v2 API 端点。

## 旧模式（已废弃）
<details>
<summary>遗留 v1 API</summary>
...
</details>
```

### 4. 术语不一致

全文统一用词：

- ✅ 始终用「API 端点」（不要混用「URL」「路由」「路径」）
- ✅ 始终用「字段」（不要混用「框」「元素」「控件」）

### 5. Skill 名称含糊

- ✅ 好：`processing-pdfs`、`analyzing-spreadsheets`
- ❌ 避免：`helper`、`utils`、`tools`

### 6. 绑定单一宿主

- ❌ 避免：正文大段写「仅在某某 IDE 中点击……」
- ✅ 好：用「若环境提供 X 工具则……，否则用对话/脚本……」

---

## Skill 创建工作流

协助用户创建 Skill 时，按以下阶段进行：

### 阶段 1：澄清需求

收集：

1. Skill 目的与主要使用场景
2. 触发场景（@ 点名、关键词、文件类型等）
3. 特殊要求或约束
4. 需遵循的现有示例或模式

用结构化多选（若支持）或对话完成收集。

### 阶段 2：设计

1. 拟定 Skill 名称（小写、连字符、最多 64 字符）
2. 撰写具体、第三人称的 description
3. 列出正文主要章节
4. 判断是否需要配套文件或脚本

### 阶段 3：实现

1. 创建 Skill 目录结构
2. 编写带 frontmatter 的 `SKILL.md`
3. 编写必要的参考文件
4. 按需添加实用脚本

### 阶段 4：验证

1. 确认 `SKILL.md` 少于 500 行
2. 确认 description 具体且含触发词
3. 全文术语一致
4. 文件引用仅一层
5. 确认在典型用法下能被正确触发（显式点名或 description 匹配）

---

## 完整示例

结构良好的 Skill 示例：

**目录结构：**

```
code-review/
├── SKILL.md          
└── references/          
    ├── STANDARDS.md
    └── examples.md
```

**SKILL.md：**

```markdown
---
name: code-review
description: 按团队规范审查代码质量、安全性与可维护性。在审查 PR、查看代码改动或用户请求代码审查时使用。
version: 1.0.0
---

# Code Review

## Quick Start

审查代码时：

1. 检查正确性与潜在缺陷
2. 核对安全最佳实践
3. 评估可读性与可维护性
4. 确认测试充分

## Review Checklist

- [ ] 逻辑正确且覆盖边界情况
- [ ] 无严重安全问题（SQL 注入、XSS 等）
- [ ] 符合项目代码风格
- [ ] 函数粒度与职责合适
- [ ] 错误处理完整
- [ ] 测试覆盖本次改动

## Providing Feedback

反馈格式：
- 🔴 **Critical**：合并前必须修复
- 🟡 **Suggestion**：建议改进
- 🟢 **Nice to have**：可选优化

## Additional Resources

- 详细编码规范见 references/STANDARDS.md
- 审查示例见 references/examples.md
```

---

## 总结清单

定稿前请核对：

### 核心质量

- description 具体且含关键词
- description 同时说明 WHAT 与 WHEN
- 第三人称表述
- SKILL.md 正文少于 500 行
- 术语全文一致
- 示例具体，非抽象描述

### 结构

- 文件引用仅一层
- 渐进式披露使用得当
- 工作流步骤清晰
- 无易过时的强时间敏感表述
- 正文未绑定单一宿主/厂商操作（见「绑定单一宿主」反面模式）

### 若包含脚本

- 脚本真正解决问题，而非敷衍推脱
- 已说明依赖包
- 错误处理明确、有用
- 无 Windows 风格路径

---

## 适合谁

- 已了解 Skill 的基本概念，准备**自己写**或**与团队共建** Skill 的开发者。  
- 需要把「审查规范、发布流程、领域术语」等沉淀成**可发现、可复用**说明，而不是每次在对话里重讲一遍。  
- 愿意在 `description` 与目录结构上多花一点时间，换后续对话更稳定、更省 token 的人。

---

## 小结

高质量 Skill 的要点可以压缩为三句话：用 `description` 解决「何时找得到」，用 `SKILL.md` 解决「一步步怎么做」，用 参考文件与脚本 解决「细节与可重复执行」；中间再用「简洁、分层引用、反面模式自检」把质量兜住。按「澄清 → 设计 → 实现 → 验证」走一遍，并对照总结清单过稿，一版 Skill 就可以长期服役。
