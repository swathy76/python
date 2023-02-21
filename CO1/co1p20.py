L1=[13,12,15,6,1,9,7,8]
print("The list of integers :",L1)
print("List of odd numbers :")
for i in L1:
    if i%2==0:
        L1.remove(i)
print(L1)      

"""#program 16
x=input("Enter the first string:")
y=input("Enter the second string:")
z=y[0]+x[1: ]+' '+x[0]+y[1: ]
print("Final string is:",z)


def chars_mix_up(a, b):
  new_a = b[:1] + a[1:]
  new_b = a[:1] + b[1:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))"""
