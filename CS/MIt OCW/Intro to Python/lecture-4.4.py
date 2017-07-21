#lecture-4.4.py
'''
This example uses lists to test valid input and see who won
'in' or 'not in' tests to see if an item is in a list
'''

VALID_OPTIONS = ["rock", "paper", "scissors"]

# a list of lists. describes the tree winning combos where the first item is the winner and the second is the loser

WINNING_COMBOS = [["paper", "rock"], ["rock", "scissors"], ["scissors", "paper"]]

def rps(player1, player2):
	'''
	plays a game of rock paper, scissors and returns a string as to who won
	'''

	# turn player1's input into lowercase and see if it is in the list
	if player1.lower() not in VALID_OPTIONS:
		return "Invalid input - must be 'paper', 'rock', or 'scissors'; got '" + str(player1) + "'"
	if player2.lower() not in VALID_OPTIONS:
		return "Invalid input - must be 'paper', 'rock', or 'scissors'; got '" + str(player2) + "'"


	if player1 == player2:
		return "Tie game"
	elif [player1, player2] in WINNING_COMBOS:
		return "player1 wins!"
	elif [player2, player1] in WINNING_COMBOS:
		return "player2 wins!"
	else: 
		return "Shouldn't get here" # should have covered all options

# test
print rps("scissors", "paper") # player1 should win
print rps("rock", "paper") # player2 should win
print rps("rock", "rock") # Tie game
print rps("rock", "blurple") # Invalid input