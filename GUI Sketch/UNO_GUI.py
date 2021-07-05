# call Uno Config into GUI
import UNO_config as uno
from tkinter import *
from PIL import ImageTk, Image

wnd = Tk()
#wnd.geometry("600x400")
wnd.title('UNO')
# file location for Haziq
#wnd.iconbitmap('D:/UR6523011/Sem 2/VGT123 Technology System Programming II/GitHub/Virtual-GUI-Game/GUI Sketch/image/uno_icon.ico')
# file location for Danish
wnd.iconbitmap('C:/gui/UNO_icon.ico')
detailFrame = Label(wnd, bg = "lavender")

gameFrame = Label(wnd, bg = 'blue')

unoDeck = uno.buildDeck()

players = []
#print(unoDeck)

def onClick(tPlyrEntry, lblNote, btnPlay):
    global detailFrame, gameFrame, unoDeck, players

    try:
        if int(tPlyrEntry.get()) < 2 or int(tPlyrEntry.get()) > 4:
            lblNote.config(text = 'Invalid!')
        else:
            gameFrame.pack()
            Label(gameFrame, padx = 270).grid(row = 0, column = 0, columnspan = 9)
            btnPlay.config(state = DISABLED)
            lblNote.config(text = 'OK!!')
            unoDeck = uno.shuffleDeck(unoDeck, int(tPlyrEntry.get()))
            #print(unoDeck)
            players = uno.player(int(tPlyrEntry.get()), players, unoDeck)
            #print(players)
            gameFrame.pack()
            cardOnTop = Label(gameFrame, text = 'Card on top of discard pile: ')
            cardOnTop.grid(row = 0, column = 0, columnspan = 9)
            page2()
    except ValueError:
        lblNote.config(text = 'Invalid!')
    """
    gameFrame.pack()
    valEntry = tPlyrEntry.get()
    if valEntry == '2' or valEntry == '3' or valEntry == '4':
        btnPlay = Button(detailFrame, text = 'PLAY', padx = 40, pady = 10, command = onClick, fg = 'WHITE', bg = "DODGERBLUE", state = DISABLED)
        btnPlay.grid(row = 0, column = 0, columnspan = 5, pady = (10, 30))

        Label(gameFrame, padx = 270).grid(row = 0, column = 0, columnspan = 9)
    else:
        Label(gameFrame, text = 'Wrong Input', padx = 270).grid(row = 0, column = 0, columnspan = 9)
    """
def page2():
    global players
    wnd2 = Toplevel(wnd)
    #wnd2.geometry("300x100")
    wnd2.title('Your Hand')

    hndFrame = Label(wnd2, bg = 'skyblue')
    hndFrame.pack()

    Label(hndFrame, padx = 100, bg = "skyblue").grid(row = 0, column = 0)
    Label(hndFrame, text = f'your card is').grid(row = 0, column = 0)
    y = 0
    for player in players[0]:
        y += 1
        Label(hndFrame, text = f'{y}) {player}').grid(padx = (20, 0), row = y, column = 0, sticky = W)        
        
def page1():
    #global detailFrame, btnPlay, tPlyrEntry, PlyrNmEntry
    detailFrame.pack()
    
    Label(detailFrame, padx = 270, bg = "lavender").grid(row = 0, column = 0, columnspan = 5)
    btnPlay = Button(detailFrame, text = 'PLAY', padx = 40, pady = 10, command = lambda: onClick(tPlyrEntry, lblNote, btnPlay), fg = 'WHITE', bg = "DODGERBLUE")
    btnPlay.grid(row = 0, column = 0, columnspan = 5, pady = (10, 30))

    tPlyr = Label(detailFrame, text = 'Total Player')#, bg = "lavender")
    PlyrNm = Label(detailFrame, text = 'Player Name')#, bg = "lavender")

    tPlyr.grid(row = 1, column = 0, padx = (20, 0))
    PlyrNm.grid(row = 2, column = 0, padx = (20, 0))

    for x in range(2):
        myLbl = Label(detailFrame, text = ':').grid(row = x + 1, column = 1)

    tPlyrVal = StringVar
    PlyrNmVal = StringVar

    tPlyrEntry = Entry(detailFrame, textvariable = tPlyrVal, width = 40)
    PlyrNmEntry = Entry(detailFrame, textvariable = PlyrNmVal, width = 40)

    tPlyrEntry.grid(row = 1, column = 2)
    PlyrNmEntry.grid(row = 2, column = 2)

    rngLbl = Label(detailFrame, text = '(Min 2. Max 4)', padx = 20)#,bg = "lavender")
    rngLbl.grid(row = 1, column = 3)

    lblNote = Label(detailFrame, text = '', padx = 30)#, bg = "lavender")
    lblNote.grid(row = 1, column = 4)

page1()

wnd.mainloop()