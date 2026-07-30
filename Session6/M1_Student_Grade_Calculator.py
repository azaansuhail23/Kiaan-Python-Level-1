name=input("Enter your name ")

sub1=int(input("Enter the Subject 1 Marks "))
sub2=int(input("Enter the Subject 2 Marks "))
sub3=int(input("Enter the Subject 3 Marks "))


total_marks=sub1+sub2+sub3
# average_marks=total_marks/3
average_marks=total_marks//3

print("Total Marks= ",total_marks)
print("Average Marks= ",average_marks)

if total_marks>=150:    #50%
    print(f"Congratulations {name} is passed!")
else:
    print(f"Sorry {name} try again")