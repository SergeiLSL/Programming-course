"""
task_3.1 - Обработка исключений

Пользователь вводит число, если оно четное -
выбрасываем исключение ValueError, если оно
меньше 0 - TypeError, если оно больше 10 - IndexError.
Обрабатываем ошибку, говорим пользователю, в чем его ошибка.

"""


def result(x):
    try:
        if n < 0:
            raise TypeError
        elif n > 10:
            raise IndexError
        elif n % 2 == 0:
            raise ValueError
        else:
            return 'Правильно'

    except TypeError:
        return 'Число должно быть больше нуля'
    except IndexError:
        return 'Число должно быть меньше десяти'
    except ValueError:
        return 'Число должно быть меньше нечетным'


n = int(input())
print(result(n))

# ---------------------------------------------------

n = int(input())
try:
    if n < 0:
        raise TypeError
    elif n > 10:
        raise IndexError
    elif n % 2 == 0:
        raise ValueError
    else:
        print('Правильно')

except TypeError:
    print('Число должно быть больше нуля')
except IndexError:
    print('Число должно быть меньше десяти')
except ValueError:
    print('Число должно быть меньше нечетным')

n = int(input())
result(n)
