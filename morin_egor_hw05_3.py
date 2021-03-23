'''
Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''

# создаем генератор
def tutors_generator(tutors, klasses):

    # Добавим None по необходимости.
    if len(tutors) > len(klasses):
        while len(tutors) > len(klasses):
            klasses.append(None)

    # Наш генератор.
    for i in range(len(tutors)):
        yield tutors[i], klasses[i]

# функция получения следующего эелемента генератора, пока не закончится
def next_generation(generator):
    try:
        print(next(generator))
    except StopIteration:
        print('...StopIteration...')
        return False
    else:
        return True


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_generator = tutors_generator(tutors, klasses)
fl = True
# цикл по генератору
while fl:
    fl = next_generation(tutors_generator)