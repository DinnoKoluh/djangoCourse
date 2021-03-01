# I can define funtions inside other functions

x = 20
def func():
    global x
    x = 40
    print("Inside func function and pyt2_classes.py file")

func()
print(x)

class Library():
    # create atributes, use a "special method" __
    # a method to initialize everything, self keyword means that this method referes 
    # to itself
    # class object attribute
    city = "Sanski Most"

    # nesto kao konstruktor
    def __init__(self, book, author = " "):
        self.book = book
        self.author = author
        self.city = "Dabar" # also possible Library.city = "something"

    def addNum(self, x, y):
        return x + y
    
    def getBook(self):
        print("The book name is: " + self.book)

x = Library(book = "White Fang",author =  "Dinno")
#print(type(x))
print(x.addNum(2,3))

print(x.book)
print(x.city)
x.city = "New York"
print(x.city)
x.getBook()


print("The name is" + __name__)