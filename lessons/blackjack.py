import random

# create a deck of cards
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank, suit) for rank in ranks for suit in suits]

# assign point values to cards
card_values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

# initialize player's hand
player_hand = []

# deal two cards to the player
for i in range(2):
    card = random.choice(deck)
    player_hand.append(card)
    deck.remove(card)

# determine the dealer's up-card
dealer_up_card = random.choice(deck)
deck.remove(dealer_up_card)

# calculate the value of the player's hand
player_hand_value = sum(card_values[card[0]] for card in player_hand)

# determine the optimal play based on the dealer's up-card and the player's hand value
if dealer_up_card[0] == 'Ace':
    if player_hand_value in range(17, 22):
        print('Stand')
    elif player_hand_value in range(13, 17):
        print('Hit')
    elif player_hand_value == 12:
        if player_hand[0][0] not in ['Ace', '2', '3', '4', '5']:
            print('Hit')
        else:
            print('Stand')
    else:
        print('Hit')
else:
    if player_hand_value >= 17:
        print('Stand')
    elif player_hand_value in range(12, 17):
        if dealer_up_card[0] in ['2', '3', '4', '5', '6']:
            print('Stand')
        else:
            print('Hit')
    elif player_hand_value == 11:
        if dealer_up_card[0] == 'Ace':
            print('Hit')
        else:
            print('Double down')
    elif player_hand_value == 10:
        if dealer_up_card[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            print('Double down')
        else:
            print('Hit')
    elif player_hand_value == 9:
        if dealer_up_card[0] in ['3', '4', '5', '6']:
            print('Double down')
        else:
            print('Hit')
    else:
        print('Hit')
