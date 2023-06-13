
import time
from num2words import num2words
from datetime import datetime


class Viaje:
    """Clase viaje, con metodos constructor y toString"""

    def __init__(self, clave, destino, origen, autobus, precio, hora, puerta, categoria):
        self.__clave = clave
        self.__destino = destino
        self.__origen = origen
        self.__autobus = autobus
        self.__precio = precio
        self.__hora = hora
        self.__puerta = puerta
        self.__categoria = categoria

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
    def origen(self):
        return self.__origen

    @origen.setter
    def origen(self, nuevo_origen):
        self.__origen = nuevo_origen

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

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria

    def __str__(self):
        cadena = f"""
Clave:  {self.__clave}
Destino:  {self.__destino.title()}
Origen: {self.__origen.title()}
Placa del autobus:  {self.__autobus.upper()}
Precio:  $ {self.__precio} MXN ({num2words(self.__precio, lang="es").upper()} PESOS)
Hora de salida:  {self.__hora} hrs
Puerta:  {self.__puerta}
Categoria: {self.__categoria.capitalize()}"""

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

    datos = {'clave': None, 'destino': None, 'origen': None, 'autobus': None,
             'precio': None, 'hora': None, 'puerta': None, 'categoria': None}

    print("Proporciona los siguinetes datos:")
    for item in datos:
        # Aclaraciones al usuario sobre la informacion que se le pide

        if item == 'autobus':
            print("\nPlaca del autobus: ")
        elif item == 'hora':
            print("\nHora de salida (HH:MM):")
        elif item == 'categoria':
            print("\nCategoria (1 - 3):")
        else:
            print(f"\n{item.capitalize()}: ")

        # Verificaciones de la informacion ingresada por el usuario
        if item == 'destino' or item == 'origen':
            while True:
                valor = input("  > ")
                temp = valor.replace(" ", "")
                if temp.isalpha():
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
                hora_str = input("  > ")
                try:
                    hora = datetime.strptime(hora_str, "%H:%M").time()
                    datos[item] = hora
                    break
                except ValueError:
                    print(" ** Ingresa una hora valida **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

                # else:
                #     print(" ** Ingresa una hora valida **", end="\r")
                #     time.sleep(1)
                #     print(" " * 35, end="\r")

        elif item == 'puerta' or item == 'categoria':
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

    info = ['destino', 'origen', 'autobus',
            'precio', 'hora', 'puerta', 'categoria']

    print("Proporciona los siguinetes datos:")
    for stuff in info:
        # Aclaraciones al usuario sobre la informacion que se le pide
        if stuff == 'autobus':
            print("\nPlaca del autobus: ")
            new_valor = input("  > ")
            trip.autobus = new_valor
        elif stuff == 'hora':
            print("\nHora de salida (HH:MM):")
        elif stuff == 'categoria':
            print("\nCategoria (1 - 3):")
        else:
            print(f"\n{stuff.capitalize()}: ")

        # Verificaciones de la informacion ingresada por el usuario
        if stuff == 'destino':
            while True:
                new_valor = input("  > ")
                temp = new_valor.replace(" ", "")
                if temp.isalpha():
                    trip.destino = new_valor
                    break
                else:
                    print(" ** Ingresa un destino valido **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")

        if stuff == 'origen':
            while True:
                new_valor = input("  > ")
                temp = new_valor.replace(" ", "")
                if temp.isalpha():
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
                hora_str = input("  > ")
                try:
                    new_hora = datetime.strptime(hora_str, "%H:%M").time()
                    trip.hora = new_hora
                    break
                except ValueError:
                    print(" ** Ingresa una hora valida **", end="\r")
                    time.sleep(1)
                    print(" " * 35, end="\r")
                # else:
                #     print(" ** Ingresa una hora valida **", end="\r")
                #     time.sleep(1)
                #     print(" " * 35, end="\r")

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

        elif stuff == 'categoria':
            while True:
                new_valor = input("  > ")
                if new_valor.isdigit() and new_valor in '123':
                    trip.puerta = new_valor
                    break
                else:
                    print(" ** Ingresa un numero de puerta valido **", end="\r")
                    time.sleep(1)
                    print(" " * 42, end="\r")
