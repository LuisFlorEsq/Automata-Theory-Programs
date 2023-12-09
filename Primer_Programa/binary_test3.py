'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Alfabeto binario
02/09/2023

'''

filename = 'alfabeto_binario.txt'

def generate_binary_strings(N):
    ''' Function that generates binary strings and saves them into a list '''
    if N == 0:
        return ['']
    
    previous_strings = generate_binary_strings(N - 1)
    
    strings = ['']  # Initialize with epsilon
    
    for string in previous_strings:
        strings.append(string + '0')
        strings.append(string + '1')
    
    return strings

def main():
    try:
        N = int(input("Enter the value of N (this will be the maximum length for Alphabet's strings): "))
        if N < 1:
            print("N must be a positive value!")
        
        binary_strings = generate_binary_strings(N) # We call the method to generate the binary strings

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
