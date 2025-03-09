# Задача 1
#через print
print("Задача 1")
def task_1() -> str:
    a: int = 5
    b: float = 3.6
    c: str ='строка'
    d: list = [1,2,3,4,5]
    e: bool = False
    print('a-', type(a))
    print('b-', type(b))
    print('c-', type(c))
    print('d-', type(d))
    print('e-', type(e))

task_1()


# # через цикл
# def task_1() -> str:
#     a: int = 5
#     b: float = 3.6
#     c: str ='строка'
#     d: list = [1,2,3,4,5]
#     e: bool = False
#     values ={'a': a, 'b': b, 'c':c, 'd':d, 'e':e}
#     for name,value in values.items():
#         print(name, '-', type(value))
#
# task_1()


# Задача 2
print('\n'+"Задача 2")
def task_2() -> list:
    j = [1, 2, 3, 5, 8, 13, 21]
    print (j[0:3])

task_2()
# последовательность чисел Фибоначи

# Задача 3
print('\n'+"Задача 3" )
def task_3():
    x = 8
    return x**2

print(task_3())