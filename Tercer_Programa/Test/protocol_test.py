'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Automata finito determinista - Protocolo
16/09/2023
100 mil cadenas de 64 bits
'''

import random
import execution_counter
import time

filename_str = 'all_strings.txt'
filename_valid = 'valid_strings.txt'
filename_invalid = 'invalid_strings.txt'

def on_off_protocol():
    '''
    Function that decides if the protocol is ready.
    0 off / 1 on.
    '''
    
    ready = random.choice(['0', '1'])
    
    return ready

def validate_string(string_val, afd):
    '''Here we will validate if a string have reached one of the final states.'''
    
    # The final state is q0
    current_state = 'q0' # We begin in the initial state
    
    # We will iterate across all the string
    
    for element in string_val:
        # Here we first access to the first key which refers to the possible state, then we access to the next key in this case the key can take the '0' or '1' values
        current_state = afd[current_state][element] 
    
    # Finally, the current_state will be the "final state" of the string to evaluate so we have to check if this state is the AFD'S final state
         
    return afd[current_state].get('final', False) # If the method .get can't find the final key it will return False
    

def generate_random_binary_string(n):
    '''Function to generate a random binary string with n len.'''
    
    return ''.join(random.choice('01') for _ in range(n))

def update_count():
    '''
    Update the execution_count.
    '''
    execution_counter.load_execution_count()
    execution_counter.execution_count += 1
    execution_counter.save_execution_count()
    
    count = execution_counter.execution_count
    
    return count
    
         
def write_string(filename_data, string_element):
    '''
    Function to save each string in the text file.
    '''         
    try:
        with open(filename_data, "a", encoding="utf-8") as f_obj:
            f_obj.write(f"{string_element}\n")
            f_obj.close()
            
    except FileNotFoundError:
        print("We couldn't find the " + filename_data + " file, please try again.")
    
           
def main():
    '''
    Here we will create all the logic code to run the program, but the most important part is to define the "AFD".
    '''
    
    # Define the afd as a dictionary where each state is the key value and then each entrance is the key for the next state
    
    afd = {
        'q0': {'0': 'q1', '1':'q3', 'final': True}, # q0 is the final state
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q1'},
        'q3': {'0': 'q2', '1': 'q0'}
        
    }
    
    # Initialize the ready variable in 1 to run the program at least 1 time
    
    ready = 1 # On_off protocol
    n = 100 # Number of strings
    m = 64 # Length of each string
    n_count = 0 # Execution count
    
     # Here we take note of the execution time to generate the binary strings
        
    start_time = time.time() 
    
    while ready == 1:
        
        
        for i in range(n):
            # Generate a random binary string and save it in the "filename_str" file
             string_element = generate_random_binary_string(m)
             write_string(filename_str, string_element)
             
             # Validate the generated string
             
             valid = validate_string(string_element, afd)
             
             if valid:
                 write_string(filename_valid, string_element)
             else:
                 write_string(filename_invalid, string_element)
                 
        # Since all the strings have been generated, we'll update the executions count
        n_count = update_count()
        str_count = "Iteracion: " + str(n_count)
        
        
        # Write the number of iteration in each text file
        write_string(filename_str, str_count)
        write_string(filename_valid, str_count)
        write_string(filename_invalid, str_count)

        time.sleep(3) # Wait for 3 seconds and then start to evaluate each string       
        
        data_strings = []
        
        ready = on_off_protocol()
        
    end_time = time.time()
    final_time = end_time - start_time
        
    print("\nThe execution time was: ")
    print(float(final_time))

        
        
          
if __name__ == "__main__":
    main()