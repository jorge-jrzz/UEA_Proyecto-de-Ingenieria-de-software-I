# Este código utiliza la librería xml.etree.ElementTree en Python para leer y manipular datos en un archivo xml.
# Esta librería es parte de la biblioteca estándar de Python y proporciona una manera fácil y eficiente de trabajar con datos en formato xml. 
# Con ElementTree, es posible acceder y modificar elementos y atributos dentro de un archivo xml de manera sencilla.
import os
import xml.etree.ElementTree as ET

# Ruta del directorio actual
dir_actual = os.getcwd()

# Ruta del archivo que se quiere abrir (relativa al directorio actual)
ruta_xml = os.path.join(dir_actual, 'autobuses.xml')

tree = ET.parse(ruta_xml)
root = tree.getroot()

i = 0

for autobus in root:
    placa = autobus.find('placa').text
    capacidad = autobus.find('capacidad').text
    chofer = autobus.find('chofer').text
    i=i+1
    print("Autobus", i, ": ")
    print("  Placa:", placa)
    print("  Capacidad:", capacidad)
    print("  Chofer:", chofer)
    print("----------------------------")

# En este ejemplo, se usa xml.etree.ElementTree.parse() para parsear el archivo XML y devolver un objeto ElementTree. Luego, se usa getroot() para obtener la raíz del árbol XML. 
# Finalmente, se recorre cada elemento hijo de la raíz y se imprimen sus etiquetas y atributos.


