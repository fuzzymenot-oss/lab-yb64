from pathlib import Path
from files_lab import read_matrix, selected_sum, write_matrix_csv
from table import row_sums, column_sums


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


def build_report(matrix):
    rs = row_sums(matrix)
    cs = column_sums(matrix)
    lines = [
        "Суммы строк: " + " ".join(str(v) for v in rs),
        "Суммы столбцов: " + " ".join(str(v) for v in cs),
        f"Результат варианта: {selected_sum(matrix)}",
    ]
    return "\n".join(lines) + "\n"


def main():
    folder = Path(__file__).resolve().parent
    source = folder / "matrix.txt"
    report = folder / "report.txt"
    csv_path = folder / "matrix.csv"
    demo_size = read_positive_integer("Введите положительный размер (проверка ввода): ")
    print(f"Принято значение: {demo_size}")
    print()

    try:
        matrix = read_matrix(source)
    except FileNotFoundError:
        print(f"Файл не найден: {source}")
        return
    except UnicodeError:
        print("Ошибка кодировки: файл должен быть в UTF-8")
        return
    except ValueError as exc:
        print(f"Неверный формат данных: {exc}")
        return
    except OSError as exc:
        print(f"Ошибка файлового доступа: {exc}")
        return

    report_text = build_report(matrix)
    try:
        with open(report, "w", encoding="utf-8") as file:
            file.write(report_text)
    except OSError as exc:
        print(f"Не удалось записать отчёт: {exc}")
        return
    try:
        write_matrix_csv(matrix, csv_path)
    except OSError as exc:
        print(f"Не удалось записать CSV: {exc}")

    print("Отчёт записан в report.txt")
    print(report_text, end="")


if __name__ == "__main__":
    main()