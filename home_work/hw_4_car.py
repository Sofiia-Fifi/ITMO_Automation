class Car:
    def __init__(self, color = None, type = None, year = None):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print('Автомобиль заведен')

    def stop_engine(self):
        print('Автомобиль заглушен')

    def release_year(self, new_year):
        self.year = new_year
        print(f'Год выпуска - {self.year}')

    def auto_type(self, new_type):
        self.type = new_type
        print(f'Тип - {self.type}')

    def auto_color(self, new_color):
        self.color = new_color
        print(f'Цвет - {self.color}')

my_car = Car()

my_car.start_engine()
my_car.stop_engine()
my_car.release_year('2025')
my_car.auto_type('седан')
my_car.auto_color('зеленый')