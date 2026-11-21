from logic import (
    add_record,
    delete_record,
    find_records,
    next_id,
    set_completed,
    statistics,
    validate_records,
)


def make_book(rid, title, category, amount, completed):
    return {
        "id": rid, "title": title, "category": category,
        "amount": amount, "completed": completed,
    }


SAMPLE = [
    make_book(1, "Война и мир", "классика", 1225, False),
    make_book(2, "Мастер и Маргарита", "классика", 480, True),
    make_book(3, "Python Crash Course", "программирование", 544, True),
]

validate_records([])                           # пустой список допустим
validate_records(SAMPLE)                       # корректный набор
print("validate_records: пустой и корректный наборы проходят")


def expect_value_error(data, label):
    try:
        validate_records(data)
    except ValueError:
        return
    assert False, f"Ошибка не обнаружена: {label}"


expect_value_error({"id": 1}, "корень не список")
expect_value_error([{"id": 1}], "нет остальных ключей")
expect_value_error(
    [make_book(1, "A", "x", 10, False), make_book(1, "B", "y", 5, False)],
    "повторный id",
)
expect_value_error(
    [make_book(True, "A", "x", 10, False)], "id логический"
)
expect_value_error(
    [make_book(1, "A", "x", True, False)], "amount логический"
)
expect_value_error(
    [make_book(1, "A", "x", -1, False)], "amount отрицательный"
)
expect_value_error(
    [make_book(1, "", "x", 10, False)], "пустое название"
)
expect_value_error(
    [make_book(1, "A", "x", 10, "true")], "completed строкой"
)
validate_records([{**make_book(1, "A", "x", 10, False), "note": "ok"}])
print("validate_records: все нарушения обнаруживаются")

assert next_id([]) == 1
assert next_id(SAMPLE) == 4

records = []
r = add_record(records, "  Python  ", "  учёба  ", 300)
assert records[0]["id"] == 1
assert records[0]["title"] == "Python"           # strip при добавлении
assert records[0]["category"] == "учёба"
assert records[0]["amount"] == 300
assert records[0]["completed"] is False

r2 = add_record(records, "Git", "учёба", 200)
set_completed(records, r2["id"], True)
assert records[1]["completed"] is True
print("add_record и next_id работают корректно")

found = find_records(SAMPLE, "MA")
assert len(found) == 1 and found[0]["id"] == 2

found = find_records(SAMPLE, "python")
assert len(found) == 1 and found[0]["id"] == 3

assert find_records(SAMPLE, "несуществующее") == []
print("find_records: поиск без регистра работает")

recs = [make_book(1, "A", "x", 10, False), make_book(2, "B", "y", 20, False)]
assert set_completed(recs, 1, True) is True
assert recs[0]["completed"] is True
assert set_completed(recs, 99, True) is False   # неизвестный id

assert delete_record(recs, 1) is True
assert len(recs) == 1 and recs[0]["id"] == 2     # id 2 сохранился
assert delete_record(recs, 99) is False

added = add_record(recs, "C", "z", 5)
assert added["id"] == 3
print("set_completed и delete_record корректно обрабатывают неизвестный id")

s = statistics(SAMPLE)
assert s["total"] == 3
assert s["done"] == 2
assert s["not_done"] == 1
assert s["total_amount"] == 1225 + 480 + 544
assert s["by_category"]["классика"] == 1225 + 480
assert s["by_category"]["программирование"] == 544

empty = statistics([])
assert empty == {"total": 0, "done": 0, "not_done": 0,
                 "total_amount": 0, "by_category": {}}
print("statistics: суммы и счётчики верны")

print("Все проверки logic пройдены")