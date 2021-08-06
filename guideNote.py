from tkinter import *
from tkinter import ttk

def rule(current, playerHand):
    playerHand.destroy()
    
    playerHand = Toplevel(current)
    playerHand.title('UNO Guide')
    playerHand.resizable(width = False, height = False)
    playerHand.iconbitmap('C:/gui/UNO_icon.ico')
    
    #Create another frame inside the canvas
    main_frame = Label(playerHand, bg = "skyblue2")
    main_frame.pack(side = LEFT, fill = BOTH, expand = True)

    Label(main_frame, text = "UNO GAME GUIDE",bg = 'skyblue2').grid(pady =10, sticky = N)
    Label(main_frame, text = "PLAYER INFORMATION",bg = 'skyblue2').grid(pady = 5,padx = 5,sticky = W)
    Label(main_frame, text = "Insert Total Player",bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "* Insert total player number in the entry box then press OK. Minimum player is 2 and maximum player is 4.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "Only number allowed !!", bg = 'skyblue2').grid(padx = 28,sticky = W)
    Label(main_frame, text = "Enter Player Name",bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "* Insert player name then click PLAY. Player can use special character, number, and word.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "  Empty name are not allowed !!", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "Name Confirmation",bg = 'skyblue2').grid(padx = 23, sticky = W)
    Label(main_frame, text = "* Press YES if you want to change or edit your name. Press NO if you want to proceed with the name.", bg = 'skyblue2').grid(padx = 23, sticky = W)
    Label(main_frame, text = "IN GAME GUIDE",bg = 'skyblue2').grid(pady = 5,padx = 5,sticky = W)
    Label(main_frame, text = "Player spot and turns will shuffle automatically at the beginning of the game.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "Each player will be provide with a label of their name and total card in the deck.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "ACTION CARD",bg = 'skyblue2').grid(pady = 5,padx = 5,sticky = W)
    Label(main_frame, text = "Action cards add an extra level of strategy to Uno. There are five action card types in an Uno deck.",bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "* Skip card - the next player in the sequence misses a turn.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "* Reverse - reverses the direction of play.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "* Draw two - the next player draws two cards and misses one turn.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "* Wild card - lets the player choose what color to play.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    Label(main_frame, text = "* Draw four - declare the next color to match, and force the next player to draw four cards.", bg = 'skyblue2').grid(padx = 23,sticky = W)
    
    Label(main_frame, text = "",bg = 'skyblue2').grid(pady = 8,sticky = W)
    return playerHand

def history(current, playerHand):
    playerHand.destroy()
    playerHand = Toplevel(current)
    playerHand.title('UNO Guide')
    playerHand.resizable(width = False, height = False)
    playerHand.iconbitmap('C:/gui/UNO_icon.ico')