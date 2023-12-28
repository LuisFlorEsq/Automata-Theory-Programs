'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Palindromos
25/12/2023

Realizar un programa que construya palindromos de un lenguaje binario.
Longitud maxima  del palindromo = 10,000 caracteres
La gramatica libre de contexto que construye palindromos, se define con las siguientes reglas de produccion

1) P -> e
2) P -> 0
3) P -> 1
4) P -> 0P0
5) P -> 1P1
'''


# Import some libraries to work with


import random
import math


# Filaname to save the program's output

filename_Rules = 'selected_rules.txt'


def is_Odd(digits):
    
    """
    Determine if the number of digits of the palindrome is an even number or not.
    """
    
    flag = False
    
    if digits % 2 != 0: # Even number
        
        flag = True
        
    else:   # Odd number
        
        flag = False
        
    return flag  
    

def generate_Palindrome(palindrome_Digits):
    
    """
    Create a random binary palindrome based on the number of digits.
    """
    # First let's define the five rules that will generate every palindrome
    
    rules = {
        1: 'e',
        2: '0',
        3: '1',
        4: '0P0',
        5: '1P1',        
    }
    
    
    # In this case the start symbol will be P and all the derivations will be performed around it
    
    final_palindrome = ""
    palindrome_historial = []
    
    selected_rules = []
    
    
    recursive_rules = [4, 5]
    terminal_symbols = [2, 3]
    
    odd_palindrome = is_Odd(palindrome_Digits)
    
    
    if odd_palindrome:
        
        size = math.floor(palindrome_Digits / 2)
        
        selected_rules.extend([random.choice(recursive_rules) for _ in range (size)])
        selected_rules.append(random.choice(terminal_symbols)) # Since we are working with an Odd palindrome we have to select a terminal symbol
    
    else: 
        
        size = int(palindrome_Digits / 2)
        
        selected_rules.extend([random.choice(recursive_rules) for _ in range (size)])
        selected_rules.append(1) # Add the first production which declares that no symbols will be added
        
    
    # Change the selecte rules with the correct symbols from the rules dictionary
    
    
    for rule in selected_rules:
        
        production_value = rules[rule]
        final_palindrome = production_value if not final_palindrome else final_palindrome.replace("P", production_value, 1)
        palindrome_historial.append(f"Selected rule: {rule} -> {production_value},  Current palindrome: {final_palindrome}")
        
        
    # Once all the productions are validated we have to deal with the "e" production
    
    aux_palindrome = final_palindrome
    
    final_palindrome = aux_palindrome.replace('e', '')
    
    
    # Open the file_text and save the historial from palindrome historial

    write_historial(filename_Rules, palindrome_historial, final_palindrome)
    
    print("\nYour palindrome is: ", final_palindrome)
    print("\nThe palindrome was generated succesfully!")
     
    return final_palindrome



def palindrome_menu():
    
    print("--------------------------------------")
    print("\nOptions\n")
    print("--------------------------------------")
    print("Select an option by entering a number:\n")
    print("1.-Enter the number of digits of the palindrome")
    print("2.-Random number of digits for the palindrome")
    print("3.-Exit")
    
    
    
def write_historial(filename, historial, final_palindrome):
    
    """
    Write the historial of the rules selected on a text file
    """
    
    try:
        
        with open(filename, "w+", encoding="utf-8") as f_obj:
            
            f_obj.write("\n".join(historial))
            f_obj.write("\nThe final palindrome is: " + final_palindrome)
        
    except FileNotFoundError:
        
        print("We couldn't find the " + filename + " file, please try again.")
    


def main():
    
    print("\nWelcome to the Palindrome implementation!\n")
    print("This program was designed in order to generate random binary palindromes\n")
    
    exit = 0
    
    while exit != 3:
        
        palindrome_menu()
        
        exit = int(input("Your choice in number: "))
        
        if exit == 1:
            
            print("-------------")
            print("\nBinary palindrome - Manual")
            palindrome_digits = int(input("\nEnter the number of digits for the palindrome: "))
            
            generate_Palindrome(palindrome_digits)
            
        elif exit == 2:
            
            print("-------------")
            print("\nBinary palindrome - Random")                
            palindrome_digits = random.randint(0, 10)
            
            generate_Palindrome(palindrome_digits)
            
        else:
            
            print("Please select a valid option.")         
        
    
    print("See ya!")
    return




# Exectute the main method when the file is executed.

if __name__ == "__main__":
    
    main()