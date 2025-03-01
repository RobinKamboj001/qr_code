import random

secrate_numbeer = random.randint(1, 100)
atempt = 0

print("Number Guessing Game")
print("Gass Number Bettwen 1 to 100")

while True:
    try:
        gass = int(input("Enter Your Number = "))
        atempt += 1
        if gass > secrate_numbeer:
            print("Ohh Selact Lower Number")
        elif gass < secrate_numbeer:
            print("Ohh Selact Higer Number")
        else:
            print(f"You Gass {secrate_numbeer} Number in {atempt} Atempts")
            break

    except ValueError:
        print("Selact Right Number")
        
