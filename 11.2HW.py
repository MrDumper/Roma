class MyException(Exception):
    print("your speed is below zero!")


class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = 0

    def message_about_reduce(self):
        print(f'Your speed has been reduced: {self.speed}')

    def increase_speed(self):
        if self.speed >= 0:
            self.speed = self.speed + 5
        print(f'Your speed has been increased: {self.speed}')

    def reduce_speed(self):
        try:
            if self.speed - 5 < 0:
                raise MyException
            self.speed = self.speed - 5
            print(f'Your speed has been reduced: {self.speed}')
        except MyException:
            print("MyException get called!")

    def stop_car(self):
        try:
            self.speed = 0
            print('Car stopped')
        except(self.speed == 0):
            print('Your car has been stopped already!')

    def print_speed(self):
        print(f'Your speed is: {self.speed}')

    @staticmethod
    def reverse_car():
        print('You have been reversed')


car = Car('BMW', 'M5 Competition', 2022)
car.increase_speed()
car.reverse_car()
car.print_speed()
car.increase_speed()
car.reduce_speed()
car.stop_car()
car.print_speed()
car.stop_car()
car.reduce_speed()