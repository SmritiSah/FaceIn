import tkinter as tk
import datetime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #title_lbl=Label(self.root, text="TRAIN DATA SET",font=("time new roman",30,"bold"),bg="white",fg="navyblue")
        #title_lbl.place(x=270,y=15,width=750,height=45)
        
        #image
        img_top=Image.open('C://SemProject/ProjectPrograms/Login_Form/images/mainphotos/sun.webp')
        img_top=img_top.resize((1290, 800),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top) 
        
        f_lbl=tk.Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1290,height=800)
        
        title_lbl=Label(self.root, text="TRAIN DATA SET",font=("time new roman",30,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=270,y=10,width=750,height=45)
        
        #button
        b2=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("time new roman",15,"bold"),bg="navyblue",fg="white")
        b2.place(x=550,y=400,width=200,height=50)
        
    def train_classifier(self):
        data_dir=("C://SemProject/ProjectPrograms/Login_Form/data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]    
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  #grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            #print(id)
            
            #C:\SemProject\ProjectPrograms\Login_Form\data\user.3_1_2023-02-25_23-29-55.jpg
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #============Train the classifier and save==============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!", parent=self.root)
        
        
if __name__=="__main__":
    root=tk.Tk()
    obj=Train(root)
    root.mainloop()  