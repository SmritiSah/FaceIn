import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk   #pip install pillow
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
import re

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        im=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/background.jpg')
        self.bg=ImageTk.PhotoImage(image=im)
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=tk.Frame(self.root,bg="black")
        frame.place(x=450,y=130,width=370,height=450)

        img1=Image.open(r"C:\SemProject\ProjectPrograms\Login_Form\images\loginicon.png")
        img1=img1.resize((100, 100), Image.LANCZOS)
        self.phototimage1=ImageTk.PhotoImage(img1)
        lblimg1=tk.Label(image=self.phototimage1, bg="black", borderwidth=0)
        lblimg1.place(x=585, y=147, width=100, height=100)

        get_str=tk.Label(frame, text="Let's Begin", font=("times new roman", 23, "bold"), fg="white", bg="black")
        get_str.place(x=110, y=115)

        username=tk.Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=37, y=200)
        self.txtuser=tk.Entry(frame, font=("calibri", 15))
        self.txtuser.place(x=140, y=200, width=180)

        password=tk.Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=37, y=250)
        self.txtpass=tk.Entry(frame, font=("calibri", 15), show="*")
        self.txtpass.place(x=140, y=250, width=180)

        ##################### ICON IMAGE ##########################

        img2=Image.open(r"C:\SemProject\ProjectPrograms\Login_Form\images\smimg.png")
        img2=img2.resize((25, 25), Image.LANCZOS)
        self.phototimage2=ImageTk.PhotoImage(img2)
        lblimg2=tk.Label(image=self.phototimage2, bg="black", borderwidth=0)
        lblimg2.place(x=462, y=332, width=25, height=25)

        img3=Image.open(r"C:\SemProject\ProjectPrograms\Login_Form\images\lock.png")
        img3=img3.resize((25, 25), Image.LANCZOS)
        self.phototimage3=ImageTk.PhotoImage(img3)
        lblimg3=tk.Label(image=self.phototimage3, bg="black", borderwidth=0)
        lblimg3.place(x=462, y=380, width=25, height=25)

        # LoginButton
        loginbtn=tk.Button(frame, text="Login",command=self.login,font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=200,y=300,width=120,height=30)

        # registerbutton
        registerbtn=tk.Button(frame,text="New User Register",command=self.register_window,font=("calibri", 11),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="blue")
        registerbtn.place(x=5,y=370,width=120)

        # forgetpassbtn
        registerbtn=tk.Button(frame,text="Forget Password?",command=self.forgot_password_window,font=("calibri", 11),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="blue")
        registerbtn.place(x=5,y=395,width=110)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    # def main_window(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Face_Recognition_System(self.new_window)
   
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Required")
        elif self.txtuser.get()=="admin" and  self.txtpass.get()=="1234":
            messagebox.showinfo("Success", "Welcome")
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition_System(self.new_window)
        else: 
            conn=mysql.connector.connect(host="localhost", user="myuser", password="new_password", auth_plugin='mysql_native_password', database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",  (
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get() 
                                                                                        ))

            row=my_cursor.fetchone()
            open_main=False
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only for admin?")     
                if open_main>0:
                   self.new_window=Toplevel(self.root)
                   self.app=Face_Recognition_System(self.new_window)     
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()                                                                              

    #=============================reset password========================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question", parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer", parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password", parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", user="myuser", password="new_password",auth_plugin='mysql_native_password', database="mydata")
            my_cursor=conn.cursor()
            query1=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value1=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query1,value1)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer", parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with new password", parent=self.root2)  
                # self.root2.destroy()                 

   # ===============================================Forgot Password window=================================================          
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Username to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", user="myuser", password="new_password",auth_plugin='mysql_native_password', database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

        if row is None:
            messagebox.showerror("My Error","Please enter the valid user name")
        else:
            conn.close()
            self.root2=Toplevel()
            self.root2.title("Forgot Password") 
            self.root2.geometry("390x420+450+160")

            l=tk.Label(self.root2,text="Forget Password", font=("times new roman", 20, "bold"),fg="red",bg="white")
            l.place(x=0,y=10,relwidth=1)


            security_Q=tk.Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
            security_Q.place(x=50, y=80)

            self.combo_security_Q=ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly")
            self.combo_security_Q["values"]=("Select","Your Birth Place","Your Father's Name", "Your Pet Name")
            self.combo_security_Q.place(x=50, y=110, width=250)
            self.combo_security_Q.current(0)

            security_A=tk.Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
            security_A.place(x=50, y=150)
            
            self.txt_security=ttk.Entry(self.root2, font=("times new roman", 15))
            self.txt_security.place(x=50, y=180, width=250)

            new_password=tk.Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
            new_password.place(x=50, y=220)
            self.txt_newpass=ttk.Entry(self.root2, font=("times new roman", 15),show="*")
            self.txt_newpass.place(x=50, y=250, width=250)

            btn=tk.Button(self.root2, text="Reset",command=self.reset_pass, font=("times new roman", 15, "bold"), fg="white", bg="green")
            btn.place(x=100,y=290)


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

        fname=tk.Label(frame, text="First Name *", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=22, y=100)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=22, y=130, width=250)

        l_name=tk.Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        l_name.place(x=370, y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        #=================== row2 ==============================

        contact=tk.Label(frame, text="Contact Number *", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact.place(x=22, y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=22, y=200, width=250)

        email=tk.Label(frame, text="Email *", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email.place(x=370, y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email ,font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        #=================== row3 ==============================

        security_Q=tk.Label(frame, text="Select Security Question *", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_Q.place(x=22, y=240)

        self.combo=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        self.combo["values"]=("Select","Your Birth Place","Your Father's Name", "Your Pet Name")
        self.combo.place(x=22, y=270, width=250)
        self.combo.current(0)

        security_A=tk.Label(frame, text="Security Answer *", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_A.place(x=370, y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        #================== row4 ==============

        pswd=tk.Label(frame, text="Password *", font=("times new roman", 15, "bold"), fg="black", bg="white")
        pswd.place(x=22,  y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=22, y=340, width=250)

        confirm_pswd=tk.Label(frame, text="Confirm Password *", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confirm_pswd.place(x=370,  y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

  
        # ================      checkbutton      ==============
        self.var_check=IntVar()
        self.checkbtn=tk.Checkbutton(frame, variable=self.var_check,text="I Agree With The Terms & Conditions",font=("times new roman",11), onvalue=1, offvalue=0)
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
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror("Error","Please fill all the required fields.")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree to our terms and conditions")
        elif len(self.var_contact.get()) != 10:
            messagebox.showerror("Error", "Contact Number must be of 10 digits")
        elif not re.search(r'@(yahoo|gmail|banasthali)\.com$', self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email ID Format\n Email-id format must be in the form:abc@gmail.com")
        
        else:
            conn=mysql.connector.connect(host="localhost", user="myuser", password="new_password",auth_plugin='mysql_native_password', database="mydata")
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
                

if __name__=="__main__":
    main() 