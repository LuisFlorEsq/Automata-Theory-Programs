'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Alfabeto binario
02/09/2023

'''

import time

filename = 'alfabeto_binario.txt'

def generate_binary_strings(N):
    ''' Function that generates binary strings and saves them into a list '''
    strings = []
    for i in range(N + 1):
        if i == 0:
            strings.append('ϵ')  # For N=0, add epsilon
        else:
            for j in range(2 ** i):
                binary_str = bin(j)[2:].zfill(i)  # Generate binary strings of length i
                strings.append(binary_str)
    
    return strings

def main():
    try:
        N = int(input("Enter the value of N (this will be the maximum length for Alphabet's strings): "))
        if N < 0:
            print("N must be a non-negative value!")
        
        start_time = time.time() 
         
        binary_strings = generate_binary_strings(N) # We call the method to generate the binary strings
        
        end_time = time.time()
        
        final_time = end_time - start_time
        
        print(final_time)

        # Save the binary strings to a text file
        try:
            with open(filename, "w", encoding="utf-8") as file_obj:
                file_obj.write("  ".join(binary_strings))
            print("The alphabet has been generated successfully.")
        except FileNotFoundError:
            print("We couldn't find the " + filename + " file, please try again.")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
