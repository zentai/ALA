import os
import json
from datetime import datetime

# ========= CONFIG =========
BASE_PATH = "/Users/zen/Downloads/minimart/"
INPUT_FILE = "input.json"  # 你放 JSON array 的地方
# ==========================


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def parse_date_path(timestamp):
    dt = datetime.fromisoformat(timestamp)
    return dt.strftime("%Y/%m/%d")


def main():
    # 读取 input JSON
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        raw_id = item["raw_id"]
        timestamp = item["timestamp"]

        # 生成 folder path
        date_path = parse_date_path(timestamp)
        full_dir = os.path.join(BASE_PATH, date_path)

        ensure_dir(full_dir)

        # 生成 file path
        file_path = os.path.join(full_dir, f"{raw_id}.json")

        # 写入（避免覆盖可以加判断）
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)

        print(f"[SAVED] {file_path}")


if __name__ == "__main__":
    main()
