
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


def press_any_key():
    """Funcion para seguir con el programa cuando el usiario lo presione cualquier tecla"""

    if os.name == "posix" or os.name == "mac":

        import termios
        import sys
        import tty

        fd = sys.stdin.fileno()

        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        import msvcrt
        msvcrt.getch()


def again(what):
    """Funcion para que el usuario decida si quiere realizar una accion otra vez"""

    agregar = input(f"\n ¿Deseas {what} otro viaje? (S/N)  ")
    agregar = agregar.lower()

    if agregar not in 'sn':
        while True:
            print("** Ingresa una opcion valida **", end="\r")
            time.sleep(1)
            print(" " * 40)
            agregar = input(f"\n ¿Deseas {what} otro viaje? (S/N)  ")
            agregar = agregar.lower()
            if agregar == 'n' or agregar == 's':
                break
    if agregar == 'n':
        return False
    elif agregar == 's':
        return True


viajes = []


def opcion1():
    """Funcion para realizar la opcion a del menu, insertar multiples viaje a una lista"""

    while True:
        clear_screen()
        print("  ---- Insertar viaje ----\n")
        viaje = insertar_viaje()
        viajes.append(viaje)

        if not again("ingresar"):
            break


def opcion3():
    """Funcion para buscar un viaje por la clave del mismo"""

    while True:
        is_there = False
        clear_screen()
        print("  ---- Buscar viajes ----\n")
        print("Proporciona la Clave del viaje: ")
        find = input("  > ")
        for trip in viajes:
            if trip.clave == find:
                is_there = True
                print("\n* ¡Viaje encontrado! *\n")
                print(trip)
                break
        if not is_there:
            print("\n ** El viaje con la clave ingresada no se encontro ** \n")

        if not again("buscar"):
            break


def opcion4():
    """Funcion para eliminar un viaje por la clave del mismo"""

    while True:
        is_there = False
        clear_screen()
        print("  ---- Eliminar viajes ----\n")
        print("Proporciona la Clave del viaje: ")
        find = input("  > ")
        for trip in viajes:
            if trip.clave == find:
                is_there = True
                print("\n* ¡Viaje encontrado! *\n")
                print(trip)
                sure = input(
                    "\n ¿Esta seguro de querer borrar este viaje? (S/N)  ")
                sure = sure.lower()
                if sure not in 'sn':
                    while True:
                        print("** Ingresa una opcion valida **", end="\r")
                        time.sleep(1)
                        print(" " * 40)
                        sure = input(
                            "\n ¿Esta seguro de querer borrar este viaje? (S/N)  ")
                        sure = sure.lower()
                        if sure == 'n' or sure == 's':
                            break
                if sure == 'n':
                    break
                elif sure == 's':
                    viajes.remove(trip)
                    print("\n* Se elimino el viaje con exito *\n")
                    break

                break

        if not is_there:
            print("\n ** El viaje con la clave ingresada no se encontro ** \n")

        if not again("eliminar"):
            break


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

        elif opcion == 'b' or opcion == '2':
            clear_screen()
            print("  ---- Mostrar viajes ----\n")
            if len(viajes) > 0:
                count = 0
                for viaje in viajes:
                    count += 1
                    print(f"\n\n  * REGISTRO {count} *")
                    print(viaje)
                print("\n--------------------")
            else:
                print("* No hay ningun viaje registrado *\n")

            print("Presione cualquier tecla para continuar...")
            press_any_key()
            clear_screen()
            print("\n* Regresando al menu principal *")
            time.sleep(1)

        elif opcion == 'c' or opcion == '3':
            opcion3()
            clear_screen()
            print("\n* Regresando al menu principal *")
            time.sleep(1)

        elif opcion == 'd' or opcion == '4':
            opcion4()
            clear_screen()
            print("\n* Regresando al menu principal *")
            time.sleep(1)

        elif opcion == 'e' or opcion == '5':
            clear_screen()
            print("  ---- Actualizar viaje ----\n")

        elif opcion == 'f' or opcion == '6':
            clear_screen()
            print("\n* VUELVA PRONTO *")
            exit()

    else:
        print("\n** Ingresa una opcion valida **")
        time.sleep(1)
