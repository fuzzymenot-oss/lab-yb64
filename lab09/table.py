def row_sums(matrix):
    return [sum(row) for row in matrix]


def column_sums(matrix):
    if not matrix:
        return []
    columns = len(matrix[0])
    result = []
    for col in range(columns):
        total = 0
        for row in range(len(matrix)):
            total += matrix[row][col]  # обращаемся по обоим индексам
        result.append(total)
    return result


def diagonal_pattern(size):
    matrix = []
    for row in range(size):
        current_row = []
        for column in range(size):
            if row == column:
                current_row.append(0)
            elif row < column:
                current_row.append(1)
            else:  # row > column
                current_row.append(2)
        matrix.append(current_row)
    return matrix


def transform(matrix):
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if value > 0:
                new_row.append(1)
            else:
                new_row.append(value)  # 0 и отрицательные как есть
        result.append(new_row)
    return result
