class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isavailable = True

    def show_info(self):
        if self.isavailable :
            print(f"{self.title} by {self.author} is available.")

        else:
            print(f"{self.title} is Currently Not available!")

    def borrow_book(self):
        if self.isavailable:
            self.isavailable = False
            print(f"{self.title} was borrowed successfully!")
        else:
            print("This book is already borrowed.")

    def return_book(self):
        if not self.isavailable:
            self.isavailable = True
            print(f"{self.title} has been returned")
        else:
            print("Already returned cannot returned")


class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("Library has no books.")
        else:
            for each_book in self.books:
                each_book.show_info()

    def search_book(self, title):
        for book_name in self.books:
            if title == book_name.title:
                print("Here")
                return
        else:
            print("not here")


book1 = Book("Atomic Habits", "James Clear")
book2 = Book("The Alchemist", "Paulo Coelho")

library1 = Library()

library1.add_books(book1)
library1.add_books(book2)

library1.search_book("Atomic Habits")