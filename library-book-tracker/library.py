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
        for same_book in self.books:
            if book.title.lower() ==  same_book.title.lower():
                print("You can't add the same book twice.")
                return
        else:
            self.books.append(book)
            print(f"{book.title}, Successfully Added!")


    def show_books(self):
        if not self.books:
            print("Library has no books.")
        else:
            for each_book in self.books:
                each_book.show_info()

    def search_book(self, title):

        for book_name in self.books:
            if title.lower() == book_name.title.lower():
                book_name.show_info()

                return
        else:
            print(f"{title} was not found in the library.")

    def remove_book(self, remove_name):
        for remove_book in self.books:
            if remove_name.lower() == remove_book.title.lower():
                self.books.remove(remove_book)
                print(f"{remove_name} successfully removed!")
                return
        else:
            print(f"{remove_name} Not Found, couldn't remove!")

book1 = Book("Atomic Habits", "James Clear")
book2 = Book("The Alchemist", "Paulo Coelho")

library1 = Library()

library1.add_books(book1)
library1.add_books(book1)

library1.remove_book("Atomic Habits")






