import random 

# Ap CompSci Principles -- Sam Zajczenko -- Texas Holdem

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
        '10H', '10D', '10S', '10C',
        'JH', 'JD', 'JS', 'JC',
        'QH', 'QD', 'QS', 'QC',
        'KH', 'KD', 'KS', 'KC',
        'AH', 'AD', 'AS', 'AC']

# Shuffle Deck
random.shuffle(deck)
players_hand = [deck.pop, deck.pop]
dealers_hand = [deck.pop, deck.pop]
community_hand = [deck.pop, deck.pop, deck.pop]

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

def computer_raise():


# One Pair
def one_pair(): 
    pass

# Two Pair

# Three of a Kind

# Straight

# Flush

# Full House

# Four of a Kind

# Straight Flush

# The Flop


# Running Main Function 
def choice():
    play = input("Would you like to play texas holdem? (yes/no)\n").lower() 
    if play.contains("yes" or "y"):
        return True
    elif play.contains("no" or "n"):
        return False
    else:
        print("Please input a valid response. \n")
        choice()
        
playing = choice()

while playing == True:
    pass