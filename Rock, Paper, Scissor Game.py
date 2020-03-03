import sys
import getpass
import Module
# variable
game = True

# print title
print("Welcome to rock, paper, scissors!")

# enter players names
playerA = str(input("Player A, please enter your name "))
playerB = str(input("Player B, please enter your name "))

def game():
    # select power
    print(playerA + " please choose your power: 1 = Rock, 2 = Paper or 3 = Scissors? ")
    powerplayerA = int(getpass.getpass("Answer ::"))
    print(playerB + " please choose your power: 1 = Rock, 2 = Paper or 3 = Scissors? ")
    powerplayerB = int(getpass.getpass("Answer ::"))

    # game logic
    if powerplayerA == powerplayerB:
        print(" Its a tie!")
    elif powerplayerA == 1:
        if powerplayerB == 3:
            print(playerA + " wins!")
        else:
            print(playerB + " wins!")
    elif powerplayerA == 2:
        if powerplayerB == 1:
            print(playerA + " wins!")
        else:
            print(playerB + " wins!")
    elif powerplayerA == 3:
        if powerplayerB == 2:
            print(playerA + " wins!")
        else:
            print(playerB + " wins!")

    reset()
            
    # restart
def reset():
    again = str(input("Would you like to play again? Y/N? "))

    if again == "y":
        game()
    if again == "n":
        sys.exit()

game()