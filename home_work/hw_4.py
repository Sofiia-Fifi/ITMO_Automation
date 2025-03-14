# Задача 1
print('\n', 'Задача 1', '\n')
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rec1 = Rectangle(2,3)
rec2 = Rectangle(6.2, 5)
rec3 = Rectangle(12, 128)

print('S = ', rec1.square(), 'P = ', rec1.perimeter())
print('S = ', rec2.square(), 'P = ', rec2.perimeter())
print('S = ', rec3.square(), 'P = ', rec3.perimeter())

# Задача 2
print('\n', 'Задача 2', '\n')

class Math:

    def __init__(self, a=10, b=2):
        self.a = a
        self.b = b

    def addition (self):
        return self.a + self.b

    def multiplication (self):
        return self.a * self.b

    def division (self):
        return self.a / self.b

    def subtraction (self):
        return self.a - self.b

number = Math(10, 2)

print(number.addition())
print(number.multiplication())
print(number.division())
print(number.subtraction())

# Задача 3
print('\n', 'Задача 3', '\n')

class ButtonsSideBar:

    def __init__(self, text, type = 'Кнопка', loc=None):
        self.text = text
        self.type = type
        self.loc = loc

    def press_button(self):
        print(f'Клик по кнопке {self.text}')

b1 = ButtonsSideBar('Text Box')
b2 = ButtonsSideBar('Check Box')
b3 = ButtonsSideBar('Radio Button')
b4 = ButtonsSideBar('Web Tables')
b5 = ButtonsSideBar('Buttons')
b6 = ButtonsSideBar('Links')
b7 = ButtonsSideBar('Broken Links - Images')
b8 = ButtonsSideBar('Upload and Download')
b9 = ButtonsSideBar('Dynamic Properties')

b1.press_button()
b2.press_button()
b3.press_button()
b4.press_button()
b5.press_button()
b6.press_button()
b7.press_button()
b8.press_button()
b9.press_button()
