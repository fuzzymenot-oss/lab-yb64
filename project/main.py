import sys
from pathlib import Path

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
)
from storage import load_records, save_records

UNIT = "стр."


def get_data_path():
    """data.json рядом со скриптом."""
    return Path(__file__).resolve().parent / "data.json"


def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Значение не может быть пустым")


def input_non_negative_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if value < 0:
            print("Количество страниц не может быть отрицательным")
            continue
        if raw.lower() in ("true", "false"):
            print("Нужно ввести целое число")
            continue
        return value


def input_positive_int(prompt):
    """Целое число > 0 для ID."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Нужно ввести целое число")
            continue
        if value <= 0:
            print("ID должен быть положительным числом")
            continue
        return value


def action_show(records):
    if not records:
        print("Нет записей")
        return
    print()
    for r in sorted(records, key=lambda x: x["id"]):
        status = "прочитана" if r["completed"] else "не прочитана"
        print(f"[{r['id']}] {r['title']} | {r['category']} | "
              f"{r['amount']} {UNIT} | {status}")
    print()


def action_add(records):
    title = input_non_empty("Название книги: ")
    category = input_non_empty("Категория (жанр/раздел): ")
    amount = input_non_negative_int(f"Количество ({UNIT}): ")
    record = add_record(records, title, category, amount)
    print(f"Добавлена книга с ID {record['id']}")


def action_find(records):
    try:
        query = input_non_empty("Поиск по названию: ")
    except ValueError as err:
        print(err)
        return
    try:
        found = find_records(records, query)
    except ValueError as err:
        print(err)
        return
    if not found:
        print("Ничего не найдено")
        return
    print()
    for r in sorted(found, key=lambda x: x["id"]):
        status = "прочитана" if r["completed"] else "не прочитана"
        print(f"[{r['id']}] {r['title']} | {r['category']} | "
              f"{r['amount']} {UNIT} | {status}")
    print()


def action_set_status(records):
    record_id = input_positive_int("ID книги: ")
    print("Выберите новый статус:")
    print("  1 — прочитана")
    print("  2 — не прочитана")
    choice = input("Ваш выбор (1 или 2): ").strip()
    if choice == "1":
        new_status = True
    elif choice == "2":
        new_status = False
    else:
        print("Неизвестная команда, статус не изменён")
        return
    if set_completed(records, record_id, new_status):
        label = "прочитана" if new_status else "не прочитана"
        print(f"Статус книги с ID {record_id}: {label}")
    else:
        print(f"Книга с ID {record_id} не найдена")


def action_delete(records):
    record_id = input_positive_int("ID книги для удаления: ")
    target = next((r for r in records if r["id"] == record_id), None)
    if target is None:
        print(f"Книга с ID {record_id} не найдена")
        return
    print(f"Удалить «{target['title']}» (ID {record_id})? Введите «да» для подтверждения.")
    answer = input("Ваш ответ: ").strip().lower()
    if answer == "да":
        if delete_record(records, record_id):
            print("Запись удалена")
        else:
            print("Не удалось удалить запись")
    else:
        print("Удаление отменено")


def action_statistics(records):
    s = statistics(records)
    print()
    print(f"Всего книг: {s['total']}")
    print(f"Прочитано: {s['done']}")
    print(f"Не прочитано: {s['not_done']}")
    print(f"Всего страниц: {s['total_amount']}")
    print("Страниц по категориям:")
    for cat in sorted(s["by_category"]):
        print(f"  {cat}: {s['by_category'][cat]}")
    print()


def action_save(path, records):
    try:
        save_records(path, records)
        print("Данные сохранены")
        return True
    except OSError as err:
        print(f"Не удалось сохранить файл: {err}")
        return False
    except ValueError as err:
        print(f"Нельзя сохранить: {err}")
        return False


MENU = """
=== Список книг для чтения ===
1 — Показать книги
2 — Добавить книгу
3 — Найти книгу
4 — Изменить статус
5 — Удалить книгу
6 — Статистика
7 — Сохранить
8 — Выйти
"""
def run_menu(records, path):
    while True:
        print(MENU)
        choice = input("Ваш выбор (1-8): ").strip()

        if choice == "1":
            action_show(records)
        elif choice == "2":
            action_add(records)
        elif choice == "3":
            action_find(records)
        elif choice == "4":
            action_set_status(records)
        elif choice == "5":
            action_delete(records)
        elif choice == "6":
            action_statistics(records)
        elif choice == "7":
            action_save(path, records)
        elif choice == "8":
            # Предложить сохранить
            while True:
                answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
                if answer == "да":
                    ok = action_save(path, records)
                    if not ok:
                        print("Сохранение не удалось — остаёмся в меню")
                        break   # вернуться в меню, не выходя
                    return       # выход
                elif answer == "нет":
                    return       # выход без сохранения
                else:
                    print("Введите «да» или «нет»")
        else:
            print("Неизвестная команда. Выберите пункт меню от 1 до 8.")

def main():
    path = get_data_path()

    if not path.exists():
        print(f"Файл {path.name} не найден. Начинаем с пустого списка.")
        records = []
    else:
        try:
            records = load_records(path)
            print(f"Загружено записей: {len(records)}")
        except FileNotFoundError:
            print("Файл исчез перед чтением. Завершение.")
            sys.exit(1)
        except UnicodeError:
            print("Файл имеет неправильную кодировку (ожидается UTF-8). Завершение без перезаписи.")
            sys.exit(1)
        except ValueError as err:
            print(f"Структура файла нарушена: {err}")
            print("Завершение. Файл НЕ перезаписан — исправьте его вручную.")
            sys.exit(1)
        except Exception as err:
            print(f"Не удалось прочитать файл: {err}")
            print("Завершение. Файл НЕ перезаписан.")
            sys.exit(1)

    run_menu(records, path)


if __name__ == "__main__":
    main()