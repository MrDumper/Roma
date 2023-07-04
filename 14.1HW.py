# Написать свой класс MyOpen, объекты которого должны поддерживать протокол контекстного менеджера.
# Он должен работать аналогично with open(‘file.txt’, ‘w+’) as f.
# Т.е вы можете применять его следующим образом:
# with MyOpen(file.txt’, ‘w+’) as f:

class MyOpen:
    def __init__(self, file_name, type_of_open):
        self._file = open(file_name, type_of_open)

    def __enter__(self):
        print("Сработал __enter__")
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Сработал __exit__")
        self._file.close()


with MyOpen("123.txt", "r") as f:
    print(f"Первая строка файла: {f.readline()}")
