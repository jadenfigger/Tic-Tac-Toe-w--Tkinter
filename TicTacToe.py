from random import randint

class ttt:
	def __init__(self, size):
		self.gridSize = size
		self.grid = self.createGrid()

		# If using minimax algorithm, user is maximizer(1) and computer is minimizer(-1)
		# If single player, then user is 1, computer is -1
		# If multiplayer, user1 is 1, user2 = -1
		self.turn = 1
		self.winner = None

	def createGrid(self):
		grid = []
		for i in range(self.gridSize):
			grid.append([])
			for j in range(self.gridSize):
				grid[i].append(0)

		return grid

	def updateGameGrid(self, index):
		self.grid[index[0]][index[1]] = self.turn
		self.findWinner(index)	

		self.turn = -self.turn
		
	def randomIndex(self):
		x = randint(0, self.gridSize-1)
		y = randint(0, self.gridSize-1)
		while (self.grid[x][y] != 0):
			x = randint(0, self.gridSize-1)
			y = randint(0, self.gridSize-1)
		return (x, y)

	def findWinner(self, index):
		

		# Row
		found = True
		for j in range(self.gridSize-1):
			if (self.grid[index[0]][j] != self.grid[index[0]][j+1] or self.grid[index[0]][j] == 0):
				found = False
				break
		if (found):
			self.winner = self.turn
			return
		
		# Column
		found = True
		for i in range(self.gridSize-1):
			if (self.grid[i][index[1]] != self.grid[i+1][index[1]] or self.grid[i][index[1]] == 0):
				found = False
				break
		if (found):
			self.winner = self.turn
			return
		
		# Top Left to Bottom Right Diagonal
		if (index[0] == index[1]):
			found = True
			for i in range(self.gridSize-1):
				if (self.grid[i][i] != self.grid[i+1][i+1] or self.grid[i][i] == 0):
					found = False
					break
			if (found):
				self.winner = self.turn
				return

		# Top Right to Bottom Left Diagonal
		if (index[0] + index[1] == self.gridSize-1):
			found = True
			for i in range(self.gridSize-1):
				if (self.grid[self.gridSize-i-1][i] != self.grid[self.gridSize-i-2][i+1] or self.grid[self.gridSize-i-1][i] == 0):
					found = False
					break
			if (found):
				self.winner = self.turn
				return
			
		
		for i in range(self.gridSize):
			for j in range(self.gridSize):
				if (self.grid[i][j] == 0):
					return

		self.winner = 0
		
