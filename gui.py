from tkinter import *
from tkinter import font
from main import * 
import sys
import TicTacToe

window = Tk()
window.config(padx=15, pady=15)

class GUIController:
	def __init__(self):
		self.backgroundColor = "#FA867A"
		self.titleColor = "#000000"
		self.frameColor = "#FFE6E8"

		self.buttonTextColor = "#0A241C"
		self.buttonColor = "#FA867A"
		self.buttonPressedColor = "#fc4430"
		self.buttonHovorColor = "#fc7365"

		self.sBtn = None
		self.mBtn = None
		self.eBtn = None
		self.iBtn = None

		self.tictactoe = None
		self.buttonList = []

		self.gameMode = None
		self.diff = None

		self.sliderValue = 3
		self.gridSlider = 3

	#Displaying the home window, is the first window called
	def disHome(self):
		# Is called at the beginning of each window function to clear the window before we draw on it again
		self.clearWindow()

		# Creating the frames
		topFrame = Frame(window)
		middleFrames = Frame(window, pady=10, relief=RIDGE, bd=2)
		middleFrameTop = Frame(middleFrames, padx=15, pady=0)
		middleFrameMid = Frame(middleFrames, padx=15, pady=0)
		middleFrameBot = Frame(middleFrames, padx=15, pady=0)
		bottomFrame = Frame(window)

		# Display the title
		Label(topFrame, text="Tic Tac Toe", bg=self.backgroundColor, fg=self.titleColor, font=("Roboto", 35)).grid(column=0, row=0, pady=15)

		buttonsList = []

		# Displaying Single Player Button
		buttonsList.append(Button(middleFrameTop, text="Single Player", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10, relief=GROOVE,
		 command=lambda x="s": self.setGameMode(x)))
		buttonsList[-1].grid(column=0, row=0, padx=2, pady=2)
		self.sBtn = buttonsList[-1]

		# Displaying Multiplayer Button
		buttonsList.append(Button(middleFrameTop, text="Multiplayer", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10, relief=GROOVE,
		 command=lambda x="m": self.setGameMode(x)))
		buttonsList[-1].grid(column=0, row=1, padx=2, pady=2)
		self.mBtn = buttonsList[-1]

		# Displaying Easy Button
		buttonsList.append(Button(middleFrameMid, text="Easy", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10, relief=GROOVE,
		 state=DISABLED if self.gameMode==None else NORMAL), command=lambda x="e": self.activateDiffBtns(x))
		buttonsList[-1].grid(column=0, row=0, padx=2, pady=2)	
		self.eBtn = buttonsList[-1]

		# Displaying Impossible Button
		buttonsList.append(Button(middleFrameMid, text="Impossible", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10, relief=GROOVE,
		 state=DISABLED if self.gameMode==None else NORMAL), command=lambda x="i": self.activateDiffBtns(x))
		buttonsList[-1].grid(column=1, row=0, padx=2, pady=2)
		self.iBtn = buttonsList[-1]

		# Changing the button colors when the mouse is hovored over
		for button in buttonsList:
			self.changeOnHover(button, self.buttonHovorColor, self.buttonColor)
		

		# Displaying the slider to change the game grid size
		Label(middleFrameBot, text="Enter Board Size:", bg=self.frameColor, fg=self.titleColor,).grid(column=0, row=0)
		
		self.gridSlider = Scale(middleFrameBot, from_=3, to=21, orient=HORIZONTAL, bg=self.frameColor, fg=self.buttonTextColor,
		activebackground=self.backgroundColor, troughcolor=self.buttonColor,
		 variable=self.sliderValue, command=self.updateSliderValue)
		self.gridSlider.grid(column=0, row=1, sticky="nsew", padx=20, pady=2)

		self.gridSlider.config()

		# Display the exit button
		Button(bottomFrame, text="Exit", bg="red", fg=self.buttonTextColor, width=10, command=lambda: sys.exit(), relief=GROOVE).grid(column=0, row=0, padx=5, pady=15, sticky="nsew")

		# Displaying the start button
		sB = Button(bottomFrame, text="Start", bg="#4ABF36", activebackground="#62FA47", fg=self.buttonTextColor, 
		width=10, relief=GROOVE, command=lambda: self.disGameWindow((self.gridSlider.get(), True)))
		sB.grid(column=1, row=0, padx=5, pady=15, sticky="nsew")
		self.changeOnHover(sB, "#56F222", "#4ABF36")

		# Displaying the frames
		topFrame.grid(column=0, row=0)
		middleFrames.grid(column=0, row=1)
		middleFrameTop.grid(column=0, row=0)
		middleFrameMid.grid(column=0, row=1)
		middleFrameBot.grid(column=0, row=2)
		bottomFrame.grid(column=0, row=2)
		# Setting the background colors
		topFrame.configure(bg=self.backgroundColor)
		middleFrames.configure(bg=self.frameColor)
		middleFrameTop.configure(bg=self.frameColor)
		middleFrameMid.configure(bg=self.frameColor)
		middleFrameBot.configure(bg=self.frameColor)
		bottomFrame.configure(bg=self.backgroundColor)
		window.configure(bg=self.backgroundColor)

		window.mainloop()
  
	# Displaying the game window with proper grid size
	def disGameWindow(self, p):
		gridSize = p[0]
		initial = p[1]

		if (initial):
			self.tictactoe = TicTacToe.ttt(gridSize)

			if (self.gameMode == None):
				messagebox.showinfo("Error", "Please select a gamemode.")
				self.disHome()
			elif (self.gameMode == "m" and self.diff == None):
				messagebox.showinfo("Error", "Please select a game difficulty when playing single player.")
				self.disHome()

		# Clear the current window
		self.clearWindow()

		topFrame = Frame(window)
		gameFrame = Frame(window, padx=15, pady=15)
		gridBackgroundFrame = Frame(gameFrame)
		bottomFrame = Frame(window)

		frames = []
		self.buttonList = []
		for i in range(gridSize):
			(i)
			frames.append([])
			self.buttonList.append([])
			for j in range(gridSize):
				px = ((j != 0) * 2,  (j != gridSize-1) * 2)
				py = ((i != 0) * 2,  (i != gridSize-1) * 2)
				frames[i].append(Frame(gridBackgroundFrame, bg=self.frameColor,
				 width=int(400/gridSize), height=int(400/gridSize)))
				frames[i][j].pack_propagate(False)
				frames[i][j].grid(row=i, column=j, padx=px, pady=py)

				self.buttonList[i].append(Button(frames[i][j], text=self.tictactoe.grid[i][j], bg=self.frameColor, relief=FLAT,
				command=lambda p=(i, j): self.buttonClicked(p)))
				self.buttonList[i][-1].pack(expand=True, fill=BOTH)


		# Displaying the score and who's turn it is
		Label(topFrame, text="Player", bg=self.frameColor, fg=self.titleColor, padx=5).grid(column=0, row=0)
		Label(topFrame, text="Computer", bg=self.frameColor, fg=self.titleColor, padx=5).grid(column=1, row=0)

		# Displaying the home button
		Button(bottomFrame, text="Exit", bg="red", fg=self.buttonTextColor, width=10,
		 command=lambda: sys.exit(), relief=GROOVE).grid(column=0, row=0, padx=5, pady=15, sticky="nsew")

		# Displaying the start button
		sB = Button(bottomFrame, text="Home", bg="#4ABF36", activebackground="#62FA47", fg=self.buttonTextColor,
		 width=10, relief=GROOVE, command=self.disHome)
		sB.grid(column=1, row=0, padx=5, pady=15, sticky="nsew")
		self.changeOnHover(sB, "#56F222", "#4ABF36")


		topFrame.grid(column=0, row=0, pady=15)
		gameFrame.grid(column=0, row=1)
		gridBackgroundFrame.grid(column=0, row=0)
		bottomFrame.grid(column=0, row=2, pady=5, sticky="n")
		# Drawing Background 
		topFrame.configure(bg=self.backgroundColor)
		gameFrame.configure(bg=self.frameColor)
		gridBackgroundFrame.configure(bg=self.buttonColor)
		bottomFrame.configure(bg=self.backgroundColor)

		window.mainloop()
		

	# Function to change properties of button on hover
	def changeOnHover(self, button, colorOnHover, colorOnLeave):
		# Adjusting backgroung of the widget
		# Background on entering widget
		button.bind("<Enter>", func=lambda e: button.config(
			background=colorOnHover))
	
		# Background color on leving widget
		button.bind("<Leave>", func=lambda e: button.config(
			background=colorOnLeave))


	def buttonClicked(self, index):
		self.buttonList[index[0]][index[1]]['font'] = self.findFontSize(self.tictactoe.gridSize)
		self.buttonList[index[0]][index[1]]['text'] = self.tictactoe.turn

		self.tictactoe.updateGameGrid(index)


	# Clears the entire window
	def clearWindow(self):
		for widget in window.winfo_children():
			widget.destroy()

	def findFontSize(self, size):
		s = 22
		if (size==3): s = 80
		elif (5 <= size <= 9): s = 40
		elif (11 <= size <= 15): s = 25
		else: s = 18

		f = font.Font(family="Roboto", size=s)
		return f

	def updateSliderValue(self, variable):
		temp = int(variable)
		if (temp%2==0):
			self.gridSlider.set(temp+1)

	def activateDiffBtns(self, d):
		self.diff = d

	def setGameMode(self, m):	
		self.gameMode = m

		if (self.gameMode == "s"):
			self.eBtn['state'] = NORMAL
			self.iBtn['state'] = NORMAL

		if (self.gameMode == "s"):
			self.sBtn['bg'] = self.buttonPressedColor
		else:
			self.mBtn['bg'] = self.buttonPressedColor