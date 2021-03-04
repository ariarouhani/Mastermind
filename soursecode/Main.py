
import soursecode.AI.ai as ai

from soursecode.model.letters import Letters
from soursecode.model.board import Board


b1 = Board()
l1 = Letters()

ai.fill_spot(l1, b1)



def game_over(state: bool):
    if state:
        print("***YOU WIN ASSHOLE***")
    else:
        print('sry you are out of lives! Fucking bitch')


def correctness(guess: str):
    temp = []
    for i in range(len(b1.spot)):
        if guess[i] == b1.spot[i]:
            temp.append("C")
        else:
            if guess[i] in b1.spot:
                temp.append("MP")
            else:
                temp.append("N")

    return temp


def handle_lives(guess, lives):
    temp = correctness(guess)
    print()
    print(list(guess))
    print(temp)
    print()
    for i in range(len(temp)):
        if temp[i] != "C":
            lives -= 1
            return lives
    else:
        game_over(True)


def init():
    lives = len(b1.spot) * 3
    while lives > 0:
        print("You have", lives, "left")
        guess = input('please enter your guess : ').upper()
        if guess == "HESOYAM":
            print(b1.spot)
        lives = handle_lives(guess, lives)
        if lives is None:
            break
    if lives == 0:
        game_over(False)


init()
