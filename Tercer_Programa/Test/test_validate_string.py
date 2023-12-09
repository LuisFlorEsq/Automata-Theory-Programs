
filename_str = 'all_strings.txt'
filename_valid = 'valid.txt'
filename_invalid = 'invalid.txt'

def validate_string(string_val, afd):
    '''Here we will validate if a string have reached one of the final states.'''
    
    # The final state is q0
    current_state = 'q0' # We begin in the initial state
    
    # We will iterate across all the string
    
    for element in string_val:
        # Here we first access to the first key which refers to the possible state, then we access to the next key in this case the key can take the '0' or '1' values
        current_state = afd[current_state][element] 
    
    # Finally, the current_state will be the "final state" of the string to evaluate so we have to check if this state is the AFD'S final state
         
    return afd[current_state].get('final', 'False') # If the method .get can't find the final key it will return False


def main():
    
     afd = {
        'q0': {'0': 'q1', '1':'q3', 'final': True}, # q0 is the final state
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q1'},
        'q3': {'0': 'q2', '1': 'q0'}
        
    }
     
     

if __name__ == "__main__":
    main()