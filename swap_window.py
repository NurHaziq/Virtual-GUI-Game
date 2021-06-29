from tkinter import *

window = Tk()
window.geometry('200x200')

frame = Label(window)
frame.pack(pady = 20)

def clear():
    global frame
    frame.pack_forget()

myButton = Button(frame, text = 'PLAY', padx = 40, pady = 10, fg = 'WHITE', bg = "DODGERBLUE", command = clear)
myButton.pack()

window.mainloop()