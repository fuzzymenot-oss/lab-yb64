from table import row_sums, column_sums, diagonal_pattern, transform

# прямоугольная 2x3
m = [[1, 2, 3], [4, 5, 6]]
snap_m = [row.copy() for row in m]
assert row_sums(m) == [6, 15]
assert column_sums(m) == [5, 7, 9]
assert m == snap_m                       # sums не мутируют вход

#  одна ячейка
one = [[7]]
assert row_sums(one) == [7]
assert column_sums(one) == [7]
assert diagonal_pattern(1) == [[0]]

# один столбец, три строки
col = [[1], [-1], [0]]
assert row_sums(col) == [1, -1, 0]
assert column_sums(col) == [0]

#  пустая матрица
empty = []
assert row_sums(empty) == []
assert column_sums(empty) == []
assert transform(empty) == []

# диагональный узор 3
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

source = [[-2, 0, 3], [4, -5, 6]]
snapshot = [row.copy() for row in source]
result = transform(source)
assert result == [[-2, 0, 1], [1, -5, 1]]
assert source == snapshot

result[0][0] = 999
assert source == snapshot
assert result[0][0] == 999

print("Все проверки table пройдены")