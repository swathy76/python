fn=open("newfile.txt",'w')
fn.write("1:Python is an amazing programming language.\n2:It is very easy to learn.\n3:Open source.")

fn.close()
fn1=open("newfile.txt",'r')
fn1.seek(0,0)

f=fn1.readlines()
for x in range(0,len(f)):
    print(f[x])
print(f)
fn1.close()  