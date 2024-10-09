from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from selenium import webdriver as opcionesSelenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import pyautogui as tiempoDeEspera

frm = Tk()
frm.title("Python RPA - Extraer datos web")
estilo = ttk.Style()
estilo.theme_use("clam") # ("clam", "alt", "default", "classic")
estilo.configure("TButton", padding=10, relief="flat")

treviewDatos = ttk.Treeview(frm, columns=(1, 2, 3), show="headings")
treviewDatos.column("1", width=100, anchor="center")
treviewDatos.heading("1", text="ID")
treviewDatos.column("2", width=500, anchor="center")
treviewDatos.heading("2", text="Due Date")
treviewDatos.column("3", width=200, anchor="center")
treviewDatos.heading("3", text="Invoice")
treviewDatos.grid(row=0, column=0, columnspan=8, sticky="nsew")

servicio = Service(ChromeDriverManager().install())
navegador = opcionesSelenium.Chrome(service=servicio)

navegador.get("https://rpachallengeocr.azurewebsites.net/")
tiempoDeEspera.sleep(3)

linea: int = 1

i: int = 1

while i < 4:
    
    tblElementos = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
    lineas = tblElementos.find_elements(By.TAG_NAME, 'tr')
    columnas = tblElementos.find_elements(By.TAG_NAME, 'td')
    tiempoDeEspera.sleep(1)
    
    for lineaActual in lineas:
        
        tiempoDeEspera.sleep(1)
        
        linea += 1
        
        texto: str = lineaActual.text

        if texto[0] != "#":
            
            texto2: str = texto.split(" ")
            
            treviewDatos.insert("", "end", values=(str(texto2[0]), str(texto2[1]),str(texto2[2])))
            
    i += 1
    
    tiempoDeEspera.sleep(2)
   
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
    tiempoDeEspera.sleep(2)
    
def exportarExcel():
    workbook = load_workbook(filename=r"dap-v1\data\base_datos_web.xlsx")
    sheet = workbook["Datos"]
    sheet.delete_rows(idx=1, amount=30000)
    
    for numeroLinea in treviewDatos.get_children():
        textoLineas = treviewDatos.item(numeroLinea)["values"]
        sheet.append(textoLineas)
    
    workbook.save(filename=r"dap-v1\data\datos_web_extraidos.xlsx")
    
    messagebox.showinfo("Exportar Excel", "Datos exportados correctamente")
    
    
    
btnExportar = Button(text="Exportar", font=("Arial", 12), command=exportarExcel)
btnExportar.grid(row=1, column=0, columnspan=8, sticky="nsew")
    
frm.mainloop()