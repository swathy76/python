from graphics.rectangle import*
from graphics.circle import*
from graphics.ThreeDgraphics.Cuboid import*
from graphics.ThreeDgraphics.Sphere import*

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of rectangle =",RectArea(l,b))
print("Perimeter of rectangle =",RectPeri(l,b))
print()

r=int(input("Enter radius of Circle:"))
print("Area of circle =",CirArea(r))
print("Perimeter of circle =",CirPerimeter(r))
print()

r=int(input("Enter radius of Sphere:"))
print("Area of Sphere =",SpArea(r))
print("Perimeter of Sphere =",SpPeri(r))
print()

l1=int(input("Enter the length of cuboid:"))
b1=int(input("Enter the breadth of cuboid:"))
h=int(input("Enter the height of cuboid:"))
print("Area of Cuboid=",area(l1,b1,h))
print("Perimeter of Cuboid =",perimeter(l1,b1,h))
print()