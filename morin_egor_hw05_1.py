'''
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
'''


# функция генератор.
def number_generator(number):
    for i in range(1, number + 1, 2):
        yield i

# функция получения следующего эелемента генератора, пока не закончится
def next_generation(number_generator):
    try:
        print(next(number_generator))
    except StopIteration:
        print('...StopIteration...')
        return False
    else:
        return True


number_generator = number_generator(100)
fl = True
# цикл по генератору
while fl:
    fl = next_generation(number_generator)