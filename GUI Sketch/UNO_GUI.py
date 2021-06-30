import UNO_config as uno
from tkinter import *
from PIL import ImageTk, Image

wnd = Tk()
#wnd.geometry("600x400")
wnd.title('UNO')
#wnd.geometry("600x400")
wnd.iconbitmap('D:/UR6523011/Sem 2/VGT123 Technology System Programming II/GitHub/Virtual-GUI-Game/GUI Sketch/image/uno_icon.ico')

detailFrame = Label(wnd, bg = "lavender")

gameFrame = Label(wnd, bg = 'blue')

unoDeck = uno.buildDeck()
#print(unoDeck)

def onClick(tPlyrEntry, lblNote):
    global detailFrame, gameFrame, unoDeck

    try:
        if int(tPlyrEntry.get()) < 2 or int(tPlyrEntry.get()) > 4:
            lblNote.config(text = 'Invalid!')
        else:
            lblNote.config(text = 'OK!!')
            unoDeck = uno.shuffleDeck(unoDeck, int(tPlyrEntry.get()))
            print(unoDeck)
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
def page1():
    #global detailFrame, btnPlay, tPlyrEntry, PlyrNmEntry
    detailFrame.pack()
    
    Label(detailFrame, padx = 270, bg = "lavender").grid(row = 0, column = 0, columnspan = 5)
    btnPlay = Button(detailFrame, text = 'PLAY', padx = 40, pady = 10, command = lambda: onClick(tPlyrEntry, lblNote), fg = 'WHITE', bg = "DODGERBLUE")
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