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

filename = 'numeros_primos.txt'
filenamePlot = 'cantidad_unos.txt'


def find_prime_numbers(N):
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
        
    for i in range(2, N+1):
         if primes[i]:
             # primes_bin.append(bin(i)[2:])
             primes_bin.append(decimal_to_binary(i))
             
    return primes_bin

    
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


def main():
    try:
        N = input("\nEnter the value of N (this will be the range of numbers where the program have to find all the prime numbers), \n "
                  + "to give a random number only press q and the program will generate a random value for N:  ")
        if N == 'q' or N == 'Q':
            N = int(random.randrange(1, 100))
            print("\nThe value of N selected for the system is: " + str(N) + ".\n")

        if int(N) < 1:
            print("\nN must be a positive value!\n")
            
        N = int(N)
        
        start_time = time.time()
        
        binary_primes = find_prime_numbers(N) # We call the method to find all the prime numbers from 2 to N
        
        end_time = time.time()
        
        final_time = end_time - start_time
        
        print("\nThe execution time was: \n")
        print(float(final_time))
        
        # Save the binary prime_numbers to a text file
        try:
            with open(filename, "w", encoding="utf-8") as f_obj:
                f_obj.write("  ".join(binary_primes))
            print("\nThe prime numbers have been generated successfully.\n")
            f_obj.close()
            draw_plot(filenamePlot, binary_primes)
        except FileNotFoundError:
            print("\nWe couldn't find the  " + filename + " file, please try again.\n")
            
    except ValueError as e:
        print(f"Error: {e}")
 
        
def count_ones(binary_primes):
    return binary_primes.count("1")


def draw_plot(filenamePlot, primes_list):
    try:
        with open(filenamePlot, "w", encoding="utf-8") as f_obj:
            count = 1
            ones_primes = []
            for prime  in primes_list:
                ones_prime = count_ones(prime)
                ones_prime = math.log10(ones_prime)
                ones_primes.append(ones_prime)
                f_obj.write(f"{count}\t{ones_prime}\n")
                count += 1
            f_obj.close()
            
            # Code to plot the number of ones in each prime number using plt
            
            plt.plot(ones_primes)
            plt.ylabel('Number of ones in each prime number')
            plt.show()
    
    except FileNotFoundError:
        print("We couldn't find the " + filenamePlot + " file, please try again.")
    

if __name__ == '__main__':
    main()