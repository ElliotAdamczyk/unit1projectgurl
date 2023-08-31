userPick = []

def userSelection():
    while userPick <= 2:
        u1 = input("Player one do you want to play Rock(r), Paper(p), or Scizzors(s)")
        u2 = input("Player two do you want to play Rock(r), Paper(p), or Scizzors(s)")
        if u1 == "r" or u1 == "s" or u1 == "p":
            userPick.append(u1)
        
print (userSelection())
print (userPick)
