import json
from pathlib import Path

from analysis import (
    validate_todos,
    completion_counts,
    top_users,
    leader_task_ids,
    select_tasks,
    task_ids,
)


def read_positive_integer(prompt):
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if value <= 0:
            print("Должно быть больше нуля")
            continue
        return value


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "todos.json"
    leaders_path = folder / "leaders.json"
    selected_path = folder / "selected.json"

    try:
        with open(source, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл не найден: {source}")
        return
    except json.JSONDecodeError as error:   # подкласс ValueError — раньше общего
        print(f"Файл не является корректным JSON: {error}")
        return
    except UnicodeError:
        print("Ошибка кодировки: файл должен быть в UTF-8")
        return
    except ValueError as error:             # общий обработчик ошибок данных
        print(f"Ошибка данных: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа: {error}")
        return

    # Проверка структуры отдельно от синтаксиса JSON.
    try:
        todos = validate_todos(data)
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)
    leader_ids = leader_task_ids(todos, leaders)

    user_id = read_positive_integer("Введите идентификатор пользователя: ")
    selected = select_tasks(todos, user_id)

    # Запись результатов ТОЛЬКО после успешной проверки входа.
    try:
        with open(leaders_path, "w", encoding="utf-8") as file:
            json.dump(leader_ids, file, ensure_ascii=False, indent=2)
        with open(selected_path, "w", encoding="utf-8") as file:
            json.dump(selected, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Не удалось сохранить результаты: {error}")
        return

    print("Завершённые задачи по пользователям:")
    for user in sorted(counts):
        print(f"  пользователь {user}: {counts[user]}")
    print(f"Лидеры: {leaders}")
    print(f"Завершённые задачи лидеров: {leader_ids}")
    print(f"Выборка варианта для пользователя {user_id}: {task_ids(selected)}")
    print("Результаты сохранены: leaders.json, selected.json")


if __name__ == "__main__":
    main()