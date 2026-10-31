raw = input("Целые числа через пробел: ")
numbers = []
for part in raw.split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if number < 0:
        selected.append(number)

count = len(selected)
total = sum(selected)
sorted_copy = sorted(selected)
print(f"Список по условию: {selected}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Отсортированная копия: {sorted_copy}")