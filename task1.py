# Создайте класс МояСтрока где будут доступны
# все возможности str и дополнительно
# хранится имя автора строки и время создания (time.time)


import time


class MyStr(str):
    """
    Класс, которому доступны все возможности str,
    а также в котором хранится строка с именем автора
    и временем создания строки
    """
    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time_create = time.time()
        return instance

    def __repr__(self):
        return f'MyStr({self.value =}, {self.name =}, {self.time_create =})'

    def print_to_console(self):
        print(self)


if __name__ == "__main__":
    str1 = MyStr(value="Это моя строка", name='Mila')
    print(repr(str1))
    print(str1.name)
    print(str1.time_create)

    str1.print_to_console()