from functions import sum_digits, average, normalize_text, select_numbers
def parse_numbers(raw):
    """Строку «целые через пробел» превращаем в список int."""
    numbers = []
    for part in raw.split():
        numbers.append(int(part))
    return numbers


def main():
    number = int(input("Целое число: "))
    print(f"Сумма цифр модуля: {sum_digits(number)}")

    raw = input("Целые числа через пробел: ")
    numbers = parse_numbers(raw)

    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg:.2f}")

    text = input("Произвольный текст: ")
    print(f"Нормализованный текст: '{normalize_text(text)}'")

    threshold = int(input("Порог (целое неотрицательное): "))
    selected = select_numbers(numbers, threshold)
    print(f"Выборка (меньше порога {threshold}): {selected}")


if __name__ == "__main__":
    main()