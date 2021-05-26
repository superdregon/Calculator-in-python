from time import sleep 

print ("Hello, welcome to my first python project, and this time, I'm here to show you my calculator.")
sleep(2)
firstnumber = input("put here your first number ")
firstnumber_int = int(firstnumber)

a = firstnumber_int
secondnumber = input("put here your second number ")
secondnumber_int = int(secondnumber)

b = secondnumber_int

resultype = str(input("what do you want to do? (write +, -, *, /) "))

if(resultype == "+"):
    print(a+b)
if(resultype == "-"):
    print(a-b)
if(resultype == "*"):
    print(a*b)
if(resultype == "/"):
    print(a/b)    


