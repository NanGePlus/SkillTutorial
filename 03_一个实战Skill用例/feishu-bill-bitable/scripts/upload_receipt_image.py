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
# 导入处理文件和目录路径的库
from pathlib import Path
# 导入第三方 HTTP 请求库
import requests
# 导入 dotenv 功能，用于加载 .env 文件中的环境变量
from dotenv import load_dotenv



# Author:@南哥AGI研习社 (B站 or YouTube 搜索“南哥AGI研习社”)


# 获取当前脚本所在目录
_SCRIPTS_DIR = Path(__file__).resolve().parent
# 加载 .env 文件到环境变量中
load_dotenv(_SCRIPTS_DIR / ".env")

# 定义飞书开放平台 API 基础路径
API = "https://open.feishu.cn/open-apis"

# 定义获取 tenant_access_token 的函数
def _tenant_token(app_id: str, app_secret: str) -> str:
    # 向飞书接口 POST 请求，获取 tenant_access_token
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
    # 返回 tenant_access_token 字段的字符串形式
    return str(body["tenant_access_token"])

# 定义上传本地图片到飞书云盘（多维表格素材）并返回 file_token 的函数
def _upload_all(token: str, app_token: str, file_path: str) -> str:
    # 读取本地文件字节长度，供上传参数 size 使用
    size = os.path.getsize(file_path)
    # 取文件名，作为上传时的展示名
    name = os.path.basename(file_path)
    # 上传挂载父节点：可用环境变量覆盖，默认同多维表格 app_token
    parent_node = os.environ.get("FEISHU_BITABLE_UPLOAD_PARENT_NODE", app_token)
    # 云盘素材一次性上传接口
    url = f"{API}/drive/v1/medias/upload_all"
    # 以 multipart 形式上传文件流
    with open(file_path, "rb") as f:
        files = {"file": (name, f, "application/octet-stream")}
        data = {
            "file_name": name,
            "parent_type": "bitable_image",
            "parent_node": parent_node,
            "size": str(size),
        }
        r = requests.post(
            url,
            headers={"Authorization": f"Bearer {token}"},
            files=files,
            data=data,
            timeout=300,
        )
    # 解析上传结果
    body = r.json()
    # 业务错误则抛出，附带完整响应便于排查
    if body.get("code") != 0:
        raise RuntimeError(json.dumps(body, ensure_ascii=False))
    # 从 data 中取出 file_token
    ft = body.get("data", {}).get("file_token")
    if not ft:
        raise RuntimeError(json.dumps(body, ensure_ascii=False))
    # 返回字符串形式的 file_token，供写入附件字段
    return str(ft)

# 定义更新指定记录、写入附件列（票根）的函数
def _update_record(
    token: str,
    app_token: str,
    table_id: str,
    record_id: str,
    field_name: str,
    file_token: str,
) -> None:
    # 多维表格单条记录更新接口 URL
    url = f"{API}/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}"
    # PUT 请求，仅更新附件字段：值为 file_token 列表
    r = requests.put(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8",
        },
        json={"fields": {field_name: [{"file_token": file_token}]}},
        timeout=120,
    )
    body = r.json()
    # 若飞书返回 code 非 0，抛出异常由上层统一处理
    if body.get("code") != 0:
        raise RuntimeError(json.dumps(body, ensure_ascii=False))

# 脚本主函数
def main() -> None:
    # 实例化参数解析对象，并设置命令行描述
    parser = argparse.ArgumentParser(description="Upload receipt image and attach to Bitable record.")
    # 指定要挂载票根的多维表格记录 ID（通常来自 create_feishu_record.py 的输出）
    parser.add_argument("--record-id", required=True, help="record_id from create_feishu_record.py")
    # 指定本地账单/票根图片路径
    parser.add_argument("--image", required=True, help="Path to receipt image file")
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
    # 附件列显示名，默认「票根」，可通过 FEISHU_RECEIPT_FIELD 覆盖
    field_name = os.environ.get("FEISHU_RECEIPT_FIELD", "票根")
    # 检查必需环境变量，缺少则打印提示并退出
    if not all([app_id, app_secret, app_token, table_id]):
        print(
            "缺少配置：请在 feishu-bill-bitable/scripts/.env 中设置 "
            "FEISHU_APP_ID、FEISHU_APP_SECRET、FEISHU_APP_TOKEN、FEISHU_TABLE_ID，"
            "或在终端导出同名环境变量。",
            file=sys.stderr,
        )
        sys.exit(2)

    # 确认图片路径存在且为文件，避免无效上传
    if not os.path.isfile(args.image):
        print(f"文件不存在: {args.image}", file=sys.stderr)
        sys.exit(1)

    # 获取 tenant_access_token
    token = _tenant_token(app_id, app_secret)
    try:
        # 上传图片，得到 file_token
        file_token = _upload_all(token, app_token, args.image)
        # 将 file_token 写入指定记录的附件列
        _update_record(token, app_token, table_id, args.record_id, field_name, file_token)
    except RuntimeError as e:
        # 上传或更新失败时，将错误信息输出到 stderr 并以非 0 退出
        print(str(e), file=sys.stderr)
        sys.exit(1)

    # 成功时在标准输出打印固定标记，便于脚本链判断
    print("ok")

# 检查脚本是否是主程序入口，如果是则运行 main 函数
if __name__ == "__main__":
    main()
