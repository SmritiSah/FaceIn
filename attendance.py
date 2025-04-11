import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        ########variables############
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        #BG
        img4=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/sundarbilu.jpg')
        img4=img4.resize((1530, 790),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=tk.Label(self.root ,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=790)
        
        title_lbl=Label(bg_img, text="ATTTENDANCE MANAGEMENT SYSTEM",font=("time new roman",30,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=270,y=33,width=800,height=45)
        
        #FRAME
        main_frame=tk.Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=30,y=115,width=1220,height=600)
        
         #L Frame
        Left_frame=tk.LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="StudentAttendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=10,width=600,height=580)
        
        img_left=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/stmain.png')
        img_left=img_left.resize((320, 100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left) 
        
        f_lbl=tk.Label(Left_frame ,image=self.photoimg_left, bg="black")
        f_lbl.place(x=0,y=0,width=600,height=130)
        
        left_inside_frame=tk.Frame(Left_frame, bd=2, relief=RIDGE,bg="white")
        left_inside_frame.place(x=2,y=140,width=590,height=350)
        
        #LabelandEntry
        
        #attendance ID  
        attendanceId_label=tk.Label( left_inside_frame,text="AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10, pady=0,sticky=W)
        
        attendanceID_entry=ttk.Entry( left_inside_frame,width=17,textvariable=self.var_atten_id,font=("times new roman",12))
        attendanceID_entry.grid(row=0,column=1,padx=2, pady=2,sticky=W)
        
        #Name 
        roll_label=tk.Label( left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10, pady=0)
        
        atten_roll=ttk.Entry( left_inside_frame,width=17,textvariable=self.var_atten_name,font=("times new roman",12))
        atten_roll.grid(row=0,column=3,pady=2)
        
        #date
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_name,font=("times new roman",12))
        atten_name.grid(row=1,column=1,pady=2)
        
        #department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_dep,font=("times new roman",12))
        atten_dep.grid(row=1,column=3,pady=2)
        
        #time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_time,font=("times new roman",12))
        atten_time.grid(row=2,column=1,pady=2)
        
        #Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2)

        atten_time=ttk.Entry(left_inside_frame,width=17,textvariable=self.var_atten_date,font=("times new roman",12))
        atten_time.grid(row=2,column=3,pady=2)
        
        
        #attendance
        attendance_label=Label(left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #bbuttons frame
        btn_frame=Frame(left_inside_frame,bd=0,relief=RIDGE,bg="white")
        btn_frame.place(x=40,y=280,width=500,height=30)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=1, padx=2.2)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2, padx=2.2)

        #delete_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        #delete_btn.grid(row=0,column=2, padx=2.2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3, padx=2.2)
        
        
        
        
        
        #R Frame
        Right_frame=tk.LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=610,y=10,width=600,height=580)
        
        table_frame=tk.Frame(Right_frame, bd=2, relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=590,height=480)
        
        #img_right=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/gorinandu.png')
        #img_right=img_right.resize((350, 165),Image.LANCZOS)
        #self.photoimg_right=ImageTk.PhotoImage(img_right)
        #f_lbl=tk.Label(Right_frame ,image=self.photoimg_right, bg="black")
        #f_lbl.place(x=0,y=0,width=600,height=200)
        
        #====================scroll bar table================
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        
    ###############fetch data################
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children()) 
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     ##import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
            
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to eport",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")   
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     
                
    def get_cursor(self,event=""):
        cursor_rows=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_rows)
        rows=content['values']     
        self.var_atten_id.set(rows[0])  
        self.var_atten_roll.set(rows[1]) 
        self.var_atten_name.set(rows[2])      
        self.var_atten_dep.set(rows[3])   
        self.var_atten_time.set(rows[4])   
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])      
        
        
    def reset_data(self):
        self.var_atten_id.set("")  
        self.var_atten_roll.set("") 
        self.var_atten_name.set("")      
        self.var_atten_dep.set("")   
        self.var_atten_time.set("")   
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")    
               
        
if __name__=="__main__":
    root=tk.Tk()
    obj=Attendance(root)
    root.mainloop() 