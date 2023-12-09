# Jiménez Rodríguez José Alfredo
# 5BM1
# Práctica de Pila

import random
from Pila import Pila
import pygame as py

def Validar(Cadenas):
    with open("./CadenasA.txt","w",encoding="utf-8") as fileCadenasA,open("./CadenasR.txt","w",encoding="utf-8") as fileCadenasR:
        cont = 0
        pasos = []
        Cadena_Pasos = Cadenas

        py.init()
        
        surface = py.display.set_mode((400,300))   # Tamaño de ventana
        font = py.font.SysFont("Garamond", 15) # Tipo de fuente y tamaño
        pila_Text = font.render('x', False, (0, 0, 0))  # Texto dentro de pila
        number1_text = font.render('1', False, (255, 255, 255)) # Texto 1
        number0_text = font.render('0', False, (255, 255, 255)) # Texto 0
        numberE_text = font.render('E', False, (255, 255, 255)) # Texto ∈

        color = (255,255,255)   # Color de cuadrados
        erase = (0, 0, 0)
        space = 250     # Separación dinámica
    
        p = Pila()
        pasos.append(f'(q, {Cadenas}, z0)')
        Estado = 'q0'

        for caracter in Cadenas:
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()

            if Estado == 'q0' and caracter == '0':
                Estado = 'q1'
                p.include(0)
                cont += 1
                Cadena_Pasos = Cadena_Pasos[1:]
                pasos.append(f'(q, {Cadena_Pasos}, ' + cont*'x' + ')')

                # Draw in pila
                py.draw.rect(surface, color, py.Rect(175, space, 50, 30))
                surface.blit(number0_text, (230, space))
                surface.blit(pila_Text, (200, space))
                py.time.delay(1000)

            elif Estado == 'q0' and caracter == '1':
                print('La cadena no empieza con 0')
                fileCadenasR.write(f'{str(Cadenas)}\n')
                break
            elif Estado == 'q1' and caracter == '0':
                p.include(0)
                cont +=1
                Cadena_Pasos = Cadena_Pasos[1:]
                pasos.append(f'(q, {Cadena_Pasos}, ' + cont*'x' + ')')

                # Drawn in pila
                py.draw.rect(surface, color, py.Rect(175, space, 50, 30))
                surface.blit(number0_text, (230, space))
                surface.blit(pila_Text, (200, space))
                py.time.delay(1000)
                
            elif Estado == 'q1' and caracter == '1':
                Estado = 'q2'
                p.extract()
                cont -= 1
                space += 40
                Cadena_Pasos = Cadena_Pasos[1:]
                pasos.append(f'(p, {Cadena_Pasos}, ' + cont*'x' + ')')

                # Erase in pila
                py.draw.rect(surface, erase, py.Rect(175, space, 80, 30))
                surface.blit(number1_text, (230, space))
                py.time.delay(1000)

            elif Estado == 'q2' and caracter == '1':
                if cont != 0 and not p.isEmpty():
                    p.extract()
                    cont -= 1
                    Cadena_Pasos = Cadena_Pasos[1:]
                    if cont == 0:
                        pasos.append(f'(f, ∈, z0)')

                        # Erase in pila
                        surface.blit(numberE_text, (200, space+20))
                    else:
                        pasos.append(f'(p, {Cadena_Pasos}, ' + cont*'x' + ')')

                    # Erase in pila
                    py.draw.rect(surface, erase, py.Rect(175, space, 80, 30))
                    surface.blit(number1_text, (230, space))
                    py.time.delay(1000)
                else:
                    print('La pila ya está vacía, no puedes seguir desapilando.')
                    break
            elif Estado == 'q2' and caracter == '0':
                fileCadenasR.write(f'{str(Cadenas)}\n')
                print('La cadena no puede apilar de nuevo después de desapilar.')
                pasos.clear()
                break

            if caracter == '0':
                space -= 40
            elif caracter == '1':
                space += 40

            py.display.flip()
            
            fileCadenasA.write(f'{str(pasos)}\n')

def main():
    seguir = 's'
    while seguir == 's':

        print("Elija la opción que desea: ")
        print("1.- De forma automática")
        print("2.- De forma manual")
        opc = input()
        n = 0

        if opc == "1":
            n = random.randint(0, 100000)
            cadena = ''.join(random.choice('01') for _ in range(0, n))
        else:
            cadena = input("Ingrese la cadena: ")

        print(f"La cadena es {cadena}")
        Validar(cadena)


        #Graficar(n)

        seguir = input('¿Desea continuar? s/n: ')

if __name__ == "__main__":
    main()