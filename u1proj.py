userPick = []

def userSelection():
    while len(userPick) < 2:
        u1 = input("Player one do you want to play Rock(r), Paper(p), or Scizzors(s)").lower()
        u2 = input("Player two do you want to play Rock(r), Paper(p), or Scizzors(s)").lower()
        if u1 == "r" or u1 == "s" or u1 == "p":
            userPick.append(u1)
        else:
            print("Please pick one of the options")
        if u2 == "r" or u2 == "s" or u2 == "p":
            userPick.append(u2)
        else:
            print("Please pick one of the options")
          



print (userSelection())
print (userPick)
