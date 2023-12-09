'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Alfabeto binario
02/09/2023
n = 28 elementos del conjunto universo
'''

import time
import random
import matplotlib.pyplot as plt
import math


filename = 'alfabeto_binario.txt'
filenamePlot = 'cantidad_unos.txt'

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

def count_ones(binary_string):
    return binary_string.count("1")
    
        
def draw_plot(filenamePlot, strings_list):
    try:
        with open(filenamePlot, "w", encoding="utf-8") as file_obj:
            count = 1
            ones_strings = []
            for string in strings_list:
                ones_string = count_ones(string)
                ones_strings.append(ones_string)
                file_obj.write(f"{count}\t{ones_string}\n")
                count+=1
            # print("\nWe have finished to count the number of Ones in each string.\n")
            #file_obj.close()
            
            # Code to plot the number of ones in each string using plt
            
            plt.plot(ones_strings)
            plt.xlabel('No. String')
            plt.ylabel('Number of ones in each string')
            plt.title('Basic Graphic')
            plt.show()
    
    except FileNotFoundError:
        print("We couldn't find the " + filenamePlot + " file, please try again.")
        
        
def draw_plot_Log(filenamePlot):
    
    '''Function that reads a file and plot the data in batch in order to prevent memory error.'''
    
    batch_size = 6000000
    x_batch = []
    y_batch = []

    
    try:
        with open(filenamePlot, "r", encoding="utf-8") as f_obj:
            
            for line in f_obj:
                
                data = line.strip().split('\t')
                x = int(data[0])
                y = int(data[1])
                
                if y != 0:
                    new_y = math.log10(y)
                else:
                    new_y = 0
                x_batch.append(x)
                y_batch.append(new_y)
                
                
                # When we have reached the batch, draw the data and clean the lists
                if len(x_batch) == batch_size:
                    plt.plot(x_batch, y_batch)
                    x_batch = []
                    y_batch = []
                    
            # Draw the left data
            
            if x_batch:
                plt.plot(x_batch, y_batch)

            plt.xlabel('No. String')
            plt.ylabel('Number of ones in each string')
            plt.title('Graphic - log10')
            plt.show()
            f_obj.close()

                    
    except FileNotFoundError:
        print("We couldn't find the " + filenamePlot + " file, please try again.")
    

def main():
    
    while True:
        try:
            
            
            N = input("\nEnter the value of N (this will be the maximum length for Alphabet's strings), \nIf you don't want "
                        + "to give a number only press q and the program will generate a random value for N: ")
            if N == 'q' or N == 'Q':
                N = int(random.randrange(1, 8))
                print("\nThe value of N selected for the system is: " + str(N) + ".\n")

            
            if int(N) < 1:
                print("N must be a positive value!")
                
            N = int(N)
            
            # Here we take note of the execution time to generate the binary strings
            
            start_time = time.time() 
            
            binary_strings = generate_binary_strings(N) # We call the method to generate the binary strings
            
            end_time = time.time()
            
            final_time = end_time - start_time
            
            print("\nThe execution time was: ")
            print(float(final_time))

            # Save the binary strings to a text file
            try:
                with open(filename, "w", encoding="utf-8") as file_obj:
                    file_obj.write("Σ = { ")
                    file_obj.write(" ".join(binary_strings))
                    file_obj.write(" }")
                    
                print("\nThe alphabet has been generated successfully.\n")
                file_obj.close()
                
                draw_plot(filenamePlot, binary_strings) # Draw the number of ones in each string
                
                print("Deleting the binary list...")
                binary_strings = []
                
                draw_plot_Log(filenamePlot)
            except FileNotFoundError:
                print("We couldn't find the " + filename + " file, please try again.")
                
        except ValueError as e:
            print(f"Error: {e}")
            
        # Ask the user to continue with another N
        choice = input("Do you want to enter a new value of N? (yes/no): ").strip().lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()