
class ttt:
	def __init__(self, size):
		print("here")
		self.gridSize = size
		self.grid = self.createGrid()

	def createGrid(self):
		grid = []
		for i in range(self.gridSize):
			grid.append([])
			for j in range(self.gridSize):
				grid[i].append(" ")

		print(grid)
		return grid
