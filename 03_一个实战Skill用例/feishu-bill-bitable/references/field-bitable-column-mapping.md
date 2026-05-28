# 字段与多维表格列映射

识别阶段输出的 JSON 键名与多维表格**列显示名**对应关系如下；`create_feishu_record.py` 按此构建 `fields`。**录入者**来自调用脚本时传入的用户标识，不在识别 JSON 内。


| JSON 字段            | 多维表格列名    | 说明                                        |
| ------------------ | --------- | ----------------------------------------- |
| `amount`           | `金额`      | 数字；支出为负、收入为正                              |
| `currency`         | `货币代码`    | 文本；识别为 `null` 时脚本默认 `CNY`                 |
| `merchant`         | `商户名称`    | 文本；识别为 `null` 时脚本默认 `未知商户`                |
| `date`             | `交易日期`    | 日期；`YYYY-MM-DD` 转为当日 00:00（本地时区）的毫秒时间戳写入  |
| `time`             | `交易时间`    | 文本；识别为 `null` 时脚本默认 `暂无`                  |
| `transaction_type` | `交易类型`    | 单选：`收入` / `支出` / `其他`；`null` 时默认 `其他`     |
| `category`         | `分类`      | 单选；须与表中选项一致；`null` 时默认 `其他`               |
| `payment_method`   | `支付方式`    | 单选；`null` 时默认 `其他`                        |
| `description`      | `交易备注`    | 文本；`null` 时默认 `暂无`                        |
| `raw_text`         | `原始OCR文本` | 文本；`null` 时默认 `暂无`                        |
| `confidence`       | `置信度`     | 单选：`高` / `中` / `低`；`null` 时默认 `低`         |
| （固定）               | `状态`      | 固定写入 `待核实`                                |
| `--open-id`        | `录入者`     | 人员类型：脚本写入 `[{"id": "<open_id>"}]`；未传则省略该列 |


**票根（仅图片链路）**：列名默认 `票根`，类型为附件；由 `upload_receipt_image.py` 上传素材后写入 `[{"file_token": "<token>"}]`。

## 写入前校验（枚举归一化）

在调用 `create_feishu_record.py` 写入多维表格之前，需对以下枚举字段做合法性校验与归一化。

### 枚举约束一览


| 字段                 | 有效枚举值                                                  | 归一化规则                                           | 校验失败处理                 |
| ------------------ | ------------------------------------------------------ | ----------------------------------------------- | ---------------------- |
| `payment_method`   | `微信支付`、`支付宝`、`银行卡`、`现金`、`其他`                           | 检测到具体银行名称/卡号信息（如"江苏银行信用卡"、"尾号3645"）→ 归一化为 `银行卡` | 值不在枚举中且无法归一化 → 拒绝写入，报错 |
| `transaction_type` | `收入`、`支出`、`其他`                                         | 检测到"退款"相关关键词 → `收入`；"红包发出"、"转账"等 → `支出`         | 值不在枚举中 → 归一化为 `其他`     |
| `category`         | `餐饮`、`交通`、`购物`、`娱乐`、`医疗`、`教育`、`住房`、`通讯`、`旅游`、`投资`、`其他` | 值不在枚举中 → `其他`                                   | 值不在枚举中 → `其他`          |
| `confidence`       | `高`、`中`、`低`                                            | 值不在枚举中 → `低`                                    | 值不在枚举中 → `低`           |


### payment_method 归一化细则

```python
# 归一化逻辑（伪代码）
def normalize_payment_method(value: str) -> str:
    if value in ("微信支付", "支付宝", "银行卡", "现金", "其他"):
        return value
    # 检测具体银行信息 → 归一化为银行卡
    bank_keywords = ["银行", "信用卡", "储蓄卡", "贷记卡", "借记卡", "尾号"]
    if any(kw in value for kw in bank_keywords):
        return "银行卡"
    # 检测微信绿色系关键词
    if any(kw in value for kw in ["微信", "财付通", "零钱"]):
        return "微信支付"
    # 检测支付宝蓝色系关键词
    if any(kw in value for kw in ["支付宝", "花呗", "余额宝"]):
        return "支付宝"
    # 检测现金关键词
    if any(kw in value for kw in ["现金", "收讫"]):
        return "现金"
    # 无法归类 → 其他
    return "其他"
```

### 校验流程

1. **读取识别 JSON**（`code` 须为 `200` 且 `amount` 非 null）
2. **枚举归一化**：对 `payment_method`、`transaction_type`、`category`、`confidence` 按上表归一化
3. **payment_method 特殊校验**：若归一化结果为 `其他`，且原始值明显包含银行信息但未被归一化，应触发报错拒绝写入（而不是默认放行）
4. **写入**：归一化后的 fields 传入 `create_feishu_record.py`

### 拒绝写入条件

满足以下任一条件时，打印原因并以退出码 `1` 终止，**不调用写入脚本**：

- `code ≠ 200` 或 `amount is None`（识别失败）
- `payment_method` 归一化后为 `其他`，且原始值包含银行名称/卡号等明确支付方式信息（说明识别出了支付方式但无法归类）

---

## 环境变量（脚本共用）

脚本启动时只会自动读取 `**scripts/.env`**（与 `create_feishu_record.py` 同级目录）。若终端已 `export` 同名变量，**以终端为准**（`.env` 不会覆盖已有环境变量）。

建议在 `scripts/.env` 中填写：

```env
FEISHU_APP_ID="cli_a964a62c11e11bd2"
FEISHU_APP_SECRET="9UOpx8gYQnFFqkPyVsPPkbbWwTPnnZjr"
FEISHU_APP_TOKEN="GSnEb7T6yaQJmMsnkERcvorcnTf"
FEISHU_TABLE_ID="tblSCCbSto54R6Vd"
FEISHU_SENDER_OPEN_ID="ou_26aa2ae05c8706c7e31b335fea110d3f"  
```

勿将 `scripts/.env` 提交到版本库。


| 变量                      | 说明                                   |
| ----------------------- | ------------------------------------ |
| `FEISHU_APP_ID`         | 自建应用 App ID                          |
| `FEISHU_APP_SECRET`     | 自建应用 App Secret                      |
| `FEISHU_APP_TOKEN`      | 多维表格 `app_token`（URL 中 `/base/` 后一段） |
| `FEISHU_TABLE_ID`       | 数据表 `table_id`                       |
| `FEISHU_SENDER_OPEN_ID` | 可选；未传 `--open-id` 时作为录入者             |


