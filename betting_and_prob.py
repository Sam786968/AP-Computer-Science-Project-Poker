import math
import random
from variables_running_game import *

 # Determine the type of hand
def determine_hand(x, community_cards):
    all_cards = x + community_cards
    
    # Check for pairs
    pairs = [card[0] for card in all_cards if all_cards.count(card) == 2]
    if len(pairs) == 1:
        return f"One pair of {pairs[0]}s"
    elif len(pairs) == 2:
        return f"Two pairs: {pairs[0]}s and {pairs[1]}s"
    
    # Check for three of a kind
    for card in all_cards:
        if all_cards.count(card) == 3:
            return f"Three of a kind: {card[0]}s"
    
    # Check for straight
    values = sorted([int(card[:-1]) for card in all_cards])
    for i in range(len(values)-4):
        if values[i:i+5] == list(range(values[i], values[i]+5)):
            return "Straight"
    
    # Check for flush
    suits = [card[-1] for card in all_cards]
    for suit in "HDCS":
        if suits.count(suit) >= 5:
            return f"Flush ({suit})"
    
    # Check for full house
    for card in all_cards:
        if all_cards.count(card) == 3:
            for card2 in all_cards:
                if card != card2 and all_cards.count(card2) == 2:
                    return f"Full house: {card[0]}s over {card2[0]}s"
    
    # Check for four of a kind
    for card in all_cards:
        if all_cards.count(card) == 4:
            return f"Four of a kind: {card[0]}s"
    
    # Check for royal flush
    for suit in "HDCS":
        suit_cards = [card for card in all_cards if card.endswith(suit)]
        values = sorted([int(card[:-1]) for card in suit_cards])
        if values == [10, 11, 12, 13, 14]:
            return f"Royal flush ({suit})"

        # If no hand is found, return high card
    values = sorted([int(card[:-1]) for card in all_cards])
    return f"High card: {values[-1]}"


# Shuffle Deck
def choice():
    play = input("Would you like to play texas holdem? (yes/no)\n").lower() 
    if play==("yes" or "y"):
        return True
    elif play==("no" or "n"):
        return False
    else:
        print("Please input a valid response. \n")
        choice()
   
   
# Betting and Probabilities 
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
