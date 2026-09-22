# Вариант 2: Расчет заказа книжного магазина.
order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

item_one_name = input("Название первой позиции: ")
item_one_qty = int(input("Количество первой позиции: "))
item_one_price = float(input("Цена единицы первой позиции: "))

item_two_name = input("Название второй позиции: ")
item_two_qty = int(input("Количество второй позиции: "))
item_two_price = float(input("Цена единицы второй позиции: "))

delivery_cost = float(input("Стоимость доставки: "))
paid_amount = float(input("Внесённая сумма: "))

# Расчёты
cost_one = item_one_qty * item_one_price
cost_two = item_two_qty * item_two_price
goods_total = cost_one + cost_two
grand_total = goods_total + delivery_cost
total_units = item_one_qty + item_two_qty
change = paid_amount - grand_total

# Вывод чека
print()
print("--- ЧЕК ЗАКАЗА ---")
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer_name}")
print("-" * 20)
print(f"{item_one_name} | {item_one_qty} | {item_one_price:.2f} | {cost_one:.2f}")
print(f"{item_two_name} | {item_two_qty} | {item_two_price:.2f} | {cost_two:.2f}")
print("-" * 20)
print(f"Стоимость товаров: {goods_total:.2f} руб.")
print(f"Доставка: {delivery_cost:.2f} руб.")
print(f"ИТОГО к оплате: {grand_total:.2f} руб.")
print(f"Общее количество единиц: {total_units}")
print(f"Внесено: {paid_amount:.2f} руб.")
print(f"СДАЧА: {change:.2f} руб.")