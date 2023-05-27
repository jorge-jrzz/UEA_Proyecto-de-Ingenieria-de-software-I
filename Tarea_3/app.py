import os
import time


def clearScreen():
    if os.name == "posix" or os.name == "mac":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def verificar(opcion):
    for c in opcion:
        if c not in 'abcde':
            return False
        else:
            return True

    for i in opcion:
        if i not in '12345':
            return False
        else:
            return True


while True:
    clearScreen()
    print("**********************************")
    print("****** Central de Autobuses ******")
    print("**********************************\n")
    print("a) Insertar viaje")
    print("b) Mostrar viajes")
    print("c) Buscar viajes")
    print("d) Eliminar viaje")
    print("e) Actualizar viaje \n")

    opcion = input("Selecciona la opción:  ")
    opcion = opcion.lower()

    if verificar(opcion):
        break
    else:
        print("\n** Ingresa una opcion valida **")
        time.sleep(1)

print(opcion)
