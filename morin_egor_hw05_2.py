'''
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
'''


# функция генератор.
def number_generator(number):
    return (i for i in range(1, number + 1, 2))

# функция получения следующего эелемента генератора, пока не закончится
def next_generation(number_generator):
    try:
        print(next(number_generator))
    except StopIteration:
        print('...StopIteration...')
        return False
    else:
        return True



number_generator = number_generator(20)
fl = True
# цикл по генератору
while fl:
    fl = next_generation(number_generator)