age=10   #Note : Its a global varialble one can access inside the entire code even in the function as well

def Random():
    print("Inside the function",age)


Random()

print("Outside the function", age)
