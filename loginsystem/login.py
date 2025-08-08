from tkinter import *
# from tkinter import Tk, Label, Entry, Button, StringVar, Frame
from tkinter import messagebox
import os

def login():
    user=username.get()
    code=password.get()

    if user=="Opik" and code=="998":
        root=Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="aqua")
        root.resizable(False,False)

        

def main_screen():

    global screen
    global username
    global password

    screen = Tk()
    screen.geometry("1280x270+150+80")
    screen.configure(bg="red")

    #icon
    # image_icon = PhotoImage(file="icon.png")
    # screen.iconphoto(False,image_icon)

    screen.title("Login System")

    IbITitle = Label(text="Login System",font=("arial",50,'bold'),fg="white",bg="black")
    IbITitle.pack(pady=50)

    bordercolor = Frame(screen,bg="black",width=800,height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor,bg="aqua",width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe,text="Username",font=("arial",30,'bold'),bg="aqua").place(x=100,y=50)
    Label(mainframe,text="Password",font=("arial",30,'bold'),bg="aqua").place(x=100,y=150)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30))
    entry_username.place(x=400,y=50)
    entry_password = Entry(mainframe,textvariable=password,width=12,bd=2,font=("arial",30),show='*')
    entry_password.place(x=400,y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(mainframe,text="Login",height="2",width=23,bg="green",fg="white",bd=0,command=login).place(x=100,y=250)
    Button(mainframe,text="Reset",height="2",width=23,bg="blue",fg="white",bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Exit",height="2",width=23,bg="red",fg="white",bd=0,command=screen.destroy).place(x=500,y=250)


    screen.mainloop()

main_screen()

