def call_by_value(age):
    age = age + 5

    print("Inside the function", age)


age = 10

# calling/invoking function
call_by_value(age)

print("Outside the function", age)


#Learn : Whenever you pass a variable to a function and you do certain changes it will reflect only in the function but not outside the function.(remain same --> changes does not reflect)