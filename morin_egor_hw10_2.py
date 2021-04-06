'''
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Cloth(ABC):

    @abstractmethod
    def __init__(self):
        self.__size_сloth= 0

    @property
    def size_сloth(self):
        return self.__size_сloth

    @size_сloth.setter
    def size_сloth(self, value):
        self.__size_сloth = value


class MySuit(Cloth):
    def __init__(self):
        super().__init__()

    @property
    def сloth_count(self):
        return 2 * self.size_сloth + 0.3

    def __str__(self):
        return f'Для костюма необходимо материала: {self.сloth_count} м.'

class MyCoat(Cloth):
    def __init__(self):
        super().__init__()

    @property
    def сloth_count(self):
        return self.size_сloth / 6.5 + 0.5

    def __str__(self):
        return f'Для пальто необходимо материала: {self.сloth_count} м.'

# Костюм
suit = MySuit()
suit.size_сloth = 10
print(suit)

# Пальто
coat = MyCoat()
coat.size_сloth = 45
print(coat)