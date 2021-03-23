'''
3.	Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
'''

# запрос на число процента
input_number = input('Введите число процента: ')

# проверка на число
if input_number.isdigit():
    # конвертируем в число
    int_percent = int(input_number)
    # получем число на которое оканчивается введеный процент
    percent = int_percent % 10
    # по условию задачи до 20
    if percent <= 20 or percent > 0:

        # Если число оканчивается на 1, но не оканчивается на 11, то вариант 1 (Именительный падеж)
        if percent == 1 and int_percent != 11:
            print(f'{input_number} процент')
        # Если число оканчивается на 2, 3, 4, и не оканчивается на 12, 13, 14, то вариант 2 (Родительный падеж)
        elif percent in [2, 3, 4] and int_percent not in [12, 13, 14]:
            print(f'{input_number} процента')
        # Всё остальное — вариант 3 (Множественный родительный падеж)
        else:
            print(f'{input_number} процентов')
    else:
        print('Введено не корректное число процента. Допустимый диапазон от 0 до 20')

else:
    print('Введено не корректное число процента')