from tkinter import *
import sys

""" This program when opened will prompt a user to create a login. After creating a login, the user will be asked to log in.
When the user enters the correct information, they will see the password book. It will have a widget that shows all account
titles, and they can choose to add, edit, or view  existing objects. Existing objects will all have username, password, and a URL.
It will also show the date the information was last changed. """

class MyApp(Frame):
	""" This class will store all of the main program settings. Dimensions and styling.	"""

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		
	def create_widgets(self):
		self.accounts_label = Label(self, text="Accounts: ", fg = "black")
		self.accounts_label.pack()
		self.account_window = Listbox(self)
		self.account_window.pack()
		self.account_window.insert(END, "A list entry")
		
	def say_hi(self):
		print("Hi there, everyone!")

if __name__ == '__main__':
	root = Tk()
	app = MyApp(master=root)
	
	for item in ["one", "two", "three", "four"]:
		app.account_window.insert(END, item)
	app.mainloop()
		