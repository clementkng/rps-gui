import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there.pack(side="top")

        self.bye_there = tk.Button(self)
        self.bye_there["text"] = "Bye World\n(click me)"
        self.bye_there.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

# create the application
root = tk.Tk()
myapp = App(master=root)

#
# here are method calls to the window manager class
#
myapp.master.title("My Tkinter Application")
myapp.master.maxsize(1000, 600)

# start the program
myapp.mainloop()