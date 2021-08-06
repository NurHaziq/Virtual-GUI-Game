import random

"""
Genarate UNO deck for 108 cards.
Parameter       ||  None
Return value    ||  deck --> list
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
Shuffles the list of items
Parameters      ||  deck --> list
Return values   ||  deck --> list
"""
def shuffleDeck(deck, shuffleTime):

    # Shuffle deck according to shuffleTime
    for times in range(shuffleTime):

        # Change card position in deck
        for cardPos in range(len(deck)):
            randPos = random.randint(0, 107)
            deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]

        return deck

"""
Initialize playar to play
Parameters      ||  inPlayer --> user
                ||  unoDeck  --> user
Return values   ||  players  --> list
"""
def player(inPlayer, players, unoDeck):
    for player in range(inPlayer):
        players.append(drawnCards(5, unoDeck))
    return players

"""
Draw card off the top of the deck
Parameters      ||  numCards    --> integer
Return values   ||  drawnCard   --> list
"""
def drawnCards(numCards, unoDeck):
    cardDrawn = []
    for x in range(numCards):
        cardDrawn.append(unoDeck.pop(0))
    return cardDrawn

"""
Show card in player hand
Parameter       ||  players     --> intiger
                ||  playerHand  --> list  
Return value    ||  None
"""
def showHand(player, playerHand):
    print(f'Player {player + 1}')
    print('Your Hand')
    print('*' * 20)
    y = 0
    for card in playerHand:
        y += 1
        print(f'{y}) {card}')
    print('')

"""
Check whether a player is able to drawn a card
Parameters      ||  color       --> string
                ||  value       --> string
                ||  playerHand  --> list
Return Value    ||  boolean
"""
def canPlay(color, value, playerHand):
    for card in playerHand:
        if 'Wild' in card:
            return True
        elif color in card or value in card:
            return True
    return False


"""
Check card in player hand to put in pile card
***********************************************
Parameters      ||  currentCard --> string
                ||  playerHand  --> list
                ||  updated     --> integer
                ||  pileCard    --> list
                ||  unoDeck     --> list
***********************************************
Return Value    ||  updated         --> integer
                ||  checkSplitCard  --> string
                ||  winner          --> integer
"""
def checkCard(currentCard, playerHand, updated, pileCard, unoDeck):

    winner = 0
    splitCard = currentCard.split(' ', 1)
    checkSplitCard = currentCard
    if currentCard == 'Pass':
        playerHand.extend(drawnCards(unoDeck, 1))
        updated = 1
    elif currentCard == 'Choose Card':
        print('Are you idiot')
    else:
        if 'Wild' in currentCard:
            pileCard.append(playerHand.pop(playerHand.index(currentCard)))
            if len(playerHand) == 0:
                winner = 1
            else:
                if 'Draw Four' in currentCard:
                    updated = 2
                else:
                    updated = 3

        elif splitCard[0] in pileCard[-1] or splitCard[1] in pileCard[-1]:
            pileCard.append(playerHand.pop(playerHand.index(currentCard)))
            if len(playerHand) == 0:
                winner = 1
            if splitCard[1] == 'Skip':
                updated = 4
            elif splitCard[1] == 'Reverse':
                updated = 5
            elif splitCard[1] == 'Draw Two':
                updated = 6
            else:
                updated = 7
    return updated, checkSplitCard, winner