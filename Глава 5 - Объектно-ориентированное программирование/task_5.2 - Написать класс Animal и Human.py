"""
Написать класс Animal и Human,сделать так, чтобы некоторые животные были
опасны для человека (хищники, ядовитые).
Другие - нет. За что будет отвечать метод is_dangerous(animal)
"""


class Printer(object):

    def __init__(self):
        self.values = []

    def log(self, *values):
        self.values = [v for v in values]
        print(self.values)


class FormattedPrinter(Printer):

    def formated_log(self, *values):
        print('***' * len(values))
        self.log(*values)
        print('***' * len(values))


if __name__ == '__main__':
    print('\n')
    prt = Printer()
    prt.log(5, 6, 7, 8, 98, 10)

    print('\n')
    f_prt = FormattedPrinter()
    f_prt.formated_log(1, 4, 3, 8, 4, 6, 7, 9)

    print('\n')
    f_prt = FormattedPrinter()
    f_prt.formated_log(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)


