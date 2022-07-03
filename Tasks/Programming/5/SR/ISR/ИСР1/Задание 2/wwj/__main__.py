from .create import *
from .delete import *
from .read import *
from .rename import *
from .write import *

if __name__ == '__main__':
    print('Введите путь к файлу: ')
    path = str(input())
    print('Введите имя файла: ')
    file_name = str(input())
    data = {"oranges": 5, "apples": 2}
    create_json(path, file_name)
    write_json(data, path, file_name)
    rename_json(path, path, file_name, file_name + '2')
    data = read_json(path, file_name + '2')
    print("Содержимое файла " + file_name + '2.json (бывшего файла ' + file_name + '.json):', data)
    delete_json(path, file_name + '2')
