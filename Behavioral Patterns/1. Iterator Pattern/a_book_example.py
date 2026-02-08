# Components Covered
    # Iterator (interface / abstraction)
    # Concrete Iterators (Forward, Reverse)
    # Aggregate (Collection interface)
    # Concrete Aggregate
    # Client usage



# 1. Iterator Interface
from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Step 2: IterableCollection Interface
class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

    @abstractmethod
    def create_reverse_iterator(self):
        pass


# Step 3: Concrete Collection (Books)
class BookCollection(IterableCollection):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def get_book_at(self, index):
        return self._books[index]

    def get_size(self):
        return len(self._books)

    def create_iterator(self):
        return ForwardBookIterator(self)

    def create_reverse_iterator(self):
        return ReverseBookIterator(self)


# Step 4: Concrete Iterators
class ForwardBookIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self):
        return self._index < self._collection.get_size()

    def next(self):
        book = self._collection.get_book_at(self._index)
        self._index += 1
        return book


class ReverseBookIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = collection.get_size() - 1

    def has_next(self):
        return self._index >= 0

    def next(self):
        book = self._collection.get_book_at(self._index)
        self._index -= 1
        return book

    
# 5. CLIENT CODE
def book_reader_demo():
    collection = BookCollection()
    collection.add_book("Clean Code")
    collection.add_book("Design Patterns")
    collection.add_book("Refactoring")

    print("Forward Reading Order:")
    iterator = collection.create_iterator()
    while iterator.has_next():
        print(iterator.next())

    print("\nReverse Reading Order:")
    reverse_iterator = collection.create_reverse_iterator()
    while reverse_iterator.has_next():
        print(reverse_iterator.next())

def book_reader_demo():
    collection = BookCollection()
    collection.add_book("Clean Code")
    collection.add_book("Design Patterns")
    collection.add_book("Refactoring")

    print("Forward Reading Order:")
    iterator = collection.create_iterator()
    while iterator.has_next():
        print(iterator.next())

    print("\nReverse Reading Order:")
    reverse_iterator = collection.create_reverse_iterator()
    while reverse_iterator.has_next():
        print(reverse_iterator.next())

book_reader_demo()