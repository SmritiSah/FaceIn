import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # title_lbl=Label(self.root, text="FACE RECOGNITION",font=("time new roman",30,"bold"),bg="white",fg="navyblue")
        # title_lbl.place(x=270,y=15,width=750,height=45)
        
        #image
        #img_top=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/face-detect.webp')
        #img_top=img_top.resize((1290, 800),Image.LANCZOS)
        #self.photoimg_top=ImageTk.PhotoImage(img_top) 
        
        #f_lbl=tk.Label(self.root,image=self.photoimg_top)
        #f_lbl.place(x=0,y=0,width=1290,height=800)
        
        #second image
        # img_top=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/face-detect.webp')
        # img_top=img_top.resize((850, 750),Image.LANCZOS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top) 
        
        # f_lbl=tk.Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=450,y=0,width=850,height=650)
        
        #first image
        img_bottom=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/dataset.jpg')
        img_bottom=img_bottom.resize((1290, 800),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom) 
        
        f_lbl=tk.Label(self.root,image=self.photoimg_bottom)  
        f_lbl.place(x=0,y=0,width=1290,height=800)
        
        #button
        b2=Button(f_lbl,text="Take Attendance",cursor="hand2",command=self.face_recog,font=("time new roman",15,"bold"),bg="white",fg="navyblue")
        b2.place(x=480,y=320,width=350,height=60)
        
        
        # title_lbl=Label(self.root, text="FACE RECOGNITION",font=("time new roman",30,"bold"),bg="navyblue",fg="white")
        # title_lbl.place(x=300,y=15,width=650,height=45)
        
        #===========attendance======#
    def mark_attendance(self,i,r,n,d):
        with open('C://SemProject/ProjectPrograms/Login_Form/attendance.csv',"r+",newline="\n") as f:
        # with open("attendance.csv", "w", newline="\n") as f:
           # pass

            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)and (n not in name_list)and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
                    
                
       
    ####### face recognition #########
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",user="myuser",password="new_password",auth_plugin='mysql_native_password',database="face_recognizer",use_pure=True)
                my_cursor=conn.cursor()
                
                my_cursor.execute("Select Name from student where Roll="+str(id))
                n=my_cursor.fetchone()
                if n is not None:
                    n="+".join(n)
                    # n = "+".join(n[0])
                
                my_cursor.execute("Select Roll from student where Roll="+str(id))
                r=my_cursor.fetchone()
                if r is not None:
                    r="+".join(r)
                # r = "+".join(r[0])
                
                my_cursor.execute("Select Dep from student where Roll="+str(id))
                d=my_cursor.fetchone()
                if d is not None:
                    d="+".join(d)
                # d = "+".join(d[0])
                
                my_cursor.execute("Select Student_id from student where Roll="+str(id))
                i=my_cursor.fetchone()
                if i is not None:
                    i="+".join(i)
                
                if confidence>77:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    
                coord=[x,y,w,y]
                
            return coord 
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        #faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faceCascade = cv2.CascadeClassifier('c:\SemProject\ProjectPrograms\Login_Form\haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
            if cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
         
if __name__=="__main__":
         root=tk.Tk()
         obj=Face_Recognition(root)
         root.mainloop()  