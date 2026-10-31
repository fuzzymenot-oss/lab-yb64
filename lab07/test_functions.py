from functions import average, normalize_text, select_numbers, sum_digits, is_palindrome
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
print("Базовые проверки пройдены")

assert sum_digits(10) == 1
assert sum_digits(-10) == 1
assert sum_digits(999) == 27

assert abs(average([0, 0, 1]) - 1 / 3) < 1e-9
src_avg = [3, 1, 2]
snap_avg = src_avg.copy()
average(src_avg)
assert src_avg == snap_avg
assert normalize_text("") == ""
assert normalize_text("a\tb\nc") == "a b c"

source = [-5, 0, 2, 5]
snapshot = source.copy()
assert select_numbers(source, 2) == [-5, 0]
assert source == snapshot

assert select_numbers([], 2) == []

assert select_numbers([1, 2, 3], 2) == [1]
assert select_numbers([2], 2) == []
assert select_numbers([1], 2) == [1]
assert select_numbers([-1, 0, 1], 0) == [-1]

assert select_numbers([-1, -1, 3, -1], 2) == [-1, -1, -1]


assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("а") is True
assert is_palindrome("   ") is False
assert is_palindrome("Python") is False
assert is_palindrome("А!") is False              
print("Проверки варианта 2 и доп. задания пройдены")