# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

new_list = []
for element in my_list:
    if element.isdigit():
        new_list.extend(['"', f'{int(element):02}', '"'])
    elif (element.startswith('+') or element.startswith('-')) and element[1:].isdigit():
        new_list.extend(['"', f'{element[0]}{int(element):02}', '"'])
    else:
        new_list.append(element)
sentence = ' '.join(new_list)
print(sentence)

# to perfect out (delete whitespaces):
# find indexes with " symbol
symbol_idxs = []
for idx, letter in enumerate(sentence):
    if letter == '"':
        symbol_idxs.append(idx)

# some logic to find delete indexes
for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1

# delete indexes from original string

for del_idx in reversed(symbol_idxs):
    sentence = sentence[:del_idx] + sentence[del_idx+1:]
