'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Bakus-Naur Condicional IF
29/12/2023

Elaborar un programa que derive la gramática Backus-Naur que define el condicional IF.
Limite establecido para la generacion de derivaciones = 1000
La gramatica libre de contexto que define a la condicional IF esta descrita por:

1) S -> iCtSA
2) A -> ;eS ϵ  
'''

# Import the necessary libraries

import random
import math

# Text files where all the output from the program will be saved

derivations_file = 'derivations.txt'
pseudocode_file  = 'pseudocode.txt'


def bakus_naur_menu():
    
    print("--------------------------------------")
    print("\nOptions\n")
    print("--------------------------------------")
    print("Select an option by entering a number:\n")
    print("1.-Enter the number of IF's to reach")
    print("2.-Select randomly the number of IF's to reach")
    print("3.-Exit")
    

def generate_Grammar(if_number, derivations_file, pseudocode_file):
    
    
    """
    Generate the grammar for the BNF notation applying derivations on the variables (S,A)
    """
    
    # Since we are working with a Free Context Grammar we have a initial symbol in this case it will S
    
    start_symbol = 'S'
    
    variables = ['S', 'A']
    
    # Clear the text files before the derivation process
    
    with open(derivations_file, 'w', encoding='utf-8') as derivations_file_obj:
        derivations_file_obj.write('')
    with open(pseudocode_file, 'w', encoding='utf-8') as pseudocode_file_obj:
        pseudocode_file_obj.write('')
    
    
    # Obtain the first derivation from the start_symbol
    
    grammar = 'iCtSA'
    write_grammar(derivations_file, grammar)
    
    # With the first derivation we have at least one IF statement so let's create a count from 1 to the number of IF's
    
    count = 1
     
    # Generate derivations until the number of IF's are reached
    
    while count < if_number:
        
        # Decide from which variable perform the derivation
        
        variable = random.choice(variables)
        
        derivation = select_random_value(variable)
        
        # Perform the derivation over the grammar
        
        # Write the derivation in the file and check if the selected derivation is epsilon
        
        write_derivation(derivations_file, variable, derivation)
        derivation = epsilon_derivation(derivation)
        
        
        grammar = grammar.replace(variable, derivation, 1)
        
        if variable == 'S':
            
            count+=1
        
        # Write the current grammar in the text file

        write_grammar(derivations_file, grammar)
    
    # When the number of IF's is reached we have to deal with all the A variables and decide if they will be considered as ;eS or ϵ

    for character in grammar:
        
        if character == 'A':
            
            # Perform a derivation over the A's variables
            
            derivation = select_random_value(character)
            write_derivation(derivations_file, character, derivation)
            
            derivation = epsilon_derivation(derivation)
            grammar = grammar.replace(character, derivation, 1)
            
            # Write the derivations in the derivations file and then the current grammar
            
            write_grammar(derivations_file, grammar)
            
    # Convert the final grammar into pseudocode and save them into a text file
    
    generate_pseudocode(grammar, pseudocode_file)
            
            
    print("\nThe derivations have been generated!\n")
    print("\nOpen the derivations.txt and pseudocode.txt files to see the results")
        
    return grammar
            
def epsilon_derivation(selected_derivation):
    
    """
    When the selected derivation is 'epsilon' replace it with ""
    """
    
    
    # Verify if the selected derivation is epsilon
    
    if selected_derivation == 'ϵ':
            selected_derivation = ""
    
    return selected_derivation

def select_random_value(key):
    
    """
    Function to randomly select the derivation from the variables
    """
    
    derivations = {
        'S': '(iCtSA)',
        'A': [';eS', 'ϵ']
    }
    
    derivation = derivations[key]
    
    # In the case that the correspondent value is a list, choose a random element
    
    if isinstance(derivation, list):
        
        return random.choice(derivation)
    
    return derivation


def write_derivation(derivations_file, variable, derivation):
    
    """
    Write in the derivations file the variable selected and their derivation
    
    """
    
    try:
        
        with open(derivations_file, 'a+', encoding='utf-8') as file_obj:
            
            file_obj.write('Variable ' + str(variable) + '-> ' + str(derivation) + '\n')
            
    except FileNotFoundError:
        
        print("We couldn't find the " + derivations_file + " file, please try again.")
    

def write_grammar(derivations_file, current_grammar):
    
    
    """
    Write the whole grammar in the derivation file.
    """
    
    try:
        
        with open(derivations_file, 'a+', encoding='utf-8') as file_obj:
            
            file_obj.write(current_grammar + '\n')
            
    except FileNotFoundError:
        
        print("We couldn't find the " + derivations_file + " file, please try again.")
    
    

def generate_pseudocode(generated_grammar, pseudocode_file):
    
    """
    Takes the grammar generated from the derivations and convert it to the correspondient if statements
    """
    
    try:
        with open(pseudocode_file, "w", encoding="utf-8") as f_obj:

            # Create a dictionary with the pseudocode for each character
            statements = {
                'i': 'if ',
                'C': '(condition)',
                't': '{',
                'S': '<statement>;',
                ';': 'else', 
                'e': '{',  
                ')': '}'
            }
            
            count = 0
            previous_symbol = None
            flag = False
            
            for i, character in enumerate(generated_grammar):
                
                # Obtain the block of code for each character in the grammar
                
                if character != '(':
                    
                    selected_symbol = statements[character]
                        
                    if character == 'i':
                        
                        f_obj.write(count*'\t' + selected_symbol)
                        count+=1
                    
                    elif selected_symbol == '{':
                        
                        f_obj.write(selected_symbol + '\n')
                    
                    elif selected_symbol == '}':
                        
                        if previous_symbol == '<statement>;':
                            count -= 2
                            flag = True
                            # count += 1
                            
                        else:
                            count -= 1
                        
                        f_obj.write('\n' + count*'\t' + selected_symbol)

                        
                        
                    elif selected_symbol == '<statement>;':
                        
                        if flag:
                            count+=1
                            flag = False
                        f_obj.write(count*'\t' + selected_symbol + '\n')
                        aux = count-1
                        f_obj.write(aux*'\t' + '}')
                        
                    # Base case
                    else:
                        f_obj.write(selected_symbol)
                    
                    previous_symbol = selected_symbol        
                    
    except FileNotFoundError:
        
        print("We couldn't find the " + pseudocode_file + " file, please try again.")


def main():
    
    print("\nWelcome to the Bakus-Naur implementation for the IF statement!\n")
    print("This program was designed in order to generate random derivations until a number of IF statements is reached\n")
    
    exit = 0
    
    while exit != 3:
        
        bakus_naur_menu()
        
        exit = int(input("Your choice in number: "))
        
        if exit == 1:
            
            print("-------------")
            print("\nBakus Naur IF conditional - Manual")
            if_number = int(input("\nEnter the number of IF statements: "))
            
            grammar = generate_Grammar(if_number, derivations_file, pseudocode_file)
            
            print("The derivated grammar is: ")
            print(grammar)
            
        elif exit == 2:
            
            print("-------------")
            print("\nBakus Naur IF conditional - Random")                
            if_number = random.randint(0, 10)
            
            grammar = generate_Grammar(if_number, derivations_file, pseudocode_file)
            print("The derivated grammar is: ")
            print(grammar)
            
        else:
            
            print("Please select a valid option.")         
        
    
    print("See ya!")
    return



# Execute the whole code

if __name__ == '__main__':
    
    main()