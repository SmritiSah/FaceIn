import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from Face_recognition import Face_Recognition
from attendance import Attendance
from tkinter import messagebox


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
    
        
        # # FIRST IMG
        # img=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/upper.jpg')
        # img=img.resize((320, 100),Image.LANCZOS)
        # self.photoimg=ImageTk.PhotoImage(img) 
        # f_lbl=tk.Label(self.root ,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=320,height=100)
        
        # # SECOND IMG
        # img1=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/upper.jpg')
        # img1=img1.resize((320, 100),Image.LANCZOS)
        # self.photoimg1=ImageTk.PhotoImage(img1) 
        # f_lbl=tk.Label(self.root ,image=self.photoimg1)
        # f_lbl.place(x=320,y=0,width=320,height=100)
        
        # # THIRD IMG
        # img3=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/upper.jpg')
        # img3=img3.resize((320, 100),Image.LANCZOS)
        # self.photoimg3=ImageTk.PhotoImage(img3) 
        # f_lbl=tk.Label(self.root ,image=self.photoimg3)
        # f_lbl.place(x=640,y=0,width=320,height=100)
        
        # #FOURTH IMG
        # img2=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/upper.jpg')
        # img2=img2.resize((320, 100),Image.LANCZOS)
        # self.photoimg2=ImageTk.PhotoImage(img2) 
        # f_lbl=tk.Label(self.root ,image=self.photoimg2)
        # f_lbl.place(x=960,y=0,width=320,height=100)
        
        #BACKGROUND
        img4=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/sa.jpg')
        img4=img4.resize((1530, 790),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=tk.Label(self.root ,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("time new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
         
        #student button 
        img5=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/bache.jpg')
        img5=img5.resize((190, 190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=240,y=80,width=190,height=190)

        b2=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=240,y=270,width=190,height=40)
        
        
        #Detect face button
        img6=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/facer.jpeg')
        img6=img6.resize((190, 190),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=540,y=80,width=190,height=190)

        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=540,y=270,width=190,height=40)
        
        #Attendance button
        img7=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/kalluishita.jpg')
        img7=img7.resize((190, 190),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=840,y=80,width=190,height=190)

        b2=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=840,y=270,width=190,height=40)
        
        #Train button
        img8=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/dataset.jpg')
        img8=img8.resize((190, 190),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=240,y=360,width=190,height=190)

        b2=Button(bg_img,text="Train",cursor="hand2", command=self.train_data,font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=240,y=540,width=190,height=40)

        #photos button
        img9=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/jyadasiphoto.jpg')
        img9=img9.resize((190, 190),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=540,y=360,width=190,height=190)

        b2=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=540,y=540,width=190,height=40)
        
        #exit button
        img10=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/exit.jpg')
        img10=img10.resize((190, 190),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.exit_data)
        b1.place(x=840,y=360,width=190,height=190)

        b2=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_data,font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=840,y=540,width=190,height=40)
        
    def open_img(self):
        os.startfile("C://SemProject/ProjectPrograms/Login_Form/data")   
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 
        
    def take_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  
          
    def exit_data(self):
        result =messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if result == tk.YES:
            root.destroy() 
        
        
        
        
if __name__=="__main__":
    root=tk.Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()