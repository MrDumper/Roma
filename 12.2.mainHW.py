from classesHW import Circle, Point, Square, Triangle

figures = [Circle(Point(1, 1), 5), Triangle(Point(1, 1), Point(1, 5), Point(3, 3)), Square(Point(1, 1), Point(2, 2))]

for figure in figures:
    print(f'Figure - {figure.class_name} perimeter = {figure.perimeter()}, square = {figure.square()}\n')
