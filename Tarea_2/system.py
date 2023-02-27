import os
import xml.etree.ElementTree as ET

# Obtiene la ruta de de la carpeta con el archivo cascade.xml
ruta_xml = os.path.join('Tarea_2', 'autobuses2.xml')
ruta_txt = os.path.join('Tarea_2', 'secciones.txt')

tree = ET.parse(ruta_xml)
root = tree.getroot()

# Variables del Script para la imprecion en consola, y el cambio de valores del archivo .xml
i = 0
# Catalogo Zona
zonas = ["Sur", "Norte", "Este", "Oeste", "Centro"]

# Abre el archivo de texto donde vienen las secciones en modo lectura
with open(ruta_txt, 'r') as archivo:
    # Lee todas las líneas del archivo y las guarda en una lista
    lista_secciones = archivo.readlines()

for autobus in root:
    placa = autobus.find('placa').text
    capacidad = autobus.find('capacidad').text
    chofer = autobus.find('chofer').text
    zona_str = autobus.find('zona').text
    seccion_str = autobus.find('seccion').text
    zona = int(zona_str)
    seccion = int(seccion_str)
    i=i+1
    print(f"{i}° Autobús:")
    print("  Placa:     ", placa)
    print("  Capacidad: ", capacidad)
    print("  Chofer:    ", chofer)
    print("  Zona:      ", zonas[zona])
    print("  Seccion:   ", lista_secciones[seccion])
    print("----------------------------")
