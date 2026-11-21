def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком")

    seen_ids = set()
    for index, record in enumerate(data):
        position = index + 1
        if not isinstance(record, dict):
            raise ValueError(f"Запись {position}: ожидается словарь")

        for key in ("id", "userId"):
            if key not in record:
                raise ValueError(f"Запись {position}: отсутствует поле '{key}'")
            value = record[key]
            if type(value) is not int or value <= 0:
                raise ValueError(
                    f"Запись {position}: поле '{key}' должно быть положительным целым"
                )
        if "title" not in record:
            raise ValueError(f"Запись {position}: отсутствует поле 'title'")
        title = record["title"]
        if type(title) is not str or not title.strip():
            raise ValueError(f"Запись {position}: поле 'title' должно быть непустой строкой")

        if "completed" not in record:
            raise ValueError(f"Запись {position}: отсутствует поле 'completed'")
        if type(record["completed"]) is not bool:
            raise ValueError(f"Запись {position}: поле 'completed' должно быть логическим")

        if record["id"] in seen_ids:
            raise ValueError(f"Запись {position}: повторный id {record['id']}")
        seen_ids.add(record["id"])

    return data


def completion_counts(todos):
    counts = {}
    for record in todos:
        user = record["userId"]
        counts[user] = counts.get(user, 0) + (1 if record["completed"] else 0)
    return counts


def top_users(counts):
    if not counts:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    return sorted(user for user, total in counts.items() if total == maximum)


def leader_task_ids(todos, leaders):
    ids = []
    for record in todos:
        if record["userId"] in leaders and record["completed"]:
            ids.append(record["id"])
    return ids


def select_tasks(todos, user_id, parameter=None):
    selected = []
    for record in todos:
        if record["userId"] == user_id and record["completed"]:
            selected.append(record)
    return selected


def task_ids(records):
    return [record["id"] for record in records]