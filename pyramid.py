n=5
for i in range(0,n):
    for k in range(0,n-i):
        print("",end=" ")
    for j in range(1):
        if(i==n-1):
            print("*  "*4,end="")
        elif i==0:
            print("* ")
        else:
            print("*","  "*(i-1),"*")
        