from mimetypes import inited
from symtable import Class


class Input:

    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

# search = Input('Местоположение')
#
# print(search.loc)


class Button:

    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

class Title:

    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

class Link:

    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

adress = Input('Работа', '#adress')
order = Button('Заказать', '#order')
basket = Title('Корзина', '#basket')
payment = Link('Оплата', '#payment')

print(adress.text, adress.loc)
print(order.text, order.loc)
print(basket.text, basket.loc)
print(payment.text, payment.loc)
