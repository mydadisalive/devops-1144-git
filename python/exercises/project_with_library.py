import library_module

library = library_module.Library("Sela1144 Library")
b1 = library_module.Book("Python 101", "John Doe", 3)
b2 = library_module.Book("Data Science Handbook", "Jane Smith", 5)
library.add_book(b1)
library.add_book(b2)
library.add_book(library_module.Book("The Hobbit", "", 8))
library.add_book(library_module.Book("lord of the rings", "J.K. Rowling", 100))
library.add_book(library_module.Book("public speech", "J.K. Rowling", 3))  

library.list_books()

library.find_by_title("The Hobbit")

