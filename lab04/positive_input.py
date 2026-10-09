
attempts_failed = 0
current_number = int(input("Введите положительное число: "))

# Пока число НЕ положительное просим снова
while current_number <= 0:
    attempts_failed += 1
    print("Ошибка! Число должно быть больше нуля.")
    current_number = int(input("Попробуйте еще раз: "))

# корректное число
square_result = current_number ** 2

print()
print(f"Квадрат числа {current_number}: {square_result}")
print(f"Количество отклоненных попыток: {attempts_failed}")