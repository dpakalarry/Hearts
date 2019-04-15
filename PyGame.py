from tkinter import *
#import tkMessageBox
import random

root = Tk()
status = "setup"
def cardClick(event, num):
    if status == "setup":
        return
    if UsrHand[i] != -1:
        lblUsCd[i].configure(image = cdList[52])
        lblUsCd[i].image = cdList[52]
        UsrHand[i] = -1



cdList = []
for j in range(1,5):
    for i in range (1,14):
        strFile = ""
        if(i < 11 and i!= 1):
            strFile = str(i) + "_of_"
        elif(i == 1):
            strFile = "ace_of_"
        elif(i == 11):
            strFile = "jack_of_"
        elif(i == 12):
            strFile = "queen_of_"
        elif(i == 13):
            strFile = "king_of_"

        if(j == 1):
            strFile = strFile + "hearts"
        elif(j == 2):
            strFile = strFile + "diamonds"
        elif(j == 3):
            strFile = strFile + "spades"
        elif(j == 4):
            strFile = strFile + "clubs"

        if(i >10):
            strFile = strFile + "2.gif"
        else:
            strFile = strFile + ".gif"
        cdList.append(PhotoImage(file = strFile))
cdList.append(PhotoImage(file = "blank.gif"))


TM = Label(root)
TM.grid(column = 10)
TC = Label(root, text = "North")
TC.grid(row = 2, column = 10)

LM = Label(root)
LM.grid(row = 10)
LC = Label(root, text = "West")
LC.grid(row = 10, column = 2)

RM = Label(root)
RM.grid(row = 10, column = 20)
RC = Label(root, text = "East")
RC.grid(row = 10, column = 19)

BM = Label(root, text = "Your Hand")
BM.grid(row = 20, column = 10)

ML = Label(root, image = cdList[52])
ML.grid(row = 10, column = 9)
MU = Label(root, image = cdList[52])
MU.grid(row = 9, column = 10)
MR = Label(root, image = cdList[52])
MR.grid(row = 10, column = 11)
MD = Label(root, image = cdList[52])
MD.grid(row = 11, column = 10)


lblUsCd = []
for i in range(0,13):
    lblUsCd.append(Label(root, image = cdList[52]))
    lblUsCd[i].grid(row = 19, column =(i+4))
    lblUsCd[i].bind("<Button-1>", cardclick(i))

deck = []
for i in range(0,52):
    deck.append(i)

UsrHand = []
for i in range(0,13):
    lngth = len(UsrHand)
    while (lngth == len(UsrHand)):
        test = random.randint(0,52)
        if(test in deck):
            UsrHand.append(test)
            deck.remove(test)
    lblUsCd[i].configure(image = cdList[test])
    lblUsCd[i].image = cdList[test]

WstHand = []
for i in range(0,13):
    lngth = len(WstHand)
    while (lngth == len(WstHand)):
        test = random.randint(0,52)
        if(test in deck):
            WstHand.append(test)
            deck.remove(test)

NrtHand = []
for i in range(0,13):
    lngth = len(NrtHand)
    while (lngth == len(NrtHand)):
        test = random.randint(0,52)
        if(test in deck):
            NrtHand.append(test)
            deck.remove(test)

EstHand = []
for i in range(0,13):
    lngth = len(EstHand)
    while (lngth == len(EstHand)):
        test = random.randint(0,52)
        if(test in deck):
            EstHand.append(test)
            deck.remove(test)

tkinter.Messagebox.showInfo("Welcome", "To start, pick three cards to pass to your opponent")
status = "pass"


root.mainloop()
