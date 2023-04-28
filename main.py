import random 

# Ap CompSci Principles -- Sam Zajczenko -- Texas Holdem
# This program simulates playing texas holdem poker with a dealer. The program has features that 
# all the player to bet, call, fold.

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

# Shuffle Deck
random.shuffle(deck)

def start(players_hand, dealers_hand, community_hand):
    print("Welcome to Texas Holdem. You be playing against the dealer to start please look at you cards and place a bet. ")
    for i in range(2):
        players_hand.append(deck.pop)
        dealers_hand.append(deck.pop)
        community_hand(deck.pop)
    community_hand(deck.pop)
    return players_hand, dealers_hand, community_hand

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

def win_rate():
    # This function will calculate a win rate for the dealer and advise them whether they should bet casino cash.
    pass

def winner():
    pass

def checking():
    i = input(" ")

def betting():
    i = input("Would you like to place a bet? (yes/no)\n")
    if i.contains("yes" or "y"):
        print(f"You have {bank} dollars. \n")
        def item():
            i = int(input("How much would you like to bet? "))
            if i > bank:
                print("Not a possible value. ")
                item()
            elif i <= bank:
                print("Your bet has been placed. ")
                return i
            elif i <= -1:
                print("Not a possible value. ")
                item()
        return item()
    else:
        pass


pot = betting()

def computer_bet():
    if win_rate() > 20: 
        print("The dealer checks. ")
        checking()
        pass

# Playing the game.


# One Pair -- Done
def one_pair(y):
    x = y.append(community_hand)
    values = [card[:-1] for card in x]
    return any(values.count(value) == 2 for value in set(values))

# Two Pair
def two_pair(y):
    x = y.append(community_hand)
    values = [card[:-1] for card in x]
    return any(values.count(value) == 2 for value in set(values))

# Three of a Kind -- Done
def one_pair(x):
    values = [card[:-1] for card in x]
    return any(values.count(value) == 3 for value in set(values))

# Straight


# Flush

# Full House

# Four of a Kind

# Straight Flush

# The Flop


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
        
playing = choice()

while playing == True:
    start(players_hand, dealers_hand, community_hand)
    pass