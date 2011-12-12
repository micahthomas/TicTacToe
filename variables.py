# TicTacToe/variables.py

# Line Formats
clearLineLarge = "*"*30 #dividers for organization (its a relif this isnt c++)
clearLineSmall = "-"*13 #the sperator between tictactoe rows

#box initial values
boxes = ["1","2","3","4","5","6","7","8","9"] # the tictactoe spaces

#players
player1 = {
	"id":1, #the id value of player
	"symbol":"x", #the mark of the player
	"turns":0, #number of turns taken by player
}
player2 = {
	"id":2, #the id value of player
	"symbol":"o", #the mark of the player
	"turns":0, #number of turns taken by player
}