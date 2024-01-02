def generate_pseudocode(generated_grammar, pseudocode_file):
    """
    Takes the grammar generated from the derivations and converts it to the corresponding if statements
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

# Example usage
generated_grammar = "iCt(iCt(iCt(iCtS;eS));eS);eS"
pseudocode_file = "pseudocode.txt"
generate_pseudocode(generated_grammar, pseudocode_file)
    
    