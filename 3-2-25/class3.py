# Problem:
# Design a Library Management System with the following features:
# A Book class that contains details like title, author, ISBN, and availability_status.
# A Member class that stores name, member_id, and a list of borrowed books.
# A Library class that manages books, allowing members to borrow and return books.
# Requirements:
# If a book is available, allow the member to borrow it.
# If the book is already borrowed, show a message that it’s unavailable.
# When a book is returned, update the availability status.

class Book():
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability
    


class Member():
    def __init__(self, name,  member_id , borrowed_book):
        self.name = name
        self member_id = member_id
        self borrowed_book = borrowed_book



class Library():
    def __init__(self,  manages_books, return_books):
        self.manages_books = manages_books
        self.return_books = return_books


book1 = Book("a","bala", True)
book2 = Book("b", "saravanan", False)
book3 = Book("c", "senthil" , True)



