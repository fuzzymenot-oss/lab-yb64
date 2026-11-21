def validate_records(records):
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for index, record in enumerate(records):
        position = index + 1
        if not isinstance(record, dict):
            raise ValueError(f"Запись {position}: ожидается словарь")

        required = ("id", "title", "category", "amount", "completed")
        for key in required:
            if key not in record:
                raise ValueError(f"Запись {position}: отсутствует поле '{key}'")

        # id: положительное целое, не bool
        rid = record["id"]
        if type(rid) is not int or rid <= 0:
            raise ValueError(
                f"Запись {position}: поле 'id' должно быть положительным целым"
            )
        if rid in seen_ids:
            raise ValueError(f"Запись {position}: повторный id {rid}")
        seen_ids.add(rid)

        # title, category: непустые строки
        for key in ("title", "category"):
            value = record[key]
            if type(value) is not str or not value.strip():
                raise ValueError(
                    f"Запись {position}: поле '{key}' должно быть непустой строкой"
                )

        # amount: целое >= 0, не bool
        amount = record["amount"]
        if type(amount) is not int or amount < 0:
            raise ValueError(
                f"Запись {position}: поле 'amount' должно быть целым числом >= 0"
            )

        # completed: строго bool
        if type(record["completed"]) is not bool:
            raise ValueError(
                f"Запись {position}: поле 'completed' должно быть логическим"
            )

    return records


def next_id(records):
    if not records:
        return 1
    return max(record["id"] for record in records) + 1


def add_record(records, title, category, amount):
    clean_title = title.strip()
    clean_category = category.strip()
    if not clean_title:
        raise ValueError("Название не может быть пустым")
    if not clean_category:
        raise ValueError("Категория не может быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество страниц должно быть целым числом >= 0")

    record = {
        "id": next_id(records),
        "title": clean_title,
        "category": clean_category,
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    if not query or not query.strip():
        raise ValueError("Поисковый запрос не может быть пустым")
    needle = query.strip().lower()
    return [
        record for record in records
        if needle in record["title"].lower()
    ]


def _find_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def set_completed(records, record_id, completed):
    if type(completed) is not bool:
        raise ValueError("Значение статуса должно быть bool")
    record = _find_by_id(records, record_id)
    if record is None:
        return False
    record["completed"] = completed
    return True


def delete_record(records, record_id):
    record = _find_by_id(records, record_id)
    if record is None:
        return False
    records.remove(record)
    return True


def statistics(records):
    total = len(records)
    done = sum(1 for r in records if r["completed"])
    not_done = total - done
    total_amount = sum(r["amount"] for r in records)
    by_category = {}
    for r in records:
        cat = r["category"]
        by_category[cat] = by_category.get(cat, 0) + r["amount"]
    return {
        "total": total,
        "done": done,
        "not_done": not_done,
        "total_amount": total_amount,
        "by_category": by_category,
    }
