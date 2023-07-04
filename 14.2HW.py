# Написать свой итератор(реализовать у него и метод __next__ и __iter__),
# чтобы при обходе циклом он отдавал только элементы на четных индексах, возведенные в квадрат.

class MyIterator:
    def __init__(self, collection, cursor=-1):
        self._collection = collection
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor >= len(self._collection):
            raise StopIteration
        if self._cursor % 2 == 0:
            res = self._collection[self._cursor] ** 2
            self._cursor += 1
            return res
        self._cursor += 1


collection_1 = MyIterator([1, 2, 3, 4, 5])

for i in collection_1:
    if i is None:
        continue
    else:
        print(i)