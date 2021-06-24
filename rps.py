from random import randint
def playGame():

    t = ["rock", "paper", "scissors"]

    comp = t[randint(0, 2)]
    player = False

    while player == False:
        print("choose one of the following:")
        player = input(t)

        if player == comp:
            print("tie")
        elif player == "rock":
            if comp == "scissors":
                print("player wins! ", player, "smashes", comp)
            else:
                print("player loses! ", comp, "covers", player)
        elif player == "scissors":
            if comp == "paper":
                print("player wins! ", player, "cuts", comp)
            else:
                print("player loses! ", comp, "smashes", player)
        elif player == "paper":
            if comp == "rock":
                print("player wins! ", player, "covers", comp)
            else:
                print("player loses! ", comp, "cuts", player)
        else:
            print("That's not a valid choice, choose again!")

        player = False
        comp = t[randint(0,2)]
