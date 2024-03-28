from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Crop Yield Prediction")
    root.configure(background="#48D1CC")
    
    State   = tk.IntVar()
    Year = tk.IntVar()
    Season = tk.IntVar()
    Crop = tk.IntVar()
    Area = tk.DoubleVar()
    Production = tk.DoubleVar()
    Rainfall = tk.DoubleVar()
    avg_temp = tk.DoubleVar()
    PH_Value_of_Soil = tk.DoubleVar()
    Type_of_soil= tk.IntVar()
    Suitable_Fertilizer = tk.IntVar()
    
   
     
    
    
    #===================================================================================================================



    def Detect():
        e1=State.get()
        print(e1)
        e2=Year.get()
        print(e2)
        e3=Season.get()
        print(e3)
        e4=Crop.get()
        print(e4)
        e5=Area.get()
        print(e5)
        e6=Production.get()
        print(e6)
        e7=Rainfall.get()
        print(e7)
        e8=avg_temp.get()
        print(e8)
        e9=PH_Value_of_Soil.get()
        print(e9)
        e10=Type_of_soil.get()
        print(e10)
        e11= Suitable_Fertilizer.get()
        print(e11)
        
       
        
        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('E:/Ravina combine project/23CP118-Crop rec+Crop yeild prediction/crop.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
        print(v)
        yes = tk.Label(root,text="Detect Crop Yeild:" +'\n'+ str(v),background="blue",foreground="white",font=('times', 20, ' bold '),width=30)
        yes.place(x=600,y=550)
        # if v[0]==1:
        #     print("Yes")
        #     yes = tk.Label(root,text="Crop Yield Prediction \nReport is Generated",background="red",foreground="white",font=('times', 20, ' bold '),width=15)
        #     yes.place(x=300,y=100)
        #     file = open(r"D://100% project//21cg148-softwere defect//21cg148-softwere defect//Report.txt", 'w')
        #     file.write("-----Softwere Report-----\n As per input data and system model softwere defect prediction for Respective Paptien softwere."
        #                "\n***Kindly Follow info***"
                    
        #             )
        #     file.close()
            
        # else:
        #     print("No")
        #     no = tk.Label(root, text="No softwere defect \nDetected", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
        #     no.place(x=300, y=100)
        #     file = open(r"D://100% project//21cg148-softwere defect//21cg148-softwere defect//Report.txt", 'w')
        #     file.write("-----Softwere Report-----\n As per input data and system model No Softwere defect Detected for Respective softwere."
        #                "\n\n***Relax and Follow below mentioned softwere!!!***"
                    
        #             )
        #     file.close()



    l1=tk.Label(root,text="State",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l1.place(x=5,y=1)
    State=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=State)
    State.place(x=500,y=1)

    l2=tk.Label(root,text="Year",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l2.place(x=5,y=50)
    Year=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Year)
    Year.place(x=500,y=50)

    l3=tk.Label(root,text="Season",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l3.place(x=5,y=100)
    Season=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Season)
    Season.place(x=500,y=100)
    
    
    l4=tk.Label(root,text="Crop",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l4.place(x=5,y=150)
    Crop=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Crop)
    Crop.place(x=500,y=150)

    l5=tk.Label(root,text="Area",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l5.place(x=5,y=200)
    Area=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Area)
    Area.place(x=500,y=200)

    l6=tk.Label(root,text="Production",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l6.place(x=5,y=250)
    Production=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Production)
    Production.place(x=500,y=250)

    l7=tk.Label(root,text="Rainfall",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l7.place(x=5,y=300)
    Rainfall=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Rainfall)
    Rainfall.place(x=500,y=300)

    l8=tk.Label(root,text="avg_temp",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l8.place(x=5,y=350)
    avg_temp=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=avg_temp)
    avg_temp.place(x=500,y=350)

    l9=tk.Label(root,text="PH_Value_of_Soil",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l9.place(x=5,y=400)
    PH_Value_of_Soil=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PH_Value_of_Soil)
    PH_Value_of_Soil.place(x=500,y=400)

    
    l12=tk.Label(root,text="Type_of_soil",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l12.place(x=5,y=450)
    Type_of_soil=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Type_of_soil)
    Type_of_soil.place(x=500,y=450)

    l10=tk.Label(root,text="Suitable_Fertilizer",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l10.place(x=5,y=500)
    Suitable_Fertilizer=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Suitable_Fertilizer)
    Suitable_Fertilizer.place(x=500,y=500)
   

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=600)


    root.mainloop()

Train()