"""word=input("Enter a word:")
l=[ord(i) for i in word]
print("Ordinal values:",l)

a=int(input("Enter side of square:"))
l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))
h=int(input("Enter height of triangle:"))
sq=lambda a:a*a
rect=lambda l,b:l*b
tri=lambda b,h:0.5*b*h
print("ar(sq)=",sq(a))
print("ar(rect)=",rect(l,b))
print("ar(tri)=",tri(b,h))"""

st=input("Enter a string:")
for i in range(0,len(st)):
    if st[-3]=='i' and st[-2]=='n' and st[-1]=='g':
        print(st+"ly")
        break
    else:
        print(st+"ing")
        break
    
        