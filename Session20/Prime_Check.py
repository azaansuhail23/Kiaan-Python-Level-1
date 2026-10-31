def Check_Prime(n):
    #Learn
    if n==2:
        return True
    
    for i in range(3,n):
        if n%i==0:
            return False
    
    return True

print(Check_Prime(19))


for i in range(2,101):
    print(i,Check_Prime(i))