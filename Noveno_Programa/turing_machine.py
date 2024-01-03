'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Programa Maquina de Turing
02/01/2024

El programa de la máquina de Turing debe de reconocer el lenguaje {0^n1^n | n>= 1}. La máquina de Turing se encuentra en el 
libro de John Hopcroft (ejercicio 8.2, segunda edición). La tabla de transiciones está adjunta en este mensaje.

Consideraciones a tener en cuenta para el desarrollo del programa:
1. El programa debe de recibir una cadena definida por el usuario o que sea determinada automáticamente por la máquina, una cadena de longitud como máximo de 1000 caracteres.
2. La salida del programa debe ser a un archivo de texto y utilizando descripciones instantáneas en cada paso de la computación.
3. Animar la máquina de Turing con cadenas menores iguales a 16 caracteres.
'''

# Import the necessary libraries

import random
import math
import time

# Text file to save the ID'S of the program

descriptions_file = 'descriptions.txt'



def turing_machine_menu():
    
    print("--------------------------------------")
    print("\nOptions\n")
    print("--------------------------------------")
    print("Select an option by entering a number:\n")
    print("1.-Enter a binary string")
    print("2.-Generate a random binary string")
    print("3.-Exit")
    

def validate_string_TM(string_input, descriptions_file):
    
    """
    Takes a string input and apply the logic of the Turing Machine to accept strings from the language {0^n1^n / n>=1}
    """
    
    # Create a dictionary to save the transitions defined from the TM
    
    transition_rules = {

        ('qo', '0'): ('qi', 'X', 'R'),
        ('qo', 'Y'): ('q3', 'Y', 'R'),
        
        ('qi', '0'): ('qi', '0', 'R'),
        ('qi', '1'): ('q2', 'Y', 'L'),
        ('qi', 'Y'): ('qi', 'Y', 'R'),

        ('q2', '0'): ('q2', '0', 'L'),
        ('q2', 'X'): ('qo', 'X', 'R'),
        ('q2', 'Y'): ('q2', 'Y', 'L'),

        ('q3', 'Y'): ('q3', 'Y', 'R'),
        ('q3', 'B'): ('q4', 'B', 'R')
        
    }
    
    try:
        
        with open(descriptions_file, 'w', encoding='utf-8') as f_obj:
            
            f_obj.write('Instantaneous Descriptions for the binary string: ' + string_input +  '\n')
            
    except FileNotFoundError:
        
        print("We couldn't find the " + descriptions_file + " file, please try again.")

    
    # Initialize some Turing Machine elements
    
    current_state = 'qo' # The initial state
    
    head_position = 0 # The head initially is on the left-most position
    
    valid = False
    
    # Convert the string into a list
    
    aux_string = list(string_input)
    
    current_symbol = aux_string[head_position]
    
    write_description(descriptions_file, head_position, aux_string, current_state)
        
    # Create a while cycle to iterate until the current state is 'q4'
    
    while current_state != 'q4':
        
        if head_position >= len(aux_string):
            
            aux_string.append('B')
            
        if head_position < 0:
            
            aux_string.insert(0, 'B')
        
        current_symbol = aux_string[head_position]
        print(current_symbol)
        transition_key = (current_state, current_symbol) # Create a key which contains the current_state and the symbol in the head_position
        print(transition_key)
        
        # Check that the transition_key is in the transition_rules dictionary
        
        if transition_key in transition_rules:
            
            next_state, write_symbol, move_direction = transition_rules[transition_key]
            
            # Change the symbol in the current head_position
            
            aux_string[head_position] = write_symbol
            
            # Update the head_position depending on the move_direction variable
            
            if move_direction == 'R':
                
                # Move the head_position to the right
                
                head_position +=1
                
            elif move_direction == 'L':
                
                # Move the head_position to the left
                
                head_position -= 1
                
            
            # Update the current_state
            
            current_state = next_state
            
            # Write the description on the text file
            print("Writing ID\n")
            
            write_description(descriptions_file, head_position, aux_string, current_state)
        
        else:
            
            valid = False
            return valid
            break
    
    # After the while cycle is ended change the valid variable to true
    
    valid = True
    
    return valid
    

def write_description(description_file, head_position, aux_string, current_state):
    
    """
    Write an Instantaneous Description on a text file
    """

    # Insert the current_state on the head_position
    
    aux_description = aux_string.copy()
    aux_description.insert(head_position, current_state)
    
    # Convert the aux_string to a string
    
    description = ''.join(aux_description)
    
    
    try:
        
        with open(description_file, 'a', encoding='utf-8') as f_obj:\
            
            if current_state != 'q4':
                
                f_obj.write(description + ' |- ')
            
            else:
                
                f_obj.write(description)
                
            
    except FileNotFoundError:
        
        print("We couldn't find the " + description_file + " file, please try again.")
    

def main():
    
    print("\nWelcome to the Turing Machine implementation!\n")
    print("This program was designed in order to accept the language of {0^n1^|n>=1}\n")
    
    exit = 0
    
    while exit != 3:
        
        turing_machine_menu()
        
        exit = int(input("Your choice in number: "))
        
        if exit == 1:
            
            print("-------------")
            print("\nTuring Machine - Manual")
            string_input = str(input("\nEnter a binary string: "))
            
            valid = validate_string_TM(string_input, descriptions_file)
            
            if valid:
                print("The binary string " + string_input + " is valid!")
            else:
                print("The binary string " + string_input + " is not valid!")

        elif exit == 2:
            
            print("-------------")
            print("\nTuring Machine - Random")                
            string_input = ''.join(random.choice('01') for _ in range(random.randint(1, 10)))
            
              
            valid = validate_string_TM(string_input, descriptions_file)
            
            if valid:
                print("The binary string " + string_input + " is valid!")
            else:
                print("The binary string " + string_input + " is not valid!")
            
        else:
            
            print("Please select a valid option.")         
        
    
    print("See ya!")
    
    return



# Execute the whole code

if __name__ == '__main__':
    
    main()