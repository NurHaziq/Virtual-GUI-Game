
"""
Genarate UNO deck for 108 cards.
Parameter       --->    None
Return value    --->    list
"""
def buildDeck():
    deck = []
    # Example Card  ---> Green 3, Yellow 5, Red Reverse
    colors = ['Red', 'Blue', 'Yellow', 'Green']
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Draw Two', 'Skip', 'Reverse']
    wilds = ['Wild', 'Wild Draw Four']
    
    # Define every color in deck
    for color in colors:
        # Make copy every color
        for value in values:
            initCard = f'{color} {value}'
            deck.append(initCard)

            # Duplicate every card in values except 0
            if value != 0:
                deck.append(initCard)

    # Make copy wild card 4
    for i in range (4):
        deck.append(wilds[0])
        deck.append(wilds[1])

    #print(deck)

    return deck

"""
shuffle all card in deck
"""

"""
assign player
"""
"""
change player position
"""

"""
giving card to all player
"""

"""
open one card from deck to start the game 
"""

"""
play according follow the rule

"""

"""
make GUI
"""
unoDeck = buildDeck()