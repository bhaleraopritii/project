from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Crop_Recommendation_System")
    root.configure(background="#65B8C9")
    
    year = tk.IntVar() 
    crop = tk.StringVar()
    month = tk.IntVar()
    rainfall = tk.DoubleVar()
    
    
    #===================================================================================================================
    def Detect():
        e1= year.get()
        print(e1)
        e2= crop.get()
        if e2=="Paddy":
            e2=0
        elif e2=="Jowar":
            e2=1
        elif e2=="Bajara":
            e2=2
        elif e2=="Maize":
            e2=3
        elif e2=="Wheat":
            e2=4
        elif e2=="Barley":
            e2=5
        elif e2=="Gram":
            e2=6
        elif e2=="Arhar":
            e2=7
        elif e2=="Moong":
            e2=8
        else: 
            e2=9
        print(e2)
        e3= month.get()
        print(e3)
        e4= rainfall.get()
        print(e4)
        
        
        
        
        #########################################################################################
        

        from joblib import dump , load
        a1=load('E:/Ravina combine project/23CP118-Crop rec+Crop yeild prediction/crop_rec11.joblib')
        v= a1.predict([[e1,e2,e3,e4]])
        
        print(v)
        yes = tk.Label(root,text="Detect Crop price:" +'\n'+ str(v),background="blue",foreground="white",font=('times', 20, ' bold '),width=30)
        yes.place(x=600,y=500)
        
                                                                                        
                                                                                                                                                                                                                                                     

   
    # l7=tk.Label(root,text="year",background="olive",font=('times', 20, ' bold '),width=15)
    # l7.place(x=5,y=100)
    # N=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=year)
    # N.place(x=400,y=100)    

    # l1=tk.Label(root,text="crop",background="olive",font=('times', 20, ' bold '),width=15)
    # l1.place(x=5,y=150)
    # P=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=crop)
    # P.place(x=400,y=150)

    # l2=tk.Label(root,text="month",background="olive",font=('times', 20, ' bold '),width=15)
    # l2.place(x=5,y=200)
    # K=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=month)
    # K.place(x=400,y=200)
    
    frame_alpr1 = tk.LabelFrame(root, text="Date", width=230, height=130, bd=5, font=('times', 14, ' bold '),fg="blue",bg="skyblue")
    frame_alpr1.grid(row=0, column=0, sticky='nw')
    frame_alpr1.place(x=510, y=100)

    l1=tk.Label(frame_alpr1,text="Month",background="skyblue",font=('times', 10, ' bold '),width=15)
    l1.place(x=1,y=1)
    Date=tk.Entry(frame_alpr1,bd=2,width=5,font=("TkDefaultFont", 20),textvar=month)
    Date.place(x=15,y=25)


    l2=tk.Label(frame_alpr1,text="Year",background="skyblue",font=('times', 10, ' bold '),width=15)
    l2.place(x=100,y=1)
    Date=tk.Entry(frame_alpr1,bd=2,width=5,font=("TkDefaultFont", 20),textvar=year)
    Date.place(x=120,y=25)

    l4=tk.Label(root,text="Rainfall",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
    l4.place(x=400,y=290)
    rain=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=rainfall)
    rain.place(x=700,y=290)
   
    l3=tk.Label(root,text="Crop",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
    l3.place(x=400,y=340)
    monthchoosen= ttk.Combobox(root, width = 27, textvariable = crop)
   # Adding combobox drop down list
    monthchoosen['values'] = (' Paddy',
   						   ' Jowar',
   						   ' Bajara',
                           'Maize',
                           'Wheat',
                           'Barley',
                           'Gram',
						   'Arhar',
                            'Moong',
                            'Urad',)
    monthchoosen.place(x=700,y=340)
   #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=500)
    def cl():
        root.destroy()
        from subprocess import call
        call(["python","Check1.py"])
        

    button2 = tk.Button(root,text="Clear",command=cl,font=('times', 20, ' bold '),width=10)
    button2.place(x=300,y=570)


    root.mainloop()

Train()