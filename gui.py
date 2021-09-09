from tkinter import *
from main import * 
import sys

window = Tk()
window.config(padx=15, pady=15)

class GUIController:
	def __init__(self):
		self.backgroundColor = "#FFE6E8"
		self.titleColor = "#000000"
		self.frameColor = "#fccfd3"

		self.buttonTextColor = "#0A241C"
		self.buttonColor = "#FA867A"
		self.buttonPressedColor = "#fc4430"
		self.buttonHovorColor = "#fc7365"


	#Displaying the home window, is the first window called
	def disHome(self):
		# Is called at the beginning of each window function to clear the window before we draw on it again
		self.clearWindow()

		# Creating the frames
		topFrame = Frame(window)

		middleFrames = Frame(window)
		middleFrameTop = Frame(middleFrames, padx=15, pady=0)
		middleFrameMid = Frame(middleFrames, padx=15, pady=0)
		bottomFrame = Frame(window)

		# Display the title
		Label(topFrame, text="Tic Tac Toe", bg=self.backgroundColor, fg=self.titleColor, font=("Roboto", 35)).grid(column=0, row=0, pady=15)

		# Display the exit button
		Button(bottomFrame, text="Exit", bg="red", fg=self.buttonTextColor, command=lambda: sys.exit()).grid(column=0, row=0, sticky="ne", pady=15)

		buttonsList = []

		# Displaying Single Player Button
		buttonsList.append(Button(middleFrameTop, text="Single Player", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10))
		buttonsList[-1].grid(column=0, row=0, padx=2, pady=2)

		# Displaying Multiplayer Button
		buttonsList.append(Button(middleFrameTop, text="Multiplayer", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10))
		buttonsList[-1].grid(column=0, row=1, padx=2, pady=2)

		# Displaying Easy Button
		buttonsList.append(Button(middleFrameMid, text="Easy", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10))
		buttonsList[-1].grid(column=0, row=0, padx=2, pady=2)	

		# Displaying Impossible Button
		buttonsList.append(Button(middleFrameMid, text="Impossible", bg=self.buttonColor, fg=self.buttonTextColor,
		 activebackground=self.buttonPressedColor, padx=10, pady=10, width=10))
		buttonsList[-1].grid(column=1, row=0, padx=2, pady=2)

		# Changing the button colors when the mouse is hovored over
		for button in buttonsList:
			self.changeOnHover(button, self.buttonHovorColor, self.buttonColor)

		# Displaying the slider to change the game grid size
		gridSize = 0
		Scale(middleFrames, from_=3, to=20, orient=HORIZONTAL, bg=self.backgroundColor, fg=self.buttonTextColor,
		variable=gridSize, relief=FLAT, activebackground=self.backgroundColor, troughcolor=self.buttonColor).grid(column=0, row=2)

		# Displaying the frames
		topFrame.grid(column=0, row=0)
		middleFrames.grid(column=0, row=1)
		middleFrameTop.grid(column=0, row=0)
		middleFrameMid.grid(column=0, row=1)
		bottomFrame.grid(column=0, row=2)
		# Setting the background colors
		topFrame.configure(bg=self.backgroundColor)
		middleFrames.configure(bg=self.backgroundColor)
		middleFrameTop.configure(bg=self.backgroundColor)
		middleFrameMid.configure(bg=self.backgroundColor)
		bottomFrame.configure(bg=self.backgroundColor)
		window.configure(bg=self.backgroundColor)

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


	# Clears the entire window
	def clearWindow(self):
		for widget in window.winfo_children():
			widget.destroy()