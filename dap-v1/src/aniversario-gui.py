from tkinter import *
from tkinter import ttk
import pandas as pd
from datetime import date
import numpy as np
from tkinter import messagebox
import win32com.client as win32

frm = Tk()
frm.title("RPA Python")

# frm.geometry("840x350")

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure(".", font=("Arial 12"), rowheight=25)

treeviewDatos = ttk.Treeview(frm, columns=(1,2,3), show="headings")
treeviewDatos.column("1", anchor=CENTER)
treeviewDatos.heading("1", text="Nombre")
treeviewDatos.column("2", anchor=CENTER)
treeviewDatos.heading("2", text="Fecha_Nacimiento")
treeviewDatos.column("3", anchor=CENTER)
treeviewDatos.heading("3", text="Email")
treeviewDatos.grid(row=2, column=0, columnspan=8, sticky=NSEW)

archivoAniversario = pd.read_csv(r"dap-v1\data\aniversarios.csv")
archivoAniversario['Fecha_Nacimiento'] = archivoAniversario['Fecha_Nacimiento'].astype(str)

archivoAniversario["Anio"] = archivoAniversario["Fecha_Nacimiento"].str[:4]
archivoAniversario["Mes"] = archivoAniversario["Fecha_Nacimiento"].str[5:7]
archivoAniversario["Dia"] = archivoAniversario["Fecha_Nacimiento"].str[-2:]

archivoAniversario["Fecha_Actual"] = date.today()
archivoAniversario["Fecha_Actual"] = archivoAniversario["Fecha_Actual"].astype(str)
archivoAniversario["Anio_Actual"] = archivoAniversario["Fecha_Actual"].str[:4]
archivoAniversario["Mes_Actual"] = archivoAniversario["Fecha_Actual"].str[5:7]
archivoAniversario["Dia_Actual"] = archivoAniversario["Fecha_Actual"].str[-2:]

archivoAniversario["Aniversario"] = np.where((archivoAniversario["Mes"] == archivoAniversario["Mes_Actual"]) &
                                                (archivoAniversario["Dia"] == archivoAniversario["Dia_Actual"]), "Si", "")

archivoAniversario = archivoAniversario.loc[archivoAniversario["Aniversario"] != "", ["Nombre", "Fecha_Nacimiento", "Email"]]

for linea in range(len(archivoAniversario)):
    treeviewDatos.insert("", END, values=(str(archivoAniversario.iloc[linea,0]), 
                                            str(archivoAniversario.iloc[linea,1]), 
                                            str(archivoAniversario.iloc[linea,2])))  

def eliminarItemTreeview():
    itemsSeleccionados = treeviewDatos.selection()
    for itemSeleccionado in itemsSeleccionados:
        treeviewDatos.delete(itemSeleccionado)
        
        messagebox.showinfo("Información", "El item se eliminó correctamente")
        
        numeroLineas()
    
btnEliminar = Button(text="Eliminar", font="Arial 12", command=eliminarItemTreeview)
btnEliminar.grid(row=1, column=0, columnspan=2, sticky=NSEW)


lblNombre = Label(text="Nombre: ", font="Arial 12")
lblNombre.grid(row=0, column=0, sticky="W")

txtNombre = Entry(font="Arial 12")
txtNombre.grid(row=0, column=1, sticky="W")

lblFechaNacimiento = Label(text="Fecha de Nacimiento: ", font="Arial 12")
lblFechaNacimiento.grid(row=0, column=2, sticky="W")

txtFechaNacimiento = Entry(font="Arial 12")
txtFechaNacimiento.grid(row=0, column=3, sticky="W")

lblEmail = Label(text="Email: ", font="Arial 12")
lblEmail.grid(row=0, column=4, sticky="W")

txtEmail = Entry(font="Arial 12")
txtEmail.grid(row=0, column=5, sticky="W")

def addItemsTreeview():
    
    if txtNombre.get() == "":
        messagebox.showinfo("Información", "El campo Nombre es obligatorio")
    elif txtFechaNacimiento.get() == "":
        messagebox.showinfo("Información", "El campo Fecha de Nacimiento es obligatorio")
    elif txtEmail.get() == "":
        messagebox.showinfo("Información", "El campo Email es obligatorio")
    else:
        treeviewDatos.insert("", END, values=(str(txtNombre.get()), 
                                            str(txtFechaNacimiento.get()), 
                                            str(txtEmail.get())))
    
        messagebox.showinfo("Información", "El item se agregó correctamente")
        
        numeroLineas()
        
        txtNombre.delete(0, END)
        txtFechaNacimiento.delete(0, END)
        txtEmail.delete(0, END)

btnAdicionar = Button(text="Adicionar", font="Arial 12", command=addItemsTreeview)
btnAdicionar.grid(row=1, column=2, columnspan=2, sticky=NSEW)

def actualizarItemsTreeview():
    
    if len(treeviewDatos.selection()) == 0:
        messagebox.showinfo("Información", "Debe seleccionar un item para actualizar")
        return
    
    if txtNombre.get() == "":
        messagebox.showinfo("Información", "El campo Nombre es obligatorio")
    elif txtFechaNacimiento.get() == "":
        messagebox.showinfo("Información", "El campo Fecha de Nacimiento es obligatorio")
    elif txtEmail.get() == "":
        messagebox.showinfo("Información", "El campo Email es obligatorio")
    else:
        itemsSeleccionado = treeviewDatos.selection()[0]
        treeviewDatos.item(itemsSeleccionado, values=(str(txtNombre.get()),
                                                        str(txtFechaNacimiento.get()),
                                                        str(txtEmail.get())))
        messagebox.showinfo("Información", "El item se actualizó correctamente")
        txtNombre.delete(0, END)
        txtFechaNacimiento.delete(0, END)
        txtEmail.delete(0, END)
                        
    

btnActualizar = Button(text="Actulizar", font="Arial 12", command=actualizarItemsTreeview)
btnActualizar.grid(row=1, column=4, columnspan=2, sticky=NSEW)


def crearEmail():
    for numeroLinea in treeviewDatos.get_children():
        
        # Email para enviar desde Outlook.
        outlook = win32.Dispatch('outlook.application')
        emailOutlook = outlook.CreateItem(0)
        
        nombre = treeviewDatos.item(numeroLinea)["values"][0]
        aniversario = treeviewDatos.item(numeroLinea)["values"][1]
        email = treeviewDatos.item(numeroLinea)["values"][2]
        
        primerNombre = nombre.split(" ")[0]
        
        emailOutlook.To = email
        emailOutlook.Subject = 'Feliz Aniversario!' + str(nombre)
        emailOutlook.HtmlBody = f"""
        <p>Felicidades, <b>{primerNombre}!</b></p>
        <p><font color="blue">Este es un correo de prueba para el envío de un correo electrónico con Python.</font></p>
        <p><a href="https://www.python.org/">Visita Python</a></p>
        <p>Saludos,</p>
        <p><img src=r"img/python-logo.png" alt="Logo Python"></p>
        """
        emailOutlook.save()
        
    messagebox.showinfo("Información", "Emails creados correctamente!")

btnCrearEmail = Button(text="Crear email", font="Arial 12", command=crearEmail)
btnCrearEmail.grid(row=1, column=6, columnspan=2, sticky=NSEW)

lblNumeroLineas = Label(text="Número de lineas: ", font="Arial 12")
lblNumeroLineas.grid(row=4, column=0, columnspan=8, sticky="W")

def numeroLineas(item=""):
    numero = 0
    lineas = treeviewDatos.get_children(item)
    for linea in lineas:
        numero += 1
    
    lblNumeroLineas.config(text="Aniversariantes: " + str(numero))
    
numeroLineas()

def pasarDatosTextbox(Event):
    item = treeviewDatos.selection()
    for linea in item:
        txtNombre.delete(0, END)
        txtFechaNacimiento.delete(0, END)
        txtEmail.delete(0, END)
        
        txtNombre.insert(0, treeviewDatos.item(linea)["values"][0])
        txtFechaNacimiento.insert(0, treeviewDatos.item(linea)["values"][1])  
        txtEmail.insert(0, treeviewDatos.item(linea)["values"][2])  
        

treeviewDatos.bind("<Double-1>", pasarDatosTextbox)


frm.mainloop()
