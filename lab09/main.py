from table import row_sums, column_sums, diagonal_pattern, transform


def print_matrix(title, matrix):
    print(title)
    for row in matrix:
        print(*row)


def read_matrix():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def main():
    matrix = read_matrix()

    print()
    print("Суммы строк:   ", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    print()
    size = int(input("Положительный размер для диагонального узора: "))
    print_matrix("Диагональный узор:", diagonal_pattern(size))

    print()
    transformed = transform(matrix)
    print_matrix("Исходная матрица (не изменилась):", matrix)
    print_matrix("Преобразованная (вариант 2: положительные -> 1):", transformed)


if __name__ == "__main__":
    main()