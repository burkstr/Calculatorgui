import tkinter as tk
#from tkinter.simpledialog import askinteger
from tkinter import *
#from tkinter import messagebox
top = Tk()
top.geometry("500x700")
answer = Text(width=35, height=2)
answer.place(x=100, y=100)
def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)
        else:
            answer.insert(tk.INSERT, x)
    except:
        answer.delete(1.0, END)
B1 = Button(top, text="1", width=10, height=5, bg="red", command=lambda: show("1"))
B1.place(x=100, y=150)
B2 = Button(top, text="2", width=10, height=5, bg="red", command=lambda: show("2"))
B2.place(x=200, y=150)
B3 = Button(top, text="3", width=10, height=5, bg="red", command=lambda: show("3"))
B3.place(x=300, y=150)
B3 = Button(top, text="/", width=10, height=5, bg="red", command=lambda: show("/"))
B3.place(x=400, y=450)
B4 = Button(top, text="*", width=10, height=5, bg="red", command=lambda: show("*"))
B4.place(x=400, y=350)
B5 = Button(top, text="-", width=10, height=5, bg="red", command=lambda: show("-"))
B5.place(x=400, y=250)
B6 = Button(top, text="+", width=10, height=5, bg="red", command=lambda: show("+"))
B6.place(x=400, y=150)
B7 = Button(top, text="4", width=10, height=5, bg="red", command=lambda: show("4"))
B7.place(x=100, y=250)
B8 = Button(top, text="5", width=10, height=5, bg="red", command=lambda: show("5"))
B8.place(x=200, y=250)
B9 = Button(top, text="6", width=10, height=5, bg="red", command=lambda: show("6"))
B9.place(x=300, y=250)
B10 = Button(top, text="7", width=10, height=5, bg="red", command=lambda: show("7"))
B10.place(x=100, y=350)
B12 = Button(top, text="8", width=10, height=5, bg="red", command=lambda: show("8"))
B12.place(x=200, y=350)
B13 = Button(top, text="9", width=10, height=5, bg="red", command=lambda: show("9"))
B13.place(x=300, y=350)
B14 = Button(top, text="0", width=25, height=5, bg="red", command=lambda: show("0"))
B14.place(x=100, y=450)
B15 = Button(top, text=".", width=10, height=5, bg="red", command=lambda: show("."))
B15.place(x=300, y=450)
B15 = Button(top, text="=", width=10, height=5, bg="green", command=lambda: show("="))
B15.place(x=200, y=550)

top.mainloop()