'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86
3 5 32
2 4 6
-1 64 -8
3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр
'''



class Matrix:

    def __init__(self, matrix_list):
        self.h = len(matrix_list)
        self.w = len(matrix_list[0])
        self.matrix_list = matrix_list


    def __str__(self):
        str_matrix = '\n'.join(list(map(lambda x: ' '.join([str(i) for i in x]), self.matrix_list)))
        return str_matrix

    def __add__(self, other):

        if self.h != other.h or self.w != other.w:
            raise Exception('Ошибка. Матрицы отличаются размерами!')

        result = [[(l[0] + l[1]) for l in zip(i[0], i[1])] for i in zip(self.matrix_list, other.matrix_list)]
        return Matrix(result)




Matrix1 = Matrix([[1, 2, 3], [3, 4, 5], [5, 5, 5], [8, 2, 1]])
print(Matrix1, end='\n\n')
Matrix2 = Matrix([[3, 2, 4], [1, 2, 1], [3, 4, 5], [3, 3, 7]])
print(Matrix2, end='\n\n')
print(Matrix1 + Matrix2)