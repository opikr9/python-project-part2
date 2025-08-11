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

        # kasir
        def Reset():
            entry_Donat.delete(0,END)
            entry_Mendoan.delete(0,END)
            entry_Rames.delete(0,END)
            entry_lolipop.delete(0,END)
            entry_esteh.delete(0,END)
            entry_Coklat.delete(0,END)
            entry_Eskrim.delete(0,END)

        def Total():
            try:a1=int(Donat.get())
            except: a1=0
        
            try:a2=int(Mendoan.get())
            except: a2=0
        
            try:a3=int(Rames.get())
            except: a3=0
        
            try:a4=int(lolipop.get())
            except: a4=0
        
            try:a5=int(esteh.get())
            except: a5=0
        
            try:a6=int(Coklat.get())
            except: a6=0
        
            try:a7=int(Eskrim.get())
            except: a7=0
        
            # menentukan harga 
            c1=3000*a1
            c2=1000*a2
            c3=5000*a3
            c4=1000*a4
            c5=3000*a5
            c6=2500*a6
            c7=3000*a7
        
            IbI_total = Label(f2,font=("aria",20,"bold"),text="Total",width=22,fg="lightyellow",bg="black")
            IbI_total.place(x=0,y=50)
        
            entry_total=Entry(f2,font=("aria",20,"bold"),textvariable=Total_bill,bd=6,width=14,bg="lightgreen")
            entry_total.place(x=20,y=100)
        
            totalcost=c1+c2+c3+c4+c5+c6+c7
            string_bill="RP.",str("%.2f" %totalcost)
        
            Total_bill.set(string_bill)
        
        
        Label(root,text="Kasir Kantin",bg="black",fg="white",font=("calibri",33),width=300,height=4).pack()
        
        #Menu Card
        f = Frame(root,bg="aqua",highlightbackground="red",highlightthickness=1,width=370,height=400)
        f.place(x=30,y=250)
        
        Label(root,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="aqua").place(x=100,y=0)
        
        Label(f,font=("Lucida Calligraphy",15,'bold'),text="Donat......Rp.3000/Pcs",fg="black",bg="aqua").place(x=10,y=80)
        Label(f,font=("Lucida Calligraphy",15,'bold'),text="Mendoan......Rp.1000/Pcs",fg="black",bg="aqua").place(x=10,y=110)
        Label(f,font=("Lucida Calligraphy",15,'bold'),text="Rames......Rp.5000/Pcs",fg="black",bg="aqua").place(x=10,y=140)
        Label(f,font=("Lucida Calligraphy",15,'bold'),text="lolipop......Rp.1000/Pcs",fg="black",bg="aqua").place(x=10,y=170)
        Label(f,font=("Lucida Calligraphy",15,'bold'),text="esteh......Rp.3000/Pcs",fg="black",bg="aqua").place(x=10,y=200)
        Label(f,font=("Lucida Calligraphy",15,'bold'),text="Coklat......Rp.2500/Pcs",fg="black",bg="aqua").place(x=10,y=230)
        Label(f,font=("Lucida Calligraphy",15,'bold'),text="Eskrim......Rp.3000/Pcs",fg="black",bg="aqua").place(x=10,y=260)
        
        
        # Total
        f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=370,height=400)
        f2.place(x=880,y=250)
        
        total=Label(f2,text="Kasir",font=("calibri",20),bg="lightyellow")
        total.place(x=160,y=10)
        
        # Input Kerja
        f1 = Frame(root,bd=5,height=400,width=450,relief=RAISED)
        f1.pack(pady=30)
        Donat=StringVar()
        Mendoan=StringVar()
        Rames=StringVar()
        lolipop=StringVar()
        esteh=StringVar()
        Coklat=StringVar()
        Eskrim=StringVar()
        Total_bill=StringVar()
        
        # Label
        IbI_Donat=Label(f1,font=("aria",20,'bold'),text="Donat",width=12,fg="blue4")
        IbI_Mendoan=Label(f1,font=("aria",20,'bold'),text="Mendoan",width=12,fg="blue4")
        IbI_Rames=Label(f1,font=("aria",20,'bold'),text="Rames",width=12,fg="blue4")
        IbI_lolipop=Label(f1,font=("aria",20,'bold'),text="lolipop",width=12,fg="blue4")
        IbI_esteh=Label(f1,font=("aria",20,'bold'),text="esteh",width=12,fg="blue4")
        IbI_Coklat=Label(f1,font=("aria",20,'bold'),text="Coklat",width=12,fg="blue4")
        IbI_Eskrim=Label(f1,font=("aria",20,'bold'),text="Eskrim",width=12,fg="blue4")

        IbI_Donat.grid(row=1,column=0)
        IbI_Mendoan.grid(row=2,column=0)
        IbI_Rames.grid(row=3,column=0)
        IbI_lolipop.grid(row=4,column=0)
        IbI_esteh.grid(row=5,column=0)
        IbI_Coklat.grid(row=6,column=0)
        IbI_Eskrim.grid(row=7,column=0)
        
        # Input
        entry_Donat=Entry(f1,font=("aria",20,"bold"),textvariable=Donat,bd=6,width=8,bg="red")
        entry_Mendoan=Entry(f1,font=("aria",20,"bold"),textvariable=Mendoan,bd=6,width=8,bg="red")
        entry_Rames=Entry(f1,font=("aria",20,"bold"),textvariable=Rames,bd=6,width=8,bg="red")
        entry_lolipop=Entry(f1,font=("aria",20,"bold"),textvariable=lolipop,bd=6,width=8,bg="red")
        entry_esteh=Entry(f1,font=("aria",20,"bold"),textvariable=esteh,bd=6,width=8,bg="red")
        entry_Coklat=Entry(f1,font=("aria",20,"bold"),textvariable=Coklat,bd=6,width=8,bg="red")
        entry_Eskrim=Entry(f1,font=("aria",20,"bold"),textvariable=Eskrim,bd=6,width=8,bg="red")
        
        
        entry_Donat.grid(row=1,column=1)
        entry_Mendoan.grid(row=2,column=1)
        entry_Rames.grid(row=3,column=1)
        entry_lolipop.grid(row=4,column=1)
        entry_esteh.grid(row=5,column=1)
        entry_Coklat.grid(row=6,column=1)
        entry_Eskrim.grid(row=7,column=1)
        
        # Tombol
        btn_reset=Button(f1,bd=5,fg="black",bg="lightgreen",font=("arial",16,"bold"),width=10,text="Reset",command=Reset)
        btn_reset.grid(row=8,column=0)
        
        btn_total=Button(f1,bd=5,fg="black",bg="lightgreen",font=("arial",16,"bold"),width=10,text="Total",command=Total)
        btn_total.grid(row=8,column=1)
        

        # end

    elif user=="" and code=="":
        messagebox.showerror("invalid", "please enter username and password")
    elif user=="":
        messagebox.showerror("invalid", "username is required")
    elif code=="":
        messagebox.showerror("invalid", "the password field is required")
    elif user != "Opik" and code != "998":
        messagebox.showerror("invalid", "invalid username and password")
    elif user!="Opik":
        messagebox.showerror("invalid", "please enter a valid username")
    elif code != "998":
        messagebox.showerror("invalid", "please enter a valid password")

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

