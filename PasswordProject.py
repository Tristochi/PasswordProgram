from tkinter import *
import sys
import sqlite3

accounts = []
users = []
passwords = []

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
		self.refresh()
		
		
	def create_widgets(self):
		self.accounts_label = Label(self, text="Accounts: ", fg = "black")
		self.accounts_label.pack()
		self.lb_values = Variable(value=accounts)
		
		self.account_window = Listbox(self, listvariable = self.lb_values)
		self.account_window.pack(padx = 5, pady = 5, side = LEFT)
		
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
		global title
		title = Entry(new_pw)
		title.grid(row=0, column=1, padx=10, pady=10)
	
		# Label and entry for Username
		Label(new_pw, text="Username: ", fg="black").grid(row=1, padx = 5, pady = 10)
		global user
		user = Entry(new_pw)
		user.grid(row=1, column=1, padx = 10, pady = 10)
		
		# Label and entry for Password
		Label(new_pw, text="Password: ", fg="black").grid(row = 2, padx = 5, pady = 10)
		global pw
		pw = Entry(new_pw)
		pw.grid(row = 2, column = 1, padx = 10, pady = 10)
		
		# Add button
		Button(new_pw, text="Apply", fg="black", command=lambda: self.update(new_pw)).grid(row = 3, pady = 20)
		
		# Cancel button
		Button(new_pw, text="Cancel", fg="black", command=lambda:new_pw.destroy()).grid(row=3, column=1, padx = 10, pady = 20)
	
	
	def update(self, master):

		c.execute('CREATE TABLE IF NOT EXISTS passwords(accountName TEXT, username TEXT, password TEXT)')
		
		acc_input = title.get()
		usr_input = user.get()
		pass_input = pw.get()
		
		accounts.append(acc_input)
		users.append(usr_input)
		passwords.append(pass_input)
		
		acc_index = len(accounts) - 1
		user_index = len(users) - 1
		pass_index = len(passwords) - 1
		
		c.execute('INSERT INTO passwords(accountName, username, password) VALUES(?, ?, ?)', (accounts[acc_index], users[user_index], passwords[pass_index]))
		conn.commit()
		
		self.account_window.insert(END, acc_input)
		
		master.destroy()				
		
		
	def refresh(self):
		 c.execute("SELECT accountName FROM passwords")
		 
		 for tup in c.fetchall():
			for usr in tup:
				self.account_window.insert(END, usr)


if __name__ == '__main__':
	conn = sqlite3.connect('Pbook.db')
	c = conn.cursor()
	root = Tk()
	app = MyApp(master=root)

	
	
	app.mainloop()
		