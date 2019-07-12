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
		self.master.title("Password Book")
		self.account_list = {"account": [], "username": [], "password": []}
		self.accounts = []
		self.users = []
		self.passwords = []
		
		
	def create_widgets(self):
		self.accounts_label = Label(self, text="Accounts: ", fg = "black")
		self.accounts_label.pack()
		self.account_window = Listbox(self)
		self.account_window.pack(padx = 5, pady = 5, side = LEFT)
		# self.account_window.insert(END, "A list entry")3
		
		self.add = Button(self, text="New Account", fg= "black", command=self.add_new)
		self.add.pack(padx = 5, pady = 5, side = LEFT)


	def add_new(self):
		new_pw = Toplevel()
		new_pw.title("Add Account: ")
		global title
		global user
		global pw
		# Label and entry for account title
		Label(new_pw, text="Account Title: ", fg = "black").grid(row=0, padx=5, pady =10)
		title = Entry(new_pw)
		title.grid(row=0, column=1, padx=10, pady=10)
	
		# Label and entry for Username
		Label(new_pw, text="Username: ", fg="black").grid(row=1, padx = 5, pady = 10)
		user = Entry(new_pw)
		user.grid(row=1, column=1, padx = 10, pady = 10)
		
		# Label and entry for Password
		Label(new_pw, text="Password: ", fg="black").grid(row = 2, padx = 5, pady = 10)
		pw = Entry(new_pw)
		pw.grid(row = 2, column = 1, padx = 10, pady = 10)
		
		# Add button
		Button(new_pw, text="Apply", fg="black", command=lambda: self.update(new_pw)).grid(row = 3, pady = 20)
		
		# Cancel button
		Button(new_pw, text="Cancel", fg="black", command=lambda:new_pw.destroy()).grid(row=3, column=1, padx = 10, pady = 20)
	
	
	def update(self, master):
		self.accounts.append(title.get())
		print(self.accounts)
		self.users.append(user.get())
		print(self.users)
		self.passwords.append(pw.get())
		print(self.passwords)

		
		for values in range(len(self.accounts)):
			self.account_list["account"].append(self.accounts[values])
			self.account_window.insert(END, self.accounts[values])
		
		master.destroy()				
		
		

if __name__ == '__main__':
	root = Tk()
	app = MyApp(master=root)
	
	
	app.mainloop()
		