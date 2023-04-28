import math
import random

# Variables for all code.
bank = 100 
players_hand = []
dealers_hand = []
community_hand = []
deck = ['2H', '2D', '2S', '2C',
        '3H', '3D', '3S', '3C',
        '4H', '4D', '4S', '4C',
        '5H', '5D', '5S', '5C',
        '6H', '6D', '6S', '6C',
        '7H', '7D', '7S', '7C',
        '8H', '8D', '8S', '8C',
        '9H', '9D', '9S', '9C',
        'TH', 'TD', 'TS', 'TC',
        'JH', 'JD', 'JS', 'JC',
        'QH', 'QD', 'QS', 'QC',
        'KH', 'KD', 'KS', 'KC',
        'AH', 'AD', 'AS', 'AC']

# Betting and Probability
scores = {
    'One Pair': 10,
    'Two Pair': 20,
    'Three of a Kind': 30,
    'Straight': 40,
    'Flush': 50,
    'Full House': 60,
    'Four of a Kind': 70,
    'Straight Flush': 80,
    'The Flop': 90,
}

# Running Main Function 
def choice():
    play = input("Would you like to play texas holdem? (yes/no)\n").lower() 
    if play.str.contains("yes" or "y"):
        return True
    elif play.str.contains("no" or "n"):
        return False
    else:
        print("Please input a valid response. \n")
        choice()
        

while choice() == True:
    random.shuffle(deck)
    print("Welcome to Texas Holdem. You be playing against the dealer to start please look at you cards and place a bet. ")
    for i in range(2):
        players_hand.append(deck.pop())
        dealers_hand.append(deck.pop())
        community_hand.append(deck.pop())
    community_hand.append(deck.pop())
    print(players_hand)
    i = one_pair(players_hand)
    print(i)
    choice()
    break
