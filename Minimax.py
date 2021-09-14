from TicTacToe import ttt as t

class Minimax:
	def __init__(self, gs):
		self.gridSize = gs
		

	def minimax(self, state, currIndex, depth, maximizer):
		winner = t.findWinner(currIndex, state)
		if (depth == 0 or winner != None):
			return state, currIndex, winner
		
		

		