'''

Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


    a = calc_cube(5)
125
    a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: 'wrong val -5


Примечание: сможете ли вы замаскировать работу декоратора?

'''


def main_simple_logger(p_filter):
    def simple_logger(func):
        def wrapper(*args):
            no_valid_list = [x for x in args if x not in list(filter(p_filter, args))]
            if len(no_valid_list) > 0:
                raise ValueError(f'wrong val: {no_valid_list}')
            str_param = ''
            for i in args:
                str_param += f'{i}: {type(i)}, '

            print(f'{str(func).split()[1]}({str_param[:(len(str_param) - 2)]})')

            return func(*args)

        return wrapper

    return simple_logger


@main_simple_logger(lambda x: x > 0)
def fun_func(x, y):
    return x ** 2 + 2 * x * y + y ** 2


print(fun_func(-5, -19))
