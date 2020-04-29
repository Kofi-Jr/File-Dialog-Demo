"""
Program: filedialogdemo.py
Author: Kofi
Excercise on pages 278 - 279
from Chapter 8
"""

from breezypythongui import EasyFrame
import tkinter.filedialog


class FileDialogDemo(EasyFrame):
	""" Demonstrates the uses of a file dialog."""

	def __init__(self):
		"""Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "File Dialog Demo")
		self.setResizable(False)


		self.outputArea = self.addTextArea(text = "", 
										   row = 0, 
										   column = 0, 
										   width = 80, 
										   height = 15)

		self.addButton(text = "Open", 
					   row = 1, 
					   column = 0, 
					   command = self.openFile)

	# Event handling method.
	def openFile(self):
		""" Pops up an open file dialog, and if is selected, displayes its text in the text area and its pathname in the title bar."""
		fList = [("Python files", "*.py"), ("Text files", "*.txt"), ("Java file", "*.java")]

		fileName = tkinter.filedialog.askopenfilename(parent = self, 
													  filetypes = fList)

		if fileName != "":
			file = open(fileName, 'r')
			text = file.read()
			file.close()
			self.outputArea.setText(text)
			self.setTitle(fileName)
			self.outputArea["state"] = "disabled"

				
# Defintion of the main() function
def main():
	FileDialogDemo().mainloop()

# Global call to the main() function
main()



