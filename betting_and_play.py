import math
import random
from variables import *

def determine_player():
    global players_hand, community_hand
    
    all_cards = players_hand + community_hand
    
    # Map face cards to their corresponding values
    face_card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    all_cards = [f"{face_card_values.get(card[:-1], card[:-1])}{card[-1]}" for card in all_cards]
    
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

def determine_computer():
    global dealers_hand, community_hand
    
    all_cards = dealers_hand + community_hand
    
    # Map face cards to their corresponding values
    face_card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    all_cards = [f"{face_card_values.get(card[:-1], card[:-1])}{card[-1]}" for card in all_cards]
    
    # Check for pairs
    pairs = [card[0] for card in all_cards if all_cards.count(card) == 2]
    if len(pairs) == 1:
        return 20
    elif len(pairs) == 2:
        return 30
    
    # Check for three of a kind
    for card in all_cards:
        if all_cards.count(card) == 3:
            return 40
    
    # Check for straight
    values = sorted([int(card[:-1]) for card in all_cards])
    for i in range(len(values)-4):
        if values[i:i+5] == list(range(values[i], values[i]+5)):
            return 50
    
    # Check for flush
    suits = [card[-1] for card in all_cards]
    for suit in "HDCS":
        if suits.count(suit) >= 5:
            return 60
    
    # Check for full house
    for card in all_cards:
        if all_cards.count(card) == 3:
            for card2 in all_cards:
                if card != card2 and all_cards.count(card2) == 2:
                    return 70
    
    # Check for four of a kind
    for card in all_cards:
        if all_cards.count(card) == 4:
            return 80
    
    # Check for royal flush
    for suit in "HDCS":
        suit_cards = [card for card in all_cards if card.endswith(suit)]
        values = sorted([int(card[:-1]) for card in suit_cards])
        if values == [10, 11, 12, 13, 14]:
            return 90
        
    # If no hand is found, return high card
    values = sorted([int(card[:-1]) for card in all_cards])
    return 10

def determine_computer_player():
    global players_hand, community_hand
    
    all_cards = players_hand + community_hand
    
    # Map face cards to their corresponding values
    face_card_values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    all_cards = [f"{face_card_values.get(card[:-1], card[:-1])}{card[-1]}" for card in all_cards]
    
    # Check for pairs
    pairs = [card[0] for card in all_cards if all_cards.count(card) == 2]
    if len(pairs) == 1:
        return 20
    elif len(pairs) == 2:
        return 30
    
    # Check for three of a kind
    for card in all_cards:
        if all_cards.count(card) == 3:
            return 40
    
    # Check for straight
    values = sorted([int(card[:-1]) for card in all_cards])
    for i in range(len(values)-4):
        if values[i:i+5] == list(range(values[i], values[i]+5)):
            return 50
    
    # Check for flush
    suits = [card[-1] for card in all_cards]
    for suit in "HDCS":
        if suits.count(suit) >= 5:
            return 60
    
    # Check for full house
    for card in all_cards:
        if all_cards.count(card) == 3:
            for card2 in all_cards:
                if card != card2 and all_cards.count(card2) == 2:
                    return 70
    
    # Check for four of a kind
    for card in all_cards:
        if all_cards.count(card) == 4:
            return 80
    
    # Check for royal flush
    for suit in "HDCS":
        suit_cards = [card for card in all_cards if card.endswith(suit)]
        values = sorted([int(card[:-1]) for card in suit_cards])
        if values == [10, 11, 12, 13, 14]:
            return 90
        
    # If no hand is found, return high card
    values = sorted([int(card[:-1]) for card in all_cards])
    return 10

# Betting and Probabilities 
# Player Betting --> WinRate --> Calling/Folding
# Bank, and Account Checking

def player_betting():
    global current_bet,player_money,current_bet
    
    if current_bet == 0:
        response = input("Would you like to place a bet? (yes/no) ").lower()
        if response in ["yes", "y"]:
            bet = int(input(f"How much would you like to bet? (You have ${player_money}) "))
            if bet < 1:
                print("The minimum bet is $1.")
                betting()
            elif bet > player_money:
                print("You do not have enough money to place that bet.")
                betting()
            else:
                current_bet = bet
                player_money -= bet
                print(f"You have placed a bet of ${bet}.")
    else:
        response = input(f"The current bet is ${current_bet}. Would you like to call, raise, or fold? ").lower()
        if response == "call":
            if player_money >= current_bet:
                player_money -= current_bet
                print("You have called the current bet.")
            else:
                print("You do not have enough money to call the current bet.")
                betting()
        elif response == "raise":
            new_bet = int(input(f"How much would you like to raise the bet to? (You have ${player_money - current_bet}) "))
            if new_bet < current_bet:
                print("You cannot raise the bet by less than the current bet.")
                betting()
            elif new_bet > player_money - current_bet:
                print("You do not have enough money to raise that much.")
                betting()
            else:
                current_bet = new_bet + current_bet
                player_money -= current_bet
                print(f"You have raised the bet to ${current_bet}.")
        elif response == "fold":
            print("You have folded.")
        else:
            print("Invalid response.")
            betting()

def computer_decision():
    global current_bet,dealer_money
    
    i = determine_computer()
    if i == 10:
        # Fold
        print("The dealer folds. ")   
        current_bet = 0 
    elif i >= 20: 
        # Call
        dealer_money -= current_bet
        current_bet *= 2
    # elif i >= 80:
    #     # Raise
    else:
        pass

def game_outcome():
    global player_money,dealer_money,current_bet
    
    if determine_computer() > determine_computer_player():
        print("The dealer wins!")
        dealer_money += current_bet
        player_money -= current_bet
        current_bet = 0
    elif determine_computer() < determine_computer_player():
        print("The player wins!")
        dealer_money -= current_bet
        players_money += current_bet
        current_bet = 0
    # elif determine_computer() == determine_computer_player():
         
        
    else:
        print("Game error. ")

def deal_cards():
    global players_hand,dealers_hand,community_hand
    players_hand.append(deck.pop())
    dealers_hand.append(deck.pop())
    community_hand.append(deck.pop())

def reset_game():
    global player_money,players_hand,dealer_money,dealers_hand,current_bet, community_hand, deck

    player_money = 100
    players_hand = []
    dealer_money = 100
    dealers_hand = []
    current_bet = 0
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

def choice():
    play = input("Would you like to play texas holdem? (yes/no)\n").lower() 
    if play in ["yes", "y"]:
        return True
    elif play in ["no", "n"]:
        reset_game()
        return False
    else:
        print("Please input a valid response. \n")
        choice()

def playing_game():
    global player_money,players_hand,dealer_money,dealers_hand
    
    # Cards shuffled and game dealt. 
    random.shuffle(deck)
    print("Welcome to Texas Holdem. You be playing against the dealer to start please look at you cards and place a bet. ")
    for i in range(2):
        deal_cards()
    community_hand.append(deck.pop())
    
    # Buy in.
    player_betting()
    
    computer_decision()
    i = current_bet
    
    # Second Stage.
    if player_money < 100:
        print(f"Your hand is, {players_hand}. ")
        community_hand.append(deck.pop())
        print(f"The flop now contains {community_hand}. ")
        determine_player()
        player_betting()
        computer_decision()
        
        # Third and Final Stage
        if current_bet > i:
            community_hand.append(deck.pop())
            print(f"The flop now contains {community_hand}. ")
            determine_player()
            player_betting()
            computer_decision()
            game_outcome()
        else:
            reset_game()
            print("You folded! ")
            
    # Folding outcomes and game error
    elif player_money == 100 :
        reset_game()
        return "You folded! "
    elif dealer_money == 100:
        reset_game()
        return "Dealer folded! "
    else:
        print("Game error. ")
        