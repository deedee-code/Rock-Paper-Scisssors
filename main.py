import random

#"R" for "rock"
#"P" for "paper"
#"S" for "scissors"


while True:
    choices = ['R', 'P', 'S']

    CPU = random.choice(choices)
    player = None

    while player not in choices:
        player = input('R, P, or S?: ').upper()

    if player == CPU:
        print("CPU: ", CPU)
        print("player: ", player)
        print("Tie!")
    elif player == "R":
        if CPU == "P":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "S":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Win!")
    elif player == "S":
        if CPU == "R":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "P":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Win!")
    elif player == "P":
        if CPU == "S":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "R":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Win!")

    play_again = input("play again? (Yes/No): ").lower()

    if play_again != 'yes':
        break

print("Bye!")