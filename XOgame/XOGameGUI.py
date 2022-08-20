import tkinter as tk
from tkinter import messagebox as mb

screen = tk.Tk()
screen.title("XOGame")
screen.eval('tk::PlaceWindow . center')
screen.resizable(False, False)
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
x = int((screen_width / 2) - 300)
y = int((screen_height / 2) - 350)
screen.geometry(f"600x600+{x}+{y}")
screen.config(background="Black", cursor="target", padx=20)
name1 = ""
name2 = ""
global m
global c
c = 1
m = 0


def action():
    name1 = entry1.get()
    name2 = entry2.get()
    if name1 == "name of player1" or name2 == "name of player2":
        mb.showerror(title="No Inputs", message="You must Enter two names")
        return
    screen.destroy()
    screen2 = tk.Tk()
    screen2.title("XOGame")
    screen2.geometry(f"600x600+{x}+{y}")
    screen2.config(background="Black", cursor="target")
    player1 = tk.Label(text=f"{name1}")
    player1.config(fg='Red', bg="Black", font=('Helvatical bold', 20))
    player1.place(x=30, y=20)
    player2 = tk.Label(text=f"{name2}")
    player2.config(fg='Red', bg="Black", font=('Helvatical bold', 20))
    player2.place(x=460, y=20)

    def click(t):
        global m
        global c
        if m == 0:
            t.config(text="X", state="disabled")
            m = 1
            c += 1
        elif m == 1:
            t.config(text="O", state="disabled")
            m = 0
            c += 1
        flist = [bt1["text"], bt2["text"], bt3["text"], bt4["text"], bt5["text"], bt6["text"], bt7["text"], bt8["text"],
                 bt9["text"]]
        for n in range(0,20,3):
            help=[0,1,2,3,4,5,6,7,8,0,3,6,1,4,7,2,5,8,0,4,8,2,4,6]
            if flist[help[n]]==flist[help[n+1]]==flist[help[n+2]] and flist[help[n]]!="":
                if flist[help[n]] == "X":
                    mb.showinfo(title="Congrats", message=f"Player (X) : {name1} WOn")
                    screen.destroy()
                else:
                    mb.showinfo(title="Congrats", message=f"Player (O) : {name2} WOn")
                    screen.destroy()




    bt1 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt1))
    bt1.place(x=205, y=200)
    bt2 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt2))
    bt2.place(x=270, y=200)
    bt3 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt3))
    bt3.place(x=335, y=200)
    bt4 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt4))
    bt4.place(x=205, y=270)
    bt5 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt5))
    bt5.place(x=270, y=270)
    bt6 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt6))
    bt6.place(x=335, y=270)
    bt7 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt7))
    bt7.place(x=205, y=340)
    bt8 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt8))
    bt8.place(x=270, y=340)
    bt9 = tk.Button(bg="Grey", disabledforeground="Blue", bd=5, width=6, height=3, font=(15),
                    command=lambda: click(bt9))
    bt9.place(x=335, y=340)


# --------------------------------------------------------------
entry1 = tk.Entry(width=20)
entry1.insert(index="1", string="name of player1")
entry1.pack(side="left")
entry1.focus()
entry2 = tk.Entry(width=20)
entry2.insert(index="1", string="name of player2")
entry2.pack(side="right")
entry2l = tk.Label(text="X", font=40, bg="black", fg="white")
entry2l.place(x=55, y=250)
entry1l = tk.Label(text="O", font=40, bg="black", fg="white")
entry1l.place(x=490, y=250)
button = tk.Button()
button.config(text="Start Game!", command=action, height=10)
button.place(x=240, y=300)

screen.mainloop()
