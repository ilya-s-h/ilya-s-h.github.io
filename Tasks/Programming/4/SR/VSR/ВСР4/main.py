"""
    ВСР 4.1
    Создание программы с реализацией вручную одного из алгоритмов сортировки (вставки, плавной сортировки).
"""

from random import randint


def sort(n):
    for i in range(len(n)):
        j = i - 1
        k = n[i]
        while n[j] > k and j >= 0:
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = k
    return n


def main():
    nums = int(input('Введите кол-во элементов массива: '))
    array = []
    for i in range(nums):
        array.append(randint(0, 50))
    print("Исходный массив:", array)
    print("Сортировка вставками: ", sort(array))


main()
