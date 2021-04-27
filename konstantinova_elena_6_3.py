# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много
# раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

from itertools import zip_longest
import json
mutual_dict = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        users_lines_count = sum(1 for line in users)
        hobby_lines_count = sum(1 for line in hobby)

        if users_lines_count < hobby_lines_count:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_users_hobby in zip_longest(users, hobby):
            if line_users_hobby is not None:
                mutual_dict[line_user.strip()] = line_users_hobby.strip()
            else:
                mutual_dict[line_user.strip()] = line_users_hobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(mutual_dict, f, ensure_ascii=False)
print(mutual_dict)

