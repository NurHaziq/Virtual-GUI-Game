from tkinter import *
from PIL import ImageTk, Image

wnd = Tk()
wnd.geometry("600x400")
wnd.title('UNO')
wnd.iconbitmap('D:/UR6523011/Sem 2/VGT123 Technology System Programming II/GitHub/Virtual-GUI-Game/GUI Sketch/image/uno_icon.ico')

frame = Label(wnd)
frame.pack()

def onClick():
    global frame
    frame.pack_forget()

btnPlay = Button(frame, text = 'PLAY', padx = 40, pady = 10, command = onClick, fg = 'WHITE', bg = "DODGERBLUE")
btnPlay.grid(row = 0, column = 0, columnspan = 5, pady = (10, 30))

tPlyr = Label(frame, text = 'Total Player')
PlyrNm = Label(frame, text = 'Player Name')

tPlyr.grid(row = 1, column = 0)
PlyrNm.grid(row = 2, column = 0)

for x in range(2):
    myLbl = Label(frame, text = ':').grid(row = x + 1, column = 1)

tPlyrVal = StringVar
PlyrNmVal = StringVar

tPlyrEntry = Entry(frame, textvariable = tPlyrVal)
PlyrNmEntry = Entry(frame, textvariable = PlyrNmVal)

tPlyrEntry.grid(row = 1, column = 2)
PlyrNmEntry.grid(row = 2, column = 2)

rngLbl = Label(frame, text = '(Min 2. Max 4)', padx = 20)
rngLbl.grid(row = 1, column = 3)

lblNote = Label(frame, text = '', padx = 30)
lblNote.grid(row = 1, column = 4)

"""
r = IntVar()

for x in range(4):
    Radiobutton(frame, text = f'Option {x + 1}', variable = r, value = x + 1).grid(column = 4)

myImg = ImageTk.PhotoImage(Image.open('D:/UR6523011/Sem 2/VGT123 Technology System Programming II/GitHub/Virtual-GUI-Game/GUI Sketch/image/uno backside.png'))
myLbl = Label(image = myImg).pack()
"""

wnd.mainloop()