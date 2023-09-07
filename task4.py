# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников
# по площади
# Должны работать все шесть
# операций сравнения


class Rectangle:
    """
    Класс с возможностью сложения и вычитания
    прямоугольников, создает новый экземпляр.
    Содержит методы calc_len, calc_square для
    вычисления периметра и площади прямоугольника,
    методы __add__ и __sub__ для вычисления
    суммы и разницы перемитров,
    и дандер-методы для сравнения прямоугольников по площади
    Отрицательные значения не допускаются.
    """
    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_square(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length_cm=
                         (self.length + other.length),
                         width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=
                         abs(self.length - other.length),
                         width_cm=self.width)

    def __eq__(self, other: "Rectangle"):
        return self.calc_square() == other.calc_square()

    def __lt__(self, other: "Rectangle"):
        return self.calc_square() < other.calc_square()

    def __gt__(self, other: "Rectangle"):
        return self.calc_square() > other.calc_square()

    def __ge__(self, other: "Rectangle"):
        return self.calc_square() >= other.calc_square()

    def __le__(self, other: "Rectangle"):
        return self.calc_square() <= other.calc_square()

    def print_rectangle(self):
        print(f'Длина: {self.length} см')
        print(f'Ширина: {self.width} см')
        print(f'Периметр: {self.calc_len()} см')
        print(f'Площадь: {self.calc_square()} см')


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2,
                   width_cm=2)
    r1.print_rectangle()
    print('---')

    r2 = Rectangle(length_cm=3)
    r2.print_rectangle()

    r3 = r2 + r1

    print('---')
    r3.print_rectangle()

    print('---')
    print(r1 == r2)
    print(r1 <= r2)
    print(r1 >= r2)
