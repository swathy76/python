st=input("Enter a string:")
for i in range(0,len(st)):
    if st[-3]=='i' and st[-2]=='n' and st[-1]=='g':
        print(st+"ly")
        break
    else:
        print(st+"ing")
        break
    """


string=input("Enter a string:")
if string.endswith('ing'):
    string += 'ly'
elif len(string) >=3:
    string += 'ing'
print(string) """   
    