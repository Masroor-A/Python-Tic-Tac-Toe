from tkinter import *

root = Tk()
root.config(background="dark gray")
colour = "white"
board = [['', '', ''], 
				 ['', '', ''], 
				 ['', '', '']]

size = 10
global turn
turn = 1
global winner
winner = ""
player = {1: "X", 0: "O"}
TL_Text = StringVar()
TM_Text = StringVar()
TR_Text = StringVar()
ML_Text = StringVar()
MM_Text = StringVar()
MR_Text = StringVar()
BL_Text = StringVar()
BM_Text = StringVar()
BR_Text = StringVar()


def WinCheck():
	if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or board[
	  0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or board[0][
	   2] == "X" and board[1][2] == "X" and board[2][2] == "X" or board[0][
	    0] == "X" and board[0][1] == "X" and board[0][2] == "X" or board[1][
	     0] == "X" and board[1][1] == "X" and board[1][2] == "X" or board[2][
	      0] == "X" and board[2][1] == "X" and board[2][2] == "X" or board[0][
	       0] == "X" and board[1][1] == "X" and board[2][2] == "X" or board[0][
	        2] == "X" and board[1][1] == "X" and board[2][0] == "X":
		global winner
		winner = "X"
		root2 = Tk()
		root2.geometry("300x100")
		sentence = "The Winner is " + winner
		text = Label(root2, text=sentence, font=('Helvetica bold', 26))
		text.grid(column=0, row=0)
		root2.mainloop()

	elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" or board[
	  0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" or board[0][
	   2] == "O" and board[1][2] == "O" and board[2][2] == "O" or board[0][
	    0] == "O" and board[0][1] == "O" and board[0][2] == "O" or board[1][
	     0] == "O" and board[1][1] == "O" and board[1][2] == "O" or board[2][
	      0] == "O" and board[2][1] == "O" and board[2][2] == "O" or board[0][
	       0] == "O" and board[1][1] == "O" and board[2][2] == "O" or board[0][
	        2] == "O" and board[1][1] == "O" and board[2][0] == "O":

		winner = "O"
		root2 = Tk()
		root2.geometry("300x100")
		sentence = "The Winner is " + winner
		text = Label(root2, text=sentence, font=('Helvetica bold', 26))
		text.grid(column=0, row=0)
		root2.mainloop()


def TL_command():
	global turn
	TL_Text.set(player[turn % 2])
	board[0][0] = player[turn % 2]
	turn += 1
	WinCheck()


def TM_command():
	global turn
	TM_Text.set(player[turn % 2])
	board[0][1] = player[turn % 2]
	turn += 1
	WinCheck()


def TR_command():
	global turn
	TR_Text.set(player[turn % 2])
	board[0][2] = player[turn % 2]
	turn += 1
	WinCheck()


def ML_command():
	global turn
	global turn
	ML_Text.set(player[turn % 2])
	board[1][0] = player[turn % 2]
	turn += 1
	WinCheck()


def MM_command():
	global turn
	MM_Text.set(player[turn % 2])
	board[1][1] = player[turn % 2]
	turn += 1
	WinCheck()


def MR_command():
	global turn
	MR_Text.set(player[turn % 2])
	board[1][2] = player[turn % 2]
	turn += 1
	WinCheck()


def BL_command():
	global turn
	BL_Text.set(player[turn % 2])
	board[2][0] = player[turn % 2]
	turn += 1
	WinCheck()


def BM_command():
	global turn
	BM_Text.set(player[turn % 2])
	board[2][1] = player[turn % 2]
	turn += 1
	WinCheck()


def BR_command():
	global turn
	BR_Text.set(player[turn % 2])
	board[2][2] = player[turn % 2]
	turn += 1
	WinCheck()


TL = Button(root,
            textvariable=TL_Text,
            width=size,
            height=size - 5,
            command=TL_command,
            background=colour)
TM = Button(root,
            textvariable=TM_Text,
            width=size,
            height=size - 5,
            command=TM_command,
            background=colour)
TR = Button(root,
            textvariable=TR_Text,
            width=size,
            height=size - 5,
            command=TR_command,
            background=colour)
ML = Button(root,
            textvariable=ML_Text,
            width=size,
            height=size - 5,
            command=ML_command,
            background=colour)
MM = Button(root,
            textvariable=MM_Text,
            width=size,
            height=size - 5,
            command=MM_command,
            background=colour)
MR = Button(root,
            textvariable=MR_Text,
            width=size,
            height=size - 5,
            command=MR_command,
            background=colour)
BL = Button(root,
            textvariable=BL_Text,
            width=size,
            height=size - 5,
            command=BL_command,
            background=colour)
BM = Button(root,
            textvariable=BM_Text,
            width=size,
            height=size - 5,
            command=BM_command,
            background=colour)
BR = Button(root,
            textvariable=BR_Text,
            width=size,
            height=size - 5,
            command=BR_command,
            background=colour)

TL.grid(column=0, row=0)
TM.grid(column=0, row=1)
TR.grid(column=0, row=2)
ML.grid(column=1, row=0)
MM.grid(column=1, row=1)
MR.grid(column=1, row=2)
BL.grid(column=2, row=0)
BM.grid(column=2, row=1)
BR.grid(column=2, row=2)

root.mainloop()
