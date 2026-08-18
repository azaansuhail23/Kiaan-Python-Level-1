num = int(input("Enter the number "))


fact = 1
i = 1

while i <= num:  # loop
    fact = fact * i

    i += 1

print(f"The factorial of a number {num} is {fact}")
