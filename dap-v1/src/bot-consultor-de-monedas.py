from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pyautogui as tiempoPausaNavegador

frm = Tk()
frm.title("Python RPA - Consultar valor del Dólar y Euro")


Label(frm, text="Moneda: ", font=("Arial 12")).grid(row=0, column=0)
cboSeleccionado = ttk.Combobox(frm, font=("Arial 12"))
cboSeleccionado["values"] = ("Dólar", 
                             "Euro", 
                             "Peso")

cboSeleccionado.grid(row=0, column=1)

cboSeleccionado.current(0)

servicio = Service(ChromeDriverManager().install())
miNavegador = webdriver.Chrome(service=servicio)

def consultarItem():

    miNavegador.get("https://www.google.com/")

    tiempoPausaNavegador.sleep(3)

    miNavegador.find_element(By.NAME, "q").send_keys("dolar hoy")

    tiempoPausaNavegador.sleep(2)

    miNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

    tiempoPausaNavegador.sleep(4)

    valorDolarGoogle = miNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

    tiempoPausaNavegador.sleep(2)

    print("El valor del dólar en Google es:", valorDolarGoogle)
    
    valorMoneda.config(text= str(cboSeleccionado.get()) + ": " + valorDolarGoogle)

btConsultar = Button(text="Consultar", font=("Arial 12"), command=consultarItem)
btConsultar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

valorMoneda = Label(frm, text="Valor: 0", font=("Arial 12 bold"))
valorMoneda.grid(row=2, column=0, columnspan=2, sticky="W")

frm.mainloop()