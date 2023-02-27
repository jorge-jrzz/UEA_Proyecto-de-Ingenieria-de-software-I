import os
import xml.etree.ElementTree as ET

# Obtiene la ruta de de la carpeta con el archivo cascade.xml
ruta_archivo = os.path.join('Tarea_2', 'autobuses2.xml')

tree = ET.parse(ruta_archivo)
root = tree.getroot()

# Variables del Script para la imprecion en consola, y el cambio de valores del archivo .xml
i = 0
# Catalogo Zona
zonas = ["Sur", "Norte", "Este", "Oeste", "Centro"]

print(zonas[0])

# '''
for autobus in root:
    placa = autobus.find('placa').text
    capacidad = autobus.find('capacidad').text
    chofer = autobus.find('chofer').text
    zona = autobus.find('zona').text
    i=i+1
    print("Autobus", i, ": ")
    print("  Placa:", placa)
    print("  Capacidad:", capacidad)
    print("  Chofer:", chofer)
    
    option = int(zona)
    print(zona)
    print(zonas[option])
        
    print("----------------------------")

# '''