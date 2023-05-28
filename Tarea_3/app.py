
import os
import time
from viaje import insertar_viaje


def clear_screen():
    """Funcion para limpiar la pantalla de la terminal"""

    if os.name == "posix" or os.name == "mac":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def verificar(option):
    """Funcion para verificar la opcion del usuario que este dentro de las opciones establecidas"""

    if option.isalpha():
        for c in option:
            if c not in 'abcdef':
                return False
            else:
                return True
    else:
        for i in option:
            if i not in '123456':
                return False
            else:
                return True


viajes = []


def opcion1():
    """Funcion para realizar la opcion a del menu, insertar multiples viaje a una lista"""

    if opcion == 'a' or opcion == '1':
        while True:
            clear_screen()
            print("  ---- Insertar viaje ----\n")
            viaje = insertar_viaje()
            viajes.append(viaje)
            agregar = input("\n ¿Deseas ingresar otro viaje? (S/N)  ")
            agregar = agregar.lower()

            if agregar not in 'sn':
                while True:
                    print("** Ingresa una opcion valida **", end="\r")
                    time.sleep(1)
                    print(" " * 40)
                    agregar = input(" ¿Deseas ingresar otro viaje? (S/N)  ")
                    agregar = agregar.lower()
                    if agregar == 'n' or agregar == 's':
                        break

            if agregar == 'n':
                break
            elif agregar == 's':
                pass
    else:
        print("Estas destro de la opcion a (insertar un viaje)")


while True:
    clear_screen()
    print("**********************************")
    print("****** Central de Autobuses ******")
    print("**********************************\n")
    print("a) Insertar viaje")
    print("b) Mostrar viajes")
    print("c) Buscar viajes")
    print("d) Eliminar viaje")
    print("e) Actualizar viaje")
    print("f) Salir \n")

    opcion = input("Selecciona la opción (a-f) or (1-6):  ")
    opcion = opcion.lower()

    if verificar(opcion):
        if opcion == 'a' or opcion == '1':
            opcion1()
            clear_screen()
            print("\n* Regresando al menu principal *")
            time.sleep(1)
        elif opcion == 'f' or opcion == '6':
            clear_screen()
            print("\n* VUELVA PRONTO *")
            exit()

    else:
        print("\n** Ingresa una opcion valida **")
        time.sleep(1)
