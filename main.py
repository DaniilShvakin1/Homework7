class Book:
    def __init__(self,  author: str, name: str):
        self.author = author
        self.name = name


    def get_information_book(self):
        return



class Libruary:
    def __init__(self,book: str):
        self.book = book
        self.books = []

    def add_book(self, book: str):
        self.books.append(book)
        print("Книга успешно добленна")

    def remove_book(self, book: list):
        if book in self.books:
            self.books.remove(book)
            print("вы удалили книгу")
        else:
            print("нет такой книги")


book = Libruary()
book1 = Book("Dont now","Harry Potter")
book2 = Book("History","Person")
Libruary.add_book(book1)
Libruary.add_book(book2)
print(("Количество книг в библиотеке"), len(book,book2))
