'''
1.1 Разработать фрагмент программы, который будет сохранять вводимые пользователем данные,
по выбору в json, или csv-файле (использовать модули csv, json) с использованием протокола менеджеров контекста,
а также расширенного синтаксиса исключений.
'''


import os
import csv
import json

class DataWriter:
    def __init__(self, fields):
        self._data = []
        self._fields = fields
        
        
    def add_data(self, value):
        for field in self._fields:
            if not value.get(field):
                raise ValueError('field value not set')
        self._data.append(value)
        
        
    def save(self, filename):
        if not filename:
            filename = 'data.csv'
        name, ext = os.path.splitext(filename)
        if ext[1:] == 'csv':
            try:
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self._fields)
                    writer.writeheader()
                    writer.writerows(self._data)
            except OSError as e:
                print('Ошибка при сохранении файла:', e)
        elif ext[1:] == 'json':
            try:
                with open(filename, 'w') as f:
                    json.dump(self._data, f)
            except OSError as e:
                print('Ошибка при сохранении файла:', e)
        else:
            raise ValueError('incorrect file type')
        
        
if __name__ == '__main__':
    writer = DataWriter(['name', 'email'])
    writer.add_data({'name': 'John', 'email': 'john@example.com'})
    writer.save('users.csv')
    writer.save('users.json')