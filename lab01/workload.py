# Учебная нагрузка по двум предметам
pr_one = input("Название первого предмета: ")
koll_one = int(input("Количество занятий по первому предмету за неделю: "))
min_one = int(input("Продолжительность одного занятия по первому предмету (мин): "))

pr_two = input("Название второго предмета: ")
koll_two = int(input("Количество занятий по второму предмету за неделю: "))
min_two = int(input("Продолжительность одного занятия по второму предмету (мин): "))

available_hours = float(input("Доступное время на неделю в часах: "))

# Расчёты
minutes_one = koll_one * min_one
minutes_two = koll_two * min_two
total_minutes = minutes_one + minutes_two
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
hours_in_four_weeks = total_hours * 4

# Вывод результата
print()
print("Учебная нагрузка")
print("----------------")
print(f"{pr_one}: {minutes_one} мин.")
print(f"{pr_two}: {minutes_two} мин.")
print(f"Общая нагрузка: {total_minutes} мин. или {total_hours:.2f} ч.")
print(f"Остаток свободного времени: {free_hours:.2f} ч.")
print(f"Нагрузка за четыре одинаковые недели: {hours_in_four_weeks:.2f} ч.")