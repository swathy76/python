#program 3
"""L1=[1,2,3,5,7,9,10]
print("List is:",L1)
print("Sum of list:",sum(L1))"""

#p4
from math import sqrt
num=int(input("Enter a 4 digit number as limit: "))
for i in range(1000,num):
    if sqrt(i)==int(sqrt(i)) and i%2 ==0:
        print(i)