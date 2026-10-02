# Перевод секунд в формат "ч мин с".
total_seconds = int(input("Введите общее количество секунд: "))

hours = total_seconds // 3600          # Сколько полных часов
remaining_after_hours = total_seconds % 3600  # Остаток после часов
minutes = remaining_after_hours // 60  # Сколько полных минут
seconds = remaining_after_hours % 60   # Сколько осталось секунд

print(f"Результат: {hours} ч {minutes} мин {seconds} с")