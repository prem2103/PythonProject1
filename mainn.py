import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
random_number = random.randint(1, 3)
if random_number == 1:
    comp = 's'
elif random_number == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Your Turn: Choose any one of these  Snake(s) Water(w) or Gun(g): ")

a = gameWin(comp, you)

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

if a is None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")
