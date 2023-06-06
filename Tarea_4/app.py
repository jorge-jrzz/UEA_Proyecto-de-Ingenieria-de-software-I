
import os
import time
from viaje import insertar_viaje, update_viaje


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


def insertar():
    """Funcion para realizar la opcion a del menu, insertar multiples viaje a una lista"""

    while True:
        clear_screen()
        print("  ---- Insertar viaje ----\n")
        viaje = insertar_viaje(viajes)
        viajes.append(viaje)

        if not again("ingresar"):
            break


def mostrar():
    """Funcion para mostrar los registros de los viajes, ordenados desendente o asendentemente"""

    clear_screen()
    print("  ---- Mostrar viajes ----\n")
    if len(viajes) > 0:
        count = 0
        lista_ordenada = []
        orden = input(
            "\n ¿Como desea que se muestren los registros? Ascending o Descending (A/D)  ")
        orden = orden.lower()

        if orden not in 'ad':
            while True:
                print("** Ingresa una opcion valida **", end="\r")
                time.sleep(1)
                print(" " * 40)
                orden = input(
                    "\n ¿Como desea que se muestren los registros? Ascending o Descending (A/D)  ")
                orden = orden.lower()
                if orden == 'a' or orden == 'd':
                    break

        if orden == 'a':
            # Ordenamiendo de la A a la Z
            lista_ordenada = sorted(
                viajes, key=lambda obj: obj.clave, reverse=False)

            print("\n - Ordenamiendo Asendente -")
            for viaje in lista_ordenada:
                count += 1
                print(f"\n\n  * REGISTRO {count} *")
                print(viaje)
            print("\n--------------------")

        elif orden == 'd':
            # Ordenamiendo de la Z a la A
            lista_ordenada = sorted(
                viajes, key=lambda obj: obj.clave, reverse=True)

            print("\n - Ordenamiendo Desendente -")
            for viaje in lista_ordenada:
                count += 1
                print(f"\n\n  * REGISTRO {count} *")
                print(viaje)
            print("\n--------------------")

    else:
        print("* No hay ningun viaje registrado *\n")

    print("Presione cualquier tecla para continuar...")
    press_any_key()


def search():
    """Funcion para buscar un viaje por la clave del mismo"""

    clear_screen()
    if len(viajes) > 0:
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
    else:
        print("* No hay ningun viaje registrado *\n")
        print("Presione cualquier tecla para continuar...")
        press_any_key()


def delete():
    """Funcion para eliminar un viaje por la clave del mismo"""

    clear_screen()
    if len(viajes) > 0:
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
                        print("\n* Se elimino con exito el viaje *\n")
                        break

                    break

            if not is_there:
                print("\n ** El viaje con la clave ingresada no se encontro ** \n")

            if not again("eliminar"):
                break
    else:
        print("* No hay ningun viaje registrado *\n")
        print("Presione cualquier tecla para continuar...")
        press_any_key()


def update():
    """Funcion para actualizar los datos de un viaje en particular"""

    clear_screen()
    if len(viajes) > 0:
        while True:
            is_there = False
            clear_screen()
            print("  ---- Actualizar viaje ----\n")
            print("Proporciona la Clave del viaje: ")
            find = input("  > ")
            for paseo in viajes:
                if paseo.clave == find:
                    is_there = True
                    print("\n* ¡Viaje encontrado! *\n")
                    update_viaje(paseo)
                    print("\n* Se actualizo con exito el viaje *\n")
                    break
            if not is_there:
                print("\n ** El viaje con la clave ingresada no se encontro ** \n")

            if not again("actualizar"):
                break
    else:
        print("* No hay ningun viaje registrado *\n")
        print("Presione cualquier tecla para continuar...")
        press_any_key()


def main() -> None:
    """Funcion principal, menu de opciones del programa"""

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
                insertar()
                clear_screen()
                print("\n* Regresando al menu principal *")
                time.sleep(1)

            elif opcion == 'b' or opcion == '2':
                mostrar()
                clear_screen()
                print("\n* Regresando al menu principal *")
                time.sleep(1)

            elif opcion == 'c' or opcion == '3':
                search()
                clear_screen()
                print("\n* Regresando al menu principal *")
                time.sleep(1)

            elif opcion == 'd' or opcion == '4':
                delete()
                clear_screen()
                print("\n* Regresando al menu principal *")
                time.sleep(1)

            elif opcion == 'e' or opcion == '5':
                update()
                clear_screen()
                print("\n* Regresando al menu principal *")
                time.sleep(1)

            elif opcion == 'f' or opcion == '6':
                clear_screen()
                print("\n* VUELVA PRONTO *")
                print("\n\n developed by Jorge Juarez\n\n")
                exit()

        else:
            print("\n** Ingresa una opcion valida **")
            time.sleep(1)


if __name__ == '__main__':
    main()
