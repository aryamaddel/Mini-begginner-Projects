import random


def dice_roll():
    number_of_dice = int(input("How many dice do you want to roll?\n:"))
    for i in range(number_of_dice):
        print('_________________________________________________________________\n')
        print(random.randint(1, 6), '\n')


dice_roll()
