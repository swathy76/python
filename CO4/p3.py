class Rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length of rectangle:"))
        self.__breadth=int(input("Enter the breadth of rectangle:"))
    def __lt__(self,ob2):
        area1=self.__length * self.__breadth
        area2=ob2.__length * ob2.__breadth
        print()
        print("Area of rectangle1 is ",area1)
        print("Area of rectangle2 is ",area2)
        return area1<area2
print("Enter the length and breadth of 1st object")
r1=Rectangle()
print()
print("Enter the length and breadth of 2nd object")
r2=Rectangle()
if r1<r2:
    print()
    print("Rectangle 1 is less than rectangle2")
else:
    print("Rectangle 1 is greater than rectangle2")