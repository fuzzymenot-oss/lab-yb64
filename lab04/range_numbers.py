# Вывод диапазона чисел.
start = int(input("Первое число (a): "))
end = int(input("Второе число (b): "))

print()
if start <= end:
    for number in range(start, end + 1):
        print(number)
else:
    for number in range(start, end - 1, -1):
        print(number)