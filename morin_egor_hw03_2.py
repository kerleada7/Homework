'''
*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
    num_translate_adv("One")
"Один"
    num_translate_adv("two")
"два"
'''

def num_translate_adv(num):
    # Словарь для хранения соответветствий англ. и рус.
    number_dict = {
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
        'ten': 'десять',
        'eleven': 'одинадцать',
        'twelve': 'двенадцать',
        'thirteen': 'тринадцать',
        'fourteen': 'четырнадцать',
        'fifteen': 'пятнадцать',
        'sixteen': 'шестнадцать',
        'seventeen': 'семнадцать',
        'eighteen': 'восемнадцать',
        'nineteen': 'девятнадцать',
        'twenty': 'двадцать',
    }

    number_translate = number_dict.get(num.lower())

    if number_translate != None:
        if num[0].islower():
            return number_translate
        else:
            return number_translate.capitalize()
    else:
        return None


print(num_translate_adv('One'))
print(num_translate_adv('twenty'))
print(num_translate_adv('skdfhl00'))

print(num_translate_adv(input('Введите число прописью на англ.: ')))