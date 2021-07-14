"""
Пользователь вводит число, если оно четное -
выбрасываем исключение ValueError, если оно
меньше 0 - TypeError, если оно больше 10 - IndexError.
Обрабатываем ошибку, говорим пользователю, в чем его ошибка.
"""


def result(i):
    if i % 2 == 0:
        raise ValueError
    elif i < 0:
        raise TypeError
    elif i > 10:
        raise IndexError
    else:
        return 'Правильное число.'

# try:
#
# except


for i in [-1, 2, 11]:
    try:
        result(i)
    except ValueError as e:
        print('Возникла ошибка значения')
    except TypeError as e:
        print('Возникла ошибка типа', e)
    except IndexError as e:
        print('Возникла ошибка индекса', e)

a = int(input())
print(result(a))
