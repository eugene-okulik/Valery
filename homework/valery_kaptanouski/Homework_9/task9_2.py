"""
Есть такой список:
temperatures = [
20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]
С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
Будем считать жарким всё, что выше 28.
Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
"""


temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_temperatures = list(filter(lambda x: x > 28, temperatures))
average_hot_temp = sum(hot_temperatures) / len(hot_temperatures)

print(hot_temperatures)
print(max(hot_temperatures))
print(average_hot_temp)
print(min(hot_temperatures))
