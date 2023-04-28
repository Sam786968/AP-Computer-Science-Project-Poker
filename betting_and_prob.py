
# Function
 # Determine the type of hand
def determine_hand(player_hand, community_cards):
    all_cards = player_hand + community_cards
    
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


