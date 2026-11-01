"""任务持久化：把待办列表存到 tasks.json。"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks() -> list[dict]:
    """从 tasks.json 读取任务；文件不存在或损坏时返回空列表。"""
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks: list[dict]) -> None:
    """把任务写回 tasks.json（中文不转义，方便直接看）。"""
    DATA_FILE.write_text(
        json.dumps(tasks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
