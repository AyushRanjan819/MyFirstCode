a = 0
pas = input("set your password:- ")
while True:
    d = input("enter your password :-")
    if d == pas:
        x=int(input("if do you want to deposit write (0) or withdraw write (1):- "))
        if x == 0:
            b = int(input("write amount you want to deposit:- "))
            a = a + b
            print("your new amount balance is :-", a)
        elif x == 1:
            b = int(input("write amount you want to withdraw:- "))
            if b > a:
                print("withdraw amount is bigger than balence")
            else:
                a = a - b
                print("your new amount balance is :-", a)
        else:
            print("incorect choice")
    else:
        print("password is incorect")
    z = input("type 'exit' if want to end:- (Y/N) ::::::->")
    if z == "Y":
        break
