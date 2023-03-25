# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
n = int(input("Введите размер массива: n = "))
max_num = int(input("Введите максимальное значение: max = "))
min_num = int(input("Введите минимальное значение значение: min = "))
arr_1 = [random.randint(-50, 50) for i in range(n)]
print(arr_1)   
result = [i for i, x in enumerate(arr_1) if min_num <= x <= max_num]
print(result)