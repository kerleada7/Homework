'''

*(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — о
бязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

'''


import sys
import general_functions


# командная строка?
if __name__ == "__main__":
    if len(sys.argv) > 2:
        number_str = sys.argv[1]
        value_money = sys.argv[2]
    else:
        number_str = input('Введите номер строки:')
        value_money = input('Введите новую сумму:')
else:
    number_str = input('Введите номер строки:')
    value_money = input('Введите новую сумму:')


general_functions.replase_money(number_str, value_money, 'bakery.csv')