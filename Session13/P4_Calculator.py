x=int(input("Enter the first no. "))
y=int(input("Enter the second no. "))


while True:
    print("-----------")
    
    operator=int(input("Press 1 for addition\nPress for subtraction\nPress 3 for multiplication\nPress 4 for dividation\nEnter "))
    
    if operator==1:
        print("Addition:", x+y)
    elif operator==2:
        print("Subtraction:",x-y)
    elif operator==3:
        print("Multiplication:",x*y)
    elif operator==4:
        print("Dividation:",x/y)
    else:
        print("Not a valid Operation")
    
    isStop=input("Press yes if you want to stop ")
    
    if isStop=="yes":
        break
    