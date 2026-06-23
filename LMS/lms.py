# Description: A simple library system where users (students) can borrow and return books. Modules:

# Register/Login
# View Available Books
# Borrow Book
# Return Book
# Forgot Password

# Book - title, std_name : set_name, get_name, constructor
# Student - name, roll, books - [] : setter and getter, constructor
# Library - books, member{}: issueBooks(std, book), returnBook

class Book:
    def __init__(self, title):
        self.__title = title
        self.__student = None

    def get_title(self):
        return self.__title
    
    def isAvailable(self):
        return self.__student==None
    
    def get_student(self):
        return self.__student
    def set_student(self, name):
        # verify
        self.__student = name

    def __str__(self):
        isAvailable = False
        if(self.__student==None):
            isAvailable = True
        return f"Title: {self.__title}, Student: {self.__student}, Available: {isAvailable}"
    
# b = Book("Nature in Future")
# print(b)
    

# Student - name, roll
class Student:
    def __init__(self, name, roll):
        self.__name = name
        self.__roll = roll
        # string list
        self.__books = []
    
    def get_name(self):
        return self.__name
    def get_roll(self):
        return self.__roll
    
    def issued_books(self):
        return self.__books
    
    def issue_book(self, book):
        self.__books.append(book)
    def return_book(self, book):
        self.__books.remove(book)


    def __str__(self):
        return f"Name: {self.__name}, Roll: {self.__roll}, Books: {self.__books}"
    

# Library - books, member{}: issueBooks(std, book), returnBook
class Library:
    books = [
        Book("Nature in Future"),
        Book("Water Life"),
        Book("Right Fight")
    ]

    students = {
        # 1: {"std": Student("ramesh", 1), "books": []},

        1: Student("ramesh", 1),
        2: Student("ramesh", 2),
        3: Student("ramesh", 3)
    }

    # issueBooks(456, 987)
    def issueBook(self, std_roll, book_index):
        # verify if std_roll and book_index are present
        current_student = self.students[std_roll]
        book_to_issue = self.books[book_index]
        current_student.issue_book(book_to_issue.get_title())

        # self.students[std_roll]["books"].append(book_to_issue)
    
    def returnBook(self, std_roll, book_index):
        # verify if std_roll and book_index are present
        current_student = self.students[std_roll]
        book_to_return = self.books[book_index]
        current_student.return_book(book_to_return.get_title())
    