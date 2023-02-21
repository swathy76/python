class Publisher():
    def __init__(self,n):
         self.name=n
    def display(self):
        print("Name of Publisher:",self.name)
class Book(Publisher):
    def __init__(self,n,t,a):
        super().__init__(n)
        self.title=t
        self.author=a
    def display(self):
        print("Title of the book is:",self.title)
        print("Author of the book is:",self.author)
class Python(Book):
    def __init__(self,n,t,a,p,pgno):
        super().__init__(n,t,a)
        self.price=p
        self.pgno=pgno
    def display(self):
        Publisher.display(self)
        Book.display(self)
        print("Price of book :",p1.price)
        print("No. of pages of book :",p1.pgno)
p1=Python("Python","Introduction to Python","Jeeva Jose",450,300)
p1.display()
        