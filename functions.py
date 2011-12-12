# TicTacToe/functions.py

import os
from variables import *

def clearScreen():
	# @description: function for clearing the terminal window using cls on
	# windows and clear on linux
	# clearScreen() adapted from http://stackoverflow.com/questions/517970
    os.system(['clear','cls'][os.name == 'nt'])
    print "Enter 'Quit' At Any Prompt To Quit The Program\n"

def buffInput(question):
	# @description: function for checking if input is quit, otherwise return
	# the input (custom input function)
	# @return: the raw_input
	raw_input_var = raw_input(question).lower()
	if (raw_input_var == "quit"):
		os._exit(0)	# quits the program with exit code 0
	else:
		try:
			return raw_input_var[0]
		except:
			return "" # if raw_input_var was empty return ""

def printIntro():
	# @description: function for printing Introduction message
	clearScreen()
	print clearLineLarge
	print "Program: TiCTaCToE"
	print "Version: 2.0" # i wanted to make it look stable :-)
	print "Author: Micah Thomas"
	print clearLineLarge
	print "This Is A 2 Player Game, Find Another Player Now!"

def printMenu():
	# @description: function for printing the Basic Menu for starting the Game
	# @return:	1: if ans == y/Y
	#			2: exceptions
	ans = ""
	while (ans not in ["y","n"]):
		ans = buffInput("(ENTER: y/n) => ").lower()
	if (ans == "y"):
		return 1
	return 0

def printError(error):
	# @description: function for a uniform and distinguishable formatting for
	# for errors and also to make sure that errors dont fill the screen by
	# calling drawBoard() before printing errors.
	drawBoard()
	print "\n\t" + error + "\n"

def drawBoard():
	# @description: function for printing the board in a uniform manner
	# Used while loop and if statements to ouptut the correct seperators
	clearScreen()
	i = 0
	while ((i < 9) & (i >= 0)):
		print boxes[i],
		if ((i+1)%3):	#i+1 because that makes the index number = the box number
			print " | ",
		else:
			if (i < 6):
				print "\n" + clearLineSmall
		i += 1
	print "\n"

def boxIsMarked(box, player):
	# @description: function for checking if a box is already filled by the
	# player's mark
	# @params:	box: the number of the box
	#			player: the number of the player
	# @return:	1: if the box is marked
	#			0: exceptions
	box -= 1
	if (player == 1):
		mark = player1["symbol"]
	else:
		mark = player2["symbol"]
	if (boxes[box] == mark):
		return 1
	else:
		return 0

def markBox(box, player):
	# @description: function for marking the box if its not already marked
	# @params:	box: the number of the box
	#			player: the number of the player
	# @return:	1: successfull
	#			0: exceptions
	if (player == 1):
		mark = player1["symbol"]
		player = 2
	else:
		mark = player2["symbol"]
		player = 1
	if (not boxIsMarked(box, player)):
		box -= 1
		boxes[box] = mark
		return 1
	else:
		printError("Invalid Selection:\n\t\tBox No.%s Is Already Marked!\n\tPlease Select An Empty Box." % box)
		return 0

def gameOver(player):
	# @description: the function for checking if the game is over by checking
	# combinations of winning possibilities.
	# @params:	player: this is the variable passed over to boxIsMarked()
	# @return:	1: if game is over
	#			0: exceptions
	if (boxIsMarked(3, player)):
		if (boxIsMarked(2, player)):
			if (boxIsMarked(1, player)):
				#top row
				return 1
		else:
			if (boxIsMarked(5, player)):
				if(boxIsMarked(7, player)):
					#top right diagonal
					return 1
			else:
				if (boxIsMarked(6, player)):
					if (boxIsMarked(9, player)):
						#right column
						return 1

	if (boxIsMarked(5, player)):
		if (boxIsMarked(8, player)):
			if (boxIsMarked(2, player)):
				#middle column
				return 1
		else:
			if (boxIsMarked(6, player)):
				if (boxIsMarked(4, player)):
					#middle row
					return 1
			else:
				if (boxIsMarked(9, player)):
					if (boxIsMarked(1, player)):
						#top left diagonal
						return 1

	if (boxIsMarked(7, player)):
		if (boxIsMarked(8, player)):
			if (boxIsMarked(9, player)):
				#bottom row
				return 1
		else:
			if (boxIsMarked(4, player)):
				if (boxIsMarked(1, player)):
					#left column
					return 1

	return 0

def ask(player):
	# @description: the function that asks the question and if the answer is
	# integer, it saves the value.
	# @params:	player: the player number
	# @return:	ans: raw_input if int, exceptions: 0
	ans = 0
	# check if input is int:
	# http://stackoverflow.com/questions/5424716
	try:
		ans = int(buffInput("Player %s: Please ENTER The Number Of The BOX You Would Like To Mark => " % player))
	except:
		printError("Invalid Input:\n\n\t\tInput Was Not An Integer!")
	return ans

def questionLoop():
	# @description: the loop that draws the board and initializes the question
	# loop untill game is over
	# @return:	1: if the winner is player 1
	#			2: if the winner is player 2
	drawBoard()
	runs = 0
	while (runs < 10):
		marked = 0
		while (marked == 0):
			ans = 0
			while (not (ans > 0 and ans < 10)):
				ans = ask(1)
				if (not (ans > 0 and ans < 10)):
					printError("Invalid Input:\n\n\t\tInput Was Not In The Range Of 1 And 9!\n\n\tSelect A Valid Box Number")
			marked = markBox(ans, 1)
		player1["turns"] += 1
		runs += 1
		if (runs == 9):
			drawBoard()
			return 3
		drawBoard()
		if (gameOver(1)):
			return 1
		marked = 0
		while (not marked):
			ans = 0
			while (not (ans > 0 and ans < 10)):
				ans = ask(2)
				if (not (ans > 0 and ans < 10)):
					printError("Invalid Input:\n\n\t\tInput Was Not In The Range Of 1 And 9!\n\n\tSelect A Valid Box Number")
			marked = markBox(ans, 2)
		player2["turns"] += 1
		runs += 1
		drawBoard()
		if (gameOver(2)):
			return 2
	return 3

def printWinner(winner):
	# @description: the function for printing the info regarding game.
	# @params: winner: the player who won
	drawBoard()
	print "The Winner Is Player %s. \nPlayer 1:\n\tTurns Taken: %s\nPlayer 2:\n\tTurns Taken: %s" % (winner, player1["turns"], player2["turns"])

def game():
	# @description: the function that defines the game loop
	winner = questionLoop()
	if (winner == 3):
		print "The Game Is A Draw!"
		print "Would You Like To Play Again?"
	else:
		printWinner(winner)

def resetVariables():
	# @description: the function for resetting the Variables
	global boxes
	global player1
	global player2
	boxes = ["1","2","3","4","5","6","7","8","9"]
	player1 = {
		"id":1,
		"symbol":"x",
		"turns":0,
	}
	player2 = {
		"id":2,
		"symbol":"o",
		"turns":0,
	}