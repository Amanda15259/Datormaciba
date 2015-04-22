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
    s = e.get()
    for i in range(k):
        print s[:i]
        w.itemconfig(t, text=s[:i])
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

def funC():
    k = 16
    s = e3.get()
    for i in range(k):
        print s[:i]
        w.move(t, 10, 0)
        w.update
        time.sleep(0.3)
    
v = tk.StringVar()
v.set("0123456789ABCDEF")

e2 = tk.Entry(root, textvariable=v)

b = tk.Button(root, text="Spied", command=funA)
b.pack() 
 
b2=tk. Button (root , text="Spied", command =funB)
b2.pack ()
e2.pack()

e3 = tk.Entry(root, textvariable=v)
b3 = tk.Button(root, text="Spied", command=funC)
b3.pack()
e3.pack()


root.mainloop()
