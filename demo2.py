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


a=int(input("Enter the score in %:"))
if(a>=70):
    b=input("Enter your name:")
    c=input("Enter your location:")
    d=input("Enter your department:")
    print(b,"you are eligible")
else:
    print("you are not eligible:")

'''
sal=int(input("Enter your salary:"))
age=int(input("Age:"))
if(sal>=20000 or age<=25):
    loan=int(input("Enter loan amount?"))
    if(loan>50000):
        print("Maximum loan amount is 50000")
    else:
        print("You are eligible for loan")
        
else:
    print("You are not eligible for loan")        
