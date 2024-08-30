class library():
    def __init__(self,books,a):
        self.books=books
        self.a=a
        print(books)
        if a in books:
            return ("This is your" ,a, "book")
        else:
            books.append(a)
    def no_of_books(self):
        if len(self.books)==len(self.books):
            print(len(self.books))
        else:
            print("Their was a problem")
        return
obj=library(["maths","hindi","english","sceince","chemestry"], input("Enter the books :"))

print(obj.no_of_books())