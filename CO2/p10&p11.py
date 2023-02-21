#p10
"""n=int(input("Enter the number : "))
print("Factors of {n} are:")
factors = [i for i in range(1,n+1) if n % i==0]
print(factors)"""



#p11
a=int(input("Enter side of square:"))
l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
h=int(input("Enter height of triangle:"))
square=lambda a:a*a
rectangle=lambda l,b:l*b
triangle=lambda b,h:0.5*b*h
print("area of square:",square(a))
print("area of rectangle:",rectangle(l,b))
print("area of triangle:",triangle(b,h))