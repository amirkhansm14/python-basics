i=int(input("enter a number"))
if(i>101 or i<0):
    print("invalid input")
elif(i>=90):
    print("grade A")
elif(i>=80):
    print("grade B")
elif(i>=70):
    print("grade C")
elif(i>=60):
    print("grade D")
else:
    print("failed")
