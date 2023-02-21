import function
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
n=int(input("Enter the option:\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Division\n"))
if n==1:
    s1=function.sum(a,b)
    print("Sum=",s1)
elif n==2:
    s2=function.sub(a,b)
    print("Difference=",s2)
elif n==3:
    s3=function.mul(a,b)
    print("Product=",s3)
elif n==4:
    s4=function.div(a,b)
    print("Quotient=",s4)
else:
    print("Invalid option")



