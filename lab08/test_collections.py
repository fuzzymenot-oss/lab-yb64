from collections_lab import (
    word_counts,
    common_topics, all_topics,
    totals_by_category, titles_in_category,
    category_summary_sorted,
)

assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}

first = ["python", "sql", "python"]
second = ["sql", "git"]
assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python", "sql"]
# один из списков пуст (ТЗ: пересечение пусто, объединение = уникальные другого)
assert common_topics([], second) == []
assert all_topics([], second) == ["git", "sql"]
assert common_topics(first, []) == []
assert all_topics(first, []) == ["python", "sql"]

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
snapshot = [record.copy() for record in records]
assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}
assert titles_in_category([], "основное") == []
assert records == snapshot            # исходные записи не изменены

books = [
    {"title": "Алгебра 10 класс",         "category": "учебник",        "amount": 12},
    {"title": "Мастер и Маргарита",       "category": "художественная", "amount": 5},
    {"title": "Геометрия 7 класс",        "category": "учебник",        "amount": 9},
    {"title": "Словарь синонимов",        "category": "справочник",     "amount": 3},
    {"title": "Преступление и наказание", "category": "художественная", "amount": 7},
    {"title": "Физика 11 класс",          "category": "учебник",        "amount": 4},
]
books_snapshot = [record.copy() for record in books]
assert totals_by_category(books) == {"учебник": 25, "художественная": 12, "справочник": 3}
assert titles_in_category(books, "учебник") == ["Алгебра 10 класс", "Геометрия 7 класс", "Физика 11 класс"]
assert titles_in_category(books, "справочник") == ["Словарь синонимов"]
assert titles_in_category(books, "несуществующая") == []
assert books == books_snapshot
assert category_summary_sorted(books) == [("учебник", 25), ("художественная", 12), ("справочник", 3)]

print("Все проверки collections пройдены")