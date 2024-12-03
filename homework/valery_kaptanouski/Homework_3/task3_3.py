"""
Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел
"""


import math


x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))

arithmetic_mean = (x + y) / 2
geometric_mean = math.sqrt(x * y)

print(f"Среднее арифметическое: {arithmetic_mean}, среднее геометрическое: {geometric_mean}")
