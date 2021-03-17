
import csv

def get_dict_files(files_users, files_hobby):
    # счетчик добавления строк None
    count_add = 0

    # открываем файлы для чтения
    with open(files_users) as data_file_fio, open(files_hobby) as data_file_hobby:
        count_file_fio = sum(1 for line in data_file_fio)
        count_file_hobby = sum(1 for line in data_file_hobby)

        data_file_fio.seek(0)
        data_file_hobby.seek(0)

        if count_file_fio < count_file_hobby:
            raise ValueError
        else:
            count_add = count_file_fio - count_file_hobby

        reader_fio = [' '.join(i) for i in list(csv.reader(data_file_fio))]
        reader_hobby = [','.join(i) for i in list(csv.reader(data_file_hobby))]

    # добавим None, если нужно
    while count_add > 0:
        reader_hobby.append(None)
        count_add -= 1

    #  Получаем словарик
    # dict_total = dict(zip(reader_fio, reader_hobby))

    return dict(zip(reader_fio, reader_hobby))


def save_common_file(files_users, files_hobby, save_file):
    # открываем файлы для чтения один для записи
    with open(files_users) as data_file_fio, open(files_hobby) as data_file_hobby, open(save_file,'w+') as file_save:
        # количество строк в документах
        count_file_fio = sum(1 for line in data_file_fio)
        count_file_hobby = sum(1 for line in data_file_hobby)
        # возвращаем
        data_file_fio.seek(0)
        data_file_hobby.seek(0)

        if count_file_fio < count_file_hobby:
            raise ValueError
        # ленивое чтение файла
        reader_fio = csv.reader(data_file_fio)
        reader_hobby = csv.reader(data_file_hobby)

        # цикл до последней фамилии
        while count_file_fio:
            if count_file_hobby == 0:
                file_save.writelines(f'\n{str(next(reader_fio)).strip()}: {None}')
            else:
                file_save.writelines(f'\n{str(next(reader_fio)).strip()}: {next(reader_hobby)}')
                count_file_hobby -= 1

            count_file_fio -= 1


def add_sale(value_money, file_add):

    try:
        fl_money = float(value_money)
    except:
        print('неправильное значение! Введите число!')
        raise ValueError

    with open(file_add, mode='a', encoding='UTF8') as f:
        f.writelines(str(fl_money)+'\n')

def show_sales(file, begin_range='', end_range=''):

    with open(file, mode='r', encoding='UTF8') as file_data:
        data_file = (l for l in file_data.readlines())


    list_data = list(data_file)
    if begin_range != '' and end_range != '':

        if begin_range.isdigit() and end_range.isdigit():
            print(''.join(list_data[int(begin_range):int(end_range)]))
        else:
            print("Введен не верный диапазон!")
            raise SyntaxError
    elif begin_range != '':
        if begin_range.isdigit():
            print(''.join(list_data[int(begin_range):]))
        else:
            print("Введен не верный диапазон!")
            raise SyntaxError
    else:
        print(''.join(list_data))


def replase_money(number_str, value_money, file_add):

    try:
        fl_money = float(value_money)
    except:
        print('неправильное значение суммы! Введите корректное число!')
        raise ValueError

    try:
        i_index = int(number_str)
    except:
        print('неправильное значение индекса! Введите корректное число!')
        raise ValueError

    with open(file_add, mode='r', encoding='UTF8') as f:
        count_file_line = sum(1 for line in f)

    if count_file_line < i_index:
        print('Индекс превышает количество строк в файле')
        raise IndexError
    elif i_index != 0:
        i_index -= 1


    with open(file_add, mode='r+', encoding='UTF8') as f:
        f.seek(i_index)
        f.writelines(str(fl_money)+'\n')

