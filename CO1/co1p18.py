"""dict1={"ben":23,"celin":24,"rocky":26,"alan":29}
dict2={"charlie":24,"david":25,"levin":27}
print("First dictionary:",dict1)
print("Second dictionary:",dict2)
print("Merged dictionary:",{**dict1,**dict2})"""


#program 14
n=int(input("Enter a number n:"))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)