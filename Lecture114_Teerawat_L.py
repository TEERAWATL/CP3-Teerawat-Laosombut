from tkinter import *
from forex_python.converter import *
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


usd_thb_2020 = []
eur_thb_2020 = []

for i in range(29):
    t = datetime(2020, 1, i+1)
    rate_usd_thb = get_rate("USD", "THB", t)
    usd_thb_2020.append(rate_usd_thb)

    rate_eur_thb = get_rate("EUR", "THB", t)
    eur_thb_2020.append(rate_eur_thb)

x = eur_thb_2020
y = usd_thb_2020


def plot_trian_model(event):
    global model
    x_model = np.array(eur_thb_2020).reshape(-1,1)
    y_model = np.array(usd_thb_2020).reshape(-1,1)
    x_trian,x_test, y_trian, y_test = train_test_split(x_model, y_model, test_size = 0.3, random_state = 5)
    model = LinearRegression()
    model.fit(x_trian,y_trian)
    y_predict = model.predict(x_model)

    fig = Figure(figsize=(4, 4), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.scatter(x, y)
    plot1.plot(x_model, y_predict)
    plot1.set_ylabel("usd_thb_2020")
    plot1.set_xlabel("eur_thb_2020")
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=200, y=50)
    label_graph = Label(window, text="USD and EUR rate exchange to THB")
    label_graph.place(x=250, y=70)
    label_graph.config(background="white")
    return model

window = Tk()
window.geometry("800x600")
window.title("USD Rate Prediction")
window.option_add("font", "tahoma bold")
window.config(background="white")


label_mian = Label(window, text="USD Rate Prediction by Linear regression")
label_mian.place(x=290, y=10)

plot_button = Button(window, text="Plot Graph and Prediction Line")
plot_button.place(x=300, y=30)
plot_button.bind('<Button-1>', plot_trian_model)


def prediction(event):
    x_value_eur = float(value_eur.get())
    x_predict_eur = np.array(x_value_eur).reshape(-1,1)
    y_value_predict = model.predict(x_predict_eur)
    for m in y_value_predict:
        label_result.configure(text= m)


abel_pavule_eur = Label(window,text="Enter Value of EUR").place(x=350, y=470)
value_eur = Entry(window)
value_eur.place(x=320, y=500)
value_eur.config(bg="light gray")



predict_button = Button(window, text="predict by Regression Model")
predict_button.place(x=300, y=550)
predict_button.bind('<Button-1>', prediction)

label_result = Button(window,text="   ")
label_result.place(x=500, y=550)
window.mainloop()
