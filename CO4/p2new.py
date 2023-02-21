class Bank:
    def __init__(self):
         self.ac=int(input("Enter Your Account Number:"))
         self.name=input("Enter Your Name:")
         self.atype=input("Enter  Your Account Type:(s/c)")
         self.bal=0

    def deposit(self,bal):
        self.bal+=bal

    def  withdraw(self,bal):
        if(self.bal==0):
            print("Insufficient Balance!!")

        else:
            self.bal-=bal
    def display(self):
       print("Account Number:",self.ac)
       print("Name:",self.name)
       print("Account Type:",self.atype)
       print("Account Balance:",self.bal)
b1=Bank()
while(True):
    print()
    print("Enter your Choice:")
    print("1:Deposit")
    print("2:Withdraw")
    print("3:View Details")
    print("4:Exit")
    c=int(input())
    if(c==1):
        amount=int(input("Enter the Amount to Deposit:"))
        b1.deposit(amount)

    elif(c==2):
        amount1=int(input("Enter the Amount to Withdraw:"))
        b1.withdraw(amount1)

    elif(c==3):
        b1.display()

    else:
        break       