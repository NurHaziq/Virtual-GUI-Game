import sqlite3
from tkinter import *

window = Tk()
window.title('Winner Database')
window.iconbitmap('C:/gui/UNO_icon.ico')

def makeDatabase():
    #Connect to Database
    player = sqlite3.connect('winningPos.db')

    #Create a cursor
    c = player.cursor()

    c.execute("""CREATE TABLE winning (
                first_place_name text,
                first_place_Totalcard integer,
                second_place_name text,
                second_place_Totalcard integer,
                third_place_name text,
                third_place_Totalcard integer,
                fourth_place_name text,
                fourth_place_Totalcard integer
                )""")

    player.commit()
    player.close()

Button(window, text = 'Click Me', command = makeDatabase).pack()
window.mainloop()