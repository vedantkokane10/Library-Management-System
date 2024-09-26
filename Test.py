import unittest 
from Library import Library
from Book import Book

class Test(unittest.TestCase):
    def test_addBook(self):
        LibraryObject = Library()
        BookObject = Book(12345,'Database Management Systems','Raghu Ramakrishnan',1996)
        LibraryObject.addBook(BookObject)
        self.assertEqual(len(LibraryObject.books),1)
        self.assertIn(BookObject,LibraryObject.books)

    def test_borrowBook(self):
        LibraryObject = Library()
        BookObject = Book(12345,'Database Management Systems','Raghu Ramakrishnan',1996)
        LibraryObject.addBook(BookObject)
        LibraryObject.borrowBook("Database Management Systems")
        self.assertTrue(LibraryObject.books[0].borrowed)

    def test_returnBook(self):
        LibraryObject = Library()
        BookObject = Book(12345,'Database Management Systems','Raghu Ramakrishnan',1996)
        LibraryObject.addBook(BookObject)
        LibraryObject.borrowBook("Database Management Systems")
        LibraryObject.returnBook("Database Management Systems")
        self.assertFalse(LibraryObject.books[0].borrowed)



if __name__ == '__main__':
    unittest.main()