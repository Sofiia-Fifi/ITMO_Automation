def test_passing ():
    assert (1, 2, 3) == (1, 2, 3,)

#
# def test_fail():
#     assert 'test'== 'testing'
#

#функция для проверки на несоответствие
def test_not():
    a = 'test'
    b = 'testing'
    assert not a == b


def test_num1():
    x = ["a", "b", "c"]
    y = [1, 2, 3]
    assert  x != y