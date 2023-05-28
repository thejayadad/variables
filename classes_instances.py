#Object-oriented programming (OOP) is a method of structuring a program by
# bundling related properties and behaviors into individual objects
class Book:
    def __init__(self, title, arthor, price):
        self.title = title
        self.arthor = arthor
        self.price = price

        self.location = title[0:2] + "." + arthor[0:2]

    def premium_book(self):
        if self.price > 16:
            return True
        else:
            return False


      

book_one = Book("Im going home", "Jace", 50)
book_two = Book("Hi mom", "Jada", 15)
print(book_one.title)
print(book_two.title)
print(book_one.premium_book())
print(book_two.premium_book())
# print(book_one)
# print(book_two)

# book_one.title = "Im going home"
# book_one.arthor = "Jace"
# book_one.price = 50

# print(book_one.title)

# book_two.title = "hi mom"
# book_two.arthor = "Jada"
# book_two.price = 15

# print(book_two.title)