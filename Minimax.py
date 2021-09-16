import copy


class Minimax:
	def __init__(self, gs, t):
		self.gridSize = gs
		self.ttt = t

	def minimax(self, state, currIndex, depth, turn):
		winner = self.ttt.findWinner(currIndex, state)

  
		if (depth == 0 or winner != None):
			if (depth == 0 and winner==None): winner = 0
			return winner, currIndex
		
		evalLimit = -turn * 10
		bestIndex = None
		for i in range(self.gridSize):
			for j in range(self.gridSize):
				if (state[i][j] == 0):
					eval, newIndex = self.minimax(self.copyGrid(state, turn, (i, j)), (i, j), depth-1, -turn)
					if (turn > 0 and eval >= evalLimit):
						print(eval, newIndex, turn)
						bestIndex = newIndex
						evalLimit = eval
					elif (turn < 0 and eval <= evalLimit):
						print(eval, newIndex, turn)
						bestIndex = newIndex
						evalLimit = eval
		return evalLimit, bestIndex


	def copyGrid(self, original, change, index):
		temp = copy.deepcopy(original)
		temp[index[0]][index[1]] = change
		return temp

		