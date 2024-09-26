# Book Class which will have details of a individual Book
# I have used camel-casing for writing the variables name 


class Book:
    def __init__(self,isbn,title,author, publicationYear):
        self.isbn = int(isbn)
        self.title = str(title)
        self.author = str(author)
        self.publicationYear = int(publicationYear)
        self.borrowed = False
        

