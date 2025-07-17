rows=6
num=1
for r in range(1,rows+1):
    num=r
    c=rows-1
    for j in range(r):
        print(num,end=" ")
        num+=c
        c-=1
    print("")