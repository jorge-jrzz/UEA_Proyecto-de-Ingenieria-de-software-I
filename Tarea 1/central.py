from xml.dom import minidom

document = minidom.parse("/Users/jorge/Library/CloudStorage/OneDrive-Personal/VS_Code/Proyecto-de-Ingenieria-I/Tarea 1/central.xml")

# Obtener la lista de elementos CentralField
central_fields = document.getElementsByTagName("CentralField")

i=0
# Recorrer la lista de elementos y obtener la información
for central_field in central_fields:
    autobus = central_field.getElementsByTagName("autobus")[0].firstChild.data
    destino = central_field.getElementsByTagName("destino")[0].firstChild.data
    i = i + 1
    print(f"{i}° Autobús: {autobus} - Destino: {destino}")
    print("------------------------------------------------------------\n")
