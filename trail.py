i=int(input("enter a number : "))
a=i
j=0
while(i>0):
    b=i%10
    j=j*10+b
    i=i//10
if(a==j):
    print("yes")
else:
    print("n")
