class Viaje:
    def __init__(self, clave, destino, autobus, precio, hora, puerta):
        self.__clave = clave
        self.__destino = destino
        self.__autobus = autobus
        self.__precio = precio
        self.__hora = hora
        self.__puerta = puerta


def insertarViaje():
    datos = {'clave': 'perro', 'destino': None, 'autobus': None,
             'precio': None, 'hora': None, 'puerta': None}

    print("Proporciona los siguinetes datos:")
    for item in datos:
        print(item.upper())
        valor = input(f"> ")


insertarViaje()
