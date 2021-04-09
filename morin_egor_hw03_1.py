'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
    num_translate("one")
"один"
    num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
'''

def num_translate(num):
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

    # возврат результата
    return number_dict.get(num)

# проверка
print(num_translate('one'))
print(num_translate('twenty'))
print(num_translate('skdfhl00'))

print(num_translate(input('Введите число прописью на англ.: ')))

