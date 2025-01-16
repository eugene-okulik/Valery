"""
Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
Спросите у пользователя salary. А bonus пусть назначается рандомом.

Если bonus - true, то к salary должен быть добавлен рандомный бонус.

Примеры результатов:

10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785'
"""


from random import randint


def bonus_count(base_salary, is_bonus_applied):
    if is_bonus_applied:
        return base_salary + randint(0, 1000)
    return base_salary

def print_result(base_salary, is_bonus_applied):
    calculated_salary = bonus_count(base_salary, is_bonus_applied)
    print(f'{base_salary}, {is_bonus_applied} - ${calculated_salary}')

while True:
    salary = int(input('Введите salary: '))
    bonus = bool(randint(0, 1))
    if salary < 0:
        print('salary не может быть отрицательным')
        break
    print_result(salary, bonus)
