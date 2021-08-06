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
#Haziq Github file location
GUI_location = 'D:/UR6523011/Sem 2/VGT123 Technology System Programming II/GitHub/Virtual-GUI-Game'
#Danish Github file location
#GUI_location = 'C:/Users/danis/OneDrive/Desktop/VGT 123/GitHub/Virtual-GUI-Game'
#Aiman Github file location
#GUI_location = 'C:/Users/user/Desktop/GitHub/Virtual-GUI-Game'

card_image_location = '/image/Uno Card'

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
winner_pic = []

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
    
def champion (window):
    root = Toplevel(window)
    root.overrideredirect(1)
    
    #GUI_location = 'C:/Users/danis/OneDrive/Desktop/UNO_GUI'
    #card_image_location = '/img'
    winner_pic.clear()
    
    currentProgress = UC.winningPosition(playerName, players, totalPlayer)
    name_pos_db = currentProgress[0]
    card_pos_db = currentProgress[1]
    
    player = sqlite3.connect('winningPos.db')
    c = player.cursor()
    
    if totalPlayer == 2:
        for x in range(2):
            name_pos_db.append('None')
            card_pos_db.append([])
    elif totalPlayer == 3:
        name_pos_db.append('None')
        card_pos_db.append([])
        
    c.execute("INSERT INTO winning VALUES (:first_place_name, :first_place_Totalcard, :second_place_name, :second_place_Totalcard, :third_place_name, :third_place_Totalcard, :fourth_place_name, :fourth_place_Totalcard)",
            {
                'first_place_name': name_pos_db [0],
                'first_place_Totalcard': len(card_pos_db [0]),
                'second_place_name': name_pos_db [1],
                'second_place_Totalcard': len(card_pos_db [1]),
                'third_place_name': name_pos_db [2],
                'third_place_Totalcard': len(card_pos_db [2]),
                'fourth_place_name': name_pos_db [3],
                'fourth_place_Totalcard': len(card_pos_db [3])
            })
    player.commit()
    player.close()

    open_pic = Image.open(f'{GUI_location}/Image/crown.png')
    resized = open_pic.resize((80, 60), Image.ANTIALIAS)
    updated_card_pic = ImageTk.PhotoImage(resized)
    winner_pic.append(updated_card_pic)

    open_pic = Image.open(f'{GUI_location}/Image/trophy.png')
    resized = open_pic.resize((150, 200), Image.ANTIALIAS)
    updated_card_pic = ImageTk.PhotoImage(resized)
    winner_pic.append(updated_card_pic)

    fStframe = Frame(root, bg = "red4")
    fStframe.pack()

    blank = Label(fStframe, text = " ",bg = "red4")
    blank.grid(padx = 5)

    congratulation = Label(fStframe,text = 'CONGRATULATION !!',padx = 40, pady = 10, bg = "red4",fg = "white", font = "helvetica")
    congratulation.grid(padx = 150)

    winner = Label(fStframe, text = "THE WINNER IS", bg = "red4",fg = "white", font = "helvetica")
    winner.grid(pady = 5)

    Label(fStframe, image = winner_pic[0], bg = 'red4').grid(pady = 10,sticky = S)

    name = Label(fStframe, text = f"Player Name : {name_pos_db[0]} ", bg = "red4",fg = "white", font = "helvetica")
    name.grid(pady = 10)
    
    Label(fStframe, image = winner_pic[1], bg = 'red4').grid(pady = 5,sticky = S)
    
    participant = Label(fStframe, text = f"2nd Place Is Player\n {name_pos_db[1]}", bg = 'red4', fg = 'white', font = "helvetica")
    participant.grid(padx = 50, pady = 10)


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
            players.append(UC.drawnCards(unoDeck, 5))
        for x in range(totalPlayer):
            
            pile_card = UC.initializeCard(pile_card, unoDeck)
        
        gameFrame.destroy()
        main_page_part_3()


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


def jump_page():
    global gameFrame, playerHand
    gameFrame.destroy()
    playerHand.destroy()
    main_page_part_3()

def check_position():
    global playerTurn
    if playerTurn >= totalPlayer:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = totalPlayer - 1


def pick_card(event):
    global clicked, putCard, playerPassCard, players, playerTurn, colors, holdWild

    def sizing_image(location):
        # Open Card Image
        open_pic = Image.open(f'{GUI_location}{card_image_location}/{location}.png')
        # Resized the Image
        resized = open_pic.resize((54, 84), Image.ANTIALIAS)
        # Updated Card Image size
        updated_card_pic = ImageTk.PhotoImage(resized)
        open_pic = updated_card_pic
        return open_pic

    if clicked.get() == 'Choose Card':
        playerPassCard = sizing_image('Pass')
    else:
        playerPassCard = sizing_image(clicked.get())
    putCard['image'] = playerPassCard


def pick_color(color):
    global clicked, pile_card, playerTurn, colorState, holdWild, currentCard, checkUpdated, playerDirection

    if colorState == 1:
        currentCard = clicked.get()

        print(currentCard)
        if currentCard != 'Choose Card':
            print(f'Player {playerTurn + 1} is change card color to = {currentCard}')
            if checkUpdated == 3:
                playerTurn += playerDirection
                check_position()
                colorState = 0
            elif checkUpdated == 2:
                playerTurn += playerDirection
                check_position()
                players[playerTurn] += UC.drawnCards(unoDeck, 4)
                playerTurn += playerDirection
                colorState = 0
            elif checkUpdated == 4:  
                # Skip
                print('Skip is selected')
                playerTurn += playerDirection
                check_position()
                playerTurn += playerDirection
            elif checkUpdated == 5:
                # Reverse
                print('Reverse is selected')
                playerDirection *= -1
                playerTurn += playerDirection
            elif checkUpdated == 6:
                # Draw Two
                print('Draw Two is selected')
                playerTurn += playerDirection
                check_position()
                players[playerTurn] += UC.drawnCards(unoDeck, 2)
                playerTurn += playerDirection
            elif checkUpdated == 7:
                # Color or value are same
                print('Color or value is selected')
                playerTurn += playerDirection
                
            check_position()
            holdWild = 1

            checkUpdated = 0
            jump_page()


def pass_card(players):
    global clicked, pile_card, playerTurn, playerDirection, colorState, currentCard, checkUpdated, holdWild, victory

    if holdWild == 1:
        print(currentCard)
        currentProgress =  UC.checkColor(clicked.get(), players[playerTurn], checkUpdated, pile_card, unoDeck, currentCard)
        checkUpdated = currentProgress[0]
        holdWild = currentProgress[2]
        victory = currentProgress[3]

        print(f'Current Hold card b = {currentProgress[1]}')
        if checkUpdated != 0:
            #check_position()
            if checkUpdated == 1:
                # Pass
                print('Pass is selected')
                playerTurn += playerDirection
            elif checkUpdated == 2:
                # Wild Draw Four
                print('Wild Draw Four is selected')
                player_hand()
            elif checkUpdated == 3:
                # Wild
                print('Wild is selected')
                player_hand()
            elif checkUpdated == 4:  
                # Skip
                print('Skip is selected')
                playerTurn += playerDirection
                check_position()
                playerTurn += playerDirection
            elif checkUpdated == 5:
                # Reverse
                print('Reverse is selected')
                playerDirection *= -1
                playerTurn += playerDirection
                holdWild = 0
            elif checkUpdated == 6:
                # Draw Two
                print('Draw Two is selected')
                playerTurn += playerDirection
                check_position()
                players[playerTurn] += UC.drawnCards(unoDeck, 2)
                playerTurn += playerDirection
                holdWild = 0
            elif checkUpdated == 7:
                # Color or value are same
                print('Color or value is selected')
                playerTurn += playerDirection
                checkUpdated = 0
                holdWild = 0
            check_position()
            jump_page()

    elif holdWild == 0:
        currentProgress =  UC.checkCard(clicked.get(), players[playerTurn], checkUpdated, pile_card, unoDeck)
        checkUpdated = currentProgress[0]
        victory = currentProgress[2]

        print(f'Current Hold card a = {currentProgress[1]}')
        if checkUpdated != 0:
            #check_position()
            if checkUpdated == 1:
                # Pass
                print('Pass is selected')
                playerTurn += playerDirection
            elif checkUpdated == 2:
                # Wild Draw Four
                print('Wild Draw Four is selected')
                holdWild = 1
                colorState = 1
                player_hand()
            elif checkUpdated == 3:
                # Wild
                print('Wild is selected')
                holdWild = 1
                colorState = 1
                player_hand()
            elif checkUpdated == 4:
                # Skip
                print('Skip is selected')
                playerTurn += playerDirection
                check_position()
                playerTurn += playerDirection
            elif checkUpdated == 5:
                # Reverse
                print('Reverse is selected')
                playerDirection *= -1
                playerTurn += playerDirection
            elif checkUpdated == 6:
                # Draw Two
                print('Draw Two is selected')
                playerTurn += playerDirection
                check_position()
                players[playerTurn] += UC.drawnCards(unoDeck, 2)
                playerTurn += playerDirection
            elif checkUpdated == 7:
                # Color or value are same
                print('Color or value is selected')
                playerTurn += playerDirection
                checkUpdated = 0
            check_position()
            jump_page()

def passwordEntry(playerName, password):
    correct = 0

    wnd = Toplevel()
    wnd.title('UNO')
    wnd.resizable(width = False, height = False)
    wnd.configure(background = 'white')
    wnd.iconbitmap(f'{GUI_location}/Image/uno_icon.ico')

    def main_Frame():
        wnd.title('UNO')
        wnd.resizable(width = False, height = False)
        wnd.configure(background = 'white')
        wnd.iconbitmap(f'{GUI_location}/Image/uno_icon.ico')
    
    def ID (event):
        global correct
        def succeed():
            player_hand()
            wnd.destroy()
        if entry2.get() == password:
            correct = 1
            succeed()
            return correct
        else:
            messagebox.showerror('UNO', 'Wrong username or password')
        
    def exit():
        sys.exit()

    label1 = Label(wnd, text = f'Username\n{playerName}')
    label2 = Label(wnd, text = 'Password')
    entry2 = Entry(wnd, show = '*')
    ext_But = Button(wnd, text = 'Cancel',command = wnd.destroy)

    entry2.bind('<Return>',ID)

    label1.grid(column = 2,row = 1,pady= 6, padx = 70)
    label2.grid(column = 2, row = 3,pady= 6, padx = 70)
    entry2.grid(column = 2, row = 4,pady= 6, padx = 70)
    ext_But.grid(column = 2, row = 5,pady= 6, padx = 70)
    
def login():
    global passwordWindow 
    
    msgBox = messagebox.askquestion('Player Turn', f'Are your player {playerTurn + 1}')
    if msgBox == 'yes':
       loginSuccess = passwordEntry(playerName[playerTurn], playerPassword[playerTurn])
       if loginSuccess == 1:
           gameFrame.destroy()       

            
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
    #playerHand.geometry('350x100')

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

        dropDown = OptionMenu(playerHand,  clicked, *options, command = pick_card)
        dropDown.grid(row = 2, column = 0, columnspan = 4)

        putCard = Button(playerHand, image = playerPassCard, command = lambda: pick_color(colors), borderwidth = 0)
        putCard.grid(row = 3, column = 0, columnspan = 4)

    else:
        cardColumnLimit = 5
        setCardRow = 1
        setCardColumn = 0

        options = ['Choose Card', 'Pass'] + players[playerTurn]

        clicked = StringVar()
        clicked.set(options[0])

        print(f'Player {playerTurn + 1} card is {players[playerTurn]}')

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
            open_pic = Image.open(f'{GUI_location}{card_image_location}/uno backside.png')
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