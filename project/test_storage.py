import json
from pathlib import Path
from tempfile import TemporaryDirectory

from storage import load_records, save_records


def write(path, text):
    path.write_text(text, encoding="utf-8")


def make_book(rid, title, category, amount, completed):
    return {
        "id": rid, "title": title, "category": category,
        "amount": amount, "completed": completed,
    }


with TemporaryDirectory() as directory:
    base = Path(directory)

    path = base / "ok.json"
    data = [
        make_book(1, "A", "x", 10, False),
        make_book(2, "B", "x", 20, True),
    ]
    save_records(path, data)
    restored = load_records(path)
    assert restored == data
    print("save/load: цикл записи-чтения проходит")

    path = base / "empty.json"
    save_records(path, [])
    assert load_records(path) == []
    print("save/load: пустой список работает")

    missing = base / "nope.json"
    try:
        load_records(missing)
    except FileNotFoundError:
        print("load: FileNotFoundError для отсутствующего файла")
    else:
        assert False, "FileNotFoundError не брошен"

    path = base / "bad.json"
    write(path, "not a json")
    try:
        load_records(path)
    except json.JSONDecodeError:
        print("load: JSONDecodeError на битом JSON")
    else:
        assert False, "JSONDecodeError не брошен"

    path = base / "wrong.json"
    write(path, json.dumps({"id": 1}))
    try:
        load_records(path)
    except ValueError:
        print("load: ValueError для объекта вместо списка")
    else:
        assert False, "ValueError не брошен"

    path = base / "dup.json"
    write(path, json.dumps([
        make_book(1, "A", "x", 10, False),
        make_book(1, "B", "y", 5, False),
    ]))
    try:
        load_records(path)
    except ValueError:
        print("load: ValueError для повторного id")
    else:
        assert False, "ValueError не брошен"

print("Все проверки storage пройдены")