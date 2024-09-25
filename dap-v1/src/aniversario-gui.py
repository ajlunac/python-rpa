from tkinter import *
from tkinter import ttk
import pandas as pd
from datetime import date
import numpy as np
from tkinter import messagebox

frm = Tk()
frm.title("RPA Python")

frm.geometry("840x350")

estilo = ttk.Style()
estilo.theme_use("clam")

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
        txtNombre.delete(0, END)
        txtFechaNacimiento.delete(0, END)
        txtEmail.delete(0, END)

btnAdicionar = Button(text="Adicionar", font="Arial 12", command=addItemsTreeview)
btnAdicionar.grid(row=1, column=2, columnspan=2, sticky=NSEW)

def actualizarItemsTreeview():
    if txtNombre.get() == "":
        messagebox.showinfo("Información", "El campo Nombre es obligatorio")
    elif txtFechaNacimiento.get() == "":
        messagebox.showinfo("Información", "El campo Fecha de Nacimiento es obligatorio")
    elif txtEmail.get() == "":
        messagebox.showinfo("Información", "El campo Email es obligatorio")
    else:
        itemsSeleccionados = treeviewDatos.selection()[0]
        treeviewDatos.item(itemsSeleccionados, values=(str(txtNombre.get()),
                                                        str(txtFechaNacimiento.get()),
                                                        str(txtEmail.get())))
        messagebox.showinfo("Información", "El item se actualizó correctamente")
        txtNombre.delete(0, END)
        txtFechaNacimiento.delete(0, END)
        txtEmail.delete(0, END)
                        
    

btnActualizar = Button(text="Actulizar", font="Arial 12", command=actualizarItemsTreeview)
btnActualizar.grid(row=1, column=4, columnspan=2, sticky=NSEW)


frm.mainloop()
