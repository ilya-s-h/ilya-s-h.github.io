"""Запись в файл .json"""
__name__ = 'write'

__all__ = ['write_json']

import json


def write_json(data, path, file_name):
    if path != '' and path != '.' and path != None:
        file = open(path + '\\' + file_name + '.json', 'w')
    else:
        file = open(file_name + '.json', 'w')
    file.write(json.dumps(data, separators=(',', ':')))
    file.close()
