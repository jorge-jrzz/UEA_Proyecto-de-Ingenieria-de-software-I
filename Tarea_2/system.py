import os
import xml.etree.ElementTree as ET

# Obtiene la ruta de de la carpeta con el archivo cascade.xml
ruta_archivo = os.path.join('Tarea_2', 'autobuses2.xml')

tree = ET.parse(ruta_archivo)
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