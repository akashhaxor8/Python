'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=input("add/sub/mul/div choose an arithmetic operation")
if(c=="add"):
    print(a+b)
elif(c=="sub"):
    print(a-b)
elif(c=="mul"):
    print(a*b)
elif(c=="div"):
    print(a/b)
else:
    print("Invalid Input")

'''

a=int(input("Enter the score in %:"))
if(a>=70):
    b=input("Enter your name:")
    c=input("Enter your location:")
    d=input("Enter your department:")
    print(b,"you are eligible")
else:
    print("you are not eligible:")