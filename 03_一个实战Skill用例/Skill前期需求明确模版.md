## 收集需求

### （1）目的与范围

**（该 Skill 应帮助完成哪类具体任务或工作流？）**

具体任务：

用户与记账助手聊天，发送账单**图片**（微信支付截图、支付宝截图、发票拍照等）或直接输入账单**文本**（支付通知、银行短信、手动描述等），AI 自动识别内容，提取金额、商户、日期等信息，自动录入飞书多维表格；图片链路还会将原始账单图片作为**票根**一并保存至表格记录中。

具体工作流：

```markdown
1. 判断用户上传的内容类型：
   **若是图片？** → 按下方「图片理解链路」
   **若是纯本文？** → 按下方「纯文本理解链路」

2. 图片理解链路：
   - 识别：严格使用 `references/bill-image-structured-recognition-prompt_v1.0.md` 进行识别和输出
   - 映射：严格使用 `references/field-bitable-column-mapping.md` 进行字段和多维表格列进行映射 
   - 写入：使用脚本 create_feishu_record.py 调用飞书接口新建记录。在技能根目录 feishu-bill-bitable/ 下执行 `./.venv/bin/python scripts/create_feishu_record.py <JSON路径>`（与小红书 Skills 一致：直接 venv python + scripts）
   - 票根：使用脚本 upload_receipt_image.py 调用飞书接口完成图片的上传并更新记录。`./.venv/bin/python scripts/upload_receipt_image.py --record-id ... --image ...`
   - 反馈：回复用户是否录入成功；成功时可复述关键字段（金额、商户、日期）

3. 纯文本理解链路：
   - 识别：严格使用 `references/bill-text-structured-recognition-prompt_v1.0.md` 进行识别和输出
   - 映射：严格使用 `references/field-bitable-column-mapping.md` 进行字段和多维表格列进行映射 
   - 写入：使用脚本 create_feishu_record.py 调用飞书接口新建记录。在技能根目录 feishu-bill-bitable/ 下执行 `./.venv/bin/python scripts/create_feishu_record.py <JSON路径>`
   - 反馈：回复用户是否录入成功；成功时可复述关键字段（金额、商户、日期）
```

### （2）存放位置

**（放在个人 Skill（**`~/.cursor/skills/`**）还是项目 Skill（**`.cursor/skills/`**）？）**

项目 Skill（`.cursor/skills/`）

### （3）触发场景

**（Agent 应在何时自动应用该 Skill？）**

```markdown
@ 本技能名 或明示需进行记账识别录入飞书多维表格（如“帮我录入账单”、“识别并记账到多维表格”等），支持高准确率的字段抽取、标准化映射、表格自动写入与票根归档，适用于个人、团队多样记账管理需求。
```

### （4）领域知识

**（有哪些 Agent 默认不知道、必须补充的专门信息？）**

脚本需要使用的相关接口文档：

- 获取飞书应用 Token：[https://open.feishu.cn/document/server-docs/authentication-management/access-token/tenant_access_token_internal](https://open.feishu.cn/document/server-docs/authentication-management/access-token/tenant_access_token_internal)
- 新增多维表格记录：[https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/create](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/create)
- 更新多维表格记录（保存票根）：[https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/update](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-table-record/update)
- 上传素材：[https://open.feishu.cn/document/server-docs/drive-v1/media/multipart-upload-media/upload_prepare](https://open.feishu.cn/document/server-docs/docs/drive-v1/media/multipart-upload-media/upload_prepare)

### （5）输出格式偏好

**（是否需要固定模板、格式或风格？）**

暂无（建议在测试中增加）

### （6）既有模式

**（是否有可参考的示例或约定？）**

暂无（建议在测试中增加）

