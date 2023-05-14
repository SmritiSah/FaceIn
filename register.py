import tkinter as tk
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk   #pip install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        self.frame = ttk.Frame(self.root)
        self.frame.pack()
        #=============variable============
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #================bg image========================
        im=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/wp2.jpg')
        self.bg=ImageTk.PhotoImage(image=im)
        bg_lbl=tk.Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        im1=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/sundarbilu.jpg')
        self.bg1=ImageTk.PhotoImage(image=im1)
        left_lbl=tk.Label(self.root,image=self.bg1)
        left_lbl.place(x=70,y=80,width=400,height=500)

        frame=tk.Frame(self.root, bg="white")
        frame.place(x=450, y=80, width=750, height=500)

        register_lbl=tk.Label(frame, text="NEW USER, REGISTER HERE", font=("times new roman", 20, "bold"), fg="black", bg="white")
        register_lbl.place(x=20, y=20)

        # ================== label & entry======================

        #=================== row1 ==============================

        fname=tk.Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=22, y=100)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=22, y=130, width=250)

        l_name=tk.Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        l_name.place(x=370, y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        #=================== row2 ==============================

        contact=tk.Label(frame, text="Contact Number", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact.place(x=22, y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=22, y=200, width=250)

        email=tk.Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email.place(x=370, y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email ,font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        #=================== row3 ==============================

        security_Q=tk.Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_Q.place(x=22, y=240)

        self.combo=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        self.combo["values"]=("Select","Your Birth Place","Your Father's Name", "Your Pet Name")
        self.combo.place(x=22, y=270, width=250)
        self.combo.current(0)

        security_A=tk.Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_A.place(x=370, y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        #================== row4 ==============

        pswd=tk.Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        pswd.place(x=22,  y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=22, y=340, width=250)

        confirm_pswd=tk.Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confirm_pswd.place(x=370,  y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

  
        # ================      checkbutton      ==============
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame, variable=self.var_check,text="I Agree With The Terms & Conditions",font=("times new roman",11), onvalue=1, offvalue=0)
        self.checkbtn.place(x=200,y=460)

        #==================     buttons      ================
        img=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/samer.jpg')
        img=img.resize((100, 50), Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=tk.Button(frame, image=self.photoimage,command=self.register_data, borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=95, y=400, width=95)

        img1=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/samel.jpg')
        img1=img1.resize((100, 50), Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=tk.Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", bg="white")
        b1.place(x=455, y=400, width=95)

        #==================         func decl          =====================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields Required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="newrootpassword", database="mydata")
            my_cursor=conn.cursor()
            query=("SELECT * FROM REGISTER WHERE email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                       )) 
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully!")   
                












if __name__ == "__main__": 
    root=tk.Tk()
    app=Register(root)
    root.mainloop()