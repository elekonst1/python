# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
eng_rus_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translator(eng_word):
    if eng_word[0] == eng_word[0].capitalize():
        eng_word = eng_word.lower()
        return eng_rus_dict[eng_word].capitalize()
    else:
        return eng_rus_dict[eng_word]

eng_number = input("Введите цифру от 0 до 10 на английском для получения перевода: ")
print(num_translator(eng_number))