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
        if opcion == 'f' or opcion == '6':
            clear_screen()
            print("\n * VUELVA PRONTO *")
            exit()
        break
    else:
        print("\n** Ingresa una opcion valida **")
        time.sleep(1)

viajes = []

if opcion == 'a' or opcion == '1':
    while True:
        clear_screen()
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
                if agregar.lower() == 'n' or agregar.lower() == 's':
                    break

        if agregar.lower() == 'n':
            break
        elif agregar.lower() == 's':
            pass

elif opcion == 'b' or opcion == '2':
    clear_screen()
    print(viajes)
