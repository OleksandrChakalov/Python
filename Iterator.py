class ListIterator():
    def __init__(self, collection, cursor):
        """
        :param collection: список
        :param cursor: іднекс з якого починається перебір.
        також повинна бути перевірка -1 >= cursor < len(collection)
        """
        super().__init__(collection, cursor)

    def first(self):
        """
        Початкове значення курсора -1.
        Тому що потрібно буде викликати next, який зсуне його на 1
        """
        self._cursor = -1

    def next(self):
        """
        якщо курсор вказує на останній елемент, то викликаємо StopIteration,
       або зсуваємо курсор на 1
        """
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        """
        повертаємо елемент
        """
        return self._collection[self._cursor]

class ListCollection():
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)


collection = (1, 2, 5, 6, 8)
aggregate = ListCollection(collection)
itr = aggregate.iterator()

# обход коллекции
while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())