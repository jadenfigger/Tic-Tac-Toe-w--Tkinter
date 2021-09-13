import gui

class ttt:
	def __init__(self, size):
		self.gridSize = size
		self.grid = self.createGrid()

		# If using minimax algorithm, user is maximizer(1) and computer is minimizer(-1)
		self.turn = 1

	def createGrid(self):
		grid = []
		for i in range(self.gridSize):
			grid.append([])
			for j in range(self.gridSize):
				grid[i].append(" ")

		return grid

	def updateGameGrid(self, index):
		self.grid[index[0]][index[1]] = self.turn

		if (self.turn == "X"): self.turn="O"
		else: self.turn="X"

		# winner = self.findWinner()			


	def findWinner(self):
		return None
