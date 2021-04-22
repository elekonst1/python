# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
number = int(input('Введите произвольное положительное число: '))
odd_numbers = (num for num in range(1, number + 1, 2))
print(*odd_numbers)


