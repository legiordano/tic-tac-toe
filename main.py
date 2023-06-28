tablero = [' '] * 9

combinaciones_ganadoras = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def dibujar_tablero():
    print("  " + tablero[0] + " | " + tablero[1] + " | " + tablero[2] + " ")
    print("-----------")
    print("  " + tablero[3] + " | " + tablero[4] + " | " + tablero[5] + " ")
    print("-----------")
    print("  " + tablero[6] + " | " + tablero[7] + " | " + tablero[8] + " ")

def hay_ganador(simbolo):
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == simbolo:
            return True
    return False

def jugar():
    jugador = 'X'
    turno = 0
    juego_terminado = False

    while not juego_terminado:
        dibujar_tablero()

        posicion = int(input("Jugador " + jugador + ", elige una posición (1-9): ")) - 1

        if tablero[posicion] == ' ':
            tablero[posicion] = jugador
            turno += 1

            if hay_ganador(jugador):
                dibujar_tablero()
                print("¡El jugador " + jugador + " ha ganado!")
                juego_terminado = True
            elif turno == 9:
                dibujar_tablero()
                print("¡Empate!")
                juego_terminado = True
            else:
                jugador = 'O' if jugador == 'X' else 'X'
        else:
            print("Posición inválida. Intenta nuevamente.")

jugar()