from Book import Book

class Library:
    def __init__(self):
        self.books = []

    def addBook(self, newBook):
        for book in self.books:
            if book.isbn == newBook.isbn and book.title == newBook.title:
                print("This book already exists in the library.")
                return
            elif book.isbn == newBook.isbn and book.title != newBook.title:
                print("A book with the same ISBN already exists in the library.")
                return
            elif book.isbn != newBook.isbn and book.title == newBook.title:
                print("A book with the same title already exists in the library.")
                return

        self.books.append(newBook)
        print(f"Book '{newBook.title}' added successfully.")

    def borrowBook(self, bookName):
        for book in self.books:
            if book.title.lower() == bookName.lower():
                if not book.borrowed:
                    book.borrowed = True
                    print(f"You have successfully borrowed {book.title}.")
                    return
                else:
                    print(f"{book.title} is already borrowed.")
                    return
        print(f"No book found with the title '{bookName}'.")

    def returnBook(self, bookName):
        for book in self.books:
            if book.title.lower() == bookName.lower():
                if book.borrowed:
                    book.borrowed = False
                    print(f"You have successfully returned {book.title}.")
                    return
                else:
                    print(f"{book.title} is not currently borrowed.")
                    return
        print(f"No book found with the title '{bookName}'.")

    def displayAllBooks(self):
        if len(self.books) == 0:
            print("No books available in the library.")
            return

        print("Books in Library:")
        for book in self.books:
            if book.borrowed == False:
                print(f"{book.title}")
