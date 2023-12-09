'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
PushDown Automata
20/11/2023
Codificar el automata de pila para identificar las cadenas binarias pertenecientes al lenguaje {0^n 1^n | n>=1}
    Convenciones a tener en cuenta:
        El proceso de la pila debe de ser animado cuando n < 20
        n tiene un valor máximo de 100,000
'''

# Import stack class from 'stack.py' file and another libraries

from stack import Stack
from pushdown_animation import initialize_animation, push_animation, pop_animation
import random

filename_ID = 'Descriptions.txt'



def actions_PDA(string, animate, filename_ID):
    """
    Function that describes the general logic to implement the PDA which accepts {0^n 1^n | n>=1}
    Args:
        string (_string_): _The string which will be evaluated_
        animate (_boolean_): _True or False, determine if the program will animate the process_
        filename_ID (_path_): _The path which will contain the ID's for the PDA_ 
    """

    # Define the PDA logic as a dictionary:
    # The first key will be the state
    # The second key will be the symbol read from the input
    # The values will represent the stack symbol
    
    
    try:
        
        with open(filename_ID, "w", encoding="utf-8") as f_obj:
            f_obj.write('The string is: ' + string + '\n')
        
    except FileNotFoundError:
        
         print("We couldn't find the " + filename_ID + " file, please try again.")
    
    
    # Some necessary variables    
    
    pda = {
        
        'q': {'0': 'q', '1': 'p'},
        'p': {'1': 'p', ' ': 'f'}
        
    }
    
    valid_string = False
    
    valid_string = validate_string_PDA(string, pda, animate)
    
    if (valid_string):
        print("The string " + string + " is valid")
    else:
        print("The string " + string + " is not valid")
        
        
   
    
    
def validate_string_PDA(string_validate, PDA, animate):
    """
    Function that implements the PDA logic to determine if the string is valid.

    Args:
        string (_String_): _String to evaluate_
        PDA (_dictionary_): _Dictionary which includes the transition rules_
    """
    
    stack = Stack()
    i = 0
    start_pop = True
    
    if animate:
        
        # First we have to initialize all the basic components for the animation 
   
   
        surface, font,  stack_Text, number1_Text, number0_Text, numberE_Text = initialize_animation()
           
        color_0 = (255,255,255)   # Rectangles color
        color_1 = (0, 0, 0)
        space = 210   

    # First we have to check if the string begins with '0'
    
    start = string_validate[0]
    
    # We will need an auxiliary string variable
    
    aux_string = string_validate + " "
    original_string = string_validate
    
    if start == '1':
        
        return False
    
    elif start == '0':
        
        current_state = 'q'
        
        
        
        for element in aux_string:
            
            print("Remaining string: " + string_validate)
            
            current_state = PDA[current_state][element]
            print(current_state)
        
            if current_state == 'q':
                stack.push('X')
                
                if animate: 
                    # Animation process
                    push_animation(surface, color_0, space, number0_Text, stack_Text)
                    space -= 40 # Update the vertical component
                
                # Consume one character from the original string
                i += 1
                string_validate = original_string[i:]
                
                    
            elif current_state == 'p':
                print(stack.peek())
                if stack.peek() == 'X':
                    stack.pop()
                    
                    if animate:
                        # Animation process
                        space = pop_animation(surface, color_1, space, number1_Text, start_pop)
                        space += 40 # Update the vertical component
                        start_pop = False
                    
                    i += 1
                    string_validate = original_string[i:]
                    
                    
                
            elif current_state == 'f':
                
                # Check if the stack is empty and the string was consumed
                
                string_remain = len(string_validate)
                
                if stack.is_empty() and string_remain == 0:
                    #print("The string " + aux_string + "is valid")
                    return True
                else:
                    #print("The string " + aux_string + "is invalid")
                    return False
           


def menu_pushdown_automata():
    
        print("--------------------------------------")
        print("\nOptions\n")
        print("--------------------------------------")
        print("Select an option by entering a number:\n")
        print("1.-Enter a string")
        print("2.-Random string")
        print("3.-Exit")
        
        
def main():
    
    
    print("\nWelcome to the PushDown Automata implementation!\n")
    print("This PDA is designed to accept the {0^n 1^n | n>=1} strings\n")
    
    exit = 0
    animate = False
    
    while exit != 3:
        
        menu_pushdown_automata()
        
        exit = int(input("Your choice in number: "))
        
        if exit == 1:
            
            binary_string = str(input("\nEnter a binary string: "))
                       
            # Calculate the binary string len, then decide if show the animation
            # Animation n < 15
            
            len_string = len(binary_string)
            
            if len_string < 15:
                
                animate = True
            
                actions_PDA(binary_string, animate, filename_ID)
            
        elif exit == 2:
            
            print("Random String")
            
        else:
            
            print("Please select a valid option.")         
        
    
    print("See ya!")
        
    
    
    
    
# Exectute the main method when the file is executed.

if __name__ == "__main__":
    
    main()