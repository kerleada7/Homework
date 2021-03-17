'''
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
    thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?
'''


def thesaurus_adv(*args):
    # Наш словарик
    dict_thesaurus = {}

    # цикл по именам и фамилиям
    for name_surname in args:
        # Получили имя и фамилию
        name, surname = name_surname.split()

        # Если в словаре нет ключа с нашей буквой, то записываем туда ключ буква Фамилиии
        # Если есть, то добавим новый словарь
        if dict_thesaurus.get(surname[0]) == None:

            # добавляем словарь в словарь
            dict_thesaurus[surname[0]] = {}
            # добавляем по ключу имени и фильтруем весь список на совпадение по первым буквам имени и фамилиии
            dict_thesaurus[surname[0]][name[0]] = list(filter(lambda x: x[0]==name[0] and x.split()[1][0]==surname[0],  args))
        else:
            # Если в словаре нет ключа с нашей буквой, то записываем туда ключ буква имени
            if dict_thesaurus[surname[0]].get(name[0]) == None:
                # добавляем по ключу имени и фильтруем весь список на совпадение по первым буквам имени и фамилиии
                dict_thesaurus[surname[0]][name[0]] = list(filter(lambda x: x[0]==name[0] and x.split()[1][0]==surname[0],  args))
                
    return dict_thesaurus

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Егор Иванов", "Егор Никтин"))
