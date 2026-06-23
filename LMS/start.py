from lms import Library, Student, Book


library = Library()
library.issueBook(1, 0)
library.issueBook(1, 2)
library.issueBook(1, 5)

print(library.students[1])