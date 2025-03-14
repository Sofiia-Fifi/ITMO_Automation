from mimetypes import inited
from symtable import Class

from task_9_checks import Checks


class Input(Checks):

    # def __init__(self, text, loc):
    #     self.loc = loc
    #     self.text = text

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text

search = Input('Поиск','#search')

print(search.text, search.check_text())


class Button(Checks):

    # def __init__(self, text, loc):
    #     self.loc = loc
    #     self.text = text

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text

class Title(Checks):

    # def __init__(self, text, loc):
    #     self.loc = loc
    #     self.text = text

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text

class Link(Checks):

    # def __init__(self, text, loc):
    #     self.loc = loc
    #     self.text = text

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text

address = Input('Работа', '#adress')
order = Button('Заказать', '#order')
basket = Title('Корзина', '#basket')
payment = Link('Оплата', '#payment')

print(address.text, address.check_text())
print(order.text, order.check_text())
print(basket.text, basket.check_text())
print(payment.text, payment.check_text())



