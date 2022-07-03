"""
    ИСР 4.1. 
    Создание программы по заполнению массивов случайными значениями. 
    Сортировка значений в списке методом вставки, плавной сортировки, с помощью встроенных функций языка.
"""

import numpy as np
import numpy.random


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i - 1
        k = nums[i]
        while nums[j] > k and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = k
    return nums


def smooth_sort(nums):
    def heap(nums, k, n):
        new_element = nums[k]
        while 2 * k + 1 < n:
            child = 2 * k + 1
            if child + 1 < n and nums[child] < nums[child + 1]:
                child += 1
            if new_element >= nums[child]:
                break
            nums[k] = nums[child]
            k = child
        nums[k] = new_element

    size = len(nums)
    for i in range(size // 2 - 1, -1, -1):
        heap(nums, i, size)
    for i in range(size - 1, 0, -1):
        temp = nums[i]
        nums[i] = nums[0]
        nums[0] = temp
        heap(nums, 0, i)
    return nums

array = list(np.random.randint(0, 100, 10))
print("Массив случайных чисел:", array)
print("\nСортировка вставками:", insertion_sort(array))
print("\nПлавная сортировка:", smooth_sort(array))
print("\n---Сортировка с помощью встроенных функций---")
print("\nСортировка массива по возрастанию:", sorted(array))
print("\nСортировка массива по убыванию:", sorted(array, reverse=True))