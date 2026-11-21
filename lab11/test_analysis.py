import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import (
    validate_todos,
    completion_counts,
    top_users,
    leader_task_ids,
    select_tasks,
    task_ids,
)

TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

snapshot = [record.copy() for record in TODOS]
validate_todos(TODOS)
assert completion_counts(TODOS) == {5: 2, 10: 2}
assert top_users(completion_counts(TODOS)) == [5, 10]
assert leader_task_ids(TODOS, [5, 10]) == [1, 3, 4, 5]
assert task_ids(select_tasks(TODOS, 5)) == [1, 5]      # вариант 2
assert TODOS == snapshot                                # записи не изменены
print("Учебный набор пройден")

assert completion_counts([]) == {}
assert top_users({}) == []
assert select_tasks([], 5) == []
only_false = [
    {"id": 1, "userId": 5, "title": "А", "completed": False},
    {"id": 2, "userId": 5, "title": "Б", "completed": False},
]
assert completion_counts(only_false) == {5: 0}
assert top_users(completion_counts(only_false)) == []   # максимум 0
assert select_tasks(only_false, 5) == []
print("Пустой и полностью незавершённый наборы пройдены")

single = [
    {"id": 1, "userId": 5, "title": "А", "completed": True},
    {"id": 2, "userId": 10, "title": "Б", "completed": False},
]
assert top_users(completion_counts(single)) == [5]
tie = [
    {"id": 1, "userId": 7, "title": "А", "completed": True},
    {"id": 2, "userId": 9, "title": "Б", "completed": True},
]
assert top_users(completion_counts(tie)) == [7, 9]
print("Лидеры пройдены")

# ---- вариант 2: неизвестный пользователь и набор без совпадений ----
assert select_tasks(TODOS, 999) == []
no_done = [{"id": 1, "userId": 5, "title": "А", "completed": False}]
assert select_tasks(no_done, 5) == []
print("Вариант 2: краевые случаи пройдены")

def expect_value_error(data, label):
    try:
        validate_todos(data)
    except ValueError:
        return
    assert False, f"Ошибка не обнаружена: {label}"

expect_value_error({"id": 1}, "вместо списка объект")
expect_value_error([
    {"id": 1, "userId": 5, "title": "А", "completed": True},
    {"id": 1, "userId": 6, "title": "Б", "completed": False},
], "повторный id")
expect_value_error([{"id": 1, "title": "А", "completed": True}], "отсутствует userId")
expect_value_error([{"id": 1, "userId": 5, "title": "А", "completed": "false"}], "completed строкой")
expect_value_error([{"id": True, "userId": 5, "title": "А", "completed": True}], "id логический")

extra = [{"id": 1, "userId": 5, "title": "А", "completed": True, "note": "x"}]
assert validate_todos(extra) == extra
print("Ошибки структуры пройдены")

# ---- запись и повторное чтение JSON ----
with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    selected = select_tasks(TODOS, 5)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(selected, file, ensure_ascii=False, indent=2)
    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)
    assert restored == selected
print("JSON-цикл пройден")

print("Все проверки analysis пройдены")