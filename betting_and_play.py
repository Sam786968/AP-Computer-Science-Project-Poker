import math
import random
from variables import *

def determine_player():
    global players_hand, community_hand
    """
    This function checks the given player's hand and the community cards
    to determine the best possible poker hand.
    """
    # Concatenate the player's and community cards
    cards = players_hand + community_hand
    
    # Count the frequency of each rank and suit
    ranks = {}
    suits = {}
    for card in cards:
        rank, suit = card[0], card[1]
        ranks[rank] = ranks.get(rank, 0) + 1
        suits[suit] = suits.get(suit, 0) + 1
    
    # Check for a flush
    flush = False
    for suit in suits:
        if suits[suit] >= 5:
            flush = True
            flush_suit = suit
            break
    
    # Check for a straight
    straight = False
    for rank in ranks:
        if ranks.get(rank) and ranks.get(chr(ord(rank)+1)) and ranks.get(chr(ord(rank)+2)) and ranks.get(chr(ord(rank)+3)) and ranks.get(chr(ord(rank)+4)):
            straight = True
            straight_rank = rank
            break
        elif ranks.get('A') and ranks.get('2') and ranks.get('3') and ranks.get('4') and ranks.get('5'):
            straight = True
            straight_rank = '5'
            break
    
    # Check for a straight flush
    straight_flush = False
    if flush and straight:
        straight_flush_cards = [card for card in cards if card[1] == flush_suit and (card[0] == straight_rank or card[0] in 'TJQKA')]
        if len(straight_flush_cards) >= 5:
            straight_flush = True
    
    # Check for four of a kind
    four_of_a_kind = False
    four_of_a_kind_rank = None
    for rank in ranks:
        if ranks[rank] == 4:
            four_of_a_kind = True
            four_of_a_kind_rank = rank
            break
    
    # Check for full house
    full_house = False
    full_house_rank1 = None
    full_house_rank2 = None
    for rank in ranks:
        if ranks[rank] == 3:
            full_house_rank1 = rank
            for rank2 in ranks:
                if rank2 != rank and ranks[rank2] >= 2:
                    full_house = True
                    full_house_rank2 = rank2
                    break
            if full_house:
                break
    
    # Check for three of a kind
    three_of_a_kind = False
    three_of_a_kind_rank = None
    for rank in ranks:
        if ranks[rank] == 3:
            three_of_a_kind = True
            three_of_a_kind_rank = rank
            break
    
    # Check for two pairs
    two_pairs = False
    pair_ranks = []
    for rank in ranks:
        if ranks[rank] == 2:
            pair_ranks.append(rank)
    if len(pair_ranks) >= 2:
        two_pairs = True
    
    # Check for one pair
    one_pair = False
    one_pair_rank = None
    for rank in ranks:
        if ranks[rank] == 2:
            one_pair = True
            one_pair_rank = rank
            break
    
    # Determine the best hand
    if straight_flush:
        return "Straight flush"
    elif four_of_a_kind:
        return "Four of a kind"
    elif full_house:
        return "Full house"
    elif flush:
        return "Flush"
    elif straight:
        return "Straight"
    elif three_of_a_kind:
        return "Three of a kind"
    elif two_pairs:
        return "Two pairs"
    elif one_pair:
        return "One pair"
    else:
        # If the player has no pair or better, return the highest card
        return "High card: " + max(ranks.keys())

def determine_computer():
    global dealers_hand, community_hand
    """
    This function checks the given player's hand and the community cards
    to determine the best possible poker hand.
    """
    # Concatenate the player's and community cards
    cards = dealers_hand + community_hand
    
    # Count the frequency of each rank and suit
    ranks = {}
    suits = {}
    for card in cards:
        rank, suit = card[0], card[1]
        ranks[rank] = ranks.get(rank, 0) + 1
        suits[suit] = suits.get(suit, 0) + 1
    
    # Check for a flush
    flush = False
    for suit in suits:
        if suits[suit] >= 5:
            flush = True
            flush_suit = suit
            break
    
    # Check for a straight
    straight = False
    for rank in ranks:
        if ranks.get(rank) and ranks.get(chr(ord(rank)+1)) and ranks.get(chr(ord(rank)+2)) and ranks.get(chr(ord(rank)+3)) and ranks.get(chr(ord(rank)+4)):
            straight = True
            straight_rank = rank
            break
        elif ranks.get('A') and ranks.get('2') and ranks.get('3') and ranks.get('4') and ranks.get('5'):
            straight = True
            straight_rank = '5'
            break
    
    # Check for a straight flush
    straight_flush = False
    if flush and straight:
        straight_flush_cards = [card for card in cards if card[1] == flush_suit and (card[0] == straight_rank or card[0] in 'TJQKA')]
        if len(straight_flush_cards) >= 5:
            straight_flush = True
    
    # Check for four of a kind
    four_of_a_kind = False
    four_of_a_kind_rank = None
    for rank in ranks:
        if ranks[rank] == 4:
            four_of_a_kind = True
            four_of_a_kind_rank = rank
            break
    
    # Check for full house
    full_house = False
    full_house_rank1 = None
    full_house_rank2 = None
    for rank in ranks:
        if ranks[rank] == 3:
            full_house_rank1 = rank
            for rank2 in ranks:
                if rank2 != rank and ranks[rank2] >= 2:
                    full_house = True
                    full_house_rank2 = rank2
                    break
            if full_house:
                break
    
    # Check for three of a kind
    three_of_a_kind = False
    three_of_a_kind_rank = None
    for rank in ranks:
        if ranks[rank] == 3:
            three_of_a_kind = True
            three_of_a_kind_rank = rank
            break
    
    # Check for two pairs
    two_pairs = False
    pair_ranks = []
    for rank in ranks:
        if ranks[rank] == 2:
            pair_ranks.append(rank)
    if len(pair_ranks) >= 2:
        two_pairs = True
    
    # Check for one pair
    one_pair = False
    one_pair_rank = None
    for rank in ranks:
        if ranks[rank] == 2:
            one_pair = True
            one_pair_rank = rank
            break
    
    # Determine the best hand
    if straight_flush:
        return 90
    elif four_of_a_kind:
        return 80
    elif full_house:
        return 70
    elif flush:
        return 60
    elif straight:
        return 50
    elif three_of_a_kind:
        return 40
    elif two_pairs:
        return 30
    elif one_pair:
        return 20
    else:
        # If the player has no pair or better, return the highest card
        return 10
    
def determine_computer_player():
    global players_hand, community_hand
    """
    This function checks the given player's hand and the community cards
    to determine the best possible poker hand.
    """
    # Concatenate the player's and community cards
    cards = players_hand + community_hand
    
    # Count the frequency of each rank and suit
    ranks = {}
    suits = {}
    for card in cards:
        rank, suit = card[0], card[1]
        ranks[rank] = ranks.get(rank, 0) + 1
        suits[suit] = suits.get(suit, 0) + 1
    
    # Check for a flush
    flush = False
    for suit in suits:
        if suits[suit] >= 5:
            flush = True
            flush_suit = suit
            break
    
    # Check for a straight
    straight = False
    for rank in ranks:
        if ranks.get(rank) and ranks.get(chr(ord(rank)+1)) and ranks.get(chr(ord(rank)+2)) and ranks.get(chr(ord(rank)+3)) and ranks.get(chr(ord(rank)+4)):
            straight = True
            straight_rank = rank
            break
        elif ranks.get('A') and ranks.get('2') and ranks.get('3') and ranks.get('4') and ranks.get('5'):
            straight = True
            straight_rank = '5'
            break
    
    # Check for a straight flush
    straight_flush = False
    if flush and straight:
        straight_flush_cards = [card for card in cards if card[1] == flush_suit and (card[0] == straight_rank or card[0] in 'TJQKA')]
        if len(straight_flush_cards) >= 5:
            straight_flush = True
    
    # Check for four of a kind
    four_of_a_kind = False
    four_of_a_kind_rank = None
    for rank in ranks:
        if ranks[rank] == 4:
            four_of_a_kind = True
            four_of_a_kind_rank = rank
            break
    
    # Check for full house
    full_house = False
    full_house_rank1 = None
    full_house_rank2 = None
    for rank in ranks:
        if ranks[rank] == 3:
            full_house_rank1 = rank
            for rank2 in ranks:
                if rank2 != rank and ranks[rank2] >= 2:
                    full_house = True
                    full_house_rank2 = rank2
                    break
            if full_house:
                break
    
    # Check for three of a kind
    three_of_a_kind = False
    three_of_a_kind_rank = None
    for rank in ranks:
        if ranks[rank] == 3:
            three_of_a_kind = True
            three_of_a_kind_rank = rank
            break
    
    # Check for two pairs
    two_pairs = False
    pair_ranks = []
    for rank in ranks:
        if ranks[rank] == 2:
            pair_ranks.append(rank)
    if len(pair_ranks) >= 2:
        two_pairs = True
    
    # Check for one pair
    one_pair = False
    one_pair_rank = None
    for rank in ranks:
        if ranks[rank] == 2:
            one_pair = True
            one_pair_rank = rank
            break
    
    # Determine the best hand
    if straight_flush:
        return 90
    elif four_of_a_kind:
        return 80
    elif full_house:
        return 70
    elif flush:
        return 60
    elif straight:
        return 50
    elif three_of_a_kind:
        return 40
    elif two_pairs:
        return 30
    elif one_pair:
        return 20
    else:
        # If the player has no pair or better, return the highest card
        return 10

# Betting and Probabilities 
# Player Betting --> WinRate --> Calling/Folding
# Bank, and Account Checking

def computer_decision(x):
    global current_bet,dealer_money, pot
    
    i = determine_computer()
    if i < 10:
        # Fold
        print("The dealer folds. ")
    elif i >= 10:
        # Calls 
        dealer_money -= x
        pot += x
        print(f"The dealer calls. The pot now has ${pot}.")  
    elif i >= 50:
        # Raise
        bet_raise = random.randint(0,dealer_money)
        y = bet_raise + x
        pot += y
        current_bet += bet_raise
        print(f"The dealer raises by ${bet_raise}. The pot now has ${pot}. ")
        player_betting()
        pass

def player_betting():
    global current_bet,player_money,current_bet,pot
    
    if current_bet == 0:
        response = input("Would you like to place a bet? (yes/no) ").lower()
        if response in ["yes", "y"]:
            bet = int(input(f"How much would you like to bet? (You have ${player_money}) "))
            if bet < 1:
                print("The minimum bet is $1.")
                player_betting()
            elif bet > player_money:
                print("You do not have enough money to place that bet.")
                player_betting()
            else:
                current_bet = bet
                player_money -= bet
                pot += bet
                print(f"You have placed a bet of ${bet}.")
                computer_decision(bet)
                
                return True
    else:
        response = input(f"The current bet is ${current_bet} and the pot is ${pot}. Would you like to pass, raise, or fold? ").lower()
        if response == "pass":
            return True
        elif response == "raise":
            new_bet = int(input(f"How much would you like to raise the bet to? (You have ${player_money}) "))
            if new_bet < current_bet:
                print("You cannot raise the bet by less than the current bet.")
                player_betting()
            elif new_bet > (current_bet + player_money):
                print("You do not have enough money to raise that much.")
                player_betting()
            elif new_bet <= (current_bet + player_money) and new_bet > current_bet:
                i = new_bet - current_bet
                pot += i
                player_money -= i
                current_bet = new_bet 
                print(f"You have raised the bet to ${current_bet} and the pot to ${pot}.")
                computer_decision(i)
                return True
            elif new_bet == current_bet:
                print("You cannot raise to the same bet. ")
                player_betting()
        elif response == "fold":
            print("You have folded.")
            return False
        else:
            print("Invalid response.")
            player_betting()

def game_outcome():
    global player_money,dealer_money,current_bet
    
    if determine_computer() > determine_computer_player():
        print("The dealer wins!")
        dealer_money += current_bet
        player_money -= current_bet
        current_bet = 0
        if choice() == True:
            playing_game()
        elif choice() == False:
            pass
    elif determine_computer() < determine_computer_player():
        print("The player wins!")
        dealer_money -= current_bet
        players_money += current_bet
        current_bet = 0
        if choice() == True:
            playing_game()
        elif choice() == False:
            pass
    elif determine_computer() == determine_computer_player():
        pass
    else:
        print("Game error. ")

def deal_cards():
    global players_hand,dealers_hand,community_hand
    players_hand.append(deck.pop())
    dealers_hand.append(deck.pop())
    community_hand.append(deck.pop())

def reset_game():
    global player_money,players_hand,dealer_money,dealers_hand,current_bet, community_hand, deck, pot

    player_money = 100
    players_hand = []
    dealer_money = 100
    pot = 0
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
    
    # The Flop: First three cards shuffled and game dealt. 
    random.shuffle(deck)
    print("Welcome to Texas Holdem. You be playing against the dealer to start please look at you cards and place a bet. ")
    for i in range(2):
        deal_cards()
    community_hand.append(deck.pop())
    print(f"The flop now contains {community_hand}.\nYour hand now contains {players_hand}. ")
    print(f"The calculated hand you have at this point is, {determine_player()}. ")
    j = player_betting()
    i = pot

    if pot > 0 and j == True:
        # The Turn. 
        community_hand.append(deck.pop())
        print(f"The flop now contains {community_hand}.\nYour hand now contains {players_hand}. ")
        print(f"The calculated hand you have at this point is, {determine_player()}. ")
        k = player_betting()
        
        # The River.
        if pot > i and k == True:
            community_hand.append(deck.pop())
            print(f"The flop now contains {community_hand}.\nYour hand now contains {players_hand}. ")
            print(f"The calculated hand you have at this point is, {determine_player()}. ")
            player_betting()
            game_outcome()
        else:
            reset_game()
            print("You folded! ")
            game_outcome()
    
    else:
        reset_game()
        print("You folded! ")
        game_outcome()