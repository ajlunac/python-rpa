from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as tiempoPausaNavegador

frm = Tk()
frm.title("Python RPA")

Label(frm, text="Moneda: ", font=("Arial 12")).grid(row=0, column=0)
cboListaMonedas = ttk.Combobox(frm, font=("Arial 12"))
cboListaMonedas["values"] = ("Dólar", "Euro", "Peso")
cboListaMonedas.grid(row=0, column=1)
cboListaMonedas.current(0)

def consultarItem():
    
    servicio = Service(ChromeDriverManager().install())
    elementoNavegador = webdriver.Chrome(service=servicio)
    elementoNavegador.get("https://www.google.com/")
    
    tiempoPausaNavegador.sleep(3)
    elementoNavegador.find_element(By.NAME, "q").send_keys("dolar hoy")
    tiempoPausaNavegador.sleep(2)
    elementoNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
    tiempoPausaNavegador.sleep(4)
    valorDolarGoogle = elementoNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
    tiempoPausaNavegador.sleep(2)
    
    if str(cboListaMonedas.get()) == "Euro":
        tiempoPausaNavegador.sleep(2)
        seleccionarCboGoogle = Select(elementoNavegador.find_element(By.CLASS_NAME, "l84FKc"))
        linea = 0
        for opcion in seleccionarCboGoogle.options:
            print(opcion.text)
            if opcion.text == "Euro":
                
                tiempoPausaNavegador.sleep(1)
                seleccionDropdownGoogle = elementoNavegador.find_element(By.CLASS_NAME, "l84FKc")
                tiempoPausaNavegador.sleep(1)
                itemSeleccionado = Select(seleccionDropdownGoogle)
                itemSeleccionado.select_by_index(linea)
                tiempoPausaNavegador.sleep(3)
                valorDolarGoogle = elementoNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
                tiempoPausaNavegador.sleep(1)
                break
                
            linea += 1
        
        tiempoPausaNavegador.sleep(2)
        valorMonedaSeleccionada.config(text= str(cboListaMonedas.get()) + ": " + valorDolarGoogle)
                   
    else:
        valorMonedaSeleccionada.config(text= str(cboListaMonedas.get()) + ": " + valorDolarGoogle)

btConsultar = Button(text="Consultar valor actual", font=("Arial 12"), command=consultarItem)
btConsultar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

valorMonedaSeleccionada = Label(frm, text="Valor: 0", font=("Arial 12 bold"))
valorMonedaSeleccionada.grid(row=2, column=0, columnspan=2, sticky="W")

frm.mainloop()