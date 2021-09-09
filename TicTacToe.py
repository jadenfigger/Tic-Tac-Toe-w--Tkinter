

class TicTacToe:
	def __init_(self, size):
		self.gameSize = size
		self.grid = self.createGrid(size)

	def createGrid(self):
		grid = [[] for i in range(self.gridSize)]
		for j in range(self.gridSize):
			grid.append(" ")

		print(grid)
		return grid
