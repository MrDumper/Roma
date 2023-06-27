import classesHW

figures = [classesHW.Circle(classesHW.Point(1, 1), 5), classesHW.Triangle(classesHW.Point(1, 1), classesHW.Point(1, 5), classesHW.Point(3, 3)), classesHW.Square(classesHW.Point(1,1), classesHW.Point(2, 2))]

for figure in figures:
    print(f'Figure - {figure.class_name} perimeter = {figure.perimeter()}, square = {figure.square()}\n')