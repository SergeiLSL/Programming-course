"""
Выберем числа кратные 5 в диапазоне чисел
"""

# 1 вариант

n, m = int(input()), int(input())
s = []
if n >= m:
    n, m = m, n

for i in range(n, m + 1):
    if i % 5 == 0:
        s.append(i)

print(*s)

# 2 вариант
print(*[i for i in range(n, m + 1) if i % 5 == 0])

# 3 вариант для развлечения

# def convert():
#     print("Выберем числа кратные 5 в диапазоне чисел 'm' и 'n' \nпри условии n > m")
#     m = int(input('Введите число m: '))
#     n = int(input('Введите число n: '))
#     if m < n:
#         print([x for x in range(m, n + 1) if x % 5 == 0])
#     if m > n:
#         print("'m' должно быть больше 'n'!!!")
#
#
# convert()
# while True:
#     flag = input('Ещё раз? [y/n]: ')
#     if flag == 'y':
#         convert()
#     else:
#         print('Good bay')
#         break
