#Autors:Amanda Beinarovica
#Fails:Pogas

import Tkinter as tk
import time
root= tk.Tk()
root.title("Mana tafele")

w = tk.Canvas(root, width=600, height=400, \
              bg="#456", relief="sunken", border=10 )
w.pack()
t = w.create_text(50, 100, text="Amanda" ,\
                  font="Courier 40 bold", fill ="#ffc", anchor="nw")

def funA():
    k = 7
    s = e2.get()
    for i in range(k):
        print s[:i]
        w.itemconfig(t, text=s[:i])
        time.sleep(0.1)
        
v = tk.StringVar()
v.set("Amanda")

def funB():
    k = 7
    s = e2.get()
    for i in range(k+2):
            w.itemconfig(t, text=s[i:])
            w.update()
            time.sleep(0.1)
v = tk.StringVar()
v.set("Amanda")

e2 = tk.Entry(root, textvariable=v)
e2.pack()

b = tk.Button(root, text="Raksti", command =funA)
b.pack()
b2 = tk.Button(root, text="Dzees", command =funB)
b2.pack()

root.mainloop()


