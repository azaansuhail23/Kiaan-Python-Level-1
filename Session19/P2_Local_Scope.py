def Random():
    age=10  #Note : age is having local scope means one can acces inside that particular function where it is used.
    
    print("Inside the function",age)

print("Outside the function",age)