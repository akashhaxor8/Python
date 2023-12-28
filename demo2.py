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
