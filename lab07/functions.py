def sum_digits(number):
    """Сумма цифр модуля целого числа. Для нуля возвращает 0."""
    n = abs(number)          #
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def average(numbers):
    """Среднее арифметическое списка; None для пустого. Источник не меняет."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вариант 2: новый список значений, строго меньших threshold.
    Порядок и повторы сохраняются, исходный список не меняется."""
    result = []
    for number in numbers:
        if number < threshold:      
            result.append(number)
    return result


def is_palindrome(text):
    """Доп. задание: палиндром по правилам работы №5 (игнорируем регистр
    и обычные пробелы, пунктуацию сравниваем как есть).
    Пустой после очистки текст -> False."""
    cleaned = text.replace(" ", "").lower()
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]