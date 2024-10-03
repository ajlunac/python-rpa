from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import pyautogui as tiempoPausaNavegador
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

frm = Tk()
frm.title("Python RPA")

Label(frm, text="Moneda: ", font=("Arial 12")).grid(row=0, column=0)
cboListaMonedas = ttk.Combobox(frm, font=("Arial 12"))
cboListaMonedas["values"] = ('Afgani afgano',
                                'Ariary malgache',
                                'Baht tailandés',
                                'Balboa',
                                'Birr etíope',
                                'Boliviano',
                                'Cedi',
                                'Chelín keniano',
                                'Chelín somalí',
                                'Chelín tanzano',
                                'Chelín ugandés',
                                'Colón costarricense',
                                'Colón salvadoreño',
                                'Corona checa',
                                'Corona danesa',
                                'Corona islandesa',
                                'Corona noruega',
                                'Corona sueca',
                                'Córdoba',
                                'Dalasi',
                                'Denar macedonio',
                                'Derechos especiales de giro',
                                'Dinar argelino',
                                'Dinar bareiní',
                                'Dinar iraquí',
                                'Dinar jordano',
                                'Dinar kuwaití',
                                'Dinar libio',
                                'Dinar serbio',
                                'Dinar tunecino',
                                'Dram armenio',
                                'Dírham de los Emiratos Árabes Unidos',
                                'Dírham marroquí',
                                'Dólar australiano',
                                'Dólar bahameño',
                                'Dólar beliceño',
                                'Dólar bermudeño',
                                'Dólar canadiense',
                                'Dólar de Barbados',
                                'Dólar de Brunéi',
                                'Dólar de Hong Kong',
                                'Dólar de Singapur',
                                'Dólar de las Islas Caimán',
                                'Dólar de las Islas Salomón',
                                'Dólar del Caribe Oriental',
                                'Dólar estadounidense',
                                'Dólar fiyiano',
                                'Dólar guyanés',
                                'Dólar jamaiquino',
                                'Dólar liberiano',
                                'Dólar namibio',
                                'Dólar neozelandés',
                                'Dólar surinamés',
                                'Dólar trinitense',
                                'Escudo caboverdiano',
                                'Euro',
                                'Factom',
                                'Florín antillano neerlandés',
                                'Florín arubeño',
                                'Forinto húngaro',
                                'Franco CFA de África Central',
                                'Franco CFA de África Occidental',
                                'Franco CFP',
                                'Franco burundés',
                                'Franco comorense',
                                'Franco congoleño',
                                'Franco guineano',
                                'Franco ruandés',
                                'Franco suizo',
                                'Franco yibutiano',
                                'Gourde',
                                'Grivna',
                                'Guaraní paraguayo',
                                'Kina',
                                'Kip laosiano',
                                'Kwacha malauí',
                                'Kwacha zambiano',
                                'Kwanza angoleño',
                                'Kyat birmano',
                                'Lari georgiano',
                                'Lek albanés',
                                'Lempira hondureño',
                                'Leone',
                                'Leu moldavo',
                                'Leu rumano',
                                'Lev',
                                'Libra de Santa Helena',
                                'Libra egipcia',
                                'Libra esterlina',
                                'Libra libanesa',
                                'Libra sudanesa',
                                'Lilangeni',
                                'Lira turca',
                                'Loti',
                                'Manat azerbaiyano',
                                'Manat turcomano',
                                'Marco bosnioherzegovino',
                                'Metical mozambiqueño',
                                'Naira',
                                'Ngultrum butanés',
                                'Nuevo dólar taiwanés',
                                'Nuevo rublo bielorruso',
                                'Nuevo séquel',
                                "Pa'anga",
                                'Pataca macaense',
                                'Peso argentino',
                                'Peso chileno',
                                'Peso colombiano',
                                'Peso cubano',
                                'Peso dominicano',
                                'Peso filipino',
                                'Peso mexicano',
                                'Peso uruguayo',
                                'Pula',
                                'Quetzal',
                                'Rand sudafricano',
                                'Real brasileño',
                                'Renminbi',
                                'Rial',
                                'Rial iraní',
                                'Rial yemení',
                                'Riel camboyano',
                                'Ringgit malayo',
                                'Riyal catarí',
                                'Riyal saudí',
                                'Rublo ruso',
                                'Rupia de Maldivas',
                                'Rupia de Mauricio',
                                'Rupia de Seychelles',
                                'Rupia de Sri Lanka',
                                'Rupia india',
                                'Rupia indonesia',
                                'Rupia nepalí',
                                'Rupia pakistaní',
                                'Sol peruano',
                                'Som kirguís',
                                'Som uzbeko',
                                'Somoni tayiko',
                                'Taka bangladesí',
                                'Tenge kazajo',
                                'Uguiya',
                                'Unidad de fomento chilena',
                                'Won surcoreano',
                                'Yen japonés',
                                'Złoty',
                                'bolívar venezolano',
                                'yuan chino (extracontinental)',
                                'Đồng vietnamita',
                                '₫ dong nam mỹ')
                                
cboListaMonedas.grid(row=0, column=1)
cboListaMonedas.current(0)

def consultarItem():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    tiempoPausaNavegador.sleep(1)
    
    opciones = Options()
    # opciones.headless = True
    
    elementoNavegador = webdriver.Chrome(options=opciones)
        
    # servicio = Service(ChromeDriverManager().install())
    # elementoNavegador = webdriver.Chrome(service=servicio)
    
    tiempoPausaNavegador.sleep(1)
    
    elementoNavegador.get("https://www.google.com/")
    tiempoPausaNavegador.sleep(3)
    elementoNavegador.find_element(By.NAME, "q").send_keys("dolar hoy")
    tiempoPausaNavegador.sleep(2)
    elementoNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
    tiempoPausaNavegador.sleep(4)
    
    valorDolarGoogle = elementoNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
    tiempoPausaNavegador.sleep(2)
    
    todasLasMonedasGoogle = Select(elementoNavegador.find_element(By.CLASS_NAME, "l84FKc"))
    linea = 0
    for posicionItem in todasLasMonedasGoogle.options:
        
        if posicionItem.text == str(cboListaMonedas.get()):
            
            tiempoPausaNavegador.sleep(2)
            seleccionDropdownGoogle = elementoNavegador.find_element(By.CLASS_NAME, "l84FKc")
            tiempoPausaNavegador.sleep(2)
            itemSeleccionado = Select(seleccionDropdownGoogle)
            tiempoPausaNavegador.sleep(3)
            itemSeleccionado.select_by_index(linea)
            break      
                    
        linea += 1
        
    tiempoPausaNavegador.sleep(4)
    valorDolarGoogle = elementoNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
    tiempoPausaNavegador.sleep(1)
    valorMonedaSeleccionada.config(text= "\n\n" + str(cboListaMonedas.get()) + ": " + valorDolarGoogle + "\n\n")
    
    elementoNavegador.quit()

btConsultar = Button(text="Consultar valor actual", font=("Arial 12"), command=consultarItem)
btConsultar.grid(row=1, column=0, columnspan=2, sticky="NSEW")

valorMonedaSeleccionada = Label(frm, text="Valor: 0", font=("Arial 12 bold"))
valorMonedaSeleccionada.grid(row=2, column=0, columnspan=2, sticky="W")

frm.mainloop()