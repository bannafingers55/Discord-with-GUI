import tkinter as tk
import os
import bot



class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="GUI Python Discord Client", font=("Courier", 40), bg="#d9ff93")
        self.label.pack()
        self.button = tk.Button(self, text = "CONNECT TO DISCORD", font=("Courier", 30), command=self.connect)
        self.button.pack()
        self.addCmd = tk.Button(self , text="Add a command", font=("Courier", 30), command=self.addCmdWin)
        self.addCmd.pack()

    def addCmdWin(self):
        import cmdWindow

    def addCmd(self):
        self.addCmdWin.destory()
        print("SUBMITTING")
        self.commandCall = self.commandCall.get()
        print(self.commandCall)
        self.commandAction = self.commandAction.get()
        print(self.commandAction)

    def connect(self):
        self.destroy()
        import run
    #def getCreds(self):
        #try:
            #f=open(self.path.get(), "r")
            #content = f.read()
            #print(content)
            #f.close()
            #if len(content) == 0:
                #self.output.configure(text="Hmm, your credentials don't seem quite right, check out our website to find out how to submit them")
                #return

            #f = open("path.txt", "w")
            #f.write(path)
            #f.close()
            #token = content
            #self.output.configure(text="We have your credentials, now we need to try and establish the connection to bot")
            #import run.py


        #except Exception as e:
            #print(e)
            #self.output.configure(text="That path doesn't seem to lead to your credentials, remember to only give the path from your current directory")

app = Window()
app.title("Discord GUI")
app.configure(background="#d9ff93")
app.mainloop()
