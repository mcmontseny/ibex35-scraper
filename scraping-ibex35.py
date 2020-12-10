import requests # Importamos requests para realizar peticiones HTTP
from bs4 import BeautifulSoup # BeautifulSoup que nos ayuda a scrapear
import csv # Librería para poder guardar los resultas en un CSV
from datetime import datetime # Importamos datetime para usar la fecha actual

print('[START] Iniciamos el scraper para obtener el valor del IBEX 35..')

# Definición de la url a scrapear
url = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'

# Realizamos la petición GET a la url y convertimos la respuesta a BeautifulSoup
print('[TASK] Enviando petición GET para obtener los datos...')

page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

print('[OK] Respuesta HTTP recibida correctamente!')

# Al analizar la web vemos que todos los valores de IBEX 35 están en una tabla
# Podemos observar que esta tabla tiene un id: 'ctl00_Contenido_tblÍndices'
# Vamos a obtener la tabla para poder tratar su contenido
print('[TASK] Analizando la tabla para obtener los valores actuales...')

table = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})

# Una vez tenemos la tabla vamos a obtener el nombre y el valor actual de IBEX 35
# Podemos ver que la segunda fila / tr contiene los valores que queremos.
# Dentro la fila vamos a obtener todas sus celdas.

row = table.find_all('tr')[1]
columns = row.find_all('td')

# Dentro de las celdas, vemos que las dos que necesitamos son la 0 y la 2.
# La posición 0 tiene el nombre del índice y la posición 2 tiene el valor.

name =  columns[0].text
value = columns[2].text

# Mostramos los valores por consola para ver si ha funcionado de forma correcta
print('[OK] Valor encontrados correctamente!')
print('[VALUES] Indice:', name, 'Valor:', value)

# Guardamos los resultados en un CSV para tener un registro de los valores diarios.
# Este documento CSV tiene 3 campos: Nombre del índice, valor y fecha de los datos.
# Al abrir el fichero le indicamos la propiedad 'a'. Esta propiedad es Append.
# Con esto logramos que si el fichero ya existe se añada el nuevo valor al final.
print('[TASK] Añadiendo el nuevo valor al fichero CSV...')
with open('valor_ibex35.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, value, datetime.now()])
print('[OK] Valor añadido correctamente en el fichero CSV!')





