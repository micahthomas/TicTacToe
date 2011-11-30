#functions.py
import os
from variables import *

def call(functionName):
	#just a quick idea that helps me understand where and why the program crashed
	print "DEBUG: " + functionName + "() has been called"
	result = globals()[functionName]()
	print "DEBUG: " + functionName + "() has exited with: " + str(result)
	return result

def printError(error):
	drawBoard();
	print "\nERROR:\n"
	for (i in error)
		print "\t" + i
	print "\n"

def clearScreen():
    os.system(['clear','cls'][os.name == 'nt'])

def printIntro():
	print
	clearScreen();
	print clearLineLarge
	print "Program: TiCTaCToE"
	print "Version: 1"
	print "Author: Micah Thomas"
	print clearLineLarge
	print "This is a 2 player game, find another player now!"

def printMenu():
	print clearLineLarge
	loopVal = 0
	while (loopVal == 0):
		ans = raw_input("ENTER(y/n) => ")
		if (ans == "y" or ans == "Y"):
			loopVal = 1
		else:
			if (ans == "n" or ans == "N"):
				loopVal = 0
			else: loopVal = 0

def drawBoard():
	clearScreen();
	i = 0
	while ((i < 9) and (i >= 0)):
		print boxes[i],
		if ((i+1)%3):
			print " | ",
		else:
			if (i < 6):
				print "\n" + clearLineSmall
		i += 1
	print "\n"

def boxIsEmpty(box):
	currMark = boxes[box-1]
	if (currMark == "x" or currMark == "o"):
		return 0
	else:
		return 1
	#TODO: make a function to check for a player's mark: boxIsMarked()
def insertMark(boxChoice, player):
	if (player == 1):
		mark = player1["symbol"]
	else:
		mark = player2["symbol"]
	print "boxChoice = " + str(boxChoice)
	if ((boxChoice > 0) and (boxIsEmpty(boxChoice))):
		boxChoice -= 1 # to make boxChoice => index of the box
		boxes[boxChoice] = mark;
		return 1
	else:
		print "Box already marked or not a valid Box selection"
		return 0

def checkGameOver():#TODO: take in player id to see if they won
	#TODO: change entire algorithm to use boxIsMarked(boxNumber, playerId)
	#TODO: change the order of if statements to large to small [its more efficient]
	if (not boxIsEmpty(1)):
		if (not boxIsEmpty(2)):
			if (not boxIsEmpty(3)):
				return 1
		else:
			if (not boxIsEmpty(4)):
				if (not boxIsEmpty(7)):
					return 1
			else:
				if (boxIsEmpty(5)):
					if (boxIsEmpty(9)):
						return 1
	
	if (not boxIsEmpty(5)):
		if (not boxIsEmpty(2)):
			if (not boxIsEmpty(8)):
				return 1
		else:
			if (not boxIsEmpty(4)):
				if (not boxIsEmpty(6)):
					return 1
			else:
				if (not boxIsEmpty(3)):
					if (not boxIsEmpty(7)):
						return 1
	
	if (not boxIsEmpty(9)):
		if (not boxIsEmpty(3)):
			if (not boxIsEmpty(6)):
				return 1
		else:
			if (not boxIsEmpty(7)):
				if (not boxIsEmpty(8)):
					return 1
	
	return 0

#TODO: make a ask() to ask question and check answer
def ask(player):
	varInput = raw_input(question % player)

#TODO: make a questionLoop()

def gameLoop():
	#TODO: use a question loop and change gameLoop to have just printMenu, questionLoop(), printWinner()
	i = 0
	gameOver = 0
	while ((gameOver == 0)):
		drawBoard();
		boxSelection = 0
		while (not boxSelection):
			varInput = raw_input();
			try:
			    varInput = int(varInput)
			except ValueError:
			    varInput = 100
			if (varInput != 100):
				boxSelection = insertMark(varInput, 1);
			print "boxSelection = " + str(boxSelection)
			gameOver = call("checkGameOver");
			if (gameOver == 0):
				break
		drawBoard();
		boxSelection = 0
		while (not boxSelection):
			varInput = raw_input("Player 2: Please ENTER the number of the box you want to mark => ");
			try:
			    varInput = int(varInput)
			except ValueError:
			    varInput = 100
			if (varInput != 100):
				boxSelection = insertMark(varInput, 2);
		gameOver = call("checkGameOver");
	return 1

#TODO: make printWinner()

#TODO: make resetValues()
