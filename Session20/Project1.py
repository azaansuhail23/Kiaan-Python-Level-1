cart={}

print(type(cart))

def add_item(name,price):
    #Updating the price if it exist
    if name in cart:
        cart[name] +=price
    else:
        cart[name]=price
        
add_item("milk",20)
add_item("Chocolates",221)
add_item("Bread",40)
add_item("Chocolates",20)
add_item("milk",19)
add_item("Chocolates",21)
add_item("Bread",33)
add_item("Chocolates",9)


#Homework : Implement the unique functionality 

# Creata a set & loop over the keys of dictionary and store it and print the set which will contains unique items