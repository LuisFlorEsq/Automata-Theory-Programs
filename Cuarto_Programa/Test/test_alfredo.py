import random

tablero = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rojos = [2,4,5,7,10,12,13,15]
negros = [1,3,6,8,9,11,14,16]
# for fila in tablero:
#     for numero, color in fila.items():
#         print(fila)
#         print(f'{numero}:{color}')


movJ1 = tablero

def mover(CasillaI, CasillaF, movimientos, Lista_Moves, combinaciones_registradas):
    filaJ, columnJ = None, None
    turno = 0

    Lista_Moves.append(CasillaI)

    while turno < len(movimientos):
        colores = movimientos[turno]
        print(f'Los colores son {colores}')
        print(movimientos)
        print(f'Vas en el turno {turno}')

        # Pos actual
        for row in range(len(tablero)):
            for column in range(len(tablero[row])):
                if tablero[row][column] == CasillaI:
                    filaJ, columnJ = row, column
                    break

        # Encontrar vecinos
        vecinos = []
        if filaJ > 0:
            vecinos.append((filaJ - 1, columnJ))
        if filaJ < 3:
            vecinos.append((filaJ + 1, columnJ))
        if columnJ > 0:
            vecinos.append((filaJ, columnJ - 1))
        if columnJ < 3:
            vecinos.append((filaJ, columnJ + 1))

        if filaJ > 0 and columnJ > 0:
            vecinos.append((filaJ - 1, columnJ - 1))
        if filaJ > 0 and columnJ < 3:
            vecinos.append((filaJ - 1, columnJ + 1))
        if filaJ < 3 and columnJ > 0:
            vecinos.append((filaJ + 1, columnJ - 1))
        if filaJ < 3 and columnJ < 3:
            vecinos.append((filaJ + 1, columnJ + 1))

        vecino_mover = []
        for row, column in vecinos:
            if (colores == 'r' and tablero[row][column] in rojos): 
                vecino_mover.append((row, column))
            elif (colores == 'b' and tablero[row][column] in negros):
                vecino_mover.append((row, column))

        print(f'El jugador está en la fila {filaJ}, columna {columnJ}. Se puede mover a los vecinos {vecino_mover}, ahora toca {movimientos[turno]}')

        if vecino_mover:
            print(len(movimientos) - 1)
            if turno < len(movimientos) - 1:
                vecino_mover = [(row, column) for row, column in vecino_mover if (row, column) != (3, 3)]
                print(vecino_mover)

            print(vecino_mover)

            pos_new = random.choice(vecino_mover)

            print(f'La posición elegida es {pos_new}')

            CasillaI = movJ1[pos_new[0]][pos_new[1]]
            Lista_Moves.append(CasillaI)
            
            print(Lista_Moves)
            turno += 1
            if CasillaI != tablero[3][3] or turno < len(movimientos):
                continue
        else:
            print('Pues no')

        print(CasillaI)
    
    # Verificar si es el último turno y si el jugador llega a la casilla final
    if turno == len(movimientos) and CasillaI == CasillaF:
        # Registra la secuencia completa de casillas visitadas
        secuencia = tuple(Lista_Moves)
        if secuencia not in combinaciones_registradas:
            combinaciones_registradas.add(secuencia)
            with open('./P4 - Tablero/Jugadas.txt', 'a') as Jg:
                Jg.write(f'{secuencia}\n')

    # Registra la secuencia completa de casillas visitadas
    secuencia = tuple(Lista_Moves)
    if secuencia not in combinaciones_registradas:
        combinaciones_registradas.add(secuencia)
        with open('./P4 - Tablero/Jugadas.txt', 'a') as Jg:
            Jg.write(f'{secuencia}\n')

    # Restablece Lista_Moves después de terminar el juego
    Lista_Moves.clear()

    return CasillaI

def Tablero(Movimientos,combinaciones_registradas):
    CasillaI = tablero[0][0]
    CasillaF = tablero[3][3]

    while CasillaI != CasillaF:
        CasillaI = tablero[0][0]

        CasillaI = mover(CasillaI, CasillaF, Movimientos, Lista_Moves=[], combinaciones_registradas=combinaciones_registradas)

def main():
    Movimientos = []
    print('===============================')
    print('Establecer movimientos')
    print('1.- Automáticamente')
    print('2.- Manualmente')
    opc = int(input())
    n = int(input('¿Cuántos movimientos quieres? (Max. 50) '))

    if opc == 1:
        for i in range(0, n - 1):
            Movimientos.append(random.choice(['b', 'r']))
        Movimientos.append('b')
        combinaciones_registradas = set()

        print(Movimientos)
        Tablero(Movimientos,combinaciones_registradas)
    elif opc != 1 and opc != 2:
        print('Elija una opción correcta')
    else:
        combinaciones_registradas = set()
        # for i in range(0, n):
        #     Movimientos.append(input(f'Ingrese el color número {i} (b/r): '))
        Movimientos = ['b', 'b', 'r', 'b', 'r', 'r', 'b', 'r', 'b', 'b']
        Tablero(Movimientos,combinaciones_registradas)

if _name_ == '_main_':
    main()
