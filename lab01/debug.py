# Фрагмент А
print("Фрагмент А")
first = "2"
second = "3"
print("Тип до преобразования:", type(first))
first_num = int(first)
second_num = int(second)
print("Тип после преобразования:", type(first_num))
sum_result = first_num + second_num
print("Результат (сумма):", sum_result)

print()

# Фрагмент Б
print("Фрагмент Б")
age_str = input("Возраст: ") # вводит число в консоли
print("Тип до преобразования:", type(age_str))
age_int = int(age_str)
print("Тип после преобразования:", type(age_int))
age_next_year = age_int + 1
print("Результат (возраст через год):", age_next_year)

print()

# Фрагмент В
print("Фрагмент В")
x = 4
y = 7
z = 10
average_correct = (x + y + z) / 3
print("Результат (среднее):", average_correct)