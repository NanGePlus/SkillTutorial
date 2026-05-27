---
name: create-a-skill
description: 指导编写结构规范、可被 Agent 发现与加载的 Skill。在用户要创建新 Skill、询问 SKILL.md 结构或优化既有 Skill 时使用。
version: 1.0.0
---

# 创建 Agent Skills

本 Skill 指导你编写有效的 Agent Skills。Skills 是 Markdown 文件，用于教 Agent 如何完成特定任务：按团队规范审查 PR、按偏好格式生成提交说明、查询数据库结构，或任何专项工作流。

## 开始之前：收集需求

创建 Skill 前，向用户收集以下关键信息：

1. **目的与范围**：该 Skill 应帮助完成哪类具体任务或工作流？
2. **触发场景**：Agent 应在何时应用该 Skill（用户 @ 点名、关键词、文件类型等）？
3. **领域知识**：有哪些 Agent 默认不知道、必须补充的专门信息？
4. **输出格式偏好**：是否需要固定模板、格式或风格？
5. **既有模式**：是否有可参考的示例或约定？

### 用户提供的原文

若用户给出了写入 Skill 的**确切措辞**，须在 `SKILL.md` 中**逐字使用**（用词与顺序一致）。不要改写、弱化或扩展其原文，也不要在未要求的情况下增加标题或评论。

### 从上下文推断

若有先前对话上下文，可根据讨论内容推断 Skill。也可基于对话中出现的工作流、模式或领域知识创建 Skill。

### 补充信息收集

需要澄清时，优先用**结构化多选**（若当前环境支持）；否则以对话方式询问。示例：

- 「该 Skill 是否应包含可执行脚本？」→ 是 / 否

---

## Skill 文件结构

### 目录布局

Skill 以**目录**形式存放，目录内包含 `SKILL.md`：

```
skill-name/
├── SKILL.md              # 必填 - 主要说明
└── references/              # 可选 - 辅助说明
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

### 加载与触发

作者能直接控制的是 **何时被选用**，与文件落在哪无关：


| 方式           | 作者应写什么                                                                  |
| ------------ | ----------------------------------------------------------------------- |
| **描述匹配**（常见） | 在 `description` 写清 WHAT + WHEN，含具体触发词（文件类型、任务名、用户常用说法）                  |
| **显式点名**     | 在 `description` 仍写清能力；若宿主仅支持 @ 加载，在正文开头加一句：「须用户 @ 本 skill（`name`）后再执行。」 |


不要把安装目录、扫描路径写进 Skill 正文——那是宿主配置，不是 Skill 内容。

### 必填元数据字段


| 字段            | 要求                             | 作用                     |
| ------------- | ------------------------------ | ---------------------- |
| `name`        | 最多 64 个字符，仅小写字母、数字、连字符         | Skill 的唯一标识            |
| `description` | 最多 1024 个字符（若环境有更严限制以环境为准），非空  | 帮助 Agent 判断何时应用该 Skill |
| `version`     | 遵循 `主.次.补丁` 语义化版本号（如 1.0.0），必填 | 标明该 Skill 的当前版本        |


---

## 如何写好 description

description 对 Skill **能否被找到**至关重要；在许多实现中，它是 Agent 在加载全文前**唯一可见**的 Skill 摘要。

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

