"""Удаление файла .json"""
__name__ = 'delete'

__all__ = ['delete_json']

import os


def delete_json(path, file_name):
    if path != '' and path != '.' and path is not None:
        os.remove(path + '\\' + file_name + '.json')
    else:
        os.remove(file_name + '.json')
