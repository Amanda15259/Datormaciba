# -*- coding: utf-8 -*-
'''Fails:" 260.py
Autors: Amanada Beinarovica
Veidojam Tafeliar uzrakstu: 01234567898ABCDEF
Programma uz tafeles tekstu raksta nesteidzoties: pe vienam burtam pussekundee
'''
import Tkinter as tk
import time
root= tk.Tk()
root.title("Mana Tafele ar dinamisku tekstu")

w = tk.Canvas(root, width=600, height=400, \
bg="#456", relief="sunken", border=10 )
w.pack()

t = w.create_text(50, 100, text="2 + 2 = \n4", \
font="Courier 40 bold", fill ="#ffc", anchor="nw")

def funA():
    k = 16
    s = e2.get()
    for i in range(k):
        print s[:i]
        w.itemconfig(t, text=s[i:])
        w.update()
        time.sleep(0.5)

def funB():
    k=16
    s = e2.get()
    w.update()
    for i in range(k):
        s[i] = ' '
        w.itemconfig(t, text= s)
        w.update
        time.sleep(0.1)
    
    
v = tk.StringVar()
v.set("0123456789ABCDEF")

e2 = tk.Entry(root, textvariable=v)

b2=tk. Button (root , text="Spied", command =funB)
b2.pack ()
e2.pack()

b = tk.Button(root, text="Speid", command=funA)
b.pack()

root.mainloop()
