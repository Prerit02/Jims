import random
a = random.randint(10,100)
print(a)
choice = input("Do you want to play the game(Y/N): ")
while choice == 'Y':
    b = int(input("Guess the Number: "))
    if a == b:
        print("Hurray! You've guessed the right number.")
        break
    elif b>a:
        print("Guess a smaller number.")
    else:
        print("Guess a larger number.")
    choice = input("Do you want to guess again(Y/N): ")
