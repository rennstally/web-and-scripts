import random

choices = ["rock", "paper", "scissors "] 

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print("computer choose:", computer)

if user == computer:
        print("its a tie")
        
elif user == "rock":
    if computer == "scissors":
       print("You win")
    else: 
         print("You lost!")

elif user == "paper":
    if computer == "rock":
         print("you win")
    else:
         print("you lose")

elif user == "scissors":
    if computer == "paper":
          print("you win")
    else:
          print("you lose")
else:
    print("Invalid choice")
