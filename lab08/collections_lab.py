


def word_counts(text):
    counts = {}
    for raw_word in text.lower().split():
        word = raw_word.strip(".,!?;:")
        if not word:
            continue
        counts[word] = counts.get(word, 0) + 1   # паттерн накопления из теории
    return counts


def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    return sorted(set(first) & set(second))


def all_topics(first, second):
    return sorted(set(first) | set(second))


def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def category_summary_sorted(records):
    totals = totals_by_category(records)
    pairs = [(category, total) for category, total in totals.items()]
    pairs.sort(key=lambda pair: (-pair[1], pair[0]))   # -total = убывание, category = алфавит
    return pairs


def print_totals(totals):
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")


if __name__ == "__main__":
    sample = "Python, python! SQL и python."
    print("Частоты слов (по алфавиту):")
    print_word_counts(word_counts(sample))

    print()
    first = ["python", "sql", "python"]
    second = ["sql", "git"]
    print("Общие темы:", common_topics(first, second))
    print("Все темы:", all_topics(first, second))

    print()
    record = {"title": "Python", "hours": 4}
    record["hours"] = 6            # изменить существующий ключ
    record["completed"] = False    # добавить новый ключ
    print("Запись-словарь:", record)

    pair = (record["title"], record["hours"])   # кортеж из двух полей
    title, hours = pair                          # распаковка в две переменные
    print(f"Пара: {title}, {hours}")

    print()
    books = [
        {"title": "Алгебра 10 класс",         "category": "учебник",        "amount": 12},
        {"title": "Мастер и Маргарита",       "category": "художественная", "amount": 5},
        {"title": "Геометрия 7 класс",        "category": "учебник",        "amount": 9},
        {"title": "Словарь синонимов",        "category": "справочник",     "amount": 3},
        {"title": "Преступление и наказание", "category": "художественная", "amount": 7},
        {"title": "Физика 11 класс",          "category": "учебник",        "amount": 4},
    ]

    print("Сводка по категориям (алфавит):")
    print_totals(totals_by_category(books))

    print()
    print("Сводка по убыванию суммы, затем название (доп. задание):")
    for category, total in category_summary_sorted(books):
        print(f"{category}: {total}")

    print()
    wanted = input("Категория для поиска: ")
    found = titles_in_category(books, wanted)
    print(f"Названия в категории '{wanted}': {found}")