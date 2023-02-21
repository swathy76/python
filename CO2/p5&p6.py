#p5
"""n=int(input("Enter a limit:"))
for i in range(1,n+1):
    for j in range(0,i+1):
        a=i*j
        if a==0:
            continue
        else:
            print(a,end=" ")
    print("\n")"""
    
#p6    
st=input("Enter a word:")        
c=0
for i in st:
    if i==" ":
        continue
    else:
        c+=1
print(c,"characters in " +st) 