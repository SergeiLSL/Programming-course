# http://codegists.com/snippet/python/hw_day1_extra3-4py_borisrubin_python
# Task 4 Напишите программу, которая выводит все кратные 5 числа
# между двумя пользовательскими числами
 
# вводим два числа типа int так как должны быть кратны 5
print('\n\nЗадание 2:   \nНайдем все числа в заданном 2 числами диапазоне кратные 5\n')
num1 = int(input('Введите 1-ое число: '))
num2 = int(input('Введите 2-ое число: '))
 
numbers = list(x for x in range(num1, num2) if x % 5 == 0)
print(numbers)