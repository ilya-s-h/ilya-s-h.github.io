"""Переименование файла .json"""
__name__ = 'rename'

__all__ = ['rename_json']

import os


def rename_json(path, new_path, file_name, new_file_name):
    if (path != '' and path != '.' and path is not None) and (new_path != '' and new_path != '.' and new_path is not None):
        os.renames(path + '\\' + file_name + '.json', new_path + '\\' + new_file_name + '.json')
    else:
        os.renames(file_name + '.json', new_file_name + '.json')
