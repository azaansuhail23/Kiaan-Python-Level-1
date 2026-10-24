def call_by_reference(list):
    list[0]="Kiaan"
    
    print("Inside the list", list)

list=[11,12,13,14,15]

call_by_reference(list)

print("Outside the list", list)

# Learn : Whenever you pass a list to a function and you do certain changes it will reflects both in function and outside the function.
