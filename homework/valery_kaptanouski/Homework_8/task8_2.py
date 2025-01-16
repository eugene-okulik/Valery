"""
Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.
"""


import sys
sys.set_int_max_str_digits(100000)


def generate_fib(max_index):
    a, b = 0, 1
    index = 0
    while index <= max_index:
        yield index, a
        a, b = b, a + b
        index += 1


list_numbers = [5, 200, 1000, 100000]


def print_fib():
    max_index = max(list_numbers)
    for index, number in generate_fib(max_index):
        if index in list_numbers:
            print(f"Число Фибоначчи под индексом {index}: {number}")


print_fib()
