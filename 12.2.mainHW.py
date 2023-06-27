import classesHW

figures = [classesHW.Circle(1, 1, 10), classesHW.Triangle(1, 1, 5, 1, 3, 3), classesHW.Square(1, 1, 2, 2)]

for figure in figures:
    print(f'perimeter = {figure.perimeter()}, square = {figure.square()}\n')