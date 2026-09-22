# Обмен значениями двух переменных через третью.
first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print()
print("До обмена:")
print(f"first_room: {first_room}")
print(f"second_room: {second_room}")

# Логика обмена
temp_room = first_room      # Сохраняем первое значение
first_room = second_room    # Первое становится вторым
second_room = temp_room     # Второе становится тем, что было первым

print()
print("После обмена:")
print(f"first_room: {first_room}")
print(f"second_room: {second_room}")