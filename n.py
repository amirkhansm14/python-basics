n=5
for i in range(0,n):
    for k in range(0,n):
        if k==0 or k==i or k==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()