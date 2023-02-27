import os
from xml.dom import minidom

# Ruta del directorio actual
dir_actual = os.getcwd()

# Ruta del archivo que se quiere abrir (relativa al directorio actual)
ruta_xml = os.path.join(dir_actual, 'central.xml')

# Se utiliza la función parse() de minidom para cargar el archivo XML. Esto crea un objeto xml_file que representa el documento XML.
document = minidom.parse(ruta_xml)

# La función getElementsByTagName() se utiliza para obtener todos los elementos con el nombre "CentralField" del archivo XML.
# El resultado se almacena en la variable central_fields.
central_fields = document.getElementsByTagName("CentralField")

i=0
# Recorrer la lista de elementos y obtener la información
for central_field in central_fields:
    autobus = central_field.getElementsByTagName("autobus")[0].firstChild.data
    destino = central_field.getElementsByTagName("destino")[0].firstChild.data
    i = i + 1
    print(f"{i}° Autobús: {autobus} \t Destino: {destino}")
    print("------------------------------------------------------------\n")

# Este código recorre la lista de elementos central_fields y para cada uno de ellos, obtiene la información del autobús y del destino. 
# Esto se hace utilizando la función getElementsByTagName() para obtener los elementos "autobus" y "destino" dentro de cada elemento "CentralField". 
# La función [0] se utiliza para obtener el primer elemento con ese nombre, y .firstChild.data se utiliza para obtener el texto dentro de ese elemento.

# Finalmente, el código imprime la información del autobús y del destino utilizando print(). 
# La sintaxis f-string se utiliza para incluir las variables autobus y destino dentro de la cadena que se imprime.
