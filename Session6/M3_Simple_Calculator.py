x=int(input("Enter the First Number "))
y=int(input("Enter the Second Number "))

op=input("Press 1 for Addition, Press 2 for Subtraction, Press 3 for Multiplication, Press 4 for Dividation ")

if op=='1':
    print("Addition=",x+y)
elif op=='2':
    print("Subtraction=",x-y)
elif op=='3':
    print("Multiplication=",x*y)
elif op=='4':
    print(x/y)
else:
    print("Invalid Operation")