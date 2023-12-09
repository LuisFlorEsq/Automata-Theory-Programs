'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Automata finito determinista - Protocolo
16/09/2023
100 mil cadenas de 64 bits
'''
import pickle

# Global variable to keep the count of runs

execution_count = 0

def load_execution_count():
    global execution_count
    try:
        with open('execution_count.pkl', 'rb') as f_obj:
            execution_count = pickle.load(f_obj)
    except FileNotFoundError:
        execution_count = 0

def save_execution_count():
    global execution_count
    with open('execution_count.pkl', 'wb') as f_obj:
        pickle.dump(execution_count, f_obj)