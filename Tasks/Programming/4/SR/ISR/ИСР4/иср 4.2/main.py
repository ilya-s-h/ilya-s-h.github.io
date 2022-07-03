"""
    ИСР 4.2. 
    Создание программы по распределению списка с случайными значениями на два списка по определенному критерию (четность/нечетность, положительные/отрицательные числа)
"""

import random

array = []
positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for i in range(10):
    array.append(random.randint(-100, 100))
for i in array:
    if i < 0:
        negative_numbers.append(i)
    elif i > 0:
        positive_numbers.append(i)
    if i % 2 == 0:
        even_numbers.append(i)
    elif i % 2 != 0:
        odd_numbers.append(i)

print('Список случайных чисел:', array)
print('\nПоложительные значения', positive_numbers)
print('Отрицательные значения', negative_numbers)
print('Четные значения', even_numbers)
print('Нечетные значения', odd_numbers)
