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
    root.title("Crop_Recommendation_System")
    root.configure(background="#65B8C9")
    
    N = tk.IntVar() 
    P = tk.IntVar()
    K = tk.IntVar()
    temperature = tk.DoubleVar()
    humidity = tk.DoubleVar()
    ph = tk.DoubleVar()
    rainfall = tk.DoubleVar()
    
    #===================================================================================================================
    def Detect():
        e1= N.get()
        print(e1)
        e2= P.get()
        print(e2)
        e3= K.get()
        print(e3)
        e4= temperature.get()
        print(e4)
        e5= humidity.get()
        print(e5)
        e6= ph.get()
        print(e6)
        e7= rainfall.get()
        print(e7)
        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('E:/Ravina combine project/Crop Recommendation/crop_rec.joblib')
        v= a1.predict([[e1,e2,e3,e4,e5,e6,e7]])
        
        print(v)
        if v[0]==0:
            print("Maize")
            yes = tk.Label(root,text="Maize \n Price: 300",background="brown",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=300,y=600)
                     
        elif v[0]==1:
            print("rice")
            no = tk.Label(root, text="rice \n Price: 600", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=300, y=600)
        
        elif v[0]==2:
            print("Chickpea")
            no = tk.Label(root, text="Chickpea \n Price: 380", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=300, y=600) 
              
        elif v[0]==3:
              print("Kidneybeans")
              no = tk.Label(root, text="Kidneybeans \n Price: 400", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
              no.place(x=300, y=600)
                  
        elif v[0]==4:
             print("pigeonpeas")
             no = tk.Label(root, text="pigeonpeas \n Price: 900", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
             no.place(x=300, y=600)
                 
        elif v[0]==5:
                    print("blackgrams")
                    no = tk.Label(root, text="blackgrams \n Price: 700", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                    no.place(x=300, y=600)
                    
        elif v[0]==6:
                 print("lentil")
                 no = tk.Label(root, text="lentil \n Price: 400", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                 no.place(x=300, y=600)
                 
        elif v[0]==7:
                 print("Pomegrante")
                 no = tk.Label(root, text="Pomegrante \n Price: 300", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                 no.place(x=300, y=600)
                 
        elif v[0]==8:
                 print("Banana")
                 no = tk.Label(root, text="Banana \n Price: 400", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                 no.place(x=300, y=600)
                 
        elif v[0]==9:
                 print("Mango")
                 no = tk.Label(root, text="Mango \n Price: 870", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                 no.place(x=300, y=600)
                 
        elif v[0]==10:
                 print("Grapes")
                 no = tk.Label(root, text="Grapes \n Price: 290", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                 no.place(x=300, y=600)
                 
        elif v[0]==11:
                 print("Watermelon")
                 no = tk.Label(root, text="Watermelon \n Price: 760", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                 no.place(x=300, y=600)
                 
                 
        elif v[0]==12:
                 print("Muskmelon")
                 no = tk.Label(root, text="Muskmelon \n Price: 876", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
                 no.place(x=300, y=600)
                 
        elif v[0]==13:
             print("Apple")
             no = tk.Label(root, text="Apple \n Price: 870", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
             no.place(x=300, y=600)
                                                                                    
        elif v[0]==14:
              print("Orange")
              no = tk.Label(root, text="Orange \n Price: 490", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
              no.place(x=300, y=600)
 
        elif v[0]==15:
              print("Papaya")
              no = tk.Label(root, text="Papaya \n Price: 100", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
              no.place(x=300, y=600)
              
        elif v[0]==16:
              print("Coconut")
              no = tk.Label(root, text="Coconut \n Price: 430", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
              no.place(x=300, y=600)
              
        elif v[0]==17:
             print("Cotton")
             no = tk.Label(root, text="Cotton \n Price: 250", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
             no.place(x=300, y=600)  

        elif v[0]==18:
             print("Jute")
             no = tk.Label(root, text="Jute \n Price: 650", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
             no.place(x=300, y=600)  
             
        elif v[0]==19:
               print("Coffee")
               no = tk.Label(root, text="Coffee \n Price: 1000", background="brown", foreground="white",font=('times', 20, ' bold '),width=15)
               no.place(x=300, y=600) 
         
        else:
           print("No Crop")
           no = tk.Label(root, text="Low", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
           no.place(x=600, y=500)
        
                                                                                        
                                                                                                                                                                                                                                                     

   
    l7=tk.Label(root,text="N",background="olive",font=('times', 20, ' bold '),width=15)
    l7.place(x=5,y=100)
    N=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=N)
    N.place(x=400,y=100)    

    l1=tk.Label(root,text="P",background="olive",font=('times', 20, ' bold '),width=15)
    l1.place(x=5,y=150)
    P=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=P)
    P.place(x=400,y=150)

    l2=tk.Label(root,text="K",background="olive",font=('times', 20, ' bold '),width=15)
    l2.place(x=5,y=200)
    K=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=K)
    K.place(x=400,y=200)
    
    l3=tk.Label(root,text="temperature",background="olive",font=('times', 20, ' bold '),width=15)
    l3.place(x=5,y=250)
    temperature=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=temperature)
    temperature.place(x=400,y=250)
    
    l6=tk.Label(root,text="humidity",background="olive",font=('times', 20, ' bold '),width=15)
    l6.place(x=5,y=300)
    temperature=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=humidity)
    temperature.place(x=400,y=300)
    
    l4=tk.Label(root,text="ph",background="olive",font=('times', 20, ' bold '),width=15)
    l4.place(x=5,y=350)
    ph=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=ph)
    ph.place(x=400,y=350)
    
    l5=tk.Label(root,text="rainfall",background="olive",font=('times', 20, ' bold '),width=15)
    l5.place(x=5,y=400)
    rainfall=tk.Entry(root,bd=2,width=20,font=("TkDefaultFont", 20),textvar=rainfall)
    rainfall.place(x=400,y=400)
   
   
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=500)

    


    root.mainloop()

Train()