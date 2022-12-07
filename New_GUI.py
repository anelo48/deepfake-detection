from cProfile import label
from lib2to3.pgen2 import pgen
import tkinter as tk
from tkinter import BOTH, N, S, E, W, END, HORIZONTAL, VERTICAL, Button, Frame, Image, Label, LabelFrame, PanedWindow, PhotoImage, filedialog, messagebox, ttk
from tkinter import font
from tkinter.constants import CENTER
from turtle import color
from webbrowser import get
from PIL import Image, ImageTk
from tkinter.font import BOLD
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.tix import DisplayStyle
from typing import TextIO
import cv2 
from tkinter import Button, filedialog
from tkinter import *
import os
from tkinter import messagebox
import sys
from sklearn import preprocessing
from PIL import Image,ImageTk


LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 
        self.logo = PhotoImage(file='ft.png')
        self.logo_label= ttk.Label(self, image= self.logo, width=20)
        PhotoImage(file='ft.png') 
        self.logo_label.pack() 

        self.teks = """Deteksi Video Deepfake Menggunakan 
        Convolutional Neural Network 
        Model ResNet50"""   

        #label menampilkan text
        w = Label (self, font=("Verdana",16), fg = "black",
                                compound = CENTER,
                                text= self.teks, background= "white"
                                ).place(x=250, y=20)

        w = Label (self, font=("Verdana",16), fg = "black",
                                compound = CENTER,
                                text= self.teks, background= "white"
                                ).place(x=250, y=20)
        # label of frame Layout 2
        self.teks = """ Ananda Amalia"""   
        w = Label (self, font=("Verdana",10), fg = "black", 
                                text= self.teks, background= "#9999cc"
                                ).place(x= 140, y=477 )
        
        self.teks = """  Nila Rahayu Hasibuan"""   
        w = Label (self, font=("Verdana",10), fg = "black", 
                                text= self.teks, background= "#9999cc"
                                ).place(x= 370, y=477 )
        self.teks = """  Muhammad Taufan Hidayat """   
        w = Label (self, font=("Verdana",10), fg = "black", 
                                text= self.teks, background= "#9999cc"
                                ).place(x=600, y=477  )
        
        # label of frame Layout 2
        self.teks = """ Dr.Ronsen Purba, M.Sc"""   
        w = Label (self, font=("Verdana",10), fg = "black", 
                                text= self.teks, background= "#9999cc"
                                ).place(x= 210, y=540 )
        
        self.teks = """  Darwin S.Kom M.Kom"""   
        w = Label (self, font=("Verdana",10), fg = "black", 
                                text= self.teks, background= "#9999cc"
                                ).place(x= 500, y=540 )
        
        dpn_btn = Button(self, text="Start",font=("Comic Sans MS",13, BOLD), fg = "#581845", bg='#f6ce38',
        borderwidth=1, highlightthickness=2,relief="flat",
        command = lambda: controller.show_frame(Page1) )
        dpn_btn.place(x=330, y=620, width=250, height=40)
  
_lbltext="Url File Video";
_lblModul="Preprocessing";
_lblDetail="Deteksi"

import ModulResNet50 as resnet50

class Page1(tk.Frame):
   
    resnet50.LoadDataSet()
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
       
        frame_statusbar = tk.Frame(self, relief = tk.SUNKEN, bd = 2,name="lbl1")
        label = tk.Label(frame_statusbar, text = "Deteksi Video Deepfake Menggunakan Convolutional Neural Network Model ResNet50",width = 250)
        label.pack(side = tk.LEFT)
        frame_statusbar.pack(side = tk.BOTTOM, fill = tk.X)

        utama_btn = Button(self, text="Utama",
                borderwidth=0, highlightthickness=0,relief="flat", foreground="navy", background="#FFCC00",font=("Comic Sans MS",10),
                command = lambda: Modul("Awal"))
        utama_btn.place(x=20, y= 65, width=210, height=45)

        buatmela_btn = Button(self, text="Melatih & Menguji",
                borderwidth=0, highlightthickness=0,relief="flat", foreground="navy",background="#FFCC00",font=("Comic Sans MS",10),
                command = lambda:Modul("MelatihMenguji"))
        buatmela_btn.place(x=235, y= 65, width=210, height=45)


        global proses_btn
        proses_btn = Button(self, text="Preprocessing",
                borderwidth=0, highlightthickness=0,relief="flat", background="#FFCC00",foreground="navy",font=("Comic Sans MS",10),
                command = lambda:click())
        proses_btn.place(x=455, y= 65, width=210, height=45) 

        global penguji
        penguji = Button(self, text="Deteksi", borderwidth=0, highlightthickness=0,relief="flat", font=("Comic Sans MS",10),background="#FFCC00",foreground="black",
                command = lambda:uji())
        penguji.place(x=670, y= 65, width=210, height=45)

        # global proses_btn
        # proses_btn = Button(self, text="Train",
        # borderwidth=0, highlightthickness=0,
        # relief="flat", background="#9999CC", command = Tran)
        # proses_btn.place(x=10, y=120, width=700, height=30)

        # global penguji
        # penguji = Button(self, text="Test",
        # borderwidth=0, highlightthickness=0,
        # relief="flat", background="#9999CC", command = uji)
        # penguji.place(x=720, y=120, width=173, height=30)    
        
        #fungsi untuk membuka file library 
        def openFile():
            filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                            title="Please select your video ?")
                  
            #fungsi untuk mengambil lokasi file
            label_file_explorer.configure(text="File: "+filepath)
            global _lbltext
            _lbltext=filepath
        
        #tombol untuk mengambil file
        tab_open = Button(self,text="Input Video",font=("Comic Sans MS",8, BOLD), fg = "black", bg='#9999CC',
        borderwidth=1, highlightthickness=2,
        command =openFile, relief="flat" )
        tab_open.place(x=20, y=10, width=96, height=38)
        
        #untuk nama lokasi file yang diambil
        label_file_explorer = Label(self, text="Lokasi File", width=107, height=2, fg="#746E6D", background="white")
        label_file_explorer.place(x=120, y= 10) 
        
        #membuat listbox
        global listbox
        listbox = Listbox(self)
        listbox.place(x=450, y=420, width=435, height=325)

        global permodelan
        
        #pembuatan membuat scroll text
        frame = tk.Frame(self, relief = tk.SUNKEN, bd = 2)
        #frame.pack(side = tk.LEFT, fill =  None, padx=10)
        frame.place(x=450, y=130)
        self.scrolled_text = ScrolledText(frame,height=21, width= 58, background='black', fg='white', font=("Verdana",8))
        # self.scrolled_text.grid(row=100, column=0, sticky=(N, S, W, E))
        self.scrolled_text.grid(column = 0, pady = 0, padx = 0)

        permodelan=self.scrolled_text

        # menampilkan layer fungsional resnet50
        report = open('report.txt','r')
        report=str(report.read())
        
        #memasukkan hasil file report ke dalam scroll text
        permodelan.insert(END,report +   "\n")

        width =420
        height = 300
        photo= Image.open("database/accuracy.png")
        photo= photo.resize((width, height),Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(photo)
        self.a_label= Label(self, image= self.photoImg, background="pink")
        self.a_label.place(x=20, y=130)
       
        model_loss= Image.open("database/model_loss.png")
        model_loss= model_loss.resize((width, height),Image.ANTIALIAS)
        self.img_model_loss = ImageTk.PhotoImage(model_loss)
        self.b_label= Label(self, image= self.img_model_loss, background="pink")
        self.b_label.place(x=20, y=440)
       
def uji():
        global jumlah_fake
        global jumlah_real
        global jumlah_data
        jumlah_real=0
        jumlah_fake=0
        jumlah_data=0
        if penguji['text']=="Deteksi":
                for i, listbox_entry in enumerate(listbox.get(0, END)):
                                        # print(listbox_entry)
                                        Det=listbox_entry.split('#')
                                        if len(Det) !=1:
                                                hasil=resnet50.modul_deepfake(Det[1])
                                                jumlah_data=jumlah_data+1
                                                if hasil=="Real":
                                                        jumlah_real=jumlah_real+1
                                                else:
                                                        jumlah_fake=jumlah_fake+1

                                                print(Det[1])
                                                print(hasil)

                permodelan.delete('1.0',END)
               
                x = round((jumlah_real / jumlah_data)*100, 2)     
                y=  round((jumlah_fake / jumlah_data)*100, 2)
                permodelan.insert(END,"Ditemukan jumlah data Real : " + str(jumlah_real) +   "  \n")
                permodelan.insert(END,"Ditemukan jumlah data Fake : " + str(jumlah_fake) +   "  \n")
                permodelan.insert(END,"Persentasi data Real adalah : " + str(x) +   " % \n")
                permodelan.insert(END,"Persentasi data Fake adalah :  " + str(y) +   " % \n")


                if jumlah_fake > jumlah_real:
                        permodelan.insert(END,"The true video is: FAKE \n")
                else :
                        permodelan.insert(END,"The true video is: REAL \n")
                 
        else:  
                info = Toplevel()		  # Popup -> Toplevel()
                info.geometry('300x110')
                info.title('Pengujian')
                epoch_label=ttk.Label(info, text="Epoch")
                epoch_label.place(x=10,y=20)
                global epoch_e
                global batch_s
                epoch_e=ttk.Entry(info)
                epoch_e.place(x=80,y=20)
                batch_label=ttk.Label(info, text="Batch Size")
                batch_label.place(x=10,y=40)
                batch_s=ttk.Entry(info)
                batch_s.place(x=80,y=40)
                def epo():
                        epochs =int(epoch_e.get())
                        batch_size =int( batch_s.get())
                        if batch_size < 0 or batch_size > 100:  
                                messagebox.showinfo("Inputan Salah", "Maaf Batch Size hanya bisa input 0 sd 100!" )
                        elif epochs < 0 or epochs > 100:
                                messagebox.showinfo("Inputan Salah", "Maaf Epochs hanya bisa input 0 sd 100!" )
                        else:
                                resnet50.model_epochs(epochs, batch_size)
                        # print(epochs,batch_size)
                        
                oke = Button(info, text="Oke", command=epo)
                oke.place(x=120, y=80)
                info.transient() 	    #Popup reduction impossible
                info.grab_set()
                #resnet50.model_epochs()
        

def Modul(aksi):
        
        global _lblDetail
        global _lblutama
     
        _lblDetail=""
     
        listbox.delete(0,END)
        if aksi=="MelatihMenguji":
                proses_btn.configure(text="Train",background="#9999CC",foreground="black") 
                penguji.configure(text="Test",background="#9999CC",foreground="black")
                
                
        else:
                proses_btn.configure(text="Preprocessing",background="#FFCC00",foreground="black") 
                penguji.configure(text="Deteksi",background="#FFCC00",foreground="black")
              
def Tran():
        listbox.delete(0,END)
        video = cv2.VideoCapture(_lbltext) 
        sds=_lbltext.split('/')
        x=len(sds)
        name_file=sds[x-1]
        listbox.insert(1, 'Location = ' + str(_lbltext))
        listbox.insert(2, 'File Name = ' + str(name_file))
        smp=name_file.split('.')
        real_name=smp[0]

        ujiFolder=sds[x-2]
        print (ujiFolder)
        if ujiFolder=="Real":
            dataset="Real"
        else:
            dataset="Fake"  
        
        fps = video.get(cv2.CAP_PROP_FPS)     
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count/fps

        listbox.insert(3, 'Frames per second = ' + str(fps))
        listbox.insert(4, 'Number of frames = ' + str(frame_count))
        listbox.insert(5, 'Duration (S) = ' + str(duration))
      
       
        minutes = int(duration/60)
        seconds = duration%60
        
        listbox.insert(6, 'Duration (M:S) = ' + str(minutes) + ':' + str(seconds))
        currentframe = 7
        i=1
        while(True): 
                ret,frame = video.read() 
                
                if ret: 
                        rs_name=real_name+'_Frame_' + str(i) +'.png'
                        name = 'DataSet_Create_Train/'+dataset+'/'+rs_name

                        cv2.imwrite(name, frame) 
                
                        CropWajah(name,rs_name)
                        listbox.insert(currentframe, 'Train .. #' + name  + "#")
                        listbox.bind('<<ListboxSelect>>', onselect_image)
                      
                        print ('Train ..' + name) 
                        currentframe += 1
                        i += 1
                else: 
                        break
        video.release()
        messagebox.showinfo("Selesai", "Ok selesai !" )

def Preprocessing():
        listbox.delete(0,END)

        video = cv2.VideoCapture(_lbltext) 
        sds=_lbltext.split('/')
        x=len(sds)
        name_file=sds[x-1]
        listbox.insert(1, 'Location = ' + str(_lbltext))
        listbox.insert(2, 'File Name = ' + str(name_file))
        smp=name_file.split('.')
        real_name=smp[0]
      
        fps = video.get(cv2.CAP_PROP_FPS)     
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count/fps

        listbox.insert(3, 'Frames per second = ' + str(fps))
        listbox.insert(4, 'Number of frames = ' + str(frame_count))
        listbox.insert(5, 'Duration (S) = ' + str(duration))
       
        minutes = int(duration/60)
        seconds = duration%60
        
        listbox.insert(6, 'Duration (M:S) = ' + str(minutes) + ':' + str(seconds))
        currentframe = 7
        i=1
        while(True): 
                ret,frame = video.read() 
                
                if ret: 
                        rs_name=real_name+'_Frame_' + str(i) +'.png'
                        name = 'Hasil_Preprocessing/'+rs_name
                        
                        cv2.imwrite(name, frame) 
                
                        CropWajah(name,rs_name)
                        listbox.insert(currentframe, 'Preprocessing .. #' + name  + "#")
                        listbox.bind('<<ListboxSelect>>', onselect_image)
                      
                        print ('Preprocessing ..' + name) 
                        currentframe += 1
                        i += 1
                        # break
                else: 
                        break
        video.release()
        messagebox.showinfo("Selesai", "Ok selesai !" )
   
   
def onselect_image(evt):
   
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    data=value.split('#')
    if len(data)  > 1:
        imagePath=data[1]
        print(imagePath)
        ShowWajah(imagePath)

def ShowWajah(imagePath):
        from PIL import Image
        im1 = Image.open(imagePath)
        im1.show()

def CropWajah(imagePath,replace_file):
       
        cascPath = "haarcascade_frontalface_default.xml"
        
        # Create the haar cascade
        faceCascade =cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
        gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
               
        )

        for (x, y, w, h) in faces:
                faces = image[y:y + h, x:x + w]
                cv2.imwrite(imagePath, faces)
      

def UjiWajah(imagePath):
      
        cascPath = "haarcascade_frontalface_default.xml"

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
        gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        Hasil="Found {0} faces!".format(len(faces))
        return Hasil

def pengujian():
        video = cv2.VideoCapture(_lbltext) 
        currentframe = 1
        while(True): 
                ret,frame = video.read() 

                if ret: 
                        name = 'Pengujian/' + str(currentframe) +'.png'
                        cv2.imwrite(name, frame) 
                
                        if currentframe==10 or currentframe==13 or currentframe==20 or currentframe==23 :
                            nila=""
                        else:
                            nila=" "    

                        nila=UjiWajah(name)
                        listbox.insert(currentframe, 'Pengujian... #' + name  + "#"+ nila)
                        listbox.bind('<<ListboxSelect>>', onselect_image)
                      
                        print ('Pengujian...' + name) 
                        currentframe += 1
                        
                else: 
                        break

        video.release()
        messagebox.showinfo("Selesai", "Sistem telah berhasil melakukan Pengujian" )         
        
# Ini adalah event saat klik proses untuk membuat frame wajah dari video yang sudah di pilih !
def click():
      
        if _lbltext=="Url File Video":
                messagebox.showinfo("Warning", "Please select the video to be processed !")
        else:   
               
               
                if proses_btn['text']=="Train":
                        messagebox.showinfo("Mulai Train", "Sistem akan melakuakn train !" )
                        Tran()     
                else:
                        # messagebox.showinfo("Mulai Train", "Sistem akan melakuakn train !" )
                        # Tran()
                        messagebox.showinfo("Mulai Preprocessing ", "Sistem akan melakukan pengujian setiap wajah pada video yang anda pilih !" )
                        Preprocessing() 
           

 
app = tkinterApp()
app.title("DeepFake")
app_w = 900
app_h = 780

#fungsi untuk menampilkan screen di tengah layar
def center_screen():
	""" gets the coordinates of the center of the screen """
	global screen_height, screen_width, x_cordinate, y_cordinate
 
	screen_width = app.winfo_screenwidth()
	screen_height = app.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
	x_cordinate = int((screen_width/2) - (app_w/2))
	y_cordinate = int((screen_height/2) - (app_h/2))
	app.geometry("{}x{}+{}+{}".format(app_w, app_h, x_cordinate, y_cordinate))
center_screen()
app.resizable(False, False) 
app.mainloop()
