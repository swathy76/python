a=int(input("Enter the current year:"))
b=int(input("Enter the final year:"))
print("The leap years are:")
while(a<=b):
    if(a%4==0 and a%100!=0)or (a%400==0 and a%100==0):    
        print(a)
        
    a=a+1  
    