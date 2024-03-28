from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Crop Yeild and Price Prediction Using Machine Learning")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image2 = Image.open('p.jpg')
image2 = image2.resize((w,h))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Crop Yeild and Price Prediction Using Machine Learning", font=('times', 30,' bold '), height=1, width=59,bg="#2E8B57",fg="white")
lbl.place(x=0, y=10)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Model_Training():
    data = pd.read_csv("E:/Ravina combine project/23CP118-Crop rec+Crop yeild prediction/test.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    # le = LabelEncoder()
    # data['Date of Booking'] = le.fit_transform(data['Date of Booking'])

    # data['Date of Journey'] = le.fit_transform(data['Date of Journey'])
    # data['Airline-Class'] = le.fit_transform(data['Airline-Class'])
    # data['Departure Time'] = le.fit_transform(data['Departure Time'])
    # data['Arrival Time'] = le.fit_transform(data['Arrival Time'])
    # data['Duration'] = le.fit_transform(data['Duration'])
    # data['Total Stops'] = le.fit_transform(data['Total Stops'])
   
   

    """Feature Selection => Manual"""
    x = data.drop(['Crop_yield'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Crop_yield']
    print(type(y))
    x.shape
    

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.10,random_state=123)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)
    
    # from sklearn.tree import DecisionTreeClassifier
    # svcclassifier = DecisionTreeClassifier()
    # svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=305,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as crop.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=305,y=420)
    from joblib import dump
    dump (svcclassifier,"crop.joblib")
    print("Model saved as crop.joblib")



def check():
    from subprocess import call
    call(["python","Check_Prediction.py"])




def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=120)

button3 = tk.Button(root, foreground="white", background="black", font=("times", 14, "bold"),
                    text="Model Training", command=Model_Training, width=19, height=2)
button3.place(x=20, y=200)

button4 = tk.Button(root, foreground="white", background="black", font=("times", 14, "bold"),
                    text=" Detection", command=check, width=19, height=2)
button4.place(x=20, y=280)
exit = tk.Button(root, text="Exit", command=window, width=19, height=2, font=('times', 14, ' bold '),bg="brown",fg="white")
exit.place(x=20, y=380)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''