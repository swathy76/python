"""a=input('Enter the names:')
L1=a.split()
for i in L1:
    occur=a.count('a')
print("Occurence of 'a' in names is",occur)    """


names=['anagha','swathy','arya','anand']
print("The list of first names is:",names)
count=0
for i in names:
    count=count+ i.count('a')
print("Occurences of 'a' in the list is:",count)    