f=open("secfile.txt",'r')
f1=open("new2.txt",'w')
lines=f.readlines()
for i in range(0,len(lines)):
    if i%2==0:
        l=f1.write(lines[i])

f.close()
f1=open("new2.txt","r")
cont=f1.read()
print(cont)
f1.close()