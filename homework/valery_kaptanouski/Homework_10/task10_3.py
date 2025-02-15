"""
Напишите программу: Есть функция, которая делает одну из арифметических операций с переданными ей числами
(числа и операция передаются в аргументы функции). Функция выглядит примерно так:

def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....
Программа спрашивает у пользователя 2 числа (вне функции)

Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:

    - если числа равны, то функция calc вызывается с операцией сложения этих чисел
    - если первое больше второго, то происходит вычитание второго из первого
    - если второе больше первого - деление первого на второе
    - если одно из чисел отрицательное - умножение
"""


def select_operation(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            result = func(first, second, '*')
        elif first == second:
            result = func(first, second, '+')
        elif first > second:
            result = func(first, second, '-')
        elif first < second:
            result = func(first, second, '/')
        else:
            result = None

        print(f"Результат: {result}")
        return result

    return wrapper


@select_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


calc(5, -2)
