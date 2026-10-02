# Расчет стоимости покупки и сдачи.
price = int(input("Цена одной тетради (руб.): "))
count = int(input("Количество тетрадей: "))
paid = int(input("Внесенная сумма (руб.): "))

cost = price * count       # Общая стоимость товара
change = paid - cost       # Сдача

print(f"Стоимость: {cost} руб.")
print(f"Сдача: {change} руб.")