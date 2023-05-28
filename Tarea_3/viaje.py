
import time
from num2words import num2words


class Viaje:
    """Clase viaje, con metodos constructor y toString"""

    def __init__(self, clave, destino, autobus, precio, hora, puerta):
        self.__clave = clave
        self.__destino = destino
        self.__autobus = autobus
        self.__precio = precio
        self.__hora = hora
        self.__puerta = puerta

    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self, nueva_clave):
        self.__clave = nueva_clave

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, nuevo_destino):
        self.__destino = nuevo_destino

    @property
    def autobus(self):
        return self.__autobus

    @autobus.setter
    def autobus(self, nuevo_autobus):
        self.__autobus = nuevo_autobus

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, nueva_hora):
        self.__hora = nueva_hora

    @property
    def puerta(self):
        return self.__puerta

    @puerta.setter
    def puerta(self, nueva_puerta):
        self.__puerta = nueva_puerta

    def __str__(self):
        cadena = f"""
Clave:  {self.__clave.upper()}
Destino:  {self.__destino.capitalize()}
Placa del autobus:  {self.__autobus.upper()}
Precio:  $ {self.__precio} MXN ({num2words(self.__precio, lang="es").upper()} PESOS)
Hora de salida:  {self.__hora} hrs
Puerta:  {self.__puerta}"""

        return cadena


def search(trips, key):
    """Funcion para buscar un viaje por la clave del mismo"""

    if len(trips) > 0:
        while True:
            is_there = False
            for trip in trips:
                if trip.clave == key:
                    is_there = True
                    return True
            if not is_there:
                return False
    else:
        return False


def insertar_viaje(viajes):
    """Funcion para creau una instancia de la clase viaje"""

    datos = {'clave': None, 'destino': None, 'autobus': None,
             'precio': None, 'hora': None, 'puerta': None}

    print("Proporciona los siguinetes datos:")
    for item in datos:
        # Aclaraciones al usuario sobre la informacion que se le pide

        if item == 'autobus':
            print("\nPlaca del autobus: ")
        elif item == 'hora':
            print("\nHora de salida (24 hrs):")
        else:
            print(f"\n{item.capitalize()}: ")

        # Verificaciones de la informacion ingresada por el usuario
        if item == 'destino':
            while True:
                valor = input("  > ")
                if valor.isalpha():
                    datos[item] = valor
                    break
                else:
                    print(" ** Ingresa un destino valido **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

        elif item == 'precio':
            while True:
                valor = input("  > $ ")
                if valor.isdigit():
                    datos[item] = valor
                    break
                else:
                    print(" ** Ingresa un precio valido **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

        elif item == 'hora':
            while True:
                valor = input("  > ")
                if valor.isdigit() and int(valor) in range(0, 24):
                    datos[item] = valor
                    break
                else:
                    print(" ** Ingresa una hora valida **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

        elif item == 'puerta':
            while True:
                valor = input("  > ")
                if valor.isdigit():
                    datos[item] = valor
                    break
                else:
                    print(" ** Ingresa un numero de puerta valido **", end="\r")
                    time.sleep(1)
                    print(" " * 42, end="\r")

        else:
            valor = input("  > ")
            if item == 'clave':
                if search(viajes, valor):
                    print(
                        "\n** La clave ingresada ya ha sido registrada para otro viaje **\n")
                    return

            datos[item] = valor

    viaje = Viaje(**datos)

    return viaje


def update_viaje(trip):
    """Funcion para actualizar los atributos de una instancia de un viaje"""

    info = ['destino', 'autobus', 'precio', 'hora', 'puerta']

    print("Proporciona los siguinetes datos:")
    for stuff in info:
        # Aclaraciones al usuario sobre la informacion que se le pide
        if stuff == 'autobus':
            print("\nPlaca del autobus: ")
            new_valor = input("  > ")
            trip.autobus = new_valor
        elif stuff == 'hora':
            print("\nHora de salida (24 hrs):")
        else:
            print(f"\n{stuff.capitalize()}: ")

        # Verificaciones de la informacion ingresada por el usuario
        if stuff == 'destino':
            while True:
                new_valor = input("  > ")
                if new_valor.isalpha():
                    trip.destino = new_valor
                    break
                else:
                    print(" ** Ingresa un destino valido **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

        elif stuff == 'precio':
            while True:
                new_valor = input("  > $ ")
                if new_valor.isdigit():
                    trip.precio = new_valor
                    break
                else:
                    print(" ** Ingresa un precio valido **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

        elif stuff == 'hora':
            while True:
                new_valor = input("  > ")
                if new_valor.isdigit() and int(new_valor) in range(0, 24):
                    trip.hora = new_valor
                    break
                else:
                    print(" ** Ingresa una hora valida **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

        elif stuff == 'puerta':
            while True:
                new_valor = input("  > ")
                if new_valor.isdigit():
                    trip.puerta = new_valor
                    break
                else:
                    print(" ** Ingresa un numero de puerta valido **", end="\r")
                    time.sleep(1)
                    print(" " * 42, end="\r")
