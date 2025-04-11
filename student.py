import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #=================variables======================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        #BG
        img4=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/sundarbilu.jpg')
        img4=img4.resize((1530, 790),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=tk.Label(self.root ,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("time new roman",30,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=270,y=33,width=750,height=45)
        
        #FRAME
        main_frame=tk.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=30,y=115,width=1220,height=600)
        
        #L Frame
        Left_frame=tk.LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=600,height=580)
        
        img_left=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/stmain.png')
        img_left=img_left.resize((320, 100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left) 
        
        f_lbl=tk.Label(Left_frame ,image=self.photoimg_left, bg="black")
        f_lbl.place(x=0,y=0,width=600,height=130)
        
        #Current Course
        Current_course_frame=tk.LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Enrolled Course",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=4,y=135,width=588,height=90)
        
        #department
        dep_label=tk.Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12),state="readonly",width=17)
        dep_combo["values"]=("Select Department","CS","IT","MT","EC")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=0,sticky=W)
        
        # course
        course_label=tk.Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=0,sticky=W)
        
        # year
        year_label=tk.Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=0,sticky=W)

        # semester
        semester_label=tk.Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Class Student Information
        Class_Student_frame=tk.LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=4,y=225,width=588,height=300)
        
        #StudentID  
        studentId_label=tk.Label(Class_Student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10, pady=0,sticky=W)
        
        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.va_std_id,width=17,font=("times new roman",12))
        studentID_entry.grid(row=0,column=1,padx=2, pady=2,sticky=W)
        
        #student name
        studentName_label=Label(Class_Student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=0,sticky=W)

        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=17,font=("times new roman",12))
        studentName_entry.grid(row=0,column=3,padx=2, pady=2,sticky=W)

        #class division
        class_div_label=Label(Class_Student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=0,sticky=W)
        
        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12),state="readonly",width=17)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #roll no
        roll_no_label=Label(Class_Student_frame,text="Roll Number",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=0,sticky=W)

        roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=17,font=("times new roman",12))
        roll_no_entry.grid(row=1,column=3,padx=2,pady=2,sticky=W)

        #gender
        gender_label=Label(Class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=0,sticky=W)
        
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #date of birth
        dob_label=Label(Class_Student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=0,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=17,font=("times new roman",12))
        dob_entry.grid(row=2,column=3,padx=2,pady=2,sticky=W)

        #Email
        email_label=Label(Class_Student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=0,sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=17,font=("times new roman",12))
        email_entry.grid(row=3,column=1,padx=2,pady=2,sticky=W)

        #phone no
        phone_label=Label(Class_Student_frame,text="Phone Number",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=0,sticky=W)

        phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=17,font=("times new roman",12))
        phone_entry.grid(row=3,column=3,padx=2,pady=2,sticky=W)

        #Address
        address_label=Label(Class_Student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=0,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=17,font=("times new roman",12))
        address_entry.grid(row=4,column=1,padx=2,pady=2,sticky=W)
        
        #Teacher name
        teacher_label=Label(Class_Student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=0,sticky=W)

        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=17,font=("times new roman",12))
        teacher_entry.grid(row=4,column=3,padx=2,pady=2,sticky=W)
        

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radiobtn1.grid(row=6,column=0, padx=10)
        
        
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=2,padx=10)
        
        #bbuttons frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=3,y=180,width=579,height=30)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0, padx=2.3)
        
        update_btn=Button(btn_frame,text="Update", command=self.update_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1, padx=2.3)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2, padx=2.3)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3, padx=2.3)
        
        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=230,y=215,width=147.4,height=30)
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=2.3)
    
        # upload_photo_btn=Button(btn_frame1,text="Upload Photo",width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # upload_photo_btn.grid(row=0,column=1,padx=2.3)
        
        #R Frame
        Right_frame=tk.LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=610,y=10,width=600,height=580)
        
        img_right=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/gorinandu.png')
        img_right=img_right.resize((350, 165),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=tk.Label(Right_frame ,image=self.photoimg_right, bg="black")
        f_lbl.place(x=0,y=0,width=600,height=250)
        
        #Search system
        # Search_frame=tk.LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        # Search_frame.place(x=4,y=200,width=588,height=60) 
        
        # search_label=Label(Search_frame,text="Search By",font=("times new roman",13,"bold"),bg="white")
        # search_label.grid(row=0,column=0,padx=2,pady=0,sticky=W)
        
        # search_combo=ttk.Combobox(Search_frame,font=("times new roman",12),state="readonly",width=12)
        # search_combo["values"]=("Select","Roll_No","Phone_No")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12))
        # search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        # search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="blue",fg="white")
        # search_btn.grid(row=0,column=3,padx=2)    
        # showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        # showAll_btn.grid(row=0,column=4,padx=2)
        
        #table frame
        table_frame=tk.Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=265,width=588,height=230) 
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #=================functions declaration=================
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                phone_regex = r"^[0-9]{10}$"
                if not re.match(phone_regex, self.var_phone.get()):
                    messagebox.showerror("Error", "Invalid Phone Number (must be 10 digits)", parent=self.root)
                    return
                
                # Validate email
                email_regex = r"^(?=.*[@])(?=.*\.)[a-zA-Z0-9_.+-]+@(gmail\.com|banasthali\.in|yahoo\.com)$"
                if not re.match(email_regex, self.var_email.get()):
                    messagebox.showerror("Error", "Invalid Email Address (must end with @gmail.com, @banasthali.in, or @yahoo.com)", parent=self.root)
                    return
                conn=mysql.connector.connect(host="localhost",user="myuser",password="new_password",auth_plugin='mysql_native_password',database="face_recognizer",use_pure=True)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.va_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(), 
                                                                                                            self.var_roll.get(), 
                                                                                                            self.var_gender.get(), 
                                                                                                            self.var_dob.get(), 
                                                                                                            self.var_email.get(), 
                                                                                                            self.var_phone.get(), 
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()                      
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        #================fetch data====================
    def  fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="myuser",password="new_password",auth_plugin='mysql_native_password',database="face_recognizer",use_pure=True)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
            
        
        #=============get cursor=================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update:
                    conn=mysql.connector.connect(host="localhost",user="myuser",password="new_password",auth_plugin='mysql_native_password',database="face_recognizer",use_pure=True)
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Student_id=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Email=%s",(

                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(), 
                                                                                                                                                                                    self.var_roll.get(), 
                                                                                                                                                                                    self.var_gender.get(), 
                                                                                                                                                                                    self.var_dob.get(), 
                                                                                                                                                                                    self.va_std_id.get(), 
                                                                                                                                                                                    self.var_phone.get(), 
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_email.get()
                                                                                                                                                                                ))                    
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #delete function
    def delete_data(self):
        if self.va_std_id=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:  
                    conn=mysql.connector.connect(host="localhost",user="myuser",password="new_password",auth_plugin='mysql_native_password',database="face_recognizer",use_pure=True)
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
        #reset
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        
        
    #========================Generate data set or take photo sample==============================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="myuser",password="new_password",auth_plugin='mysql_native_password',database="face_recognizer",use_pure=True)
                my_cursor=conn.cursor()
                sql = "select roll from student where Student_id=%s"
                val = (self.va_std_id.get(),)
                my_cursor.execute(sql, val)
                r = my_cursor.fetchone()  # Fetch the first row of the result set
                r = int(r[0])

                

                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_div.get(), 
                                                                                                                                                                                    self.var_roll.get(), 
                                                                                                                                                                                    self.var_gender.get(), 
                                                                                                                                                                                    self.var_dob.get(), 
                                                                                                                                                                                    self.var_email.get(), 
                                                                                                                                                                                    self.var_phone.get(), 
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.va_std_id.get()
                                                                                                                                                                                )) 
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()      
                
                #====================Load predefined data on face frontals from opencv==================
                face_classifier=cv2.CascadeClassifier("C:\SemProject\ProjectPrograms\Login_Form\haarcascade_frontalface_default.xml")
                
                
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)#detect faces
                    for (x, y, w, h) in faces:#detect faces using the slicing
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0

                # Set the focus back to the main window
                self.root.focus_set()
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)is not None:
                        img_id +=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        
                        file_name_path=f"C:\SemProject\ProjectPrograms\Login_Form\data/user."+str(r)+"."+str(img_id)+".jpg" 
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)   #scale colorthickness
                        cv2.imshow("Cropped Face",face)
                       
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!", parent=self.root)         
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    
                 
if __name__=="__main__":
    root=tk.Tk()
    obj=Student(root)
    root.mainloop()         