"""
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
“Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
dignissim vitae libero” и после этого выводит получившийся текст на экран. Знаки препинания не должны
оказаться внутри слова. Если после слова идет запятая или точка, этот знак препинания должен идти после
того же слова, но уже преобразованного.
"""


my_text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
          "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

added_postfix = "ing"

my_parsed_text = my_text.split()
my_parsed_text_with_postfix = []

for item in my_parsed_text:
    # Проверяем наличие знаков препинания
    if '.' in item or ',' in item:
        punctuation = item[-1] # Сохраняем последний символ в слове как знак препинания
        item = item[:-1] # Убираем последний символ из слова
        item = item + added_postfix + punctuation # Добавляем 'ing' и возвращаем знак препинания
    else:
        item = item + added_postfix # Если знаков препинания нет, просто добавляем 'ing'

    my_parsed_text_with_postfix.append(item)

# Соединяем слова обратно в строку
my_new_text = ' '.join(my_parsed_text_with_postfix)
print(my_new_text)
