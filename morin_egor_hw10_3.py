'''
Осуществить программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
    сложение (__add__()),
    вычитание (__sub__()),
    умножение (__mul__()),
    деление (__floordiv____truediv__()).
Эти методы должны применяться только к клеткам и выполнять
    увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
    больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
В этом случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
Тогда метод make_order() вернёт строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке
    (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).
'''


class Cell:
    def __init__(self, cell_count):
        try:
            if cell_count <= 0:
                raise ValueError('Количество клеток должно быть больше 0')

            self.cell_count = int(cell_count)
        except:
            raise ValueError('Количество клеток должно быть задано числом')

    def __str__(self):
        return str(f' Количество клеток: {self.cell_count}')

    def __add__(self, other):
        if type(other) != Cell:
            ValueError('Сложение выполняется только клетка с клеткой')
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if type(other) != Cell:
            ValueError('Вычитание выполняется только клетка с клеткой')

        if self.cell_count < other.cell_count:
            ValueError('Клетка не может быть отрицательной, но может быть мертвой = 0')

        return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        if type(other) != Cell:
            ValueError('Умножение выполняется только клетка с клеткой')

        return Cell(self.cell_count * other.cell_count)

    def __floordiv__(self, other):
        if type(other) != Cell:
            ValueError('Деление выполняется только клетка с клеткой')

        if other.cell_count == 0:
            ValueError('Делить на мертвую клетку нельзя')

        return Cell(self.cell_count // other.cell_count)

    def __truediv__(self, other):
        if type(other) != Cell:
            ValueError('Деление выполняется только клетка с клеткой')

        if other.cell_count == 0:
            ValueError('Делить на мертвую клетку нельзя')

        return Cell(self.cell_count % other.cell_count)

    @staticmethod
    def make_order(cell, row_count):
        print(f'Количество клеток: {cell.cell_count}; Количество клеток в ряду: {row_count}')
        return '\n'.join('*' * row_count for i in range(cell.cell_count // row_count)) + '\n' + '*' * (cell.cell_count % row_count)


cell_mobius = Cell(22)
print(cell_mobius)

cell_sirius = Cell(11)
print(cell_sirius)

print(cell_mobius // cell_sirius)

print(Cell.make_order(cell_mobius, 5))
