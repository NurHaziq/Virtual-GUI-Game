from tkinter import *
from PIL import ImageTk, Image

wnd = Tk()
wnd.geometry("600x400")
wnd.title('UNO')
wnd.iconbitmap('C:/gui/UNO_icon.ico')

detailFrame = Label(wnd, bg = "lavender")
detailFrame.pack()

def onClick():
    global detailFrame
    detailFrame.pack_forget()

btnPlay = Button(detailFrame, text = 'PLAY', padx = 40, pady = 10, command = onClick, fg = 'WHITE', bg = "DODGERBLUE")
btnPlay.grid(row = 0, column = 0, columnspan = 5, pady = (10, 30))

tPlyr = Label(detailFrame, text = 'Total Player')#, bg = "lavender")
PlyrNm = Label(detailFrame, text = 'Player Name')#, bg = "lavender")

tPlyr.grid(row = 1, column = 0)
PlyrNm.grid(row = 2, column = 0)

for x in range(2):
    myLbl = Label(detailFrame, text = ':').grid(row = x + 1, column = 1)

tPlyrVal = StringVar
PlyrNmVal = StringVar

tPlyrEntry = Entry(detailFrame, textvariable = tPlyrVal, width = 60)
PlyrNmEntry = Entry(detailFrame, textvariable = PlyrNmVal, width = 60)

tPlyrEntry.grid(row = 1, column = 2)
PlyrNmEntry.grid(row = 2, column = 2)

rngLbl = Label(detailFrame, text = '(Min 2. Max 4)', padx = 20)#,bg = "lavender")
rngLbl.grid(row = 1, column = 3)

lblNote = Label(detailFrame, text = '', padx = 30)#, bg = "lavender")
lblNote.grid(row = 1, column = 4)

"""
r = IntVar()

for x in range(4):
    Radiobutton(detailFrame, text = f'Option {x + 1}', variable = r, value = x + 1).grid(column = 4)

myImg = ImageTk.PhotoImage(Image.open('D:/UR6523011/Sem 2/VGT123 Technology System Programming II/GitHub/Virtual-GUI-Game/GUI Sketch/image/uno backside.png'))
myLbl = Label(image = myImg).pack()
"""

wnd.mainloop()