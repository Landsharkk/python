import random

suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:    
    for rank in ranks:
        #print(f'{rank} of {suit}')
        card = (rank + ' of ' + suit)
        deck.append(card)

#print('Deck: ' + str(deck)) #what's in the deck?

print(f'There are {len(deck)} cards in the deck.')

print('Dealing ...')

hand = random.choices(deck, k=5)

for card in hand:
    deck.remove(card)

#print(deck)
#print(hand)

print(f'There are {len(deck)} cards in the deck.')
print('Player has the following cards in their hand: ')
print(hand)

