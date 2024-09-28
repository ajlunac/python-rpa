import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

frm = Tk()
frm.title("RPA Python - Generador de Certificados")

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure(".", font=("Arial 12"), rowheight=30)

treeviewDatos = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6), show="headings")

treeviewDatos.column(1, anchor="center")
treeviewDatos.heading(1, text="Dirección")

treeviewDatos.column(2, anchor="center")
treeviewDatos.heading(2, text="Nombre")

treeviewDatos.column(3, anchor="center")
treeviewDatos.heading(3, text="Numero Documento")

treeviewDatos.column(4, anchor="center")
treeviewDatos.heading(4, text="Fecha Inicial")

treeviewDatos.column(5, anchor="center")
treeviewDatos.heading(5, text="Fecha Final")

treeviewDatos.column(6, anchor="center")
treeviewDatos.heading(6, text="Email")

treeviewDatos.grid(row=4, column=0, columnspan=6, sticky="nsew", pady=15)

def pasarDatosTreeview(event):
    itemSeleccionado = treeviewDatos.selection()
    for columna in itemSeleccionado:
        txtDireccion.delete(0, END)
        txtNombre.delete(0, END)
        txtDocumento.delete(0, END)
        txtFechaInicial.delete(0, END)
        txtFechaFinal.delete(0, END)
        txtEmail.delete(0, END)
        
        txtDireccion.insert(0, treeviewDatos.item(columna, "values")[0])
        txtNombre.insert(0, treeviewDatos.item(columna, "values")[1])
        txtDocumento.insert(0, treeviewDatos.item(columna, "values")[2])
        txtFechaInicial.insert(0, treeviewDatos.item(columna, "values")[3])
        txtFechaFinal.insert(0, treeviewDatos.item(columna, "values")[4])
        txtEmail.insert(0, treeviewDatos.item(columna, "values")[5])
        




treeviewDatos.bind("<Double-1>", pasarDatosTreeview)

datosUsuarios = pd.read_csv(r"dap-v1\data\datosCertificados.csv")

datosUsuarios["Fecha_Inicial"] = datosUsuarios["Fecha_Inicial"].astype(str)
datosUsuarios["Fecha_Final"] = datosUsuarios["Fecha_Final"].astype(str)

for linea in range(len(datosUsuarios)):
    treeviewDatos.insert("", "end", values=(str(datosUsuarios.iloc[linea, 0]),
                                            str(datosUsuarios.iloc[linea, 1]),
                                            str(datosUsuarios.iloc[linea, 2]),
                                            str(datosUsuarios.iloc[linea, 3]),
                                            str(datosUsuarios.iloc[linea, 4]),
                                            str(datosUsuarios.iloc[linea, 5]),))
    

lblDireccion = Label(text="Dirección: ", font=("Arial 12"))
lblDireccion.grid(row=0, column=0, sticky="E", pady=15)
txtDireccion = Entry(font=("Arial 12"))
txtDireccion.grid(row=0, column=1, sticky="W", pady=15)

lblNombre = Label(text="Nombre: ", font=("Arial 12"))
lblNombre.grid(row=0, column=2, sticky="E", pady=15)
txtNombre = Entry(font=("Arial 12"))
txtNombre.grid(row=0, column=3, sticky="W", pady=15)

lblDocumento = Label(text="Numero Documento: ", font=("Arial 12"))
lblDocumento.grid(row=0, column=4, sticky="E", pady=15)
txtDocumento = Entry(font=("Arial 12"))
txtDocumento.grid(row=0, column=5, sticky="W", pady=15)

lblFechaInicial = Label(text="Fecha Inicial: ", font=("Arial 12"))
lblFechaInicial.grid(row=1, column=0, sticky="E", pady=15)
txtFechaInicial = Entry(font=("Arial 12"))
txtFechaInicial.grid(row=1, column=1, sticky="W", pady=15)

lblFechaFinal = Label(text="Fecha Final: ", font=("Arial 12"))
lblFechaFinal.grid(row=1, column=2, sticky="E", pady=15)
txtFechaFinal = Entry(font=("Arial 12"))
txtFechaFinal.grid(row=1, column=3, sticky="W", pady=15)

lblEmail = Label(text="Email: ", font=("Arial 12"))
lblEmail.grid(row=1, column=4, sticky="E", pady=15)
txtEmail = Entry(font=("Arial 12"))
txtEmail.grid(row=1, column=5, sticky="W", pady=15)

def filtrarDatos():
    pass

btnFiltrar = Button(text="Filtrar", font=("Arial 12"), command=filtrarDatos)
btnFiltrar.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=20)

def generarCertificado():
    pass

btnGenerarCertificado = Button(text="Generar Certificado", font=("Arial 12"), command=generarCertificado)
btnGenerarCertificado.grid(row=5, column=2, columnspan=2, sticky="nsew", padx=20)

def generarCertificadoEnMasa():
    pass

btnGenerarCertificadoEnMasa = Button(text="Generar Certificado en Masa", font=("Arial 12"), command=generarCertificadoEnMasa)
btnGenerarCertificadoEnMasa.grid(row=5, column=4, columnspan=2, sticky="nsew", padx=20)

frm.mainloop()