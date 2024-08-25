import random
z = 10000
l = [[0,123],[0,342],[0,1568]]

for w in range (0,5):
    for i in l:
        print(i)
    a = int(input("which stoke do you want to buy 0, 1, 2:- "))
    b = int(input("how many stoke do you want to buy:- "))
    l[a][0] = b
    print(l)
    c = b*(l[a][1])
    z=(z-c)
    print("balance after stoke buy",z)
    for j in l:
        j[1] = ((j[1]*random.randint(-5,5))//100)+j[1]
    z = (j[1]+z)
    print("balance after a day",z)
