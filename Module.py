# Module
import sys 
import getpass

def title(title):
    print("Welcome to rock, paper, scissors!")
    
def rockpaperscissors():
    
    start = True

    if start == True:
        playerA = str(input("Player A, please enter your name "))
        playerB = str(input("Player B, please enter your name "))
        start = False

    print(playerA + " please choose your power: Rock, Paper or Scissors? ")
    powerplayerA = getpass.getpass("Answer ::")
    print(playerB + " please choose your power: Rock, Paper or Scissors? ")
    powerplayerB = getpass.getpass("Answer ::")

    if powerplayerA == powerplayerB:
        print(" Its a tie!")
    elif powerplayerA == "rock":
        if powerplayerB == "scissors":
            print(playerA + " wins!")
        else:
            print(playerB + " wins!")
    elif powerplayerA == "paper":
        if powerplayerB == "rock":
            print(playerA + " wins!")
        else:
            print(playerB + " wins!")
    elif powerplayerA == "sciccors":
        if powerplayerB == " paper":
            print(playerA + " wins!")
        else:
            print(playerB + " wins!")

    playagain()


def playagain():
    again = str(input("Would you like to play again? Y/N? "))

    if again == "Y":
        rockpaperscissors()
    if again == "N":
        sys.exit()