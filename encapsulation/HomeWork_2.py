class Book:
    author = None
    price = None
    title = None

    def __init__(self, a, p, t):
        self.author = a
        self.title = t
        # self.price = p
        self.change_price(p)

    def display(self):
        print(f"Author: {self.author}, Price: {self.price}, Title: {self.title}")

    def change_price(self, p):
        if(p>10):
            self.price = p

comic_book = Book("Raj", 110, "Zero to Hero")
comic_book.display()

java_book = Book("Arun Kumar",1100,"Java in 20 days")
java_book.display()

python_book = Book("Subodh",-1200,"AWS architecture")
# python_book.price = -1100
python_book.display()
python_book.change_price(-100)
python_book.display()

