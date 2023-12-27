"""
if(True):
    print("Yes")
else:
    print("No")

print("win"=="win") #comparison operator

rcb="win"
if(rcb=="win"):
    print("We won the cup")
else:
    print("Sorry RCB loses")

Meghna=input("Meghna Died or Not?")
if(Meghna=="Died"):
    print("Surya meets priya")
else:
    print("Surya weds Meghna")

Mark=int(input("Provide the Mark?"))
if(Mark>35):
    print("He got Pass")
else:
    print("He has failed")


income=int(input("Please provide your yearly income?"))
if(income<7000):
    print("Scholarship is available")
else:
    print("Not eligible for Scholarship")


a=int(input("Enter a number:"))
if(a%3==0 and a%5==0):
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")

a=int(input("Enter a number:"))
if(a%2==0):
    print("It is even number")
else:
    print("It is odd number")

"""
a=int(input("enter the mark:"))
if(a<35):
    print("poor student")
elif(a>35 and a<70):
    print("Average student")
elif(a>70 and a<100):
    print("Good student")
else:
    print("Invalid input")
