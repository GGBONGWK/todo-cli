"""todo-cli：一个用来练习 Git 与 GitHub 的命令行待办工具。"""

import sys

# 暂存在内存里，程序一退出就没了（第 4 步用分支来做持久化）
TASKS: list[dict] = []


def add_task(title: str) -> None:
    TASKS.append({"title": title, "done": False})
    print(f"已添加：{title}（当前共 {len(TASKS)} 条）")


def list_tasks() -> None:
    if not TASKS:
        print("还没有任务。用 python todo.py add <内容> 添加。")
        return
    for index, task in enumerate(TASKS, start=1):
        mark = "x" if task["done"] else " "
        print(f"{index}. [{mark}] {task['title']}")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("用法：python todo.py add <内容> | list")
        return 1

    command = argv[1]

    if command == "add":
        if len(argv) < 3:
            print("请提供任务内容，例如：python todo.py add 买牛奶")
            return 1
        add_task(" ".join(argv[2:]))
        return 0

    if command == "list":
        list_tasks()
        return 0

    print(f"未知命令：{command}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
