# Программа проверяет, является ли число положительным или отрицательным, и выводит соответствующее сообщение

# Задание 1.

num = 3
# num = -5
# num = 0


if num >=0:
    print ('Число больше, либо равно 0')
else:
    print('Число отрицательное')


# Задача 1: Напишите программу, которая отвечает "Да" или "Нет" на вопрос содержит ли str_1 в себе str_2?
# str_2 = 'test1'
# str_1 = 'test'

def yes_no(str_1, str_2):
    if str_1 in str_2:
        print ('Да')
    else:
      print('Нет')

yes_no(str_1 = 'test', str_2 = 'test1')

# Задание 2

# num_float = 3.4
# num_float = 0
num_float = -5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:                 # Дополнительная проверка
    print('Ноль')
else:
    print('Отрицательное число')

# составные условия if-or

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('печать запрещена')

# Задача 2
# in range (5, 7) от 5 до 7 - не включается в диапазон

def degree(year):
    if 1 <= year <= 4:
        print('Бакалавр')
    elif 5 <= year <= 6:
        print('Магистр')
    elif 7 <= year <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

degree(4)

# Задача 3

def compare(numb):
    if numb > 100 or numb <-100:
        print('-')
    else:
        print('+')

compare(-300)