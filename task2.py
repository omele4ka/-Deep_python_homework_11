# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку. При нового экземпляра класса,
# старые данные из ранее созданных экземпляров сохраняются
# в пару списков-архивов, которые также являются свойствами экземпляра.


class Archive:
    """
    класс хранит пару свойств:
    число и строку.
    При нового экземпляра класса,
    старые данные из ранее созданных экземпляров сохраняются
    в пару списков-архивов, которые также являются свойствами экземпляра
    """
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, number: int) -> None:
        self.text = text
        self.number = number

    def print_archive(self):
        print('Archive Data:')
        for i in range(len(self.old_text)):
            print(f'Text: {self.old_text[i]}, Number: {self.old_int[i]}')


if __name__ == "__main__":
    a1 = Archive(text='T', number=1)
    a2 = Archive(text='E', number=2)
    a3 = Archive(text='Z', number=3)

    print(a2.instance.old_text)
    print(a2.instance.old_int)

    print('---')

    print(a3.text)
    print(a3.number)

    a3.print_archive()