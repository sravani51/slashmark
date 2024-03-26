import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")
    return name

def pick(name):
    number = random.randint(1, 200)
    guesses_taken = 0
    while guesses_taken < 6:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guess < number:
                    print("The guess is too low.")
                elif guess > number:
                    print("The guess is too high.")
                else:
                    print('Good job, ' + name + '! You guessed my number in ' + str(guesses_taken) + ' guesses!')
                    return
            else:
                print("Please enter a number between 1 and 200.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print('Nope. The number I was thinking of was ' + str(number))

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    player_name = intro()
    pick(player_name)
    play_again = input("Do you want to play again? (yes/no): ")