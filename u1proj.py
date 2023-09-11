userPick = []

game = True
def userSelection():
    u1choice = True
    u2choice = True
    while len(userPick) < 2:
        while u1choice == True:
            u1 = input("Player one do you want to play Rock(r), Paper(p), or Scizzors(s)").lower()
            if u1 == "r" or u1 == "s" or u1 == "p":
                userPick.append(u1)
                u1choice = False
            else:
                print("Please pick one of the options")
        while u2choice == True:
            u2 = input("Player two do you want to play Rock(r), Paper(p), or Scizzors(s)").lower()
            if u2 == "r" or u2 == "s" or u2 == "p":
                userPick.append(u2)
                u2choice = False
            else:
                print("Please pick one of the options")
                
        print(userPick)

def playGame():
        userSelection()
        if userPick[0] == "r" and userPick[1] == "p":
            print("User 2 Wins")
        if userPick[0] == "p" and userPick[1] == "r":
            print("User 1 Wins")
        if userPick[0] == "p" and userPick[1] == "s":
            print("User 2 Wins")
        if userPick[0] == "s" and userPick[1] == "p":
            print("User 1 Wins")
        if userPick[0] == "s" and userPick[1] == "r":
            print("User 2 Wins")
        if userPick[0] == "r" and userPick[1] == "s":
            print("User 1 Wins")
        if userPick[0] == "r" and userPick[1] == "r":
            print("Tie")
        if userPick[0] == "s" and userPick[1] == "s":
            print("Tie")
        if userPick[0] == "p" and userPick[1] == "p":
            print("Tie")

playGame()
