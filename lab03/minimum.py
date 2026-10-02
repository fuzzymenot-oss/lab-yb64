# Поиск минимального из трёх чисел без встроенных функций.
num_one = int(input("Первое число: "))
num_two = int(input("Второе число: "))
num_three = int(input("Третье число: "))

# Логика сравнения
if num_one <= num_two and num_one <= num_three:
    minimum_value = num_one
elif num_two <= num_one and num_two <= num_three:
    minimum_value = num_two
else:
    # Если первое и второе не меньше третьего, значит третье — минимум
    # (или равно одному из них)
    minimum_value = num_three

print(f"Минимальное число: {minimum_value}")