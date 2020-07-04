from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pdb
# Debugger - colocar donde se desea: pdb.set_trace()

# open firefox - headless mode
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# voy a la pagina
driver.get("https://ar.indeed.com/?r=us")
print("Accediendo a indeed.com")

# ingreso lo que busco
titulo = driver.find_element_by_name("q")
titulo.send_keys(input("Ingrese palabra clave a buscar: "))

# ingreso lugar
lugar = driver.find_element_by_name("l")
lugar.send_keys(input("Ingrese localidad: "))

# envio el formulario
lugar.submit()
print("Enviando formulario")

# creo un archivo y lo abro
# archivo = open("trabajos.txt", "x") --  will create a file, returns an error if the file exist

archivo = open("trabajos.txt", "a")  # will create a file if the specified file does not exist

# pausa para evitar error de carga
timeout = 3 # segundos
try:
    element_present = EC.presence_of_element_located((By.ID, 'resultsCol'))
    WebDriverWait(driver, timeout).until(element_present)
    print("Comienza lectura de datos")
except TimeoutException:
    print("Error de carga")

# obtengo todos los links
links = driver.find_elements_by_css_selector('#resultsCol div a')

# imprimo los datos
print("Escribiendo datos en archivo")
for elem in links:
    href = elem.get_attribute('href')
    if href is not None and "https://ar.indeed.com/rc" in href:
        # print(href)
        archivo.write(elem.get_attribute('text'))
        archivo.write("\n")
        archivo.write(href)
        archivo.write("\n")
        archivo.write(" ------------------------------------------ ")
        archivo.write("\n")

# cierro el browser y el archivo
driver.close()
archivo.close()
print("Datos guardados")
