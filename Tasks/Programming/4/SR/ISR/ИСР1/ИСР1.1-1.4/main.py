import json
import pandas as pd

def print_json(file, fields):
    """
    Функция для считывания json-данных из файла и вывода их в табличном виде на экран
    """

    try:
        with open(file) as file_obj:
            data = json.load(file_obj)

    except FileNotFoundError:
        print("Ошибка, файл не найден")
        return "STOP"

    except json.decoder.JSONDecodeError:
        print("Ошибка при считывании файла .json")
        return "STOP"

    else:

        # Проверяем, все ли поля есть в JSON
        for field in fields:
            if len(data) > 0:
                if field not in data[0]:
                    raise ValueError(f'Поле {field} отсутствует в файле .json')
            else:
                raise ValueError("Файл .json пуст")

        # Создаём таблицу
        table = pd.DataFrame(data, columns=fields)

        # Увеличиваем индекс
        table.index += 1
        print(table)

        file_obj.close()

        return data


if __name__ == "__main__":
    print_json("./data.json", ["date", "temperature", "latitude", "longitude"])


if __debug__:
    fields = ["date", "temperature", "latitude", "longitude"]
    data = print_json("./data.json", fields)
    for field in fields:
            if len(data) > 0:
                assert field in data[0], ValueError(f'Поле {field} отсутствует в файле .json')
            else:
                raise ValueError("Файл .json пуст")