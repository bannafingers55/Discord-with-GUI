import tkinter as tk
import os


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="GUI Python Discord Client", font=("Courier", 30), bg="#d9ff93")
        self.creds = tk.Label(self, text="Please enter the file path to your discord credentials", font=("Courier", 13), bg="#d9ff93")
        self.path = tk.Entry(self)
        self.submitCreds = tk.Button(self, text="Submit File Path", command=self.getCreds)
        self.output = tk.Label(self, text="Sumbit a file path to your credentials first.")
        self.label.pack()
        self.creds.pack(side=tk.LEFT)
        self.path.pack(side=tk.LEFT)
        self.submitCreds.pack(side=tk.BOTTOM)
        self.output.pack(side=tk.BOTTOM)

    def getCreds(self):
        try:
            f=open(self.path.get(), "r")
            content = f.read()
            print(content)
            f.close()
            if len(content) == 0:
                self.output.configure(text="Hmm, your credentials don't seem quite right, check out our website to find out how to submit them")
                return

            f = open("path.path", "w")
            f.write(path)
            f.close()
            token = content
            self.output.configure(text="We have your credentials, now we need to try and establish the connection to bot")
            import run.py


        except Exception as e:
            print(e)
            self.output.configure(text="That path doesn't seem to lead to your credentials, remember to only give the path from your current directory")






app = Window()
app.title("Discord GUI")
app.configure(background="#d9ff93")
app.mainloop()
