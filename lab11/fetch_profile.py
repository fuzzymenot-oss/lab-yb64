import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

def fetch_profile(login):
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-course-lab11",
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data

def main():
    try:
        data = fetch_profile(input("Логин GitHub: "))
        output = Path(__file__).resolve().parent / "profile.json"
        with open(output, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"Профиль сохранён: {data['login']}")
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")

def print_profile(data):
    """Общий вывод профиля для обоих источников; null не подменяется выдумкой."""
    print(f"Логин: {data['login']}")
    print(f"ID: {data.get('id')}")
    print(f"Имя: {data.get('name')}")


def load_local_sample():
    path = Path(__file__).resolve().parent / "profile_sample.json"
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Локальный пример не похож на профиль пользователя")
    return data


def main_with_menu():
    print("Источник профиля: 1 — сеть, 2 — локальный пример")
    choice = input("Выбор: ").strip()
    try:
        if choice == "1":
            data = fetch_profile(input("Логин GitHub: "))
            output = Path(__file__).resolve().parent / "profile.json"
            with open(output, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
        elif choice == "2":
            data = load_local_sample()
            print("Использованы учебные локальные данные")
        else:
            print("Неизвестный пункт меню")
            return
        print_profile(data)
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main_with_menu()