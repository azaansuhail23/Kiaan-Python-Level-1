char = "A"
ascii_value = ord(char)
print(f"ASCII value of {char} is {ascii_value}")  # Output: ASCII value of A is 65

char_B = "B"
print("The ascii value of B is",ord(char_B))

print("---------")

for row in range(1, 6):
    character = "A"

    for col in range(row):
        print(character, end="")

        character = chr(ord(character) + 1)
    print()
