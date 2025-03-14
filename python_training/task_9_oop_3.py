class Soda:

    def __init__(self, add):
        self.add = add

    def show_my_drink(self):
        if self.add is not None:
            print('Газировка и {}'.format(self.add))
        else:
            print('Обычная газировка')

lime = Soda(None)
orange = Soda('Апельсин')

lime.show_my_drink()
orange.show_my_drink()


# Решение из лекции
class Soda:

    def __init__(self, add = None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print(f'Газировка и {self.add}')  #  То же, что и .format
        else:
            print('Обычная газировка')

lime = Soda()
orange = Soda('Апельсин')

lime.show_my_drink()
orange.show_my_drink()