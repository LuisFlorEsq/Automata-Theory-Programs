import turtle as t
from classes import state
from classes import transition
    

def mover(x,y,c):
    if(c == 's'):
        t.up()
    t.goto(x,y)
    t.pendown()
    
    
    
def plot_decision_afd():
    '''
    Draw the elements from the decision afd.
    '''
    
    # Definicion de las posiciones para dibujar los circulos
    # 295,45 q0
    # 85, 45 q1
    # 85, -160 q2
    # -295, -160 q3
    
    radius = 45
    inner_radius = radius - 5
    
    decision_states = [
        
        state(-295, 45, radius, 'q0'),
        state(-295, 45, inner_radius, ''),
        state(85, 45, radius, 'q1'),
        state(85, -160, radius, 'q2'),
        state(-295, -160, radius, 'q3')
        
    ]
    
    
    decision_transitions = [
        
        # X = q_initial.x +- 40; Y = q_initial +- 40
        # X = q_initial.x +- 10; Y = q_initial +- 10
        transition(-255, 55, 45, 55, -110, 60, '0'),
        transition(45, 25, -255, 25, -110, 0, '0'),
        transition(95, 5, 95, -120, 100, -58, '1'),
        transition(75, -120, 75, 5, 80, -58, '1')

    ]
    
    # Draw each state from the decision AFD
    
    for state_element in decision_states:
        state_element.draw()
        
    # Draw each transition line from the decision AFD
    
    for transition_element in decision_transitions:
        transition_element.draw()
        
    t.exitonclick()
    
    
def plot_protocol_afd():
    '''
    Draw the elements from the protocol afd.
    '''
    
    return
    
    
    

def Graficar():
    font_size = 16
    radio = 45
    radio1 = 40
    Letra = ('Times New Roman', font_size,'bold')
    t.title('Autómata')
    
    mover(-250,200,'s')
    t.write('Start',align='center',font=Letra)
    
    mover(-200, 215,'s')
    mover(-110,215,'')
    t.stamp()
    
    mover(-57,170,'s')
    t.circle(radio)
    mover(-57,200,'s')
    t.write('Ready',align='center',font=Letra)
    
    mover(-10,215,'s')
    mover(30,215,'')
    t.stamp()
    
    mover(10,220,'s')
    t.write('Data',align='center',font=Letra)
    
    mover(80,170,'s')
    t.circle(radio)
    mover(80,200,'s')
    t.write('Sending',align='center',font=Letra)
    
    mover(125,225,'s')
    t.circle(30,extent=270)
    t.stamp()
    mover(200,260,'s')
    t.write('Timeout',align='center',font=Letra)
    
    # Linea para conectar el primer automata con el segundo
    mover(80,155,'s')
    mover(80,140,'')
    mover(-250,140,'')
    mover(-250,100,'')
    t.stamp()
    
    
    mover(-295,45,'s') # Posicionar el cursor en estas coordenadas
    t.circle(radio) # Dibujar el ciruclo 
    mover(-290,45,'s') # Moverse a esta coordenada para dibujar el circulo pequeno
    t.circle(radio1) # Dibujar el circulo pequeno 
    mover(-250,35,'s') # Moverse a estas coordenadas para escribir el texto
    t.write('q0',align='center',font=Letra) # Escribir el texto
    
    mover(-190,55,'s') # Posicionar el cursor en estas coordenadas
    mover(65,55,'') # Mover la flecha hasta esta coordenada dibujando el recorrido
    t.stamp() # Crear una copia de la flecha en el ultimo lugar
    mover(-57,60,'s') # Moverse a esta coordenada
    t.write('0',align='center',font=Letra) # Escribir el texto de la  linea
    
    mover(85,45,'s') # Mover para dibujar el circulo
    t.circle(radio) # Dibujar circulo
    mover(125,35,'s') # Mover para texto
    t.write('q1',align='center',font=Letra) # Escribir el texto
    
    mover(65,35,'s')
    mover(-190,35,'')
    t.stamp()
    mover(-57,10,'s')
    t.write('0',align='center',font=Letra)
    
    mover(-260,-10,'s')
    mover(-260,-100,'')
    t.stamp()
    mover(-240,-100,'s')
    mover(-240,-10,'')
    t.stamp()
    mover(-275,-50,'s')
    t.write('1',align='center',font=Letra)
    mover(-225,-50,'s')
    t.write('1',align='center',font=Letra)
    
    mover(-295,-160,'s')
    t.circle(radio)
    mover(-250,-175,'s')
    t.write('q2',align='center',font=Letra)
    
    mover(-190,-160,'s')
    mover(65,-160,'')
    t.stamp()
    mover(65,-180,'s')
    mover(-190,-180,'')
    t.stamp()
    
    mover(85,-160,'s')
    t.circle(radio)
    mover(125,-175,'s')
    t.write('q3',align='center',font=Letra)
    
    mover(-57,-155,'s')
    t.write('0',align='center',font=Letra)
    mover(-57,-215,'s')
    t.write('0',align='center',font=Letra)
    mover(115,-10,'s')
    mover(115,-100,'')
    t.stamp()
    mover(135,-100,'s')
    mover(135,-10,'')
    t.stamp()
    mover(100,-50,'s')
    t.write('1',align='center',font=Letra)
    mover(145,-50,'s')
    t.write('1',align='center',font=Letra)
    mover(900,900,'s')
    t.exitonclick()
    

def main():
    #Graficar()
    # plot_decision_afd()
    import turtle as t

# Configura la tortuga
t.speed(1)  # Velocidad baja para visualización

# Dibuja una flecha hacia abajo
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)

# Dibuja la parte izquierda de la flecha
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)

# Dibuja la parte inferior de la flecha
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)

# Cierra la ventana al hacer clic
t.exitonclick()
    
if __name__ == "__main__":
  main()