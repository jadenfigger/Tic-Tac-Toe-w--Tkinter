import gui

class ttt:
	def __init__(self, size):
		self.gridSize = size
		self.grid = self.createGrid()

		self.turn = "X"

	def createGrid(self):
		grid = []
		for i in range(self.gridSize):
			grid.append([])
			for j in range(self.gridSize):
				grid[i].append(" ")

		return grid

	def drawNextMove(self, index):
		self.grid[index[0]][index[1]] = self.turn

		if (self.turn == "X"): self.turn="O"
		else: self.turn="X"

		winner = self.findWinner()

		# if (winner == None):
		# 	gui.GUIController.disGameWindow(gui.GUIController(), self.gridSize)


	def findWinner(self):
		return None
