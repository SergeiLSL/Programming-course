"""
Создать матрицу любых чисел 3 на 4,
сначала вывести все строки, потом все столбцы
https://silvertests.ru/GuideView.aspx?id=34372
"""

m = [
    [5, 6, 7, 8],
    [15, 13, 9, 4],
    [6, 18, 15, 28]
]
x = [x[:] for x in m]
print(x)  # вывод в строку

print()

x = [x[0] for x in m], [x[1] for x in m], [x[2] for x in m], [x[3] for x in m]
print(x)  # вывод всех столбцов в строку

