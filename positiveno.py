# # # # # # #positive
# # # # # # # i=int(input("enter a number"))
# # # # # # # if(i>=1):
# # # # # # #     print("the number is positive")
 
# # # # # # #dividible by 5
# # # # # # #i=int(input("enter a number"))
# # # # # # # if(i%5==0):
# # # # # # #     print("number is divisible by 5")

# vowels
# i=str(input("enter a letter : "))
# if(i=="a","e","i","o","u","A","E","I","O","U"):
#     print("its a vowel")

# # # # # # #python
# # # # # # # i=str(input("enter a word : "))
# # # # # # # if(i=="python"):
# # # # # # #      print("the enterd word is python")

# # # # # #                                      #if else
# # # # # # #odd or even
# # # # # # # i=int(input("enter a number : "))
# # # # # # # if(i%2==0):
# # # # # # #     print(f"{i} is even")
# # # # # # # else:
# # # # # # #     print(f"{i} is odd ")    

# # # # # # #vote
# # # # # # # i=int(input("enter the age : "))
# # # # # # # if(i>=18):
# # # # # # #     print("you can vote")
# # # # # # # else:
# # # # # # #     print("you cant vote")    

# # # # # # #greater
# # # # # # # i=int(input("enter the number : "))
# # # # # # # j=int(input("enter the number : "))
# # # # # # # if(i==j):
# # # # # # #     print("both are same values")
# # # # # # # elif(i>j):
# # # # # # #     print(f"{i} is greater than {j}")
# # # # # # # else:
# # # # # # #     print(f"{i} is less than {j}")

# # # # # # #leapyear
# # # # # # # i=int(input("enter a year : "))
# # # # # # # if(i%4==0):
# # # # # # #     print(f"{i} is a leap year")
# # # # # # # else:
# # # # # # #      print(f"{i} is not a leap year")

# # # # # # #
# # # # # # # i=int(input("enter the number of units"))
# # # # # # # if(i>0 and i<=100):
# # # # # # #     a=i*5
# # # # # # #     print(a)
# # # # # # # elif( )


# # # # # #                                                #LOOP SATEMENTS 
# # # # # # # i=int(input("enter a number : "))
# # # # # # # while i<=10:
# # # # # # #     if(i%2==0):
# # # # # # #         print(i)
# # # # # # #     i+=1



# # # # # # # i=int(input("enter a number"))
# # # # # # # while i>=0:
# # # # # # #     if(i%2==0):
# # # # # # #        print(i)
# # # # # # #     i-=1 

# # # # # # #calculator
# # # # # # # a=0
# # # # # # # i=int(input("enter a number"))
# # # # # # # while i!=-1:
# # # # # # #     a=a+i
# # # # # # #     i=int(input("enter a number"))
# # # # # # # print(a)    



# # # # # #                          #19/06/2025

# # # # # #        #sum of digits
# # # # # # # i=int(input("enter a number"))
# # # # # # # j=0
# # # # # # # while(i>0):
# # # # # # #     a=i%10
# # # # # # #     j=j+a
# # # # # # #     i=i/10
# # # # # # # print(j)

# # # # # #              #palindrome
# # # # # # # i=int(input("enter a number"))
# # # # # # # j=0
# # # # # # # b=i
# # # # # # # while(b>0):
# # # # # # #     a=(b%10) 
# # # # # # #     j=(j*10)+a
# # # # # # #     b=b//10
# # # # # # # if(j==i):
# # # # # # #     print("its  a palindrome")
# # # # # # # else:
# # # # # # #     print("its not palindrome")

# # # # # #           #count number
# # # # # # # i=int(input("enter a number"))
# # # # # # # j=0
# # # # # # # while i>0:
# # # # # # #     j=j+1
# # # # # # #     i=i//10
# # # # # # # print(j)
# # # # # # #or
# # # # # # # b=len(str(i))
# # # # # # # print(b)
# # # # # #             #count occurance
# # # # # # # i=int(input("enter a number : "))
# # # # # # # j=int(input("enter the number to check : "))
# # # # # # # a=0
# # # # # # # while i>0:
# # # # # # #     if(i%10==j):
# # # # # # #        a=a+1
# # # # # # #     i=i//10
# # # # # # # print(a)
 
# # # # # #      #amstrong number
# # # # # # # i=int(input("enter a number"))
# # # # # # # a=i
# # # # # # # j=0
# # # # # # # b=len(str(i))
# # # # # # # while i!=0:
# # # # # # #     r=i%10
# # # # # # #     j=j+(r**b)
# # # # # # #     i=i//10

# # # # # # # if(a==j):
# # # # # # #     print("its a amstrong number")
# # # # # # # else:
# # # # # # #     print("its not an amstrong number")





# # # # # # #for loop
# # # # # # # i=("python","loops","sequence","condition","range")
# # # # # # # for iterator in range(len(i)):
# # # # # # #     print(i[iterator].upper(),end=" , ")

# # # # # # # numbers=[4,2,6,7,3,5,8,10,6,1,9,2]
# # # # # # # square=0
# # # # # # # squares=[]
# # # # # # # for value in numbers:
# # # # # # #     square=value**2
# # # # # # #     squares.append(square)
# # # # # # # print("the list of squares is",squares)

# # # # # # # string="Python Loop"
# # # # # # # for s in string:
# # # # # # #     if s=="o":
# # # # # # #         print("if block")
# # # # # # # else:
# # # # # # #     print(s)

# # # # # # #reverse using for loop
# # # # # # # i=int(input("enter a numnber"))
# # # # # # # r=len(str(i))
# # # # # # # b=0
# # # # # # # for j in range(r):
# # # # # # #       a=(i%10) 
# # # # # # #       b=(b*10)+a
# # # # # # #       i=i//10
# # # # # # # print(b)
# # # # # #          #even
# # # # # # # i=int(input("enter a numnber : "))
# # # # # # # for j in range(i+1):
# # # # # # #     if(j%2==0):
# # # # # # #       print(j)

# # # # # # #multiplication
# # # # # # # i=int(input("enter a number"))
# # # # # # # b=int(input("enter the limit"))
# # # # # # # for j in range(1,10+1):
# # # # # # #     if(i>0):
# # # # # # #         a=j*i
# # # # # # #         print(i,"*",j,"=",a)
       
# # # # # # # i="python"
# # # # # # # # b=""
# # # # # # # # for j in i: 
# # # # # # # #     b=j+b
# # # # # # # # print(b)

# # # # # # # a=i[::-1]
# # # # # # # print(a)

# # # # # # # n=5
# # # # # # # for i  in range(0,n):
# # # # # # #     for j in range(0,n):
# # # # # # #         print("* ",end=" ")
# # # # # # #     print()    

# # # # # # # n=5
# # # # # # # a=1
# # # # # # # for i  in range(0,n):
# # # # # # #     for j in range(0,n):
# # # # # # #         print(a,end=" ")
# # # # # # #         a=a+1
# # # # # # #     print()    
       
# # # # # #      #inverted right half pyramid
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,n-i):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()

# # # # # #        #left  half pyramid
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,n-i):
# # # # # # #         print(" ",end=" ")

# # # # # # #     for k in range(0,i+1):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()

# # # # # #       #fully pyramid
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,n-i):
# # # # # # #         print("",end=" ")

# # # # # # #     for k in range(0,i+1):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()

# # # # # #         #right half pyramid
# # # # # # # n=5
# # # # # # # for i in range(0,n+1):
# # # # # # #     for j in range(0,i):
# # # # # # #         print("* ",end=" ")
# # # # # # #     print()

# # # # # #         #inverted left half
# # # # # # # n=5
# # # # # # # for i in range(0,n+1):
# # # # # # #     for j in range(0,i):
# # # # # # #         print("  ",end=" ")
# # # # # # #     for k in range(0,n-i):
# # # # # # #         print("* ",end=" ")
# # # # # # #     print()
# # # # # #              #inverted pyramid
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,i):
# # # # # # #         print("",end=" ")
# # # # # # #     for k in range(0,n-i):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()

# # # # # #          #rombus
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,i):
# # # # # # #         print(" ",end=" ")
# # # # # # #     for k in range(0,n):
# # # # # # #         print("* ",end=" ")
# # # # # # #     print()

# # # # # #         #daimond
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,n-i):
# # # # # # #         print("",end=" ")

# # # # # # #     for k in range(0,i+1):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()
# # # # # # # n=n-1
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,i+2):
# # # # # # #         print("",end=" ")
# # # # # # #     for k in range(0,n-i):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()

# # # # # #        #hourglass pattern
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,i+1):
# # # # # # #         print("",end=" ")
# # # # # # #     for k in range(0,n-i):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()
# # # # # # # n=n-1
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,n-i):
# # # # # # #         print("",end=" ")

# # # # # # #     for k in range(0,i+2):
# # # # # # #         print("*",end=" ")
# # # # # # #     print()

# # # # # #          #hollow square
# # # # # # # n=5
# # # # # # # for i in range(0,n+1):
# # # # # # #     for j in range(0,n+1):
# # # # # # #         if (i==0 or i==n or j==0 or j==n):
# # # # # # #           print("* ",end=" ")
# # # # # # #         else:
# # # # # # #            print("  ",end=" ")  
# # # # # # #     print()
     
# # # # # #             #hollow pyramid
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #      for k in range(0,n-i): 
# # # # # # #         print(" ",end="")
# # # # # # #      for j in range(0,i+1):
# # # # # # #         if j==0  or i==n-1:
# # # # # # #                 print("* ",end="")
# # # # # # #      for l in range(0,i):
# # # # # # #         if l==i-1 and i!=n-1:
# # # # # # #           print("*",end=" ")
# # # # # # #         else:
# # # # # # #             print(" ",end=" ")  
# # # # # # #      print() 

# # # # # #  #inverted hollow full pyramid

# # # # # # # n=5
# # # # # # # for i in range(0,n+1):
# # # # # # #      for k in range(0,i): 
# # # # # # #         print("",end=" ")
# # # # # # #      for j in range(0,i):
# # # # # # #         if j==0:
# # # # # # #                 print("* ",end="")
# # # # # # #      for l in range(1,n+2):
# # # # # # #         if l==n-i or i==0:
# # # # # # #           print("*",end=" ")
# # # # # # #         else:
# # # # # # #             print(" ",end=" ")  
# # # # # # #      print()

# # # # # #        #hollow diamond
# # # # # # # n=5
# # # # # # # for i in range(0,n-1):
# # # # # # #      for k in range(0,n-i): 
# # # # # # #         print(" ",end="")
# # # # # # #      for j in range(0,i+1):
# # # # # # #         if j==0:
# # # # # # #                 print("* ",end="")
# # # # # # #      for l in range(0,i):
# # # # # # #         if l==i-1:
# # # # # # #           print("*",end=" ")
# # # # # # #         else:
# # # # # # #             print(" ",end=" ")  
# # # # # # #      print() 
# # # # # # # for i in range(1,n+1):
# # # # # # #      for k in range(0,i): 
# # # # # # #         print("",end=" ")
# # # # # # #      for j in range(0,i):
# # # # # # #         if j==0:
# # # # # # #                 print("* ",end="")
# # # # # # #      for l in range(1,n+2):
# # # # # # #         if l==n-i and l!=5:
# # # # # # #           print("*",end=" ")
# # # # # # #         else:
# # # # # # #             print(" ",end=" ")  
# # # # # # #      print()

# # # # # #         #print first letter "A"
# # # # # # # n=5
# # # # # # # for i in range(0,n):
# # # # # # #      for k in range(0,n-i): 
# # # # # # #         print(" ",end="")
# # # # # # #      for j in range(0,i+1):
# # # # # # #         if j==0  or i==3:
# # # # # # #                 print("* ",end="")
# # # # # # #      for l in range(0,i):
# # # # # # #         if l==i-1 and i!=n and i!=3:
# # # # # # #           print("*",end=" ")
# # # # # # #         else:
# # # # # # #             print(" ",end=" ")  
# # # # # # #      print() 




# # # # # # # a="hello world"
# # # # # # # # print(a[::-1])
# # # # # # # # a[1]="y"
# # # # # # # print(len(a))

# # # # #     # count letters in a string or number in intier
# # # # # # # a="PYTHHON"
# # # # # # # # print(a.lower())
# # # # # # # b=a.count("H")
# # # # # # # print(b)
# # # # #             #find the starting index of a word or a letter in a string
# # # # # # # a="python is a fun programing language"
# # # # # # # print(a.find("fun"))
# # # # #             #replace a string
# # # # # # a="bat boll"
# # # # # # b=a.replace("ba","ro")
# # # # # # print(b)


# # # # #           #append ie add a value  to the list at last index
# # # # # # a=[1,2,3,4]
# # # # # # a.append(5)
# # # # # # print(a)

# # # # #             #insert into a list 
# # # # # # a=[1,2,3,4,5]
# # # # # # a.insert(2,2)
# # # # # # print(a)
# # # # # # a=["a","e","i","u"]
# # # # # # a.insert(3,"o")
# # # # # # print(a)


# # # # #              #extend a list by adding two list
# # # # # # a=[1,2,3,4,5]
# # # # # # b=[6,7,8,9]
# # # # # # a.extend(b)
# # # # # # print(a)



# # # # # # a=[]
# # # # # # b=int(input("enter the number : "))
# # # # # # for i in range(0,b):
# # # # # #     c=int(input("enter a number to list : "))
# # # # # #     a.append(c)
# # # # # # print(a)

# # # # #        #add only even numbers to the list
# # # # # # a=int(input("enter the limit value : "))
# # # # # # b=[]
# # # # # # for i in range(0,a):
# # # # # #     if i%2==0:
# # # # # #         b.append(i)
# # # # # # print(b)        


# # # # # # prime_number=[2,3,5,7]
# # # # # # remove_element=prime_number.pop(2)
# # # # # # print(remove_element)
# # # # # # print(prime_number)

# # # # # # a=[1,2,3,4,5,6,7,8,9,10]
# # # # # # for i in range(len(a)):
# # # # # #     if i<=len(a)-1:
# # # # # #        if a[i]%2==0:
# # # # # #          a.pop(i)
# # # # # # print(a)
# # # # # c=[]
# # # # # while True:
# # # # #     print("1.Add")
# # # # #     print("2.Remove")
# # # # #     a=int(input("enter you choice : "))
# # # # #     if a==1:
# # # # #         b=int(input("enter the value in list : "))
# # # # #         c.append(b)
# # # # #         print(c)
# # # # #     elif a==2:
# # # # #         d=int(input("enter the to be removed : "))
# # # # #         for i in range(len(c)):
# # # # #           if c[i]==d:
# # # # #              c.pop(i)
# # # # #              print(c)
# # # # #              break

# # # # # a=["a","b","c","d"]
# # # # # del a[1]
# # # # # print(a)

# a=["a","b","c","d"]
# del a[-1]
# print(a)

# # # # # a=["a","b","c","d"]
# # # # # del a[0:2]
# # # # # print(a)

# # # # # a=["a","b","c","d"]
# # # # # a.remove("b")
# # # # # print(a)


# # # # a=["a","b","c","d"]
# # # # a.reverse()
# # # # print(a)


# # # # a=[1,2,3,4]
# # # # b=a*2
# # # # print(b)


# # # c=[1,2,3,4,5,]

# # # a=[1,2,3,4]
# # # b=a+c
# # # print(b)

# # a=[1,2,3,4]
# # # print(5 in a)

# # # a=["a","k","aks"]
# # print(max(a))

# a=[1,2,3,4,5]
# b=[2,3,5,6,7]
#  c=set(a).intersection(b)
# c=set(a)&set(b)
# print(c)

# a=[1,2,3,4,5]
# b=[2,3,5,6,7]
# c=[]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             c.append(b[j])
# print(c)

# a=[1,2,3,4,5]
# b=[2,3,5,6,7]
# c=[]
# for i in range(len(a)):
#     if a[i] in b:
#         c.append(a[i])
# print(c)
              #max
# a=[2,3,1,4,5]
# b=a[0]
# for i in a:
#     if i>b:
#      b=i   
# print(b)
             #min
# a=[2,3,1,4,5]
# b=a[0]
# for i in a:
#     if i<b:
#         b=i
# print(b)        



# a=[1,2,3,4,5]
# b=[i**2 for i in a]
# print(b)


# m=[[j for j in range(3)]for i in range(3)]
# print(m)


# a=(0,"m",[1,2],(1,2))
# print(a)
# a=()
# print(a)

# a=[1,2,2,4]
# print(a.index(2))


# s=set()
# print(type(s))

# s={1,6,4,'abc'}
# print(type(s))

# a=set(["monday","tuesday","wednessday","thursday"])
# print(a)
# print(type(a))
# for i in a:
    # print(i)


# a.add("friday")
# print(a)

# a.update(["friday","saturday"])
# print(a)

# a.discard("monday")
# print(a)

# a.remove("monday")
# print(a)

# a={1,2,3,4,6}
# b={1,3,6}
# c={1,5,6,8}
# print(a>b)
# print(a<b)
# print(b==c)
# print(a|b)
# print(a&b)

# a=[1,2,2,4,6]
# b=set(a)
# print(b)



# b=set()
# for i in range(5):
#     a=int(input("enter the number : "))
#     b.add(a)
# print(b)



# a="Python Programming is fun!"
# b=set()
# for i in range(len(a)):
#     if a[i] in ("a","A","e","E","i","I","o","O","u","U"):
#         b.add(a[i])
# print(b)

# a={"kak","abs","hk"}
# b=set()
# for i in a:
#     c=set(i)
#     if (len(i))==(len(c)):      
#         b.add(i)
# print(b)


# a=int(input("enter a number :"))
# b=1
# for i in range(1,a+1):
#      b=b*i
# print(b)
# while a>0:
#     b=b*a
#     a=a-1
# print(b)
# n=6
# a=0
# for i in range(0,n):
#     for j in range(0,i):
#         a=a+1
#         b=i*(n-1)
#         print(a,end=" ")
#     print()
# n=5
# b=n
# for i in range(0,n):
#     for j in range(0,i):
#         print(" *",end="")
#     print()

# a=int(input("enter a number : "))
# b=int(a/2)
# if a==2:
#              print("prime")
#              pass
# for c in range(2,b+1): 
#         if a%1==0 and a%c==0 and a%a==0:
#             print(" not prime")
#             break
#         else:
#             print("prime")
#             break


#dictionary
# c={"Nepal":"Kathmandu","Italy":"Rome"}
# print(c)
# c["Japan"]="Tokyo"  #update or  add
# print(c)
# # print(c["Japan"])
# for i in c:
#     print(c[i])


# s={111:"Eric",112:"Kyle",113:"Butters"}
# s[112]="Stan"
# print(s)

# print(s[111]) 
# print(s[113])
# del s[111]
# print(s)

# a={}
# for i in range(1,11):
#     b=i**2
#     a[i]=b
# print(a)

        #with argument with return type
# def square(num):
#     return num**2
# object_=square(6)
# print(object_)

        #with argument without return type
# def square(num):
#     print(num**2)
# square(6)
      
# def a(string):
#     return len(string)
# print(a("function"))
# print(a("python"))

        #without argument with return type
# def message():
#     return "Welcome" 
# msg=message()
# print(msg)

  #without argument without return type
# def print_numbers():
#     for i in range(1,6):
#         print(i)
# print_numbers() 

# def function(n1,n2=20):
#     print(n1)
#     print(n2)
# function(30)

# def function(n1,n2):
#     print(n1)
#     print(n2)
# function(n1=30,n2=20)

# import copy
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=copy.copy(a)
# b[1][0]=2
# print(b)
# print(a)
# b=copy.deepcopy(a)
# b[1][0]=2
# print(b)
# print(a)
# a={1,2,3,4}
# b=copy.copy(a)
# b.update([6,7])
# print(b)
# print(a)
# def even(n):
#     if n%2==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# a=int(input("enter a number : "))
# even(a)    

# def fact(n):
#     b=1
#     for i in range(1,n+1):
#         b=b*i
#     print(b)    
# a=int(input("enter a number : "))
# fact(a)     

# def prime(n):
#     s=True
#     b=int(n/2)
#     if n==2:
#         s=True
#         pass
#     for i in range(2,b+1):
#         if n%1==0 and n%i==0 and n%n==0:
#             s=False
#             break  
#     if s==True:
#         print(n,"is prime")
#     elif s==False:
#         print(n,"is not prime")
# a=int(input("enter a number : "))
# prime(a)


# def a(**b):
#     print(f"hai {b['name']} your age is {b['age']} and from {b['adres']}")
# a(name="ak",age=16,adres="akvilla")

# n=10
# a=0
# b=1
# c=0
# print(a,b,end=" ")
# while n>0:
#     c=a+b
#     a=b
#     b=c
#     n-=1  
#     print(c,end=" ")

# for i in range(6):
#     a=65
#     for k in range(i):
#         print(chr(a),end=" ")
#         a=a+1
#     print()    


# a=10
# def ak(n):
#     global a
#     a+=n
#     print(a)
# ak(5)

# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(5))
# a="oneteam" 
# for i in range(len(a)):
#     b=0
#     for j in range(len(a)):
#         if a[i]==a[j]:
#             b=b+1
#     print(a[i],"=",b)
a="oneteam" 
c=set(a)
for i in c:
    b=0
    for j in range(len(a)):
        if i==a[j]:
            b=b+1
    print(i,"=",b)