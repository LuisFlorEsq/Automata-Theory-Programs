'''
Flores Esquivel Luis Antonio
Teoria de la Computacion 5BM1
Automata finito no determinista - Tablero
30/09/2023
'''

class Square:
    
    def __init__(self, x_square, y_square, colour, value):
        
        self.x_sq = x_square
        self.y_sq = y_square
        self.colour = colour
        self.value = value
        self.neighbors = []
        
        
    def add_neighbor(self, neighbor):
        
        self.neighbors.append(neighbor)
        
    def possible_neighbors(self, next_colour):
        
        neighbors_moves = []
        
        for neighbor in self.neighbors:
            
            if neighbor.colour == next_colour: # Check if we can move to the neighbour
                
                neighbors_moves.append(neighbor)
        
        return neighbors_moves
        