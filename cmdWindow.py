import tkinter as tk
import time
class CommandWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="Command Call", font=("Courier", 15))
        self.label.pack()
        self.commandCall = tk.Entry(self)
        self.commandCall.pack()
        self.label = tk.Label(self, text="Command Action",  font=("Courier", 15))
        self.label.pack()
        self.commandAction = tk.Entry(self)
        self.commandAction.pack()
        self.submit = tk.Button(self, text="Submit Command",  font=("Courier", 15),command=self.addCommand)
        self.submit.pack()

    def addCommand(self):
        commandCall = self.commandCall.get()
        commandAction = self.commandAction.get()
        print("Command Call: ".format(commandCall))
        print("Command Action".format(commandAction))
        f = open("cmds/index", "a+")
        f.write(commandCall + "\n")
        f.write(commandAction + "\n")
        f.close()
        time.sleep(1)
        self.destroy()

app = CommandWindow()
app.title("Add command")
app.mainloop()
