import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def waktu():
    string = strftime('%H:%M:%S %p %D')
    label.config(text=string)
    label.after(1000,waktu)

label = tk.Label(root, font=("calibri", 50, "bold"), background='black', foreground="aqua")
label.pack(anchor="center")

waktu()

root.mainloop()