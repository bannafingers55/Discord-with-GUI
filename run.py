import os
from bot import FilterBot
import tkinter as tk
import time

if os.path.isdir("data/") == False:
	print("Creating data directory")
	os.mkdir("data/")

try:
	f = open("data/token.data", "r")
	content = f.read()
	f.close()
except:
	f = open("data/token.data", "w+")
	window = tk.Tk()
	label = tk.Label(window, text="ENTER YOUR TOKEN")
	label.pack()
	entry = tk.Entry(window)
	entry.pack()
	def getToken():
		token = entry.get()
		f.write(token)
		f.close()
		print("Token saved")
		time.sleep(1)
		window.destroy()

	button = tk.Button(window, text="submit", command=getToken)
	button.pack()
	window.mainloop()


print("Booting...")

b = FilterBot()
b.run()
