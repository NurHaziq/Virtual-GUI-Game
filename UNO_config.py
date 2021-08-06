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


"""
Check card in player hand to put in pile card during wild card
***************************************************************
Parameters      ||  currentCard --> string
                ||  playerHand  --> list
                ||  updated     --> integer
                ||  pileCard    --> list
                ||  unoDeck     --> list
                ||  cardColor   --> string
***************************************************************
Return Value    ||  updated         --> integer
                ||  checkSplitCard  --> string
                ||  Nabil           --> integer
                ||  winner          --> integer
"""
def checkColor(currentCard, playerHand, updated, pileCard, unoDeck, cardColor):

    Nabil = 1
    updated = 0
    winner = 0

    splitCard = currentCard.split(' ', 1)
    checkSplitCard = currentCard
    if currentCard == 'Pass':
        playerHand.extend(drawnCards(unoDeck, 1))
        updated = 1
    elif currentCard == 'Choose Card':
        print('Are you idiot')
    else:
        if splitCard[0] in cardColor:
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
                Nabil = 0
    return updated, checkSplitCard, Nabil, winner


"""
Rechange the positon for winner according to their  total card
***************************************************************
Parameters      ||  playerName  --> list
                ||  playerCard  --> list
                ||  totalPlayer --> integer
***************************************************************
Return Value    ||  rechangeNamePos --> integer
                ||  rechangeCardPos --> string
"""
def winningPosition(playerName, playerCard, totalPlayer):

    name = playerName
    card = playerCard
    
    rechangeNamePos = []
    rechangeCardPos = []

    save = 0
    pos = 0

    def rechage_the_pos(save):
        for x in range(len(card)):
            if save > len(card[x]):
                save = len(card[x])
                pos = x
        return pos

    def go_to_this():
        for x in range(totalPlayer):
            save = refData
            pos = rechage_the_pos(save)
            rechangeCardPos.append(card.pop(card.index(card[pos])))
            rechangeNamePos.append(name.pop(name.index(name[pos])))
            
    for x in range(totalPlayer):
        if save < len(card[x]):
            save = len(card[x])

    refData = save + 1

    for x in range(totalPlayer):
        print(f'Player{x + 1} Name = {name[x]}')
        print(f'Player{x + 1} Card ={card[x]}')

    print('*' * 30)
    print('After Change the position')
    print('*' * 30)

    go_to_this()

    for x in range(totalPlayer):
        if x == 0:
            print(f'{x + 1}st Place = {rechangeNamePos[x]}')
        elif x == 1:
            print(f'{x + 1}nd Place = {rechangeNamePos[x]}')
        elif x == 2:
            print(f'{x + 1}rd Place = {rechangeNamePos[x]}')
        elif x == 3:
            print(f'{x + 1}th Place = {rechangeNamePos[x]}')
        print(f'Total Card ({len(rechangeCardPos[x])}) = {rechangeCardPos[x]}')
    
    return rechangeNamePos, rechangeCardPos