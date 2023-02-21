class Rectangle:
    def __init__(self,l1,b1):
        self.l1=l1
        self.b1=b1
        
    def peri(self):
        return 2 * (self.l1 + self.b1)
          
    def area(self):
        return self.l1 * self.b1
    def compare(self,r2):
      
        if r.area() > r2.area():
            print("Area of R1 is greater than R2")
        else:
            print("Area of R1 is less than R2")    
      

l1=int(input("Enter length of R1:"))
b1=int(input("Enter breadth of R1:"))
r=Rectangle(l1,b1)
print("Perimeter of R1: %s cm" %(r.peri()))  
print("Area of R1: %s cm^2" %(r.area()))
print()
l2=int(input("Enter length of R2:"))
b2=int(input("Enter breadth of R2:"))
r2=Rectangle(l2,b2)
print("Area of R2=",r2.area())
print("Perimeter of R2=",r2.peri())
print()
r.compare(r2)