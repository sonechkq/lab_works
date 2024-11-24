import json

def task() -> float:
    json_file_path = 'input.json'

    total_sum = 0.0

    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

            for entry in data:
                score = entry.get('score', 0)
                weight = entry.get('weight', 0)

                total_sum += score * weight

    except FileNotFoundError:
        print(f"Файл {json_file_path} не найден.")
        return 0.0
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
        return 0.0

    return round(total_sum, 3)

print(task())
