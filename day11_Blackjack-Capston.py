import os
import random
from art import logo


arr = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
liP = [];
liC = [];


def a_random_number():
    x = random.randint(0, 12)
    return x


def add_card(liP):
    x = random.randint(0, 12)
    liP.append(arr[x])


def sum_nums(liP):
    s = 0
    for i in liP:
        s += liP[i]
    return s


def if_bust(li):
    s1 = 0
    for i in li:
        s1 += i
    if s1 > 21:
        return True
    return False


def calculate_result(liP, liC):
    s1 = 0
    s2 = 0
    for i in liP:
        s1 += i
    for i in liC:
        s2 += i
        if s2 > s1:
            print("Computer win")
            return

    if s1 > 21:
        print("You are bust")
        print("Computer wins")
    elif s2 > 21:
        print("Computer is bust")
        print("You win")
    else:
        if s1 > s2:
            print(f"Your cards are {liP} \n")
            print(f"Computer's cards are {liC} \n")
            print("You win")
        elif s1 < s2:
            print(f"Your cards are {liP} \n")
            print(f"Computer's cards are {liC}  \n")
            print("Computer win")
        else:
            print("Game is a draw")


def black_jack():
    while 1:

        liP = [];
        liC = [];
        x1 = a_random_number()
        x2 = a_random_number()
        liP.append(arr[x1])
        liP.append(arr[x2]);

        print(f"Your cards are {liP} \n")

        y1 = a_random_number()
        y2 = a_random_number()
        liC.append(arr[y1])

        print(f"Computer's cards are {liC} and $ \n")
        liC.append(arr[y2])

        while 1:
            calc = int(input("To hit press 1, to stand press 2"))
            if calc == 1:
                add_card(liP)
                if if_bust(liP):
                    print(f"Your cards are {liP} \n")
                    print(f"Computer's cards are {liC}  \n")
                    print("You are bust")
                    print("Computer wins")
                    break
                print(f"Your cards are {liP} \n")
                print(f"Computer's cards are {liC} and $ \n")
                add_card(liC)
                if if_bust(liC):
                    print(f"Your cards are {liP} \n")
                    print(f"Computer's cards are {liC}  \n")
                    print("Computer is bust")
                    print("You win")
                    break

            else:
                calculate_result(liP, liC)
                break

        ch = input("Do you want to continue play Blackjack \n")
        if ch == 'n':
            print("Thank you for being here.")
            print("Have a nice day")
            break
        # os.system("cls || clear")

        # os.system("clear")
        print("\n" *20)
        print(logo)


start = input("Do you want to play BlackJack ?")
if start == 'y':
    print(logo)
    black_jack()
else:
    print("Thank you for being here.")
    print("Have a nice day")
