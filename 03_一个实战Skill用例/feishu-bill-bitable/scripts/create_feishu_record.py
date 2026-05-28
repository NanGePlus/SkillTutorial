# 导入未来注解（支持更灵活的类型提示）
from __future__ import annotations
# 导入命令行参数解析模块
import argparse
# 导入 json 处理模块
import json
# 导入操作系统相关功能
import os
# 导入系统级别参数与函数
import sys
# 导入日期时间处理类
from datetime import datetime
# 导入处理文件和目录路径的库
from pathlib import Path
# 导入任意类型和可选类型标注
from typing import Any, Optional
# 导入第三方 HTTP 请求库
import requests
# 导入dotenv功能，用于加载.env文件中的环境变量
from dotenv import load_dotenv



# Author:@南哥AGI研习社 (B站 or YouTube 搜索“南哥AGI研习社”)


# 获取当前脚本所在目录
_SCRIPTS_DIR = Path(__file__).resolve().parent
# 加载.env文件到环境变量中
load_dotenv(_SCRIPTS_DIR / ".env")

# 定义飞书开放平台 API 基础路径
API = "https://open.feishu.cn/open-apis"

# 定义获取 tenant_access_token 的函数
def _tenant_token(app_id: str, app_secret: str) -> str:
    # 向飞书接口POST请求，获取tenant_access_token
    r = requests.post(
        f"{API}/auth/v3/tenant_access_token/internal",
        json={"app_id": app_id, "app_secret": app_secret},
        timeout=60,
    )
    # 检查请求状态码，若有异常则抛出
    r.raise_for_status()
    # 将响应内容解析为 json
    body = r.json()
    # 检查 code 是否为 0
    if body.get("code") != 0:
        # 若不为 0，则抛出异常并输出内容
        raise RuntimeError(f"tenant_access_token: {body}")
    # 返回tenant_access_token字段的字符串形式
    return str(body["tenant_access_token"])

# 定义将日期字符串转为毫秒级时间戳的函数
def _date_to_ms(date_str: str) -> int:
    # 去除字符串首尾空格，并按"%Y-%m-%d"格式解析为datetime对象
    dt = datetime.strptime(date_str.strip(), "%Y-%m-%d")
    # 返回以毫秒为单位的UTC时间戳整数
    return int(dt.timestamp() * 1000)

# 定义将识别结果和 open_id 转化为飞书字段映射的函数
def _normalize_payment_method(value: Optional[str]) -> str:
    """归一化支付方式枚举值"""
    if value is None:
        return "其他"
    allowed = {"微信支付", "支付宝", "银行卡", "现金", "其他"}
    if value in allowed:
        return value
    # 检测具体银行信息 → 归一化为银行卡
    bank_keywords = ["银行", "信用卡", "储蓄卡", "贷记卡", "借记卡", "尾号"]
    if any(kw in value for kw in bank_keywords):
        return "银行卡"
    # 检测微信关键词
    if any(kw in value for kw in ["微信", "财付通", "零钱"]):
        return "微信支付"
    # 检测支付宝关键词
    if any(kw in value for kw in ["支付宝", "花呗", "余额宝"]):
        return "支付宝"
    # 检测现金关键词
    if any(kw in value for kw in ["现金", "收讫"]):
        return "现金"
    return "其他"


def _normalize_transaction_type(value: Optional[str]) -> str:
    """归一化交易类型枚举值"""
    if value in ("收入", "支出", "其他"):
        return value
    if value is None:
        return "其他"
    return "其他"


def _normalize_category(value: Optional[str]) -> str:
    """归一化分类枚举值"""
    allowed = {"餐饮", "交通", "购物", "娱乐", "医疗", "教育", "住房", "通讯", "旅游", "投资", "其他"}
    if value in allowed:
        return value
    return "其他"


def _normalize_confidence(value: Optional[str]) -> str:
    """归一化置信度枚举值"""
    if value in ("高", "中", "低"):
        return value
    return "低"


def recognition_to_fields(rec: dict[str, Any], open_id: Optional[str]) -> dict[str, Any]:
    # 写入前校验：payment_method 归一化
    raw_pm = rec.get("payment_method")
    pm_normalized = _normalize_payment_method(raw_pm)
    # 拒绝写入条件：归一化为"其他"且原始值包含银行信息（识别出了但无法归类）
    bank_keywords = ["银行", "信用卡", "储蓄卡", "贷记卡", "借记卡", "尾号"]
    if pm_normalized == "其他" and raw_pm is not None and any(kw in raw_pm for kw in bank_keywords):
        raise ValueError(f"支付方式无法归类：原始值「{raw_pm}」包含银行信息但无法归入枚举值")

    fields: dict[str, Any] = {
        "金额": rec["amount"],
        "货币代码": rec.get("currency") if rec.get("currency") is not None else "CNY",
        "商户名称": rec.get("merchant") if rec.get("merchant") is not None else "未知商户",
        "交易时间": rec.get("time") if rec.get("time") is not None else "暂无",
        "交易类型": _normalize_transaction_type(rec.get("transaction_type")),
        "分类": _normalize_category(rec.get("category")),
        "支付方式": pm_normalized,
        "交易备注": rec.get("description") if rec.get("description") is not None else "暂无",
        "原始OCR文本": rec.get("raw_text") if rec.get("raw_text") is not None else "暂无",
        "置信度": _normalize_confidence(rec.get("confidence")),
        "状态": "待核实",
    }
    d = rec.get("date")
    if d:
        fields["交易日期"] = _date_to_ms(str(d))
    if open_id:
        fields["录入者"] = [{"id": open_id}]
    return fields

# 脚本主函数
def main() -> None:
    # 实例化参数解析对象，并设置命令行描述
    parser = argparse.ArgumentParser(description="Create Feishu Bitable record from bill JSON.")
    # 添加参数，用于指定 JSON 文件路径，默认从标准输入读取
    parser.add_argument(
        "json_source",
        nargs="?",
        default="-",
        help="Path to JSON file, or '-' for stdin",
    )
    # 添加 open-id 参数，指定录入者 open_id，默认取环境变量
    parser.add_argument(
        "--open-id",
        dest="open_id",
        default=os.environ.get("FEISHU_SENDER_OPEN_ID"),
        help="Feishu user open_id for 录入者 column",
    )
    # 解析以上命令行参数到 args
    args = parser.parse_args()

    # 获取飞书 APP ID
    app_id = os.environ.get("FEISHU_APP_ID")
    # 获取飞书 APP Secret
    app_secret = os.environ.get("FEISHU_APP_SECRET")
    # 获取飞书多维表格的 APP Token
    app_token = os.environ.get("FEISHU_APP_TOKEN")
    # 获取飞书多维表格的 Table ID
    table_id = os.environ.get("FEISHU_TABLE_ID")
    # 检查必需环境变量，缺少则打印提示并退出
    if not all([app_id, app_secret, app_token, table_id]):
        print(
            "缺少配置：请在 feishu-bill-bitable/scripts/.env 中设置 "
            "FEISHU_APP_ID、FEISHU_APP_SECRET、FEISHU_APP_TOKEN、FEISHU_TABLE_ID，"
            "或在终端导出同名环境变量。",
            file=sys.stderr,
        )
        sys.exit(2)

    # 如果参数值是"-"，则从标准输入读取json，否则从文件读取
    raw = sys.stdin.read() if args.json_source == "-" else open(args.json_source, encoding="utf-8").read()
    # 将json文本解析成字典
    rec = json.loads(raw)

    # 如果识别code不为200或金额为None，则判定为不允许写入
    if rec.get("code") != 200 or rec.get("amount") is None:
        print("识别结果不允许写入：需要 code=200 且 amount 非 null", file=sys.stderr)
        sys.exit(1)

    # 获取tenant_access_token
    token = _tenant_token(app_id, app_secret)
    # 根据识别结果与open_id拼装表格字段
    fields = recognition_to_fields(rec, args.open_id)

    # 拼接飞书多维表格API的URL
    url = f"{API}/bitable/v1/apps/{app_token}/tables/{table_id}/records"
    # 发送POST请求，创建新记录
    r = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        json={"fields": fields},
        timeout=120,
    )
    # 解析返回内容为json
    body = r.json()
    # 若错误码不为0，输出报错信息
    if body.get("code") != 0:
        print(json.dumps(body, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

    # 获取返回数据的record_id字段
    record_id = body.get("data", {}).get("record", {}).get("record_id")
    # 如果没有获取到record_id，输出错误信息后退出
    if not record_id:
        print(json.dumps(body, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

    # 输出记录ID，作为脚本标准输出
    print(record_id)

# 检查脚本是否是主程序入口，如果是则运行main函数
if __name__ == "__main__":
    main()
