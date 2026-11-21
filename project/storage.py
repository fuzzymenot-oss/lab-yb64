
import json


def load_records(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Локальный импорт, чтобы не создавать циклическую зависимость
    from logic import validate_records
    validate_records(data)
    return data


def save_records(path, records):
    from logic import validate_records
    validate_records(records)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)