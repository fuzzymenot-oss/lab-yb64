# Вариант 2: Упаковка книг в коробки.
total_books = int(input("Общее количество книг: "))
capacity = int(input("Вместимость одной коробки (книг): "))

full_boxes = total_books // capacity      # Полностью заполненные коробки
remainder = total_books % capacity        # Остаток неполной коробки
min_boxes = (total_books + capacity - 1) // capacity  # Минимум коробок для всего объема

print(f"Полностью заполненных коробок: {full_boxes}")
print(f"Остаток книг в последней коробке: {remainder}")
print(f"Минимальное количество коробок: {min_boxes}")