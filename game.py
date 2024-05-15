import random

def gamewon(comp,you):
    if comp==you:
        return None
    
    elif comp=="s":
        if you=="w":
            return False
        if you=="g":
            return True
        

    elif comp=="w":
        if you=="g":
            return False
        if you=="s":
            return True
        

    elif comp=="g":
        if you=="s":
            return False
        if you=="w":
            return True


print("comp turn : Snake(s),Water(w),Gun(g):-")
randnum = random.randint(1,3)

if randnum==1:
    comp = "s"
elif randnum==2:
    comp="w"
elif randnum==3:
    comp="g"

you = input("your turn : Snake(s),Water(w),Gun(g):-")

a = gamewon(comp,you)

print("computer choose :-",comp)
print("you choose :-",you)

if a==None:
    print("Game tied!")
elif a:
    print("You won the game!")
else:
    print("You lose the game!")