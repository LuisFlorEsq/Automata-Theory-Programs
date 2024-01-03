import random
import turtle
import time

def rectangle(t):
    for _ in range(4):
        t.forward(80)
        t.left(90)
    t.forward(80)

def writeall(letter, pos, t):
    t[0].up()
    t[1].down()
    t[0].forward(80*(pos))
    t[0].write(letter, font=("Arial", 12, "normal"))

    t[1].up()
    t[1].forward(80*(pos))
    t[1].down()
    t[1].left(-90)
    t[1].forward(100)
    t[1].stamp()
    t[1].forward(-100)
    t[1].left(90)

    t[2].up()
    t[2].setx(-533)
    t[2].forward(80*pos)

    if letter == 'B':
        rectangle(t[3])

    x, y = t[2].position()
    # Crear un fondo blanco estampando un cuadrado
    t[2].color("white")
    t[2].penup()
    t[2].goto(x - 10, y + 15)  # Ajustar según el tamaño del texto
    t[2].pendown()
    t[2].begin_fill()
    for _ in range(4):
        t[2].forward(20)  # Ajustar según el tamaño del texto
        t[2].right(90)
    t[2].end_fill()

    # Regresar a la posición original
    t[2].penup()
    t[2].goto(x, y)
    t[2].pendown()
    t[2].color('black')
    t[2].write(letter, font=("Arial", 12, "normal"))

    t[1].up()
    t[0].setx(-533)
    t[1].setx(-533)

    t[0].clear()
    t[1].clear()


        
def string(cadena, t):
    for i, letra in enumerate(cadena):
        t[0].write(letra, font=("Arial", 12, "normal"))
        t[0].forward(80)
        rectangle(t[1])

def TM(cadena,t):
    font = ("Arial", 12, "normal")
    if(len(cadena) <= 15):
        t[0].up()
        t[1].up()
        t[2].up()
        t[3].up()

        t[0].setx(-533)
        t[1].setx(-533)
        t[2].setx(-533)
        t[3].setx(-570)
        
        t[0].sety(200)
        t[1].sety(190)
        t[2].sety(17)
        t[3].sety(-20)
        
        t[0].down()
        t[1].down()
        t[3].down()
        
        string(cadena, t=[t[2], t[3]])

    cadena = list(cadena)
    pos = 0
    estado = 0
    while(True):
        if estado == 0 and cadena[pos] == '0':
            writeall('X', pos, t=[t[0], t[1], t[2], t[3]])
            cadena[pos] = 'X'
            pos += 1
            estado = 1
            if pos > len(cadena) - 1:
                cadena.append('B')          
            print(cadena)
            continue
        elif estado == 0 and cadena[pos] == 'Y':
            writeall('Y', pos, t=[t[0], t[1], t[2], t[3]])
            cadena[pos] = 'Y'
            pos += 1
            estado = 3
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 1 and cadena[pos] == '0':
            writeall('0', pos, t=[t[0], t[1], t[2], t[3]])
            pos += 1
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 1 and cadena[pos] == '1':
            writeall('Y', pos, t=[t[0], t[1], t[2], t[3]])
            estado = 2
            cadena[pos] = 'Y'
            pos -= 1
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 1 and cadena[pos] == 'Y':
            writeall('Y', pos, t=[t[0], t[1], t[2], t[3]])
            pos += 1
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 2 and cadena[pos] == '0':
            writeall('0', pos, t=[t[0], t[1], t[2], t[3]])
            pos -= 1
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 2 and cadena[pos] == 'X':
            writeall('X', pos, t=[t[0], t[1], t[2], t[3]])
            estado = 0
            pos += 1
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 2 and cadena[pos] == 'Y':
            writeall('Y', pos, t=[t[0], t[1], t[2], t[3]])
            pos -= 1
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 3 and cadena[pos] == 'Y':
            writeall('Y', pos, t=[t[0], t[1], t[2], t[3]])
            pos += 1
            if pos > len(cadena) - 1:
                cadena.append('B')
            print(cadena)
            continue
        elif estado == 3 and cadena[pos] == 'B':
            writeall('B', pos, t=[t[0], t[1], t[2], t[3]])
            estado = 4
            pos += 1 
            continue
        elif estado == 4:
            print('Cadena aceptada')
            break
        else:
            print('Cadena no aceptada')
            break
    time.sleep(5)
    t[0].clear()
    t[1].clear()
    t[2].clear()
    t[3].clear()

def main():
    t = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
    seguir = 's'
    while seguir == 's':

        print("Elija la opción que desea: ")
        print("1.- De forma automática")
        print("2.- De forma manual")
        opc = input()
        n = 0

        if opc == "1":
            n = random.randint(0, 15)
            cadena = ''.join(random.choice('01') for _ in range(0, n))
            print(f"La cadena es {cadena}")
            TM('01', t)
        elif opc == '2':
            cadena = input("Ingrese la cadena: ")
            print(f"La cadena es {cadena}")
            TM(cadena, t)
        else:
            print("Ingrese una opción válida.")

        seguir = input('¿Desea continuar? s/n: ')

if __name__ == '__main__':
    main()
    