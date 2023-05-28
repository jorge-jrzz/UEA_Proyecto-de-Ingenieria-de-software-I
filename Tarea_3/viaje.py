from num2words import num2words


class Viaje:
    def __init__(self, clave, destino, autobus, precio, hora, puerta):
        self.__clave = clave
        self.__destino = destino
        self.__autobus = autobus
        self.__precio = precio
        self.__hora = hora
        self.__puerta = puerta

    def __str__(self):
        cadena = f"""
Clave:  {self.__clave}
Destino:  {self.__destino}
Autobus:  {self.__autobus}
Precio:  $ {self.__precio} MXN ({num2words(self.__precio, lang="es").upper()})
Hora de salida:  {self.__hora} hrs
Puerta:  {self.__puerta}"""
        return cadena


def insertarViaje():
    datos = {'clave': None, 'destino': None, 'autobus': None,
             'precio': None, 'hora': None, 'puerta': None}

    print("Proporciona los siguinetes datos:")
    for item in datos:
        if item == 'hora':
            print("\nHora de salida:")
        else:
            print(f"\n{item.capitalize()}: ")
        valor = input("  > ")
        datos[item] = valor

    viaje = Viaje(**datos)
    return viaje


viaje = insertarViaje()
print(viaje)
