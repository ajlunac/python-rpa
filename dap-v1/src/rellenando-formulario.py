# Importamos las librearias necesarias para la ejecución del script.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyautogui as tiempoPausaComputador
import pandas as pd

# Abre el archivo de datos de Excel.
datosExcel = pd.read_excel(r"dap-v1\data\datos_formulario.xlsx")

# Formulario de Tkinter.
frm = Tk()
frm.title("RPA Python - Rellenando Formulario Web")
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("TLabel", font=("Arial", 12), rowheight=40)

# Se crea un Treeview para mostrar los datos del formulario.
treeviewDatos = ttk.Treeview(frm, columns=(1,2,3,4,5), show='headings')
treeviewDatos.column(1, anchor='center')
treeviewDatos.heading(1, text='Nome')
treeviewDatos.column(2, anchor='center')
treeviewDatos.heading(2, text='Email')
treeviewDatos.column(3, anchor='center')
treeviewDatos.heading(3, text='Sexo')
treeviewDatos.column(4, anchor='center')
treeviewDatos.heading(4, text='Estado')
treeviewDatos.column(5, anchor='center')
treeviewDatos.heading(5, text='Cor Favorita')
treeviewDatos.grid(row=2, column=0, columnspan=10, sticky="nsew")

for linea in range(len(datosExcel)):
    
    treeviewDatos.insert("", "end", values=(str(datosExcel.iloc[linea, 0]), 
                                            str(datosExcel.iloc[linea, 1]), 
                                            str(datosExcel.iloc[linea, 2]), 
                                            str(datosExcel.iloc[linea, 3]), 
                                            str(datosExcel.iloc[linea, 4])))


def rellenarEnMasa():
    
    # Pasa línea por lína del treeviewDatos.
    for child in treeviewDatos.get_children():
        
        linea = treeviewDatos.item(child)["values"]

        columnaNome = linea[0]
        columnaEmail = linea[1]
        columnaSexo = linea[2]
        columnaEstado = linea[3]
        columnaCorFavorita = linea[4]
        
        # Verifica la version de chrome y descarga el driver correspondiente.
        service = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=service)

        # Abre el navegador y ingresa a la página de SurveyMonkey que contiene un formulario.
        navegador.get("https://pt.surveymonkey.com/r/79WHF9G")

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(3)

        # Rellenar el campo de nombre.
        navegador.find_element(By.NAME, "112904979").send_keys(columnaNome)

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(1)

        # Rellenar el campo de email.
        navegador.find_element(By.ID, "112904987").send_keys(columnaEmail)

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(1)

        if columnaSexo == "Masculino":
           # Clickear en el radio button de género masculino.
            navegador.find_element(By.ID, "112905004_855492046_label").click()
        else:
            # Clickear en el radio button de género femenino.
            navegador.find_element(By.ID, "112905004_855492047_label").click()

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(2)

        # Selecciona la opción del estado de la lista de estados.
        selectEstado = Select(navegador.find_element(By.ID, "112905103"))

        linea = 0
        
        for item in selectEstado.options:
            
            if item.text == str(columnaEstado):
                
                tiempoPausaComputador.sleep(1)
                
                selectItemEstado = navegador.find_element(By.ID, "112905103")
                
                tiempoPausaComputador.sleep(1)
                
                itemSeleccionado = Select(selectItemEstado)
                
                tiempoPausaComputador.sleep(1)
                
                itemSeleccionado.select_by_index(linea)
                
                break
            
            linea += 1

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(1)

        # Rellenar el campo de cor favorite.
        navegador.find_element(By.NAME, "112905214").send_keys(columnaCorFavorita)

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(1)

        # Clickear en el botón de enviar.
        navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(2)
                
btnLlenadoEnMasa = Button(frm, text="Llenar Formulario en Masa", font=( "Arial", 12), command=rellenarEnMasa)
btnLlenadoEnMasa.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Visualizar la ventana.
frm.mainloop()


