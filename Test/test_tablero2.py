import random
import pygame
from time import sleep

class Ficha:
    def __init__(self, image):
        self.image = image

    def decoder(self, route, size):
        tabla_coordenadas = {
            'a': (1 * size, 1 * size), 'b': (2 * size, 1 * size), 'c': (3 * size, 1 * size), 'd': (4 * size, 1 * size),
            'e': (1 * size, 2 * size), 'f': (2 * size, 2 * size), 'g': (3 * size, 2 * size), 'h': (4 * size, 2 * size),
            'i': (1 * size, 3 * size), 'j': (2 * size, 3 * size), 'k': (3 * size, 3 * size), 'l': (4 * size, 3 * size),
            'm': (1 * size, 4 * size), 'n': (2 * size, 4 * size), 'o': (3 * size, 4 * size), 'p': (4 * size, 4 * size)
        }
        logic_route = [tabla_coordenadas.get(i) for i in route]
        self.route = logic_route
        
# A dictionary that contains the possible states that the chess piece can go to, depending on the current state and the instruction.
tabla_estados = {
    'a': {'W': 'be', 'R': 'f'},
    'b': {'W': 'eg', 'R': 'acf'},
    'c': {'W': 'bdg', 'R': 'fh'},
    'd': {'W': 'g', 'R': 'ch'},
    'e': {'W': 'bj', 'R': 'afi'},
    'f': {'W': 'ebjg', 'R': 'acik'},
    'g': {'W': 'bdjl', 'R': 'cfik'},
    'h': {'W': 'gdl', 'R': 'ck'},
    'i': {'W': 'ejm', 'R': 'gn'},
    'j': {'W': 'egmo', 'R': 'fikn'},
    'k': {'W': 'jglo', 'R': 'fhnp'},
    'l': {'W': 'go', 'R': 'hkp'},
    'm': {'W': 'j', 'R': 'in'},
    'n': {'W': 'mjo', 'R': 'ik'},
    'o': {'W': 'jl', 'R': 'nkp'},
    'p': {'W': 'ol', 'R': 'k'}
}

def recalculate(route_1, route_2, num_try, starter):
    try:
        for i in range(len(route_1)):
            if route_1[i] == route_2[i]:
                if num_try == 2:
                    if starter == 1:
                        route_2.insert(i, route_2[i - 1])
                    else:
                        route_1.insert(i, route_1[i - 1])
                    return False, route_1, route_2
                else:
                    return True, route_1, route_2
        return False, route_1, route_2
    except IndexError:
        return False, route_1, route_2

def rand_start():
    return 2 if random.randint(1, 10) % 2 == 0 else 1

def clean_routes(end, path):
    index = path.index(end)
    return path[:index + 1]

def routes(current, path):
    if not path:
        yield (current,)
        return
    first, *newpath = path
    for state in tabla_estados[current][first]:
        for route in routes(state, newpath):
            yield (current,) + route

def chess(path, inicio):
    with open("Practica5/all_routes" + inicio + ".txt", "w+") as all_routes:
        for i, W in enumerate(routes(inicio, path), 1):
            all_routes.write(''.join(W) + "\n")
        print("Rutas totales encontradas:", i)

def randomInst(num):
    return ''.join(random.choice("RW") for _ in range(num))

def best_routes(possible_routes, end):
    with open(possible_routes) as openfileobject:
        rank = []
        for line in openfileobject:
            if end in line:
                clean_line = clean_routes(end, line)
                rank.append(clean_line)
        clean_rank = list(dict.fromkeys(rank))
        rank_5 = sorted(clean_rank, key=lambda x: len(x))
        print("Rutas ganadoras encontradas:", len(rank))
        print("Mejores rutas:")
        print(rank_5[-5:])
        return rank_5[-5:]

if __name__ == "__main__":
    while True:
        try:
            aut = input("Todo automático? (Y/N): ").lower()
            if aut != "n":
                num_jugadores = rand_start()
                rute = randomInst(random.randint(1, 10))
            else:
                num_jugadores = int(input("Cuantos jugadores vas a usar? (1, 2): "))
                if num_jugadores < 1:
                    break
                if num_jugadores == 1:
                    rute = input("Ingrese la cadena a evaluar usando R y W (si quiere random ponga 0): ").upper()
                if num_jugadores == 2:
                    
                    rute = input("Ingrese la cadena a evaluar usando R y W (si quiere random ponga 0) para la primera ficha 'a': ").upper()
                    rute_2 = input("Ingrese la cadena a evaluar usando R y W (si quiere random ponga 0) para la segunda ficha 'd': ").upper()

                if rute == "0":
                    rute = randomInst(random.randint(1, 10))

                if len(rute) >= 50:
                    print("Error, más de 50 caracteres")
                    break

            print("Ruta a evaluar:", rute)
            print("Calculando rutas de ficha 1")
            chess(rute, 'a')
            routes_1 = best_routes("Practica5/all_routesa.txt", 'p')
            b_piece = Ficha('Practica5/B_piece.png')
            b_player = pygame.transform.scale(pygame.image.load(b_piece.image), [50, 50])

            if num_jugadores >= 2:
                print("Calculando rutas de ficha 2")
                chess(rute_2, 'd')
                routes_2 = best_routes("Practica5/all_routesd.txt", 'm')
                w_piece = Ficha('Practica5/W_piece.png')
                w_player = pygame.transform.scale(pygame.image.load(w_piece.image), [50, 50])

            try:
                if num_jugadores >= 2:
                    inicio = rand_start()
                    print("Inicia:", inicio)
                    accept, final_r1, final_r2 = recalculate(list(routes_1[0]), list(routes_2[0]), 1, inicio)
                    if accept:
                        if inicio == 1:
                            accept, final_r1, final_r2 = recalculate(list(routes_1[0]), list(routes_2[1]), 2, inicio)
                        else:
                            accept, final_r1, final_r2 = recalculate(list(routes_1[1]), list(routes_2[0]), 2, inicio)
                    r1 = ''.join(final_r1)
                    r2 = ''.join(final_r2)
                    print(r1)
                    print(r2)
                else:
                    r1 = routes_1[0]
                    print(r1)
                pygame.display.init()
                white, black = (245, 245, 220), (155, 155, 155)
                gameDisplay = pygame.display.set_mode((600, 600))
                pygame.display.set_caption("ChessBoard")
                size = 100
                boardLength = 4
                gameDisplay.fill(white)
                cnt = 0
                for i in range(1, boardLength + 1):
                    for z in range(1, boardLength + 1):
                        if cnt % 2 == 0:
                            pygame.draw.rect(gameDisplay, black, [size * z, size * i, size, size])
                        else:
                            pygame.draw.rect(gameDisplay, white, [size * z, size * i, size, size])
                        cnt += 1
                    cnt -= 1
                pygame.draw.rect(gameDisplay, black, [size, size, boardLength * size, boardLength * size], 1)
                gameDisplay.blit(b_player, [size, size])
                b_piece.decoder(r1, size)
                if num_jugadores >= 2:
                    gameDisplay.blit(w_player, [4 * size, size])
                    w_piece.decoder(r2, size)
                pygame.display.update()
                if num_jugadores >= 2:
                    if len(b_piece.route) > len(w_piece.route):
                        movements = len(w_piece.route)
                    else:
                        movements = len(b_piece.route)
                    try:
                        if inicio == 1:
                            for i in range(movements):
                                gameDisplay.blit(b_player, list(b_piece.route[i]))
                                pygame.display.update()
                                sleep(3)
                                gameDisplay.blit(w_player, list(w_piece.route[i]))
                                pygame.display.update()
                                sleep(3)
                        else:
                            for i in range(movements):
                                gameDisplay.blit(w_player, list(w_piece.route[i]))
                                pygame.display.update()
                                sleep(3)
                                gameDisplay.blit(b_player, list(b_piece.route[i]))
                                pygame.display.update()
                                sleep(3)
                        print("Terminó la partida")
                        sleep(10)
                        pygame.display.quit()
                    except IndexError:
                        print("Terminó la partida")
                        sleep(10)
                        pygame.display.quit()
                else:
                    for i in b_piece.route:
                        gameDisplay.blit(b_player, list(i))
                        pygame.display.update()
                        sleep(3)
                    print("Terminó la partida")
                    sleep(10)
                    pygame.display.quit()
            except IndexError:
                print("No hay rutas ganadoras para 1 o más jugadores")
            opc = input("Salir? (Y/N): ").lower()
            if opc != "n":
                print("\n¡Adiós!")
                pygame.display.quit()
                quit()
        except KeyboardInterrupt:
            print("\n¡Adiós!")
            pygame.display.quit()
            quit()
        except KeyError:
            print("La cadena tiene caracteres no válidos, favor de revisar")
        except ValueError:
            print("Valor incorrecto")