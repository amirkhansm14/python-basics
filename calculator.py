while True:
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.Exit")
    i=int(input("enter your choice :"))
    if i==1:
        a=int(input("enter a number :"))
        b=int(input("enter a number :"))
        c=a+b
        print(c)
    elif i==2:
        a=int(input("enter a number :"))
        b=int(input("enter a number :"))
        c=a-b
        print(c)
    elif i==3:
        a=int(input("enter a number :"))
        b=int(input("enter a number :"))
        c=a*b
        print(c)
    elif i==4:
        a=int(input("enter a number :"))
        b=int(input("enter a number :"))
        if b>0:
          c=a/b
          print(c)
        else:
            print("must be greater tah zero")
    elif i==5:
        break   
    else:
        print("enter a valid choice")

