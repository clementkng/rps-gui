import tkinter

window = tkinter.Tk()
window.title("RPS-AI GUI")
# I am fine with the original Tkinter icon, so I will leave it in

# Create a label widget called 'lbl'
lbl = tkinter.Label(window, text="Human")
# Create a text entry widget to be called 'ent'
# ent = tkinter.Entry(window)

# Create a label widget called 'lbl'
lbl1 = tkinter.Label(window, text="Computer")
# Create a text entry widget to be called 'ent'
# ent1 = tkinter.Entry(window)
# Create a button widget called btn

scorelist = ["win", "tie", "win"]
for s in scorelist:
    l = tkinter.Label(window,text=s)
    l.pack(fill=tkinter.X)
vslbl = tkinter.Label(window, text="VS.")
btn = tkinter.Button(window, text="Login", fg="#a1dbcd", bg="#383a39")

# photo = tkinter.PhotoImage(file="blocks1.gif")
# w = tkinter.Label(window, image=photo)
# w.pack()

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple']
# for c in colors:
#     b = tkinter.Button(text=c,bg=c)
#     b.pack(fill=tkinter.X) # aligned along X axis, or Y axis

# presses=0
# def addClick():
#     global presses
#     presses += 1
#     lblp.configure(text=presses)
# lblp = tkinter.Label(window, text=presses)
# lblp.pack()

# def callback():
#     print("Button clicked!")
# btnclick = tkinter.Button(window, text="Click Me", command = addClick)
# btnclick.pack()

# pack (add) the widget to the window
lbl.pack(side = tkinter.LEFT)
# ent.pack()
lbl1.pack(side = tkinter.RIGHT)
# ent1.pack()
btn.pack(side = tkinter.BOTTOM)
vslbl.pack()

window.configure(background="#a1dbcd")


window.mainloop()