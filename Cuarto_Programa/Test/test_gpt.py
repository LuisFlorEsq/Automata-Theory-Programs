class Casilla:
    def __init__(self, x, y, color, valor):
        self.x = x
        self.y = y
        self.color = color  # Puedes usar "R" y "B" para representar el color
        self.valor = valor
        self.vecinos = []

    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)

    def verificar_color_vecino(self, color_objetivo):
        for vecino in self.vecinos:
            if vecino.color == color_objetivo:
                return True
        return False

# Crear un tablero de casillas
tablero = [[None] * 4 for _ in range(4)]
for x in range(4):
    for y in range(4):
        color = 'R' if (x + y) % 2 == 0 else 'B'  # Asignar colores alternados
        valor = x * 4 + y + 1
        casilla = Casilla(x, y, color, valor)
        tablero[x][y] = casilla

# Establecer vecinos para cada casilla (incluyendo movimientos diagonales)
for x in range(4):
    for y in range(4):
        casilla_actual = tablero[x][y]
        vecinos = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nuevo_x = x + dx
                nuevo_y = y + dy
                if 0 <= nuevo_x < 4 and 0 <= nuevo_y < 4 and (nuevo_x != x or nuevo_y != y):
                    vecinos.append(tablero[nuevo_x][nuevo_y])
        casilla_actual.vecinos = vecinos

# Ejemplo de uso
casilla_actual = tablero[1][1]
color_objetivo = 'R'  # Color al que quieres moverte
puede_moverse = casilla_actual.verificar_color_vecino(color_objetivo)
print(f"¿Puede moverse a un vecino de color {color_objetivo}? {puede_moverse}")
