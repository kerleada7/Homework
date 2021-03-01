'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
 (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
     get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово
можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
'''

import random

def get_randon_value(list):
    # получаем радномное значение в зависимости от длины списка
    number_lucky = random.randrange(len(list))
    return list[number_lucky]

def get_jokes(count_repeat=1, use_once=False):

    # результирующий спсиок
    result_list = []

    # Наборы данных
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    i = 0
    # Цикл на повторения
    while i<count_repeat:
        i+=1

        #  если один из список пустой прекратим цикл
        if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
            result_list.append('Один из списков закончился!')
            break

        # получаем рандомные значения
        nouns_value = get_randon_value(nouns)
        adverbs_value = get_randon_value(adverbs)
        adjectives_value = get_randon_value(adjectives)

        #  добавляем рандомные значения в список
        result_list.append(f'{nouns_value} '
                           f'{adverbs_value} '
                           f'{adjectives_value}')

        # если использовать можно 1 раз, то после использования удаляем из списка
        if use_once:
            nouns.remove(nouns_value)
            adverbs.remove(adverbs_value)
            adjectives.remove(adjectives_value)


    return result_list

# Вывод
print(get_jokes(2))
print(get_jokes(5, True))
print(get_jokes(10, True))