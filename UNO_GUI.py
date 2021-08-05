from tkinter import *
import UNO_config as UC
import sys
import guideNote as GN
import sqlite3

window = Tk()
window.title('UNO')
window.resizable(width = False, height = False)
window.iconbitmap('C:/gui/UNO_icon.ico')

detailFrame1 = Label(window, bg = 'skyblue2')
guideInfo = Label(window)
view_rank = Label(window)

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
Define main page for Frame 1
**************************************
parameter       ||  None
**************************************
return value    ||  None
'''
def main_page_part_1():
    detailFrame1.pack(fill = X)

    buttonPlay = Button(detailFrame1, text = 'PLAY', padx = 40, pady = 10,
        fg = 'WHITE', bg = "blue4", state = DISABLED)
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

    okayButton = Button(detailFrame1, text = 'OK', padx = 5, pady = 3, fg = 'WHITE',  bg = "blue4")
    okayButton.grid(row = 2, column = 2, pady = 10)

    ruleButton = Button(detailFrame1, text = 'GUIDE', fg = 'WHITE',  bg = "blue4", command = guideClicked)
    ruleButton.grid(row = 0, column = 4)
    
    historyButton = Button(detailFrame1, text = 'HISTORY', fg = 'white', bg = 'blue4', command = rankView)
    historyButton.grid(row = 0, column = 0)

main_page_part_1()

window.mainloop()