# Importamos las librearias necesarias para la ejecución del script.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyautogui as tiempoPausaComputador

# Verifica la version de chrome y descarga el driver correspondiente.
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

# Abre el navegador y ingresa a la página de SurveyMonkey que contiene un formulario.
navegador.get("https://pt.surveymonkey.com/r/79WHF9G")

# Tiempo del coputador pra procesar la informacion.
tiempoPausaComputador.sleep(3)

# Rellenar el campo de nombre.
navegador.find_element(By.ID, "112904979").send_keys("Lupe Luna")

# Tiempo del coputador pra procesar la informacion.
tiempoPausaComputador.sleep(1)

# Rellenar el campo de email.
navegador.find_element(By.ID, "112904987").send_keys("lupe.luna@mail.com")

# Tiempo del coputador pra procesar la informacion.
tiempoPausaComputador.sleep(1)

# Clickear en el radio button de género femenino.
navegador.find_element(By.ID, "112905004_855492047_label").click()

# Tiempo del coputador pra procesar la informacion.
tiempoPausaComputador.sleep(1)

# Selecciona la opción 2 de la lista de estados.
rbtnSexo = navegador.find_element(By.ID, "112905103")
itemSeleccionado = Select(rbtnSexo)
itemSeleccionado.select_by_index(2)

# Tiempo del coputador pra procesar la informacion.
tiempoPausaComputador.sleep(1)

# Rellenar el campo de cor favorite.
navegador.find_element(By.NAME, "112905214").send_keys("Azul")

# Tiempo del coputador pra procesar la informacion.
tiempoPausaComputador.sleep(3)

# Clickear en el botón de enviar.
navegador.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button').click()

# Tiempo del coputador pra procesar la informacion.
tiempoPausaComputador.sleep(2)



