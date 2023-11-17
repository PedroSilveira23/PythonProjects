import random

def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    
    
    roll = input("Roll the dice? (Yes/No) ")
    
    while roll.lower() == "Yes".lower():
        #gerado um numero aleatorio de 1 a 6
        dice1 = random.randint(1, 6)
        #gerado um numero aleatorio de 1 a 6
        dice2 = random.randint(1, 6)
        
        print("Dice rolled: {} and {} ".format(dice1, dice2))
        #impressao do numero gerado do dice1
        print("\n".join(dice_drawing[dice1]))
        #impressao do numero gerado do dice2
        print("\n".join(dice_drawing[dice2]))
        
        roll = input("Roll dice again? (Yes/No) ")
    
roll_dice()