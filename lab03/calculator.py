# Простой калькулятор.
first_num = float(input("Первое число: "))
operator = input("Операция (+, -, *, /): ")
second_num = float(input("Второе число: "))

# Проверка операций
if operator == "+":
    result = first_num + second_num
    print(f"Результат: {result:.2f}")
elif operator == "-":
    result = first_num - second_num
    print(f"Результат: {result:.2f}")
elif operator == "*":
    result = first_num * second_num
    print(f"Результат: {result:.2f}")
elif operator == "/":
    if second_num == 0:
        print("Деление на ноль запрещено")
    else:
        result = first_num / second_num
        print(f"Результат: {result:.2f}")
else:
    print("Неизвестная операция")