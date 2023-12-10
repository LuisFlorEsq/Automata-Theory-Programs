'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
PushDown Automata
29/11/2023
    n < 15 Para el proceso de animacion
    Modulo para graficar la animacion del proceso de la pila para el PDA
'''

import random
import pygame as py


# Define the possible animations for the stack

# Push, Pop and isEmpty



def initialize_animation():
    
    """
    Initialize pygame and set the basic configuration
    """
    py.init()
    
    # Basic configuration
    surface = py.display.set_mode((500,500)) # Window size
    font = py.font.SysFont("Garamond", 15) # Type font and size font
    
    # Text configuration
    stack_Text = font.render('X', False, (0, 0, 0))
    number1_Text = font.render('1', False, (255, 255, 255))
    number0_Text = font.render('0', False, (255, 255, 255))
    numberE_Text = font.render('E', False, (255, 255, 255))
    stackZ0_Text = font.render('Z0', False, (0, 0, 0))
    
    color_init = (255, 255, 255)
    space_init = 330
    
    # Draw the first element of the stack
    py.draw.rect(surface, color_init, py.Rect(175, space_init, 50, 30))
    surface.blit(stackZ0_Text, (200, space_init))
    py.time.delay(1000)
    py.display.flip()
    
    

    return surface, font, stack_Text, number1_Text, number0_Text, numberE_Text
 
def push_animation(surface, color, space, number0_Text, stack_Text):
    
    """
    Generates a square with pygame to represent the push animation
    """
    
    # Draw a white rectangle on the window
    
    
    py.draw.rect(surface, color, py.Rect(175, space, 50, 30))
    surface.blit(number0_Text, (230, space))
    surface.blit(stack_Text, (200, space))
    py.time.delay(1000)
    py.display.flip()
    

# def state_animation(surface, color, coords, state_Text):
    
#     """
#     Generates a square with pygame to represent the current state
#     """
    
#     # Draw a white rectangle on the window
    
    
#     py.draw.rect(surface, color, py.Rect(175, space, 50, 30))
#     surface.blit(number0_Text, (230, space))
#     surface.blit(stack_Text, (200, space))
#     py.time.delay(1000)
#     py.display.flip()
    
    
    
def pop_animation(surface, color, space, number1_Text, first_call):
    
    """
    Remove a square with pygame to represent the pop animation
    
    """
    
    # Update the vertical component only on the first call
    if first_call:
        
        space += 40
    
    # Draw a black rectangle on the window
    py.draw.rect(surface, color, py.Rect(175, space, 80, 30)) # Draw a bigger rectangle in order to erase the zeros (width = 80)
    surface.blit(number1_Text, (230, space))
    py.time.delay(1000)
    py.display.flip()
    
    return space

    
    
# def main():
#     """
#     Function to test the animation elements 
#     """
    
    
#     # First we have to initialize all the basic components for the animation 
   
   
#     surface, font,  stack_Text, number1_Text, number0_Text, numberE_Text = initialize_animation()
    
#     # Define the color of the rectangles and the space between them
    
#     color = (255,255,255)   # Color de cuadrados
#     erase = (0, 0, 0)
#     space = 250   
    
    
#     for i in range(0, 3):
        
#         push_animation(surface, color, space, number0_Text, stack_Text)
        
#         space -= 40
    
#     space += 40
    
#     for i in range(0, 3):
        
#         pop_animation(surface, erase, space, number1_Text)
        
#         space += 40


# if __name__ == '__main__':
    
#     main()
    
    
