x=map(int,input("Enter the list of integers:").split(" "))
l1=[]
for i in x:
    if(i>100):
       l1.append('over')
    else:
        l1.append(i)
print("List of integers are:",l1)        