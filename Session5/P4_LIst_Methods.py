name=["K","I","A","A","N"]

print(len(name))

# 1. append -> will add any data type(one at a time) at the end
name.append(9)
name.append("Azaan")
name.append(False)
print(name)

# 2. extend -> will add multiple elements at time
name.extend(['Rastogi','Suhail',24,12,70.12])
print(name)

# 3. count -> will give the count of a particular element
marks=[12,13,8,9,0,8,17,12,13,13,8]
print(marks.count(8))


# 4. index -> will give me the position/index of the element appeared for the first time
print(marks.index(8))

# 5. Revese
list=[1,2,3,4,5]
list.reverse()

print(list)

# 5 4 3 2 1
list.pop()
print(list)  # 5 4 3 2 


# https://www.w3schools.com/python/python_lists_methods.asp