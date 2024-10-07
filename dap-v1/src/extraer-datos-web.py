from selenium import webdriver as opcionesSelenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui as tiempoDeEspera

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
            
            print(f"Coluna 1: {texto2[0]}")
            print(f"Coluna 2: {texto2[1]}")
            print(f"Coluna 3: {texto2[2]}")
            
    i += 1
    
    tiempoDeEspera.sleep(2)
   
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
    tiempoDeEspera.sleep(2)
   
   
    