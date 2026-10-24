def list_product(list):
    prod=1  #Learn
    
    for i in range(len(list)):
        prod=prod*list[i]
    
    print("The product of the list elements is",prod)


def list_sum(list):
    sum=0 #Learn
    
    for i in range(len(list)):
        sum=sum + list[i]
    
    print("The sum of the list elements is",sum)

list=[1,2,3,4,5]

list_product(list)

list_sum(list)

# Homework : https://sandbox.codeyoung.com/#/exercises/1D4gwFgTA6Yw/eFlfTRM6PP1U
