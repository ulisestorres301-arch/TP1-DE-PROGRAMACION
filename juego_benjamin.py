import random

def cargar_estadisticas():
    try:
        archivo = open("estadisticas_ppt.txt", "r")

        jugadas = int(archivo.readline())
        ganadas = int(archivo.readline())
        perdidas = int(archivo.readline())
        empates = int(archivo.readline())

        archivo.close()

    except:
        jugadas = 0
        ganadas = 0
        perdidas = 0
        empates = 0

    return jugadas, ganadas, perdidas, empates


def guardar_estadisticas(jugadas, ganadas, perdidas, empates):

    archivo = open("estadisticas_ppt.txt", "w")

    archivo.write(str(jugadas) + "\n")
    archivo.write(str(ganadas) + "\n")
    archivo.write(str(perdidas) + "\n")
    archivo.write(str(empates) + "\n")

    archivo.close()


def mostrar_estadisticas(jugadas, ganadas, perdidas, empates):

    print("\n----- ESTADISTICAS -----")
    print("Partidas jugadas:", jugadas)
    print("Partidas ganadas:", ganadas)
    print("Partidas perdidas:", perdidas)
    print("Empates:", empates)
    print("------------------------\n")


def jugar():

    opciones = ["Piedra", "Papel", "Tijera"]

    jugadas, ganadas, perdidas, empates = cargar_estadisticas()

    jugador = int(input("1-Piedra  2-Papel  3-Tijera: "))

    while jugador < 1 or jugador > 3:
        jugador = int(input("Ingrese 1, 2 o 3: "))

    maquina = random.randint(1, 3)

    print("Vos elegiste:", opciones[jugador - 1])
    print("La computadora eligio:", opciones[maquina - 1])

    jugadas += 1

    if jugador == maquina:
        print("Empate")
        empates += 1

    elif (jugador == 1 and maquina == 3) or \
         (jugador == 2 and maquina == 1) or \
         (jugador == 3 and maquina == 2):

        print("Ganaste")
        ganadas += 1

    else:
        print("Perdiste")
        perdidas += 1

    guardar_estadisticas(jugadas, ganadas, perdidas, empates)


def menu():

    opcion = -1

    while opcion != 0:

        print("\n=== PIEDRA PAPEL O TIJERA ===")
        print("1 - Jugar")
        print("2 - Ver estadisticas")
        print("0 - Volver")

        opcion = int(input("Opcion: "))

        if opcion == 1:
            jugar()

        elif opcion == 2:

            jugadas, ganadas, perdidas, empates = cargar_estadisticas()

            mostrar_estadisticas(
                jugadas,
                ganadas,
                perdidas,
                empates
            )

        elif opcion == 0:
            print("Saliendo...")

        else:
            print("Opcion incorrecta")


menu()
