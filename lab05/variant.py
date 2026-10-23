text = input("Введите текст: ")
words = text.split()
count = 0

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if not cleaned:
        continue
    if cleaned.endswith("я"):
        print(cleaned)
        count += 1

print()
if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")