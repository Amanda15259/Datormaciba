#-*- coding: utf-8 -*-
# Autors: Amanda Beinarovica

import Tkinter as tk
root= tk.Tk();
root.title( " Mana Tafele " )
v = tk.StringVar()
w = tk.Canvas(root, width=600, height=400, \
    bg="#456", relief="sunken", border=10 )
w.pack()

def fun():
    e = tk.Entry(root, textvariable=v)
    e.pack()
    w.itemconfig(t, text=e.get())

b = tk.Button(root, text="Spied", command=fun)
b.pack()                  
t = w.create_text(50, 100,anchor='sw',text=" 2+2=4 ", \
    font="Courier 40 italic", fill ="#ffc")
w.mainloop()



