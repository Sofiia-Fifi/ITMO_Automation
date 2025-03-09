def take_arg (a=(1,2,3,4)):
    return a[1]

print(take_arg())
print(take_arg((3,4,5,6))) #задаем новый кортеж


def find_sq (radius, pi=3.14159):
    return pi*radius**2

print(find_sq(2))

def fn_l(s:str = ' ') -> int:
    return len(s)

print(fn_l('Hello world!'))

def req_22(n: list, m: list) -> int:
    return max(len(n), len(m))
print(req_22([1,2,3,4], [4,5,6,7,8,9]))

def free_list(a: list):
    a.append('test')
    return a

print(free_list([1,2,3]))

def num_list(b: list) ->int:
    result = 0
    for elem in b:
        result = result+elem
    return result

print(num_list([1,2,3,4]))