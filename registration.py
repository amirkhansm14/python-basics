while True:
    print("1.User registration")
    print("2.Login")
    i=int(input("enter your choice :"))
    if i==1:
        a=input("Enter your name :")
        b=int(input("enter your age :"))
        if b<18:
            continue
        j=int(input("enter phone number :"))
        if len(str(j))!=10:
            continue
        c=input("Enter your address :")
        d=input("enter user name :")
        e=input("enter password :")
        
    elif i==2:
        f=input("enter user name : ")
        g=input("enter password :")
        if f==d and g==e:
            print(a)
            print(b)
            print(c)
        else:
            print("invalid user name/ pasword")