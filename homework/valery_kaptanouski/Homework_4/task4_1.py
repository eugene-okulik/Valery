"""
Создание словаря

Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.
Для каждого элемента задайте значение соответствующее названию ключа. Например в элемент с ключом ‘tuple’
добавьте кортеж в качестве значения. Содержимое этого кортежа (или что вы там добавляете) - на вашу фантазию,
но количество элементов в каждом таком значении должно быть не меньше пяти. Т.е. если добавляете кортеж,
то в нем как минимум должно быть (1, 2, 3, 4, 5), если список, то не меньше пяти элементов, если словарь,
то не меньше пяти пар ключ-значение, итд.

Действия с элементами словаря my_dict:

Для того, что хранится под ключом ‘tuple’:
выведите на экран последний элемент
Для того, что хранится под ключом ‘list’:
добавьте в конец списка еще один элемент
удалите второй элемент списка
Для того, что хранится под ключом ‘dict’:
добавьте элемент с ключом ('i am a tuple',) и любым значением
удалите какой-нибудь элемент
Для того, что хранится под ключом ‘set’:
добавьте новый элемент в множество
удалите элемент из множества
В конце выведите на экран весь словарь

"""


from pprint import pprint


my_dict = {
    'tuple': (42, "Hello, World!", 3.14, True, [1, 2, 3], {"key": "value"}, None),
    'list': [99, "Python is fun!", 2.718, False, ["apple", "banana"], {"name": "John", "age": 30}, (1, 2)],
    'dict': {
        "integer": 123,
        "string": "Python",
        "float": 1.618,
        "boolean": True,
        "list": [7, 8, 9],
        "tuple": ("a", "b", "c"),
        "nested_dict": {"inner_key": "inner_value"}
    },
    'set': {1, "set_element", 3.14, False, (7, 8), "unique", None}
}

pprint(my_dict['tuple'][-1])
print()

my_dict['list'].append("date")
my_dict['list'].pop(1)
pprint(my_dict['list'])
print()

my_dict['dict'][('i am a tuple',)] = (9, 8, 7, 6, 5)
pprint(my_dict['dict'])
print()

my_dict['set'].add("New value")
pprint(my_dict['set'])
