from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum


def expect_value_error(path, label):
    try:
        read_matrix(path)
    except ValueError:
        print(f"OK (ValueError): {label}")
        return
    assert False, f"Ошибка не обнаружена: {label}"


with TemporaryDirectory() as directory:
    base = Path(directory)

    p = base / "ok.txt"
    p.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(p) == [[7, -1]]
    print("Проверка чтения пройдена")

    p = base / "zero.txt"
    p.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(p) == [[0]]
    print("Проверка [[0]] пройдена")

    p = base / "empty.txt"
    p.write_text("", encoding="utf-8")
    expect_value_error(p, "пустой файл")

    p = base / "bad_header.txt"
    p.write_text("0 3\n", encoding="utf-8")
    expect_value_error(p, "заголовок 0 3")

    p = base / "short_row.txt"
    p.write_text("1 2\n1\n", encoding="utf-8")
    expect_value_error(p, "строка данных короче columns (строка 2)")

    p = base / "nan_cell.txt"
    p.write_text("1 2\n1 x\n", encoding="utf-8")
    expect_value_error(p, "нечисловая ячейка (строка 2)")

    p = base / "extra_rows.txt"
    p.write_text("1 1\n5\n6\n", encoding="utf-8")
    expect_value_error(p, "лишняя строка данных")

    missing = base / "nope.txt"
    try:
        read_matrix(missing)
    except FileNotFoundError:
        print("OK (FileNotFoundError): отсутствующий путь")
    else:
        assert False, "FileNotFoundError не обнаружена"

assert selected_sum([[1, -2, 3], [4, 0, -6]]) == -8
print("Проверка selected_sum (вариант 2) пройдена")

print("Все проверки files пройдены")