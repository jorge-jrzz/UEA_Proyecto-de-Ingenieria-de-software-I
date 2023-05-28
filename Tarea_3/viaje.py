
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

    def __str__(self):
        cadena = f"""
Clave:  {self.__clave.upper()}
Destino:  {self.__destino.capitalize()}
Placa del autobus:  {self.__autobus.upper()}
Precio:  $ {self.__precio} MXN ({num2words(self.__precio, lang="es").upper()} PESOS)
Hora de salida:  {self.__hora} hrs
Puerta:  {self.__puerta}"""

        return cadena


def insertar_viaje():
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
            datos[item] = valor

    viaje = Viaje(**datos)

    return viaje
