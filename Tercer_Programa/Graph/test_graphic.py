import turtle as t
from classes import state
from classes import transition
from classes import self_transition
from classes import special_transition    

def mover(x,y,c):
    if(c == 's'):
        t.up()
    t.goto(x,y)
    t.pendown()
    
    
def plot_protocol_afd():
    '''
    Draw the elements from the protocol afd.
    '''
    
    # Definicion de las posiciones para dibujar los circulos
    # -57 210
    # 80 210
    
    radius = 45
    
    protocol_states = [
        
        state(-57, 210, radius, 'Ready'),
        state(80, 210, radius, 'Sending')
    ]
    
    protocol_transitions = [
        
        transition(-200, 215, -110, 215, -250, 200, 'Start', 0),
        transition(-10, 215, 30, 215, 10, 220, 'Data', 0),
        self_transition(125, 225, 200, 260, 'Timeout', 30, 270),
        transition(80, 155, 80, 150, 80, 140, '', 90),
        special_transition(90, 5, 90, 380, -90, 40, -230, 130, '1')       
    ]
    
    # Draw each state from the protocol AFD
    
    for state_element in protocol_states:
        state_element.draw()
        
    # Draw each transition line from the decision AFD
    
    for transition_element in protocol_transitions:
        transition_element.draw()
        

    
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
        transition(-255, 55, 45, 55, -110, 60, '0', 0),
        transition(45, 25, -255, 25, -110, 0, '0', 180),
        transition(95, 5, 95, -120, 110, -58, '1', 90),
        transition(65, -120, 65, 5, 60, -58, '1', -90),
        transition(45, -150, -255, -150, -110, -140, '0', 180),
        transition(-255, -180, 45, -180, -110, -200, '0', 0),
        transition(-285, -120, -285, 5, -275, -55, '1', -90),
        transition(-315, 5, -315, -120, -335, -55, '1',  90),
        transition(-340, 45, -355, 45, -355, 45, '', 180),
        special_transition(180, 10, 90, 150, 90, 250, 0, 0, '') 

    ]
        
    # Draw each state from the decision AFD
    
    for state_element in decision_states:
        state_element.draw()
        
    # Draw each transition line from the decision AFD
    
    for transition_element in decision_transitions:
        transition_element.draw()
        
    t.exitonclick()
    
    

def main():
    #Graficar()
    
    # Create an instance for the window
    screen = t.Screen()
    
    # Change the window's title
    screen.title("Protocolo AFD")
    
    
    plot_protocol_afd()
    plot_decision_afd()
    
if __name__ == "__main__":
  main()