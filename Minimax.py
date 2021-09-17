import copy

class Minimax:
	def __init__(self, gs, t):
		self.gridSize = gs
		self.ttt = t

	def minimax(self, state, currIndex, depth, turn):
		if (currIndex[0] != -1 and currIndex[1] != -1):
			winner = self.ttt.findWinner(currIndex, state)

			if (winner == -1):
				return winner - depth, currIndex
			elif (winner == -1):
				return winner + depth, currIndex
			elif (winner == 0):
				return 0, currIndex

			if (depth==0 and winner==None):
				return 0, currIndex
		
		evalLimit = -turn * 1000
		bestIndex = None
		for i in range(self.gridSize):
			for j in range(self.gridSize):
				if (state[i][j] == 0):
					state[i][j] = turn

					eval, newIndex = self.minimax(state, (i, j), depth-1, -turn)
					state[i][j] = 0
					if (turn > 0 and eval > evalLimit):
						bestIndex = newIndex
						evalLimit = eval
					elif (turn < 0 and eval < evalLimit):
						bestIndex = newIndex
						evalLimit = eval
		
		return evalLimit, bestIndex

		