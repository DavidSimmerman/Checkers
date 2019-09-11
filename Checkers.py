from tkinter import *
import functools

screen = Tk()
screen.title("Checkers")
screen.configure(background="white")

headerFrame = Frame(screen)
headerFrame.pack(fill=X)
headerText = Label(headerFrame, text="Checkers", bg="red", fg="black", font="none 30 bold")
headerText.pack(fill=X)
headerText = Label(headerFrame, text="", bg="white", fg="black", font="none 30 bold")
headerText.pack(fill=X)

blank_image = PhotoImage()

brdSpace = [63]
spcStatus = [63]
firstSel = -1
secondSel = -1
turnClr = "w"
whiteCnt = 0
blackCnt = 0


# ==============Functions=============
def exitGame():
    screen.destroy()
    exit()


def playChecksAgain():
    global goFrame
    goFrame.destroy()
    boardFrame.destroy()
    twoPlayers()


def gameOver(team):
    global goFrame
    goFrame = Frame(screen, bg="white")
    goFrame.pack(fill=X)
    GOText = "Game over! " + team + " wins!"
    GOTextLabel = Label(goFrame, text=GOText, bg="white", fg="black", font="none 25 bold")
    GOTextLabel.grid(row=0, column=0, columnspan=3)
    GOPlayAgainBtn = Button(goFrame, text="Play Again", fg="black", font="none 16 bold", relief=GROOVE, command=playChecksAgain)
    GOPlayAgainBtn.grid(row=1, column=0)
    GOMenu = Button(goFrame, text="Menu", fg="black", font="none 16 bold", relief=GROOVE,
                            command=playChecksAgain)
    GOMenu.grid(row=1, column=1)
    GOQuit = Button(goFrame, text="Quit", fg="black", font="none 16 bold", relief=GROOVE,
                            command=exitGame)
    GOQuit.grid(row=1, column=2)


def checkWin():
    global blackCnt
    global whiteCnt
    global turnClr
    if whiteCnt == 0:
        turnClr = "GO"
        gameOver("Black")
    if blackCnt == 0:
        turnClr = "GO"
        gameOver("White")



def checkQueen(spc):
    if spcStatus[spc] is "w":
        if spc == 57 or spc == 59 or spc == 61 or spc == 63:
            brdSpace[spc].config(text="❂")
            spcStatus[spc] = "wq"
            print("USER LOG: Space " + str(spc) + " has become a King!")
    if spcStatus[spc] is "b":
        if spc == 0 or spc == 2 or spc == 4 or spc == 6:
            brdSpace[spc].config(text="❂")
            spcStatus[spc] = "bq"
            print("USER LOG: Space " + str(spc) + " has become a King!")


#TODO Create a cant move return
def canMove(fSel, sSel):
    if spcStatus[fSel] is "w":
        if fSel == sSel-7 or fSel == sSel-9:
            return "move"
        elif fSel == sSel - 18:
            if spcStatus[sSel - 9] is "b" or spcStatus[sSel - 9] is "bq":
                return sSel - 9
            else:
                return "nomove"
        elif fSel == sSel - 14:
            if spcStatus[sSel - 7] is "b" or spcStatus[sSel - 7] is "bq":
                return sSel - 7
            else:
                return "nomove"
        else:
            return "nomove"
    if spcStatus[fSel] is "b":
        if fSel == sSel+7 or fSel == sSel+9:
            return "move"
        elif fSel == sSel+18:
            if spcStatus[sSel+9] is "w" or spcStatus[sSel+9] is "wq":
                return sSel+9
            else:
                return "nomove"
        elif fSel == sSel+14:
            if spcStatus[sSel+7] is "w" or spcStatus[sSel+7] is "wq":
                return sSel+7
            else:
                return "nomove"
        else:
            return "nomove"
    if spcStatus[fSel] is "bq":
        if fSel == sSel+7 or fSel == sSel+9 or fSel == sSel-7 or fSel == sSel-9:
            return "move"
        elif fSel == sSel+18:
            if spcStatus[sSel+9] is "w" or spcStatus[sSel+9] is "wq":
                return sSel+9
            else:
                return "nomove"
        elif fSel == sSel+14:
            if spcStatus[sSel+7] is "w" or spcStatus[sSel+7] is "wq":
                return sSel+7
            else:
                return "nomove"
        elif fSel == sSel-18:
            if spcStatus[sSel-9] is "w" or spcStatus[sSel-9] is "wq":
                return sSel-9
            else:
                return "nomove"
        elif fSel == sSel-14:
            if spcStatus[sSel-7] is "w" or spcStatus[sSel-7] is "wq":
                return sSel-7
            else:
                return "nomove"
        else:
            return "nomove"
    if spcStatus[fSel] is "wq":
        if fSel == sSel+7 or fSel == sSel+9 or fSel == sSel-7 or fSel == sSel-9:
            return "move"
        elif fSel == sSel+18:
            if spcStatus[sSel+9] is "b" or spcStatus[sSel+9] is "bq":
                return sSel+9
            else:
                return "nomove"
        elif fSel == sSel+14:
            if spcStatus[sSel+7] is "b" or spcStatus[sSel+7] is "bq":
                return sSel+7
            else:
                return "nomove"
        elif fSel == sSel-18:
            if spcStatus[sSel-9] is "b" or spcStatus[sSel-9] is "bq":
                return sSel-9
            else:
                return "nomove"
        elif fSel == sSel-14:
            if spcStatus[sSel-7] is "b" or spcStatus[sSel-7] is "bq":
                return sSel-7
            else:
                return "nomove"
        else:
            return "nomove"


#TODO Add force jump
def movePc(fSel, sSel):
    global turnClr
    newSts = spcStatus[fSel]
    brdSpace[fSel].config(fg="red", bg="red")
    spcStatus[fSel] = "o"
    if newSts is "w":
        brdSpace[sSel].config(fg="white")
        spcStatus[sSel] = "w"
        turnClr = "b"
        checkQueen(sSel)
    if newSts is "b":
        brdSpace[sSel].config(fg="black")
        spcStatus[sSel] = "b"
        turnClr = "w"
        checkQueen(sSel)
    if newSts is "bq":
        brdSpace[sSel].config(fg="black", text="❂")
        spcStatus[sSel] = "bq"
        brdSpace[fSel].config(text="⬤")
        turnClr = "w"
    if newSts is "wq":
        brdSpace[sSel].config(fg="white", text="❂")
        spcStatus[sSel] = "wq"
        brdSpace[fSel].config(text="⬤")
        turnClr = "b"


#TODO Add win condition
#TODO Add double jumps
def jumpPc(fSel, sSel, jpc):
    global turnClr
    global blackCnt
    global whiteCnt
    newSts = spcStatus[fSel]
    brdSpace[fSel].config(fg="red", bg="red")
    spcStatus[fSel] = "o"
    brdSpace[jpc].config(fg="red")
    if spcStatus[jpc] is "bq" or spcStatus[jpc] is "wq":
        brdSpace[jpc].config(text="⬤")
    spcStatus[jpc] = "o"
    if newSts is "w":
        brdSpace[sSel].config(fg="white")
        spcStatus[sSel] = "w"
        turnClr = "b"
        checkQueen(sSel)
        blackCnt -= 1
    if newSts is "b":
        brdSpace[sSel].config(fg="black")
        spcStatus[sSel] = "b"
        turnClr = "w"
        checkQueen(sSel)
        whiteCnt -= 1
    if newSts is "bq":
        brdSpace[sSel].config(text="❂", fg="black")
        spcStatus[sSel] = "bq"
        brdSpace[fSel].config(text="⬤")
        turnClr = "w"
        checkQueen(sSel)
        whiteCnt -= 1
    if newSts is "wq":
        brdSpace[sSel].config(text="❂", fg="white")
        spcStatus[sSel] = "wq"
        brdSpace[fSel].config(text="⬤")
        turnClr = "b"
        checkQueen(sSel)
        blackCnt -= 1
    checkWin()

#TODO remove blue selector if not used
def spaceClicked(spcNumb):
    global firstSel
    global secondSel
    if spcStatus[spcNumb] == turnClr:
        print("USER LOG: Space " + str(spcNumb) + " is the first selection")
        firstSel = spcNumb
        brdSpace[firstSel].configure(bg="#100b93")
    elif spcStatus[spcNumb] is "bq" and turnClr is "b":
        print("USER LOG: Space " + str(spcNumb) + " is the first selection")
        firstSel = spcNumb
        brdSpace[firstSel].configure(bg="#100b93")
    elif spcStatus[spcNumb] is "wq" and turnClr is "w":
        print("USER LOG: Space " + str(spcNumb) + " is the first selection")
        firstSel = spcNumb
        brdSpace[firstSel].configure(bg="#100b93")
    if spcStatus[spcNumb] is "o" and firstSel is not -1:
        print("USER LOG: Space " + str(spcNumb) + " is the second selection")
        secondSel = spcNumb
        if canMove(firstSel, secondSel) is "move":
            print("USER LOG: moved " + str(firstSel) + " to " + str(secondSel) + ".")
            movePc(firstSel, secondSel)
        elif canMove(firstSel, secondSel) is "nomove":
            print("USER LOG: There is no move here!")
        elif canMove(firstSel, secondSel) > -1:
            print("jump")
            jumpPc(firstSel, secondSel, canMove(firstSel, secondSel))


def click():
    print("USER LOG: A black space was clicked")


# ==============SetsUpGame=============
def setBoard():
    global whiteCnt
    global blackCnt
    for i in range(64):
        brdSpace.append("")
        spcStatus.append("")
    spcCnt = 0
    wSCnt = 0
    bSCnt = 41
    for x in range(8):
        for y in range(8):
            print("AUTO LOG: Creating a space for: (" + str(x) + ", " + str(y) + ").")
            if x % 2 == 0:
                if spcCnt % 2 == 0:
                    brdSpace[spcCnt] = Button(boardFrame, image=blank_image, text="⬤", bg="red", fg="red",
                                              font="none 50 bold", height=70, width=70, bd=0, compound=CENTER,
                                              command=functools.partial(spaceClicked, spcCnt))
                    brdSpace[spcCnt].grid(row=x, column=y)
                    spcCnt += 1
                    spcStatus[spcCnt] = "o"
                else:
                    brdSpace[spcCnt] = Button(boardFrame, image=blank_image, text="⬤", bg="black", fg="black",
                                              font="none 50 bold", height=70, width=70, bd=0, compound=CENTER,
                                              command=click)
                    brdSpace[spcCnt].grid(row=x, column=y)
                    spcCnt += 1
                    spcStatus[spcCnt] = "o"
            else:
                if spcCnt % 2 == 0:
                    brdSpace[spcCnt] = Button(boardFrame, image=blank_image, text="⬤", bg="black", fg="black",
                                              font="none 50 bold", height=70, width=70, bd=0, compound=CENTER,
                                              command=click)
                    brdSpace[spcCnt].grid(row=x, column=y)
                    spcCnt += 1
                    spcStatus[spcCnt] = "o"
                else:
                    brdSpace[spcCnt] = Button(boardFrame, image=blank_image, text="⬤", bg="red", fg="red",
                                              font="none 50 bold", height=70, width=70, bd=0, compound=CENTER,
                                              command=functools.partial(spaceClicked, spcCnt))
                    brdSpace[spcCnt].grid(row=x, column=y)
                    spcCnt += 1
                    spcStatus[spcCnt] = "o"
    for w in range(12):
        brdSpace[wSCnt].config(fg="white")
        spcStatus[wSCnt] = "w"
        if wSCnt == 6:
            wSCnt += 1
        if wSCnt == 15:
            wSCnt -= 1
        wSCnt += 2
    for b in range(12):
        brdSpace[bSCnt].config(fg="black")
        spcStatus[bSCnt] = "b"
        if bSCnt == 47:
            bSCnt -= 1
        if bSCnt == 54:
            bSCnt += 1
        bSCnt += 2
    whiteCnt = 12
    blackCnt = 12
# ====================================


# ================Menu================
def menu():
    global brdSpace
    global menuFrame

    menuFrame = Frame(screen, background="white")
    menuFrame.pack()
    welcomeText = Label(menuFrame, text="Welcome to checkers!", bg="white", fg="black", font="none 20 bold")
    welcomeText.grid(row=0, column=0, sticky=N, columnspan=2)

    onepButton = Button(menuFrame, text="One Player(coming soon)", fg="black", font="none 16 bold", relief=GROOVE,
                        command=onePlayer)
    onepButton.grid(row=1, column=0, sticky=N)
    twopButton = Button(menuFrame, text="Two Players", fg="black", font="none 16 bold", relief=GROOVE,
                        command=twoPlayers)
    twopButton.grid(row=2, column=0, sticky=N)

    spacer = Label(menuFrame, text="", bg="white")
    spacer.grid(row=3)

    quitBTN = Button(menuFrame, text="Quit Game", fg="black", font="none 16 bold", relief=GROOVE, command=exitGame)
    quitBTN.grid(row=4, sticky=S)
# ====================================


# ==============OnePlayer=============
def onePlayer():
    print("op")


# ====================================
# ==============TwoPlayer=============
def twoPlayers():
    global menuFrame
    global boardFrame

    menuFrame.destroy()
    boardFrame = Frame(screen, background="white")
    boardFrame.pack()

    setBoard()
# ====================================


menu()

screen.mainloop()
