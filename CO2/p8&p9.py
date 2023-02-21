#p8
"""a=[]
n=int(input("Enter the number of elements in the list:"))
for x in range(0,n):
    ele=input("Enter word"+ str(x+1)+":")
    a.append(ele)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i) >max1):
        max1=len(i)
        temp=i
print("The word with longest length is:",temp)
print("Length of",temp,"is",len(temp))"""

#p9
n=int(input("Enter a limit : "))
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end="")
    print("\n")
for i in reversed(range(0,n)):
    for j in reversed(range(0,i)):
        print("*",end="")
    print("\n")