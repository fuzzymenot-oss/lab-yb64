
import csv


def read_matrix(path):

    with open(path, "r", encoding="utf-8") as file:
        lines = list(file)

    if not lines:
        raise ValueError("Пустой файл: нет заголовка")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError(
            f"Строка 1: в заголовке ожидалось 2 числа, найдено {len(header)}"
        )
    try:
        rows = int(header[0])
        columns = int(header[1])
    except ValueError:
        raise ValueError(
            f"Строка 1: заголовок должен содержать целые числа, найдено {header}"
        )
    if rows <= 0 or columns <= 0:
        raise ValueError(
            f"Строка 1: размеры должны быть положительными, найдено {rows} {columns}"
        )

    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(f"Ожидалось {rows} строк данных, найдено {len(data_lines)}")

    matrix = []
    for index, line in enumerate(data_lines):
        line_number = index + 2          # заголовок = строка 1
        tokens = line.split()
        if len(tokens) != columns:
            raise ValueError(
                f"Строка {line_number}: ожидалось {columns} чисел, найдено {len(tokens)}"
            )
        row = []
        for token in tokens:
            try:
                row.append(int(token))
            except ValueError:
                raise ValueError(
                    f"Строка {line_number}: нечисловая ячейка '{token}'"
                )
        matrix.append(row)

    return matrix


def selected_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            if value < 0:
                total += value
    return total


def write_matrix_csv(matrix, path):
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(matrix)