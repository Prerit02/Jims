import random
response = input("Do you want to play Rock-Paper-Scissor(Y/N): ")
list1 = ['Rock','Paper','Scissor']
cpu_count = 0
player_count = 0
while response == 'Y':
    choice = input("Select one from Rock/Paper/Scissor: ")
    a = random.choice(list1)
    if choice == 'Rock' and a == 'Paper':
        cpu_count += 1
        player_count += 0
    elif choice == 'Rock' and a == 'Scissor':
        cpu_count += 0
        player_count += 1
    elif choice == 'Rock' and a == 'Rock':
        cpu_count += 0
        player_count += 0
    elif choice == 'Paper' and a == 'Scissor':
        cpu_count += 1
        player_count += 0
    elif choice == 'Scissor' and a == 'Paper':
        cpu_count += 0
        player_count += 1
    response = input("Do you want to continue playing(Y/N): ")
if player_count > cpu_count:
    print("Player Wins")
elif player_count < cpu_count:
    print("CPU Wins")
else:
    print("Game Draw")
