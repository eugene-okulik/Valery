"""
Допустим, какая-то программа возвращает результат своей работы в таком виде:

результат операции: 42
результат операции: 514
результат работы программы: 9

С помощью срезов и метода index получите из каждой строки с результатом число, прибавьте к полученному числу 10,
результат сложения распечатайте.
"""


line1 = "результат операции: 42"
line2 = "результат операции: 514"
line3 = "результат работы программы: 9"

start_index1 = line1.index(":") + 2
start_index2 = line2.index(":") + 2
start_index3 = line3.index(":") + 2

number1 = line1[start_index1:]
number2 = line2[start_index2:]
number3 = line3[start_index3:]

result1 = int(number1) + 10
result2 = int(number2) + 10
result3 = int(number3) + 10

print(result1)
print(result2)
print(result3)
