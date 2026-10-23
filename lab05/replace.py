text = input("Введите текст: ")

#считаем количество двоеточий
count_colons = text.count(":")

# выполняем замену
new_text = text.replace(":", "-")

print(f"Количество замен: {count_colons}")
print(f"Новая строка: {new_text}")