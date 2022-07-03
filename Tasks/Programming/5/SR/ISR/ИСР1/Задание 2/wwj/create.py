"""Создание файла .json"""
__name__ = 'create'

__all__ = ['create_json']


def create_json(path, file_name):
    if path != '' and path != '.' and path is not None:
        file = open(path + '\\' + file_name + '.json', 'w')
    else:
        file = open(file_name + '.json', 'w')
    file.close()
