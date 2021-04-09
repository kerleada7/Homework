'''

Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3


    a = calc_cube(5)
5: <class 'int'>


Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:
    a = calc_cube(5)
calc_cube(5: <class 'int'>)

'''

def simple_logger(func):
    def wrapper(*args, **kwargs):
        str_param = ''
        for i in args:
            str_param += f'{i}: {type(i)}, '

        for i in kwargs:
            str_param += f'{i}: {type(i)}, '

        print(f'{str(func).split()[1]}({str_param[:(len(str_param)-2)]})')

        return func(*args, **kwargs)
    return wrapper


@simple_logger
def fun_func(x, y, comment):
    print(comment)
    return x**2+2*x*y+y**2

print(fun_func(2, 4, comment='Результат функции:'))