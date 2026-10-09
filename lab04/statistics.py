n = int(input("Сколько чисел ввести (n >= 1): "))

total_sum = 0  # Накопитель суммы
count_positive = 0  # Счетчик положительных
maximum_value = None  # максимум

for i in range(n):
    current_num = int(input(f"Число {i + 1}: "))

    total_sum += current_num

    # Подсчет положительных (> 0)
    if current_num > 0:
        count_positive += 1

    if maximum_value is None or current_num > maximum_value:
        maximum_value = current_num

print()
print(f"Сумма: {total_sum}")
print(f"Положительных чисел: {count_positive}")
print(f"Максимум: {maximum_value}")