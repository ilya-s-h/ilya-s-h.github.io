"""Чтение файла .json"""
__name__ = 'read'

__all__ = ['read_json']

import json


def read_json(path, file_name):
    if path != '' and path != '.' and path is not None:
        file = open(path + '\\' + file_name + '.json', 'r')
    else:
        file = open(file_name + '.json', 'r')
    data = json.load(file)
    return data
