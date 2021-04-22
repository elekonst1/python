# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

#src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [num for num in src if src[next(src)] > src[next(src) - 1]]
# print(result)

# def new_list_generator(i):
#     for num in src:
#         if num in src == src[0]:
#             continue
#         if src[i] > src[i-1]:
#             i += 1
#             yield num
#         else:
#             continue
#
# result = new_list_generator(1)
# print(*result)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
i = 1
while i < len(my_list):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])
        i += 1
    else:
        i += 1
        continue
print(new_list)


