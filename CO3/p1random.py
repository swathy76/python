import random
mylist=['Ann','Ben','Ciril','Deril','Eric','Fugi']
print(random.choice(mylist))
print(random.sample(mylist,k=1))
random.shuffle(mylist)
print(mylist)
print(random.randrange(3,9))
print(random.choices(mylist,k=4))

