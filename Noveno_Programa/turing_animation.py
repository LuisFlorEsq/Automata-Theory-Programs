'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Programa Maquina de Turing
02/01/2024
    n < 15 Condicion necesaria para llevar a cabo el proceso de animacion, donde n es la longitud de la cadena binaria
    Modulo para graficar la animacion del proceso de la Maquina de Turing
'''

# Import the necessary libraries

import tkinter as tk
import time

def animate_process(descriptions_file, canvas, main_window):
    """
    Animate the whole process of the Turning Machine
    """

    
    # Open the descriptions text file to animate the proccess
    
    try:
        
        with open(descriptions_file, "r", encoding='utf-8') as f_obj:
            
            descriptions_txt_lines = f_obj.readlines()
            
            descriptions_txt = descriptions_txt_lines[1]
            
            # Split the text to work without the '|-' symbol
            
            descriptions_list = descriptions_txt.split(' |- ')
            
            animate_step(descriptions_list, canvas, 0, main_window)
                                        
    except FileNotFoundError:
        
        print("We couldn't find the " + descriptions_file + " file, please try again.")


def animate_step(descriptions_list, canvas, index, main_window):
    
    """
    Animate each step from the Turing Machine process
    """
    
    if index < len(descriptions_list):
        
        description = descriptions_list[index]
        current_description = convert_description(description)
        # print(current_description)
        
        head_position = next((i for i, s in enumerate(current_description) if s.startswith('q')), None)
        current_state = current_description[head_position] if head_position is not None else ''
        current_text = "Current state: " + current_state

        # Update canvas
        draw_machine(current_description, head_position, canvas)
        draw_text(current_text, canvas)

        # Schedule the next update after a delay
        canvas.after(1000, animate_step, descriptions_list, canvas, index + 1, main_window)
    
    else:
        
        # When all the steps were animated, destroy the window
        
        main_window.destroy()
        
        

def draw_machine(current_description, head_position, canvas):
    """
    Draw the rectangles of the Turing Machine based on the current_description
    """
    
    canvas.delete('all')
    
    # Iterate over the current_description to create a square for each character
    
    for i, character in enumerate(current_description): 
        
        canvas.create_rectangle(100 + i * 50, 150, 150 + i * 50, 200, outline="black")
        canvas.create_text(125 + i * 50, 175, text=character, fill="black")
    
    # Mark the current head_position
    
    canvas.create_rectangle(100 + head_position * 50, 150, 150 + head_position * 50, 200, outline="red", width=3)


def draw_text(current_text, canvas):
    """
    Write text on the window to describe the current_state of the Turing Machine
    """
    
    canvas.create_text(400, 50, text=current_text, fill="black", font=('Helvetica', 14, 'bold'))


def convert_description(description):
    """
    Takes a description as string and split it into a list considering qo, qi, ... as a single element

    Args:
        description (_string_): String description in the descriptions_list
    """
    
    i = 0
    size_description = len(description)
    current_description = []
    
    while i < size_description:
        
        if description[i] == 'q':
            
            # Concatenate the next character
            
            current_description.append(description[i:i+2])
            i+=2
        else:
            
            current_description.append(description[i])
            i+=1
            
    
    return current_description