import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Time Clock")

def time():
    string = strftime('%H:%M:%S %p \n%D')
    lable.config(text=string)
    lable.after(1000,time)

lable = tk.Label(root,font=("calibri", 50, "bold"),background='yellow',foreground='black')

time()
lable.pack()
root.mainloop()
