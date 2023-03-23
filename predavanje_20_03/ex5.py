# Napravite program koji će vam omogućiti igranje igre protiv računala - kamen, škare, papir

import random

computerChoice = random.randint(1, 3)
userChoice = input("Choose rock, paper or scissors: ").lower()
possibleChoices = {"rock": 1, "paper": 2, "scissors": 3}


def rockPaperScissors(choice):
    if possibleChoices[choice] == computerChoice:
        print(f"Draw, you both chose {choice}")
    if (
        (possibleChoices[choice] == 1 and computerChoice == 3)
        or (possibleChoices[choice] == 2 and computerChoice == 1)
        or (possibleChoices[choice] == 3 and computerChoice == 2)
    ):
        print(
            f"You win, {choice} beats {list(possibleChoices.keys())[computerChoice-1]}"
        )
    if (
        (possibleChoices[choice] == 3 and computerChoice == 1)
        or (possibleChoices[choice] == 1 and computerChoice == 2)
        or (possibleChoices[choice] == 2 and computerChoice == 3)
    ):
        print(
            f"You lose, {list(possibleChoices.keys())[computerChoice-1]} beats {choice}"
        )


rockPaperScissors(userChoice)
