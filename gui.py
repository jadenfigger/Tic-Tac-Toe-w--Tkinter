from tkinter import *
from main import * 
import sys

window = Tk()
window.config(padx=15, pady=15)

class GUIController:
	def __init__(self):
		self.backgroundColor = "#FFE6E8"
		self.titleColor = "#000000"

		self.buttonTextColor = "#0A241C"
		self.buttonColor = "#FA867A"
		self.buttonPressedColor = "#fc8174"
		self.buttonHovorColor = "#fc7365"

		self.frameColor = "#f2f2f2"

	#Displaying the home window, is the first window called
	def disHome(self):
		# Is called at the beginning of each window function to clear the window before we draw on it again
		self.clearWindow()

		# Creating the frames
		rightFrame = Frame(window)
		topFrame = Frame(window)
		middleFrame = Frame(window)

		# Display the title
		Label(topFrame, text="Tic Tac Toe", bg=self.backgroundColor, fg=self.titleColor).grid(column=0, row=0)

		buttonsList = []

		# Display the exit button
		Button(rightFrame, text="Exit", bg="red", fg=self.buttonTextColor, command=lambda: sys.exit()).grid(column=0, row=0, sticky="ne")

		# Display the options
		buttonsList.append(Button(middleFrame, text="Single Player", bg=self.buttonColor, fg=self.buttonTextColor, activebackground=self.buttonPressedColor, padx=10, pady=10))
		buttonsList[-1].grid(column=0, row=0, sticky="nsew")
		buttonsList.append(Button(middleFrame, text="Multiplayer", bg=self.buttonColor, fg=self.buttonTextColor, activebackground=self.buttonPressedColor, padx=10, pady=10))
		buttonsList[-1].grid(column=1, row=0, sticky="nsew")
		buttonsList.append(Button(middleFrame, text="Easy", bg=self.buttonColor, fg=self.buttonTextColor, activebackground=self.buttonPressedColor, padx=10, pady=10))
		buttonsList[-1].grid(column=0, row=1, sticky="nsew")	
		buttonsList.append(Button(middleFrame, text="Impossible", bg=self.buttonColor, fg=self.buttonTextColor, activebackground=self.buttonPressedColor, padx=10, pady=10))
		buttonsList[-1].grid(column=1, row=1, sticky="nsew")

		for button in buttonsList:
			self.changeOnHover(button, self.buttonHovorColor, self.buttonColor)

		# Displaying the frames
		rightFrame.grid(column=1, row=0)
		topFrame.grid(column=0, row=0)
		middleFrame.grid(column=0, row=1)
		# Setting the background colors
		rightFrame.configure(bg=self.backgroundColor)
		topFrame.configure(bg=self.backgroundColor)
		middleFrame.configure(bg=self.backgroundColor)
		window.configure(bg=self.backgroundColor)

		window.mainloop()
  

	# function to change properties of button on hover
	def changeOnHover(self, button, colorOnHover, colorOnLeave):
		# adjusting backgroung of the widget
		# background on entering widget
		button.bind("<Enter>", func=lambda e: button.config(
			background=colorOnHover))
	
		# background color on leving widget
		button.bind("<Leave>", func=lambda e: button.config(
			background=colorOnLeave))


	# Clears the entire window
	def clearWindow(self):
		for widget in window.winfo_children():
			widget.destroy()