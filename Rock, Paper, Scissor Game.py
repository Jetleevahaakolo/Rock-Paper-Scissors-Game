import sys
import getpass

# print title
print("Welcome to rock, paper, scissors!")

# enter players names
playerA = str(input("Player A, please enter your name "))
playerB = str(input("Player B, please enter your name "))

def game():
    # select power
    print(playerA + " please choose your power: 1 = rock, 2 = paper or 3 = scissors? ")
    powerplayerA = int(getpass.getpass("Answer ::"))
    print(playerB + " please choose your power: 1 = rock, 2 = paper or 3 = scissors? ")
    powerplayerB = int(getpass.getpass("Answer ::"))

    # game logic
    if powerplayerA == powerplayerB:
        print(" Its a tie!")
    elif powerplayerA == 1:
        if powerplayerB == 3:
            print("Congrats "+ playerA + "You are the Winner!")
        else:
            print("Congrats "+ playerB + "You are the Winner!")
    elif powerplayerA == 2:
        if powerplayerB == 1:
            print("Congrats "+ playerA + "You are the Winner!")
        else:
            print("Congrats "+ playerB + "You are the Winner!")
    elif powerplayerA == 3:
        if powerplayerB == 2:
            print("Congrats "+ playerA + "You are the Winner!")
        else:
            print("Congrats "+ playerB + "You are the Winner!")
    reset()
            
# restart
def reset():
    again = str(input("Would you like to play again? Y/N? "))

    if again == "y":
        game()
    if again == "n":
        sys.exit()
game()