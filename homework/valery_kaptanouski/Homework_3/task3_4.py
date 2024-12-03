"""
Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь
"""
import math

first_triangle_leg = float(input("Введите значение первого катета прямоугольного треугольника (число!): "))
second_triangle_leg = float(input("Введите значение второго катета прямоугольного треугольника (число!): "))

hypotenuse = math.sqrt(first_triangle_leg**2 + second_triangle_leg**2)
square = (first_triangle_leg * second_triangle_leg) / 2

print(f"Гипотенуза прямоугольного треугольника: {hypotenuse}, площать прямоугольного треугольника: {square}")
