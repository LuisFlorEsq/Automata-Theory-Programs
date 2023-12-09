'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Numeros primos contenidos en un rango
04/09/2023
n = 10 millones
'''

import time
import random
import math
import matplotlib.pyplot as plt
import os

filename = 'numeros_primos.txt'
filename_decimal = 'numeros_primos_decimal.txt'

filenamePlot = 'cantidad_unos.txt'


def find_prime_numbers(N, file_decimals):
    '''
    Function to find all the prime numbers smaller than an N value using
    the Sieve of Eratosthenes algorithm
    '''
    
    # We will eliminate all the numbers that can't be described as a prime number, 2 is the only pair prime number
    
    primes = [True for i in range(N+1)] # First we initialize a list of all possible prime numbers
    primes_bin = []
    
    test = 2 
    
    while(test * test <= N):
        
        if(primes[test] == True):
            
            # Let's find all the multiples of test, lower than N
            for i in range(test * test, N+1, test): # Here we use the range method with the following parameters: (start, stop, step) each of them has the following req. (optional, required, optional)
                primes[i] = False
        
        test += 1 # We check for each number lower than N
        
    # Next we have to convert each of the prime numbers to binary format and save them into a file
    
    save_decimal_prime(filename_decimal, "Σ = {")
    
    for i in range(2, N+1):
         if primes[i]:
            save_decimal_prime(file_decimals, str(i) + ",")
            primes_bin.append(bin(i)[2:])
             #primes_bin.append(decimal_to_binary(i))

    save_decimal_prime(filename_decimal, "}")
    
    return primes_bin


def save_decimal_prime(filename, prime_number):
    
    '''
    In order to save resources we create a function to save each prime number in decimal format into another file text.
    '''
    
    try:
        
        with open(filename, "a", encoding="utf-8") as f_obj:
            f_obj.write(prime_number + " ")
        
    except FileNotFoundError:
         print("We couldn't find the " + filename + " file, please try again.")

    
def decimal_to_binary(decimal_number):
    '''
    Function that ask for a decimal number and convert it to a binary number
    '''
    binary_number = 0
    key_value = 1
    
    while decimal_number != 0:
        # Save the module in the correct order
        binary_number = binary_number + decimal_number % 2 * key_value
        decimal_number //= 2
        key_value *= 10
        
    return str(binary_number)


def count_ones(binary_primes):
    return binary_primes.count("1")


def draw_plot(filenamePlot, primes_list):
    try:
        with open(filenamePlot, "w", encoding="utf-8") as f_obj:
            count = 1
            ones_primes = []
            for prime  in primes_list:
                ones_prime = count_ones(prime)
                ones_primes.append(ones_prime)
                f_obj.write(f"{count}\t{ones_prime}\n")
                count += 1
            f_obj.close()
            
            # Code to plot the number of ones in each prime number using plt
            
            plt.plot(ones_primes)
            plt.xlabel('No. String')
            plt.ylabel('Number of ones in each string')
            plt.title('Basic - Graphic')
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
            
            # If the file already exists, then delete it
            
            if os.path.exists(filename_decimal):
                os.remove(filename_decimal)
        
            
            N = input("\nEnter the value of N (this will be the range of numbers where the program have to find all the prime numbers), \n "
                    + "if you want to give a random number only press q and then the program will generate a random value for N:  ")
            if N == 'q' or N == 'Q':
                N = int(random.randrange(2, 100000))
                print("\nThe value of N selected for the system is: " + str(N) + ".\n")

            if int(N) < 1:
                print("\nN must be a positive value!\n")
                
            N = int(N)
            
            start_time = time.time()
            
            binary_primes = find_prime_numbers(N, filename_decimal) # We call the method to find all the prime numbers from 2 to N
            
            end_time = time.time()
            
            final_time = end_time - start_time
            
            print("\nThe execution time was: \n")
            print(float(final_time))
            
            # Save the binary prime_numbers to a text file
            try:
                with open(filename, "w", encoding="utf-8") as f_obj:
                    f_obj.write("Σ = { ")
                    f_obj.write("  ".join(binary_primes))
                    f_obj.write(" }")

                    
                print("\nThe prime numbers have been generated successfully.\n")
                f_obj.close()
                
                draw_plot(filenamePlot, binary_primes)
                
                
                print("Deleting the binary list...")
                binary_primes = []
                
                draw_plot_Log(filenamePlot)
                
                
            except FileNotFoundError:
                print("\nWe couldn't find the  " + filename + " file, please try again.\n")
                
        except ValueError as e:
            print(f"Error: {e}")
        
        # Ask the user to continue with another N
        choice = input("Do you want to enter a new value of N? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
        
 
        


if __name__ == '__main__':
    main()