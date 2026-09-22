# Карточка студента
last_name = input("Фамилия: ")
first_name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст в полных годах: "))
favorite_subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю: "))

# Расчёты
full_name = first_name + " " + last_name
age_in_four_years = age + 4
preparation_four_weeks = study_hours * 4
preparation_per_day = study_hours / 7

# Вывод итоговой карточки после завершения всего ввода
print()
print("Карточка студента")
print("-----------------")
print(f"Полное имя: {full_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Любимый предмет: {favorite_subject}")
print(f"Возраст сейчас: {age}")
print(f"Возраст через четыре года: {age_in_four_years}")
print(f"Подготовка за четыре недели: {preparation_four_weeks:.2f} ч.")
print(f"Средняя подготовка в день: {preparation_per_day:.2f} ч.")