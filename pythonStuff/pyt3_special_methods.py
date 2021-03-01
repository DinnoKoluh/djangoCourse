class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("Animal")
    
    def eats (self):
        print("eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self) # can be but it does not have to be
        print("Dog created")
    
    def eats(self):
        print("dog eating")


x = Dog()
x.who_am_i()
x.eats()


# special methods
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "[Title: {x}, Author: {y}, Pages: {z}]".format(x = self.title, y = self.author, z = str(self.pages)) 

    def __len__(self):
        return self.pages 

    def __del__(self):
        print("The book doesnt exist anymore")

b = Book("pytjhon", "Dinno", 200)
print(b)
print(len(b))
del(b) # to delete an instance of an object
