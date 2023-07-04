# Написать генератор, который будет принимать на вход имя файла и
# генерировать построчно(т.е yield каждой строки).

def generator(f_name):
    f = open(f_name, 'r')
    while True:
        line = f.readline()
        if not line:
            print("EoF! Goodbye!")
            f.close()
            yield line
        else:
            yield print(line)


s = generator('123.txt')
next(s)
next(s)
