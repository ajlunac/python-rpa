from selenium import webdriver as opcionesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tiempoDeEspera

navegador = opcionesSelenium.Chrome()

navegador.get("https://rpachallengeocr.azurewebsites.net/")
tiempoDeEspera.sleep(3)

tblElementos = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

lineas = tblElementos.find_elements(By.TAG_NAME, 'tr')
columnas = tblElementos.find_elements(By.TAG_NAME, 'td')

# linea = 1

for lineaActual in lineas:
    tiempoDeEspera.sleep(1)
    print(lineaActual.text)
    