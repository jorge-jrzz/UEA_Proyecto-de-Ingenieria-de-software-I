import os
import xml.etree.ElementTree as ET
from viaje import Viaje

# Ruta del directorio actual
dir_actual = os.getcwd()

# Ruta del archivo que se quiere abrir (relativa al directorio actual)
ruta_xml = os.path.join(dir_actual, 'central.xml')

lista_viajes = []


def cargar():
    """Función para cargar los registrso del archivo xml a la lista del sistema"""

    datos = {'clave': None, 'destino': None, 'origen': None, 'autobus': None,
             'precio': None, 'hora': None, 'puerta': None, 'categoria': None}

    tree = ET.parse(ruta_xml)
    root = tree.getroot()

    # Acceder a la clave de cada registro
    for viaje in root.findall('viaje'):
        datos['clave'] = viaje.get('clave')
        datos['destino'] = viaje.find('destino').text
        datos['origen'] = viaje.find('origen').text
        datos['autobus'] = viaje.find('autobus').text
        datos['precio'] = viaje.find('precio').text
        datos['hora'] = viaje.find('hora').text
        datos['puerta'] = viaje.find('puerta').text
        datos['categoria'] = viaje.find('categoria').text

        viaje = Viaje(**datos)

        lista_viajes.append(viaje)

    return lista_viajes
