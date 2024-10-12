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
    
lblNome = Label(text="Nome: ", font=("Arial", 12))
lblNome.grid(row=0, column=0, sticky="w")

txtNome = Entry(font=("Arial", 12))
txtNome.grid(row=0, column=1, sticky="w")

lblEmail = Label(text="Email: ", font=("Arial", 12))
lblEmail.grid(row=0, column=2, sticky="w")

txtEmail = Entry(font=("Arial", 12))
txtEmail.grid(row=0, column=3, sticky="w")

lblSexo = Label(text="Sexo: ", font=("Arial", 12))
lblSexo.grid(row=0, column=4, sticky="w")

txtSexo = Entry(font=("Arial", 12))
txtSexo.grid(row=0, column=5, sticky="w")

lblEstado = Label(text="Estado: ", font=("Arial", 12))
lblEstado.grid(row=0, column=6, sticky="w")

txtEstado = Entry(font=("Arial", 12))
txtEstado.grid(row=0, column=7, sticky="w")

lblCorFavorita = Label(text="Cor Favorita: ", font=("Arial", 12))
lblCorFavorita.grid(row=0, column=8, sticky="w")

txtCorFavorita = Entry(font=("Arial", 12))
txtCorFavorita.grid(row=0, column=9, sticky="w")

def limpiarCampos():
    
    # Limpiar los campos de texto.	
    txtNome.delete(0, END)
    txtEmail.delete(0, END)
    txtSexo.delete(0, END)
    txtEstado.delete(0, END)
    txtCorFavorita.delete(0, END)


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
                
btnLlenadoEnMasa = Button(frm, text="Rellenar Formulario en Masa", font=( "Arial", 12), command=rellenarEnMasa)
btnLlenadoEnMasa.grid(row=1, column=0, columnspan=2, sticky="nsew")

def addItemTreview():
    
    if txtNome.get() == "":
        messagebox.showwarning("Atención", "El campo Nome no puede estar vacío.")
    elif txtEmail.get() == "":
        messagebox.showwarning("Atención", "El campo Email no puede estar vacío.")
    elif txtSexo.get() == "":
        messagebox.showwarning("Atención", "El campo Sexo no puede estar vacío.")
    elif txtEstado.get() == "":
        messagebox.showwarning("Atención", "El campo Estado no puede estar vacío.")
    elif txtCorFavorita.get() == "":
        messagebox.showwarning("Atención", "El campo Cor Favorita no puede estar vacío.")
    else:
        treeviewDatos.insert("", "end", values=(str(txtNome.get()), 
                                                str(txtEmail.get()), 
                                                str(txtSexo.get()), 
                                                str(txtEstado.get()), 
                                                str(txtCorFavorita.get())))
        
        messagebox.showinfo("Información", "Datos agregados correctamente.")
        	
        limpiarCampos()
        
        

btnAdicionar = Button(frm, text="Adicionar", font=( "Arial", 12), command=addItemTreview)
btnAdicionar.grid(row=1, column=2, columnspan=2, sticky="nsew")

def actualizarItemTreview():
    
    if txtNome.get() == "":
        messagebox.showwarning("Atención", "El campo Nome no puede estar vacío.")
    elif txtEmail.get() == "":
        messagebox.showwarning("Atención", "El campo Email no puede estar vacío.")
    elif txtSexo.get() == "":
        messagebox.showwarning("Atención", "El campo Sexo no puede estar vacío.")
    elif txtEstado.get() == "":
        messagebox.showwarning("Atención", "El campo Estado no puede estar vacío.")
    elif txtCorFavorita.get() == "":
        messagebox.showwarning("Atención", "El campo Cor Favorita no puede estar vacío.")
    else:

        # Selecciona la fila seleccionada en el treeviewDatos.
        itemSeleccionado = treeviewDatos.selection()[0]
        
        treeviewDatos.item(itemSeleccionado, values=(str(txtNome.get()), 
                                                str(txtEmail.get()), 
                                                str(txtSexo.get()), 
                                                str(txtEstado.get()), 
                                                str(txtCorFavorita.get())))
        
        messagebox.showinfo("Información", "Datos actualizados correctamente.")
        
        limpiarCampos()
        
        

btnActualizar = Button(frm, text="Actualizar", font=( "Arial", 12), command=actualizarItemTreview)
btnActualizar.grid(row=1, column=4, columnspan=2, sticky="nsew")

def pasarDatosSeleccionados(Event):
    
    item = treeviewDatos.selection()
    
    for i in item:
        
        limpiarCampos()
        
        txtNome.insert(0, treeviewDatos.item(i)["values"][0])
        txtEmail.insert(0, treeviewDatos.item(i)["values"][1])
        txtSexo.insert(0, treeviewDatos.item(i)["values"][2])
        txtEstado.insert(0, treeviewDatos.item(i)["values"][3])
        txtCorFavorita.insert(0, treeviewDatos.item(i)["values"][4])
    
#  Pasar los datos seleccionados en el treeviewDatos al campo de texto.
treeviewDatos.bind("<Double-1>", pasarDatosSeleccionados)


def eliminarItemTreview():
    
    # Selecciona la fila seleccionada en el treeviewDatos.
    itemsSeleccionado = treeviewDatos.selection()
    
    # Elimina la fila seleccionada.
    for itemSeleccionado in itemsSeleccionado:
        
        treeviewDatos.delete(itemSeleccionado)
        
        messagebox.showinfo("Información", "Datos eliminados correctamente.")
        
        limpiarCampos()

btnEliminar = Button(frm, text="Eliminar", font=( "Arial", 12), command=eliminarItemTreview)
btnEliminar.grid(row=1, column=6, columnspan=2, sticky="nsew")


def rellenarFormulario():
    
    if txtNome.get() == "":
        messagebox.showwarning("Atención", "El campo Nome no puede estar vacío.")
    elif txtEmail.get() == "":
        messagebox.showwarning("Atención", "El campo Email no puede estar vacío.")
    elif txtSexo.get() == "":
        messagebox.showwarning("Atención", "El campo Sexo no puede estar vacío.")
    elif txtEstado.get() == "":
        messagebox.showwarning("Atención", "El campo Estado no puede estar vacío.")
    elif txtCorFavorita.get() == "":
        messagebox.showwarning("Atención", "El campo Cor Favorita no puede estar vacío.")
    else:
        
        # Verifica la version de chrome y descarga el driver correspondiente.
        service = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=service)

        # Abre el navegador y ingresa a la página de SurveyMonkey que contiene un formulario.
        navegador.get("https://pt.surveymonkey.com/r/79WHF9G")

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(3)

        # Rellenar el campo de nombre.
        navegador.find_element(By.NAME, "112904979").send_keys(txtNome.get())

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(1)

        # Rellenar el campo de email.
        navegador.find_element(By.ID, "112904987").send_keys(txtEmail.get())

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(1)

        if txtSexo.get() == "Masculino":
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
            
            if item.text == str(txtEstado.get()):
                
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
        navegador.find_element(By.NAME, "112905214").send_keys(txtCorFavorita.get())

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(1)

        # Clickear en el botón de enviar.
        navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()

        # Tiempo del coputador pra procesar la informacion.
        tiempoPausaComputador.sleep(2)
        
        messagebox.showinfo("Información", "Formulario rellenado correctamente.")
        
        limpiarCampos()
        

btnLlenarFormulario = Button(frm, text="Llenar Formulario", font=( "Arial", 12), command=rellenarFormulario)
btnLlenarFormulario.grid(row=1, column=8, columnspan=2, sticky="nsew")

# Visualizar la ventana.
frm.mainloop()


