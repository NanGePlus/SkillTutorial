# 飞书 + Skill 搭建智能记账助手（图片识别 + 文本识别自动录入）

## 功能介绍

通过 Skill 实现智能记账：用户与 Agent 聊天，发送账单**图片**（微信支付截图、支付宝截图、发票拍照等）或直接输入账单**文本**（支付通知、银行短信、手动描述等），AI 自动识别内容，提取金额、商户、日期等信息，自动录入飞书多维表格；图片链路还会将原始账单图片作为**票根**一并保存至表格记录中。

- **图片识别链路**：图片 → 结构化识别 JSON → 校验 → 写入多维表格 → 上传票根并更新记录。
- **文本识别链路**：文本 → 结构化识别 JSON → 校验 → 写入多维表格。

关键约束：仅当识别 JSON 满足 `code === 200` 且 `amount` 非 null 时才允许写入。

在体验本期应用案例之前，建议先参考如下这期案例的分享。两者实现的功能完全一致，只是采用了不同的技术实现方案：

```
7x24小时在线的私人数字员工：飞书+n8n+AI=你的「效率特种兵」，同样的架构，换Prompt，搞定N个场景。拖拽搭建｜产品/运营/自由职业者的效率外挂
- YouTube频道对应视频: [https://youtu.be/mu1E7UC0HXc](https://youtu.be/mu1E7UC0HXc)              
- B站频道对应视频: [https://www.bilibili.com/video/BV1eaokBDEv8/](https://www.bilibili.com/video/BV1eaokBDEv8/) 
```

---

## 本 Skill 范围

```
用户账单图片/文本
  ↓
按 Prompt 生成结构化 JSON（只输出 JSON）
  ↓
写入前校验：code=200 && amount≠null
  ├─ 否：解释失败原因（不写入）
  └─ 是：
      ↓
  在 feishu-bill-bitable/ 下仅调用：
  ./.venv/bin/python scripts/create_feishu_record.py <识别 JSON 路径>
      └─（仅图片链路）./.venv/bin/python scripts/upload_receipt_image.py ...
```

---

## 本 Skill 文件结构

```
feishu-bill-bitable/
├── SKILL.md                          # 技能主文件
├── references/                       # 引用文档目录
│   ├── bill-image-structured-recognition-prompt_v1.0.md      # 图片识别 prompt
│   ├── bill-text-structured-recognition-prompt_v1.0.md       # 文本识别 prompt
│   └── field-bitable-column-mapping.md                       # 字段映射表
└── scripts/
    ├── requirements.txt              # 依赖包
    ├── .env                          # 本地环境变量
    ├── create_feishu_record.py       # 写入记录
    └── upload_receipt_image.py       # 上传票根并更新记录
```

---

## 前置准备

### 1. 环境要求

- **Python**：3.11+
- **网络**：可访问 `open.feishu.cn`
- **识别模型**：图片链路需要视觉能力，且能严格按 Prompt **只输出 JSON**

### 2. 需要准备的资源

- 飞书个人或企业账号（可创建自建应用）

---

## 第一部分：飞书应用配置

### 步骤 1：创建企业自建应用

1. 访问 [飞书开放平台](https://open.feishu.cn/app)
2. 点击「创建企业自建应用」
3. 填写应用信息：
  - **应用名称**：智能记账助手
  - **应用描述**：发送账单图片或文本，AI 自动识别并录入记账
  - **图标**：可上传一个记账相关的图标
4. 点击「确定创建」

### 步骤 2：开通权限

进入「权限管理」页面，开通以下权限（权限类型：应用身份）：

**必须开通（核心权限）：**

```
bitable:app                   # 查看、评论、编辑和管理多维表格
base:record:create            # 新增记录
```

开通方式：

1. 在搜索框中搜索权限名称（如 `base:record:create`）
2. 选中后点击「确认开通」
3. 确认开通，重复以上步骤直到全部开通

### 步骤 3：发布应用

1. 进入「版本管理与发布」页面
2. 点击「创建版本」
3. 填写版本信息：
  - **版本号**：1.0.0
  - **更新说明**：初始版本
4. 点击「保存」
5. 点击「申请发布」→「确认申请」
6. 联系企业管理员审核通过

### 步骤 4：创建飞书多维表格

详情请参考 **多维表格配置说明.md** 文件内具体描述

---

## 第二部分：本 Skill 参数配置

### 步骤 1：创建项目虚拟环境

在技能根目录 `feishu-bill-bitable/` 下**只**使用本目录内的 `.venv`，所有脚本与 Agent 代为执行的 Python 命令均通过 `./.venv/bin/python` 调用；**不要**使用系统 `python` / `python3`、Anaconda 自带环境或其他路径下的解释器。

在 `feishu-bill-bitable/` 目录中执行：

```bash
cd feishu-bill-bitable
python3 -m venv .venv

./.venv/bin/python -m pip install -U pip
./.venv/bin/python -m pip install -r scripts/requirements.txt
```

### 步骤 1（续）：CLI 使用方式

在 `feishu-bill-bitable/` 目录下，所有写入与票根操作**默认**为直接调用 venv 内的 Python 脚本：

```bash
./.venv/bin/python scripts/create_feishu_record.py <识别JSON文件路径>
./.venv/bin/python scripts/upload_receipt_image.py --record-id <record_id> --image <票根图片绝对路径>
```

### 步骤 2：配置环境变量

在技能根目录下的 `scripts/.env` 中设置以下变量（**不含** Python 解释器路径；解释器固定为技能根目录 `./.venv/bin/python`）：

- `FEISHU_APP_ID`：飞书平台自建应用的 APP_ID
- `FEISHU_APP_SECRET`：飞书平台自建应用的 APP_SECRET
- `FEISHU_APP_TOKEN`：飞书平台多维表格 URL 中 `/base/` 后面的那段
- `FEISHU_TABLE_ID`：飞书平台多维表格 URL 中 `table=` 后面的表 ID
- `FEISHU_SENDER_OPEN_ID`：写入飞书用户即录入者 `OPEN_ID`

安全提醒：**不要**把 Secret 提交到 Git。

举例如下所示：

```
FEISHU_APP_ID="cli_a964a62c11e11bd2"
FEISHU_APP_SECRET="Kd2jKjAgGZoeJUCgj5E8oeq5OVtY2XBw"
FEISHU_APP_TOKEN="GSnEb7T6yaQJmMsnkERcvorcnTf"
FEISHU_TABLE_ID="tblSCCbSto54R6Vd"
FEISHU_SENDER_OPEN_ID="ou_26aa2ae05c8706c7e31b335fea110d3f"  
```

---

## 第三部分：测试验证

### 步骤 1：工作目录与解释器

- **工作目录**：必须为 `feishu-bill-bitable`，以便 `scripts` 与包路径正确。
- **解释器**：默认使用 `./.venv/bin/python` 调用 CLI，勿用未装依赖的系统 Python。

### 步骤 2：常用 CLI 示例

1. 在 `scripts` 目录下手动创建一个 `recognition.json` 文件，内容需确保 `code=200` 且 `amount` 字段有值，例如：
  ```json
    {
      "code": 200,
      "amount": -10.9,
      "currency": "CNY",
      "merchant": "自测-瑞幸咖啡",
      "date": "2026-05-09",
      "time": "16:03",
      "transaction_type": "支出",
      "category": "餐饮",
      "payment_method": "微信支付",
      "description": "脚本自测写入",
      "raw_text": "selftest",
      "confidence": "高"
    }
  ```
2. 在技能根目录 `feishu-bill-bitable/` 下，依次执行以下命令完成自测：
  ```bash
    cd feishu-bill-bitable
    ./.venv/bin/python scripts/create_feishu_record.py scripts/recognition.json
    ./.venv/bin/python scripts/upload_receipt_image.py --record-id "recvjA4mgWITzv" --image "scripts/test.png"
  ```

> 注意：`record-id` 替换为上一步创建记录后返回的实际 ID，`image` 参数为待上传的票根图片文件路径

### 步骤 3：作为 AI Agent 技能使用

#### 图片链路识别测试

1. 与 Agent 聊天，发送一张微信支付或支付宝截图
2. Agent 按照 Skill 进行处理
3. 处理完成后返回录入的明细消息
4. 打开多维表格，确认新记录已写入，且「票根」字段已附上原始账单图片

#### 文本链路识别测试

1. 与 Agent 聊天，直接发送账单文本，如：`瑞幸咖啡 -¥38.5 2026-04-24 09:32 微信支付 生椰拿铁`
2. Agent 按照 Skill 进行处理
3. 处理完成后返回录入的明细消息
4. 打开多维表格，确认新记录已写入

**验证数据准确性：**

- 金额是否正确（支出为负数）
- 商户名称是否正确
- 日期格式是否为 `YYYY-MM-DD`
- 分类和支付方式是否准确
- 图片链路是否成功保存「票根」附件

