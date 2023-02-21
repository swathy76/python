"""n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial is:",fact)"""

#program 2
def fibanocci(n):
        if n <= 1:
            return n  
        else:  
            return(fibanocci(n-1) + fibanocci(n-2))  
num =int(input("Enter the term:"))  
if num <= 0:  
    print("Please enter a positive integer")  
else:  
   print("Fibanocci sequence:")  
for i in range(num):  
   print(fibanocci(i))

"""num =6
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()"""