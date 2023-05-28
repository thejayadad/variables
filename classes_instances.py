

class Book:
    def __init__(self, title, arthor, price):
        self.title = title
        self.arthor = arthor
        self.price = price
        self.location = title[0:2] + "." + arthor[0:2]

    def premuim_book(self):
        if self.price > 15:
            return True
        else:
            return False


    def foundation(self):
        return '{}{}'.format(self.title, self.arthor)


    

book_one = Book('Bye Bye', 'Jace', 50)
book_two = Book('Hi Hie', 'Jada', 10)

# book_one.title = "Going Home"
# book_one.arthor = "Jace"
# book_one.price = 50

# book_two.title = "Bye Bye"
# book_two.arthor = "Jada"  
# book_two.price = 20

print(book_one)
print(book_two)

print(book_two.title)
print(book_two.location)
print(book_two.premuim_book())
print(book_one.foundation())