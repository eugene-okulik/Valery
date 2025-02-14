"""
List comprehension
Дан такой кусок прайс-листа:

(Копируйте эту переменную (константу) в код прямо как есть)

PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''
При помощи list comprehension и/или dict comprehension превратите этот текст в словарь такого вида:

{'тетрадь': 50, 'книга': 200, 'ручка': 100, 'карандаш': 70, 'альбом': 120, 'пенал': 300, 'рюкзак': 500}
В выполнении не должно быть циклов.

Обратите внимание, что цены в словаре имеют тип int (они не в кавычках)
"""


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


split_price_list = PRICE_LIST.splitlines()
print(split_price_list)

goods_list = [x.rsplit(' ', 1) for x in split_price_list]
print(goods_list)

goods_dict = {key: int(value[:-1]) for key, value in goods_list}
print(goods_dict)
