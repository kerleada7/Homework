'''
2.	Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
a.	Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
b.	К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
c.	* Решить задачу под пунктом b, не создавая новый список.
'''


# Создание списка кубов
cube_number = 1
list_cube = []
while cube_number <= 1000:
    if cube_number % 2 != 0:
        list_cube.append(cube_number ** 3)

    cube_number += 1

# Переменные для хранения итоговых сумм
sum_element_paragraph_a = 0
sum_element_paragraph_b = 0

# цикл по элементам списка
for element in range(0, len(list_cube)):

    # временная переменная для получения суммы текущего числа
    temp_sum_element = 0
    # конверитруем число в строку, для вычисления суммы всех цифр
    str_element = str(list_cube[element])
    for i in str_element:
        temp_sum_element += int(i)

    # если вычисленная сумма делится на 7, складываем
    if temp_sum_element % 7 == 0:
        sum_element_paragraph_a +=list_cube[element]

# цикл по элементам списка
for element in range(0, len(list_cube)):

    list_cube[element] += 17

    # временная переменная для получения суммы текущего числа
    temp_sum_element = 0
    # конверитруем число в строку, для вычисления суммы всех цифр
    str_element = str(list_cube[element])
    for i in str_element:
        temp_sum_element += int(i)

    # если вычисленная сумма делится на 7, складываем
    if temp_sum_element % 7 == 0:
        sum_element_paragraph_b += list_cube[element]

# Вывод данных
print(f' Сумма чисел по условию a: {sum_element_paragraph_a}')
print(f' Сумма чисел по условию b: {sum_element_paragraph_b}')