# TicTacToe/main.py

from functions import *

printIntro(); # prints introduction
print "Would You Like To Play The Game?"
menu = printMenu();
while (menu == 1):
	game();
	menu = printMenu();
	resetVariables();