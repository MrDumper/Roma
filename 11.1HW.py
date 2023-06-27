class House:
    def __init__(self, flats, floors, square):
        self.__flats = flats
        self.__floors = floors
        self.__square = square

    def print_house_flats(self):
        print(f'In this house {self.__flats} flats')

    def print_house_floors(self):
        print(f'In this house {self.__floors} floors')


class Bird:
    def __init__(self, type, speed, age):
        self.__type = type
        self.__speed = speed
        self.__age = age

    def print_bird_type(self):
        print(f'This is {self.__type}')

    def print_bird_speed(self):
        print(f'Speed of this bird is {self.__speed}')


class TShirt:
    def __init__(self, sex, size, color):
        self.__sex = sex
        self.__size = size
        self.__color = color

    def print_tshirt_size(self):
        print(f'Size is {self.__size}')

    def print_tshirt_color(self):
        print(f'Color is {self.__color}')


class Book:
    def __init__(self, name, author, theme):
        self.__name = name
        self.__author = author
        self.__theme = theme

    def print_book_theme(self):
        print(f'Theme of this book is {self.__theme}')

    def print_book_name(self):
        print(f'That book name\'s is {self.__name}')


class Computer:
    def __init__(self, gpu, cpu, ram):
        self.__gpu = gpu
        self.__cpu = cpu
        self.__ram = ram

    def print_computer_ram(self):
        print(f'RAM of this computr - {self.__ram}')

    def print_computer_gpu(self):
        print(f'GPU is {self.__gpu}')


house = House(1, 2, 3)
tshirt = TShirt(4, 5, 6)
bird = Bird(7, 8, 9)
book = Book(0, 'a', 'b')
computer = Computer('c', 'd', 'e')
house.print_house_floors()
house.print_house_flats()
tshirt.print_tshirt_size()
tshirt.print_tshirt_color()
bird.print_bird_speed()
bird.print_bird_type()
book.print_book_theme()
book.print_book_name()
computer.print_computer_ram()
computer.print_computer_gpu()