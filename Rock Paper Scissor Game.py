import sys

playerA = str(input("Player A, please enter your name "))
playerB = str(input("Player B, please enter your name "))

def rockpaperscissors():
    powerplayerA = str(input(playerA + " please choose your power: Rock, Paper or Scissors? "))
    powerplayerB = str(input(playerB + " please choose your power: Rock, Paper or Scissors? "))

    if powerplayerA == powerplayerB:
        print("Its a tie!")
    elif powerplayerA == "Rock":
        if powerplayerB == "Scissors":
            print(playerA + "wins!")
        else:
            print(playerB + "wins!")
    elif powerplayerA == "Paper":
        if powerplayerB == "Rock":
            print(playerA + "wins!")
        else:
            print(playerB + "wins!")
    elif powerplayerA == "Scissors":
        if powerplayerB == "Paper":
            print(playerA + "wins!")
        else:
            print(playerB + "wins!")

    playagain()


def playagain():
    again = str(input("Would you like to play again? Y/N? "))

    if again == "Y":
        rockpaperscissors()
    if again == "N":
        sys.exit()

rockpaperscissors()