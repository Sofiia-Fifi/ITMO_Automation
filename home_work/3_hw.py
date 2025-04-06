# Задача 1

def compare (a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print('Числа равны')

compare(3, -6)


# Задача 2

def yes_no(a, b):
    if abs(a-b) == 135:
        print('Yes')
    else:
        print('No')

yes_no(100, 235)


# Задача 3

def month(n):
    if n in range (3,6):
        print('Время года - весна')
    elif n in range (6, 9):
        print('Время года - лето')
    elif n in range (9,12):
        print('Время года - осень')
    elif n in (1,2, 12):
        print('Время года - зима')
    else:
        print('Проверьте введенное значение')

month(2)

# Задача 4

def ten_or_not(t, e, n):
    if (t and e  and n) > 10:
        print('Yes')
    else:
        print('No')

ten_or_not(11, 12, 15)


# Задача 5*

def five_list(l: list) -> int:
    if len(l) > 5:
        print('Введено больше пяти значений списка')
    else:
        positive_numbers = [num for num in l if num >0]
        print (len(positive_numbers))


five_list([1, 2, 5, 6, 7])

# Задача 6*

def days_in_years(y: int, m: int):
    if y >0 and m in range (1, 13):
        days_count = y * m * 29
        print (days_count)
    elif y==0 and m in range (1, 13):
        days_count = m * 29
        print (days_count)
    elif y >=0 and m == 0:
        days_count = y*12*29
        print (days_count)
    else:
        print('Введите корректные данные: год - не меньше 0, месяц - от 1 до 12')


days_in_years(5, 6)
