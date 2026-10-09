# Вариант 2: Сумма и количество отрицательных чисел.
n = int(input("Сколько чисел ввести (n >= 0): "))

count_negative = 0
sum_negative = 0

# выполняется n раз если n=0, он пропускается полностью.
for i in range(n):
    current_num = int(input(f"Число {i + 1}: "))

    # число < 0
    if current_num < 0:
        count_negative += 1
        sum_negative += current_num

print()
print(f"Количество отрицательных чисел: {count_negative}")
print(f"Сумма отрицательных чисел: {sum_negative}")