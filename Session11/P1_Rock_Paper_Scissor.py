import random  # random is a inbuilt

game = [
    """
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
    PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
   SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

# ASCII Values

print(game[0])
print(game[1])
print(game[2])

user = int(input("What do you choose?\n 0=Rock\n 1=Paper\n 2=Scissor\n Enter: "))

if user > 2 or user < 0:
    print("Invalid Choice!")
else:
    computer = random.randint(0, 2)

    print("You chosse : ")
    print(game[user])

    print("Computer choose : ")
    print(game[computer])

    if user == computer:
        print("🤝 Draw!")
    elif user == 0 and computer == 1:
        print("You Loose!")
    elif user == 0 and computer == 2:
        print("🎉 You Win!")
    elif user == 1 and computer == 0:
        print("🎉 You Win!")
    elif user == 1 and computer == 2:
        print("You Loose!")
    elif user == 2 and computer == 0:
        print("You Loose!")
    else:
        print("🎉 You Win!")
