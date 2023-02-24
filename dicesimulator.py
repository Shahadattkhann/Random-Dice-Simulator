from  dice_disgn import design
from random import randint

while True:
    roll_again = input("'y' for roll, and 'n' for no: ")
    if roll_again == "y":
        no = randint(1,6)
        design(no)
        continue
    elif roll_again == "n":
        break
    else:
        print("invalid!")
        continue
print(f"Exit From Rollin Dice")