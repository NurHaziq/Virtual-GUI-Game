from tkinter import *
import UNO_config as UC
import sys
import guideNote as GN
import sqlite3
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.title('UNO')
window.resizable(width = False, height = False)

# Change it to the direction path in ur computer
GUI_location = 'D:/UR6523011/Sem 2/VGT123 Technology System Programming II/GitHub/Virtual-GUI-Game'
card_image_location = '/image/Uno Card'
"""
card_image_location = '/img/Uno Card'
GUI_location = 'C:/Users/danis/OneDrive/Desktop/UNO_GUI'
"""
"""
card_image_location = '/image/Uno Card'
GUI_location = 'C:/Users/user/Desktop/GitHub/Virtual-GUI-Game'
"""

window.iconbitmap(f'{GUI_location}/GUI Sketch/image/uno_icon.ico')

detailFrame1 = Label(window, bg = 'skyblue2')
detailFrame2 = Label(window, bg = 'skyblue2')

gameFrame = Label(window,  bg = 'skyblue1')

totalPlayer = None

'''
Naming for each individual player is stored in playerName
Total card for each individual player is store in players
'''
playerName = ['', '', '', '']
players = []

playerNameEntry = []
playerPassword = []
playerPasswordEntry = []

card_pic = []

pile_card = []
PlayerCurrentCard = []
playerPassCard = None
playerPutCard = []

clicked = None
putCard = None
colorState = 0
checkUpdated = 0
victory = 0

passwordWindow = Label(window)
guideInfo = Label(window)
playerHand = Label(window)
view_rank = Label(window)

playerTurn = 0
playerDirection = 1

unoDeck = UC.buildDeck()
unoDeck = UC.shuffleDeck(unoDeck, 3)

colors = ['Red', 'Blue', 'Yellow', 'Green']
currentCard = None
holdWild = 0


def guideClicked():
    global guideInfo
    guideInfo = GN.rule(window, guideInfo)
    
def rankView():
    global view_rank
    
    view_rank.destroy()
    
    view_rank = Toplevel(window)
    view_rank.title('Ranking View')
        
    players = sqlite3.connect('winningPos.db')
    c = players.cursor()
    c.execute("SELECT*, oid FROM winning ")
    ranked = c.fetchall()

    print(ranked)
    print(len(ranked))

    count = 1
    Label(view_rank, text = f'Total Game Played ({len(ranked)})').grid(row = 0, column = 1, columnspan = len(ranked))
    Label(view_rank, text = 'Win Streak').grid(row = 0, column = len(ranked) + 1)
    Label(view_rank, text = '1st Place').grid(row = 1, column = 0)
    Label(view_rank, text = 'Card Balance').grid(row = 2, column = 0)
    Label(view_rank, text = '2nd Place').grid(row = 3, column = 0)
    Label(view_rank, text = 'Card Balance').grid(row = 4, column = 0)
    Label(view_rank, text = '3rd Place').grid(row = 5, column = 0)
    Label(view_rank, text = 'Card Balance').grid(row = 6, column = 0)
    Label(view_rank, text = '4th Place').grid(row = 7, column = 0)
    Label(view_rank, text = 'Card Balance').grid(row = 8, column = 0)

    for rank in ranked:
        for x in range(8):
            if x == 0:
                rank[x]
            Label(view_rank, text = rank[x]).grid(row = x + 1, column = count)
        count += 1
    
    current = ''
    count_streak = 0

    def go_to_this(current, count_streak):
        for rank in ranked:
            save = rank[0]
            for x in range(1):
                if current == save:
                    current = save
                    count_streak += 1
                elif current != save:
                    current = save
                    count_streak = 0
        return current, count_streak

    winStreak = go_to_this(current, count_streak)
    print(winStreak)
    
    Label(view_rank, text = f'{winStreak[0]}\n{winStreak[1]}').grid(row = 1, column = len(ranked) + 1)

    players.commit()
    players.close()


'''
Button Play when it clicked
**************************************************
Parameter       ||  buttonPlay      --> state
**************************************************
Return value    ||  detailFrame2    --> Label
                ||  playerNameEntry --> list
                ||  playerName      --> list
                || totalPlayer      --> integer
'''
def playClick(buttonPlay):
    global detailFrame2, gameFrame, pile_card, unoDeck

    countName = 0
    countPassword = 0
    lockEntry = 0

    '''
    Define function for Changing Player Name
    **************************************************
    Parameter       ||  None
    **************************************************
    Return value    ||  detailFrame2    --> Label
    ''' 
    def proceed():
        msgBox = messagebox.askquestion('Player Naming', 'Do you want to change Player Name or Password ?')
        if msgBox == 'yes':
            lockEntry = 0
        else:
            lockEntry = 1
            buttonPlay['state'] = DISABLED

        return lockEntry
            
    '''
    Check last entry name and update the playerName List
    '''
    # Save the playerNameEntry into playerName list using for loop
    for x in range(totalPlayer):
        playerName[x] = playerNameEntry[x].get().title()
        playerPassword[x] = playerPasswordEntry[x].get()

    # Check if playerName list is not empty
    for x in playerName:
        if x != '':
            countName += 1
            
    for x in playerPassword:
        if x != '':
            countPassword += 1
            
    if countName == totalPlayer and countPassword == totalPlayer:
        lockEntry = proceed()
    
    # Destroy the detailFrame2
    detailFrame2.destroy()

    # Recreate detailFrame2
    detailFrame2 = Label(window, bg = 'skyblue2')
    detailFrame2.pack(fill = X)

    # clear playerNameEntry list
    playerNameEntry.clear()
    playerPasswordEntry.clear()

    '''
    If in playerName list had empty string it will show Invalid because Player shouldn't had empty name
    Then if it's has name and update the entry
    '''
    for x in range(totalPlayer):
        Label(detailFrame2, text = f'Player Name {x + 1}', bg = "skyblue2").grid(row = x, column = 0, pady = 5)
        Label(detailFrame2, text = ':' ,bg = "skyblue2").grid(row = x, column = 1, pady = 5)

        nameEntry = Entry(detailFrame2, width = 20)
        nameEntry.grid(row = x, column = 2, pady = 5)
        
        Label(detailFrame2, text = f'Password {x + 1}', bg = "skyblue2").grid(row = x, column = 3, pady = 5)
        Label(detailFrame2, text = ':', bg = "skyblue2").grid(row = x, column = 4, pady = 5)

        passwordEntry = Entry(detailFrame2, width = 20, show = "*")
        passwordEntry.grid(row = x, column = 5, pady = 5)

        if playerName[x] == '' or playerPassword[x] == '':
            Label(detailFrame2, text = 'Invalid!', fg = 'red', bg = "skyblue2").grid(row = x, column = 6)
            nameEntry.insert(0, playerName[x])
            passwordEntry.insert(0, playerPassword[x])
        
        elif playerName[x] != '' and playerPassword[x] != '':
            Label(detailFrame2, text = 'OK!', fg = 'green', bg = "skyblue2").grid(row = x, column = 6)

            nameEntry.insert(0, playerName[x])
            passwordEntry.insert(0, playerPassword[x])
            
            if lockEntry == 1:
                nameEntry['state'] = DISABLED
                passwordEntry['state'] = DISABLED
            
        playerNameEntry.append(nameEntry)
        playerPasswordEntry.append(passwordEntry)

    if lockEntry == 1:
        for player in range(totalPlayer):
            players.append(UC.drawnCards(unoDeck, 1))
        for x in range(totalPlayer):
            
            pile_card = UC.initializeCard(pile_card, unoDeck)


'''
Button OKAY when it clicked
*********************************************************
Parameter       ||  totalPlayerEntry    --> Entry
                ||  rangeLabelNote      --> Label
                ||  buttonPlay          --> state
                ||  okayButton          --> state
*********************************************************
Return value    ||  totalPlayer         --> integer
'''
def okayClick(totalPlayerEntry, rangeLabelNote, buttonPlay, okayButton):
    global totalPlayer
    try:
        if int(totalPlayerEntry.get()) < 2 or int(totalPlayerEntry.get()) > 4:
            rangeLabelNote.config(text = 'Invalid!', fg = 'red')
            
        else:
            totalPlayer = int(totalPlayerEntry.get())

            buttonPlay['state'] = NORMAL
            totalPlayerEntry['state'] = DISABLED
            okayButton['state'] = DISABLED
            rangeLabelNote.config(text = 'OK!!', fg = 'green')

            main_page_part_2()

    except ValueError:
        rangeLabelNote.config(text = 'Invalid!', fg = 'red')


"""
Check card in player hand to put in pile card during wild card
***************************************************************
Parameters      ||  None
***************************************************************
Return Value    ||  playerTurn      --> integer
                ||  playerHand      --> Label
                ||  totalPlayer     --> integer
                ||  players         --> list
                ||  PlayerCurrentCard   --> string
                ||  playerPassCard      --> string
                ||  gameFrame           --> Label
"""
def player_hand():
    global  playerTurn, playerHand, totalPlayer, players, PlayerCurrentCard, playerPassCard, \
            gameFrame, clicked, putCard

    playerHand.destroy()

    playerHand = Toplevel(window)
    playerHand.title(f'In Your Hand Player {playerTurn + 1}')
    playerHand.resizable(width = False, height = False)
    window.iconbitmap('C:/gui/UNO_icon.ico')
    

    gameFrame.destroy()
    main_page_part_3()

    PlayerCurrentCard.clear()

    """
    Resize the image to specific dimension
    ***************************************************************
    Parameters      ||  location --> string
    ***************************************************************
    Return Value    ||  updated_card_pic    --> ImageTk.PhotoImage
    """
    def sizing_image(location):
        # Open Card Image
        open_pic = Image.open(f'{GUI_location}{card_image_location}/{location}.png')
        # Resized the Image
        resized = open_pic.resize((54, 84), Image.ANTIALIAS)
        # Updated Card Image size
        updated_card_pic = ImageTk.PhotoImage(resized)
        return updated_card_pic

    playerPassCard = sizing_image('Pass')

    Label(playerHand, text = 'Your Card').grid(row = 0, column = 0, columnspan = len(players[playerTurn]))

    if colorState == 1:

        options = ['Choose Card'] + colors

        clicked = StringVar()
        clicked.set(options[0])

        for x in range(len(colors)):
            PlayerCurrentCard.append(sizing_image(colors[x]))

            Label(playerHand, image = PlayerCurrentCard[x]).grid(row = 1, column = x, padx = 5)

        dropDown = OptionMenu(playerHand,  clicked, *options)
        dropDown.grid(row = 2, column = 0, columnspan = 4)

        putCard = Button(playerHand, image = playerPassCard, borderwidth = 0)
        putCard.grid(row = 3, column = 0, columnspan = 4)

    else:
        cardColumnLimit = 5
        setCardRow = 1
        setCardColumn = 0

        options = ['Choose Card', 'Pass'] + players[playerTurn]

        clicked = StringVar()
        clicked.set(options[0])

        card_pos = 0
        for x in range(len(players[playerTurn])):
            PlayerCurrentCard.append(sizing_image(players[playerTurn][x]))

            # Change change row for card in player hand
            if x >= cardColumnLimit:
                cardColumnLimit += 5
                setCardRow += 1
                setCardColumn = 0

            Label(playerHand, image = PlayerCurrentCard[x]).grid(row = setCardRow, column = setCardColumn, padx = 5)
            
            setCardColumn += 1
        
        dropDown = OptionMenu(playerHand,  clicked, *options, command = pick_card)
        dropDown.grid(row = setCardRow + 1, column = 0, columnspan = 5)

        putCard = Button(playerHand, image = playerPassCard, command = lambda: pass_card(players), borderwidth = 0)
        putCard.grid(row = setCardRow + 2, column = 0, columnspan = 5)


'''
Define the main page for Frame 3
****************************************************
parameter       || None
****************************************************
return Value    ||  gameFrame   --> Label
                ||  unoDeck     --> list
                ||  card_pic    --> list
                ||  players     --> list
                ||  pile_card   --> list
'''
def main_page_part_3():
    global gameFrame, unoDeck, card_pic, players, pile_card, playerTurn, victory

    gameFrame = Label(window,  bg = 'skyblue1')
    gameFrame.pack(fill = X)

    for x in range(8):
       Grid.columnconfigure(gameFrame, x, weight = 1)
    current_row = 0

    """
    Function to show your card and store in in card_pic
    **************************************************
    Parameter       ||  None
    **************************************************
    Return value    ||  card_pic    --> list
    
    """
    def sizing_image():
        global card_pic
        card_pic.clear()
        for x in range(totalPlayer):
            # Open Card Image
            #open_pic = Image.open(f'{GUI_location}{card_image_location}/uno backside.png')
            open_pic = Image.open(f'{GUI_location}/img/Uno Card/uno backside.png')
            # Resized the Image
            resized = open_pic.resize((54, 84), Image.ANTIALIAS)
            if x == 0:
                # Open Card Image
                open_pic_1 = Image.open(f'{GUI_location}{card_image_location}/{pile_card[-1]}.png')
                # Resized the Image
                resized_1 = open_pic_1.resize((54, 84), Image.ANTIALIAS)
                # Updated Card Image size
                updated_card_pic_1 = ImageTk.PhotoImage(resized_1)
                card_pic.append(updated_card_pic_1)
                updated_card_pic = ImageTk.PhotoImage(resized)              
                card_pic.append(updated_card_pic)
            # Rotate the image
            resized = resized.rotate(angle = rotate[x], expand = True)
            # Updated Card Image size
            updated_card_pic = ImageTk.PhotoImage(resized)              
            card_pic.append(updated_card_pic)
            
            if x == 0:
                Label(gameFrame, image = card_pic[x], bg = 'skyblue1').grid(row = 2, column = 3, rowspan = 2, sticky = 'e')
                Label(gameFrame, image = card_pic[x + 1], bg = 'skyblue1').grid(row = 2, column = 4, rowspan = 2, sticky = 'w')
            Label(gameFrame, image = card_pic[x + 2], bg = 'skyblue1').grid(row = player_position[x][0], column = player_position[x][2], rowspan = 2, columnspan = 2, sticky = player_position[x][4])
            Label(gameFrame,text = f'Player {x + 1}: {playerName[x]}', bg = 'skyblue1').grid(row = player_position[x][0], column = player_position[x][3], sticky = player_position[x][5])
            Label(gameFrame,text = f'Total Card: {len(players[x])}',  bg = 'skyblue1').grid(row = player_position[x][1], column = player_position[x][3], sticky = player_position[x][6])

    if totalPlayer > 2:
        rotate = [180, 270, 90, 0]
        player_position = [[0, 1, 3, 5, 'ew', 'ws', 'wn'],  [2, 3, 1, 0, 'w', 'es', 'en'], [2, 3, 5, 7, 'e', 'ws', 'wn'], [4, 5, 3, 5, 'ew', 'ws', 'wn']]
    else:
        rotate = [180, 0]
        player_position = [[0, 1, 3, 5, 'ew', 'ws', 'wn'], [4, 5, 3, 5, 'ew', 'ws', 'wn']]
    sizing_image()

    if holdWild == 1:
        Label(gameFrame, text = f'Player {playerTurn + 1} Turn\nCurrent Card : {pile_card[-1]}\nColor : {currentCard}', bg = 'skyblue1').grid(row = 0,  column = 0, columnspan = 2)
    else:
        Label(gameFrame, text = f'Player {playerTurn + 1} Turn\nCurrent Card : {pile_card[-1]}', bg = 'skyblue1').grid(row = 0,  column = 0, columnspan = 2)

    quit_But = Button(gameFrame, text = "QUIT\nGAME", bg = "red", width = 8, height = 2, command = window.destroy)
    quit_But.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 10)

    if victory == 1:
        champion(window)
        view_But = Button(gameFrame, text = "SHOW YOUR\nCARD", bg = "blue4",fg = 'white', width = 10, height = 2, command = login, state = DISABLED)
    else:
        view_But = Button(gameFrame, text = "SHOW YOUR\nCARD", bg = "blue4",fg = 'white', width = 10, height = 2, command = login)
    view_But.grid(row = 6, column = 9, sticky = E, padx = 10, pady = 10)


'''
Define the main page for Frame 2
****************************************************
parameter       || None
****************************************************
return Value    ||  detailFrame2    --> Label
'''
def main_page_part_2():
    global detailFrame2
    detailFrame2 = Label(window, bg = 'skyblue2')
    detailFrame2.pack(fill = X)

    for x in range(totalPlayer):
        Label(detailFrame2, text = f'Player Name {x + 1}', bg = "skyblue2").grid(row = x, column = 0, pady = 5)
        Label(detailFrame2, text = ':', bg = "skyblue2").grid(row = x, column = 1, pady = 5)

        nameEntry = Entry(detailFrame2, width = 20)
        nameEntry.grid(row = x, column = 2, pady = 5)
        playerNameEntry.append(nameEntry)
        playerName.append('')
        
        Label(detailFrame2, text = f'Password {x + 1}', bg = "skyblue2").grid(row = x, column = 3, pady = 5)
        Label(detailFrame2, text = ':', bg = "skyblue2").grid(row = x, column = 4, pady = 5)

        passwordEntry = Entry(detailFrame2, width = 20, show = "*")
        passwordEntry.grid(row = x, column = 5, pady = 5)
        playerPasswordEntry.append(passwordEntry)
        playerPassword.append('')
        


'''
Define main page for Frame 1
**************************************
parameter       ||  None
**************************************
return value    ||  None
'''
def main_page_part_1():
    detailFrame1.pack(fill = X)

    buttonPlay = Button(detailFrame1, text = 'PLAY', padx = 40, pady = 10,
        fg = 'WHITE', bg = "blue4",command = lambda : playClick (buttonPlay), state = DISABLED)
    buttonPlay.grid(row = 0, column = 0, columnspan = 5, pady = (10, 30))

    totalPlayer = Label(detailFrame1, text = 'Total Player', bg = "skyblue2")
    totalPlayer.grid(row = 1, column = 0, padx = (20, 0))

    Label(detailFrame1, text = ':', bg = "skyblue2").grid(row = 1, column = 1)

    totalPlayerValue = StringVar

    totalPlayerEntry = Entry(detailFrame1, textvariable = totalPlayerValue, width = 40)
    totalPlayerEntry.grid(row = 1, column = 2)

    rangeLabel = Label(detailFrame1, text = '(Min 2. Max 4)', padx = 20,bg = "skyblue2")
    rangeLabel.grid(row = 1, column = 3)

    rangeLabelNote = Label(detailFrame1, text = '', padx = 30, bg = "skyblue2")
    rangeLabelNote.grid(row = 1, column = 4)

    okayButton = Button(detailFrame1, text = 'OK', padx = 5, pady = 3,command = lambda : okayClick(totalPlayerEntry, rangeLabelNote, buttonPlay, okayButton), fg = 'WHITE',  bg = "blue4")
    okayButton.grid(row = 2, column = 2, pady = 10)

    ruleButton = Button(detailFrame1, text = 'GUIDE', fg = 'WHITE',  bg = "blue4", command = guideClicked)
    ruleButton.grid(row = 0, column = 4)
    
    historyButton = Button(detailFrame1, text = 'HISTORY', fg = 'white', bg = 'blue4', command = rankView)
    historyButton.grid(row = 0, column = 0)

main_page_part_1()


window.mainloop()