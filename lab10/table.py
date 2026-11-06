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
            total += matrix[row][col]
        result.append(total)
    return result
